# T-008 第二章执行计划

## 摘要
- 本计划只服务于第2章，不扩展到第3章到第5章正文。
- 本轮目标是完成第2章 `2.1 -> 2.2 -> 2.3.1 -> 2.3.2 -> 2.3.3 -> 2.4` 的 working draft，并在稳定后再并回 `document.tex`。
- 主流程为 `$doc-coauthoring`，局部编辑为 `$graduation-thesis-editor`；编译仍按 VS Code LaTeX Workshop 的 recipe `latexmk (xelatex)` 与 `.vscode/settings.json` 执行。
- 落稿策略固定为“先侧写 working draft，再并回正式骨架”，不直接在 `document.tex` 中边写边改。

## 计划定位
- 这是“第二章专项计划”，不是整篇论文总计划。
- 本计划默认继承以下长期记忆文档：
  - `<your-thesis-repo>\thesis\paper-outline.md`
  - `<your-thesis-repo>\thesis\paper-evidence-map.md`
  - `<your-thesis-repo>\thesis\paper-writing-log.md`
- 本计划同时继承 `plan_skill.md` 与 `plan_skill2.md` 中已经稳定的主链路：
  - `academic-paper-strategist -> doc-coauthoring -> graduation-thesis-editor -> academic-paper-composer`
- 但在本轮明确固定：
  - 不重新调用 `$academic-paper-strategist`
  - 不进入 `$academic-paper-composer`

## 本章范围
- 只写：
  - `2.1 空间转录组技术概述`
  - `2.2 Visium HD 数据特点与细胞分割难点`
  - `2.3.1 Watershed 方法`
  - `2.3.2 Cellpose 方法`
  - `2.3.3 StarDist 方法`
  - `2.4 本章小结`
- 不启动：
  - 第3章方法实现
  - 第4章实验结果
  - 任何 `SMURF` 独立小节
- 本章叙事边界：
  - `2.1` 只写空间转录组概念、主流技术路线和技术意义。
  - `2.2` 只写 Visium HD 平台特点、规则 bin 与真实细胞边界不一致，以及为什么需要 segmentation、custom binning 和 cell reconstruction。
  - `2.3.1` 与 `2.3.2` 只写基础方法背景，不写成本文实际执行模块。
  - `2.3.3` 可以写 StarDist 与本文后续 `stage0` 初始分割的联系，但不能把它写成贯穿全文所有阶段的方法。
  - `2.4` 只做技术背景收束，不提前给出实验优劣判断。
- 禁写点：
  - 不写未核实的平台商业规格。
  - 不写“每个 bin 都天然对应一个细胞”。
  - 不把特定数据集经验写成所有 Visium HD 数据的通用规律。
  - 不无文献支撑地比较 Watershed、Cellpose、StarDist 的绝对优劣。
  - 不提前写第3章工程流程和第4章实验结论。
- 数据与方法口径：
  - 第2章不单开 `SMURF` 小节。
  - 只有 `2.3.3` 可以自然过渡到第3章的 `stage0` 初始分割环节。
  - 评价指标定义仍然只放在第3章 `3.5`，第2章不提前展开。

## 启动前提
- 已满足：
  - 第2章文献素材包已完成。
  - 第2章 evidence 已稳定登记在 `paper-evidence-map.md`。
  - `document.tex` 中已有第2章骨架。
  - 第1章已完成，便于保持第1章到第2章的叙事衔接。
- 若以下条件不满足，则不应直接执行本计划：
  - 第2章边界再次摇摆。
  - 文献素材包路径失效。
  - 第3章与第2章职责重新混淆。

## 必读材料
- 论文蓝图：
  - `<your-thesis-repo>\thesis\paper-outline.md`
- 证据映射：
  - `<your-thesis-repo>\thesis\paper-evidence-map.md`
- 写作日志：
  - `<your-thesis-repo>\thesis\paper-writing-log.md`
