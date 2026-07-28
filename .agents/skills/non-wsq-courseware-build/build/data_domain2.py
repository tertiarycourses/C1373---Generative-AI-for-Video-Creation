"""Topic 2 labs for C1373."""

DOMAIN2 = [
    dict(
        num=3,
        topic=2,
        title="Write the Timed Script, Caption and Storyboard Pack",
        duration=60,
        objective="LO2: generate and verify a hook-body-close script, post copy and production-ready beat sheet",
        goal="Convert the selected concept into a truthful 25–35 second script whose narration, visuals, text and sound perform distinct jobs.",
        workflow=["Draft the arc", "Build timed beats", "Write post copy", "Read, time and verify"],
        desc=(
            "You will use the Lab 2 concept card to draft a hook-body-close script, then transform it "
            "into a time-coded storyboard. You will add a plain-language description and relevant tags, "
            "read the script aloud, verify every claim and create the production hand-off for Lab 5."
        ),
        build=(
            "A 03-video-script-storyboard.md containing the final narration, timed beat table, caption "
            "plan, post description, relevant hashtags, claim ledger, timing record and AI-draft-to-final "
            "edit comparison."
        ),
        services="Text editor · timer · AI assistant · script-storyboard-template.md",
        prerequisites=[
            "Completed 02-selected-concept.md and 01-audience-prompt-brief.md.",
            "Open labs/assets/script-storyboard-template.md.",
            "Keep the selected hook, body promise and proof source unchanged unless a verification defect is found.",
        ],
        steps=[
            (
                "Save script-storyboard-template.md as 03-video-script-storyboard.md. Paste the selected "
                "audience job, angle, primary hook, body promise, approved proof and next action into the "
                "Source brief section. Ask the AI assistant for three 25–35 second scripts using Hook, Body "
                "and Close. Require one fix per body beat and a claim-to-source table.",
                "Write 3 short-form scripts for <AUDIENCE JOB>.\nHook: preserve this promise: <PRIMARY HOOK>.\nBody: teach exactly 3 verified fixes from <APPROVED SOURCE>.\nClose: recap the 3 fixes and invite the viewer to save the checklist.\nDuration: 25–35 seconds at a natural speaking pace.\nOutput: Hook | Body beat 1 | Body beat 2 | Body beat 3 | Close | Claim-to-source table.\nDo not add benefits, statistics, urgency or product claims beyond the source.",
            ),
            (
                "Select one AI draft and retain it under Selected AI draft. Edit it into the Harbour Bean "
                "voice: practical, warm and precise. Read the final narration aloud with a timer twice. "
                "Record Attempt 1 and Attempt 2 duration; revise until the second attempt is between 25 and "
                "35 seconds without rushing. Add a comparison table with AI draft, Final edit and Reason/source.",
                "Timing record: Attempt 1 <SECONDS> | change made <EDIT> | Attempt 2 <SECONDS>\nVoice check: practical | warm | precise | no hype | no guaranteed result.",
            ),
            (
                "Complete the storyboard table with one row per beat and the columns Time, Spoken line, "
                "Shot function, Visual, On-screen text, Sound and Source/rights. Use 0–3 seconds for the "
                "hook, three body beats, one proof/recap beat and one close. Give each visual exactly one "
                "shot function: orient, demonstrate, prove, transition or close.",
                "Minimum rows: 0–3s hook | beat 1 | beat 2 | beat 3 | proof/recap | close\nVisual prompt format: subject + action + setting + camera + lighting + composition + exclusions.",
            ),
            (
                "Add Caption and post copy. Draft a two-sentence description that names the viewer problem "
                "and the three verified variables without introducing new claims. Add three to five relevant "
                "hashtags, including subject and audience context; reject unrelated high-volume tags. Under "
                "Caption plan, identify the five words that receive emphasis and the intended line breaks.",
                "Description pattern: <PROBLEM>. Check <FIX 1>, <FIX 2> and <FIX 3> before the next brew. <NEXT ACTION>.\nHashtag rule: subject relevance first; no unrelated trend or generic virality tag.",
            ),
            (
                "Finish the Claim and production gate. For every factual phrase list Claim, Source location, "
                "Status and Action. Remove or rewrite every NEEDS EVIDENCE item. Check that the hook is "
                "fulfilled, every beat is producible, on-screen text is concise, sound has a defined role, "
                "rights are resolvable and significant synthetic media will be disclosed where required.",
                "Gate: hook fulfilled | duration 25–35s | 3 verified fixes | 6+ timed rows | one job per visual | post copy adds no claims | rights path visible | disclosure considered.",
            ),
        ],
        test=(
            "03-video-script-storyboard.md must contain the source brief, retained AI draft, final narration, "
            "two recorded timings with the second between 25 and 35 seconds, an edit comparison, at least six "
            "timed storyboard rows, five caption-emphasis words, a two-sentence description, three to five "
            "relevant hashtags and no unresolved claim in the production gate."
        ),
        checkpoint=(
            "Keep 03-video-script-storyboard.md in 02-script. Lab 4 uses its voice and visual anchors; "
            "Labs 5 and 6 use the final narration, beat table and source/rights column as the production plan."
        ),
        troubleshooting=[
            (
                "The script exceeds 35 seconds.",
                "Remove repeated setup, keep one sentence per fix and move optional detail into the post description.",
            ),
            (
                "The visuals merely repeat the spoken words.",
                "Assign a shot function and show the action or proof while narration explains the meaning.",
            ),
            (
                "The post copy adds a new benefit.",
                "Delete it or add a verified source before it enters the claim ledger.",
            ),
        ],
        challenge=(
            "Write the alternate-hook version while keeping every body and close word identical. Record the "
            "exact hook variable so the two versions form a controlled future test."
        ),
        reflection=(
            "Which edit made the script easier to watch rather than merely easier to read?"
        ),
    ),
    dict(
        num=4,
        topic=2,
        title="Build the Brand Prompt Kit and Four-Week Content System",
        duration=60,
        objective="LO2: plan a consistent short-form series and calendar grounded in audience needs, brand rules and approved evidence",
        goal="Turn one successful production brief into a repeatable twelve-video system without repeating the same message.",
        workflow=["Define brand anchors", "Choose pillars", "Plan 12 episodes", "Run consistency gates"],
        desc=(
            "You will convert the Harbour Bean source and Lab 3 creative choices into a reusable brand prompt "
            "kit, three content pillars, a recurring series format and a four-week calendar. Each calendar row "
            "will name its viewer job, evidence, production owner and learning hypothesis."
        ),
        build=(
            "A 04-brand-prompt-kit.md and completed 04-content-calendar.csv with three pillars, one recurring "
            "series, twelve distinct episodes, owners, evidence sources, rights state and testable learning questions."
        ),
        services="Text editor · spreadsheet · AI assistant · content-calendar.csv",
        prerequisites=[
            "Completed Labs 1–3.",
            "Open labs/assets/content-calendar.csv.",
            "Use the same Harbour Bean brand facts, voice and red lines.",
        ],
        steps=[
            (
                "Create 04-brand-prompt-kit.md. Add Audience promise, Point of view, Voice, Vocabulary, Avoid, "
                "Palette, Typography, Composition, Caption treatment, Pace, Sound, AI disclosure and Review gates. "
                "Fill each field from the source pack and Lab 3 final decisions. Use explicit positive guidance "
                "and avoid rules rather than adjectives alone.",
                "Voice: practical, warm, precise.\nUse: plain verbs, observable actions, measured claims.\nAvoid: luxury hype, guarantees, imitation, shame, invented scarcity.\nVisual anchors: daylight pantry | navy #17324D | copper #B46A3C | cream #FFF5E6 | clean close-ups.",
            ),
            (
                "Add a Reusable media prompt with Subject, Action, Setting, Camera, Lighting, Composition, "
                "Brand anchors and Exclusions. Add a Reusable writing prompt using A-P-P-S-O-R. Finish with a "
                "continuity checklist covering subject, product, palette, camera direction, lighting, caption "
                "style, voice and disclosure.",
                "Media prompt: <SUBJECT> <ACTION> in a <SETTING>; <CAMERA> with <LIGHTING>; vertical 9:16 <COMPOSITION>; navy, copper and cream brand anchors; no text, logos, deformed objects or changing product details.\nWriting prompt: Audience <...> | Purpose <...> | Proof <...> | Style <...> | Output <...> | Review <...>.",
            ),
            (
                "Save content-calendar.csv as 04-content-calendar.csv. Keep three pillars: Office-brew fixes, "
                "Ingredient explainers and Equipment routines. Create a recurring series called '30-second "
                "pantry coffee clinic'. Ask AI for four distinct episodes per pillar, then transfer exactly "
                "twelve rows across four weeks. Every row must state audience job, angle, hook channel, source, "
                "format, next action and production owner.",
                "Create 12 episodes for the supplied brand: 4 Office-brew fixes, 4 Ingredient explainers, 4 Equipment routines. Preserve the brand kit. Output: Week, Pillar, Episode, Audience job, Angle, Hook channel, Source, Format, Next action, Owner. Do not repeat Lab 3's exact promise.",
            ),
            (
                "Complete the remaining calendar fields: Asset need, Rights/disclosure state, Workflow state, "
                "Learning hypothesis and Success signal. Use only the states Brief, Script, Assets, Edit, Review, "
                "Scheduled and Learn. Mark any row with an unresolved source or rights issue BLOCKED in Notes.",
                "Hypothesis pattern: If <ONE CREATIVE CHANGE> for <AUDIENCE>, then <RELEVANT SIGNAL> will change because <REASON>.\nRights states: Cleared | Original | Permission required | BLOCKED.",
            ),
            (
                "Run three checks. First, each pillar has four rows and each week has three rows. Second, no two "
                "consecutive rows share the same angle and hook channel. Third, each episode has a distinct viewer "
                "job or proof mechanism. At the end of 04-brand-prompt-kit.md add a 30-day production rhythm with "
                "six named cadence points: brief day, script day, asset day, edit day, approval day and learning review.",
                "Calendar count: 3 pillars × 4 episodes = 12; 4 weeks × 3 episodes = 12.\nConsistency does not mean repetition: keep promise, voice and visual anchors; vary useful question, angle and evidence mechanism.",
            ),
        ],
        test=(
            "04-brand-prompt-kit.md must contain all thirteen brand fields, two reusable prompts, eight "
            "continuity checks and a 30-day production rhythm naming all six cadence points. "
            "04-content-calendar.csv must contain exactly twelve complete episode rows, four "
            "per pillar and three per week, valid workflow and rights states, a named owner and one learning "
            "hypothesis plus success signal per row. No BLOCKED row may be scheduled."
        ),
        checkpoint=(
            "Keep the Lab 4 files. Lab 5 uses the media prompt and continuity checklist; Lab 8 uses the workflow "
            "states, learning hypotheses and 30-day rhythm to build the scaled production plan."
        ),
        troubleshooting=[
            (
                "The calendar repeats Lab 3 twelve times.",
                "Vary the viewer question, angle family and evidence mechanism while preserving the three pillars.",
            ),
            (
                "The brand kit is only adjectives.",
                "Add concrete vocabulary, colours, framing, caption and avoid examples that another creator can apply.",
            ),
            (
                "A scheduled row has unclear media rights.",
                "Change the state to BLOCKED and specify the required permission or replacement.",
            ),
        ],
        challenge=(
            "Create a fourth optional pillar and explain why it extends rather than dilutes the existing audience promise."
        ),
        reflection=(
            "Which elements must stay constant for recognition, and which should change to keep the series useful?"
        ),
    ),
]
