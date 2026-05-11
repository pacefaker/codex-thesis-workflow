# 章节执行计划模板

## 摘要
- 本计划仅服务于 `[章节名 / 任务切片名]`，不自动扩展到整篇论文。
- 本轮写作目标是：[填写本轮要完成的章节、小节或任务范围]。
- 本轮主 skill 是：[通常为 `$doc-coauthoring` 或其他主流程 skill]。
- 若本轮涉及编译，编译规则是：[填写 recipe 与配置来源]。

## 计划定位
- 这是一个“章节级执行计划”，不是整篇论文总计划。
- 它默认继承：
  - `G:\bishe\JLU-CCST-Thesis\thesis\paper-outline.md`
  - `G:\bishe\JLU-CCST-Thesis\thesis\paper-evidence-map.md`
  - `G:\bishe\JLU-CCST-Thesis\thesis\paper-writing-log.md`
- 它必须服从当前冻结版论文结构、章节证据边界和数据集角色口径。

## 本章范围
- 只写：[填写本轮负责的小节，例如 `2.1 -> 2.4`]
- 不启动：[填写明确不在本轮内的章节或小节]
- 本章叙事边界：
  - [填写本章能写什么]
  - [填写本章不能越界写什么]
- 数据集或方法口径：
  - [例如：保持 `Visium HD MouseBrain` 为主线]
  - [例如：不要提前写实验结论]

## 启动前提
- 已具备以下前置条件：
  - [例如：章节素材包已完成]
  - [例如：章节证据映射已稳定]
  - [例如：目标章节已有 LaTeX 骨架或 working draft]
- 如果以下条件不满足，则不要直接执行本计划：
  - [例如：本章边界仍不稳定]
  - [例如：证据尚未整理]
  - [例如：仍处于从零规划阶段]

## 必读材料
- 论文蓝图：
  - `G:\bishe\JLU-CCST-Thesis\thesis\paper-outline.md`
- 证据映射：
  - `G:\bishe\JLU-CCST-Thesis\thesis\paper-evidence-map.md`
- 写作日志：
  - `G:\bishe\JLU-CCST-Thesis\thesis\paper-writing-log.md`
- 本章素材包：
  - [填写本章素材包路径]
- 目标正文文件：
  - [填写 working draft 或 `document.tex` 路径]

## Skill 调用顺序
1. 主流程 skill
- 默认先用 `$doc-coauthoring` 做：
  - 空白起草
  - 小节骨架搭建
  - 分节共写
  - working draft 侧写

2. 局部编辑 skill
- 只有当已经存在草稿、零散段落、实验结果、图表或 caption 需求时，才使用 `$graduation-thesis-editor`。
- 它只负责：
  - 局部润色
  - 缩写 / 扩写
  - 逻辑检查
  - reviewer 视角诊断
  - 实验分析补写
  - 图表标题 / caption
- 可根据需要创建子智能体执行这些局部 editor 任务。
- 这里的“是否创建子智能体”只针对局部 editor 任务本身，不等同于章节结束时的 reader testing。
- 但并不是所有局部 editor 任务都必须拆成子智能体：
  - 如果任务规模不大、修改目标单一、串行处理更稳，允许直接在主线程完成。
  - 只有在以下情况下优先考虑创建子智能体：
    - 需要陌生读者视角
    - 存在可并行拆开的多个局部编辑任务
    - 需要避免主线程上下文污染
- 是否创建子智能体、创建几个子智能体，不必在模板里预先写死，但执行前必须显式判断一次。

3. 可选风格清理
- 只有在本章内容已经稳定后，才可选使用 `$humanizer` 做最终语言去公式化。

4. 明确禁止提前使用的 skill
- 在本章 working draft 未稳定前，不使用 `$academic-paper-composer`。
- 如果本章仍处于蓝图不稳定或证据未冻结阶段，不直接进入章节起草，而应先回到 `$academic-paper-strategist` 或蓝图整理环节。

## 推荐章节微流程
### 阶段 A：建立 working draft 骨架
- 用主流程 skill 创建本章专属 working draft。
- 先明确本章包含哪些一级或二级小节。

### 阶段 B：按小节顺序推进
- 固定写作顺序，不在没有特别说明的情况下跳写。
- 若某个小节证据最复杂，可允许增加迭代轮次，但不随意打乱全章顺序。

### 阶段 C：小节级处理
1. 先由 `$doc-coauthoring` 完成小节草稿。
2. 再对照章节素材包或起草卡做边界检查。
3. 若出现语言、逻辑、实验分析或 caption 层面的局部需求，再切换到 `$graduation-thesis-editor`。
4. 小节通过后继续下一节，不建议边写边并回正式骨架。

### 阶段 D：整章级复核
- 全章草稿完成后，再做一次整章 reviewer 式诊断。
- 只在整章稳定后，才考虑并回正式正文文件。
- 每章完成后，必须显式调用至少 1 个 fresh-reader 子智能体执行 reader testing，这一步是章节收尾必做项，不再采用“按需跳过”的口径。
- 章节级 reader testing 与局部 editor 任务不同：前者固定要求使用子智能体，后者仍然按任务规模判断是否需要子智能体。
- 章节级 reader testing 默认采用“前文连续阅读”模式，而不是默认只读当前章：
  - 若当前为第 1 章，则只读第 1 章。
  - 若当前为第 N 章，则主测试先读已稳定的前置章节，再读第 N 章。
  - 若上下文过长，最低不得少于“上一章 + 当前章”。
  - 若需要额外检查“本章脱离前文时是否也能单独成立”，可追加一次“只读当前章”的补充测试，但这不是默认主测试。
