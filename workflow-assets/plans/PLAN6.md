# T-012B 摘要执行计划

## 摘要
- 本计划只服务于摘要与关键词，不扩展到第5章正文、整篇论文定稿、致谢或附录。
- 本轮目标是基于已稳定的第1章到第5章正文、第5章总结素材包和摘要素材包，完成高质量摘要 working draft，并在稳定后并回 `cover.tex`。
- 本计划将摘要明确定位为“贡献说明书（statement of contribution）”，而不是“论文简介”；摘要应在有限篇幅内交代本文解决了什么问题、采用了什么核心思路、形成了什么可成立的贡献判断。
- 本轮主 skill 固定为 `$doc-coauthoring`；已有草稿后的局部诊断、润色或中英转换固定交给 `$graduation-thesis-editor`；仅在末期需要轻微去公式化时才可选 `$humanizer`。
- 落稿策略固定为“先侧写 abstract working draft，再并回前置页模板”；摘要工作草稿固定为 `<private-thesis-repo>\thesis\abstract-working-draft.md`。
- 编译规则固定为 VS Code LaTeX Workshop 的 recipe `latexmk (xelatex)`，严格按 `<private-thesis-repo>\.vscode\settings.json` 执行，输出到 `<private-thesis-repo>\thesis\build\`。

## 计划定位
- 这是一个“摘要专项执行计划”，不是整篇论文总计划。
- 它默认继承：
  - `<private-thesis-repo>\thesis\paper-outline.md`
  - `<private-thesis-repo>\thesis\paper-evidence-map.md`
  - `<private-thesis-repo>\thesis\paper-writing-log.md`
- 它必须服从当前冻结版论文结构、数据集角色口径和结果边界。
- 为避免把摘要写成“凭印象复述”，本计划同时固定读取：
  - `<private-thesis-repo>\文档\参考文献\第五章总结素材包\`
  - `<private-thesis-repo>\文档\参考文献\摘要素材包\`
- `<private-thesis-repo>\文档\如何写论文之摘要篇.pdf` 的核心规则已被吸收进本计划与摘要素材包，后续默认以更新后的 `PLAN6.md + 摘要素材包` 为 authority，不再回退到旧轻量入口。

## 本章范围
- 只写：
  - 中文摘要
  - 中文关键词
  - 英文摘要
  - 英文关键词
- 不启动：
  - 第5章正文重写
  - 整篇论文定稿链路
  - 致谢、附录、封面信息的其他字段
  - 任意正文未出现的新实验结果或新数据集角色
- 本章叙事边界：
  - 摘要只允许压缩研究目标、方法链路、实验组织、稳定结论边界与总体展望。
  - 摘要不得复述第4章结果表，也不得写成第5章的缩略版流水账。
  - 中文摘要的默认起草结构为“背景/任务 -> 科学问题 -> 方法创新 -> 结果与贡献 -> 收束判断”；“五句话原则”仅作为软性起草方法，不机械限制中英摘要必须写成五句。
- 数据集或方法口径：
  - `Visium HD MouseBrain` 始终是唯一主实验线。
  - `Human Ovarian` 始终只作 supporting dataset。
  - `Xenium Ovarian` 与 `Xenium MouseBrain` 始终只作 workflow-support dataset。
  - `EXP-007` 始终只能写成当前最强 candidate，不能写成已 promoted baseline。

## 启动前提
- 已具备以下前置条件：
  - 第1章到第5章正文已经稳定并并回 `document.tex`。
  - 第5章已按 `PLAN5.md` 完成关闭。
  - `<private-thesis-repo>\文档\参考文献\第五章总结素材包\` 已稳定。
  - `<private-thesis-repo>\文档\参考文献\摘要素材包\` 已建立。
  - `<private-thesis-repo>\thesis\cover.tex` 已提供摘要与关键词入口。
- 如果以下条件不满足，则不要直接执行本计划：
  - 第1章到第5章仍处于大范围重写状态。
  - 第5章和摘要的职责再次混淆。
  - 摘要 authority 入口仍只靠旧的轻量笔记，而没有读取 `PLAN6.md + 摘要素材包`。

## 必读材料
- 论文蓝图：
  - `<private-thesis-repo>\thesis\paper-outline.md`
- 证据映射：
  - `<private-thesis-repo>\thesis\paper-evidence-map.md`
- 写作日志：
  - `<private-thesis-repo>\thesis\paper-writing-log.md`
- 第5章素材包：
  - `<private-thesis-repo>\文档\参考文献\第五章总结素材包\README.md`
  - `<private-thesis-repo>\文档\参考文献\第五章总结素材包\正文可写层\摘要联动提示卡.md`
- 摘要素材包：
  - `<private-thesis-repo>\文档\参考文献\摘要素材包\README.md`
  - `<private-thesis-repo>\文档\参考文献\摘要素材包\摘要结构与结果句规则卡.md`
  - `<private-thesis-repo>\文档\参考文献\摘要素材包\摘要事实边界卡.md`
  - `<private-thesis-repo>\文档\参考文献\摘要素材包\摘要压缩顺序卡.md`
  - `<private-thesis-repo>\文档\参考文献\摘要素材包\摘要关键词与中英对齐卡.md`
- 目标正文文件：
  - `<private-thesis-repo>\thesis\abstract-working-draft.md`
  - `<private-thesis-repo>\thesis\cover.tex`
  - `<private-thesis-repo>\thesis\document.tex`
  - `<private-thesis-repo>\thesis\document.bib`

## Skill 调用顺序
1. 主起草流程
- 默认先用 `$doc-coauthoring` 做：
  - 中文摘要骨架搭建
  - 研究问题、方法链路、实验组织、稳定结论边界的压缩
  - 中文关键词初稿整理

2. 局部编辑流程
- 只有当已经存在摘要草稿后，才使用 `$graduation-thesis-editor`。
- 它只负责：
  - 中文摘要局部润色
  - 中文摘要逻辑检查
  - 英文摘要等义转换与局部修订
  - reviewer 视角检查摘要是否越界
- 英文摘要也必须建立在已有中文摘要之上，不允许跳过中文摘要直接自由生成英文版。

3. 可选风格清理
- 只有在中英文摘要都稳定后，才可选使用 `$humanizer` 对中文摘要做非常轻量的去公式化处理。

4. 明确禁止提前使用的 skill
- 在摘要未稳定前，不使用 `$academic-paper-composer`。
- 如果摘要边界或数据集角色再次发生漂移，不直接继续润色，而应先回到本计划和摘要素材包重新校准。

## 推荐章节微流程
### 阶段 A：建立摘要 working draft 骨架
- 用主流程 skill 维护 `<private-thesis-repo>\thesis\abstract-working-draft.md`。
- 先固定骨架：
  - `## 中文摘要`
  - `## 中文关键词`
  - `## English Abstract`
  - `## English Keywords`