- 第2章素材包：
  - `<your-thesis-repo>\文档\参考文献\第二章文献素材包\README.md`
  - `<your-thesis-repo>\文档\参考文献\第二章文献素材包\第二章文献目录.md`
  - `<your-thesis-repo>\文档\参考文献\第二章文献素材包\第二章分节起草卡.md`
- 目标正文：
  - `<your-thesis-repo>\thesis\document.tex`
  - `<your-thesis-repo>\thesis\document.bib`

## Skill 调用顺序
1. 主起草流程
- 用 `$doc-coauthoring` 创建：
  - `<your-thesis-repo>\thesis\chapter2-working-draft.md`
- 固定起草顺序为：
  - `2.1`
  - `2.2`
  - `2.3.1`
  - `2.3.2`
  - `2.3.3`
  - `2.4`

2. 第二章写作硬约束
- `2.1` 只保持在技术概述与路线比较层面。
- `2.2` 只写 Visium HD 平台特点与细胞级难点，不写具体实验结果。
- `2.3.1` 不把 Watershed 写成本文实际执行模块。
- `2.3.2` 不把 Cellpose 写成本文代码已集成模块。
- `2.3.3` 只说明 StarDist 与初始分割阶段的直接联系，不把它写成贯穿全文所有阶段的方法。
- `2.4` 只做本章小结，不提前评价实验优劣。

3. 局部编辑流程
- 当某个小节已经有草稿后，才允许用 `$graduation-thesis-editor` 做：
  - 局部润色
  - 逻辑检查
  - reviewer 视角诊断
- 常见 route 固定为：
  - `revision / 表达润色（中文论文）`
  - `revision / 逻辑检查`
  - `analysis / 论文整体以 Reviewer 视角进行审视`
- 可根据需要创建子智能体执行这些局部 editor 任务。
- 这里的“是否创建子智能体”只针对局部 editor 任务本身，不等同于章节完成后的 reader testing。
- 但并不是每次局部 editor 任务都必须创建子智能体：
  - 如果任务规模不大、目标单一、串行处理更稳，可以直接在主线程完成。
  - 如果任务需要陌生读者视角、可并行拆开的多个局部任务，或需要避免主线程上下文污染，再优先考虑创建子智能体。
- 是否创建子智能体、创建几个子智能体，由当时的任务拆分复杂度决定，但执行前必须显式判断一次。

4. 可选风格清理
- 只有整章已经稳定之后，才可选使用 `$humanizer` 做局部语言去公式化。

5. 禁止提前进入的流程
- 本计划中不使用 `$academic-paper-composer`。
- 本计划默认不重新调用 `$academic-paper-strategist`；只有在第2章边界或证据发生实质变化时，才允许回到 strategist。

## 分阶段执行流程
### 阶段 A：建立第2章 working draft 骨架
- 用 `$doc-coauthoring` 创建 `chapter2-working-draft.md`。
- 固定六个小节骨架：
  - `2.1 空间转录组技术概述`
  - `2.2 Visium HD 数据特点与细胞分割难点`
  - `2.3.1 Watershed 方法`
  - `2.3.2 Cellpose 方法`
  - `2.3.3 StarDist 方法`
  - `2.4 本章小结`

### 阶段 B：按小节顺序推进
- 不跳序推进，保持与 `paper-writing-log.md`、`document.tex` 和后续日志同步一致。
- 默认允许 `2.2` 和 `2.3.3` 投入更多迭代轮次，因为它们最容易与第3章职责发生混淆。

### 阶段 C：每个小节的固定微流程
1. 用 `$doc-coauthoring` 先完成该节的“要点筛选 + 小节草稿”。
2. 草稿完成后，立刻对照 `第二章分节起草卡.md` 做边界检查。
3. 若该节存在以下问题，再调用 `$graduation-thesis-editor`：
   - 语言重复
   - 逻辑跳跃
   - 方法角色表达不清
   - StarDist 与后续流程关系写得过重或过散
   - 存在章节边界越界风险
