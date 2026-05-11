---
name: thesis-closeout-reviewer
description: Diagnosis-only reviewer for an existing Chinese LaTeX graduation thesis in late-stage closeout. Use when the user wants to audit a full thesis or chapter without rewriting it, such as "整篇论文做收口审稿", "按 reviewer 视角检查全文", "先找问题不要直接改", "做复审/对抗性审稿/结构与证据审计", or "检查第4章/第5章是否还有 reviewer 级漏洞". It reads `paper-outline.md`, `paper-evidence-map.md`, `paper-writing-log.md`, and the provided thesis text to produce a prioritized issue ledger with severity, issue type, evidence location, and suggested repair skill. Do not use it to draft or directly polish text.
---

# Thesis Closeout Reviewer

Use this skill as a project-specific audit layer for a Chinese LaTeX graduation thesis that already has a working draft.

## Core role

- Diagnosis only. Do not directly rewrite the manuscript.
- Read the project authorities before judging the text:
  - `paper-outline.md`
  - `paper-evidence-map.md`
  - `paper-writing-log.md`
- Combine two audit sources:
  - the 4 closeout audit dimensions adapted from `content-review-agent`
  - the multi-perspective review mindset adapted from `academic-paper-reviewer`
- Output a repair queue, not polished prose.

## When to use

Use this skill for:

- full-thesis closeout review
- reviewer-style diagnosis before revision
- re-review after one repair round
- Chapter 4 / Chapter 5 focused audit
- adversarial challenge of claims, boundaries, or logic
- language-risk screening before final style cleanup

## When not to use

- For local rewriting, shortening, expansion, logic repair, experiment analysis, or captions, use `graduation-thesis-editor`.
- For section-level reopening and coauthoring, use `doc-coauthoring`.
- For explicit de-AI or final language cleanup, use `humanizer`.
- For Word/DOCX submission packaging, use `academic-paper-composer`.

## Required reading

Read these files for every invocation:

1. `references/review-modes.md`
2. `references/output-template.md`

Read `references/audit-framework.md` whenever the task is a full review, chapter review, or re-review.

## Operating rules

- Always classify the request into exactly one review mode before auditing.
- Ground every finding in the thesis authorities or the supplied manuscript text.
- Do not invent evidence gaps that are contradicted by `paper-evidence-map.md`.
- Do not upgrade a stylistic dislike into a structural defect unless it creates reader misunderstanding.
- Prioritize issues that affect:
  - structure boundary
  - evidence boundary
  - cross-chapter coherence
  - experiment interpretation
  - language risk
- Suggest exactly one primary repair skill for each issue.
- If `deep-research` is not available locally, still use it as a recommendation label only when the issue is truly evidence-seeking.
- If no major issue exists, say so explicitly and return only residual risks plus optional polish opportunities.

## Default workflow

1. Read the three project authorities.
2. Choose one review mode from `references/review-modes.md`.
3. Load the audit dimensions from `references/audit-framework.md`.
4. Inspect the supplied text only through a diagnosis lens.
5. Output the issue ledger using `references/output-template.md`.
6. Stop after diagnosis. Do not drift into editing.

