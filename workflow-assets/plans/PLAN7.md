# T-013 全文收口、复审与定稿执行计划

## 摘要
- 本计划服务于 `T-013`：在第1章到第5章正文与摘要均已稳定并回之后，对整篇论文执行全文收口、复审、按问题分流修补与最终定稿整理。
- 当前目标不是重新展开章节起草，也不是继续随机全文润色，而是基于当前 merged draft 做全文级风险排查、最小必要修补、模板与格式收口，以及最终提交前整理。
- 本轮全文收口默认不整包预读所有章节素材包；采用“**全文级 authority 默认读长期记忆三件套 + 正式稿，定位到某一章或摘要后再强制补读对应章节计划与素材包**”的策略。
- 当前激活切片固定为 `T-013A 学长意见吸收与定稿分流`：本轮要把学长意见正式吸收到 authority 中，再分流处理第3章/第4章图像、第五章结构与模板收口。
- `T-013A` 的 5 条修补主线固定为：
  - 页13大图缩页
  - AI 味 / 符号统一小修
  - Chapter 3 + Chapter 4 图像丰富度补强
  - Chapter 5 结构改为 `5.1 全文总结` + `5.2 研究展望`
  - 字体与 LaTeX 模板格式收口
- 当前本地主链 skill 固定为：
  - `$codex-project-memory`
  - `$thesis-closeout-reviewer`
  - `$academic-paper-reviewer`
  - `$graduation-thesis-editor`
  - `$doc-coauthoring`
  - `$humanizer`
  - `$academic-plotting`
  - `$academic-paper-composer`
- `T-013` 覆盖范围固定为“**收口到定稿**”，`$academic-paper-composer` 不再继续无限后置，而是作为本计划末段的正式定稿整理工具。
- 本轮格式 authority 固定为当前本地 `JLU-CCST-Thesis` 模板；LaTeX 视为允许项，不再把“是否能用 LaTeX”当作阻塞问题。

## 计划定位
- 这是一个“整篇论文级执行计划”，不是章节计划模板的简单套壳。
- 它默认继承：
  - [paper-outline.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-outline.md)
  - [paper-evidence-map.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-evidence-map.md)
  - [paper-writing-log.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-writing-log.md)
- 它必须服从当前冻结目录、章节证据边界、数据集角色口径与摘要边界。
- 当前阶段已经不是章节起草期：
  - 第1章到第5章正文已完成并并回 [document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex)
  - 中英文摘要已稳定并回 [cover.tex](/G:/bishe/JLU-CCST-Thesis/thesis/cover.tex)
  - 各章 chapter-end reader testing 与摘要专项 fresh-reader testing 已有执行记录
  - `T-013` 的默认动作是全文收口与定稿，而不是重新大面积重写正文

## 本轮范围
- 只做：
  - 全文级 closeout diagnosis
  - 全文级 reviewer / re-review
  - 按问题分流的局部修补
  - 必要时的局部重开
  - 模板、版式、图表、前置页与提交流程收口
  - 最终定稿整理
- `T-013A` 的批准实改范围还包括：
  - 先改 authority，再动正文
  - 第3章现有图 `图3-1` 到 `图3-4` 的尺寸、字体、标题与注释统一
  - 第4章基于真实实验归档补强图像丰富度
  - 第5章从单节 `5.1 全文总结与展望` 重开为双节 `5.1 全文总结` + `5.2 研究展望`
  - 在本地模板 authority 下做安全的字体与 LaTeX 版式收口
- 不默认启动：
  - 第1章到第5章的大范围重写
  - 除已批准的第5章双节拆分外，重新规划目录结构
  - 重新建立章节素材包
  - 新增超出正文证据范围的新实验结论
  - 改变数据集角色层级
  - 改写 `EXP-007` 的结论强度
