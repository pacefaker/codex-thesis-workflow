# T-013C 定向降 AI 执行计划

## 摘要
- 本计划服务于 `T-013C`：在 `PLAN7.md` 已完成一轮克制降 AI 收口之后，对摘要、第1章、第2章、第3章少量边界段、第4章解释段与 `4.6`、第5章 `5.1 / 5.2` 执行一轮更定向的语言去公式化。
- 本轮目标不是重新起草章节，也不是开启新一轮全文重写，而是在不改事实、不改章节职责、不改结果强度的前提下，继续降低明显的模板化总结腔、空泛转承句和过整齐的 AI 总结节奏。
- 本轮主流程固定为 `$graduation-thesis-editor -> $humanizer`：先由 `$graduation-thesis-editor` 稳住逻辑、边界、论证节奏与论文语体，再由 `$humanizer` 对少量已稳定段落做 very light 去 AI 清理。
- 本轮默认不创建子智能体；原因固定为：修改集中在同一份正式稿与同一套 authority 上，目标是统一语气和手写感，主线程串行更稳。
- 本轮只处理语言风格和表达节奏，不替代 `PLAN7.md` 的模板 / 前置页 / 提交前核查主线。

## 计划定位
- 这是 `T-013` 下的一个“定向降 AI / 语言收口”专项计划，不是新一轮全文重写计划。
- 它默认继承：
  - `<your-thesis-repo>\文档\参考文献\写作计划\PLAN7.md`
  - `<your-thesis-repo>\thesis\paper-outline.md`
  - `<your-thesis-repo>\thesis\paper-evidence-map.md`
  - `<your-thesis-repo>\thesis\paper-writing-log.md`
- 它只处理语言风格和表达节奏，不重新决定章节职责、实验边界、数据集角色层级和结果强度。
- 当前正式稿入口固定为：
  - `<your-thesis-repo>\thesis\document.tex`
  - `<your-thesis-repo>\thesis\cover.tex`
- 本轮继续服从 `PLAN7.md` 已写死的总约束：
  - `Visium HD MouseBrain` 是唯一主实验线
  - `Human Ovarian` 只作 supporting dataset
  - 两个 Xenium 只作 workflow-support dataset
  - `EXP-007` 只能写成当前最强 candidate，不能写成已 promoted baseline

## 本轮范围
- 只处理以下高价值降 AI 区域：
  - 第1章：`1.1`、`1.2`、`1.3`、`1.4` 中的引入句、转承句、收束句
  - 第2章：`2.1` 到 `2.4` 的综述开头、结尾与承接句
  - 第3章：`3.1`、`3.3`、`3.4` 中的概念解释段、方法边界说明段、过渡句
  - 第4章：`4.2` 数据集角色说明段、`4.3` baseline 设计理由段、`4.5` 中结果解释与可视化讨论段、`4.6` 本章小结
  - 第5章：`5.1 全文总结`、`5.2 研究展望`
  - 摘要：中文摘要、英文摘要；关键词仅在中英不一致时微调
- 不启动：
  - 第1章到第5章的重写
  - 目录结构变更
  - 图表、参考文献或数据事实改写
  - 任意新实验结论、新数据集角色或更强结论表述
- 本轮语言收口只允许：
  - 去掉过强的模板化总结腔、空泛转承句、重复排比句
  - 弱化说明书腔 / 元话语腔
  - 优化句法组织、节奏与承接
- 本轮语言收口明确禁止：
  - 改研究背景事实、论文定位、章节分工与引用事实
  - 改技术分类框架、文献归纳逻辑、方法流程事实边界
  - 动第3章高技术密度主段、公式、图表事实说明与 run-level 边界
  - 动第4章表 `4-1` 到表 `4-7` 的事实内容、数值、指标、run 编号与 candidate 口径
  - 把第5章总结改成结果复述，或把展望改成既成成果
  - 让英文摘要比中文摘要更“敢写”

## 启动前提
- 已具备以下前置条件：
  - `PLAN7.md` 已执行过一轮“正文逻辑大检查 + 克制降 AI”收口
  - `document.tex` 与 `cover.tex` 已构成当前正式稿入口
  - 第1章到第5章及摘要对应的 `PLAN + 素材包` 已稳定
  - 当前任务只需语言收口，不需要重新建立章节 working draft
