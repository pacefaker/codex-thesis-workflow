# T-007 第一章执行计划

## 摘要
- 本计划只服务于第1章，不扩展到第2章到第5章正文。
- 本轮目标是完成第1章 `1.1 -> 1.2 -> 1.3 -> 1.4` 的 working draft，并在稳定后再并回 `document.tex`。
- 主流程仍然是 `$doc-coauthoring`，这一点和之前保持一致。
- `$graduation-thesis-editor` 仍然只承担局部编辑、逻辑检查和 reviewer 诊断；这次唯一实质增强的是加入了全局 route-first 调用规则。
- 编译方式固定为 VS Code LaTeX Workshop 的 recipe `latexmk (xelatex)`，并严格按照 `<your-thesis-repo>/.vscode/settings.json` 中现有 `.vscode/settings.json` 配置执行；输出目录遵循 `latex-workshop.latex.outDir = "./build"`，即 `<your-thesis-repo>\thesis\build\`。
- 落稿策略固定为“先侧写 working draft，再并回 `document.tex`”，不直接在正式骨架里边写边改。

## 计划定位
- 这是“第一章专项计划”，不是整篇论文总计划。
- 本计划默认继承以下长期记忆文档：
  - `<your-thesis-repo>\thesis\paper-outline.md`
  - `<your-thesis-repo>\thesis\paper-evidence-map.md`
  - `<your-thesis-repo>\thesis\paper-writing-log.md`

## 本章范围
- 只写：
  - `1.1 研究背景与意义`
  - `1.2 国内外研究现状`
  - `1.3 本文主要研究内容`
  - `1.4 论文结构安排`
- 不启动：
  - 第2章到第5章正文起草
  - 摘要、关键词、定稿链路
- 本章叙事边界：
  - 围绕空间转录组背景、研究现状、本文工作定位和论文结构安排展开
  - 不提前展开第2章的方法细节
  - 不提前写实验结果
- 数据集角色口径：
  - `Visium HD MouseBrain` 为主线
  - `Human Ovarian` 只作 supporting dataset
  - `Xenium Ovarian` 与 `Xenium MouseBrain` 只作 workflow support

## 启动前提
- 已满足：
  - 第一章引言素材包已就绪
  - 论文目录与章节证据边界已冻结
  - `document.tex` 中已有第1章骨架
- 如以下条件不满足，则不应强行启动正文起草：
  - 第一章素材包缺失
  - 第1章边界仍不稳定
  - 主数据集角色口径仍在摇摆

## 必读材料
- 论文蓝图：
  - `<your-thesis-repo>\thesis\paper-outline.md`
- 证据映射：
  - `<your-thesis-repo>\thesis\paper-evidence-map.md`
- 写作日志：
  - `<your-thesis-repo>\thesis\paper-writing-log.md`
- 第一章素材包：
  - `<your-thesis-repo>\文档\参考文献\第一章引言素材包\README.md`
  - `<your-thesis-repo>\文档\参考文献\第一章引言素材包\第一章研究现状目录.md`
  - `<your-thesis-repo>\文档\参考文献\第一章引言素材包\第一章分节起草卡.md`
- 目标正文：
  - `<your-thesis-repo>\thesis\document.tex`

## Skill 调用顺序
1. 主起草流程
- 用 `$doc-coauthoring` 创建：
  - `<your-thesis-repo>\thesis\chapter1-working-draft.md`
- 然后按以下顺序推进：
  - `1.1`
  - `1.2`
  - `1.3`
  - `1.4`

2. 第一章写作硬约束
- `1.2` 只保持在研究现状层面，不展开 Watershed、Cellpose、StarDist 的方法细节。
- 第1章不写实验结果。
- `1.3` 必须保持四数据集层级口径稳定。
- `1.4` 只说明论文结构安排，不偷塞实验结论。

3. 局部编辑流程
- 当某个小节已经有草稿后，才允许用 `$graduation-thesis-editor` 做：
  - 局部润色
  - 逻辑检查
  - reviewer 视角诊断
- 可根据需要创建子智能体执行这些局部 editor 任务。
- 这里的“是否创建子智能体”只针对局部 editor 任务本身，不等同于章节完成后的 reader testing。
- 但并不是每次局部 editor 任务都必须创建子智能体：
  - 如果任务规模不大、目标单一、串行处理更稳，可以直接在主线程完成。
  - 如果任务需要陌生读者视角、可并行拆开的多个局部任务，或需要避免主线程上下文污染，再优先考虑创建子智能体。
- 是否创建子智能体、创建几个子智能体，由当时的任务拆分复杂度决定，但执行前必须显式判断一次，不在本计划里提前写死。

4. 可选风格清理
- 只有整章已经稳定之后，才可选使用 `$humanizer` 做局部语言去公式化。

5. 禁止提前进入的流程
- 本计划中不使用 `$academic-paper-composer`。

6. 默认不再调用的 skill
- 本计划默认不再调用 `$academic-paper-strategist`，这个 skill 默认放在“第1章到第5章 working draft 都稳定之后”的定稿收口阶段使用，而不是作为第1章启动阶段的主 skill。
- 只有在以下情况发生时，才允许回到 strategist：
  - 第1章结构发生改动
  - 四数据集角色口径发生变化
  - 第一章新增了会影响叙事边界的重要证据

## 分阶段执行流程
### 阶段 A：建立第1章 working draft 骨架
- 用 `$doc-coauthoring` 创建 `chapter1-working-draft.md`。
- 固定四个一级部分：
  - `1.1 研究背景与意义`
  - `1.2 国内外研究现状`
  - `1.3 本文主要研究内容`
  - `1.4 论文结构安排`

### 阶段 B：按小节顺序推进
- 实际起草顺序固定为：
  - `1.1`
  - `1.2`
  - `1.3`
  - `1.4`
- 虽然 `1.2` 最难，但仍不跳序，保证与 `paper-writing-log.md`、`document.tex` 和后续日志同步一致。
- `1.2` 允许投入最多迭代轮次。
- `1.4` 应当最后一次成稿。

### 阶段 C：每个小节的固定微流程
1. 用 `$doc-coauthoring` 先完成该节的“要点筛选 + 小节草稿”。
2. 草稿完成后，立刻对照 `第一章分节起草卡.md` 做边界检查。
3. 若该节存在以下问题，再调用 `$graduation-thesis-editor`：
   - 语言重复
   - 逻辑跳跃
   - 过度像综述摘要
   - 存在章节边界越界风险
4. 小节通过后继续下一个小节，不立刻并回 `document.tex`。

### 阶段 D：整章级复核
- 四节都完成后，再调用一次 `$graduation-thesis-editor` 做整章 reviewer 式检查。
- 重点检查：
  - `1.2` 是否提前展开了第2章的方法细节
  - `1.3` 是否破坏了 “Visium 主线 / Human Ovarian supporting / 两个 Xenium workflow support” 的口径
  - `1.4` 是否提前塞入实验结论
  - 全章是否把工程实现写成原创理论算法
- 第1章完成后，必须显式调用至少 1 个 fresh-reader 子智能体执行 reader testing。
- 这一轮 chapter-end reader testing 是本计划的强制步骤，不再采用“只判断是否需要”的口径。
- 第1章是“前文连续阅读”规则的特例：由于不存在更早章节，本轮主测试固定为“只读第1章”。
- 若后续需要额外检查“第1章脱离目录说明时是否也足够自洽”，可在主测试之外再补做一次更换 reader 的复测；但默认不要求额外扩展输入范围。
- 第1章 reader testing 重点检查：
  - `1.2` 是否让陌生读者误以为第2章方法细节已经展开
  - `1.3` 是否让陌生读者误以为四个数据集承担并列主实验角色
  - `1.4` 是否提前泄露实验结果或过度承诺后文结论
  - 全章是否把工程化流程误读为原创理论算法
- 若 reader testing 发现明显误读风险，应先修订，再进行一次轻量复测后才允许关闭第1章。

### 阶段 E：并回正式 LaTeX 骨架
- 只有在整章 working draft 稳定后，才一次性并回 `<your-thesis-repo>\thesis\document.tex`。
- 并回时再把作者-年份式引用占位转换成正式 LaTeX 引用形式。
- `document.bib` 只补“第1章最终实际用到”的条目，不提前批量灌入所有候选文献。

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

### 1.2 小节润色提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 把第1章 `1.2 国内外研究现状` 的现有草稿改成更正式的中文毕业论文表述，但不改变主张与证据边界。

Expected route type:
- revision / 表达润色（中文论文）

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 如果 routing 判断这不是局部编辑任务，就不要强行套 editor，而应交还给 $doc-coauthoring。
- 不要在这次调用中顺手做逻辑检查或 reviewer 诊断。
```

