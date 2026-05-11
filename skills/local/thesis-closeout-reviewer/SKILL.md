---
name: thesis-closeout-reviewer
description: Diagnosis-only reviewer for an existing Chinese LaTeX graduation thesis in late-stage closeout. Use when the user wants to audit a full thesis or chapter without rewriting it, such as "整篇论文做收口审稿", "按 reviewer 视角检查全文", "先找问题不要直接改", "做复审/对抗性审稿/结构与证据审计", or "检查第4章/第5章是否还有 reviewer 级漏洞". It reads project authority documents and the supplied thesis text to produce a prioritized issue ledger with severity, issue type, evidence location, and suggested repair skill. Do not use it to draft or directly polish text.
---

# Thesis Closeout Reviewer

Use this skill as a project-specific audit layer for a Chinese LaTeX graduation thesis that already has a working draft.

## Core role

- Diagnosis only. Do not directly rewrite the manuscript.
- Read the project authorities before judging the text.
- Combine project-specific closeout checks with a reviewer-style pressure test.
- Output a repair queue, not polished prose.

## Public repository note

This repository preserves:

- review modes
- audit dimensions
- output ledger format
- routing boundaries

It does not include private thesis files or claim to mirror any single upstream repository.

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
- For later Word / DOCX packaging, use `academic-paper-composer`.

## Required reading

Read these files for every invocation:

1. `references/review-modes.md`
2. `references/output-template.md`

Read `references/audit-framework.md` whenever the task is a full review, chapter review, or re-review.

## Operating rules

- Always classify the request into exactly one review mode before auditing.
- Ground every finding in the supplied thesis text and the relevant authority docs.
- Separate structure, evidence, experiment-interpretation, and language-risk issues.
- Do not disguise a structural rewrite need as a polish issue.
