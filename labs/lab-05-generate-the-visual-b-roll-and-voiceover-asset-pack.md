# Lab 5 — Generate the Visual, B-Roll and Voiceover Asset Pack

**Course:** Generative AI for Video Creation  
**Course Code:** C1373  
**Version:** v1.0 (28 July 2026)  
**Topic 3:** Creating and Editing Videos with Generative AI  
**Maps to:** LO3: create brand-consistent candidate media and document provenance, rights, continuity and disclosure decisions  
**Duration:** 60 minutes  
**Tools:** CapCut Desktop/AI video or approved generator · microphone or text-to-speech · spreadsheet · text editor

---

## Goal

Produce or prototype every media element required by the Lab 3 storyboard and reject defective or untraceable candidates before editing.

## What You Will Do

You will translate the timed storyboard into precise visual and voice prompts, create candidate media with CapCut AI or another approved generator, and complete an asset register. If a generation feature is unavailable, you will use the same prompt with an approved alternative or create a storyboard placeholder in CapCut so the edit can still be completed.

## What You Will Build

A 03-media folder with accepted scene assets, plus any project-only placeholder clips, a voiceover track or recorded scratch narration, a 05-asset-register.csv and a 05-contact-sheet-review.md documenting prompt, version, source, continuity, rights, disclosure and accept/reject decisions.

## Prerequisites

- Completed 03-video-script-storyboard.md and 04-brand-prompt-kit.md.
- Open labs/assets/asset-register.csv.
- Do not upload a real person's face, voice, private footage or protected brand asset without permission.

> **Data note.** Use only the supplied synthetic scenario or material you are authorised to use. Do not clone a real person's face or voice, copy another creator's identity, or use unlicensed music. Verify claims, rights, accessibility and AI disclosure before any external use.

## Steps

### 1. Create 05-contact-sheet-review.md and copy the six or more storyboard beats from Lab 3. For each beat state its Shot function, Required subject/action, Evidence need, Media type and Fallback. Name files using scene-purpose-version, for example S01-bitter-cup-v01.mp4. A fallback may be an authorised stock clip, self-recorded neutral object shot or a labelled colour-and-text placeholder.

```text
Required functions across the pack: orient | demonstrate | prove | transition | close.
Required folder: C1373-work/03-media.
Naming: S<NN>-<purpose>-v<NN>.<ext>
```

### 2. For each generated beat, write a media prompt using Subject, Action, Setting, Camera, Lighting, Composition, Brand anchors and Exclusions. In CapCut Desktop choose AI video maker, then Instant AI video when available; enter the prompt or Lab 3 script, select a vertical 9:16 ratio and an appropriate realistic or minimal style. Generate no more than two candidates for that beat and stop as soon as one passes the acceptance rule; create no more than twelve generated candidates in the whole lab. If generation is unavailable, create an exact project-only fallback: New project > Ratio > 9:16 > Text > Add text; type '[PLACEHOLDER — <ASSET ID>: <SHOT FUNCTION>]'; choose Canvas > Color and set navy; drag the text layer to two seconds; duplicate and relabel it for each missing beat. Save the project as C1373-placeholders and register each item as project-only.

```text
Prompt example: Close overhead view of neutral adult hands making pour-over coffee in a clean office pantry; steady circular pour into copper dripper; soft daylight; 9:16 composition with upper and lower text-safe space; navy surface and cream mug; no logos, text, extra fingers, changing dripper, steam obscuring the action or camera shake.
Stop rule: maximum 2 candidates per beat and 12 total; stop earlier when one candidate passes.
```

### 3. Generate or record the final narration in short segments. For CapCut text-to-speech, open a project, add Text, paste one script segment, select Text to speech, choose an available licensed synthetic voice and generate. Preview the pronunciation of 'Harbour Bean' and 'one to sixteen ratio' first. Alternatively record an authorised scratch voice. On Windows open Start > Sound Recorder; on macOS open Applications > Voice Memos. Select the microphone, press Record, read one script segment, press Stop, rename the recording VO-v01 and place or import it into 03-media. Note whether the voice is synthetic or human-authorised.

```text
Voice check: exact final script | natural pace | key terms correct | no added words | identity not misleading | disclosure path recorded.
```

### 4. Save asset-register.csv as 05-asset-register.csv. Create one row for every generated, recorded, stock or placeholder asset. Complete Asset ID, Filename, Beat, Tool/source, Prompt/source URL, Generation date, Version, Rights basis, Likeness/voice permission, AI alteration, Disclosure need, Continuity status, Quality status, Decision and Notes. Do not leave rights or permission blank.

```text
Allowed decisions: ACCEPT | REVISE | REJECT | PLACEHOLDER.
Allowed rights basis examples: original self-recording | licensed generator output under current account terms | authorised stock with source URL | classroom placeholder only.
```

### 5. Review every candidate at full size and playback speed. In 05-contact-sheet-review.md add one row per asset covering Object continuity, Human anatomy/likeness, Motion, Text/logo artefacts, Brand fit, Crop/safe zone and Scene function. Reject material defects; do not plan to hide them with a fast edit. Confirm that at least one accepted asset or explicit placeholder exists for every beat.

```text
Acceptance rule: the asset performs the beat's stated job, contains no misleading detail, has a known rights basis and can be used safely in a 9:16 edit.
```

## Test It

The 03-media folder must contain accepted scene assets for every generated or recorded file, while C1373-placeholders may supply missing beats as explicitly registered project-only clips; together they must cover at least six storyboard beats plus a voice track or scratch narration. 05-asset-register.csv must have a complete row for every generated, recorded or project-only item with no blank rights, permission, AI alteration, disclosure, continuity, quality or decision field. 05-contact-sheet-review.md must have one row for every candidate and placeholder. Asset files, project-only placeholders, register rows and review rows must reconcile one to one; no rejected asset may be marked for use.

## Checkpoint and Rejoin Point

Keep the media folder, the C1373-placeholders CapCut project, 05-asset-register.csv and 05-contact-sheet-review.md together. Lab 6 opens the placeholder project as its editing base when project-only clips exist, imports only ACCEPT files, and carries disclosure and rights notes into the export gate.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Text-to-video changes the product or hands between frames. | Simplify the motion, shorten the prompt or use an authorised still with a slow keyframed camera move. |
| The generator menu is unavailable or requires a different plan. | Use an approved alternative or the labelled CapCut placeholder; keep the same storyboard and register fields. |
| The synthetic voice mispronounces a phrase. | Split the line, add punctuation or phonetic spelling, and regenerate only that segment. |

## Challenge

Create a second accepted version of one scene with a different camera treatment but identical subject, action, evidence and brand anchors. Compare which better fulfils the shot function.

## Reflection

Which rejected asset looked attractive at first, and which documented quality gate prevented it from entering the edit?

---

[← Lab 4](lab-04-build-the-brand-prompt-kit-and-four-week-content-system.md) · [Lab 6 →](lab-06-edit-caption-mix-and-export-the-vertical-video.md)
