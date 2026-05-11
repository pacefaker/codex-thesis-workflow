# T-010 第四章前半部分执行计划

## 摘要
- 本计划只服务于第4章前半部分 `4.1 -> 4.4`，不扩展到 `4.5`、`4.6`、第5章正文或整篇论文定稿。
- 本轮目标是基于第4章实验素材包 V2 的 `README.md + 前半写作层/`，完成第4章前半部分的 working draft，并在稳定后先将 `4.1 -> 4.4` 并回 `document.tex`。
- 主流程固定为 `$doc-coauthoring`，局部编辑固定为 `$graduation-thesis-editor`；不重新调用 `$academic-paper-strategist`，不进入 `$academic-paper-composer`。
- 落稿策略固定为“先侧写 working draft，再并回正式骨架”；第4章唯一工作草稿固定为 [chapter4-working-draft.md](/G:/bishe/JLU-CCST-Thesis/thesis/chapter4-working-draft.md)。
- 编译规则固定为 VS Code LaTeX Workshop 的 recipe `latexmk (xelatex)`，严格按 [settings.json](/G:/bishe/JLU-CCST-Thesis/.vscode/settings.json) 执行，输出到 `G:\bishe\JLU-CCST-Thesis\thesis\build\`。

## 计划定位
- 这是“第4章前半部分专项计划”，不是整篇论文总计划，也不是 `T-011` 的结果分析计划。
- 本计划默认继承以下长期记忆文档：
  - [paper-outline.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-outline.md)
  - [paper-evidence-map.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-evidence-map.md)
  - [paper-writing-log.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-writing-log.md)
- 本计划同时继承 [plan_skill.md](/D:/Desktop/plan_skill.md) 与 [plan_skill2.md](/D:/Desktop/plan_skill2.md) 中已经稳定的主链路：
  - `academic-paper-strategist -> doc-coauthoring -> graduation-thesis-editor -> academic-paper-composer`
- 但在本轮明确固定：
  - 不重新调用 `$academic-paper-strategist`
  - 不进入 `$academic-paper-composer`
  - 不把 `结果分析层/` 当作 `T-010` 的默认正文事实源

## 本章范围
- 只写：
  - `4.1 实验环境与参数设置`
  - `4.2 数据集介绍`
  - `4.3 基线实验设计`
  - `4.4 单变量对比实验设计`
- 不启动：
  - `4.5 实验结果与分析`
  - `4.6 本章小结`
  - 任意 baseline 正式结果表
  - 任意 `candidate / promotion_review` 结论
- 本章叙事边界：
  - `4.1` 只写环境分层、脚本链路、固定参数组与评价参数组。
  - `4.2` 只写四数据集角色、评价资格与主次层级。
  - `4.3` 只写 baseline 设计对象、评价链路与角色分层，不提前写结果。
  - `4.4` 只写单变量实验编号体系、控制变量原则、参数轴与设计目的，不提前写结果判断。
- 数据集角色口径：
  - `Visium HD MouseBrain` 是主实验数据集。
  - `Human Ovarian` 只作 supporting dataset。
  - `Xenium Ovarian` 与 `Xenium MouseBrain` 只作 workflow-support dataset。
- 禁写点：
  - 不把四个数据集写成同等级正式评价数据集。
  - 不把 `Human Ovarian` 写成与 `Visium HD MouseBrain` 并列主线。
  - 不把两个 Xenium 数据集写成正式 `mIoU / PQ / F1` 主比较对象。
  - 不在 `4.1 -> 4.4` 提前写 baseline 五项正式结果、14 组单变量结果、`candidate` 判断或 `promotion_review` 结论。

## 启动前提
- 已满足：
  - 第4章实验素材包 V2 已完成三层重组。
  - [paper-evidence-map.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-evidence-map.md) 中第4章边界已经稳定。
  - [paper-writing-log.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-writing-log.md) 已明确 `T-010` 默认只读 `README.md + 前半写作层/`。
  - [document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex) 中已有第4章骨架。
  - 第1章到第3章已稳定，可为第4章提供前文连续阅读上下文。
- 若以下条件不满足，则不应直接执行本计划：
  - 第4章职责再次与第3章或第5章混淆。
  - 第4章素材包 V2 路径失效。
  - `前半写作层/` 与 `结果分析层/` 的边界重新摇摆。

## 必读材料
- 论文蓝图：
  - [paper-outline.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-outline.md)
- 证据映射：
  - [paper-evidence-map.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-evidence-map.md)
- 写作日志：
  - [paper-writing-log.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-writing-log.md)
- 第4章素材包根说明：
  - [README.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/第四章实验素材包/README.md)
- 第4章素材包前半写作层：
  - [第四章实验环境与参数卡.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/第四章实验素材包/前半写作层/第四章实验环境与参数卡.md)
  - [第四章数据集概览卡.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/第四章实验素材包/前半写作层/第四章数据集概览卡.md)
  - [第四章baseline设计卡.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/第四章实验素材包/前半写作层/第四章baseline设计卡.md)
  - [第四章单变量实验设计卡.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/第四章实验素材包/前半写作层/第四章单变量实验设计卡.md)
  - [第四章前半图表建议清单.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/第四章实验素材包/前半写作层/第四章前半图表建议清单.md)
- 目标正文：
  - [chapter4-working-draft.md](/G:/bishe/JLU-CCST-Thesis/thesis/chapter4-working-draft.md)
  - [document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex)
  - [document.bib](/G:/bishe/JLU-CCST-Thesis/thesis/document.bib)

## 证据优先级
- 第一优先：`README.md + 前半写作层/`
- 第二优先：长期记忆三件套
- 第三优先：`后台核对层/` 仅用于核验参数、图源与 run-level 事实
- 默认规则：
  - 主起草阶段不读取 `结果分析层/` 作为正文事实源。
  - `后台核对层/` 只用于核验，不直接抄原话入正文。
  - 旧的单层素材包不再作为 authority 使用。

## 图表计划
- `4.1` 固定对应：
  - `表4-1 实验环境与参数设置表`
- `4.2` 固定对应：
  - `表4-2 数据集概览表`
- `4.3` 固定对应：
  - `表4-3 baseline 设计与比较对象表`
- `4.4` 固定对应：
  - `表4-4 单变量实验设计矩阵`
- `4.1 -> 4.4` 默认不强制插图。
- baseline 结果图、单变量结果图与 `EXP-007` 对比图全部推迟到 `4.5`。

## Skill 调用顺序
1. 主起草流程
- 用 `$doc-coauthoring` 创建并维护：
  - [chapter4-working-draft.md](/G:/bishe/JLU-CCST-Thesis/thesis/chapter4-working-draft.md)
- 固定起草顺序为：
  - `4.1`
  - `4.2`
  - `4.3`
  - `4.4`

2. 第4章前半部分写作硬约束
- `4.1` 允许写 `smurf` / `stardist-env`、单 GPU、核心脚本链路、参数分组。
- `4.1` 禁止写 `hostname`、`cwd`、`lscpu` 全量输出、`nvidia-smi` 原始输出、正式评价指标。
- `4.2` 必须写死四数据集角色层级，不把 `2048` 写进标题。
- `4.3` 只写 baseline 设计对象与比较角色，不写五项正式结果。
- `4.4` 只写 `BASE + EXP-001 ~ EXP-014` 的设计逻辑，不写任何结果列与 candidate 标签。

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
- 只有在第4章整章稳定之后，才可选使用 `$humanizer` 做局部语言去公式化。

5. 禁止提前进入的流程
- 本计划中不使用 `$academic-paper-composer`。
- 本计划默认不重新调用 `$academic-paper-strategist`；只有在第4章边界或证据发生实质变化时，才允许回到 strategist。

## 分阶段执行流程
### 阶段 A：建立第4章 working draft 骨架
- 用 `$doc-coauthoring` 创建 [chapter4-working-draft.md](/G:/bishe/JLU-CCST-Thesis/thesis/chapter4-working-draft.md)。
- 先固定前半部分四个小节骨架：
  - `4.1 实验环境与参数设置`
  - `4.2 数据集介绍`
  - `4.3 基线实验设计`
  - `4.4 单变量对比实验设计`
- `4.5` 与 `4.6` 仅保留为后续 `T-011` 续写位置，不在本轮展开。

### 阶段 B：按小节顺序推进
- 不跳序推进，保持与 [paper-writing-log.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-writing-log.md)、[document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex) 和后续日志同步一致。
- 默认允许 `4.2` 与 `4.4` 投入更多迭代轮次，因为它们最容易发生角色越界与结果前移。

### 阶段 C：每个小节的固定微流程
1. 用 `$doc-coauthoring` 先完成该节的“要点筛选 + 小节草稿”。
2. 草稿完成后，立刻对照第4章素材包 `前半写作层/` 做边界检查。
3. 若该节存在以下问题，再调用 `$graduation-thesis-editor`：
   - 语言重复
   - 逻辑跳跃
   - 数据集角色表达不清
   - baseline / 单变量设计写得像结果分析
   - 存在章节边界越界风险
4. 小节通过后继续下一节，不立刻并回 [document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex)。

### 阶段 D：前半章 slice-end 复核
- `4.1 -> 4.4` 都完成后，再调用一次 `$graduation-thesis-editor` 做 slice-end reviewer 式检查。
- 重点检查：
  - `4.1` 是否写成宿主机原始输出转抄
  - `4.2` 是否破坏四数据集角色层级
  - `4.3` 是否提前写入 baseline 正式结果
  - `4.4` 是否把设计矩阵写成穷举搜索或自动调参
- 本轮只要求完成 slice-end reviewer 诊断，不把这一步冒充为正式 chapter-end reader testing。
- 如 reviewer 诊断暴露明显误读风险，应先修订，再并回前半章稳定稿。

### 阶段 E：并回与编译
- `4.1 -> 4.4` 稳定后，允许先并回 [document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex)。
- 并回时仅更新前半部分，`4.5 / 4.6` 继续保留占位，等待 `T-011`。
- 编译只在前半章已经并回 [document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex) 后执行。
- 第4章正式 chapter-end reader testing 明确延后到 `T-011` 整章关闭时执行。
- 届时默认主测读取范围固定为：
  - `第1章 + 第2章 + 第3章 + 第4章`
- 若上下文长度在实际执行时过长，最低回退范围不得少于：
  - `第3章 + 第4章`
- 若需要补查“脱离前文时第4章是否仍自洽”，可追加一次“只读第4章”的专项测试，但不能替代默认主测。

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

### 4.2 小节逻辑检查提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 检查第4章 `4.2 数据集介绍` 当前草稿是否破坏了四数据集角色层级，或是否把 supporting / workflow-support 数据集写得过重。

Expected route type:
- revision / 逻辑检查

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 本次调用只做诊断，不同时做润色改写。
```