### 1.2 小节逻辑检查提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 检查第1章 `1.2 国内外研究现状` 当前草稿是否存在逻辑跳跃、无支撑主张或章节边界越界问题。

Expected route type:
- revision / 逻辑检查

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 本次调用只做诊断，不同时做润色改写。
```

### 第一章 reviewer 式整章检查提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 以毕业论文 reviewer 的视角检查第1章整章草稿，逐节指出具体问题。

Expected route type:
- analysis / 论文整体以 Reviewer 视角进行审视

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 本次调用只做 reviewer 式诊断，不顺手整体重写全文。
```

## 推荐提示词
### 第一章主起草提示词
```text
Use $doc-coauthoring.

Read first:
- <your-thesis-repo>\thesis\paper-outline.md
- <your-thesis-repo>\thesis\paper-evidence-map.md
- <your-thesis-repo>\thesis\paper-writing-log.md
- <your-thesis-repo>\文档\参考文献\第一章引言素材包\README.md
- <your-thesis-repo>\文档\参考文献\第一章引言素材包\第一章研究现状目录.md
- <your-thesis-repo>\文档\参考文献\第一章引言素材包\第一章分节起草卡.md
- <your-thesis-repo>\thesis\document.tex

Task:
创建 `<your-thesis-repo>\thesis\chapter1-working-draft.md`，并按 `1.1 -> 1.2 -> 1.3 -> 1.4` 的顺序共写第1章。

Rules:
- `1.2` 只保持在研究现状层面。
- 不展开 Watershed / Cellpose / StarDist 的方法细节。
- 不在第1章写实验结果。
- 叙事中心保持在 `Visium HD MouseBrain`。
- `Human Ovarian` 仅作 supporting。
- 两个 Xenium 数据集仅作 workflow-support。
- 如 bibliography 尚未冻结，可先使用作者-年份式引用占位。
```

