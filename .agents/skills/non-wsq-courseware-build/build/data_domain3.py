"""Topic 3 labs for C1373."""

DOMAIN3 = [
    dict(
        num=5,
        topic=3,
        title="Generate the Visual, B-Roll and Voiceover Asset Pack",
        duration=60,
        objective="LO3: create brand-consistent candidate media and document provenance, rights, continuity and disclosure decisions",
        goal="Produce or prototype every media element required by the Lab 3 storyboard and reject defective or untraceable candidates before editing.",
        workflow=["Plan shot functions", "Generate small batches", "Review continuity", "Register every asset"],
        desc=(
            "You will translate the timed storyboard into precise visual and voice prompts, create candidate "
            "media with CapCut AI or another approved generator, and complete an asset register. If a generation "
            "feature is unavailable, you will use the same prompt with an approved alternative or create a "
            "storyboard placeholder in CapCut so the edit can still be completed."
        ),
        build=(
            "A 03-media folder with accepted scene assets, plus any project-only placeholder clips, a voiceover track or "
            "recorded scratch narration, a 05-asset-register.csv and a 05-contact-sheet-review.md documenting "
            "prompt, version, source, continuity, rights, disclosure and accept/reject decisions."
        ),
        services="CapCut Desktop/AI video or approved generator · microphone or text-to-speech · spreadsheet · text editor",
        prerequisites=[
            "Completed 03-video-script-storyboard.md and 04-brand-prompt-kit.md.",
            "Open labs/assets/asset-register.csv.",
            "Do not upload a real person's face, voice, private footage or protected brand asset without permission.",
        ],
        steps=[
            (
                "Create 05-contact-sheet-review.md and copy the six or more storyboard beats from Lab 3. For each "
                "beat state its Shot function, Required subject/action, Evidence need, Media type and Fallback. "
                "Name files using scene-purpose-version, for example S01-bitter-cup-v01.mp4. A fallback may be an "
                "authorised stock clip, self-recorded neutral object shot or a labelled colour-and-text placeholder.",
                "Required functions across the pack: orient | demonstrate | prove | transition | close.\nRequired folder: C1373-work/03-media.\nNaming: S<NN>-<purpose>-v<NN>.<ext>",
            ),
            (
                "For each generated beat, write a media prompt using Subject, Action, Setting, Camera, Lighting, "
                "Composition, Brand anchors and Exclusions. In CapCut Desktop choose AI video maker, then Instant "
                "AI video when available; enter the prompt or Lab 3 script, select a vertical 9:16 ratio and an "
                "appropriate realistic or minimal style. Generate no more than two candidates for that beat and "
                "stop as soon as one passes the acceptance rule; create no more than twelve generated candidates "
                "in the whole lab. If generation is unavailable, create an exact project-only fallback: New project > "
                "Ratio > 9:16 > Text > Add text; type '[PLACEHOLDER — <ASSET ID>: <SHOT FUNCTION>]'; choose "
                "Canvas > Color and set navy; drag the text layer to two seconds; duplicate and relabel it for each "
                "missing beat. Save the project as C1373-placeholders and register each item as project-only.",
                "Prompt example: Close overhead view of neutral adult hands making pour-over coffee in a clean office pantry; steady circular pour into copper dripper; soft daylight; 9:16 composition with upper and lower text-safe space; navy surface and cream mug; no logos, text, extra fingers, changing dripper, steam obscuring the action or camera shake.\nStop rule: maximum 2 candidates per beat and 12 total; stop earlier when one candidate passes.",
            ),
            (
                "Generate or record the final narration in short segments. For CapCut text-to-speech, open a project, "
                "add Text, paste one script segment, select Text to speech, choose an available licensed synthetic "
                "voice and generate. Preview the pronunciation of 'Harbour Bean' and 'one to sixteen ratio' first. "
                "Alternatively record an authorised scratch voice. On Windows open Start > Sound Recorder; on "
                "macOS open Applications > Voice Memos. Select the microphone, press Record, read one script segment, "
                "press Stop, rename the recording VO-v01 and place or import it into 03-media. Note whether the "
                "voice is synthetic or human-authorised.",
                "Voice check: exact final script | natural pace | key terms correct | no added words | identity not misleading | disclosure path recorded.",
            ),
            (
                "Save asset-register.csv as 05-asset-register.csv. Create one row for every generated, recorded, "
                "stock or placeholder asset. Complete Asset ID, Filename, Beat, Tool/source, Prompt/source URL, "
                "Generation date, Version, Rights basis, Likeness/voice permission, AI alteration, Disclosure need, "
                "Continuity status, Quality status, Decision and Notes. Do not leave rights or permission blank.",
                "Allowed decisions: ACCEPT | REVISE | REJECT | PLACEHOLDER.\nAllowed rights basis examples: original self-recording | licensed generator output under current account terms | authorised stock with source URL | classroom placeholder only.",
            ),
            (
                "Review every candidate at full size and playback speed. In 05-contact-sheet-review.md add one row "
                "per asset covering Object continuity, Human anatomy/likeness, Motion, Text/logo artefacts, Brand "
                "fit, Crop/safe zone and Scene function. Reject material defects; do not plan to hide them with a "
                "fast edit. Confirm that at least one accepted asset or explicit placeholder exists for every beat.",
                "Acceptance rule: the asset performs the beat's stated job, contains no misleading detail, has a known rights basis and can be used safely in a 9:16 edit.",
            ),
        ],
        test=(
            "The 03-media folder must contain accepted scene assets for every generated or recorded file, while "
            "C1373-placeholders may supply missing beats as explicitly registered project-only clips; together they "
            "must cover at least six storyboard beats plus a voice track or scratch narration. "
            "05-asset-register.csv must have a complete row for every generated, recorded or project-only item "
            "with no blank rights, permission, AI alteration, disclosure, continuity, quality or decision field. "
            "05-contact-sheet-review.md must have one row for every candidate and placeholder. Asset files, "
            "project-only placeholders, register rows and review rows must reconcile one to one; no rejected asset "
            "may be marked for use."
        ),
        checkpoint=(
            "Keep the media folder, the C1373-placeholders CapCut project, 05-asset-register.csv and "
            "05-contact-sheet-review.md together. Lab 6 opens the placeholder project as its editing base when "
            "project-only clips exist, imports only ACCEPT files, and carries disclosure and rights notes into "
            "the export gate."
        ),
        troubleshooting=[
            (
                "Text-to-video changes the product or hands between frames.",
                "Simplify the motion, shorten the prompt or use an authorised still with a slow keyframed camera move.",
            ),
            (
                "The generator menu is unavailable or requires a different plan.",
                "Use an approved alternative or the labelled CapCut placeholder; keep the same storyboard and register fields.",
            ),
            (
                "The synthetic voice mispronounces a phrase.",
                "Split the line, add punctuation or phonetic spelling, and regenerate only that segment.",
            ),
        ],
        challenge=(
            "Create a second accepted version of one scene with a different camera treatment but identical subject, "
            "action, evidence and brand anchors. Compare which better fulfils the shot function."
        ),
        reflection=(
            "Which rejected asset looked attractive at first, and which documented quality gate prevented it from entering the edit?"
        ),
    ),
    dict(
        num=6,
        topic=3,
        title="Edit, Caption, Mix and Export the Vertical Video",
        duration=60,
        objective="LO3: assemble a coherent 9:16 video and verify captions, audio, continuity, accessibility, rights and export settings",
        goal="Turn the accepted Lab 5 assets and final script into a review-ready vertical MP4 that remains understandable with sound on or off.",
        workflow=["Build the timeline", "Correct captions", "Balance sound", "Run export gates"],
        desc=(
            "You will create a CapCut Desktop project, assemble the storyboard beats, generate and correct "
            "captions, apply restrained transitions, balance voice and sound, preview the full result and export "
            "a review file. You will retain a quality log instead of relying on memory."
        ),
        build=(
            "A saved CapCut project, 06-harbour-bean-v1.mp4 and "
            "06-edit-quality-log.md containing timeline, caption, continuity, audio, safe-zone, rights, "
            "disclosure and export evidence."
        ),
        services="CapCut Desktop · accepted Lab 5 media · headphones · phone-sized preview",
        prerequisites=[
            "Completed Lab 5 asset pack and register.",
            "Completed Lab 3 final narration and storyboard.",
            "Use only assets marked ACCEPT or PLACEHOLDER; classroom placeholders are not approved for external publication.",
        ],
        steps=[
            (
                "Open CapCut Desktop. If Lab 5 created any project-only PLACEHOLDER clips, open "
                "C1373-placeholders and immediately save a duplicate as C1373-Harbour-Bean-v1; keep the "
                "registered placeholders on its timeline. If no project-only placeholder exists, select New "
                "project and save it as C1373-Harbour-Bean-v1. Import only ACCEPT media files from "
                "C1373-work/03-media, add the voice or scratch narration, and set the canvas or Ratio control "
                "to 9:16. Place accepted clips and retained placeholders in storyboard order. Create "
                "06-edit-quality-log.md with the required gate headings.",
                "Quality-log headings: Timeline | Captions | Visual continuity | Audio | Safe zones | Rights/disclosure | Export | Full-preview defects and fixes.",
            ),
            (
                "Build the narrative spine. Align the primary hook to 0–3 seconds, trim each body visual to its "
                "spoken beat and keep the final runtime between 25 and 35 seconds. Use Split at beat boundaries. "
                "Apply only a clean cut, short dissolve or one justified motion transition. Record actual start/end "
                "times for hook, three fixes, proof/recap and close in the Timeline gate.",
                "Timeline check: hook 0–3s | three body beats | proof/recap | close | total 25–35s | no empty gap | no unregistered asset.",
            ),
            (
                "Generate captions. In current CapCut Desktop choose Captions, Auto Captions, select the correct "
                "language and Generate. If your version uses Text, Auto captions, use that equivalent path. Play "
                "the full video and correct every word, number and brand term. Break long captions at phrase "
                "boundaries, keep essential text inside the central safe area and apply the cream/navy brand style "
                "with readable contrast.",
                "Caption verification words: Harbour Bean | bitter | grind | ratio | contact time.\nAccessibility check: understandable muted | no text collision | natural line breaks | accurate timing | readable contrast.",
            ),
            (
                "Balance audio. Keep voice or primary sound clearly dominant. Add only an original or documented "
                "cleared practice track, or leave music out. Reduce music beneath speech, add short fades and remove "
                "any distracting effect. Listen once on headphones and once on ordinary speakers; record defects "
                "and fixes in the Audio gate.",
                "Audio log: source/right basis | voice intelligibility | music level | fades | pronunciation | headphone check | speaker check.",
            ),
            (
                "Run three full previews: sound on, muted and phone-sized. Correct all visible defects. In CapCut "
                "select Export, choose MP4, 1080 × 1920, 30 fps and an appropriate high-quality bitrate, then export "
                "as 06-harbour-bean-v1.mp4 to C1373-work/05-export. Reopen the exported file and watch it end to end. "
                "Record filename, dimensions, duration, file opens, full-preview result and any placeholder restriction.",
                "Export gate: MP4 | 1080×1920 | 30 fps | 25–35s | captions burned in and correct | audio clear | rights/disclosure carried forward | file reopens.",
            ),
        ],
        test=(
            "06-harbour-bean-v1.mp4 must open, use a 9:16 frame, run for 25–35 seconds, contain the hook, "
            "three fixes, recap and close, and remain understandable when muted. 06-edit-quality-log.md must "
            "record every gate, the five caption terms, both audio checks, three full previews, final export "
            "settings and any external-use restriction. The edit may contain no REJECT asset."
        ),
        checkpoint=(
            "Keep the project file, exported MP4, quality log and Lab 5 asset register. Lab 7 uses this exact "
            "export and carries forward its rights, disclosure and placeholder status."
        ),
        troubleshooting=[
            (
                "Auto captions are inaccurate or do not generate.",
                "Confirm the language and clean voice track, mute music and regenerate once. If it still fails, choose Text > Add text, paste the first narration phrase, position and style it, drag the layer edges to match that phrase, duplicate the text layer for each remaining phrase, replace the wording and retime every layer before the full preview.",
            ),
            (
                "Important text is hidden or cropped.",
                "Move it into the central safe area, shorten the line and preview at phone size.",
            ),
            (
                "The video exceeds 35 seconds.",
                "Cut pauses and duplicate meaning; do not accelerate speech until it becomes unnatural.",
            ),
        ],
        challenge=(
            "Export the alternate-hook version with every later beat identical. Name it 06-harbour-bean-hook-b.mp4 "
            "and record the one changed element."
        ),
        reflection=(
            "Which preview mode revealed a defect that was easy to miss in the editor?"
        ),
    ),
]
