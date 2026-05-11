# T-009R 第三章重写执行计划

## 摘要
- 本计划只服务于第3章重写，不扩展到第4章到第5章正文。
- 本轮目标不是沿用旧 `T-009` 口径做小修，而是基于第三章素材包 V2，按“方法设计 + 最少必要实现机制”重写第3章 `3.1 -> 3.6` 的 working draft。
- 主流程固定为 `$doc-coauthoring`，局部编辑固定为 `$graduation-thesis-editor`；不重新调用 `$academic-paper-strategist`，也不进入 `$academic-paper-composer`。
- 编译规则继续固定为 VS Code LaTeX Workshop 的 `latexmk (xelatex)`，严格按 [settings.json](/G:/bishe/JLU-CCST-Thesis/.vscode/settings.json) 执行，输出到 `G:\bishe\JLU-CCST-Thesis\thesis\build\`。
- 落稿策略固定为“先侧写 working draft，再并回正式骨架”；第3章唯一工作草稿仍固定为 [chapter3-working-draft.md](/G:/bishe/JLU-CCST-Thesis/thesis/chapter3-working-draft.md)。

## 计划定位
- 这是“第3章重写专项计划”，不是整篇论文总计划。
- 本计划默认继承以下 authority：
  - [paper-outline.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-outline.md)
  - [paper-evidence-map.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-evidence-map.md)
  - [paper-writing-log.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-writing-log.md)
  - [README.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/第三章方法素材包/README.md)
- 本计划明确是旧 `T-009` 完成后的重收口续篇，因此内部任务编号统一切换为 `T-009R`。
- 本计划不再引用旧版单层素材包 authority 文件；所有第三章写作入口统一切换到 V2 双层素材包。

## 本章范围
- 只写：
  - `3.1 框架整体思路与流程`
  - `3.2 图像分割与初始细胞区域构建`
  - `3.3 基于表达信息的细胞扩展与优化机制`
  - `3.4 流形展开与空间结构重构`
  - `3.5 分割结果回写与评价指标`
  - `3.6 本章小结`
- `3.5` 内部继续展开：
  - `3.5.1 Precision`
  - `3.5.2 Recall`
  - `3.5.3 F1-score`
  - `3.5.4 mIoU`
  - `3.5.5 PQ`
- 不启动：
  - 第4章实验结果
  - 第5章总结
  - 任意 `SMURF` 独立小节
- 第3章固定定位：
  - 第3章只写方法链路、阶段职责、输入输出关系和最少必要实现机制。
  - 第3章应用自己的话介绍该方法思路，正文尽量不显式使用 `SMURF` 字样。
  - 第3章默认不写 run-level 台账，不写实验优劣判断，不写大段默认参数说明。

## 启动前提
- 已满足：
  - 第1章和第2章已完成，可为第3章提供前文上下文。
  - 第三章素材包 V2 已完成，且已分为“正文可写层 / 后台核对层”。
  - [document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex) 中已有第3章骨架。
  - [paper-outline.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-outline.md) 与 [paper-evidence-map.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-evidence-map.md) 已完成第三章口径收紧。
- 若以下条件不满足，不应直接执行本计划：
  - 第3章职责再次与第2章或第4章混淆。
  - 第三章素材包 V2 路径失效。
  - 第3章证据优先级再次摇摆回“旧单层素材包”。

## 必读材料
- 长期记忆三件套：
  - [paper-outline.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-outline.md)
  - [paper-evidence-map.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-evidence-map.md)
  - [paper-writing-log.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-writing-log.md)
- 第三章素材包 V2 根说明：
  - [README.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/第三章方法素材包/README.md)
- 第三章素材包 V2 正文可写层：
  - [第三章写作总纲.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/第三章方法素材包/正文可写层/第三章写作总纲.md)
  - [第三章分节起草卡.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/第三章方法素材包/正文可写层/第三章分节起草卡.md)
  - [第三章最少必要机制卡.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/第三章方法素材包/正文可写层/第三章最少必要机制卡.md)
  - [第三章图表建议清单.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/第三章方法素材包/正文可写层/第三章图表建议清单.md)
- 第三章素材包 V2 后台核对层：
  - [第三章流程核对总表.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/第三章方法素材包/后台核对层/第三章流程核对总表.md)
  - [第三章参数核对表.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/第三章方法素材包/后台核对层/第三章参数核对表.md)
  - [第三章运行事实附录.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/第三章方法素材包/后台核对层/第三章运行事实附录.md)
  - [第三章图产物索引.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/第三章方法素材包/后台核对层/第三章图产物索引.md)
- 目标正文与文献库：
  - [document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex)
  - [document.bib](/G:/bishe/JLU-CCST-Thesis/thesis/document.bib)
- 外部方法来源与术语核对材料：
  - [2025.05.28.656357v1.full.pdf](/G:/bishe/JLU-CCST-Thesis/文档/2025.05.28.656357v1.full.pdf)
  - `https://the-mitra-lab.github.io/SMURF/index.html`
  - `https://the-mitra-lab.github.io/SMURF/Data_structure/index.html`
  - `https://the-mitra-lab.github.io/SMURF/api/reference/smurf.make_preparation.html`
  - `https://the-mitra-lab.github.io/SMURF/api/reference/smurf.make_pixels_cells.html`

