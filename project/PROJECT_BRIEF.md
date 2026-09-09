# PROJECT BRIEF — 《奥菲斯计划：03:17》

## Product
- 科幻悬疑 ADV / Visual Novel
- Ren'Py 为目标引擎
- 高密度谜团 + 人物戏 + 多 Route 重读反转
- 首要目标是“故事成立且人物自然”，而不是技术设定堆叠

## Architecture
- 每条普通 Route 内部采用单一、自洽时间线。
- 不依赖平行世界之间的角色交互。
- 不同 Route 可以拥有彼此互斥的 Route Truth。
- Shared 层优先固定“玩家看见了什么”，而不是“这些现象唯一意味着什么”。
- 一条 Route 不需要解释所有 Project Truth；`truth != exposure`。
- Ch4 通常需要给出可信、可行动的 Working Truth。
- Ch5 通常需要产生足够大的 Deep Truth / Reveal Delta，而不是仅复演答案。
- NULL Meta Route 在普通 Route 足够成熟后再开发，不反向预设普通 Route 的答案。

## Current working Route IDs
- FLESH
- ECHO
- ORIGIN
- BLINDSPOT
- NOBODY
- NULL（Meta）

## Current development priority
1. 让普通 Route 的 Story Engine 各自成立。
2. 用 Route Interface 反复检查它们是否还能共享同一个 Ch2 观测层。
3. ORIGIN 仍是最大 Route Story Engine 缺口。
4. NOBODY 需要对共享 Ch2 的所有“疑似未来痕迹”完成本地因果账本。
5. BLINDSPOT 的物理机制已达 SOLVABLE，但后段人物代价/分叉仍需重构。
