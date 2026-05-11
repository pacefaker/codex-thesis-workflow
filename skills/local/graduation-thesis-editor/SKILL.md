---
name: graduation-thesis-editor
description: Local editing toolkit for an existing Chinese LaTeX graduation thesis. Use when the user already has draft text, notes, experiment results, figures, or captions and needs localized thesis tasks such as translation, rewriting, shortening, expansion, polishing, logic checking, reviewer-style diagnosis of a provided section, experiment analysis from provided data, or figure and table captions. Route every request to exactly one canonical task family before editing. Do not use as the main zero-to-one writing workflow; prefer doc-coauthoring for full coauthoring from a blank page or multi-stage drafting.
---

# Graduation Thesis Editor

Use this skill as a local paragraph-and-section editing toolkit for a Chinese LaTeX graduation thesis.

## Core rules

- Assume the default target is a Chinese LaTeX graduation thesis unless the user clearly asks for another format.
- Preserve the user's meaning, claims, numbers, terminology, and notation.
- Do not fabricate citations, experimental conclusions, statistical significance, or reviewer opinions.
- For LaTeX-generation tasks, output clean LaTeX only unless the user explicitly asks for explanation.
- For Chinese explanation tasks, output natural Chinese only and avoid LaTeX noise unless required.
- Keep revisions proportional. Do not over-edit passages that are already acceptable.
- Treat this skill as local editing support, not as the primary blank-page writing workflow.
- Always route before editing. Do not improvise a new task family when an existing route already matches.
- Use exactly one route per invocation. If a request is mixed, split it into serial subtasks.

## Public repository note

This public repository preserves:

- route design
- task contracts
- local adaptation logic
- handoff boundaries

It does not preserve high-risk third-party long prompt text verbatim.

## Routing protocol

Read `references/workflow.md` and `references/routing.md` first for every invocation.

Then follow this order:

1. Decide whether the request belongs to this skill at all.
2. If it is a blank-page, chapter-planning, or staged coauthoring task, hand off to `doc-coauthoring`.
3. If the user explicitly asks for final de-AI cleanup, prefer `humanizer` unless they explicitly require the internal fallback route.
4. Normalize the request into one atomic task.
5. Select exactly one `Route ID` from `references/routing.md`.
6. Read only the single reference file and section named by that route.
7. Execute using the public-safe route contract for that task.

## Required execution record

Before execution, report:

- `Route ID`
- `Prompt Source`
- `Prompt Snapshot Type`

Default expected value:

- `Prompt Snapshot Type: public-safe summary`

## Route families

- `translation.md`: translation and note-to-prose rewriting
- `revision.md`: shortening, expansion, polishing, logic checking, and internal de-AI fallback
- `analysis.md`: experiment analysis and reviewer-style diagnosis
- `figures.md`: figure captions, table captions, diagram briefs, and plot/title guidance

## Handoff boundary

- If the user is starting from a blank page, needs full chapter planning, wants staged coauthoring, or asks for an end-to-end writing workflow, prefer `doc-coauthoring`.
- If the user is drafting an entire chapter from outline and evidence files rather than editing existing prose, prefer `doc-coauthoring`.
- Use this skill after there is already material to edit, analyze, translate, or critique.