## 证据优先级
- 第一优先：第三章素材包 `正文可写层/`
- 第二优先：第三章素材包 `后台核对层/`
- 第三优先：SMURF 预印本与官网术语页
- 默认规则：
  - 正文主张优先来自 `正文可写层/`。
  - `后台核对层/` 只用于核对事实、路径、参数和 reviewer 式复查，不直接抄入正文。
  - SMURF 官网 / API / Data Structure 页只用于术语、对象语义和阶段职责核对，不提升为高于本地素材包的正文事实源。
- 明确禁止继续引用已废弃的旧版单层素材包根目录 authority 文件。

## 本章边界
- `3.1` 只写流程分段、输入输出关系、与既有思路的关系。
  - 禁止 GT 前置。
  - 禁止 run-level 统计。
- `3.2` 只写 `StarDist + spatial object` 的实际实现机制。
  - 禁止图像尺寸、标签数、裁切坐标、初始细胞数。
  - 禁止把 Watershed / Cellpose 写成实际执行模块。
- `3.3` 只写过滤、聚类、分组优化、GPU、early stop。
  - 禁止 `group_count`、mixed spot 统计、epoch 数、默认参数值清单。
  - 禁止补理论最优性和数学证明。
- `3.4` 只写结果组装与空间结构重构层。
  - 禁止 `n_clusters`、stage4 定量统计、完整生物学复现叙事。
  - 正文首段必须显式限制为“结果组装与空间结构重构层”。
- `3.5` 只写 transfer、GT 对齐位置和指标定义。
  - 禁止 baseline 数值。
  - 禁止详细阈值表。
  - 禁止未使用指标如 `mAP`。
- `3.6` 只做方法收束与桥接第4章。
  - 禁止提前写实验优劣判断。

## 图表计划
- 保留：
  - 图3-1 整体流程图
  - 图3-2 初始分割与区域构建示意图
  - 图3-4 空间结构重构结果图
- 图3-3 固定为 1 组机制解释图，不再保留多张过程图并列展示。
- 表3-1 固定为“阶段职责与最少必要实现机制表”。
- 表3-2 固定为“评价指标定义表”。
- 第3章图表默认服务于解释方法，不服务于证明结果优劣。

## Skill 调用顺序
### 1. 主流程：`$doc-coauthoring`
- 第3章主起草 workflow 固定为 `$doc-coauthoring`。
- 按该 skill 的三段逻辑执行：
  - `Context Gathering`
  - `Refinement & Structure`
  - `Reader Testing`
- 由于本章已经具备长期记忆与素材包 V2，`Context Gathering` 的输入固定由本计划的“必读材料”清单承担，不再临场自由发散。
- 用 `$doc-coauthoring` 创建并维护唯一 working draft：
  - [chapter3-working-draft.md](/G:/bishe/JLU-CCST-Thesis/thesis/chapter3-working-draft.md)

### 2. 局部编辑：`$graduation-thesis-editor`
- `$graduation-thesis-editor` 只用于已有草稿后的局部编辑、逻辑检查和 reviewer 诊断。
- 它不是第3章 blank-page writing workflow，不能替代 `$doc-coauthoring`。
- 每次调用前必须执行 route-first。
- 常见 route 固定为：
  - `revision / 表达润色（中文论文）`
  - `revision / 逻辑检查`
  - `analysis / 论文整体以 Reviewer 视角进行审视`