### 阶段 B：先写中文摘要
1. 先按 `摘要结构与结果句规则卡.md` 确定“背景/任务 -> 科学问题 -> 方法创新 -> 结果与贡献 -> 收束判断”的闭环结构。
2. 再按 `摘要压缩顺序卡.md` 压缩正文事实，生成中文摘要草稿。
3. 对照 `摘要事实边界卡.md` 检查是否越界，并确认“科学问题”优先描述结构性困难，而不是只停留在经验现象。
4. 检查结果句是否以适度具体的事实锚点回应前文问题，禁止只写空泛的“显著提升”。
5. 如有必要，再调用 `$graduation-thesis-editor` 做中文摘要局部逻辑检查或论文表述润色。

### 阶段 C：再写关键词
- 中文关键词优先从正文主线、方法主线和实验主线中抽取，不堆叠细节参数名。
- 英文关键词必须与中文关键词一一对应，不额外扩展新术语。

### 阶段 D：最后写英文摘要
- 以中文摘要为唯一语义源完成英文摘要。
- 英文摘要完成后，必须对照 `摘要关键词与中英对齐卡.md` 检查：
  - 数据集角色层级是否一致
  - 结论强度是否放大
  - `EXP-007` 是否被错误写成 promoted baseline
  - 结果句是否比中文摘要更“敢写”或更具体

### 阶段 E：摘要 reviewer 式诊断
- 中英文摘要稳定后，必须做一次 reviewer 式诊断。
- 检查重点：
  - 摘要是否重述正文而非新增正文外内容
  - 是否破坏数据集角色层级
  - 是否把 `EXP-007` 写成定案
  - 英文摘要是否比中文摘要更“敢写”
- 摘要完成后，必须执行一次reader testing，读取当前摘要额外检查“首次阅读摘要是否也能单独成立没有错误“，若首轮 reader testing 暴露明显误读风险，应先修订，再进行第二轮轻量复测后才允许关闭摘要。

### 阶段 E：并回与编译

### 阶段 F：并回与编译
- 摘要稳定后，并回 `<private-thesis-repo>\thesis\cover.tex`。
- 编译只在并回 `cover.tex` 后执行。
- 如需全文一致性核读，应在摘要并回后再执行，而不是在 working draft 状态就宣称关闭。

## `$graduation-thesis-editor` 调用规则
- 每次调用必须先走该 skill 的全局 route-first 规则。
- 调用前必须明确：
  - `Task goal`
  - `Expected route type`
  - `Route ID / Prompt Source / Prompt Preserved Verbatim`
- 一次调用只允许一个 route。
- 混合请求必须拆成串行步骤：
  - “检查摘要并润色” = 先 reviewer / logic check，再润色
  - “写英文并顺手改中文” = 先英文等义转换，再单独润色中文
- 如果 routing 判断这是 blank-page 规划任务，应交还 `$doc-coauthoring`。

