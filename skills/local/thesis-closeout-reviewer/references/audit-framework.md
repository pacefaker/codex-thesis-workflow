# Audit Framework

This skill combines project-specific closeout checks with a multi-perspective review mindset.

## Required project authorities

Always ground findings against:

- `paper-outline.md`: frozen structure and non-negotiable rules
- `paper-evidence-map.md`: allowed claims, forbidden claims, and chapter evidence boundaries
- `paper-writing-log.md`: current milestone, stage, and active routing rules

## Audit Dimension 1: Spec Audit

Check whether the text violates the frozen structure or chapter boundary rules.

Typical questions:

- Does this section write content that belongs to another chapter?
- Does it violate a non-negotiable rule from `paper-outline.md`?
- Does the chapter title promise one thing while the body delivers another?
- Does the text reopen a boundary that has already been frozen?

Common issue type label:

- `structure-boundary`

## Audit Dimension 2: Evidence Audit

Check whether claims are supported by the current evidence map.

Typical questions:

- Is the claim actually supported by the cited experiment, package, or chapter evidence?
- Has a supporting dataset been upgraded into a main line?
- Has a candidate result been written as a finalized conclusion?
- Has the abstract or conclusion moved beyond the stable evidence boundary?

Common issue type labels:

- `evidence-boundary`
- `citation-fact`

## Audit Dimension 3: AI Style Scrub Checklist

Check whether the prose carries high-risk formulaic patterns.

Look for:

- mechanical transitions
- inflated certainty
- empty praise adjectives
- abstract nouns with no concrete anchor
- repetitive sentence rhythm
- generic contribution claims without a tied fact

Common issue type label:

- `language-risk`

## Audit Dimension 4: Flow Appraisal

Check whether a fresh reader can follow the thesis without context loss.

Typical questions:

- Does the section open by clarifying its role?
- Is the connection to the previous chapter or previous paragraph visible?
- Are explanation layers in the right order: intuition first, then mechanism, then result?
- Does Chapter 4 explain why the results look this way, not just list them?
- Does Chapter 5 close the loop instead of merely restating headings?

Common issue type label:

- `chapter-flow`

## Multi-Perspective Overlay

Apply these reviewer mindsets after the 4 core dimensions:

### Methodology Reviewer

Use for:

- Chapter 4
- metric interpretation
- fairness of comparisons

Look for:

- ambiguous experiment setup
- unsupported result interpretation
- missing negative-result discussion

### Domain Reviewer

Use for:

- Chapter 2
- contribution framing
- theory and background positioning

Look for:

- background statements that overreach literature support
- method framing that confuses source method and current engineering implementation

### Perspective Reviewer

Use for:

- cross-chapter coherence
- reader-facing clarity

Look for:

- missing bridges
- sections that assume too much hidden context
- abrupt role changes of datasets or results

### Devil's Advocate

Use for:

- adversarial mode
- Chapter 5 summary claims
- abstract and conclusion stress test

Look for:

- strongest counter-argument against the main takeaway
- logical leaps
- cherry-picking of favorable interpretation
- "so what?" weakness