- 章节级 reader testing 至少检查：
  - 本章与前后章节是否发生职责混淆
  - 陌生读者是否会误解本章的方法角色、数据集角色或主张边界
  - 本章是否提前泄露后续章节的实验结论或方法实现
- 若首轮 reader testing 暴露明显误读风险，应先修订，再进行第二轮轻量复测后才允许关闭本章。

### 阶段 E：并回与编译
- 并回时处理正式引用、LaTeX 结构对齐和必要的章节同步。
- 编译只在并回后执行，不把编译当作起草期的默认动作。
- 整篇论文主体起草完成后，必须显式调用子智能体再做一次全文 reader testing。
- 全文 reader testing 重点检查：
  - 跨章节逻辑是否连贯
  - 章节之间是否存在边界回流或结论重复
  - 主线数据集、supporting dataset 与 workflow-support dataset 的口径是否全篇一致
  - 引言、方法、实验、总结之间是否存在前后矛盾或过度主张

## `$graduation-thesis-editor` 调用规则
- 每次调用必须先走该 skill 的全局 route-first 规则。
- 调用前必须先判断该任务是否需要子智能体：
  - 若任务规模不大、不是必须并行拆开的工作，可不调用子智能体。
  - 若任务需要陌生视角、并行诊断或上下文隔离，再创建子智能体。
- 调用前必须明确：
  - `Task goal`
  - `Expected route type`
  - `Route ID / Prompt Source / Prompt Preserved Verbatim`
- 一次调用只允许一个 route。
- 混合请求必须拆成串行两步或多步：
  - “检查并改写” = 先逻辑检查，再润色
  - “分析并润色” = 先实验分析，再润色
  - “reviewer 看一遍并顺手改掉” = 先 reviewer 诊断，再局部改写
- 如果 routing 判断这是空白起草、章节规划或多轮共写任务，必须交还 `$doc-coauthoring`，不能强行套用 editor prompt。

### 常用 route 对照
- 小节润色：
  - `revision / 表达润色（中文论文）`
- 小节逻辑检查：
  - `revision / 逻辑检查`
- 整章 reviewer 诊断：
  - `analysis / 论文整体以 Reviewer 视角进行审视`
- 实验结果分析：
  - `analysis / 实验分析`
- 图标题 / 图 caption：
  - `figures / 生成图的标题`
- 表标题 / 表 caption：
  - `figures / 生成表的标题`

## 推荐提示词模板
### 主起草提示词
```text
Use $doc-coauthoring.

Read first:
- [paper-outline.md 路径]
- [paper-evidence-map.md 路径]
- [paper-writing-log.md 路径]
- [本章素材包路径]
- [目标正文路径]

Task:
- 基于上述材料，起草 [章节 / 小节范围]，并按既定顺序推进。

Rules:
- 只在本章证据边界内写作。
- 不提前展开属于后续章节的方法或实验内容。
- 如 bibliography 尚未冻结，可先使用作者-年份式引用占位。
```

### 局部编辑提示词
```text
Use $graduation-thesis-editor.

Task goal:
- [只写一个局部目标，例如：把这段第2章草稿改成更正式的论文表述]

Expected route type:
- [例如：revision / 表达润色（中文论文）]

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 如果 routing 判断这不是局部编辑任务，就停止强行调用 editor，并改用更合适的主流程 skill。
```

### reviewer 式诊断提示词
```text
Use $graduation-thesis-editor.

Task goal:
- [例如：以 reviewer 视角检查第4.5节实验分析]

Expected route type:
- analysis / 论文整体以 Reviewer 视角进行审视

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 本次调用只做诊断，不顺手改写全文。
```

## 编译规则
- 只有当本章内容已经并回目标正文文件后，才执行编译。
- 编译 recipe：
  - [例如：VS Code LaTeX Workshop `latexmk (xelatex)`]
- 配置来源：
  - [例如：`G:\bishe\JLU-CCST-Thesis\.vscode\settings.json`]
- 输出目录：
  - [例如：`G:\bishe\JLU-CCST-Thesis\thesis\build\`]

## 执行后同步
- 本轮完成后，至少同步：
  - `paper-writing-log.md`
- 如本章证据边界、可写主张或图表落点发生变化，再同步：
  - `paper-evidence-map.md`
- 如正文骨架或章节安排发生调整，再同步：
  - `document.tex`
  - 必要时同步 `paper-outline.md`
- 若本轮已经完成一个完整章节，还应在日志中记录该章的子智能体 reader testing 是否已执行、发现了什么问题、是否完成修订回合。
- 若本轮已经完成一个完整章节，还应在日志中记录该章 reader testing 的读取范围，例如“只读第 1 章”或“上一章 + 当前章”。

## 验收标准
- 本计划的执行范围没有偷偷扩展成整篇论文任务。
- 主起草流程确实由 `$doc-coauthoring` 承担。
- `$graduation-thesis-editor` 只用于局部编辑、分析和诊断。
- 每次 editor 调用都显式报告 route 信息。
- `$humanizer` 仅在章节稳定后作为可选收口工具。
- 未提前误用 `$academic-paper-composer`。
- 本章正文没有越过既定证据边界。
- 本章 working draft 在稳定前不提前并回正式正文。
- 章节关闭前，chapter-end reader testing 的读取范围符合“前文连续阅读优先”的规则。

## 禁止事项
- 不要把章节计划写成整篇论文总计划。
- 不要用 `$graduation-thesis-editor` 代替空白起草。
- 不要把两个 editor prompt 混成一个自定义 prompt。
- 不要在章节草稿还不稳定时提前进入 composer 定稿流程。
