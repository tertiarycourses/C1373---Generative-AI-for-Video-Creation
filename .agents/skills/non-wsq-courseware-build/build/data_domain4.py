"""Topic 4 labs for C1373."""

DOMAIN4 = [
    dict(
        num=7,
        topic=4,
        title="Prepare the Publish, Disclosure and Repurposing Pack",
        duration=60,
        objective="LO4: package a reviewed video for TikTok and adapt its invariant message to other short-form destinations",
        goal="Create a reconstructable publish decision and platform-specific adaptation plan without sending an unapproved post live.",
        workflow=["Validate the export", "Package metadata", "Check settings and disclosure", "Design adaptations"],
        desc=(
            "You will validate the Lab 6 export, create TikTok cover and post copy, resolve rights and AI "
            "disclosure, walk through the current upload controls with a private or stop-before-post practice "
            "setting, and design platform-specific adaptations from the clean master."
        ),
        build=(
            "A 07-publish-and-repurpose-pack.md containing the final publish checklist, metadata, cover plan, "
            "rights and disclosure record, settings evidence, approval decision and a TikTok/Reels/Shorts "
            "adaptation matrix."
        ),
        services="TikTok app or TikTok Studio practice view · text editor · Lab 6 MP4 and quality log",
        prerequisites=[
            "Completed 06-harbour-bean-v1.mp4, 06-edit-quality-log.md and 05-asset-register.csv.",
            "Use a trainer-approved practice account with audience set to Only you, stop before the final Post control, or use labs/assets/tiktok-publish-controls-offline.md for a witnessed offline simulation.",
            "Do not publish externally when any placeholder, rights, permission, claim or disclosure issue remains.",
        ],
        steps=[
            (
                "Create 07-publish-and-repurpose-pack.md from labs/assets/publish-pack-template.md. In Export "
                "identity record the exact filename, duration, dimensions, version, edit log and asset register. "
                "Rewatch the MP4 and confirm hook fulfilment, caption accuracy, audio, safe zones and final frame. "
                "Copy unresolved restrictions verbatim; do not convert a classroom placeholder into an approved asset.",
                "Export identity: filename | version | dimensions | duration | source project | edit-log path | asset-register path | external-use status.",
            ),
            (
                "Write the TikTok package: one cover line of no more than seven words, a two-sentence description, "
                "three to five relevant hashtags and an accessibility/context note. Add no claim that is absent from "
                "the final video and source ledger. Under Rights and disclosure, record music source, generated "
                "visuals, synthetic or human voice, likeness permission, commercial content context and required "
                "AI-generated-content label.",
                "Cover example: Fix bitter office coffee.\nDescription pattern: <VIEWER PROBLEM>. Check <FIX 1>, <FIX 2> and <FIX 3> before the next brew. Save this checklist.\nRights/disclosure decision: Required | Not required with reason | BLOCKED pending <ITEM>.",
            ),
            (
                "Open TikTok and tap Add post +, upload 06-harbour-bean-v1.mp4, then tap Continue or Next. Set the "
                "cover and paste the reviewed description. Open More options; if the video is completely generated "
                "or significantly AI-edited, turn on the AI-generated content setting. Complete the content "
                "disclosure control for brand or product promotion as required by the current account. Set Who can "
                "watch this video to Only you for practice, or stop before Post. Save a screenshot file beside the "
                "publish pack. If login or upload is unavailable, open tiktok-publish-controls-offline.md, read each "
                "control row aloud with the trainer, fill the same settings in the pack, mark the evidence OFFLINE "
                "SIMULATION and record trainer name plus date/time. Publish externally only with explicit account-owner approval.",
                "Practice controls to record: cover | description | hashtags | audience | comments | reuse/duet/stitch where available | commercial-content disclosure | AI-generated content | copyright check where available | final approval owner.\nEvidence: screenshot file that exists, or trainer-witnessed offline log with name and date/time.",
            ),
            (
                "Complete the publish gate with one status per item: PASS, BLOCKED or NOT APPLICABLE with reason. "
                "Cover message, description, hashtags, accessibility, rights, music, likeness, voice, commercial context, "
                "AI disclosure, audience, interaction settings, copyright check, owner and timing must all appear. "
                "State the final decision as APPROVED FOR PRIVATE PRACTICE, BLOCKED or APPROVED BY <OWNER> FOR EXTERNAL USE.",
                "No blank status is allowed. A single BLOCKED item makes the final decision BLOCKED.",
            ),
            (
                "Build the adaptation matrix for TikTok, Instagram Reels and YouTube Shorts. Use rows for Audience "
                "context, Target duration, Aspect ratio, Safe-zone review, Opening change, Caption treatment, "
                "Description/metadata, Next action, Audio-rights check, AI disclosure, Export filename and Owner. "
                "Identify the invariant promise and proof above the matrix. Create adaptations from the clean project "
                "master, never from a downloaded watermarked post.",
                "Invariant: audience problem | three verified fixes | Harbour Bean voice | claim ledger.\nAdapt per destination: opening context | pace/duration | safe zones | metadata | next action | rights/disclosure.",
            ),
        ],
        test=(
            "07-publish-and-repurpose-pack.md must identify the exact Lab 6 export, contain the cover, description, "
            "three to five relevant hashtags, complete rights/disclosure record, every publish-gate item with a "
            "status, visible practice-control evidence supported by an existing screenshot file or a trainer-witnessed "
            "offline log, a named final decision and all twelve adaptation-matrix rows "
            "for three destinations. No BLOCKED item may be described as approved."
        ),
        checkpoint=(
            "Keep the publish pack with the MP4, edit log and asset register. Lab 8 uses its final decision, "
            "adaptation matrix and owner fields to connect audience learning with the scaled production workflow."
        ),
        troubleshooting=[
            (
                "The TikTok menu labels differ from the lab.",
                "Use the equivalent current Add post, More options, audience and disclosure controls and record the labels shown.",
            ),
            (
                "The AI-generated-content decision is unclear.",
                "Treat realistic generated or significantly altered image, video or audio as requiring review and consult current TikTok guidance before external use.",
            ),
            (
                "A music source is not cleared for brand promotion.",
                "Replace it with original or commercially cleared audio, re-export and update the asset register.",
            ),
        ],
        challenge=(
            "Create one platform-specific alternate opening for Reels and one for Shorts while preserving the same "
            "verified body proof. Explain why each change fits its viewing context."
        ),
        reflection=(
            "Which publish control carries information that cannot be repaired after viewers have already seen the post?"
        ),
    ),
    dict(
        num=8,
        topic=4,
        title="Analyse Performance and Build the Scaled Improvement Plan",
        duration=60,
        objective="LO4: interpret post metrics cautiously, choose a one-variable iteration and govern a repeatable production workflow",
        goal="Turn a bounded synthetic dataset into observations, alternative explanations, one controlled next test and a 30-day production board.",
        workflow=["Calculate comparable metrics", "Separate observation from cause", "Design one test", "Govern the pipeline"],
        desc=(
            "You will analyse supplied synthetic TikTok post data, use AI to organise—but not invent—findings, "
            "select one variable for the next version and convert the Lab 4 calendar into a governed production "
            "board with owners, gates, measures and stop rules."
        ),
        build=(
            "A completed 08-performance-calculations.csv, an 08-performance-iteration-plan.md and "
            "08-production-board.csv with traceable observations, alternative explanations, a controlled "
            "test, workflow states, owners, entry/exit gates and a 30-day learning cadence."
        ),
        services="Spreadsheet · text editor · AI assistant · synthetic-tiktok-analytics.csv · Lab 4 calendar",
        prerequisites=[
            "Completed 04-content-calendar.csv and 07-publish-and-repurpose-pack.md.",
            "Open labs/assets/synthetic-tiktok-analytics.csv and labs/assets/production-board.csv.",
            "Treat every supplied metric as synthetic classroom data; do not infer real audience behaviour.",
        ],
        steps=[
            (
                "Create 08-performance-iteration-plan.md and add Publication and adaptation hand-off. Copy from "
                "Lab 7 the exact final decision, primary destination, one destination-specific adaptation change "
                "and approval owner. If Lab 7 is BLOCKED, name the unresolved item and carry it into the Blocker "
                "field of every affected production-board row; do not treat private practice as external approval.",
                "Required hand-off fields: Lab 7 final decision | Primary destination | Adaptation change | Approval owner | Unresolved blocker or NONE.",
            ),
            (
                "Save synthetic-tiktok-analytics.csv as 08-performance-calculations.csv. Add the columns "
                "Two-second hold, Six-second hold, Completion rate, Engagement rate and Action rate. In row 2 "
                "calculate each as the relevant count divided by Views: 2-second views, 6-second views, "
                "Completed views, Likes+Comments+Shares+Saves, and Profile visits+Link clicks. Format as percentages "
                "and fill the formulas down. Check that every result is between 0% and 100%.",
                "If Views is column C: Two-second hold =D2/C2; Six-second hold =E2/C2; Completion rate =F2/C2; Engagement rate =SUM(H2:K2)/C2; Action rate =SUM(L2:M2)/C2.\nAdjust letters only after matching the actual headers.",
            ),
            (
                "Continue in the existing 08-performance-iteration-plan.md. Add Context, Comparable baseline, Observations, "
                "Alternative explanations, Missing evidence, Decision and Review window. Compare videos with the "
                "same audience and similar duration before comparing the calculated rates. Write at least four "
                "numeric observations that name the video and metric; do not use causal words in this section.",
                "Observation pattern: Video <ID> has <METRIC> of <VALUE>, compared with <BASELINE VALUE> for <COMPARABLE SET>.\nBanned in observations: caused | proves | because | algorithm prefers.",
            ),
            (
                "Paste only the table and your four observations into the AI assistant. Ask it to check calculations, "
                "suggest at least two alternative explanations per material pattern and list missing evidence. Require "
                "it to distinguish OBSERVATION, HYPOTHESIS and QUESTION. Verify every number against the spreadsheet "
                "and delete any unsupported platform explanation.",
                "Review the synthetic table below. (1) Check arithmetic, (2) separate observations from hypotheses, (3) give at least two plausible alternatives per pattern, (4) list missing evidence, and (5) do not claim causation or a universal platform rule. Use only the supplied table.\n<PASTE TABLE AND OBSERVATIONS>",
            ),
            (
                "Choose one next-version variable: primary hook, beat-two duration, first visual, caption density or "
                "close. State why it is linked to a specific observation, then define Keep constant, Baseline, Success "
                "signal, Guardrail, Minimum review window and Stop/continue rule. Use the Lab 2 alternate hook when "
                "hook is selected; otherwise preserve both hooks and document the single changed element.",
                "Test statement: Change <ONE VARIABLE> from <A> to <B> for <AUDIENCE>. Keep <AT LEAST FOUR ITEMS> constant. Compare <RELEVANT RATE> against <BASELINE> after <WINDOW>. Stop or revise if <GUARDRAIL>.",
            ),
            (
                "Save production-board.csv as 08-production-board.csv and transfer the next six eligible rows from "
                "the Lab 4 calendar. An eligible row has a named owner, a source, a rights/disclosure state other than "
                "BLOCKED, and a current workflow state of Brief or later. Use only Brief, Script, Assets, Edit, Review, "
                "Scheduled and Learn states. Complete "
                "Owner, Evidence source, Required artifact, Entry gate, Exit gate, Rights/disclosure, Planned date, "
                "Learning hypothesis, Success signal and Blocker. A row with missing evidence, rights or owner must "
                "stay in its last valid workflow state, have a nonblank Blocker field and may not enter Scheduled.",
                "State gates: Brief requires audience+purpose+proof | Script requires verified claims+timing | Assets requires register+rights | Edit requires accepted media | Review requires quality log | Scheduled requires publish gate+owner | Learn requires comparable metrics+decision.",
            ),
            (
                "In 08-performance-iteration-plan.md add 30-day cadence and process controls. Name weekly brief, production, approval and learning "
                "review points. Track median cycle time, items blocked by rights, first-review defects, rework count and "
                "posts with a documented learning decision. Add stop rules for unverified claims, missing permission, "
                "misleading synthetic media and repeated quality failure.",
                "Volume is not the primary control. Scale only when every item can be traced from source brief to asset register, approval and learning decision.",
            ),
        ],
        test=(
            "08-performance-calculations.csv must contain all five rate columns with valid percentages for every "
            "row. 08-performance-iteration-plan.md must contain the five Lab 7 hand-off fields, four checked numeric observations, at least two "
            "alternative explanations for each material pattern, missing evidence, exactly one changed variable, "
            "four or more keep-constant items, a baseline, success signal, guardrail, window and stop/continue rule. "
            "08-production-board.csv must contain six rows, valid states, all ten governance fields and no blocked "
            "item in Scheduled. The iteration plan must also contain all four weekly cadence points, all five named "
            "process measures and all four stop rules."
        ),
        checkpoint=(
            "The Lab 8 files complete the C1373 portfolio. To rejoin later, start with the selected production-board "
            "row, follow its entry gate and use the iteration plan's keep-constant list before changing the next video."
        ),
        troubleshooting=[
            (
                "A calculated percentage exceeds 100%.",
                "Check the header-to-column mapping, denominator and whether counts were added twice.",
            ),
            (
                "AI invents a reason for the performance change.",
                "Relabel it HYPOTHESIS, require an alternative explanation and state the missing evidence.",
            ),
            (
                "The production board has too many items in progress.",
                "Limit active work, clear blockers and finish review gates before starting more briefs.",
            ),
        ],
        challenge=(
            "Perform a sensitivity check with a second comparable baseline and explain whether the same one-variable "
            "test remains the best next step."
        ),
        reflection=(
            "Which metric or workflow measure would be most dangerous to optimise in isolation, and why?"
        ),
    ),
]