- 全文边界约束：
  - `Visium HD MouseBrain` 始终是唯一主实验线。
  - `Human Ovarian` 始终只作 supporting dataset。
  - `Xenium Ovarian` 与 `Xenium MouseBrain` 始终只作 workflow-support dataset。
  - `EXP-007` 始终只能写成 strongest current candidate，不能写成已 promoted baseline。
  - 第3章继续保持“方法设计 + 最少必要实现机制”的边界，不得在全文收口阶段反向写成实验章。

## 启动前提
- 已具备以下前置条件：
  - [paper-outline.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-outline.md)、[paper-evidence-map.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-evidence-map.md)、[paper-writing-log.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-writing-log.md) 已同步到“前五章与摘要已完成”的阶段。
  - [document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex)、[cover.tex](/G:/bishe/JLU-CCST-Thesis/thesis/cover.tex)、[document.bib](/G:/bishe/JLU-CCST-Thesis/thesis/document.bib) 已构成当前正式稿入口。
  - [PLAN1.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN1.md) 到 [PLAN6.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN6.md) 及对应素材包已稳定，可作为局部回读 authority。
  - 当前模板编译入口与输出路径已固定在 [.vscode/settings.json](/G:/bishe/JLU-CCST-Thesis/.vscode/settings.json) 与 `thesis/build/`。
- 若以下条件不满足，则不要直接执行本计划：
  - 章节边界再次发生实质变化
  - 数据集角色口径再次摇摆
  - 正式稿与 working draft 之间出现明显不同步
  - 模板入口或编译配置失效
- `T-013A` 的额外硬前提：
  - 若要改第3章图与正文，先回读 [PLAN3.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN3.md) + `第三章方法素材包/`
  - 若要改第4章图与正文，先回读 [PLAN4.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN4.md) / [PLAN4p.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN4p.md) + `第四章实验素材包/`
  - 若要改第5章正文，先回读 [PLAN5.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN5.md) + `第五章总结素材包/`
  - 若要改摘要，先回读 [PLAN6.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN6.md) + `摘要素材包/`

## 必读材料
- 长期记忆三件套：
  - [paper-outline.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-outline.md)
  - [paper-evidence-map.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-evidence-map.md)
  - [paper-writing-log.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-writing-log.md)
- 正式稿入口：
  - [document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex)
  - [cover.tex](/G:/bishe/JLU-CCST-Thesis/thesis/cover.tex)
  - [document.bib](/G:/bishe/JLU-CCST-Thesis/thesis/document.bib)
- 编译配置：
  - [settings.json](/G:/bishe/JLU-CCST-Thesis/.vscode/settings.json)
- 章节与摘要计划入口：
  - [PLAN1.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN1.md)
  - [PLAN2.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN2.md)
  - [PLAN3.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN3.md)
  - [PLAN4.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN4.md)
  - [PLAN4p.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN4p.md)
  - [PLAN5.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN5.md)
  - [PLAN6.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN6.md)

## 默认 authority 读取规则
### A. 全文级默认 authority
- 默认只读：
  - [paper-outline.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-outline.md)
  - [paper-evidence-map.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-evidence-map.md)
  - [paper-writing-log.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-writing-log.md)
  - [document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex)
  - [cover.tex](/G:/bishe/JLU-CCST-Thesis/thesis/cover.tex)
  - [document.bib](/G:/bishe/JLU-CCST-Thesis/thesis/document.bib)
  - [settings.json](/G:/bishe/JLU-CCST-Thesis/.vscode/settings.json)
- 默认不把所有章节素材包整包读入全文收口主线。

### B. 章节级问题分流 authority
- 若问题定位到第1章：
  - 强制补读 [PLAN1.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN1.md) + `第一章引言素材包/`
- 若问题定位到第2章：
  - 强制补读 [PLAN2.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN2.md) + `第二章文献素材包/`
- 若问题定位到第3章：
  - 强制补读 [PLAN3.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN3.md) + `第三章方法素材包/`
- 若问题定位到第4章前半：
  - 强制补读 [PLAN4.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN4.md) + `第四章实验素材包/前半写作层/`