- 每次调用前必须报告：
  - `Route ID`
  - `Prompt Source`
  - `Prompt Preserved Verbatim`
- 一次调用只允许一个 route。
- 混合请求必须拆成串行两步或多步。

### 3. 局部 editor 任务的子智能体规则
- 可根据需要创建子智能体执行局部 editor 任务。
- 这里的“是否创建子智能体”只针对局部 editor 任务本身，不等同于章节完成后的 reader testing。
- 但并不是一律都要创建子智能体：
  - 如果任务规模不大、目标单一、串行处理更稳，可以直接主线程完成。
  - 只有在需要陌生视角、可并行拆开的多个局部任务，或需要避免上下文污染时，才优先考虑创建子智能体。
- 是否创建子智能体、创建几个子智能体，由当时的任务拆分复杂度决定，但执行前必须显式判断一次。

### 4. chapter-end reader testing
- chapter-end reader testing 继续作为强制步骤。
- 章节级 reader testing 与局部 editor 任务不同：前者固定要求至少 1 个 fresh-reader 子智能体执行，后者仍按任务规模判断是否需要子智能体。
- 第3章的章节级 reader testing 默认采用“前文连续阅读”模式，而不是默认只读当前章。
- 第3章默认主测读取范围固定为：
  - `第1章 + 第2章 + 第3章`
- 若上下文长度在实际执行时过长，最低回退范围不得少于：
  - `第2章 + 第3章`
- 若需要补查“脱离前文时本章是否仍自洽”，可追加一次“只读第3章”的专项测试。
- 但“只读第3章”不能替代默认主测。
- 第3章 reader testing 至少检查：
  - 本章与第2章、第4章是否发生职责混淆
  - 陌生读者是否会误解第3章的方法角色、数据集角色或主张边界
  - 读者是否会误以为 GT 是整条流程的前置输入，而不是 `3.5` 的评价输入
  - 读者是否会误以为 `3.4` 已经完成原论文级别的完整生物学复现
  - 本章是否提前泄露第4章的实验结果或优劣判断

### 5. 禁止提前使用
- 不重新调用 `$academic-paper-strategist`
- 不提前进入 `$academic-paper-composer`
- 只有整章已经稳定之后，才可选使用 `$humanizer` 做局部语言去公式化。

## 分阶段流程
### 阶段 A：建立第3章 working draft 骨架
- 用 `$doc-coauthoring` 打开并重写 [chapter3-working-draft.md](/G:/bishe/JLU-CCST-Thesis/thesis/chapter3-working-draft.md)。
- 固定六个小节骨架：
  - `3.1`
  - `3.2`
  - `3.3`
  - `3.4`
  - `3.5`
  - `3.6`

### 阶段 B：按小节顺序推进
- 固定顺序：
  - `3.1 -> 3.2 -> 3.3 -> 3.4 -> 3.5 -> 3.6`
- 不跳序推进。
- 默认允许 `3.1`、`3.4`、`3.5` 投入最多迭代轮次。

### 阶段 C：小节级微流程
1. 先由 `$doc-coauthoring` 完成该节的“要点筛选 + 小节草稿”。
2. 草稿完成后立刻对照 V2 素材包正文可写层做边界检查。
3. 若存在语言重复、逻辑跳跃、来源边界混淆、章节越界，再调用 `$graduation-thesis-editor`。
4. 小节通过后继续下一个小节，不立刻并回 [document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex)。

### 阶段 D：整章级复核
- 六节完成后，用 `$graduation-thesis-editor` 做一次 reviewer 式整章诊断。
- 重点检查：
  - `3.1` 是否把“参考既有思路”写成“本文原创发明完整框架”
  - `3.2` 是否把 Watershed / Cellpose 写成实际执行模块
  - `3.4` 是否夸大为完整生物学复现
  - `3.5` 是否把 GT 写成前置输入或把指标定义写成结果结论
