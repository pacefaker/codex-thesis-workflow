# T-012A 第五章总结与展望执行计划

## 摘要
- 本计划只服务于第5章正文，不扩展到摘要、全文 reader testing、整篇论文定稿或致谢等后续部分。
- 本轮目标是基于第5章总结素材包的 `README.md + 正文可写层/`，完成第5章双节结构：
  - `5.1 全文总结`
  - `5.2 研究展望`
- 主流程固定为 `$doc-coauthoring`，局部编辑固定为 `$graduation-thesis-editor`，可选末期使用 `$humanizer`；不重新调用 `$academic-paper-strategist`，不进入 `$academic-paper-composer`。
- 落稿策略固定为“先侧写 working draft，再并回正式骨架”；第5章唯一工作草稿固定为 `<private-thesis-repo>/thesis/chapter5-working-draft.md`。
- 编译规则固定为 VS Code LaTeX Workshop 的 recipe `latexmk (xelatex)`，严格按 `<private-thesis-repo>/.vscode/settings.json` 执行，输出到 `<private-thesis-repo>\thesis\build\`。
- 第5章完成后，本计划只负责第5章 chapter-end reader testing；摘要起草与全文 reader testing 在 `T-012B / PLAN6.md` 的后续阶段单独收口，不混入本计划主体。

## 计划定位
- 这是“第5章正文专项计划”，不是整篇论文总计划，也不是摘要与全文关闭计划。
- 本计划默认继承以下长期记忆文档：
  - `<private-thesis-repo>/thesis/paper-outline.md`
  - `<private-thesis-repo>/thesis/paper-evidence-map.md`
  - `<private-thesis-repo>/thesis/paper-writing-log.md`
- 本计划同时继承 `<private-notes>/plan_skill.md` 与 `<private-notes>/plan_skill2.md` 中已经稳定的主链路：
  - `academic-paper-strategist -> doc-coauthoring -> graduation-thesis-editor -> academic-paper-composer`
- 但在本轮明确固定：
  - 不重新调用 `$academic-paper-strategist`
  - 不进入 `$academic-paper-composer`
  - 摘要不纳入本计划主体
  - 全文 reader testing 不纳入本计划主体
- 本计划当前版本用于承接 `T-013A` 对第5章的结构刷新：旧版单节 `5.1 全文总结与展望` 不再作为后续 reread 的 authority。

## 本章范围
- 只写：
  - `5.1 全文总结`
  - `5.2 研究展望`
- 不启动：
  - 摘要
  - 全文 reader testing
  - 定稿链路
  - 任意新增图表
  - 任意新实验结果、新数据集角色、新 promoted baseline 判断
- 本章叙事边界：
  - `5.1` 只收束全文任务、方法链路、实验组织、数据集角色与当前最稳妥的结论边界。
  - `5.2` 只写后续方向、剩余风险与继续验证路径，不回头再开结果章节。
  - `5.1` 与 `5.2` 都不新增 `5.1.1 / 5.2.1` 等内部标题。
- 数据集角色口径：
  - `Visium HD MouseBrain` 仍是全文唯一主实验线。
  - `Human Ovarian` 仍只作 supporting dataset。
  - `Xenium Ovarian` 与 `Xenium MouseBrain` 仍只作 workflow-support dataset。
  - `EXP-007` 仍只能写成当前最强 candidate，不能写成已 promoted baseline。
- 禁写点：
  - 不写正文未出现的新实验结论。
  - 不把 `Human Ovarian` 或两个 Xenium 写成与 `Visium HD MouseBrain` 同等级主线。
  - 不写临床落地、生产部署、大规模通用性或工业化应用。
  - 不详细复述五项指标表、14 组 run 明细、`assigned_ratio / n_valid_bins / n_pred` 等细节统计。
  - 不把未来工作写成“已经完成的改进”或“必然会得到的结果”。

## 启动前提
- 已满足：
  - 第5章总结素材包已完成双层整理，并已同步为 `5.1 全文总结 + 5.2 研究展望` 结构。
  - `<private-thesis-repo>/thesis/paper-evidence-map.md` 中第5章边界与素材入口已经稳定。
  - `<private-thesis-repo>/thesis/paper-writing-log.md` 已明确 `T-012A` 与 `T-013A` 下的第5章 authority 切换。
  - `<private-thesis-repo>/thesis/document.tex` 与 `<private-thesis-repo>/thesis/chapter5-working-draft.md` 可作为当前正文入口。
  - 第1章到第4章已稳定，可为第5章提供前文连续阅读上下文。
- 若以下条件不满足，则不应直接执行本计划：
  - 第5章素材包路径失效。
  - 第5章职责再次与第4章结果分析或摘要收口混淆。
  - 第1章到第4章仍处于大范围重写状态。

## 必读材料
- 论文蓝图：
  - `<private-thesis-repo>/thesis/paper-outline.md`
- 证据映射：
  - `<private-thesis-repo>/thesis/paper-evidence-map.md`
- 写作日志：
  - `<private-thesis-repo>/thesis/paper-writing-log.md`
- 第5章素材包根说明：
  - `<private-reference>/README.md`
- 第5章素材包正文可写层：
  - `<private-reference>/第五章写作总纲.md`
  - `<private-reference>/第五章总结要点卡.md`
  - `<private-reference>/第五章展望边界卡.md`
  - `<private-reference>/第五章章节承接卡.md`
  - `<private-reference>/摘要联动提示卡.md`
- 目标正文：
  - `<private-thesis-repo>/thesis/chapter5-working-draft.md`
  - `<private-thesis-repo>/thesis/document.tex`
  - `<private-thesis-repo>/thesis/document.bib`

## 证据优先级
- 第一优先：`README.md + 正文可写层/`
- 第二优先：已稳定的第1章到第4章正文与长期记忆三件套
- 第三优先：`后台核对层/` 仅用于核验结论来源与 authority 位置
- 默认规则：
  - 主起草阶段不把 `后台核对层/` 当作正文事实源。
  - 不从第4章表格、指标细节或图源说明中直接抽原话拼接第5章。
  - 第5章的目标是收束全文，不是重述第4章所有实验细节。

## 图表计划
- 第5章默认不新增图表。
- 若后续执行时确需补 1 张总览图，必须单独说明：
  - 图源来自何处
  - 图在第5章中承担什么作用
  - 为什么不会造成边界越界
- 本计划中不预设第5章图表。

## Skill 调用顺序
1. 主起草流程
- 用 `$doc-coauthoring` 创建并维护：
  - `<private-thesis-repo>/thesis/chapter5-working-draft.md`
- 第5章固定按以下顺序推进：
  1. `5.1` 第1段：全文任务与论文定位
  2. `5.1` 第2段：方法链路与工程实现完成项
  3. `5.1` 第3段：实验组织与数据集角色完成项
  4. `5.1` 第4段：当前最稳妥的结论边界
  5. `5.2` 第1段：剩余风险与继续验证方向
  6. `5.2` 第2段：全文收束与后续研究展望

2. 第5章写作硬约束
- `5.1` 允许从全文视角总结：
  - 工程化整理定位
  - `stage0-stage4 + transfer + metric + figures` 的整体链路
  - 主实验线与 supporting / workflow-support 的角色层级
  - 正式 baseline、14 组单变量实验与关键方向的稳定结论边界
- `5.1` 禁止：
  - 新的实验结果或正文未出现的新结论
  - 将 future work 提前并入“已完成工作”
  - 第4章结果表和图组的长段复述
- `5.2` 允许：
  - 围绕 `stage2` 高杠杆轴继续验证
  - 完善 supporting / workflow-support 数据集上的流程复核
  - 增强更细粒度可视化与解释性
  - 对剩余风险和未闭环点做克制收束
- `5.2` 禁止：
  - 把 `EXP-007` 写成必然会 promoted
  - 把 future work 写成已完成成果
  - 引入临床落地、工业部署或正文未建立的新方向

3. 局部编辑流程
- 当第5章已有草稿后，才允许用 `$graduation-thesis-editor` 做：
  - 局部润色
  - 逻辑检查
  - reviewer 视角诊断
- 常见 route 固定为：
  - `revision / 逻辑检查`
  - `analysis / 论文整体以 Reviewer 视角进行审视`
  - `revision / 表达润色（中文论文）`
- 可根据需要创建子智能体执行这些局部 editor 任务。
- 但并不是每次局部 editor 任务都必须创建子智能体：
  - 如果任务规模不大、目标单一、串行处理更稳，可以直接在主线程完成。
  - 如果任务需要陌生读者视角、可并行拆开的多个局部任务，或需要避免主线程上下文污染，再优先考虑创建子智能体。
- 是否创建子智能体、创建几个子智能体，由当时任务拆分复杂度决定，但执行前必须显式判断一次。

4. 可选风格清理
- 只有在第5章稳定之后，才可选使用 `$humanizer` 做局部语言去公式化。

5. 禁止提前进入的流程
- 本计划中不使用 `$academic-paper-composer`。
- 本计划默认不重新调用 `$academic-paper-strategist`；只有在第5章边界或证据发生实质变化时，才允许回到 strategist。

## 推荐章节微流程
### 阶段 A：建立第5章 working draft 骨架
- 用 `$doc-coauthoring` 创建 `<private-thesis-repo>/thesis/chapter5-working-draft.md`。
- 先固定第5章骨架：
  - `# 第5章 总结与展望`
  - `## 5.1 全文总结`
  - `## 5.2 研究展望`