- 若问题定位到第4章结果或本章小结：
  - 强制补读 [PLAN4p.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN4p.md) + `第四章实验素材包/结果分析层/`
- 若问题定位到第5章：
  - 强制补读 [PLAN5.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN5.md) + `第五章总结素材包/正文可写层/`
- 若问题定位到摘要：
  - 强制补读 [PLAN6.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN6.md) + `摘要素材包/`

### C. 默认禁止
- 不要把“每次全文审稿都默认读入所有章节素材包”写成 `T-013` 规则。
- 不要在局部修补时跳过对应章节 authority，直接凭全文上下文回改高风险章节。

## Skill 调用顺序
1. `$codex-project-memory`
- 用于维持 `T-013` 的文档优先、范围收束和同步纪律。
- 只负责约束、进度和文档同步，不直接承担正文大段改写。

2. `$thesis-closeout-reviewer`
- 作为全文级本地审稿入口，默认第一步。
- 任务是输出问题台账，不直接改正文。

3. `$academic-paper-reviewer`
- 作为外部视角复审器与 re-review 工具。
- 只做 review findings / roadmap，不承担日常微调。

4. `$graduation-thesis-editor`
- 作为局部修补唯一默认编辑器。
- 只在已有正文基础上做局部逻辑修复、缩写、扩写、实验分析、caption 或 reviewer 视角诊断。
- 每次调用都必须 route-first。

5. `$doc-coauthoring`
- 仅当某一章或某一节必须真正“重开”时使用。
- 不再作为 `T-013` 的默认主流程。
- `T-013A` 中优先用于：authority 文档重校，以及第5章双节结构重开。

6. `$humanizer`
- 只用于末期叙述性段落的轻量去公式化。
- 默认只覆盖摘要、绪论、结论/总结段。

7. `$academic-plotting`
- 只在现成真实图源不足以入文时触发。
- `T-013A` 中优先原则是“先抽真实实验图，再考虑重绘或新绘图”，不为“显得丰富”而虚构图片。

8. `$academic-paper-composer`
- 作为 `T-013` 末段的正式定稿整理工具。
- 前提是前面的诊断、局部修补和必要复审已经完成。

## 子智能体使用规则
- `T-013` 不默认对每一步都创建子智能体，但**每次进入一个新的实质任务前，必须显式判断一次是否需要子智能体协助**。
- 判断原则固定为：
  - 若当前任务目标单一、修改范围小、串行处理更稳，则默认不创建子智能体。
  - 若当前任务需要陌生读者视角、可并行拆分的多问题桶，或需要上下文隔离以避免章节边界互相污染，则优先考虑创建子智能体。

### 默认不需要子智能体的场景
- `Pass 0` 状态校准与 authority 对齐。
- `$thesis-closeout-reviewer` 的常规整篇诊断。
- `$academic-paper-reviewer` 的常规整篇复审或 re-review。
- 单目标、低改动面的局部修补，例如一段承接句、一段摘要表述、单个 caption、一次局部润色。
- `$humanizer` 的末期轻量风格清理。
- `$academic-paper-composer` 的主线定稿整理。

### 优先考虑子智能体的场景
- 需要 `fresh-reader` 视角的全文或局部 reader testing。
- 存在可并行拆开的、且写入范围互不重叠的问题桶，例如“第4章结果边界复核”和“摘要-正文一致性补测”。
- 需要把高风险章节边界问题与摘要/结论收口问题做上下文隔离，避免相互污染。

### 使用子智能体时的硬约束
- 一次只分配一个清晰职责，不给混合任务。
- 必须明确其读取范围、目标文本范围和输出目标。
- 多个子智能体不得同时修改同一段正文或同一组紧邻段落。
- 子智能体的输出默认先作为诊断或局部建议，再决定是否并回主线正文。

### 不使用子智能体时的要求
- 若本轮决定不使用子智能体，也必须在执行前显式说明理由，例如“当前任务范围小、目标单一、主线程串行更稳”。