4. 小节通过后继续下一节，不立刻并回 `document.tex`。

### 阶段 D：整章级复核
- 六节都完成后，再调用一次 `$graduation-thesis-editor` 做整章 reviewer 式检查。
- 重点检查：
  - `2.2` 是否与第3章 `3.1` 的流程描述发生混淆
  - 读者是否会误以为 Watershed 或 Cellpose 是本文实际执行模块
  - 读者是否会误以为 StarDist 贯穿全文所有阶段
  - 全章是否提前泄露第4章实验优劣判断
- 第二章完成后，必须显式调用至少 1 个 fresh-reader 子智能体执行 reader testing。
- 这一轮 chapter-end reader testing 是本计划的强制步骤，不再采用“只判断是否需要”的口径。
- 第二章主测试默认采用“前文连续阅读”模式：fresh reader 先读第1章，再读第2章，而不是默认只读第2章。
- 若上下文控制或专项检查需要，也可追加一次“只读第2章”的补充测试，用于判断本章脱离前文时的自洽性；但这不是默认主测试。
- 第二章 reader testing 重点检查：
  - `2.2` 与 `3.1` 的边界是否仍然混淆
  - 读者是否会误以为 Watershed 或 Cellpose 是本文实际执行模块
  - 读者是否会误以为 StarDist 贯穿全文所有阶段
  - 读者是否会把第2章误读成已经包含第4章实验结论
- 若 reader testing 暴露明显误读风险，应先修订，再进行一次轻量复测后才允许关闭第2章。

### 阶段 E：并回正式 LaTeX 骨架
- 只有在整章 working draft 稳定后，才一次性并回 `<your-thesis-repo>\thesis\document.tex`。
- 并回时优先复用 `document.bib` 中已存在条目，不重复灌入第1章已经使用过的空间转录组综述文献。
- `document.bib` 只补“第2章最终实际新增用到”的条目，例如：
  - Watershed 经典文献
  - Cellpose 核心文献
  - StarDist 2D / 3D 文献
  - 如正文直接使用 10x 官方网页材料，则补真实网页引用信息；若只作为内部核对材料，则不强制写入 `.bib`
- 编译规则与 `PLAN1` 相同：VS Code LaTeX Workshop `latexmk (xelatex)`，输出到 `<your-thesis-repo>\thesis\build\`。

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
- 如果 routing 判断当前任务不是“已有草稿后的局部编辑任务”，必须停止强行使用 editor，并交回 `$doc-coauthoring`。
- 混合请求必须拆开，不能在一次调用里同时做“检查 + 改写”。

### 2.2 小节润色提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 把第2章 `2.2 Visium HD 数据特点与细胞分割难点` 的现有草稿改成更正式的中文毕业论文表述，但不改变主张与证据边界。

Expected route type:
- revision / 表达润色（中文论文）

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 如果 routing 判断这不是局部编辑任务，就不要强行套 editor，而应交还给 $doc-coauthoring。
- 不要在这次调用中顺手做逻辑检查或 reviewer 诊断。
```

### 2.3.3 小节逻辑检查提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 检查第2章 `2.3.3 StarDist 方法` 当前草稿是否把 StarDist 写得过重、是否与第3章后续流程角色发生混淆。

Expected route type:
- revision / 逻辑检查

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 本次调用只做诊断，不同时做润色改写。
```

### 第二章 reviewer 式整章检查提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 以毕业论文 reviewer 的视角检查第2章整章草稿，逐节指出具体问题。

Expected route type:
- analysis / 论文整体以 Reviewer 视角进行审视

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 本次调用只做 reviewer 式诊断，不顺手整体重写全文。
```

