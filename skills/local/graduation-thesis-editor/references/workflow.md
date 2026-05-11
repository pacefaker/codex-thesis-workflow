# Graduation thesis local editor guide

Use this document to decide when this skill should be used locally and when another skill should take over.

## What this skill is for

Use this skill when there is already material on the table and the job is local editing or support work.

Typical tasks:

- translate Chinese draft text into English LaTeX
- translate English LaTeX into readable Chinese
- rewrite rough Chinese notes into academic prose
- shorten, expand, polish, or logic-check an existing passage
- analyze experiment tables or metric summaries
- review a provided section from a reviewer-like angle
- write figure captions, table captions, or diagram briefs

## What this skill is not for

Do not treat this skill as the main zero-to-one thesis workflow.

Do not use it as the first choice when the user needs:

- blank-page thesis planning
- staged coauthoring from topic to chapter structure
- iterative document building across multiple writing rounds
- reader-testing style workflow for an entire chapter or paper

For those cases, prefer `doc-coauthoring`.

## How to use it

Choose the smallest matching task and route to one reference only unless the request clearly combines multiple local tasks.

- `translation.md`: translation and note-to-prose rewriting
- `revision.md`: shortening, expansion, polishing, logic checking, and de-AI fallback
- `analysis.md`: experiment analysis and reviewer-style diagnosis
- `figures.md`: figure captions, table captions, and diagram briefs

## Recommended handoff order

If the user is writing from scratch:

1. Use `doc-coauthoring` to plan and coauthor the document.
2. Return to this skill for section-level editing, experiments, figures, and local cleanup.
3. Use `humanizer` only for explicit final style cleanup.

If the user already has a draft:

1. Use this skill directly for the local task.
2. Bring in `humanizer` only when the user explicitly asks for de-AI cleanup.
