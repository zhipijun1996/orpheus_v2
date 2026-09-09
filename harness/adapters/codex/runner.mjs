#!/usr/bin/env node
import { Codex } from "@openai/codex-sdk";
import { parse as parseYaml } from "yaml";
import { execFileSync } from "node:child_process";
import { existsSync } from "node:fs";
import { mkdir, readFile, writeFile, mkdtemp } from "node:fs/promises";
import { tmpdir } from "node:os";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, "../../..");

function argsOf(argv) {
  const out = {};
  for (let i = 0; i < argv.length; i += 1) {
    const a = argv[i];
    if (!a.startsWith("--")) continue;
    const key = a.slice(2).replaceAll("-", "_");
    const next = argv[i + 1];
    if (next && !next.startsWith("--")) {
      out[key] = next;
      i += 1;
    } else {
      out[key] = true;
    }
  }
  return out;
}

const cli = argsOf(process.argv.slice(2));
const task = cli.task;
const target = cli.target;
const goal = cli.goal;
const inferredMode = /(?:ROUTE|STORY)_ENGINE/i.test(String(task || "")) ? "ROUTE_ENGINE" : "GENERAL";
const mode = cli.mode || inferredMode;
const forgeWorkers = Number(cli.forge_workers || 0) || undefined;
const cliSeedPolicy = String(cli.seed_policy || "").toLowerCase();
const fixedSeedIds = String(cli.seed_ids || "")
  .split(",")
  .map((s) => s.trim())
  .filter(Boolean);
const includeMetaSeeds = Boolean(cli.include_meta_seeds) || target === "ROUTE_NULL";

if (!task || !target || !goal) {
  console.error("Usage: npm run sprint -- --task <TASK_ID> --target <REGISTRY_ID> --goal <text> [--mode MODE] [--forge-workers N] [--seed-policy controlled|random|off] [--seed-ids ID1,ID2]");
  process.exit(2);
}

const roles = JSON.parse(await readFile(path.join(here, "roles.json"), "utf8"));
const pipeline = await readFile(path.join(root, "harness/03_PIPELINE.md"), "utf8");

function pythonCommand() {
  const candidates = process.platform === "win32" ? ["python", "py"] : ["python3", "python"];
  for (const exe of candidates) {
    try {
      execFileSync(exe, ["--version"], { stdio: "ignore" });
      return exe;
    } catch {}
  }
  throw new Error("Python was not found; Context Pack generation requires Python.");
}

const packText = execFileSync(
  pythonCommand(),
  ["tools/build_context_pack.py", target, task, mode],
  { cwd: root, encoding: "utf8" },
);
await writeFile(path.join(root, "runtime/CONTEXT_PACK.yaml"), packText, "utf8");
const pack = parseYaml(packText);

const sourceFiles = [];
for (const entry of pack.files || []) {
  const abs = path.join(root, entry.path);
  sourceFiles.push({
    id: entry.id,
    path: entry.path,
    text: await readFile(abs, "utf8"),
  });
}

function matches(id, pattern) {
  if (pattern === "*") return true;
  if (pattern.endsWith("*")) return id.startsWith(pattern.slice(0, -1));
  return id === pattern;
}

function contextFor(roleName) {
  const patterns = roles[roleName].context_ids || [];
  return sourceFiles
    .filter((f) => patterns.some((p) => matches(f.id, p)))
    .map((f) => `\n## ${f.id} — ${f.path}\n${f.text}`)
    .join("\n");
}

const safeTask = String(task).replace(/[^A-Za-z0-9._-]+/g, "_");
const stamp = new Date().toISOString().replace(/[:.]/g, "-");
const runId = `${stamp}_${safeTask}`;
const runDir = path.join(root, "runtime/FRESH_SESSIONS", runId);
await mkdir(path.join(runDir, "reviews"), { recursive: true });
const tempRoot = await mkdtemp(path.join(tmpdir(), "orpheus-harness-"));

