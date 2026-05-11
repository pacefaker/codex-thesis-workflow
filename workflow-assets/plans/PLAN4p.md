# T-011 第四章结果部分执行计划

## 摘要
- 本计划只服务于第4章结果部分 `4.5.1 -> 4.5.4`、`4.6` 以及第4章正式 chapter-end reader testing，不扩展到 `4.1 -> 4.4` 重写、第5章正文或整篇论文定稿。
- 本轮目标是基于第4章实验素材包 V2 的 `README.md + 结果分析层/`，完成第4章结果部分 working draft，并在整章稳定后关闭第4章。
- 主流程固定为 `$doc-coauthoring`，局部编辑固定为 `$graduation-thesis-editor`；不重新调用 `$academic-paper-strategist`，不进入 `$academic-paper-composer`。
- 第4章唯一工作草稿继续固定为 `<your-thesis-repo>/thesis/chapter4-working-draft.md`，不新建 `chapter4-result-draft.md` 或其他副本。
- 编译规则固定为 VS Code LaTeX Workshop 的 recipe `latexmk (xelatex)`，严格按 `<your-thesis-repo>/.vscode/settings.json` 执行，输出到 `<your-thesis-repo>\thesis\build\`。

## 计划定位
- 这是“第4章结果部分专项计划”，不是整篇论文总计划，也不是 `T-010` 的补丁。
- 本计划默认继承以下长期记忆文档：
  - `<your-thesis-repo>/thesis/paper-outline.md`
  - `<your-thesis-repo>/thesis/paper-evidence-map.md`
  - `<your-thesis-repo>/thesis/paper-writing-log.md`
- 本计划同时继承 `<planning-notes>/plan_skill.md` 与 `<planning-notes>/plan_skill2.md` 中已经稳定的主链路：
  - `academic-paper-strategist -> doc-coauthoring -> graduation-thesis-editor -> academic-paper-composer`
- 但在本轮明确固定：
  - 不重新调用 `$academic-paper-strategist`
  - 不进入 `$academic-paper-composer`
  - 不把 `<reference-materials>/2025.05.28.656357v1.full.pdf` 当作 `4.5 / 4.6` 的主事实源
  - `T-010` 已完成的 `4.1 -> 4.4` 视为前置稳定内容，本轮不重写，只做必要的整章级衔接复核

## 本章范围
- 只写：
  - `4.5.1 基线实验结果`
  - `4.5.2 单变量参数对比结果`
  - `4.5.3 关键实验结果分析`
  - `4.5.4 可视化结果与讨论`
  - `4.6 本章小结`
- 不启动：
  - `4.1 -> 4.4` 的回头重写
  - 第5章总结与展望正文
  - 任意“最终 promoted baseline 已确定”的结论
  - 任意把 supporting / workflow-support 数据集抬升成并列主结果线的写法
- 本章叙事边界：
  - `4.5.1` 只写正式 baseline 结果，主叙事围绕 `Visium HD MouseBrain`，`Human Ovarian` 最多保留 supporting note，两个 Xenium 不进入正式指标主比较。
  - `4.5.2` 必须写 14 组单变量结果与参数轴摘要，不能省略 `EXP-006`、`EXP-009` 等负结果。
  - `4.5.3` 只展开 `BASE / EXP-004 / EXP-006 / EXP-007` 四组关键 run，并明确 `EXP-007` 是当前最强 candidate 但未 promoted。
  - `4.5.4` 只写可视化能支持什么、不能支持什么，不把图像讨论写成最终优劣证明。
  - `4.6` 只收束本章稳定结论、剩余风险和第5章桥接，不新增未在 `4.5` 展开的结果。
- 数据集角色口径：
  - `Visium HD MouseBrain` 是唯一主结果线。
  - `Human Ovarian` 只作 supporting dataset / supporting baseline。
  - `Xenium Ovarian` 与 `Xenium MouseBrain` 只作 workflow-support dataset。
- 禁写点：
  - 不把 `EXP-007` 写成已 promoted baseline。
  - 不把 `Human Ovarian` 写成与 `Visium HD MouseBrain` 并列主实验线。
  - 不把两个 Xenium 数据集写成正式 `Precision / Recall / F1 / mIoU / PQ` 主比较对象。
  - 不在 `4.6` 新增 `4.5` 未展开的结果、图源解释或 run-level 细节。

## 启动前提
- 已满足：
  - 第4章实验素材包 V2 已完成三层重组。
  - `<your-thesis-repo>/thesis/paper-evidence-map.md` 中第4章边界与 `4.6` evidence 入口已经稳定。
  - `<your-thesis-repo>/thesis/paper-writing-log.md` 已明确 `T-011` 默认读 `README.md + 结果分析层/`。
  - `<your-thesis-repo>/thesis/document.tex` 与 `<your-thesis-repo>/thesis/chapter4-working-draft.md` 中已有 `4.5 / 4.6` 骨架占位。
  - 第1章到第3章以及第4章前半部分已稳定，可为第4章正式 chapter-end reader testing 提供前文连续阅读上下文。
- 若以下条件不满足，则不应直接执行本计划：
  - `结果分析层/` 与 `后台核对层/` 的边界重新摇摆。
  - 第4章职责再次与第3章方法描述或第5章总结展望混淆。
  - 第4章结果层素材路径失效，或关键结果卡无法正常读取。

## 必读材料
- 论文蓝图：
  - `<your-thesis-repo>/thesis/paper-outline.md`
- 证据映射：
  - `<your-thesis-repo>/thesis/paper-evidence-map.md`
- 写作日志：
  - `<your-thesis-repo>/thesis/paper-writing-log.md`
- 前序计划：
  - [PLAN4.md](PLAN4.md)
- 第4章素材包根说明：
  - `<reference-materials>/README.md`
- 第4章素材包结果分析层：
  - `<reference-materials>/第四章结果边界与可写结论卡.md`
  - `<reference-materials>/第四章baseline结果卡.md`
  - `<reference-materials>/第四章单变量结果总表.md`
  - `<reference-materials>/第四章关键结果分析卡.md`
  - `<reference-materials>/第四章结果图表建议清单.md`
  - `<reference-materials>/第四章本章小结卡.md`
- 目标正文：
  - `<your-thesis-repo>/thesis/chapter4-working-draft.md`
  - `<your-thesis-repo>/thesis/document.tex`
  - `<your-thesis-repo>/thesis/document.bib`

## 证据优先级
- 第一优先：`README.md + 结果分析层/`
- 第二优先：长期记忆三件套与 [PLAN4.md](PLAN4.md)
- 第三优先：`后台核对层/` 仅用于核验 `assigned_ratio / n_valid_bins / n_pred`、图源、`promotion_review` 语境与 run-level 事实
- 默认规则：
  - 主起草阶段不把 `<reference-materials>/2025.05.28.656357v1.full.pdf` 当作结果事实源。
  - `后台核对层/` 只用于核验，不直接抄原话入正文。
  - `4.6` 默认先从 `<reference-materials>/第四章结果边界与可写结论卡.md` 与 `<reference-materials>/第四章本章小结卡.md` 取结论，不临场从 `后台核对层/` 拼接收束段落。

## 图表计划
- `4.5.1` 固定对应：
  - `表4-5 baseline 结果表`
  - `图4-1 baseline 核心可视化`
- `4.5.2` 固定对应：
  - `表4-6 单变量总表`
- `4.5.3` 固定对应：
  - `表4-7 关键实验对比表`
  - `图4-2 baseline 与 EXP-007 对比图`
- `4.5.4` 固定对应：
  - `图4-3 可视化结果与讨论图组`
- `4.6` 默认不新增图表。

## Skill 调用顺序
1. 主起草流程
- 用 `$doc-coauthoring` 在 `<your-thesis-repo>/thesis/chapter4-working-draft.md` 中继续完成：
  - `4.5.1`
  - `4.5.2`
  - `4.5.3`
  - `4.5.4`
  - `4.6`
- 固定起草顺序为：
  - `4.5.1 -> 4.5.2 -> 4.5.3 -> 4.5.4 -> 4.6`

2. 第4章结果部分写作硬约束
- `4.5.1` 允许写 `Visium HD MouseBrain` baseline 五项结果与 supporting note。
- `4.5.1` 禁止把 `Human Ovarian` 写成并列主 baseline，也禁止把两个 Xenium 写成正式指标主比较对象。
- `4.5.2` 必须保留正负结果，并按参数轴归类解释，不写成组合优化或自动调参结论。
- `4.5.3` 只展开 `BASE / EXP-004 / EXP-006 / EXP-007`，且必须同时写出 `EXP-007` 的覆盖收缩风险。
- `4.5.4` 只承担“图像支持什么、不能支持什么”的讨论功能，不替代指标比较。
- `4.6` 只收束本章稳定结论与风险，不把候选方向写成既成事实。

3. 局部编辑流程
- 当某个小节已经有草稿后，才允许用 `$graduation-thesis-editor` 做：
  - 局部润色
  - 逻辑检查
  - 实验分析补写
  - reviewer 视角诊断
- 常见 route 固定为：
  - `revision / 逻辑检查`
  - `analysis / 实验分析`
  - `analysis / 论文整体以 Reviewer 视角进行审视`
  - `revision / 表达润色（中文论文）`
- 可根据需要创建子智能体执行这些局部 editor 任务。
- 这里的“是否创建子智能体”只针对局部 editor 任务本身，不等同于整章关闭时的 chapter-end reader testing。
- 但并不是每次局部 editor 任务都必须创建子智能体：
  - 如果任务规模不大、目标单一、串行处理更稳，可以直接在主线程完成。
  - 如果任务需要陌生读者视角、可并行拆开的多个局部任务，或需要避免主线程上下文污染，再优先考虑创建子智能体。
- 是否创建子智能体、创建几个子智能体，由当时任务拆分复杂度决定，但执行前必须显式判断一次。

4. 可选风格清理
- 只有在第4章整章稳定之后，才可选使用 `$humanizer` 做局部语言去公式化。

5. 禁止提前进入的流程
- 本计划中不使用 `$academic-paper-composer`。
- 本计划默认不重新调用 `$academic-paper-strategist`；只有在第4章边界或证据发生实质变化时，才允许回到 strategist。

## 推荐章节微流程
### 阶段 A：确认第4章结果部分骨架
- 在 `<your-thesis-repo>/thesis/chapter4-working-draft.md` 中确认以下骨架仍然存在：
  - `4.5.1 基线实验结果`
  - `4.5.2 单变量参数对比结果`
  - `4.5.3 关键实验结果分析`
  - `4.5.4 可视化结果与讨论`
  - `4.6 本章小结`
- 本轮不改 `4.1 -> 4.4` 已稳定内容，只把它们视为整章前文上下文。

### 阶段 B：按小节顺序推进
- 固定按 `4.5.1 -> 4.5.2 -> 4.5.3 -> 4.5.4 -> 4.6` 推进，不跳写。
- 默认允许 `4.5.2` 与 `4.5.3` 投入更多迭代轮次，因为它们最容易发生“只挑正结果”“把 candidate 写成定案”与“覆盖收缩风险漏写”的问题。

### 阶段 C：每个小节的固定微流程
1. 用 `$doc-coauthoring` 先完成该节的“要点筛选 + 小节草稿”。
2. 草稿完成后，立刻对照第4章素材包 `结果分析层/` 做边界检查。
3. 若该节存在以下问题，再调用 `$graduation-thesis-editor`：
   - 语言重复
   - 逻辑跳跃
   - 只挑正结果写
   - 把 candidate 写成 promoted baseline
   - supporting / workflow-support 数据集角色表达不清
   - 可视化讨论写成最终优劣证明
4. 小节通过后继续下一节，不立刻并回 `<your-thesis-repo>/thesis/document.tex`。

### 阶段 D：整章 reviewer 诊断
- `4.5 / 4.6` 草稿完成后，必须调用一次 `$graduation-thesis-editor` 做第4章整章 reviewer 式检查，而不只检查后半章本身。
- 重点检查：
  - `4.2` 的四数据集角色口径是否被 `4.5 / 4.6` 破坏
  - `EXP-007` 是否被误写成已 promoted baseline
  - `Human Ovarian` 是否被写成并列主结果线
  - 两个 Xenium 是否被写成正式指标主比较数据集
  - `4.6` 是否把候选方向、风险解释或后续工作写成既成结论
- 如 reviewer 诊断暴露明显误读风险，应先修订，再进入整章关闭流程。

### 阶段 E：并回与编译
- `4.5 / 4.6` 稳定后，将其并回 `<your-thesis-repo>/thesis/document.tex`。
- 并回时只更新第4章结果部分与本章小结，不回头重写 `4.1 -> 4.4`。
- 编译只在 `4.5 / 4.6` 已并回 `<your-thesis-repo>/thesis/document.tex` 后执行。
- `document.bib` 默认不改；只有当 `4.5 / 4.6` 实际新增正文引用时，才补入对应条目。

### 阶段 F：第4章正式 chapter-end reader testing
- 这是第4章整章关闭动作，必须显式调用至少 1 个 fresh-reader 子智能体执行。
- 默认主测读取范围固定为：
  - `第1章 + 第2章 + 第3章 + 第4章`
- 若上下文过长，最低回退范围固定为：
  - `第3章 + 第4章`
- 若需要额外检查“脱离前文时第4章是否也能单独成立”，需要追加一次“只读第4章”的补充测试，但不能替代默认主测。
- reader testing 至少检查：
  - 本章与第2章数据集介绍是否发生职责混淆
  - 是否会把 `EXP-007` 误读为已 promoted baseline
  - 是否会把 supporting / workflow-support 数据集误读成并列主结果线
  - `4.6` 是否把候选方向、风险解释或后续工作写成既成结论
- 若首轮 reader testing 暴露明显误读风险，应先修订，再进行第二轮轻量复测后才允许关闭第4章。

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

### 4.5.2 小节逻辑检查提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 检查第4章 `4.5.2 单变量参数对比结果` 当前草稿是否遗漏负结果，或是否把参数轴总结写成组合优化 / 自动调参式结论。

Expected route type:
- revision / 逻辑检查

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 本次调用只做诊断，不同时做润色改写。
```

