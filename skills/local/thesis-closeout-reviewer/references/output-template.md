# Output Template

The output must be diagnosis-only.

## Required structure

### 1. Review Verdict

Use 2 to 4 short bullets:

- current overall risk
- strongest issue cluster
- whether immediate rewrite is needed or only targeted repair

### 2. Issue Ledger

Use a flat table with these columns:

| ID | Severity | Issue Type | Evidence Location | Why It Matters | Suggested Repair Skill |
| --- | --- | --- | --- | --- | --- |

Rules:

- `Severity` must be one of: `P0`, `P1`, `P2`, `P3`
- `Issue Type` should usually be one of:
  - `structure-boundary`
  - `evidence-boundary`
  - `chapter-flow`
  - `experiment-interpretation`
  - `language-risk`
  - `citation-fact`
  - `figure-table`
- `Evidence Location` must point to a concrete place in the supplied text or authority docs
- `Suggested Repair Skill` must be exactly one of:
  - `graduation-thesis-editor`
  - `doc-coauthoring`
  - `humanizer`
  - `deep-research`
  - `academic-plotting`
  - `academic-paper-composer`

### 3. Repair Order

Give 3 to 6 ordered bullets.

Rules:

- Fix structure and evidence before style.
- Put Chapter 4 and Chapter 5 ahead of cosmetic wording if both are present.
- If a section must be reopened, say so explicitly instead of disguising it as a polish issue.

### 4. Re-Review Trigger

End with one short line:

- `适合直接进入修复`
- `适合修复后再做 re-review`
- `需要先补证据再修文`

## Severity definitions

- `P0`: blocking credibility problem; must be fixed before any polish
- `P1`: major reviewer-visible problem; should be fixed in the current round
- `P2`: moderate weakness; fix if time allows after core issues
- `P3`: minor polish or residual risk

## Routing guidance

- Use `graduation-thesis-editor` for local repair, local logic checks, experiment analysis strengthening, and captions.
- Use `doc-coauthoring` when a section needs true structural reopening or staged rewriting.
- Use `humanizer` only for final style cleanup on stable narrative sections.
- Use `deep-research` only when the problem is genuinely evidence-seeking.
- Use `academic-plotting` only when a figure or chart is the cleanest fix.
- Use `academic-paper-composer` only for later Word/DOCX packaging or submission-stage rework.

## Forbidden output behavior

- Do not rewrite the manuscript inline.
- Do not merge diagnosis and repair into one step.
- Do not recommend more than one primary repair skill per issue.
- Do not pad the issue list with trivialities if only a few issues truly matter.