const seedPoolPath = path.join(root, "project/ideas/creative_seeds.yaml");
let seedPool = { active_seeds: [], adversarial_probes: [] };
if (existsSync(seedPoolPath)) {
  seedPool = parseYaml(await readFile(seedPoolPath, "utf8")) || seedPool;
}

const activeSeeds = (seedPool.active_seeds || []).filter((s) => s.status === "ACTIVE");
const adversarialSeeds = (seedPool.adversarial_probes || []).map((s) => ({
  ...s,
  kind: "ADVERSARIAL",
  scope: "probe",
  status: "ACTIVE",
  normal_exposure: false,
}));
const seedById = new Map([...activeSeeds, ...adversarialSeeds].map((s) => [s.id, s]));

const defaultSeedPolicy = mode === "ROUTE_ENGINE" ? (roles.forge.seed_policy || "controlled") : "off";
let seedPolicy = fixedSeedIds.length ? "fixed" : (cliSeedPolicy || defaultSeedPolicy);
if (!new Set(["controlled", "random", "off", "fixed"]).has(seedPolicy)) {
  throw new Error(`Unknown seed policy: ${seedPolicy}`);
}

function hashInt(text) {
  let h = 2166136261;
  for (const ch of String(text)) {
    h ^= ch.charCodeAt(0);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}

function shuffled(items) {
  const out = [...items];
  for (let i = out.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [out[i], out[j]] = [out[j], out[i]];
  }
  return out;
}

function controlledOrder(items, key) {
  return [...items].sort((a, b) => hashInt(`${key}:${a.id}`) - hashInt(`${key}:${b.id}`));
}

function normalEligibleSeeds() {
  if (fixedSeedIds.length) {
    const missing = fixedSeedIds.filter((id) => !seedById.has(id));
    if (missing.length) throw new Error(`Unknown fixed seed ids: ${missing.join(", ")}`);
    return fixedSeedIds.map((id) => seedById.get(id));
  }
  return activeSeeds.filter((s) => {
    if (includeMetaSeeds) return s.scope === "meta" || s.normal_exposure !== false;
    return s.scope !== "meta" && s.normal_exposure !== false;
  });
}

function nextDifferentKind(ordered, start, usedKinds = new Set()) {
  for (let offset = 0; offset < ordered.length; offset += 1) {
    const item = ordered[(start + offset) % ordered.length];
    if (!usedKinds.has(item.kind)) return item;
  }
  return ordered[start % ordered.length];
}

function buildForgeProfiles(workerCount) {
  const profiles = [{ exposure: "BLIND", seeds: [] }];
  if (workerCount <= 1) return profiles;
  if (seedPolicy === "off") {
    while (profiles.length < workerCount) profiles.push({ exposure: "BLIND", seeds: [] });
    return profiles;
  }

  const pool = normalEligibleSeeds();
  if (!pool.length) {
    while (profiles.length < workerCount) profiles.push({ exposure: "BLIND", seeds: [] });
    return profiles;
  }

  const ordered = seedPolicy === "random" ? shuffled(pool) : controlledOrder(pool, runId);
  const singleA = ordered[0];
  profiles.push({ exposure: "SEEDED_SINGLE", seeds: [singleA] });
  if (profiles.length >= workerCount) return profiles;

  if (workerCount === 3) {
    const first = ordered[1 % ordered.length];
    const second = nextDifferentKind(ordered, 2, new Set([first.kind]));
    profiles.push({ exposure: "SEEDED_FUSION", seeds: [first, second].filter(Boolean) });
    return profiles;
  }

  const singleB = nextDifferentKind(ordered, 1, new Set([singleA.kind]));
  profiles.push({ exposure: "SEEDED_SINGLE", seeds: [singleB].filter(Boolean) });
  if (profiles.length >= workerCount) return profiles;

  let cursor = 2;
  const fusionA = ordered[cursor % ordered.length];
  cursor += 1;
  const fusionB = nextDifferentKind(ordered, cursor, new Set([fusionA.kind]));
  profiles.push({ exposure: "SEEDED_FUSION", seeds: [fusionA, fusionB].filter(Boolean) });
  cursor += 1;

  while (profiles.length < workerCount) {
    if (profiles.length % 2 === 0) {
      profiles.push({ exposure: "SEEDED_SINGLE", seeds: [ordered[cursor % ordered.length]] });
      cursor += 1;
    } else {
      const a = ordered[cursor % ordered.length];
      cursor += 1;
      const b = nextDifferentKind(ordered, cursor, new Set([a.kind]));
      cursor += 1;
      profiles.push({ exposure: "SEEDED_FUSION", seeds: [a, b].filter(Boolean) });
    }
  }
  return profiles;
}

const codex = new Codex();
const sessions = [];

function envModel(roleName) {
  const key = `HARNESS_MODEL_${roleName.toUpperCase()}`;
  return process.env[key] || roles[roleName].model;
}

async function runFresh(roleName, label, artifactText = "", extraInstructions = "", metadata = {}) {
  const role = roles[roleName];
  const workingDirectory = path.join(tempRoot, label.replace(/[^A-Za-z0-9._-]+/g, "_"));
  await mkdir(workingDirectory, { recursive: true });

  const requestedModel = envModel(roleName);
  const prompt = `You are the ${roleName} role in an EXTERNAL FRESH CODEX SESSION created by the Narrative Harness.\n\nTask: ${task}\nMode: ${mode}\nTarget: ${target}\nGoal: ${goal}\n\nRole contract:\n${role.instruction}\n${extraInstructions ? `\nBatch-specific instructions:\n${extraInstructions}\n` : ""}\nExecution rules:\n- This is a new thread. Do not assume or reconstruct any parent conversation.\n- Use only the context embedded in this prompt and the frozen artifact below.\n- Treat Project Story Contract and Route Interface obligations as hard task architecture when present.\n- Do not browse the repository or archive.\n- Do not write files; return your result in the final response.\n- Be concise and evidence-based.\n\nHarness pipeline policy:\n${pipeline}\n\nAllowed context:${contextFor(roleName)}\n\nFrozen artifact, if any:\n${artifactText || "(none)"}`;

  const attempts = [requestedModel, null];
  let lastError;
  for (const model of attempts) {
    try {
      const thread = codex.startThread({
        workingDirectory,
        skipGitRepoCheck: true,
        sandboxMode: "read-only",
        model: model || undefined,
        modelReasoningEffort: role.reasoning_effort,
        networkAccessEnabled: false,
        webSearchMode: "disabled",
        approvalPolicy: "never",
      });
      const turn = await thread.run(prompt);
      const record = {
        role: roleName,
        label,
        thread_id: thread.id,
        requested_model: requestedModel,
        model_used: model || "runtime-default",
        reasoning_effort: role.reasoning_effort,
        independence: "FRESH_SESSION",
        parent_history_inherited: false,
        context_ids: sourceFiles
          .filter((f) => (role.context_ids || []).some((p) => matches(f.id, p)))
          .map((f) => f.id),
        usage: turn.usage,
        degraded_model: model === null,
        ...metadata,
      };
      sessions.push(record);
      return { text: turn.finalResponse, record };
    } catch (error) {
      lastError = error;
      if (model === null) break;
    }
  }
  throw lastError;
}

const workerCount = forgeWorkers || (mode === "ROUTE_ENGINE" ? roles.forge.route_engine_workers : roles.forge.workers) || 2;
const candidatesPerWorker = Number(roles.forge.candidates_per_worker || 2);
const forgeProfiles = buildForgeProfiles(workerCount);

function forgeBatchInstructions(profile) {
  const base = `Return exactly ${candidatesPerWorker} concise, structurally distinct candidate spines. Each must independently satisfy the hard task architecture; do not rank them.`;
  if (profile.exposure === "BLIND") {
    return `${base}\nIdea Seed exposure: NONE. You are the blind control. Do not infer an unseen seed pool or search for one.`;
  }
  const seedText = profile.seeds
    .map((s) => `- ${s.statement}`)
    .join("\n");
  return `${base}\nOptional Idea Seeds:\n${seedText}\nThese are provocations, not requirements. You may use, mutate, fuse, invert, or reject them. They carry no authority over Project State, Story Contract, Route Interface, or Canon. Do not mention seed IDs, seed provenance, or the fact that seeds were supplied in your output.`;
}

const forgeResults = await Promise.all(
  forgeProfiles.map((profile, i) => runFresh(
    "forge",
    `forge_${i + 1}`,
    "",
    forgeBatchInstructions(profile),
    {
      seed_exposure: profile.exposure,
      seed_ids: profile.seeds.map((s) => s.id),
    },
  )),
);

const seedProvenance = {
  run_id: runId,
  policy: seedPolicy,
  pool: "project/ideas/creative_seeds.yaml",
  blind_worker_required: true,
  reviewer_provenance_hidden: true,
  assignments: forgeProfiles.map((profile, i) => ({
    forge: i + 1,
    exposure: profile.exposure,
    seeds: profile.seeds.map((s) => ({ id: s.id, kind: s.kind, statement: s.statement })),
  })),
};
await writeFile(path.join(runDir, "SEED_PROVENANCE.json"), JSON.stringify(seedProvenance, null, 2), "utf8");

const frozenCandidates = forgeResults
  .map((r, i) => `# Forge ${i + 1}\n\n${r.text}`)
  .join("\n\n---\n\n");
await writeFile(path.join(runDir, "FROZEN_CANDIDATES.md"), frozenCandidates, "utf8");

const reviewNames = ["cold_reader", "drama_reviewer", "mystery_reviewer", "logic_scout"];
const reviewPairs = await Promise.all(
  reviewNames.map(async (name) => [name, await runFresh(name, name, frozenCandidates)]),
);

for (const [name, result] of reviewPairs) {
  await writeFile(path.join(runDir, "reviews", `${name}.md`), result.text, "utf8");
}

const frozenReviews = reviewPairs
  .map(([name, result]) => `# ${name}\n\n${result.text}`)
  .join("\n\n---\n\n");

const synthesisInput = `# Frozen candidates\n\n${frozenCandidates}\n\n# Frozen independent reviews\n\n${frozenReviews}`;
const synthesis = await runFresh("synthesizer", "synthesizer", synthesisInput);
await writeFile(path.join(runDir, "SYNTHESIS.md"), synthesis.text, "utf8");

const manifest = {
  run_id: runId,
  task,
  mode,
  target,
  goal,
  execution_mode: "FRESH_SESSION_SDK",
  context_pack: "runtime/CONTEXT_PACK.yaml",
  seed_policy: seedPolicy,
  seed_provenance: `runtime/FRESH_SESSIONS/${runId}/SEED_PROVENANCE.json`,
  sessions,
  artifacts: {
    candidates: `runtime/FRESH_SESSIONS/${runId}/FROZEN_CANDIDATES.md`,
    reviews: reviewNames.map((n) => `runtime/FRESH_SESSIONS/${runId}/reviews/${n}.md`),
    synthesis: `runtime/FRESH_SESSIONS/${runId}/SYNTHESIS.md`,
  },
  note: "Cognitive execution only. Seed provenance is intentionally withheld from Review/Synthesis and restored for the primary Orchestrator after convergence. The primary Orchestrator still owns Formal Sprint outputs and State writeback.",
};
await writeFile(path.join(runDir, "MANIFEST.json"), JSON.stringify(manifest, null, 2), "utf8");
await writeFile(path.join(root, "runtime/FRESH_SESSIONS/LATEST"), `${runId}\n`, "utf8");

console.log(JSON.stringify({
  status: "READY_FOR_ORCHESTRATOR",
  run_id: runId,
  run_dir: `runtime/FRESH_SESSIONS/${runId}`,
  forge_workers: workerCount,
  seed_policy: seedPolicy,
  synthesis: manifest.artifacts.synthesis,
  seed_provenance: manifest.seed_provenance,
  independent_reviews: reviewNames,
}, null, 2));