### 4.5.3 实验分析补写提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 根据 `BASE / EXP-004 / EXP-006 / EXP-007` 的结果与风险说明，补写第4章 `4.5.3 关键实验结果分析`。

Expected route type:
- analysis / 实验分析

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 本次调用只做实验分析，不顺手合并成整节润色。
```

### 第4章整章 reviewer 式检查提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 以毕业论文 reviewer 的视角检查完整第4章，重点关注 `4.5 / 4.6` 是否破坏了第4章既有的数据集角色口径、结论边界和章节职责。

Expected route type:
- analysis / 论文整体以 Reviewer 视角进行审视

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 本次调用只做 reviewer 式诊断，不顺手整体重写全文。
```

### 4.6 局部润色提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 在不改变结论边界和风险表述的前提下，把第4章 `4.6 本章小结` 调整为更自然的中文论文表述。

Expected route type:
- revision / 表达润色（中文论文）

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 本次调用只做局部润色，不新增结论。
```

## 推荐提示词
### 第4章结果部分主起草提示词
```text
Use $doc-coauthoring.

Read first:
- <your-thesis-repo>\文档\参考文献\写作计划\PLAN4p.md
- <your-thesis-repo>\thesis\paper-outline.md
- <your-thesis-repo>\thesis\paper-evidence-map.md
- <your-thesis-repo>\thesis\paper-writing-log.md
- <your-thesis-repo>\文档\参考文献\第四章实验素材包\README.md
- <your-thesis-repo>\文档\参考文献\写作计划\PLAN4.md
- <your-thesis-repo>\文档\参考文献\第四章实验素材包\结果分析层\第四章结果边界与可写结论卡.md
- <your-thesis-repo>\文档\参考文献\第四章实验素材包\结果分析层\第四章baseline结果卡.md
- <your-thesis-repo>\文档\参考文献\第四章实验素材包\结果分析层\第四章单变量结果总表.md
- <your-thesis-repo>\文档\参考文献\第四章实验素材包\结果分析层\第四章关键结果分析卡.md
- <your-thesis-repo>\文档\参考文献\第四章实验素材包\结果分析层\第四章结果图表建议清单.md
- <your-thesis-repo>\文档\参考文献\第四章实验素材包\结果分析层\第四章本章小结卡.md
- <your-thesis-repo>\thesis\chapter4-working-draft.md
- <your-thesis-repo>\thesis\document.tex
- <your-thesis-repo>\thesis\document.bib