- 本轮不在 working draft 中提前展开摘要或全文 reader testing 记录。

### 阶段 B：先写 `5.1`，后写 `5.2`
- 不跳写。
- `5.1` 固定先完成“任务定位 -> 方法完成项 -> 实验组织 -> 稳定结论边界”。
- `5.2` 再承接“剩余风险 -> 继续验证方向 -> 全文结束语”。
- 若 `5.1` 尚未稳定，不应提前扩写 `5.2`。

### 阶段 C：每个段落的固定微流程
1. 用 `$doc-coauthoring` 先完成该段的要点筛选与段落草稿。
2. 草稿完成后，立刻对照第5章素材包 `正文可写层/` 做边界检查。
3. 若该段存在以下问题，再调用 `$graduation-thesis-editor`：
   - 语言重复
   - 逻辑跳跃
   - 数据集角色层级表达不清
   - 把总结写成新的结果章节
   - 把未来工作写成既成事实
4. 段落通过后继续下一段，不立刻并回 `<private-thesis-repo>/thesis/document.tex`。

### 阶段 D：第5章 reviewer 式诊断
- 第5章草稿完成后，必须调用一次 `$graduation-thesis-editor` 做第5章 reviewer 式检查。
- 重点检查：
  - `5.1` 是否把第4章 candidate 写成定案
  - `5.1` 是否把展望内容提前写成“已完成工作”
  - `5.2` 是否引入正文之外的新方向
  - 数据集角色层级是否仍一致