## 推荐收口微流程
### Pass 0：状态校准
- 先确认以下入口一致：
  - [document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex)
  - [cover.tex](/G:/bishe/JLU-CCST-Thesis/thesis/cover.tex)
  - [document.bib](/G:/bishe/JLU-CCST-Thesis/thesis/document.bib)
  - [settings.json](/G:/bishe/JLU-CCST-Thesis/.vscode/settings.json)
- 用长期记忆三件套校准当前阶段，不再回到章节起草期。
- 若发现正式稿、working draft 和日志状态不一致，先修正文档状态认知，再进入正文处理。

### Pass 0.5：authority 重校
- 先同步：
  - [paper-outline.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-outline.md)
  - [paper-evidence-map.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-evidence-map.md)
  - [paper-writing-log.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-writing-log.md)
  - [PLAN5.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN5.md)
  - `第五章总结素材包/`
- `T-013A` 中任何涉及第5章双节拆分、图像补强或模板安全收口的正文修改，都必须建立在这一步之后。

### Pass 1：全文 closeout diagnosis
- 默认先用 `$thesis-closeout-reviewer`。
- 只输出问题台账，不直接改正文。
- 问题必须按以下类型归档：
  - 结构边界
  - 证据边界
  - 跨章衔接
  - 实验解释
  - 语言风险
  - 模板与版式风险

### Pass 2：按问题分流修补
- 局部补写、缩写、逻辑修复、实验分析、caption：
  - `$graduation-thesis-editor`
- 某章或某节必须真正重开：
  - `$doc-coauthoring`
- 图表确有缺口：
  - `$academic-plotting`
- 本阶段固定执行以下闭环：
  1. 问题定位到哪一章或摘要
  2. 补读对应 `PLAN + 素材包`
  3. 再做局部修改
- 若 `Pass 1` 只暴露 minor issues，则只做最小修补，不得借机重新展开大范围重写。
- `T-013A` 的分流优先级固定为：
  1. 第5章双节结构与对应 authority 同步
  2. 第3章页13大图与现有图风格统一
  3. 第4章真实图源补强
  4. AI 味 / 符号 / 模板字体与 LaTeX 格式收口

### Pass 3：全文级 re-review
- 默认用 `$academic-paper-reviewer`。
- 用途固定为：
  - 整篇复审
  - 对抗性审稿
  - 修改后 residual issue 检查
  - 必要时的 re-review
- 本阶段只产出 review findings / roadmap，不顺手改文。

### Pass 4：定稿前轻量语言打磨
- 只有当事实边界、章节边界和结果边界都稳定后，才考虑：
  - 对摘要、绪论、结论/总结段使用 `$humanizer`
- 默认不对第3章、第4章整章做去公式化。
- 若语言问题只出现在方法章或实验章，优先仍由 `$graduation-thesis-editor` 做局部论文表述修正。

### Pass 5：定稿整理
- 用 `$academic-paper-composer` 做：
  - 定稿整理
  - 模板收口
  - working draft 清理
  - 图表与前置页收口
  - 最终提交前包整理
- 本阶段仍必须遵守长期记忆三件套和章节边界，不得借定稿之名放大结论或改写事实。

## 全文 reader testing 规则
- 当前不是从零开始：
  - 各章 chapter-end reader testing 已有执行记录
  - 摘要专项 fresh-reader testing 已完成
  - 摘要与正文之间已有一轮全文级一致性核对记录
- `T-013` 中是否追加全文 fresh-reader testing，取决于本轮是否发生实质修改。

### 默认规则
- 若本轮只做 very minor 文句、格式或模板清理：
  - 可不强制重做整篇 fresh-reader testing
  - 可只做 reviewer 级 re-review 或定点复测
- 若本轮对以下内容做了实质修改：
  - 第4章
  - 第5章
  - 摘要
  - 跨章承接段
  - 数据集角色表述
  - 结果边界表述
  - 则必须追加一轮全文级 fresh-reader testing，或至少做“第4章 + 第5章 + 摘要”的收口复测