Task:
继续维护 `<your-thesis-repo>\thesis\chapter4-working-draft.md`，按 `4.5.1 -> 4.5.2 -> 4.5.3 -> 4.5.4 -> 4.6` 的顺序共写第4章结果部分与本章小结。

Rules:
- 默认主读入入口是 `README.md + 结果分析层/`。
- 不把 `后台核对层/` 当作正文默认事实源，只在需要核验 `assigned_ratio / n_valid_bins / n_pred`、图源或 `promotion_review` 语境时回看。
- `4.5.1` 主叙事围绕 `Visium HD MouseBrain`，`Human Ovarian` 只作 supporting note，两个 Xenium 不进正式指标主比较。
- `4.5.2` 必须保留负结果，不能只挑正结果写。
- `4.5.3` 必须同时写出 `EXP-007` 的提升信号与覆盖收缩风险。
- `4.5.4` 不把图像讨论写成最终优劣证明。
- `4.6` 默认先读 `第四章结果边界与可写结论卡.md` 与 `第四章本章小结卡.md`，不新增 `4.5` 未展开的结果。
- 如 bibliography 尚未冻结，可先使用作者-年份式引用占位。
```

## 编译规则
- 只有在第4章结果部分已经并回 `<your-thesis-repo>/thesis/document.tex` 后，才执行编译。
- 编译 recipe：
  - VS Code LaTeX Workshop `latexmk (xelatex)`
- 配置来源：
  - `<your-thesis-repo>/.vscode/settings.json`
- 输出目录：
  - `<your-thesis-repo>\thesis\build\`

## 执行后同步
- 创建 `PLAN4p.md` 后，至少同步：
  - `<your-thesis-repo>/thesis/paper-writing-log.md`
- 启动 `T-011` 并完成 `4.5 / 4.6` working draft 后，至少同步：
  - `<your-thesis-repo>/thesis/paper-writing-log.md`
  - `<your-thesis-repo>/thesis/chapter4-working-draft.md`
- 如果结果部分已经并回正式骨架，再同步：
  - `<your-thesis-repo>/thesis/document.tex`
  - 必要时同步 `<your-thesis-repo>/thesis/document.bib`
- 第4章正式 chapter-end reader testing 完成后，必须在日志中登记：
  - 是否执行
  - 主测读取范围
  - 是否做了“只读第4章”的补测
  - 是否完成修订闭环

## 验收标准
- `PLAN4p.md` 已按 [PLAN_TEMPLATE.md](PLAN_TEMPLATE.md) 的结构创建，而不是自由发挥版本。
- `PLAN4p.md` 明确只服务 `4.5 / 4.6` 与第4章关闭，不回头重写 `4.1 -> 4.4`。
- `PLAN4p.md` 的默认读入入口明确为 `README.md + 结果分析层/`。
- `PLAN4p.md` 已写死 `4.5.1 -> 4.5.4` 与 `4.6` 的禁写点，不会把 `EXP-007` 写成已 promoted baseline，也不会破坏四数据集角色层级。
- `PLAN4p.md` 已写死唯一 working draft 为 `<your-thesis-repo>/thesis/chapter4-working-draft.md`。
- `PLAN4p.md` 已写死 `4.6` 默认以 `<reference-materials>/第四章结果边界与可写结论卡.md` 和 `<reference-materials>/第四章本章小结卡.md` 为收口入口。
- `PLAN4p.md` 已区分 `T-010` 的 slice-end reviewer 诊断与 `T-011` 的正式 chapter-end reader testing。
- `PLAN4p.md` 已写死编译方式为 `<your-thesis-repo>/.vscode/settings.json` 中的 `latexmk (xelatex)`，输出到 `thesis/build/`。

## 禁止事项
- 不要把 `PLAN4p.md` 写成整篇论文总计划。
- 不要让 `T-011` 默认读取 `后台核对层/` 作为正文事实源。
- 不要在 `4.5 / 4.6` 中把 `EXP-007` 写成已 promoted baseline。
- 不要把 `Human Ovarian` 或两个 Xenium 数据集升级成并列主结果线。
- 不要把 `4.6` 写成第5章总结与展望的提前展开。
- 不要在第4章整章未稳定时提前进入 `$academic-paper-composer`。