- 如 reviewer 诊断暴露明显误读风险，应先修订，再进入第5章关闭流程。

### 阶段 E：并回与编译
- 第5章稳定后，将其并回 `<private-thesis-repo>/thesis/document.tex`。
- 并回时只更新第5章正文，不同时处理摘要。
- 编译只在第5章已并回 `<private-thesis-repo>/thesis/document.tex` 后执行。
- `document.bib` 默认不改；只有当第5章实际新增正文引用时，才补入对应条目。

### 阶段 F：第5章 chapter-end reader testing
- 这是第5章关闭动作，必须显式调用至少 1 个 fresh-reader 子智能体执行。
- 默认主测读取范围固定为：
  - `第1章 + 第2章 + 第3章 + 第4章 + 第5章`
- 若上下文过长，最低回退范围固定为：
  - `第4章 + 第5章`
- 若需要额外检查“脱离前文时第5章是否仍可单独成立”，可追加一次“只读第5章”的补充测试，但不能替代默认主测。
- reader testing 至少检查：
  - `5.1` 是否把第4章 candidate 写成定案
  - `5.2` 是否把 future work 写成既成成果
  - 数据集角色层级是否仍一致
  - 第5章是否把总结写成新的结果章节
- 本轮 reader testing 只对应“第5章关闭”，不宣称“全文 reader testing 已完成”。

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
- 混合请求必须拆开，不能在一次调用里同时做“检查 + 改写”或“分析 + 润色”。

## 推荐提示词
### 第5章 reviewer 式检查提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 以毕业论文 reviewer 的视角检查第5章当前草稿，重点看 `5.1` 是否越界重述结果、`5.2` 是否把未来工作写成既成成果，以及数据集角色层级是否被破坏。

Expected route type:
- analysis / 论文整体以 Reviewer 视角进行审视

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 本次调用只做诊断，不顺手整体重写正文。
```

### 第5章局部润色提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 在不改变结论边界、数据集角色和风险表述的前提下，把第5章 `5.1` 或 `5.2` 的某一段调整为更自然的中文论文表述。

Expected route type:
- revision / 表达润色（中文论文）

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 本次调用只做局部润色，不新增结论。
```

### 第5章边界检查提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 检查第5章双节结构下，`5.1` 与 `5.2` 的边界是否清楚，是否存在“总结与展望互相污染”的问题。

Expected route type:
- revision / 逻辑检查

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 本次调用只做边界检查，不顺手扩写。
```

## 推荐提示词
### 第5章主起草提示词
```text
Use $doc-coauthoring.

