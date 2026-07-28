"""Topic 1 labs for C1373."""

DOMAIN1 = [
    dict(
        num=1,
        topic=1,
        title="Build the Audience, Tool and AI Prompt Brief",
        duration=60,
        objective="LO1: explain the audience, recommendation-signal and responsible-use choices that govern a generative AI video workflow",
        goal="Create the evidence boundary and reusable A-P-P-S-O-R prompt that will govern all later Harbour Bean video work.",
        workflow=["Inspect sources", "Define audience", "Check tool roles", "Prompt and verify"],
        desc=(
            "You will read the synthetic Harbour Bean brand and audience sources, define one precise "
            "viewer job, map the production stack and use the A-P-P-S-O-R pattern to generate a grounded "
            "video brief. You will review an initial and refined AI response instead of treating fluent "
            "creative output as verified truth."
        ),
        build=(
            "A 01-audience-prompt-brief.md containing approved brand facts, an audience-job statement, "
            "recommendation-signal hypotheses, a tool-role map, one reusable A-P-P-S-O-R prompt, two "
            "AI-response versions and a claim-to-source ledger."
        ),
        services="Text editor · ChatGPT, Claude or Copilot · supplied synthetic source pack",
        prerequisites=[
            "Open labs/assets/harbour-bean-brand-brief.md and labs/assets/audience-signals.md.",
            "Confirm that one organisation-approved AI assistant is available.",
            "Create a C1373-work folder with 01-source, 02-script, 03-media, 04-edit and 05-export subfolders.",
        ],
        steps=[
            (
                "Create 01-audience-prompt-brief.md in C1373-work/01-source. Add the headings Brand, "
                "Audience, Moment, Problem, Desired outcome, Approved proof, Voice, Visual anchors, "
                "Red lines and Unknowns. Fill them only from harbour-bean-brand-brief.md and "
                "audience-signals.md; enter UNKNOWN when neither source supports a field.",
                "Required source rule: every material statement must name harbour-bean-brand-brief.md, audience-signals.md or UNKNOWN.",
            ),
            (
                "Add Audience job and Recommendation hypotheses. Write one sentence in the form "
                "'When <MOMENT>, <AUDIENCE> wants to <JOB> so they can <OUTCOME>.' Then write three "
                "labelled hypotheses connecting the proposed video to a viewer interaction, content "
                "information signal or search match. Mark each as HYPOTHESIS, not a platform fact.",
                "Audience job: When <MOMENT>, <AUDIENCE> wants to <JOB> so they can <OUTCOME>.\nHypothesis H1 — interaction: <TESTABLE EXPECTATION>\nHypothesis H2 — content information: <TESTABLE EXPECTATION>\nHypothesis H3 — search match: <TESTABLE EXPECTATION>",
            ),
            (
                "Add a Tool-role map with the columns Job, Primary tool, Input, Output, Human check and "
                "Fallback. Complete rows for research/ideation, scripting, media generation, editing, "
                "captions, audio and export. Use an approved AI assistant and CapCut Desktop where "
                "available; name an offline storyboard or manual edit fallback for every cloud feature.",
                "Rows: research/ideation | scripting | media generation | editing | captions | audio | export\nHuman checks: evidence | privacy | rights | continuity | accessibility | disclosure",
            ),
            (
                "Under Reusable prompt, write and run one A-P-P-S-O-R prompt using only the approved "
                "source text. Ask for five 25–35 second video concepts, each with angle, hook, body proof, "
                "scene plan, next action and risk flag. Paste the response under Initial response and add "
                "a ledger with Version, Claim, Source, Status and Fix. Mark unsupported statements NEEDS EVIDENCE.",
                "Audience: <PASTE AUDIENCE JOB>.\nPurpose: Teach one useful way to improve bitter office coffee.\nProof: Use only the delimited Harbour Bean source text below; write UNKNOWN for missing facts.\nStyle: Practical, warm and precise; daylight pantry; navy, copper and cream; no hype or imitation.\nOutput: Five distinct 25–35 second concepts. For each show angle, verbal/visual hook, three body beats, source-backed proof, next action and production risk.\nReview: Add a claim ledger and flag privacy, likeness, music, rights or AI-disclosure issues.\n--- APPROVED SOURCE ---\n<PASTE RELEVANT SOURCE TEXT>\n--- END SOURCE ---",
            ),
            (
                "Refine the prompt once by adding the most important missing constraint you found. Run it "
                "again, paste it under Refined response and update the ledger with Initial or Refined in "
                "the Version column. Finish with a six-line readiness check: audience is specific, source "
                "boundary is visible, tool roles are assigned, fallback exists, claims are traceable and "
                "human approval is named.",
                "Iteration note: The initial response failed because <DEFECT>. I added <CONSTRAINT>. The refined response now <OBSERVABLE IMPROVEMENT>.",
            ),
        ],
        test=(
            "Open 01-audience-prompt-brief.md. It must contain all ten source headings, one complete "
            "audience-job sentence, three labelled recommendation hypotheses, seven tool-role rows, a "
            "six-part A-P-P-S-O-R prompt, two labelled AI responses, no unsupported claim marked OK and "
            "all six readiness lines."
        ),
        checkpoint=(
            "Keep 01-audience-prompt-brief.md in 01-source. If you rejoin later, use its audience job, "
            "approved proof, voice, visual anchors and red lines as the only strategic input to Labs 2–8."
        ),
        troubleshooting=[
            (
                "The AI returns generic 'viral video' ideas.",
                "Paste the audience job, source facts and output columns, then prohibit generic virality claims.",
            ),
            (
                "The response invents product benefits or customer results.",
                "Remove the claim and add 'Use only the approved source; otherwise write UNKNOWN and a question.'",
            ),
            (
                "A named tool or feature is unavailable.",
                "Keep the same job and hand-off; use the listed fallback and record the substituted tool.",
            ),
        ],
        challenge=(
            "Run the refined prompt in a second approved assistant. Compare source discipline, useful "
            "variation and production feasibility with the same rubric; do not treat agreement as proof."
        ),
        reflection=(
            "Which human check prevents the most serious failure in this workflow, and what artifact proves that check occurred?"
        ),
    ),
    dict(
        num=2,
        topic=1,
        title="Create and Score an AI Video Idea and Hook Bank",
        duration=55,
        objective="LO1: connect audience needs and recommendation signals to truthful, testable short-form video concepts",
        goal="Generate meaningfully different concepts and select one primary hook plus one controlled alternate using explicit criteria.",
        workflow=["Generate angle families", "Write multimodal hooks", "Score consistently", "Lock the concept"],
        desc=(
            "You will turn the Lab 1 brief into an idea bank across mistake, demonstration, comparison, "
            "myth, checklist and story angles. You will write verbal, visual and text-overlay hooks, reject "
            "misleading options and score the survivors before locking the Harbour Bean production concept."
        ),
        build=(
            "A completed 02-idea-hook-bank.csv with twelve concepts and a 02-selected-concept.md with "
            "the chosen angle, primary hook, alternate hook, body promise, proof source, next action, "
            "production risks and a one-variable future test."
        ),
        services="Spreadsheet · text editor · AI assistant · idea-hook-bank-template.csv",
        prerequisites=[
            "Completed 01-audience-prompt-brief.md from Lab 1.",
            "Open labs/assets/idea-hook-bank-template.csv.",
            "Use the same synthetic audience, proof, voice and red lines from the approved brief.",
        ],
        steps=[
            (
                "Save a copy of idea-hook-bank-template.csv as 02-idea-hook-bank.csv. Ask the AI assistant "
                "for two concepts in each angle family: mistake, demonstration, comparison, myth, checklist "
                "and story. Require every row to include audience tension, useful promise, supporting source "
                "and a feasible 25–35 second production path. Transfer exactly twelve rows to the sheet.",
                "Using the approved Harbour Bean brief below, create exactly 12 short-video concepts: 2 mistake, 2 demonstration, 2 comparison, 2 myth, 2 checklist and 2 story. Use only supplied proof. Output CSV-ready columns: ID, angle family, audience tension, promise, proof source, scene mechanism, next action, risk.\n<PASTE LAB 1 APPROVED BRIEF>",
            ),
            (
                "For each concept write three hook channels in the sheet: Spoken hook, First visual and "
                "On-screen text. The three should reinforce the same promise without repeating identical "
                "words. If an option uses false urgency, guaranteed results, withheld context, unrelated "
                "trends or imitation of a recognisable creator, record its ID and rejection reason under "
                "Rejected ideas in 02-selected-concept.md, then replace it with a new eligible concept from "
                "the same angle family. Continue until the sheet contains exactly twelve eligible rows.",
                "Hook check: clear audience problem | specific promised value | body can fulfil it | no invented urgency | no copied identity.\nReplacement rule: log the rejected ID and reason, then replace it in the CSV so exactly 12 eligible rows remain.",
            ),
            (
                "Score every remaining concept from 1 to 5 for Audience fit, Clarity, Source support, "
                "Distinctiveness and Production feasibility. Calculate Total as the sum of the five scores. "
                "Add a Decision note that explains any score below 3; do not change a score merely to make "
                "a favourite idea win.",
                "Spreadsheet formula for row 2 Total: =SUM(I2:M2)\nUse the equivalent columns if your spreadsheet places the five score fields elsewhere.",
            ),
            (
                "Filter Total from highest to lowest. Choose one primary concept only after reading its risk "
                "and source fields. Choose one alternate with the same body promise but a different opening "
                "channel so it can become a one-variable hook test. Create 02-selected-concept.md using the "
                "required headings below.",
                "Headings: Audience job | Angle | Primary spoken hook | Primary first visual | Primary on-screen text | Alternate hook | Body promise | Approved proof | Next action | Production risks | Test variable | Keep constant",
            ),
            (
                "Run a fulfilment check with a partner or the AI assistant as critic. Give only the selected "
                "hook and body promise. Ask what the viewer expects to receive, compare that expectation with "
                "the planned body and edit any mismatch. Record the original wording, final wording and reason "
                "under Hook fulfilment check.",
                "Critique this hook and body promise. State (1) what a reasonable viewer expects, (2) whether the body fulfils it, (3) any misleading implication, and (4) the smallest repair. Do not propose a more sensational hook.",
            ),
        ],
        test=(
            "02-idea-hook-bank.csv must contain exactly twelve eligible rows across all six angle families, three hook "
            "channels per row, five numeric scores, a total and decision note. 02-selected-concept.md "
            "must contain every required heading, one primary and one alternate hook, one stated test "
            "variable, at least three keep-constant items, the before/after fulfilment check and a Rejected "
            "ideas log containing every replaced ID and reason, or the line 'No ideas rejected'."
        ),
        checkpoint=(
            "Keep both Lab 2 files. Lab 3 uses the selected audience, angle, primary hook, alternate hook, "
            "body promise and verified proof to build the timed script and storyboard."
        ),
        troubleshooting=[
            (
                "The twelve ideas differ only in wording.",
                "Regenerate by angle family and require a different evidence mechanism or scene treatment per family.",
            ),
            (
                "Every concept receives the same score.",
                "Write observable anchors for 1, 3 and 5, then rescore one criterion at a time across all rows.",
            ),
            (
                "The highest score is difficult to produce.",
                "Lower its feasibility score honestly or simplify the scene mechanism while preserving the promise.",
            ),
        ],
        challenge=(
            "Design a visual-first alternate that communicates the same truthful promise before any spoken word. "
            "Explain which audience signal it is intended to improve and why that remains only a hypothesis."
        ),
        reflection=(
            "Which selection criterion changed your initial preference, and what does that reveal about creative judgement?"
        ),
    ),
]