- 然后必须显式调用 fresh-reader 子智能体做 chapter-end reader testing。
- 主测默认先按“前文连续阅读”模式执行，即先读已稳定前文，再读第3章。
- 如需补查“只读第3章时是否仍自洽”，可在主测之外追加一次只读当前章的补测，但不能替代主测。
- 若 reader testing 暴露明显误读风险，先修订，再做一次轻量复测后才允许关闭本章。

### 阶段 E：并回与编译
- 只有在整章 working draft 稳定后，才一次性并回 [document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex)。
- `document.bib` 只补本章最终实际新增使用条目。
- 编译只在并回后执行。
- 整篇论文主体章节起草完成后，必须显式调用 fresh-reader 子智能体再做一次全文 reader testing，不能按需跳过。
- 全文 reader testing 重点检查：
  - 跨章节逻辑是否连贯
  - 第2章、第3章、第4章之间是否存在边界回流或结论重复
  - 主线数据集、supporting dataset 与 workflow-support dataset 的角色口径是否全篇一致
  - 引言、方法、实验、总结之间是否存在前后矛盾或过度主张

## `$graduation-thesis-editor` 调用规则
- 每次调用都必须先执行该 skill 的全局 route-first 规则。
- 调用前必须先判断该任务是否需要子智能体：
  - 若任务规模不大、不是必须并行拆开的工作，可不调用子智能体。
  - 若任务需要陌生视角、并行诊断或上下文隔离，再创建子智能体。
- 调用前必须显式给出：
  - `Task goal`
  - `Expected route type`
  - `Route ID / Prompt Source / Prompt Preserved Verbatim`
- 一次调用只能对应一个 route。
- 如果 routing 判断当前任务不是“已有草稿后的局部编辑任务”，必须停止强行使用 editor，并交还 `$doc-coauthoring`。
- 混合请求必须拆开，不能在一次调用里同时做“检查 + 改写”或“分析 + 润色”。

## 推荐提示词
### 第3章主起草提示词
```text
Use $doc-coauthoring.

Read first:
- G:\bishe\JLU-CCST-Thesis\文档\参考文献\写作计划\PLAN3.md
- G:\bishe\JLU-CCST-Thesis\thesis\paper-outline.md
- G:\bishe\JLU-CCST-Thesis\thesis\paper-evidence-map.md
- G:\bishe\JLU-CCST-Thesis\thesis\paper-writing-log.md
- G:\bishe\JLU-CCST-Thesis\文档\参考文献\第三章方法素材包\README.md
- G:\bishe\JLU-CCST-Thesis\文档\参考文献\第三章方法素材包\正文可写层\第三章写作总纲.md
- G:\bishe\JLU-CCST-Thesis\文档\参考文献\第三章方法素材包\正文可写层\第三章分节起草卡.md
- G:\bishe\JLU-CCST-Thesis\文档\参考文献\第三章方法素材包\正文可写层\第三章最少必要机制卡.md
- G:\bishe\JLU-CCST-Thesis\文档\参考文献\第三章方法素材包\正文可写层\第三章图表建议清单.md
- G:\bishe\JLU-CCST-Thesis\文档\2025.05.28.656357v1.full.pdf
- https://the-mitra-lab.github.io/SMURF/index.html
- https://the-mitra-lab.github.io/SMURF/Data_structure/index.html
- https://the-mitra-lab.github.io/SMURF/api/reference/smurf.make_preparation.html
- https://the-mitra-lab.github.io/SMURF/api/reference/smurf.make_pixels_cells.html
- G:\bishe\JLU-CCST-Thesis\thesis\document.tex
- G:\bishe\JLU-CCST-Thesis\thesis\document.bib

Task:
Rewrite G:\bishe\JLU-CCST-Thesis\thesis\chapter3-working-draft.md and co-author Chapter 3 in this order:
3.1 -> 3.2 -> 3.3 -> 3.4 -> 3.5 -> 3.6

Rules:
- Treat 正文可写层 as the default evidence source.
- Use 后台核对层 only when fact-checking is necessary.
- Keep Chapter 3 at the “method design + minimum necessary implementation mechanisms” level.
- Do not write GT as a pipeline input in 3.1.
- Do not write image size, crop coordinates, initial cell counts, group_count, n_clusters, epoch counts, or default parameter tables into the正文.
- Do not write Watershed or Cellpose as actual execution modules.
- Do not turn 3.4 into a full biological unrolling / zonation reproduction claim.
- Do not write experiment results in Chapter 3.
- Keep citations minimal and real; only add new bib entries if the final draft truly uses them.
```