## 推荐提示词
### 第二章主起草提示词
```text
Use $doc-coauthoring.

Read first:
- <your-thesis-repo>\文档\参考文献\写作计划\PLAN2.md
- <your-thesis-repo>\thesis\paper-outline.md
- <your-thesis-repo>\thesis\paper-evidence-map.md
- <your-thesis-repo>\thesis\paper-writing-log.md
- <your-thesis-repo>\文档\参考文献\第二章文献素材包\README.md
- <your-thesis-repo>\文档\参考文献\第二章文献素材包\第二章文献目录.md
- <your-thesis-repo>\文档\参考文献\第二章文献素材包\第二章分节起草卡.md
- <your-thesis-repo>\thesis\document.tex
- <your-thesis-repo>\thesis\document.bib

Task:
创建 `<your-thesis-repo>\thesis\chapter2-working-draft.md`，并按 `2.1 -> 2.2 -> 2.3.1 -> 2.3.2 -> 2.3.3 -> 2.4` 的顺序共写第2章。

Rules:
- `2.1` 只写空间转录组概述与技术路线。
- `2.2` 只写 Visium HD 特点与细胞级难点。
- `2.3.1` 和 `2.3.2` 不写成本文实际模块。
- `2.3.3` 可自然过渡到第3章 `stage0` 初始分割。
- `2.4` 只做本章收束。
- 不提前展开第3章工程流程和第4章实验结果。
- 如 bibliography 尚未冻结，只补本章实际新增用到的引用条目。
```

## 编译规则
- 只有在第2章 working draft 已经并回 `<your-thesis-repo>\thesis\document.tex` 后，才执行编译。
- 编译 recipe：
  - VS Code LaTeX Workshop `latexmk (xelatex)`
- 配置来源：
  - `<your-thesis-repo>\.vscode\settings.json`
- 输出目录：
  - `<your-thesis-repo>\thesis\build\`

## 执行后同步
- 完成第2章 working draft 后，至少同步：
  - `<your-thesis-repo>\thesis\paper-writing-log.md`
- 如第2章正文已经并回正式骨架，再同步：
  - `<your-thesis-repo>\thesis\document.tex`
  - `<your-thesis-repo>\thesis\document.bib`
- 如第2章边界、可写主张或图表落点发生变化，再同步：
  - `<your-thesis-repo>\thesis\paper-evidence-map.md`
- 第2章完成后，必须在日志中登记子智能体 reader testing 是否已执行、发现的问题和是否完成修订闭环。
- 第2章完成后，必须在日志中登记本轮 reader testing 的读取范围，默认应写明“第1章 + 第2章”。
- 整篇论文完成后，必须显式调用子智能体再做一次全文 reader testing，而不是按需决定是否执行。

## 验收标准
- `PLAN2.md` 内容完整对齐模板与 `PLAN1` 风格。
- `chapter2-working-draft.md` 被规划为唯一工作草稿文件。
- `2.1` 至少稳定使用 4 篇核心综述/路线文献。
- `2.2` 明确使用 Visium HD 平台材料与分割难点文献，且不写成数据集实验结论。
- `2.3.1` 不把 Watershed 写成本文实际执行模块。
- `2.3.2` 不把 Cellpose 写成本文代码已集成模块。
- `2.3.3` 明确只有初始区域生成与 StarDist 直接衔接。
- `2.4` 不提前评价实验优劣。
- 每次 `$graduation-thesis-editor` 调用都显式报告 route 信息。
- 第2章关闭前已经显式完成至少 1 轮子智能体 reader testing。
- 第2章关闭前，chapter-end reader testing 已按“第1章 + 第2章”为默认主测试范围执行并记录。
- 只有整章稳定后，才允许把第2章并回 `document.tex`。
- `document.bib` 只在并回阶段补本章实际新增使用条目。

## 禁止事项
- 不要把 `PLAN2.md` 当作整篇论文的总计划。
- 不要用 `$graduation-thesis-editor` 代替第2章空白起草。
- 不要把两个 editor prompt 混成一次调用。
- 不要在第2章草稿还不稳定时提前进入 `$academic-paper-composer`。

