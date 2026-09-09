#!/usr/bin/env node
import { Codex } from "@openai/codex-sdk";
import { parse as parseYaml } from "yaml";
import { execFileSync } from "node:child_process";
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

if (!task || !target || !goal) {
  console.error("Usage: npm run sprint -- --task <TASK_ID> --target <REGISTRY_ID> --goal <text> [--mode MODE] [--forge-workers N]");
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

const codex = new Codex();
const sessions = [];

function envModel(roleName) {
  const key = `HARNESS_MODEL_${roleName.toUpperCase()}`;
  return process.env[key] || roles[roleName].model;
}

async function runFresh(roleName, label, artifactText = "") {
  const role = roles[roleName];
  const workingDirectory = path.join(tempRoot, label.replace(/[^A-Za-z0-9._-]+/g, "_"));
  await mkdir(workingDirectory, { recursive: true });

  const requestedModel = envModel(roleName);
  const prompt = `You are the ${roleName} role in an EXTERNAL FRESH CODEX SESSION created by the Narrative Harness.\n\nTask: ${task}\nMode: ${mode}\nTarget: ${target}\nGoal: ${goal}\n\nRole contract:\n${role.instruction}\n\nExecution rules:\n- This is a new thread. Do not assume or reconstruct any parent conversation.\n- Use only the context embedded in this prompt and the frozen artifact below.\n- Treat Project Story Contract and Route Interface obligations as hard task architecture when present.\n- Do not browse the repository or archive.\n- Do not write files; return your result in the final response.\n- Be concise and evidence-based.\n\nHarness pipeline policy:\n${pipeline}\n\nAllowed context:${contextFor(roleName)}\n\nFrozen artifact, if any:\n${artifactText || "(none)"}`;

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

const workerCount = forgeWorkers || roles.forge.workers || 2;
const forgeResults = await Promise.all(
  Array.from({ length: workerCount }, (_, i) => runFresh("forge", `forge_${i + 1}`)),
);

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
  sessions,
  artifacts: {
    candidates: `runtime/FRESH_SESSIONS/${runId}/FROZEN_CANDIDATES.md`,
    reviews: reviewNames.map((n) => `runtime/FRESH_SESSIONS/${runId}/reviews/${n}.md`),
    synthesis: `runtime/FRESH_SESSIONS/${runId}/SYNTHESIS.md`,
  },
  note: "Cognitive execution only. The primary Orchestrator must still produce Formal Sprint outputs and apply State writeback.",
};
await writeFile(path.join(runDir, "MANIFEST.json"), JSON.stringify(manifest, null, 2), "utf8");
await writeFile(path.join(root, "runtime/FRESH_SESSIONS/LATEST"), `${runId}\n`, "utf8");

console.log(JSON.stringify({
  status: "READY_FOR_ORCHESTRATOR",
  run_id: runId,
  run_dir: `runtime/FRESH_SESSIONS/${runId}`,
  synthesis: manifest.artifacts.synthesis,
  independent_reviews: reviewNames,
}, null, 2));