Read first:
- <private-thesis-repo>\文档\参考文献\写作计划\PLAN5.md
- <private-thesis-repo>\thesis\paper-outline.md
- <private-thesis-repo>\thesis\paper-evidence-map.md
- <private-thesis-repo>\thesis\paper-writing-log.md
- <private-thesis-repo>\文档\参考文献\第五章总结素材包\README.md
- <private-thesis-repo>\文档\参考文献\第五章总结素材包\正文可写层\第五章写作总纲.md
- <private-thesis-repo>\文档\参考文献\第五章总结素材包\正文可写层\第五章总结要点卡.md
- <private-thesis-repo>\文档\参考文献\第五章总结素材包\正文可写层\第五章展望边界卡.md
- <private-thesis-repo>\文档\参考文献\第五章总结素材包\正文可写层\第五章章节承接卡.md
- <private-thesis-repo>\thesis\chapter5-working-draft.md
- <private-thesis-repo>\thesis\document.tex
- <private-thesis-repo>\thesis\document.bib

Task:
创建并维护 `<private-thesis-repo>\thesis\chapter5-working-draft.md`，按固定顺序完成第5章 `5.1 全文总结` 与 `5.2 研究展望`。

Rules:
- 默认主读入入口是 `README.md + 正文可写层/`。
- 不把 `后台核对层/` 当作正文事实源。
- `5.1` 只写已完成工作与稳定结论边界。
- `5.2` 只写后续方向、剩余风险与继续验证路径。
- 不新增正文未出现的新实验结果、新数据集角色或新的 promoted baseline 判断。
- 保持 `Visium HD MouseBrain` 为唯一主实验线，`Human Ovarian` 为 supporting dataset，两个 Xenium 为 workflow-support dataset。
- `EXP-007` 只能写成当前最强 candidate，不能写成已 promoted baseline。
- 本轮不处理摘要，也不宣称完成全文 reader testing。
```

## 编译规则
- 只有在第5章已经并回 `<private-thesis-repo>/thesis/document.tex` 后，才执行编译。
- 编译 recipe：
  - VS Code LaTeX Workshop `latexmk (xelatex)`
- 配置来源：
  - `<private-thesis-repo>/.vscode/settings.json`
- 输出目录：
  - `<private-thesis-repo>\thesis\build\`

## 执行后同步
- 创建或刷新 `PLAN5.md` 后，至少同步：
  - `<private-thesis-repo>/thesis/paper-writing-log.md`
- 启动 `T-012A` 并完成第5章 working draft 后，至少同步：
  - `<private-thesis-repo>/thesis/paper-writing-log.md`
  - `<private-thesis-repo>/thesis/chapter5-working-draft.md`
- 如果第5章已经并回正式骨架，再同步：
  - `<private-thesis-repo>/thesis/document.tex`
  - 必要时同步 `<private-thesis-repo>/thesis/document.bib`
- 第5章 chapter-end reader testing 完成后，必须在日志中登记：
  - 是否执行
  - 主测读取范围
  - 是否做了“只读第5章”的补测
  - 是否完成修订闭环
- 摘要与全文 reader testing 的收口记录，不在本计划同步范围内。

## 验收标准
- `PLAN5.md` 已按 [PLAN_TEMPLATE.md](PLAN_TEMPLATE.md) 的结构创建，而不是自由发挥版本。
- `PLAN5.md` 明确只服务第5章 `5.1 + 5.2`，不把摘要和全文 reader testing 混入本计划主体。
- `PLAN5.md` 已写死默认主读入入口为 `README.md + 正文可写层/`。
- `PLAN5.md` 已写死第5章唯一 working draft 为 `<private-thesis-repo>/thesis/chapter5-working-draft.md`。
- `PLAN5.md` 已区分：
  - `5.1` 只写全文总结
  - `5.2` 只写研究展望
- `PLAN5.md` 已明确区分：
  - 第5章 chapter-end reader testing
  - 全文 reader testing
- `<private-thesis-repo>/thesis/paper-writing-log.md` 更新后，后续执行者不需要再临场决定：
  - 第5章是否仍是单节
  - 第5章是否新建独立 working draft
  - 第5章默认是否读后台核对层
  - 第5章关闭时做的是章节测试还是全文测试

## 禁止事项
- 不要把 `PLAN5.md` 写成整篇论文总计划。
- 不要让 `T-012A` 在执行 `PLAN5.md` 时默认读取 `后台核对层/` 作为正文事实源。
- 不要在第5章把 `EXP-007` 写成已 promoted baseline。
- 不要把 `Human Ovarian` 或两个 Xenium 数据集升级成并列主结果线。
- 不要把第5章写成第4章结果表复读。
- 不要把 `5.2` 写成“既成成果清单”。
- 不要在第5章未稳定时提前进入 `$academic-paper-composer`。
