## HARNESS_CORE
# Core

1. **Story first** — prove the story is worth telling before proving full closure.
2. **Character causality** — major actions and reversals follow from established desire, knowledge, and consequential experience.
3. **One spine** — each candidate keeps one dominant causal Story Spine; synthesis favors depth and compression.
4. **Scoped truth** — truth is scoped as `shared / route / meta`, and Route truths may be mutually incompatible.
5. **Truth differs from exposure** — world logic may close while each Route reveals only what its drama requires.
6. **Current state is context** — active state drives work; process history serves provenance.
7. **Minimal context** — each task receives only the information required to perform that task.
8. **Shared-route co-evolution** — Routes explain current shared observations; strong Route ideas may propose minimal Shared deltas, accepted only through cross-route review.
9. **Human authority** — AI may advance candidates; aesthetic commitment, Route survival, architecture shifts, and `LOCKED` status remain Human decisions.



## PROJECT_BRIEF
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
- 普通Route的共享故事锚点与Ch2/Ch4/Ch5章节功能以 `project/state/STORY_CONTRACT.yaml` 为当前项目合同。
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



## AUTHOR_SHARED
# 01｜共同人工约束

version: 0.3
status: provisional_human
authority: 当前架构探索的人工作品前提

## 基本架构

[C01] 五条普通Route共享同一份Ch1与Ch2演出。

[C02] 每条普通Route内部采用单一、自洽的历史。

[C03] 不同Route可以对同一组共同观测给出互斥的底层真相。

[C04] Ch1以日常和关系戏建立程砚、林岚、周启明的亲近感与实验生活。

[C05] 2036年03:17发生奥菲斯重大实验事故，程砚在事故后持续追查真相并研究阿尔戈。

## Ch2共同演出

[C06] 程砚先观察到实验出现初始异常，随后观察到黑色NULL人物表象。

[C07] 程砚继续进入危险区域或实施救援时，被NULL阻断。

[C08] C07之后，NULL的一个动作使程砚离开直接危险位置。

[C09] 程砚因救援受阻而情绪崩溃，林岚接住并安抚他。

[C10] 林岚随后成为POV角色，并主动尝试完成一项事故现场操作。

[C11] 林岚视角中，NULL开枪击伤她的左肩或左上臂。

[C12] 枪击后切回程砚视角，程砚看见受伤的林岚并经历爆炸与昏厥。

[C13] Ch2只固定玩家实际经历的观测与顺序，底层身份、机制、动机和完整因果由Route解释。

## Ch3—Ch5共同功能

[C14] Ch3从林岚被枪击后的主观连续体验起步，她首先把眼前处境理解为事故附近的延续。

[C15] 林岚在Ch3中的身体来源、主体连续性、真实时间与真实地点由各Route解释。

[C16] Ch3需要产生一次关于“自己在哪里、现在是什么时候、眼前画面是什么”的认知翻转。

[C17] Ch4呈现程砚事故后多年的人生、研究与追查，并让孩童时期的程浠进入玩家视野。

[C18] Ch4包含程砚与林岚跨越多年后的重逢，核心情绪是熟悉、陌生与时间造成的距离同时存在。

[C19] Ch4允许程砚与林岚双视角，并形成对03:17的第一层可信解释与下一步行动目标。

[C20] Ch5进入或高强度重建2036事故因果，使Ch2已经看过的动作获得新的意义。

## 人物与叙事效果

[C21] 2036程砚、未来程砚、林岚、周启明、程浠的关键行动都由各自当时的经历、认知、欲望与关系推动。

[C22] 周启明在每条Route中拥有主动目标、关键决定与可见后果。

[C23] 每条Route都需要情绪起伏、真相差异、提前铺垫与可回看的伏笔。

[C24] 新增背景故事优先服务人物关系、动机与关键选择，并按其影响范围归入Shared或Route。

[C25] 架构探索先证明故事和人物值得继续开发，再补完整事故闭环、技术边界和证据链。

[C26] Shared演出的新增或微调以最小Delta提出，并经过人工确认与五Route兼容检查。



## AUTHOR_EXPERIENCE_MAP
# 07｜五Route体验地图

version: 0.3
status: provisional_human
purpose: 单Route作者只读取其他Route的体验目标，不读取其他Route完整解答。

[X01] FLESH把“独立未来身体真的回来”转化为主动成为NULL、救援与自我牺牲选择。
[X02] ECHO把“未来人格回返”转化为两具身体、四个主体之间的行动权与连续性问题。
[X03] ORIGIN把“事故后真实形成的父女关系”转化为女儿主动阻止父亲全救计划的黑暗因果。
[X04] BLINDSPOT把“历史中仍未被唯一确定的过程”转化为真实救援机会及其现实代价。
[X05] NOBODY把同一03:17完全落回2036本地人物与系统，并通过调查重新分配NULL行为的主体与责任。
[X06] 五条Route共享同一Ch2的核心观测，但Ch5需要让玩家获得明显不同的真相、人物判断与情绪余味。
[X07] 单Route初稿优先形成自己的情绪和因果身份，跨Route整合阶段再读取五条完整答案进行去重与兼容检查。