### 4.4 小节逻辑检查提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 检查第4章 `4.4 单变量对比实验设计` 当前草稿是否提前混入结果列、candidate 判断或自动调参式表述。

Expected route type:
- revision / 逻辑检查

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 本次调用只做诊断，不同时做润色改写。
```

### 第4章前半部分 reviewer 式检查提示词
```text
Use $graduation-thesis-editor.

Task goal:
- 以毕业论文 reviewer 的视角检查第4章前半部分 `4.1 -> 4.4` 草稿，逐节指出具体问题。

Expected route type:
- analysis / 论文整体以 Reviewer 视角进行审视

Rules:
- 先执行 skill 的 routing protocol。
- 只能选择一个 route。
- 执行前报告 Route ID / Prompt Source / Prompt Preserved Verbatim。
- 本次调用只做 reviewer 式诊断，不顺手整体重写全文。
```

## 推荐提示词
### 第4章前半部分主起草提示词
```text
Use $doc-coauthoring.

Read first:
- G:\bishe\JLU-CCST-Thesis\文档\参考文献\写作计划\PLAN4.md
- G:\bishe\JLU-CCST-Thesis\thesis\paper-outline.md
- G:\bishe\JLU-CCST-Thesis\thesis\paper-evidence-map.md
- G:\bishe\JLU-CCST-Thesis\thesis\paper-writing-log.md
- G:\bishe\JLU-CCST-Thesis\文档\参考文献\第四章实验素材包\README.md
- G:\bishe\JLU-CCST-Thesis\文档\参考文献\第四章实验素材包\前半写作层\第四章实验环境与参数卡.md
- G:\bishe\JLU-CCST-Thesis\文档\参考文献\第四章实验素材包\前半写作层\第四章数据集概览卡.md
- G:\bishe\JLU-CCST-Thesis\文档\参考文献\第四章实验素材包\前半写作层\第四章baseline设计卡.md
- G:\bishe\JLU-CCST-Thesis\文档\参考文献\第四章实验素材包\前半写作层\第四章单变量实验设计卡.md
- G:\bishe\JLU-CCST-Thesis\文档\参考文献\第四章实验素材包\前半写作层\第四章前半图表建议清单.md
- G:\bishe\JLU-CCST-Thesis\thesis\chapter4-working-draft.md
- G:\bishe\JLU-CCST-Thesis\thesis\document.tex
- G:\bishe\JLU-CCST-Thesis\thesis\document.bib