- 如果以下条件不满足，则不要直接执行本计划：
  - 章节边界再次发生变化
  - 数据集角色口径再次摇摆
  - `document.tex` 与 `cover.tex` 不是当前正式稿真源
  - 当前问题实质上是模板 / 前置页 / 提交包问题而不是正文语言问题

## 必读材料
- 总体 authority：
  - `<your-thesis-repo>\文档\参考文献\写作计划\PLAN7.md`
  - `<your-thesis-repo>\thesis\paper-outline.md`
  - `<your-thesis-repo>\thesis\paper-evidence-map.md`
  - `<your-thesis-repo>\thesis\paper-writing-log.md`
  - `<your-thesis-repo>\thesis\document.tex`
  - `<your-thesis-repo>\thesis\cover.tex`
- 章节级强制回读规则：
  - 改第1章：先读 `PLAN1.md + 第一章引言素材包`
  - 改第2章：先读 `PLAN2.md + 第二章文献素材包`
  - 改第3章：先读 `PLAN3.md + 第三章方法素材包`
  - 改第4章：先读 `PLAN4.md + PLAN4p.md + 第四章实验素材包`
  - 改第5章：先读 `PLAN5.md + 第五章总结素材包`
  - 改摘要：先读 `PLAN6.md + 摘要素材包`

## Skill 调用顺序
1. `$graduation-thesis-editor`
- 作为主流程编辑器，负责先稳住逻辑、边界、章节职责和论文语体。
- 所有章级正文与摘要修改都先经它，而不是直接丢给 `$humanizer`。
- 本轮 route 分配固定为：
  - 第1章、第2章、第5章、摘要正文：优先 `revision / 表达润色（中文论文）`
  - 第3章、第4章：先 `revision / 逻辑检查`，再对通过边界检查的段落使用 `revision / 表达润色（中文论文）`

2. `$humanizer`
- 只对已经稳定的局部段落做 very light 去 AI。
- 重点处理引言式、边界式、总结式、展望式段落。
- 不允许直接整章交给 `$humanizer`。
- 不允许把 `$humanizer` 用在：
  - 第3章高技术密度主段
  - 第4章数值分析主段
  - 表图说明中的事实性字段

3. 子智能体规则
- 本轮默认不需要子智能体。
- 原因固定为：修改集中在同一份正式稿与同一套 authority 上，目标是统一语气和手写感；主线程串行更稳。
- 若本轮额外做 QA，最多只允许在全部修改完成后加一次“诊断型” fresh-reader 检查，不在主起草过程中并行拆分。

## 推荐执行微流程
### 阶段 A：建立 target map
- 先在 `document.tex` 与 `cover.tex` 中标出本轮要动的段落桶，不直接大面积改文。
- 段落桶固定为：
  - 第1章引入 / 收束
  - 第2章综述开头 / 结尾
  - 第3章边界说明
  - 第4章解释段与 `4.6`
  - 第5章 `5.1 / 5.2`
  - 摘要中英文

### 阶段 B：按固定顺序串行处理
- 执行顺序固定为：
  1. 摘要
  2. 第5章
  3. 第4章
  4. 第1章
  5. 第2章
  6. 第3章
- 原因写死为：
  - 先处理最容易暴露 AI 总结腔、又最影响答辩印象的摘要与总结章
  - 再处理实验章收束
  - 最后处理方法章和文献章，避免高技术段被过度润色

### 阶段 C：每一章 / 摘要的固定动作
1. 先回读对应 `PLAN + 素材包`
2. 再用 `$graduation-thesis-editor` 做逻辑与论文表述收口
3. 最后只对明显仍带模板腔的段落补一层 `$humanizer`

### 阶段 D：并回与验证
- 所有修改仍并回现有正式稿入口：
  - `<your-thesis-repo>\thesis\document.tex`
  - `<your-thesis-repo>\thesis\cover.tex`