## 推荐提示词模板
### 摘要主起草提示词
```text
Use $doc-coauthoring.

Read first:
- <private-thesis-repo>\文档\参考文献\写作计划\PLAN6.md
- <private-thesis-repo>\thesis\paper-outline.md
- <private-thesis-repo>\thesis\paper-evidence-map.md
- <private-thesis-repo>\thesis\paper-writing-log.md
- <private-thesis-repo>\文档\参考文献\第五章总结素材包\README.md
- <private-thesis-repo>\文档\参考文献\第五章总结素材包\正文可写层\摘要联动提示卡.md
- <private-thesis-repo>\文档\参考文献\摘要素材包\README.md
- <private-thesis-repo>\文档\参考文献\摘要素材包\摘要结构与结果句规则卡.md
- <private-thesis-repo>\文档\参考文献\摘要素材包\摘要事实边界卡.md
- <private-thesis-repo>\文档\参考文献\摘要素材包\摘要压缩顺序卡.md
- <private-thesis-repo>\文档\参考文献\摘要素材包\摘要关键词与中英对齐卡.md
- <private-thesis-repo>\thesis\document.tex
- <private-thesis-repo>\thesis\cover.tex

Task:
- 基于上述材料，先完成高质量中文摘要，再整理中英文关键词，最后基于中文摘要生成英文摘要。

Rules:
- 把摘要写成 contribution statement，而不是论文简介。
- 中文摘要优先按“背景/任务 -> 科学问题 -> 方法创新 -> 结果与贡献 -> 收束判断”闭环组织；五句话原则只作为软性起草方法。
- 科学问题优先写结构性困难，不只写经验现象。
- 结果句必须回扣前文问题，采用适度具体策略，可保留“五项指标评价链、14组实验、stage2 高杠杆方向、EXP-007 为最强 candidate 但仍有风险”等事实锚点，但不要强塞细粒度数值。
- 只允许重述正文已经稳定的内容，不新增正文外结论。
- 保持 `Visium HD MouseBrain` 为唯一主实验线，`Human Ovarian` 为 supporting dataset，两个 Xenium 为 workflow-support dataset。
- `EXP-007` 只能写成当前最强 candidate，不能写成已 promoted baseline。
- 英文摘要必须以后定的中文摘要为唯一语义源。
```

### 摘要 reviewer 诊断提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 以 reviewer 视角检查当前摘要（中英双语）是否越界、是否放大结论、是否破坏数据集角色层级。

Expected route type:
- analysis / 论文整体以 Reviewer 视角进行审视

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 本次调用只做诊断，不顺手整体重写摘要。
```

### 英文摘要局部修订提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 在不新增事实、不放大结论的前提下，把当前英文摘要调整为更自然的学术英文表达。

Expected route type:
- revision / 表达润色（中文论文）

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 如果 routing 判断当前任务更适合翻译类 route，则按 routing 结果执行，不强行混入中文摘要改写。
```

## 编译规则
- 只有当摘要已经并回 `cover.tex` 后，才执行编译。
- 编译 recipe：
  - VS Code LaTeX Workshop `latexmk (xelatex)`
- 配置来源：
  - `<private-thesis-repo>\.vscode\settings.json`
- 输出目录：
  - `<private-thesis-repo>\thesis\build\`

## 执行后同步
- 本轮完成后，至少同步：
  - `<private-thesis-repo>\thesis\paper-writing-log.md`
- 若摘要 authority、关键词口径或摘要证据入口发生变化，再同步：
  - `<private-thesis-repo>\thesis\paper-evidence-map.md`
  - `<private-thesis-repo>\thesis\paper-outline.md`
- 若摘要正式并回前置页，再同步：
  - `<private-thesis-repo>\thesis\cover.tex`

## 验收标准
- `PLAN6.md` 已按 `PLAN_TEMPLATE.md` 的结构创建，而不是轻量笔记式入口。
- 摘要 authority 已显式迁移到 `写作计划/PLAN6.md + 摘要素材包/`。
- `PLAN6.md` 能明确回答：摘要是什么、按什么闭环起草、结果句如何适度具体、以及结果句必须如何回扣前文问题。
- 中文摘要、英文摘要和关键词没有超出正文证据边界。
- `Visium HD MouseBrain` / `Human Ovarian` / Xenium 的角色层级在中英摘要中保持一致。
- `EXP-007` 没有被写成已 promoted baseline。
- 摘要稳定后，已并回 `cover.tex` 并可编译。

## 禁止事项
- 不要把摘要写成“论文简介”或“章节目录压缩版”。
- 不要把摘要当作“比正文更敢写”的结论浓缩。
- 不要跳过中文摘要，直接生成独立英文摘要。
- 不要把第4章结果表、细节统计或图像讨论直接拼进摘要。
- 不要只靠 `thesis/abstract-light-entry.md` 回忆摘要规则；后续以 `PLAN6.md + 摘要素材包` 为准。