Task:
创建并维护 `G:\bishe\JLU-CCST-Thesis\thesis\chapter4-working-draft.md`，按 `4.1 -> 4.2 -> 4.3 -> 4.4` 的顺序共写第4章前半部分。

Rules:
- 只读取 `README.md + 前半写作层/` 作为默认主起草入口。
- 不读取 `结果分析层/` 作为正文事实源。
- `4.1` 不抄写 host-specific 原始输出。
- `4.2` 保持 `Visium HD MouseBrain` 主线、`Human Ovarian` supporting、两个 Xenium workflow-support 的层级。
- `4.3` 不提前写 baseline 五项正式结果。
- `4.4` 不提前写 14 组实验结果、candidate 标签或 `promotion_review` 结论。
- 如 bibliography 尚未冻结，可先使用作者-年份式引用占位。
```

## 编译规则
- 只有在第4章前半部分已经并回 [document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex) 后，才执行编译。
- 编译 recipe：
  - VS Code LaTeX Workshop `latexmk (xelatex)`
- 配置来源：
  - [settings.json](/G:/bishe/JLU-CCST-Thesis/.vscode/settings.json)
- 输出目录：
  - `G:\bishe\JLU-CCST-Thesis\thesis\build\`

## 执行后同步
- 创建 `PLAN4.md` 后，至少同步：
  - [paper-writing-log.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-writing-log.md)
- 启动 `T-010` 并完成前半章 working draft 后，至少同步：
  - [paper-writing-log.md](/G:/bishe/JLU-CCST-Thesis/thesis/paper-writing-log.md)
  - [chapter4-working-draft.md](/G:/bishe/JLU-CCST-Thesis/thesis/chapter4-working-draft.md)
- 如果前半章已经并回正式骨架，再同步：
  - [document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex)
  - 必要时同步 [document.bib](/G:/bishe/JLU-CCST-Thesis/thesis/document.bib)
- 第4章正式 chapter-end reader testing 延后到 `T-011` 后，届时必须在日志中登记：
  - 是否执行
  - 主测读取范围
  - 是否做了“只读第4章”的补测
  - 是否完成修订闭环

## 验收标准
- `PLAN4.md` 已按 [PLAN_TEMPLATE.md](/G:/bishe/JLU-CCST-Thesis/文档/参考文献/写作计划/PLAN_TEMPLATE.md) 的结构创建，而不是自由发挥版本。
- `PLAN4.md` 明确只服务 `4.1 -> 4.4`，不提前扩展到 `4.5`。
- `PLAN4.md` 的默认读入入口明确为 `README.md + 前半写作层/`。
- `PLAN4.md` 已写死 `4.1` 到 `4.4` 的禁写点，不会把结果层内容前移。
- `PLAN4.md` 已写死唯一 working draft 为 [chapter4-working-draft.md](/G:/bishe/JLU-CCST-Thesis/thesis/chapter4-working-draft.md)。
- `PLAN4.md` 已写死 `4.1 -> 4.4` 稳定后允许先并回 [document.tex](/G:/bishe/JLU-CCST-Thesis/thesis/document.tex)。
- `PLAN4.md` 已区分 `T-010` 的 slice-end reviewer 诊断与 `T-011` 的正式 chapter-end reader testing。
- `PLAN4.md` 已写死编译方式为 [settings.json](/G:/bishe/JLU-CCST-Thesis/.vscode/settings.json) 中的 `latexmk (xelatex)`，输出到 `thesis/build/`。

## 禁止事项
- 不要把 `PLAN4.md` 写成整篇论文总计划。
- 不要让 `T-010` 默认读取 `结果分析层/`。
- 不要在 `4.1 -> 4.4` 提前写任何正式结果表、结果增量或 candidate 判断。
- 不要把 slice-end reviewer 诊断记录成“第4章正式 chapter-end reader testing 已完成”。
- 不要在第4章前半部分未稳定时提前进入 `$academic-paper-composer`。