- 编译规则固定为 `.vscode/settings.json` 中的 `latexmk (xelatex)`
- 输出目录固定为 `<your-thesis-repo>\thesis\build\`

## `$graduation-thesis-editor` 调用规则
- 每次调用都必须 route-first。
- 一次调用只允许一个 route。
- 混合任务必须拆成串行步骤。
- 调用前必须显式给出：
  - `Task goal`
  - `Expected route type`
  - `Route ID`
  - `Prompt Source`
  - `Prompt Preserved Verbatim`
- 不默认使用其内部 de-AI fallback 替代 `$humanizer`；只有在用户明确要求“结果必须紧贴 LaTeX 约束且不走 humanizer”时，才考虑 fallback。

## `$humanizer` 调用规则
- 只用于显式 de-AI 或 final style cleanup。
- 只做 small, high-value edits，不做 wholesale rewrite。
- 必须保留原作者的 claims、numbers、stance 和 academic hedging。
- 学位论文场景下，“更像人写的”指的是更可信、更自然，而不是更口语化或更夸张。

## 推荐提示词模板
### 第1章 / 第2章 / 第5章 / 摘要的 GTE 提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 对当前已稳定段落做局部论文表述润色，降低模板化总结腔与空泛转承句，但不改变事实、章节职责和结论强度。

Expected route type:
- revision / 表达润色（中文论文）

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 本次调用只处理当前段落桶，不顺手扩大到整章重写。
```

### 第3章 / 第4章的 GTE 提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 先检查当前段落是否存在边界越界、措辞过强或方法/实验职责混淆，再仅对通过边界检查的段落做局部论文表述收口。

Expected route type:
- revision / 逻辑检查

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 本次调用先做检查，不顺手升级结论强度。
```

### Humanizer 提示词
```text
Use $humanizer.

Task:
- 对已通过 GTE 收口的局部段落做 very light 去 AI 清理，只去掉模板化总结腔、空泛转承句和过整齐的句式，不改事实、不改术语、不改结论边界。
```

## 编译规则
- 只有在修改已并回 `document.tex` 或 `cover.tex` 后，才执行编译。
- 编译 recipe：
  - VS Code LaTeX Workshop `latexmk (xelatex)`
- 配置来源：
  - `<your-thesis-repo>\.vscode\settings.json`
- 输出目录：
  - `<your-thesis-repo>\thesis\build\`

## 执行后同步
- 最小更新：
  - `<your-thesis-repo>\thesis\paper-writing-log.md`
- 记录内容固定为：
  - 哪些章做了定向降 AI
  - 哪些章只做了 GTE，没有追加 `$humanizer`
  - 编译是否通过
  - 是否出现 authority 风险
- 默认不修改：
  - `<your-thesis-repo>\thesis\paper-outline.md`
  - `<your-thesis-repo>\thesis\paper-evidence-map.md`
  - 任意章节素材包本体

## 验收标准
- `PLAN8.md` 已按 `PLAN_TEMPLATE.md` 的结构创建，而不是随手记要点。
- `PLAN8.md` 已明确从属 `PLAN7.md`，不会与 `PLAN7` 的模板 / 前置页主线冲突。
- 计划中已写死“改某章先回读该章 `PLAN + 素材包`”，不会再次凭 closeout 直改章级正文。
- 计划中已明确区分：
  - `$graduation-thesis-editor` 用于稳逻辑和边界
  - `$humanizer` 用于 very light 去 AI
- 计划中已写死不处理的高风险区域：
  - 第3章高技术密度主段
  - 第4章数值 / 表格主段
  - 任何会加强结论的措辞
- 执行完成后的正文应满足：
  - 公式化总结腔明显减少
  - 章节职责、实验边界、数据集层级和 candidate 口径完全不变
  - 中文摘要与英文摘要结论强度仍一致
  - 编译继续通过
  - 不新增新的可见版式硬伤

## 禁止事项
- 不把本计划理解为“全文再重写一遍”。
- 不为追求手写感而改动实验事实、数字、结论边界或数据集角色。
- 不把 `$humanizer` 当作章级主流程编辑器。
- 不在未回读对应 `PLAN + 素材包` 的前提下直接碰章级正文。
- 不新增图、不改图表事实、不改参考文献条目。

## 假设与默认
- 默认“你刚刚说的地方”包含摘要、第1章、第2章、第3章少量边界段、第4章解释段与 `4.6`、第5章 `5.1 / 5.2`。
- 默认本轮目标是“定向降 AI”，不是“全文再重写一遍”。
- 默认 `$humanizer` 只做 very light cleanup，不追求把整篇论文改成完全口语化或风格剧变。
- 默认创建 `PLAN8.md` 时只最小同步 `paper-writing-log.md`，不改 `paper-outline.md` 与 `paper-evidence-map.md`。