### `3.1` 逻辑检查提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 检查第3章 `3.1 框架整体思路与流程` 当前草稿是否把“参考既有流形展开思路”写成了“本文原创发明完整框架”，以及是否把 GT 写成了流程前置输入。

Expected route type:
- revision / 逻辑检查

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 本次调用只做诊断，不同时做润色改写。
```

### `3.4` 逻辑检查提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 检查第3章 `3.4 流形展开与空间结构重构` 当前草稿是否夸大了工程重建范围，是否把当前结果写成完整 intestine unrolling / zonation 生物学复现。

Expected route type:
- revision / 逻辑检查

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 本次调用只做诊断，不同时做润色改写。
```

### 第3章整章 reviewer 诊断提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 以毕业论文 reviewer 的视角检查第3章整章草稿，逐节指出边界越界、来源夸大、GT 角色错误、实验结果前置和过度主张问题。

Expected route type:
- analysis / 论文整体以 Reviewer 视角进行审视

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 本次调用只做 reviewer 式诊断，不顺手重写全文。
```

## 编译规则
- 只有在第3章 working draft 已经并回 [document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex) 后，才执行编译。
- 编译 recipe：
  - VS Code LaTeX Workshop `latexmk (xelatex)`
- 配置来源：
  - [settings.json](/G:/bishe/JLU-CCST-Thesis/.vscode/settings.json)
- 输出目录：
  - `G:\bishe\JLU-CCST-Thesis\thesis\build\`
- 对应配置依据：
  - `latex-workshop.latex.outDir = "./build"`

## 执行后同步
- 本轮完成后，至少同步：
  - [paper-writing-log.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-writing-log.md)
- 若第3章边界、allowed claims、图表落点发生变化，再同步：
  - [paper-evidence-map.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-evidence-map.md)
- 若第3章重写后并回正式正文，再同步：
  - [document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex)
  - [document.bib](/G:/bishe/JLU-CCST-Thesis/thesis/document.bib)
- chapter-end reader testing 完成后，必须在 [paper-writing-log.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-writing-log.md) 中登记：
  - 是否执行
  - 主测读取范围
  - 是否做了只读第3章的补测
  - 发现了什么问题
  - 是否完成修订闭环
- 整篇论文主体章节完成后，必须在日志中登记是否已完成全文 reader testing，以及全文 reader testing 的读取范围与主要问题。

## 验收标准
- `PLAN3.md` 标题已改为 `T-009R 第三章重写执行计划`。
- `PLAN3.md` 不再引用旧版第三章根目录 authority 文件。
- `PLAN3.md` 已明确“正文可写层优先、后台核对层次之、官网/API 仅做术语核对”的证据优先级。
- `PLAN3.md` 中的 `3.1` 到 `3.6` 边界与 [paper-evidence-map.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-evidence-map.md) 完全一致。
- `PLAN3.md` 已写死第3章默认主 reader testing 范围为“第1章 + 第2章 + 第3章”。
- `PLAN3.md` 已明确章节级 reader testing 默认采用“前文连续阅读优先”的规则，而不是默认只读当前章。
- `PLAN3.md` 已写死编译方式为 `.vscode/settings.json` 中的 `latexmk (xelatex)`，输出到 `thesis/build/`。
- `PLAN3.md` 仍把 [chapter3-working-draft.md](/G:/bishe/JLU-CCST-Thesis/thesis/chapter3-working-draft.md) 作为唯一工作草稿文件。
- 每次 `$graduation-thesis-editor` 调用都必须 route-first。
- 第3章关闭前已经显式完成至少 1 轮子智能体 chapter-end reader testing。
- 第3章重写前不提前进入 `$academic-paper-composer`。

## 禁止事项
- 不要把 `PLAN3.md` 当作整篇论文的总计划。
- 不要用 `$graduation-thesis-editor` 代替第3章 blank-page writing。
- 不要把多个 editor prompt 合并成一次调用。
- 不要在第3章 working draft 尚未稳定时提前并回正式正文。
- 不要把官网/API 页当成高于本地素材包的正文事实源。
