# Lab 8 — Analyse Performance and Build the Scaled Improvement Plan

**Course:** Generative AI for Video Creation  
**Course Code:** C1373  
**Version:** v1.0 (28 July 2026)  
**Topic 4:** Publishing, Optimising and Scaling TikTok Content  
**Maps to:** LO4: interpret post metrics cautiously, choose a one-variable iteration and govern a repeatable production workflow  
**Duration:** 60 minutes  
**Tools:** Spreadsheet · text editor · AI assistant · synthetic-tiktok-analytics.csv · Lab 4 calendar

---

## Goal

Turn a bounded synthetic dataset into observations, alternative explanations, one controlled next test and a 30-day production board.

## What You Will Do

You will analyse supplied synthetic TikTok post data, use AI to organise—but not invent—findings, select one variable for the next version and convert the Lab 4 calendar into a governed production board with owners, gates, measures and stop rules.

## What You Will Build

A completed 08-performance-calculations.csv, an 08-performance-iteration-plan.md and 08-production-board.csv with traceable observations, alternative explanations, a controlled test, workflow states, owners, entry/exit gates and a 30-day learning cadence.

## Prerequisites

- Completed 04-content-calendar.csv and 07-publish-and-repurpose-pack.md.
- Open labs/assets/synthetic-tiktok-analytics.csv and labs/assets/production-board.csv.
- Treat every supplied metric as synthetic classroom data; do not infer real audience behaviour.

> **Data note.** Use only the supplied synthetic scenario or material you are authorised to use. Do not clone a real person's face or voice, copy another creator's identity, or use unlicensed music. Verify claims, rights, accessibility and AI disclosure before any external use.

## Steps

### 1. Create 08-performance-iteration-plan.md and add Publication and adaptation hand-off. Copy from Lab 7 the exact final decision, primary destination, one destination-specific adaptation change and approval owner. If Lab 7 is BLOCKED, name the unresolved item and carry it into the Blocker field of every affected production-board row; do not treat private practice as external approval.

```text
Required hand-off fields: Lab 7 final decision | Primary destination | Adaptation change | Approval owner | Unresolved blocker or NONE.
```

### 2. Save synthetic-tiktok-analytics.csv as 08-performance-calculations.csv. Add the columns Two-second hold, Six-second hold, Completion rate, Engagement rate and Action rate. In row 2 calculate each as the relevant count divided by Views: 2-second views, 6-second views, Completed views, Likes+Comments+Shares+Saves, and Profile visits+Link clicks. Format as percentages and fill the formulas down. Check that every result is between 0% and 100%.

```text
If Views is column C: Two-second hold =D2/C2; Six-second hold =E2/C2; Completion rate =F2/C2; Engagement rate =SUM(H2:K2)/C2; Action rate =SUM(L2:M2)/C2.
Adjust letters only after matching the actual headers.
```

### 3. Continue in the existing 08-performance-iteration-plan.md. Add Context, Comparable baseline, Observations, Alternative explanations, Missing evidence, Decision and Review window. Compare videos with the same audience and similar duration before comparing the calculated rates. Write at least four numeric observations that name the video and metric; do not use causal words in this section.

```text
Observation pattern: Video <ID> has <METRIC> of <VALUE>, compared with <BASELINE VALUE> for <COMPARABLE SET>.
Banned in observations: caused | proves | because | algorithm prefers.
```

### 4. Paste only the table and your four observations into the AI assistant. Ask it to check calculations, suggest at least two alternative explanations per material pattern and list missing evidence. Require it to distinguish OBSERVATION, HYPOTHESIS and QUESTION. Verify every number against the spreadsheet and delete any unsupported platform explanation.

```text
Review the synthetic table below. (1) Check arithmetic, (2) separate observations from hypotheses, (3) give at least two plausible alternatives per pattern, (4) list missing evidence, and (5) do not claim causation or a universal platform rule. Use only the supplied table.
<PASTE TABLE AND OBSERVATIONS>
```

### 5. Choose one next-version variable: primary hook, beat-two duration, first visual, caption density or close. State why it is linked to a specific observation, then define Keep constant, Baseline, Success signal, Guardrail, Minimum review window and Stop/continue rule. Use the Lab 2 alternate hook when hook is selected; otherwise preserve both hooks and document the single changed element.

```text
Test statement: Change <ONE VARIABLE> from <A> to <B> for <AUDIENCE>. Keep <AT LEAST FOUR ITEMS> constant. Compare <RELEVANT RATE> against <BASELINE> after <WINDOW>. Stop or revise if <GUARDRAIL>.
```

### 6. Save production-board.csv as 08-production-board.csv and transfer the next six eligible rows from the Lab 4 calendar. An eligible row has a named owner, a source, a rights/disclosure state other than BLOCKED, and a current workflow state of Brief or later. Use only Brief, Script, Assets, Edit, Review, Scheduled and Learn states. Complete Owner, Evidence source, Required artifact, Entry gate, Exit gate, Rights/disclosure, Planned date, Learning hypothesis, Success signal and Blocker. A row with missing evidence, rights or owner must stay in its last valid workflow state, have a nonblank Blocker field and may not enter Scheduled.

```text
State gates: Brief requires audience+purpose+proof | Script requires verified claims+timing | Assets requires register+rights | Edit requires accepted media | Review requires quality log | Scheduled requires publish gate+owner | Learn requires comparable metrics+decision.
```

### 7. In 08-performance-iteration-plan.md add 30-day cadence and process controls. Name weekly brief, production, approval and learning review points. Track median cycle time, items blocked by rights, first-review defects, rework count and posts with a documented learning decision. Add stop rules for unverified claims, missing permission, misleading synthetic media and repeated quality failure.

```text
Volume is not the primary control. Scale only when every item can be traced from source brief to asset register, approval and learning decision.
```

## Test It

08-performance-calculations.csv must contain all five rate columns with valid percentages for every row. 08-performance-iteration-plan.md must contain the five Lab 7 hand-off fields, four checked numeric observations, at least two alternative explanations for each material pattern, missing evidence, exactly one changed variable, four or more keep-constant items, a baseline, success signal, guardrail, window and stop/continue rule. 08-production-board.csv must contain six rows, valid states, all ten governance fields and no blocked item in Scheduled. The iteration plan must also contain all four weekly cadence points, all five named process measures and all four stop rules.

## Checkpoint and Rejoin Point

The Lab 8 files complete the C1373 portfolio. To rejoin later, start with the selected production-board row, follow its entry gate and use the iteration plan's keep-constant list before changing the next video.

## Troubleshooting

| If this happens | Fix |
|---|---|
| A calculated percentage exceeds 100%. | Check the header-to-column mapping, denominator and whether counts were added twice. |
| AI invents a reason for the performance change. | Relabel it HYPOTHESIS, require an alternative explanation and state the missing evidence. |
| The production board has too many items in progress. | Limit active work, clear blockers and finish review gates before starting more briefs. |

## Challenge

Perform a sensitivity check with a second comparable baseline and explain whether the same one-variable test remains the best next step.

## Reflection

Which metric or workflow measure would be most dangerous to optimise in isolation, and why?

---

[← Lab 7](lab-07-prepare-the-publish-disclosure-and-repurposing-pack.md) · [Labs index →](README.md)