## AUTHOR_PREFLIGHT_PROTOCOL
# 09｜架构探索工作协议

version: 0.3
status: provisional_human

[P01] 架构探索先交一段可以直接阅读的故事，再交分析表。
[P02] 每个候选优先说明人物经历过什么、知道什么、想要什么、做了什么以及关系因此怎样变化。
[P03] 关键人物包括2036程砚、未来程砚、林岚、周启明与程浠，实际参与本线关键因果的人都需要自己的目标与行动。
[P04] 候选至少包含一次情绪上升或下降、一次关系变化，以及一个能让玩家重新理解Ch2的真相差异。
[P05] 候选需要给出2至4个可以提前放入Ch1—Ch4的铺垫或伏笔机会。
[P06] 新背景故事可以用于建立人物关系、研究经历、承诺、误解和长期动机。
[P07] 科幻机制优先创造人物选择、场景价值或同时解释多个既有现象。
[P08] 一个新规则若主要作用只是把人物推向唯一预设结果，应标记为当前架构弱点并优先寻找更自然的实现。
[P09] 尚未展开的年份、设备细节、证据链和局部操作可以标记为OPEN。
[P10] 已经出现的人物动机矛盾、POV冲突、同一身体位置冲突和因果互斥应标记为CONTRADICTION。
[P11] 架构探索阶段不以完整NULL字段、完整技术边界或完整证据表作为候选胜出的理由。
[P12] 综合稿改变关键动机、身份、因果动作或主要机制后，需要重新独立评审。
[P13] 没有值得继续开发的候选时允许NO_SELECTION，并把最关键的失败原因交给Human Gate。



## AUTHOR_BLINDSPOT
# 05｜BLINDSPOT 人工约束

version: 0.3
status: provisional_human

[B01] 本线的时间介入利用尚未被未来可靠、唯一确定的历史过程。
[B02] 已经被可靠确认的关键观测继续作为本线必须满足的历史锚点。
[B03] 两次有限干预与一次完整回返是当前工作结构。
[B04] 程砚与林岚先经历“越努力修正已知前因，结果越回到既有观测”的挫败。
[B05] 角色随后找到真正可行动的历史空白，并至少成功完成一次有意义的救援。
[B06] 成功救援带来一个具体、可见、由人物行动造成的现实代价。
[B07] 后段价值冲突来自角色对成功与代价的亲历。
[B08] 周启明在救援与后果中拥有主动目标、判断和行动，并参与后段价值分歧。
[B09] 林岚对自身人生、公开真相和继续干预拥有独立意见。
[B10] 本线的核心情绪是程砚终于找到能够救人的未知空间，同时理解使用这种空间会改变其他人的人生。
[B11] Ch5重新解释Ch2中“被看见、未被看见、后来被记录”的差别为何会改变行动可能。



## CHAR_CHENG
id: CHENG_YAN
name: 程砚
status: provisional
role: 男主 / 奥菲斯研究者
shared_facts:
- 2036与林岚、周启明共同参与奥菲斯实验。
- 03:17事故后长期追查事故并继续相关研究。
- 对林岚与周启明的失去具有强烈私人动机。
route_variable:
- 2054对阿尔戈的最终技术结论
- 是否以身体、人格、有限干预或完全本地推理方式参与2036真相
- 18年研究具体路径与代价
candidate_facts:
- 事故造成严重左臂损伤/后期机械臂意象是否全Route共享，待重新确认。



## CHAR_LIN
id: LIN_LAN
name: 林岚
status: provisional
role: 女主 / 奥菲斯研究者
shared_facts:
- 2036与程砚、周启明共同参与奥菲斯实验。
- 03:17现场遭受肩部相关伤害，并从年轻程砚之后的正常可确认生活中消失。
route_variable:
- 2054出现的林岚是否为身体连续、人格连续、本地重建或其它Route Truth。
- 生物学林岚在2036后的Route级命运。



## CHAR_ZHOU
id: ZHOU_QIMING
name: 周启明
status: provisional
role: 导师 / 奥菲斯实验负责人
shared_facts:
- 是程砚与林岚的导师/实验负责人。
- 事故最后阶段存在年轻程砚直接确认其仍在核心的候选Shared锚点。
route_variable:
- 03:17最后区间的实际行动与最终命运。
- 是否执行某些NULL动作。
- 不同Route中对未来干预/历史边界的理解。



## CHAR_DAUGHTER
id: DAUGHTER
name: 程浠
working_label: 养女
status: candidate
role: 程砚在03:17事故后的人生中形成的真实女儿关系
candidate_facts:
- 她与程砚形成真实父女关系，程砚不把她仅视作林岚替代品。
- 她与林岚具有相同/近似核DNA是高价值候选，但尚未提升为Shared硬事实。
open_dimensions:
- entry_timing_in_post_2036_life
- age_at_2054
- route_exposure
- biological_relation_meaning
- temporal_role