- `T-013A` 已预设会发生第4章 / 第5章实质改动，因此最低要求固定为：
  - 重做一次 Chapter 5 fresh-reader testing
  - 追加一次 `Chapter 4 + Chapter 5 + 摘要` 的联动 fresh-reader testing
  - 全部收口后再做一次 `$academic-paper-reviewer` 式 re-review

### 必查项
- `Visium HD MouseBrain` 是否仍是唯一主实验线
- `Human Ovarian` 是否仍只作 supporting dataset
- 两个 Xenium 是否仍只作 workflow-support dataset
- `EXP-007` 是否仍只写成 strongest current candidate 而非 promoted baseline
- 第3章方法边界是否被第4章或第5章回改后反向破坏
- 摘要与正文的结论强度是否仍一致

## `$graduation-thesis-editor` 调用规则
- 每次调用都必须先执行该 skill 的全局 route-first 规则。
- 调用前必须先判断该任务是否需要子智能体。
- 调用前必须显式给出：
  - `Task goal`
  - `Expected route type`
  - `Route ID / Prompt Source / Prompt Preserved Verbatim`
- 一次调用只能对应一个 route。
- 混合请求必须拆成串行步骤：
  - “检查并改写” = 先诊断，再改写
  - “分析并润色” = 先实验分析，再润色
  - “reviewer 看一遍并顺手改掉” = 先 reviewer 诊断，再局部改写
- 如果 routing 判断当前任务属于空白起草、章节规划或多轮共写，则必须交回 `$doc-coauthoring`。

## 推荐提示词
### 1. 全文先找问题
```text
Use $thesis-closeout-reviewer.

Read first:
- G:\bishe\JLU-CCST-Thesis\thesis\paper-outline.md
- G:\bishe\JLU-CCST-Thesis\thesis\paper-evidence-map.md
- G:\bishe\JLU-CCST-Thesis\thesis\paper-writing-log.md
- G:\bishe\JLU-CCST-Thesis\thesis\document.tex
- G:\bishe\JLU-CCST-Thesis\thesis\cover.tex

Task:
- 对整篇论文做收口审稿，只输出问题台账，不直接改写正文。

Rules:
- 重点检查结构边界、证据边界、跨章衔接、实验解释、语言风险和模板/版式风险。
- 不凭审稿印象要求新增正文外结论。
```

### 2. 修改后再做全文 re-review
```text
Use $academic-paper-reviewer to re-review my revised thesis, focus on unresolved reviewer-level issues, and do not rewrite the manuscript directly.
```

### 3. 局部修补高风险段落
```text
Use $graduation-thesis-editor.

Task goal:
- 在不改变结论边界、数据集角色和实验事实的前提下，修补这段正文中的局部逻辑或表述问题。

Expected route type:
- revision / 逻辑检查

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 若问题属于高风险章节，先补读对应 PLAN 与素材包再执行。
```

### 4. 某一节必须重开
```text
Use $doc-coauthoring 基于当前冻结目录、长期记忆三件套、对应章节 PLAN 和章节素材包，只重开这一节或这一小段，按既有边界重写，不扩散到整篇论文。
```

### 5. 定稿整理
```text
Use $academic-paper-composer 基于当前 merged draft、长期记忆三件套和已稳定的章节边界，对论文做定稿整理、模板收口和提交前清理，但不要改写超出证据范围的内容。
```

## 模板与编译收口规则
- 核心样式文件 [jluthesisUTF8.sty](/G:/bishe/JLU-CCST-Thesis/thesis/jluthesisUTF8.sty) 不作为本轮常规修改目标。
- 模板目录结构不再随意调整。
- 但 `T-013A` 允许在当前本地模板 authority 下，对 [jluthesisUTF8.sty](/G:/bishe/JLU-CCST-Thesis/thesis/jluthesisUTF8.sty)、[cover.tex](/G:/bishe/JLU-CCST-Thesis/thesis/cover.tex) 与 [document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex) 做安全、可回溯的格式收口，以解决字体、书签、页眉页脚、目录字符串与图表版式问题。
- `T-013` 优先处理以下 closeout 项：
  - 编译稳定性
  - 图表编号与引用一致性
  - 摘要、目录、参考文献、致谢、科研情况等前后页完整性
  - `overfull / underfull` 等排版风险的筛查与最小修正