## 编译规则
- 只有在第1章 working draft 已经并回 `<your-thesis-repo>\thesis\document.tex` 后，才执行编译。
- 编译 recipe：
  - VS Code LaTeX Workshop `latexmk (xelatex)`
- 配置来源：
  - `<your-thesis-repo>\.vscode\settings.json`
- 输出目录：
  - `<your-thesis-repo>\thesis\build\`

## 执行后同步
- 完成第1章 working draft 后，至少同步：
  - `<your-thesis-repo>\thesis\paper-writing-log.md`
- 如果第1章可写主张、引用边界或图表落点有变化，再同步：
  - `<your-thesis-repo>\thesis\paper-evidence-map.md`
- 如果第1章正文已经并回正式骨架，再同步：
  - `<your-thesis-repo>\thesis\document.tex`
- 第1章完成后，必须在日志中登记子智能体 reader testing 是否已执行、发现的问题和是否完成修订闭环。
- 第1章完成后，必须在日志中登记本轮 reader testing 的读取范围为“只读第1章”。
- 整篇论文完成后，必须显式调用子智能体再做一次全文 reader testing，而不是按需决定是否执行。

## 验收标准
- `chapter1-working-draft.md` 已生成，并覆盖 `1.1` 到 `1.4`。
- `chapter1-working-draft.md` 在整章稳定前不提前并回 `document.tex`。
- `1.1` 至少稳定使用 4 篇核心背景文献。
- `1.2` 至少稳定使用 6 篇研究现状文献，且包含至少 1 篇中文综述。
- `1.2` 没有展开第2章的方法细节。
- `1.3` 保持 `Visium 主线 / Human Ovarian supporting / 两个 Xenium workflow support` 的稳定口径。
- `1.4` 只说明论文结构安排，不提前评价实验结果。
- 每次 `$graduation-thesis-editor` 调用都显式报告 route 信息。
- 第1章关闭前已经显式完成至少 1 轮子智能体 reader testing。
- 第1章关闭前，chapter-end reader testing 已按“只读第1章”的范围执行并记录。
- 只有 reviewer 式整章检查通过后，才允许把第1章并回 `document.tex`。
- `document.bib` 只在并回阶段补实际使用条目。

## 禁止事项
- 不要把 `PLAN1.md` 当作整篇论文的总计划。
- 不要用 `$graduation-thesis-editor` 代替第1章空白起草。
- 不要把两个 editor prompt 混成一次调用。
- 不要在第1章草稿还不稳定时提前进入 `$academic-paper-composer`。

