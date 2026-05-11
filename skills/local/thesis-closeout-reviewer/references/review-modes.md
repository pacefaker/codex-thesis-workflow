# Review Modes

Use exactly one mode per invocation.

## `full`

Use for:

- "整篇论文做收口审稿"
- "按 reviewer 视角检查全文"
- first-pass full-thesis diagnosis

Behavior:

- Audit the whole supplied thesis text.
- Output the highest-priority 8 to 15 issues.
- Cover all 5 closeout classes:
  - structure boundary
  - evidence boundary
  - chapter flow
  - experiment interpretation
  - language risk

## `re-review`

Use for:

- "复审"
- "检查修改后还剩什么问题"
- a second pass after one repair round

Behavior:

- Compare the repaired text against the previously identified issue classes.
- Focus on unresolved issues, partial fixes, and newly introduced regressions.
- Do not restate every old issue if it has clearly been resolved.

## `chapter4-focus`

Use for:

- Chapter 4 only
- experiment design and result interpretation checks

Behavior:

- Prioritize evidence boundary, fairness of claims, negative-result honesty, and "why this happened" explanation depth.
- Flag result statements that outrun the actual metrics or visuals.

## `chapter5-focus`

Use for:

- Chapter 5 only
- conclusion and future-work checks

Behavior:

- Prioritize summary honesty, contribution framing, limitation handling, and future-work realism.
- Flag over-claiming and speculative statements presented as completed results.

## `adversarial`

Use for:

- "对抗性审稿"
- "最苛刻地找问题"
- "按 Devil's Advocate 角度看"

Behavior:

- Stress-test core claims, logic chains, and hidden assumptions.
- Prefer fewer but sharper issues.
- Elevate only problems that could materially damage credibility.

## `language-risk`

Use for:

- "先找语言风险"
- "先标出像模板化 AI 写作的句子"

Behavior:

- Focus on high-risk wording in abstract, introduction, and conclusion.
- Do not turn this into a broad structural review unless the text itself creates misunderstanding.