- `T-013A` 的格式重点还包括：
  - 正文页码 13 的大图缩页
  - 第3章与第4章图题、图内英文、字号与字体观感统一
  - 不改模板骨架前提下的字体与 LaTeX 版式安全收口
- 不在 `T-013` 中重新打开大规模模板机制重构。

### 编译规则
- 编译 recipe：
  - VS Code LaTeX Workshop `latexmk (xelatex)`
- 配置来源：
  - [settings.json](/G:/bishe/JLU-CCST-Thesis/.vscode/settings.json)
- 输出目录：
  - `G:\bishe\JLU-CCST-Thesis\thesis\build\`

## 执行后同步
- `T-013` 任一收口切片完成后，至少同步：
  - [paper-writing-log.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-writing-log.md)
- 若本轮修改了正式稿：
  - [document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex)
  - [cover.tex](/G:/bishe/JLU-CCST-Thesis/thesis/cover.tex)
  - 必要时同步 [document.bib](/G:/bishe/JLU-CCST-Thesis/thesis/document.bib)
- 若本轮改变了某一章的可写边界、证据入口或收口规则，再同步：
  - [paper-evidence-map.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-evidence-map.md)
  - 必要时同步 [paper-outline.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-outline.md)
- 若本轮追加了全文 fresh-reader testing 或 reviewer re-review，必须在日志中登记：
  - 是否执行
  - 读取范围
  - 发现的问题
  - 是否完成修订闭环

## 验收标准
- `PLAN7.md` 已明确切换为 `T-013` 的全文收口、复审与定稿计划，而不是“初稿润色计划”。
- `PLAN7.md` 已把 `$academic-paper-composer` 纳入 `T-013` 末段，而不是继续无限后置。
- `PLAN7.md` 已明确采用“全文默认 authority + 章节问题分流 authority”的双层读取机制。
- `PLAN7.md` 已写死：章节计划与素材包不是每轮全文审稿都整包读，但一旦修某章就必须回读该章 `PLAN + 素材包`。
- `PLAN7.md` 已把全文流程固定为：
  - 先诊断
  - 再分流修补
  - 再 re-review
  - 再轻量语言打磨
  - 最后定稿整理
- `PLAN7.md` 已明确：当前已有前置 reader testing / 一致性核对历史，后续是否补做全文 fresh-reader testing 取决于本轮是否发生实质修改。
- `PLAN7.md` 已将“按任务规模显式判断是否需要子智能体”的规则纳入正式约束。
- `PLAN7.md` 已把模板与版式收口纳入约束，但不重新打开模板机制重构。
- `PLAN7.md` 已把 `T-013A` 的 5 条修补主线写死，并明确“先改 authority，再动正文”。
- `PLAN7.md` 已明确：第5章拆为 `5.1 全文总结` + `5.2 研究展望` 后，必须同步回改 authority 与素材包，而不是直接硬拆正文。
- `PLAN7.md` 已明确：第3章默认优化现有图号，第4章优先补真实 supporting / workflow-support 图源。
- `PLAN7.md` 已明确：本地 `JLU-CCST-Thesis` 模板是当前格式 authority，LaTeX 可直接用于本轮 closeout。

## 禁止事项
- 不要把 `PLAN7.md` 写成章节起草计划或整篇论文重写计划。
- 不要跳过诊断直接全文盲润。
- 不要让 `$academic-paper-reviewer` 接管日常局部润色。
- 不要让 `$humanizer` 提前介入方法章或实验章主修链。
- 不要在局部修补高风险章节时跳过对应章节 authority。
- 不要在中文 LaTeX 正文尚未收口前，随意切换到其他提交流程或改动模板结构。
