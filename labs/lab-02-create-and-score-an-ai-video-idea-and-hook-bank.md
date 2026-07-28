# Lab 2 — Create and Score an AI Video Idea and Hook Bank

**Course:** Generative AI for Video Creation  
**Course Code:** C1373  
**Version:** v1.0 (28 July 2026)  
**Topic 1:** Getting Started with Generative AI for TikTok  
**Maps to:** LO1: connect audience needs and recommendation signals to truthful, testable short-form video concepts  
**Duration:** 55 minutes  
**Tools:** Spreadsheet · text editor · AI assistant · idea-hook-bank-template.csv

---

## Goal

Generate meaningfully different concepts and select one primary hook plus one controlled alternate using explicit criteria.

## What You Will Do

You will turn the Lab 1 brief into an idea bank across mistake, demonstration, comparison, myth, checklist and story angles. You will write verbal, visual and text-overlay hooks, reject misleading options and score the survivors before locking the Harbour Bean production concept.

## What You Will Build

A completed 02-idea-hook-bank.csv with twelve concepts and a 02-selected-concept.md with the chosen angle, primary hook, alternate hook, body promise, proof source, next action, production risks and a one-variable future test.

## Prerequisites

- Completed 01-audience-prompt-brief.md from Lab 1.
- Open labs/assets/idea-hook-bank-template.csv.
- Use the same synthetic audience, proof, voice and red lines from the approved brief.

> **Data note.** Use only the supplied synthetic scenario or material you are authorised to use. Do not clone a real person's face or voice, copy another creator's identity, or use unlicensed music. Verify claims, rights, accessibility and AI disclosure before any external use.

## Steps

### 1. Save a copy of idea-hook-bank-template.csv as 02-idea-hook-bank.csv. Ask the AI assistant for two concepts in each angle family: mistake, demonstration, comparison, myth, checklist and story. Require every row to include audience tension, useful promise, supporting source and a feasible 25–35 second production path. Transfer exactly twelve rows to the sheet.

```text
Using the approved Harbour Bean brief below, create exactly 12 short-video concepts: 2 mistake, 2 demonstration, 2 comparison, 2 myth, 2 checklist and 2 story. Use only supplied proof. Output CSV-ready columns: ID, angle family, audience tension, promise, proof source, scene mechanism, next action, risk.
<PASTE LAB 1 APPROVED BRIEF>
```

### 2. For each concept write three hook channels in the sheet: Spoken hook, First visual and On-screen text. The three should reinforce the same promise without repeating identical words. If an option uses false urgency, guaranteed results, withheld context, unrelated trends or imitation of a recognisable creator, record its ID and rejection reason under Rejected ideas in 02-selected-concept.md, then replace it with a new eligible concept from the same angle family. Continue until the sheet contains exactly twelve eligible rows.

```text
Hook check: clear audience problem | specific promised value | body can fulfil it | no invented urgency | no copied identity.
Replacement rule: log the rejected ID and reason, then replace it in the CSV so exactly 12 eligible rows remain.
```

### 3. Score every remaining concept from 1 to 5 for Audience fit, Clarity, Source support, Distinctiveness and Production feasibility. Calculate Total as the sum of the five scores. Add a Decision note that explains any score below 3; do not change a score merely to make a favourite idea win.

```text
Spreadsheet formula for row 2 Total: =SUM(I2:M2)
Use the equivalent columns if your spreadsheet places the five score fields elsewhere.
```

### 4. Filter Total from highest to lowest. Choose one primary concept only after reading its risk and source fields. Choose one alternate with the same body promise but a different opening channel so it can become a one-variable hook test. Create 02-selected-concept.md using the required headings below.

```text
Headings: Audience job | Angle | Primary spoken hook | Primary first visual | Primary on-screen text | Alternate hook | Body promise | Approved proof | Next action | Production risks | Test variable | Keep constant
```

### 5. Run a fulfilment check with a partner or the AI assistant as critic. Give only the selected hook and body promise. Ask what the viewer expects to receive, compare that expectation with the planned body and edit any mismatch. Record the original wording, final wording and reason under Hook fulfilment check.

```text
Critique this hook and body promise. State (1) what a reasonable viewer expects, (2) whether the body fulfils it, (3) any misleading implication, and (4) the smallest repair. Do not propose a more sensational hook.
```

## Test It

02-idea-hook-bank.csv must contain exactly twelve eligible rows across all six angle families, three hook channels per row, five numeric scores, a total and decision note. 02-selected-concept.md must contain every required heading, one primary and one alternate hook, one stated test variable, at least three keep-constant items, the before/after fulfilment check and a Rejected ideas log containing every replaced ID and reason, or the line 'No ideas rejected'.

## Checkpoint and Rejoin Point

Keep both Lab 2 files. Lab 3 uses the selected audience, angle, primary hook, alternate hook, body promise and verified proof to build the timed script and storyboard.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The twelve ideas differ only in wording. | Regenerate by angle family and require a different evidence mechanism or scene treatment per family. |
| Every concept receives the same score. | Write observable anchors for 1, 3 and 5, then rescore one criterion at a time across all rows. |
| The highest score is difficult to produce. | Lower its feasibility score honestly or simplify the scene mechanism while preserving the promise. |

## Challenge

Design a visual-first alternate that communicates the same truthful promise before any spoken word. Explain which audience signal it is intended to improve and why that remains only a hypothesis.

## Reflection

Which selection criterion changed your initial preference, and what does that reveal about creative judgement?

---

[← Lab 1](lab-01-build-the-audience-tool-and-ai-prompt-brief.md) · [Lab 3 →](lab-03-write-the-timed-script-caption-and-storyboard-pack.md)
