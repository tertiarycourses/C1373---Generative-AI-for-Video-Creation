"""Single source of truth for Generative AI for Video Creation (C1373)."""

TITLE = "Generative AI for Video Creation"
SHORT_TITLE = "Generative AI for Video Creation"
COURSE_CODE = "C1373"
COURSE_URL = "https://www.tertiarycourses.com.sg/generative-ai-for-video-creation.html"
VERSION = "v1.0"
VERSION_DATE = "28 July 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Allen Wong"
DAYS = 2
DAY_MINUTES = 480
INSTRUCTIONAL_MINUTES = 450
MODE = "Instructor-led, hands-on practical labs"
DAILY_TIMING = (
    "9:30 am – 6:30 pm (1-hour lunch; two 15-minute tea breaks; "
    "7.5 instructional hours)"
)
DARK_THEME = False

LEARNING_OUTCOMES = [
    "LO1: Explain how short-form recommendation systems, audience signals and responsible generative AI practices shape video decisions.",
    "LO2: Use structured prompts to generate audience-relevant ideas, hooks, scripts, captions, hashtags and a coherent content plan.",
    "LO3: Create and edit a brand-consistent vertical video with generated visuals, voiceover, captions, sound and a documented rights check.",
    "LO4: Prepare, publish, analyse, repurpose and scale short-form video content through an evidence-led production workflow.",
]

LO_TITLES = [
    "Audience & AI",
    "Ideate & Script",
    "Create & Edit",
    "Publish & Improve",
]


def _section(title, definition, why, how, example, use_when, avoid_when, quality):
    return dict(
        title=title,
        definition=definition,
        why=why,
        how=how,
        example=example,
        use_when=use_when,
        avoid_when=avoid_when,
        quality=quality,
    )


TOPICS = [
    dict(
        num=1,
        code="01",
        title="Getting Started with Generative AI for TikTok",
        subtitle="Short-form video and GenAI · Tool setup · Recommendation signals and audience · Effective prompting",
        weighting="Day 1 morning · 2 labs",
        concepts=[
            ("Short-form story", "A focused promise, fast proof and clear next action designed for vertical, mobile viewing."),
            ("Recommendation signals", "Viewer interactions, content information and user context influence what each person is shown."),
            ("Production stack", "An AI assistant plans; a generator creates candidate media; an editor assembles and checks the video."),
            ("Prompt brief", "Audience, purpose, source facts, creative constraints, output format and review gates make generation useful."),
        ],
        sections=[
            _section(
                "Introduction to Short-Form Video and Generative AI",
                "Short-form video communicates one useful idea through a compact visual and audio sequence. Generative AI can propose concepts, draft scripts, create candidate images or clips, synthesize voice and accelerate edits, but it does not know the brand truth, audience context or usage rights unless a person supplies and checks them.",
                "The production bottleneck is rarely a lack of generated material; it is choosing a relevant promise and turning it into a coherent viewing experience. A human-led workflow separates message decisions from media generation and keeps the creator accountable for truth, permission, safety and final quality.",
                [
                    "Define one audience, one viewing situation and one useful outcome.",
                    "Turn the outcome into a hook, supporting proof and next action.",
                    "Generate candidate words, visuals and audio against the same brief.",
                    "Assemble a rough cut, review it in context and remove anything unsupported.",
                    "Export only after message, accessibility, rights and disclosure checks pass.",
                ],
                [
                    "Harbour Bean Co. wants busy office workers to improve bitter pantry coffee.",
                    "The video promises three practical fixes, demonstrates each fix and closes with a save-this checklist.",
                    "AI supplies draft options; the creator verifies every product and brewing claim against the synthetic source pack.",
                ],
                [
                    "You have a bounded message and approved source material.",
                    "AI can reduce drafting or production time while a person reviews the result.",
                ],
                [
                    "The idea depends on an invented claim, copied creator identity or unlicensed asset.",
                    "The workflow would publish generated output without a full human preview.",
                ],
                [
                    ("FAILURE SIGNAL", "The clip looks polished but the viewer cannot state its one useful promise."),
                    ("REPAIR MOVE", "Rewrite the concept as audience + problem + promised value in one sentence."),
                    ("QUALITY EVIDENCE", "Every scene supports the promise and the creator can trace its factual claims."),
                ],
            ),
            _section(
                "Setting Up AI Tools for Video Creation",
                "A practical tool stack has three roles: a language assistant for research and scripting, a media generator for candidate visuals or voice, and a nonlinear editor for timing, captions, sound and export. One product may cover several roles, but the files, settings and review gates should remain visible and portable.",
                "Tool features, plans and labels change quickly. Designing around durable jobs rather than one button lets creators switch products, use an offline fallback and preserve the project when a feature or account is unavailable.",
                [
                    "Create one project folder with source, script, storyboard, media, edit and export subfolders.",
                    "Confirm access to an approved AI assistant and CapCut Desktop or an equivalent editor.",
                    "Set a 9:16 vertical canvas and a consistent naming convention before generating assets.",
                    "Record each generated asset's prompt, tool, date, source input and intended use.",
                    "Keep an offline storyboard and manual-edit path for unavailable premium or regional features.",
                ],
                [
                    "The C1373 project stores 01-source, 02-script, 03-media, 04-edit and 05-export artifacts.",
                    "A generated coffee-pour clip is saved with its prompt and rights note instead of remaining only in a tool history.",
                    "If text-to-video is unavailable, the storyboard is completed with supplied synthetic stills or authorised stock.",
                ],
                [
                    "Several tools contribute to one production and provenance must remain clear.",
                    "You need a repeatable folder and file hand-off between ideation and editing.",
                ],
                [
                    "A tool requires protected business data that is not approved for that service.",
                    "The production depends on one premium feature with no fallback or export route.",
                ],
                [
                    ("FAILURE SIGNAL", "Files are named final2-new-final and no one knows their source."),
                    ("REPAIR MOVE", "Use scene-purpose-version names and a simple asset register."),
                    ("QUALITY EVIDENCE", "Another learner can reopen the project and identify every required source file."),
                ],
            ),
            _section(
                "Understanding the TikTok Recommendation System and Audience",
                "TikTok describes recommendation as a prediction process influenced mainly by user interactions, content information and user information. For many viewers, interactions such as watch time, completion, skips, likes, shares and comments carry substantial weight, while search also considers how well content matches the query.",
                "There is no universal algorithm trick. Creators improve relevance by serving a clear audience need, earning attention honestly, making the subject legible through words and visuals, and studying how real viewers respond instead of optimising for myths.",
                [
                    "Define a narrow audience job, tension and moment of need.",
                    "Research patterns through TikTok Studio or Creative Center without copying another creator.",
                    "State the content promise in the opening words, visual and on-screen text.",
                    "Use keywords and context that accurately describe the video.",
                    "Review retention and meaningful response signals after publication, then form one testable hypothesis.",
                ],
                [
                    "Audience: office workers using basic pantry equipment.",
                    "Moment: the first sip tastes bitter and they want a quick fix before the next meeting.",
                    "Opening: a close-up of the brew plus 'Bitter office coffee? Fix these 3 things.'",
                    "The topic and wording are relevant even if a trending sound is not used.",
                ],
                [
                    "You can state a specific viewer problem and observable benefit.",
                    "Analytics or direct audience feedback can inform the next iteration.",
                ],
                [
                    "The plan relies on engagement bait, misleading suspense or unrelated trending tags.",
                    "A single post's result is treated as proof of a permanent platform rule.",
                ],
                [
                    ("FAILURE SIGNAL", "The brief says only 'people on TikTok'."),
                    ("REPAIR MOVE", "Add audience, moment, problem, desired outcome and evidence source."),
                    ("QUALITY EVIDENCE", "The hook, content and next action all serve the same viewer job."),
                ],
            ),
            _section(
                "Effective Prompting for Video Ideas and Content",
                "A video prompt is a production brief expressed as instructions. The course uses A-P-P-S-O-R: Audience, Purpose, Proof, Style, Output and Review. This structure grounds creative variation in source facts while making format and quality requirements observable.",
                "Vague prompts generate generic lists and can hide invented claims. A structured prompt produces alternatives that can be compared, shows where evidence is missing and creates reusable hand-offs from idea to script, shot list and edit.",
                [
                    "State the audience and one purpose for the video.",
                    "Paste or attach the approved proof source and prohibit unsupported claims.",
                    "Set style constraints such as tone, pace, aspect ratio and brand cues.",
                    "Specify the requested table, duration, scenes and number of options.",
                    "Require a review ledger for facts, rights, disclosure and uncertainty.",
                ],
                [
                    "Audience: busy Singapore office workers; purpose: teach three fixes for bitter pantry coffee.",
                    "Proof: use only the supplied Harbour Bean source pack.",
                    "Output: five 25–35 second concepts with hook, proof, scenes and save-worthy takeaway.",
                    "Review: flag any claim or asset that needs a source or permission.",
                ],
                [
                    "The source pack and desired output can be clearly bounded.",
                    "You need several alternatives that share the same strategic brief.",
                ],
                [
                    "The prompt asks AI to imitate a living creator or fabricate customer proof.",
                    "The creator plans to select by excitement without checking fit, evidence and feasibility.",
                ],
                [
                    ("FAILURE SIGNAL", "Five options are merely five phrasings of the same generic idea."),
                    ("REPAIR MOVE", "Require distinct angles, mechanisms or viewer tensions and a comparison rubric."),
                    ("QUALITY EVIDENCE", "Each chosen idea links audience need, approved proof and a feasible production path."),
                ],
            ),
        ],
    ),
    dict(
        num=2,
        code="02",
        title="Generating Scripts, Ideas and Hooks with AI",
        subtitle="Ideas, angles and hooks · Scripts, captions and hashtags · Series and content calendars · Brand voice and style",
        weighting="Day 1 afternoon · 2 labs",
        concepts=[
            ("Angle", "The specific lens that makes a familiar subject useful to this audience now."),
            ("Hook-body-close", "The opening earns attention, the body delivers proof and the close completes the promise."),
            ("Beat sheet", "A time-boxed map of spoken line, visual, on-screen text and sound for each moment."),
            ("Content system", "A repeatable relationship among audience problem, pillar, format, evidence and next action."),
        ],
        sections=[
            _section(
                "Generating Video Ideas, Angles and Hooks",
                "A topic is broad; an angle selects the specific tension, perspective or transformation. A hook is the first clear signal of relevance, delivered through spoken words, on-screen text, visual action or sound. Effective hooks promise value without withholding essential context or misleading the viewer.",
                "AI can produce many openings quickly, but volume alone creates sameness. Separating angle generation from hook writing and scoring options against relevance, clarity, proof and production feasibility produces more useful variety.",
                [
                    "Turn the audience problem into several angle families: mistake, demonstration, comparison, myth, checklist or story.",
                    "Generate verbal, visual and text-overlay hooks for each promising angle.",
                    "Remove hooks that overpromise or depend on unsupported urgency.",
                    "Score options on audience fit, clarity, credible proof, novelty and feasibility.",
                    "Select one primary hook and one alternate for a controlled future test.",
                ],
                [
                    "Topic: better office coffee.",
                    "Mistake angle: 'Your water is not the only reason office coffee tastes bitter.'",
                    "Demonstration angle: show two brews side by side before naming the three variables.",
                    "Checklist angle: 'Before your next cup, check grind, ratio and contact time.'",
                ],
                [
                    "A verified subject can support several useful perspectives.",
                    "The production team can demonstrate or source the promised proof.",
                ],
                [
                    "The hook implies a result the body cannot deliver.",
                    "The idea copies a recognisable creator's phrase, face, voice or signature treatment.",
                ],
                [
                    ("FAILURE SIGNAL", "The hook is loud but no audience benefit appears in the first moments."),
                    ("REPAIR MOVE", "Name the viewer problem and promised takeaway explicitly."),
                    ("QUALITY EVIDENCE", "A colleague can predict the body from the hook and finds the promise fulfilled."),
                ],
            ),
            _section(
                "Writing Scripts, Captions and Hashtags with AI",
                "A short-form script coordinates narration, visuals, on-screen text and timing rather than presenting a block of prose. Captions improve comprehension and accessibility; post descriptions and hashtags add truthful context and discovery cues but should not be used to disguise an unrelated subject.",
                "Writing each channel separately causes repetition or conflict. A beat sheet lets the creator see whether spoken lines, visuals and text complement one another, while a claim ledger prevents fluent AI copy from turning assumptions into facts.",
                [
                    "Write the hook, body proof and close as a 25–35 second spoken arc.",
                    "Split the arc into time-coded beats with one visual job per beat.",
                    "Use on-screen text to reinforce key words, not transcribe every design decision.",
                    "Draft a plain-language post description and a small set of relevant hashtags.",
                    "Read aloud, time the script and verify every factual claim before recording.",
                ],
                [
                    "0–3s: bitter-cup reaction and problem statement.",
                    "3–21s: three fixes shown with labelled close-ups.",
                    "21–28s: before/after comparison and concise recap.",
                    "28–32s: 'Save this before your next office brew' and accessible post description.",
                ],
                [
                    "The message must fit a precise duration and coordinate several media channels.",
                    "You can review the script against an approved source pack.",
                ],
                [
                    "The caption includes irrelevant high-volume tags or hidden claims.",
                    "The narration is generated in a person's voice without permission.",
                ],
                [
                    ("FAILURE SIGNAL", "The script reads well but runs far beyond the target duration."),
                    ("REPAIR MOVE", "Time it aloud, cut duplicate meaning and assign one job to each beat."),
                    ("QUALITY EVIDENCE", "Every beat has a purpose, duration, visual and verified claim."),
                ],
            ),
            _section(
                "Planning Series and Content Calendars",
                "A content series explores one audience problem through recurring, recognisable episodes. A content calendar connects each episode to a pillar, angle, source, format, production status and next action so the team can publish consistently without generating random filler.",
                "Scaling output without a plan often repeats ideas and weakens brand trust. A calendar balances useful formats and viewer stages, reveals asset dependencies early and creates a learning agenda for future videos.",
                [
                    "Choose three durable pillars tied to audience questions and brand credibility.",
                    "Create repeatable series formats with a stable promise and flexible episode subject.",
                    "Map episodes to dates, evidence sources, owners, assets and review status.",
                    "Balance discovery, education, demonstration and conversation goals.",
                    "Record the hypothesis each publication will help explore.",
                ],
                [
                    "Pillar 1: office-brew fixes; Pillar 2: ingredient explainers; Pillar 3: quick equipment routines.",
                    "Series: '30-second pantry coffee clinic' with one observable problem per episode.",
                    "The calendar assigns one source, one owner and one measurable learning question to every row.",
                ],
                [
                    "A creator has several verified themes and needs a sustainable cadence.",
                    "Production dependencies and review responsibilities must be visible.",
                ],
                [
                    "The calendar prioritises posting frequency over useful, evidenced content.",
                    "AI-generated repetitions are published merely to fill empty dates.",
                ],
                [
                    ("FAILURE SIGNAL", "Twelve rows repeat one sales message with different dates."),
                    ("REPAIR MOVE", "Vary the viewer job, angle and format while keeping the brand promise stable."),
                    ("QUALITY EVIDENCE", "Each row has a distinct purpose, source, owner and learning hypothesis."),
                ],
            ),
            _section(
                "Keeping a Consistent Brand Voice and Style",
                "Brand consistency is a system of choices: audience promise, point of view, vocabulary, tone, colour, typography, composition, pace, sound and disclosure practice. It does not mean every video is visually identical; it means variation remains recognisably governed.",
                "Generative tools can drift between styles or imitate familiar internet aesthetics. A compact brand and prompt kit gives AI explicit boundaries, while side-by-side review ensures the final edit still sounds and looks like the organisation rather than the tool.",
                [
                    "Define voice traits with positive guidance and concrete avoid rules.",
                    "Specify a small palette, type hierarchy, framing pattern and caption treatment.",
                    "Create reusable prompt anchors for subject, environment, lighting and mood.",
                    "Compare generated assets for continuity, rights risk and unintended artefacts.",
                    "Record justified exceptions when an episode intentionally changes the pattern.",
                ],
                [
                    "Harbour Bean voice: practical, warm, precise; avoid luxury hype and guaranteed outcomes.",
                    "Visual anchor: daylight pantry setting, navy and copper accents, clean close-ups and readable cream captions.",
                    "Every output is edited back to these anchors before it enters the timeline.",
                ],
                [
                    "Several people or tools contribute to one channel.",
                    "A recurring series needs variation without losing recognition.",
                ],
                [
                    "The brief requests imitation of a named living artist or creator.",
                    "Consistency is used to justify retaining a defective or misleading generated asset.",
                ],
                [
                    ("FAILURE SIGNAL", "Each scene looks as if it belongs to a different brand."),
                    ("REPAIR MOVE", "Apply the same prompt anchors, palette, type and review checklist."),
                    ("QUALITY EVIDENCE", "Independent reviewers identify the same voice and visual cues across assets."),
                ],
            ),
        ],
    ),
    dict(
        num=3,
        code="03",
        title="Creating and Editing Videos with Generative AI",
        subtitle="Generated visuals and B-roll · Voiceovers, avatars and text-to-video · Editing, captions and effects · Music and transitions",
        weighting="Day 2 morning · 2 labs",
        concepts=[
            ("Shot function", "Every visual should orient, demonstrate, prove, transition or support the next action."),
            ("Continuity", "Subject, lighting, palette, direction and screen position remain coherent across generated scenes."),
            ("Editorial hierarchy", "Timing, captions, voice and sound guide attention without competing for it."),
            ("Rights and disclosure", "Source, permission, commercial music status and significant AI alteration are checked before use."),
        ],
        sections=[
            _section(
                "Generating Visuals, B-Roll and Images with AI",
                "Visual generation converts a written description and optional reference into candidate stills or clips. B-roll supports the main message by establishing place, demonstrating action, providing proof or smoothing a transition; it should not exist merely because a generator can make it.",
                "Generated media can contain temporal instability, impossible details, embedded marks, visual bias or inconsistent products. A shot-function plan and contact-sheet review keep the creator focused on communication and reject defects before editing time is spent.",
                [
                    "Translate each beat into a shot function and required evidence.",
                    "Write prompts with subject, action, setting, camera, light, composition and exclusions.",
                    "Generate small batches and label every candidate with prompt and version.",
                    "Review anatomy, object continuity, text, brand accuracy, rights and disclosure needs.",
                    "Select only assets that support the beat and can be cropped safely to 9:16.",
                ],
                [
                    "Beat: demonstrate a steady pour over coffee grounds.",
                    "Prompt: close overhead view, neutral hands, daylight pantry, copper dripper, navy surface, vertical composition, no text or logos.",
                    "Candidates with changing dripper shape or unreadable packaging are rejected and logged.",
                ],
                [
                    "A scene is illustrative and no truthful real-world capture is required.",
                    "The prompt and resulting asset can be documented and reviewed.",
                ],
                [
                    "The visual would imply a real event, endorsement or product result that did not occur.",
                    "A real person's likeness, private location or protected asset is used without permission.",
                ],
                [
                    ("FAILURE SIGNAL", "The asset is attractive but its action or object changes between frames."),
                    ("REPAIR MOVE", "Simplify the motion, shorten the clip or replace it with an authorised still plus camera movement."),
                    ("QUALITY EVIDENCE", "The selected asset performs one stated shot function without material artefacts."),
                ],
            ),
            _section(
                "AI Voiceovers, Avatars and Text-to-Video",
                "Text-to-speech creates audio from a script; avatar tools combine generated or authorised presenters with speech; text-to-video creates moving scenes from text or images. These systems accelerate prototyping, localisation and pickup lines, but synthetic likeness and voice require consent, clear context and careful listening.",
                "A natural-sounding voice can still mispronounce a brand, flatten meaning or imply a speaker identity that was never authorised. Reviewing intelligibility, pace, pronunciation, emotional fit and disclosure prevents speed from becoming deception.",
                [
                    "Prepare a final, verified script with pronunciation notes and natural punctuation.",
                    "Choose a licensed synthetic voice or record an authorised human voice.",
                    "Generate short segments so errors can be corrected without rebuilding the whole track.",
                    "Listen against the script, edit timing and keep music below the spoken message.",
                    "Record the tool, voice, date, permission and required disclosure in the asset register.",
                ],
                [
                    "The phrase 'one to sixteen brew ratio' is tested in a five-second voice sample first.",
                    "Mispronounced brand wording is respelled or recorded by an authorised speaker.",
                    "The final voiceover is divided by beat and aligned to the storyboard before visuals are generated.",
                ],
                [
                    "A licensed synthetic voice improves accessibility, consistency or localisation.",
                    "The audience will not be misled about who is speaking.",
                ],
                [
                    "The workflow clones a person's voice or likeness without explicit permission.",
                    "A realistic synthetic presenter would create a false endorsement or authoritative statement.",
                ],
                [
                    ("FAILURE SIGNAL", "The voice is intelligible but rushed, flat or mispronounces key terms."),
                    ("REPAIR MOVE", "Split the script, add punctuation and pronunciation guidance, then regenerate only the affected line."),
                    ("QUALITY EVIDENCE", "A listener can follow the message and identify synthetic use from the planned context or label."),
                ],
            ),
            _section(
                "Editing, Captions and Effects with AI Tools",
                "Editing converts selected assets into a timed argument. AI features can detect scenes, remove pauses, reframe subjects and generate captions, but the editor still decides rhythm, emphasis, continuity and whether the automatic result is accurate.",
                "Short-form attention is easily overloaded. A clear visual hierarchy, readable captions and deliberate cuts make the message understandable with sound on or off, while a full preview catches transcription errors and abrupt AI-assisted edits.",
                [
                    "Create a 9:16 project and assemble the voice or main action first.",
                    "Place visuals against the beat sheet and trim every clip to its communication job.",
                    "Generate captions, correct every word and break lines at natural phrase boundaries.",
                    "Apply restrained transitions, motion and effects only when they clarify change.",
                    "Preview full-screen on a phone-sized display and export a review copy.",
                ],
                [
                    "The three fixes each receive a labelled close-up and a clean cut on the voiceover phrase.",
                    "Auto captions are corrected from 'contact thyme' to 'contact time' and kept clear of interface overlays.",
                    "A before/after comparison uses one simple split rather than several decorative effects.",
                ],
                [
                    "Automatic transcription or reframing can accelerate a reviewed edit.",
                    "The creator can correct errors and control the final timeline.",
                ],
                [
                    "Captions are assumed correct because the audio sounded clear.",
                    "Effects compete with the message or conceal continuity problems.",
                ],
                [
                    ("FAILURE SIGNAL", "Important text is cropped, mistranscribed or hidden by platform controls."),
                    ("REPAIR MOVE", "Use safe-zone guides, shorten phrases and review every caption at playback speed."),
                    ("QUALITY EVIDENCE", "The video remains understandable without sound and comfortable with sound."),
                ],
            ),
            _section(
                "Adding Music, Sound and Transitions",
                "Audio has layers: voice or primary sound, music, ambience and effects. Transitions connect scenes in picture and sound. For brand or product content, TikTok recommends music from its Commercial Music Library unless the creator has all necessary rights for another track.",
                "Music creates energy but can also obscure speech or introduce a rights problem. Sound and transitions should support pacing, meaning and brand fit; a documented rights source and balanced mix are part of production quality.",
                [
                    "Choose the primary audio layer and set it before adding music.",
                    "Select original, licensed or commercially cleared music and record its source.",
                    "Lower music beneath speech and use short fades to avoid clicks.",
                    "Add effects only where they clarify an action or emphasis.",
                    "Run a headphone, speaker and muted playback check before export.",
                ],
                [
                    "A quiet pour sound establishes the demonstration, then a cleared low-key beat supports the three fixes.",
                    "Music drops slightly under each spoken instruction and fades before the final call to action.",
                    "The rights log names the library, track, date and intended commercial use.",
                ],
                [
                    "The source license covers the intended channel and purpose.",
                    "Sound contributes rhythm, clarity or an accessible cue.",
                ],
                [
                    "A trending song is used for brand promotion without commercial permission.",
                    "Loud effects or rapid transitions reduce intelligibility or comfort.",
                ],
                [
                    ("FAILURE SIGNAL", "The voice is hard to hear or the team cannot explain the music rights."),
                    ("REPAIR MOVE", "Rebalance the mix and replace the track with documented cleared audio."),
                    ("QUALITY EVIDENCE", "The rights log is complete and the mix works on ordinary phone speakers."),
                ],
            ),
        ],
    ),
    dict(
        num=4,
        code="04",
        title="Publishing, Optimising and Scaling TikTok Content",
        subtitle="Publishing and scheduling · Performance analysis and iteration · Cross-platform repurposing · Scaled production workflow",
        weighting="Day 2 afternoon · 2 labs",
        concepts=[
            ("Publish gate", "Message, metadata, accessibility, rights, disclosure and settings are reviewed before a post goes live."),
            ("Metric chain", "Reach, retention, engagement and action metrics answer different questions at different stages."),
            ("One-variable test", "Change one meaningful element while keeping the audience promise and evidence stable."),
            ("Production governance", "Templates, owners, states, asset registers and stop rules enable quality at higher volume."),
        ],
        sections=[
            _section(
                "Publishing and Scheduling TikTok Videos",
                "Publishing is the final packaging and governance step: video file, cover, description, relevant tags, accessibility, audience setting, disclosure, rights and timing. Scheduling separates production from release, but it does not remove the need for a final account-level preview and approval.",
                "A technically correct export can still fail through clipped text, unclear metadata, an incorrect privacy setting or missing AI disclosure. A publish gate makes these visible and creates a recoverable record of what was approved.",
                [
                    "Validate 9:16 framing, resolution, sound, captions and safe zones.",
                    "Write accurate cover text, description, keywords and relevant tags.",
                    "Complete rights, permission, commercial-content and AI-generated-content checks.",
                    "Choose audience, interaction and timing settings intentionally.",
                    "Preview the final post screen, record approval and publish or schedule.",
                ],
                [
                    "The Harbour Bean video exports as MP4 at 1080 × 1920.",
                    "The description names the three coffee variables without adding new claims.",
                    "The checklist records synthetic voice and visuals, cleared music source and the appropriate creator label.",
                ],
                [
                    "The account owner has reviewed the final file and platform settings.",
                    "Every material asset and claim has a traceable source or permission.",
                ],
                [
                    "The post screen introduces a new unsupported claim or removes necessary context.",
                    "Disclosure or commercial-music requirements are unresolved.",
                ],
                [
                    ("FAILURE SIGNAL", "The right video is uploaded with the wrong cover, setting or disclosure."),
                    ("REPAIR MOVE", "Use a two-person or two-pass publish gate with saved evidence."),
                    ("QUALITY EVIDENCE", "The approval log reconstructs the file, metadata, settings and reviewer."),
                ],
            ),
            _section(
                "Analysing Performance and Iterating with AI",
                "Analytics describe behaviour, not creative truth. TikTok Studio provides account and post metrics such as views, engagement and audience information. A useful analysis connects the content hypothesis to the relevant metric, compares like with like and states uncertainty before proposing the next test.",
                "AI is good at organising a supplied dataset and suggesting questions, but it can over-explain small samples or confuse correlation with cause. A baseline, denominator, comparison window and one-variable test keep iteration disciplined.",
                [
                    "Restate the video's audience, promise and experiment hypothesis.",
                    "Inspect reach, early retention, completion, engagement and action metrics at the correct grain.",
                    "Compare with a relevant baseline and note sample or data limitations.",
                    "Ask AI for observations, alternative explanations and missing evidence—not a guaranteed cause.",
                    "Choose one change, one success measure and one review window.",
                ],
                [
                    "Synthetic data shows strong first-three-second hold but a drop during the second fix.",
                    "The team considers pace, visual clarity and caption density as hypotheses.",
                    "The next version shortens that beat while keeping hook, audience and offer constant.",
                ],
                [
                    "A defined hypothesis and comparable baseline exist.",
                    "The team can distinguish observations from interpretations.",
                ],
                [
                    "One video's result is used to declare a universal platform rule.",
                    "AI receives personal viewer data or invents reasons not present in the dataset.",
                ],
                [
                    ("FAILURE SIGNAL", "The report lists metrics but no decision or uncertainty."),
                    ("REPAIR MOVE", "Link each metric to a question, label hypotheses and select one bounded test."),
                    ("QUALITY EVIDENCE", "The iteration plan names the variable, baseline, target and review date."),
                ],
            ),
            _section(
                "Repurposing Content Across Platforms",
                "Repurposing preserves the core promise and evidence while adapting duration, framing, metadata, safe zones, pacing and audience expectations for another platform. It is redesign, not identical cross-posting or automatic cropping.",
                "A strong source video can support several channels, but each surface has different controls and viewing contexts. An adaptation matrix prevents clipped subjects, duplicated captions and platform-inappropriate calls to action.",
                [
                    "Identify the invariant message, proof and brand elements.",
                    "List destination format, duration, safe-zone, audio and metadata requirements.",
                    "Create a platform-specific cut from the clean master, not a downloaded watermarked post.",
                    "Rewrite the opening and next action for the destination audience context.",
                    "Review captions, crop, rights and disclosure again before export.",
                ],
                [
                    "The 32-second vertical master becomes a 25-second Reel and a 45-second Short with an expanded explanation.",
                    "The three verified fixes remain unchanged, but cover text and next action adapt to each surface.",
                    "Each export uses the clean project master and its own checklist row.",
                ],
                [
                    "The core content remains relevant and rights cover the destination.",
                    "A platform-specific change improves fit without changing the evidence.",
                ],
                [
                    "The crop hides the demonstration or interface-safe text.",
                    "A music or asset license does not cover the destination or commercial purpose.",
                ],
                [
                    ("FAILURE SIGNAL", "The same file is posted everywhere with clipped text and generic metadata."),
                    ("REPAIR MOVE", "Build a destination matrix and create separate exports from the clean master."),
                    ("QUALITY EVIDENCE", "Each version passes format, message, rights and accessibility review."),
                ],
            ),
            _section(
                "Scaling a Content Production Workflow with AI",
                "A scalable workflow moves each content item through defined states—from brief and evidence to concept, script, assets, edit, review, publish and learn. Templates and AI reduce repeated effort; named owners, versioning, rights records and stop rules prevent quality from collapsing as volume grows.",
                "More output magnifies weak briefs, unsupported claims and asset confusion. Production capacity should grow only when the team can see work in progress, reconstruct decisions and learn from published results.",
                [
                    "Define required artifacts and entry/exit criteria for every production state.",
                    "Create reusable prompt, script, storyboard, asset-register, edit and publish templates.",
                    "Assign owners for factual review, rights, edit quality and account approval.",
                    "Track cycle time, rework, blocked items and post-publication learning.",
                    "Automate only low-risk transformations with human checks before external use.",
                ],
                [
                    "Harbour Bean's board has Brief, Script, Assets, Edit, Review, Scheduled and Learn states.",
                    "An item cannot enter Edit without a verified script and asset register.",
                    "Weekly review examines both content signals and production defects before increasing cadence.",
                ],
                [
                    "The team repeats a stable workflow with clear controls and owners.",
                    "Templates save time without hiding evidence, rights or approval status.",
                ],
                [
                    "Automation would scrape, impersonate, spam or publish without review.",
                    "The team measures volume while ignoring rework, rights risk or audience value.",
                ],
                [
                    ("FAILURE SIGNAL", "Publishing volume rises while defects and rework become invisible."),
                    ("REPAIR MOVE", "Add state gates, named reviewers, cycle-time and defect measures."),
                    ("QUALITY EVIDENCE", "Any post can be traced from source brief through assets, approval and learning."),
                ],
            ),
        ],
    ),
]

DAY_THEMES = {
    1: "Audience, prompts, ideas, scripts and a coherent content system",
    2: "Generated media, editing, publishing, analytics and scaled production",
}


def SCHEDULE(lab_titles):
    return {
        1: (
            DAY_THEMES[1],
            [
                ("9:30", "9:50", 20, "admin", "Welcome, course orientation and learning approach"),
                ("9:50", "10:50", 60, "topic", "Topic 1 — Getting Started with Generative AI for TikTok"),
                ("10:50", "11:05", 15, "break", "Tea break"),
                ("11:05", "12:05", 60, "lab", "Hands-on: " + lab_titles([1])),
                ("12:05", "13:00", 55, "lab", "Hands-on: " + lab_titles([2])),
                ("13:00", "14:00", 60, "lunch", "Lunch break"),
                ("14:00", "15:10", 70, "topic", "Topic 2 — Generating Scripts, Ideas and Hooks with AI"),
                ("15:10", "15:25", 15, "break", "Tea break"),
                ("15:25", "16:25", 60, "lab", "Hands-on: " + lab_titles([3])),
                ("16:25", "17:25", 60, "lab", "Hands-on: " + lab_titles([4])),
                ("17:25", "18:10", 45, "lab", "Guided production clinic: refine Labs 1–4 and complete the Day 1 checkpoint"),
                ("18:10", "18:30", 20, "recap", "Day 1 recap, reflection and Q&A"),
            ],
        ),
        2: (
            DAY_THEMES[2],
            [
                ("9:30", "10:30", 60, "topic", "Topic 3 — Creating and Editing Videos with Generative AI"),
                ("10:30", "11:30", 60, "lab", "Hands-on: " + lab_titles([5])),
                ("11:30", "11:45", 15, "break", "Tea break"),
                ("11:45", "12:45", 60, "lab", "Hands-on: " + lab_titles([6])),
                ("12:45", "13:00", 15, "recap", "Morning edit checkpoint and troubleshooting"),
                ("13:00", "14:00", 60, "lunch", "Lunch break"),
                ("14:00", "15:00", 60, "topic", "Topic 4 — Publishing, Optimising and Scaling TikTok Content"),
                ("15:00", "15:15", 15, "break", "Tea break"),
                ("15:15", "16:15", 60, "lab", "Hands-on: " + lab_titles([7])),
                ("16:15", "17:15", 60, "lab", "Hands-on: " + lab_titles([8])),
                ("17:15", "18:00", 45, "lab", "Guided workflow clinic: complete the portfolio and 30-day production plan"),
                ("18:00", "18:30", 30, "recap", "Course recap, workplace action planning and Q&A"),
            ],
        ),
    }


COURSE_OVERVIEW = dict(
    section_title="The Human-Led AI Video Production System",
    concepts_title="Six Ideas That Keep Video Useful and Trustworthy",
    concepts=[
        ("Audience before output", "Start with a real viewer job, not an exciting generator feature."),
        ("One promise", "Every short video earns attention by making and fulfilling one clear promise."),
        ("Proof boundary", "Use approved facts and mark unknowns instead of asking AI to fill gaps."),
        ("Scene function", "Each visual or sound orients, demonstrates, proves, transitions or closes."),
        ("Rights and disclosure", "Record source, permission, commercial status and significant AI alteration."),
        ("Learn through signals", "Use relevant metrics and one-variable tests, not algorithm myths."),
    ],
    framework_title="The A-P-P-S-O-R Prompt Pattern",
    framework=[
        ("Audience", "Name the viewer, situation, tension and desired outcome."),
        ("Purpose", "State the one job the content should perform."),
        ("Proof", "Supply approved facts, examples and source boundaries."),
        ("Style", "Set voice, visual, pacing, brand and avoid rules."),
        ("Output", "Specify concepts, duration, beats, columns and file hand-off."),
        ("Review", "Require truth, rights, disclosure, accessibility and feasibility checks."),
    ],
    statement=dict(
        headline="AI accelerates production; people own the promise, proof and publish decision.",
        body="A strong short-form workflow combines creative variation with audience relevance, traceable assets and deliberate human review.",
        kicker="THE CORE IDEA",
    ),
    pillars_title="What You Will Build",
    pillars=[
        ("Discover", ["An audience and prompt brief", "A scored idea bank with hook alternatives"]),
        ("Design", ["A timed script and storyboard", "A four-week brand-consistent content system"]),
        ("Produce", ["A generated asset and rights register", "A captioned vertical review export"]),
        ("Improve", ["A publish and adaptation pack", "An analytics-led iteration and scaling plan"]),
    ],
    arc_title="The Eight-Lab Learning Arc",
    arc=[
        "Brief — define the audience, source facts, tool roles and responsible-use boundary.",
        "Explore — generate distinct angles and hooks, then select with explicit criteria.",
        "Script — coordinate spoken line, visual, on-screen text and timing.",
        "Systemise — turn the same brand promise into a sustainable content calendar.",
        "Generate — create candidate visuals and voice with provenance and quality checks.",
        "Edit — assemble, caption, mix, preview and export a vertical video.",
        "Publish — package metadata, settings, rights, disclosure and adaptations.",
        "Learn — diagnose synthetic performance data and design the next controlled test.",
    ],
    deep_dives=[
        dict(
            title="The Content Traceability Chain",
            kicker="FROM SOURCE TO LEARNING",
            items=[
                ("Source", "Approved brand fact, audience evidence or authoritative guidance."),
                ("Claim", "The exact statement the source supports."),
                ("Beat", "The timed message and media job that communicates the claim."),
                ("Asset", "The generated, recorded or licensed material used in the beat."),
                ("Approval", "The human review of truth, rights, accessibility and disclosure."),
                ("Signal", "The post-publication observation that informs the next test."),
            ],
        ),
        dict(
            title="Four Checks Before Any Export",
            kicker="HUMAN REVIEW",
            items=[
                ("Message", "Does the body fulfil the opening promise for the intended audience?"),
                ("Media", "Are visuals, voice, captions, timing and sound coherent and readable?"),
                ("Trust", "Are facts, permissions, rights and AI disclosure complete?"),
                ("Delivery", "Are format, safe zones, settings, owner and next action correct?"),
            ],
        ),
    ],
)

LAB_SHOTS = {}

LG_INTRO = (
    "This Learner Guide accompanies Generative AI for Video Creation (C1373), a two-day, "
    "15-hour course for beginners who want to plan, create, edit and improve short-form video "
    "with generative AI. It follows the four-topic outline published by Tertiary Infotech "
    "Academy and teaches each concept before the related hands-on work."
)

LG_INTRO2 = (
    "Eight connected labs use the synthetic Harbour Bean Co. scenario. You will move from an "
    "audience and prompt brief to an idea bank, timed script, content calendar, generated asset "
    "register, captioned vertical video, publish pack and analytics-led scaling plan. Every "
    "checkpoint is a complete artifact, so you can rejoin safely or later substitute approved "
    "information from your own organisation."
)

LG_SETUP = dict(
    needs=[
        "A Windows or Mac laptop with a modern browser, a text editor and a spreadsheet application.",
        "An approved generative AI assistant such as ChatGPT, Claude or Microsoft Copilot.",
        "CapCut Desktop or an equivalent editor that supports a 9:16 project, captions, audio and MP4 export.",
        "Optional access to CapCut AI video or another organisation-approved image/video generator; supplied placeholders are the fallback.",
        "The files in labs/assets/, downloaded together into one C1373 working folder.",
        "Only synthetic, public or organisation-approved information and media.",
    ],
    verify_text=(
        "Open your approved AI assistant and send the prompt below. Confirm the response contains "
        "exactly six labelled lines. Then open harbour-bean-brand-brief.md, "
        "content-calendar.csv and synthetic-tiktok-analytics.csv from labs/assets/."
    ),
    verify_code=(
        "For a short video about fixing bitter office coffee, respond with exactly six lines "
        "labelled Audience, Purpose, Proof, Style, Output and Review."
    ),
    conventions=[
        "Prompt blocks are pasted into an approved AI assistant after replacing angle-bracket placeholders.",
        "Menu labels can move; use the equivalent current control and record any difference in the lab file.",
        "Keep generated outputs, prompts and rights notes in the project folder rather than only in a tool history.",
        "Use the supplied synthetic Harbour Bean scenario when you do not have approved workplace material.",
        "Never paste credentials, personal data, confidential footage or private likenesses into a course tool.",
    ],
)

LAB_NOTE = (
    "Use only the supplied synthetic scenario or material you are authorised to use. "
    "Do not clone a real person's face or voice, copy another creator's identity, or use "
    "unlicensed music. Verify claims, rights, accessibility and AI disclosure before any external use."
)

LG_WRAPUP = dict(
    title="Wrap-Up and Source Notes",
    intro=(
        "The finished Harbour Bean portfolio demonstrates a complete short-form production chain "
        "from audience evidence to a governed improvement plan. Product interfaces will change, "
        "but the audience, proof, scene-function, rights and learning controls remain durable."
    ),
    sections=[
        dict(
            title="The Workflow You Can Reuse",
            bullets=[
                "Define one audience job and one truthful content promise.",
                "Ground prompts in approved sources and require visible review gates.",
                "Design the hook, body, close and beat sheet before generating media.",
                "Create candidate assets in small batches and record provenance.",
                "Edit for clarity, captions, safe zones, balanced audio and brand continuity.",
                "Publish with rights, settings and disclosure checks, then run one-variable learning tests.",
            ],
        ),
        dict(
            title="Authoritative References Used",
            bullets=[
                "Tertiary Infotech Academy course outline: https://www.tertiarycourses.com.sg/generative-ai-for-video-creation.html",
                "TikTok recommendation systems: https://support.tiktok.com/en/using-tiktok/exploring-videos/how-tiktok-recommends-content",
                "TikTok AI-generated content guidance: https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content",
                "TikTok Studio features and analytics: https://support.tiktok.com/en/using-tiktok/creating-videos/tiktok-studio",
                "TikTok commercial use of music: https://support.tiktok.com/en/business-and-creator/creator-and-business-accounts/commercial-use-of-music-on-tiktok",
                "TikTok Creative Codes: https://ads.tiktok.com/business/library/TikTok_CreativeCodes_May2023.pdf",
                "CapCut AI video maker: https://www.capcut.com/tools/free-ai-video-generator",
                "CapCut auto-caption troubleshooting and workflow: https://www.capcut.com/help/auto-captions",
                "CapCut text-to-speech: https://www.capcut.com/tools/ai-text-to-speech",
                "OpenAI prompt-engineering best practices: https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices",
            ],
        ),
        dict(
            title="Non-Negotiable Human Checks",
            bullets=[
                "Confirm the tool, data, likeness, voice, music and destination rights for the intended use.",
                "Trace material claims to source evidence and remove unsupported wording.",
                "Preview the entire video with sound on, sound off and a phone-sized frame.",
                "Name the person who approves the final file, settings, disclosure and learning plan.",
            ],
        ),
    ],
)

LG_NEXT_STEPS = [
    "Rebuild the Harbour Bean video with a different angle while keeping the same verified source facts.",
    "Create a source pack for one approved workplace brand and replace every synthetic field systematically.",
    "Publish only through the account owner's current approval process and retain the publish checklist.",
    "Review three to five comparable posts before changing a content-system rule.",
    "Audit prompt templates, tool permissions, music sources and disclosure practice every month.",
]

LG_GLOSSARY = [
    ("Angle", "The specific perspective or tension through which a broad topic becomes relevant."),
    ("A-P-P-S-O-R", "The course prompt pattern: Audience, Purpose, Proof, Style, Output and Review."),
    ("Asset register", "A record of each media item's source, prompt, version, rights, disclosure and use."),
    ("Beat", "A short timed unit that coordinates narration, visual, on-screen text and sound."),
    ("B-roll", "Supporting footage used to establish, demonstrate, prove or transition around the main action."),
    ("Call to action", "The next step invited from the viewer after the promise has been delivered."),
    ("Caption", "Text that represents spoken content or adds essential on-screen context."),
    ("Completion rate", "The proportion of video starts that reached the end, subject to the platform's current definition."),
    ("Content pillar", "A durable theme connected to audience needs and credible brand knowledge."),
    ("Content series", "A repeatable format and promise that can support multiple episodes."),
    ("Hook", "The opening verbal, visual, text or sound cue that establishes relevance."),
    ("Human review gate", "A defined point where a person verifies and approves the work before it progresses."),
    ("Iteration hypothesis", "A testable explanation for a result and the one change proposed for the next version."),
    ("Prompt anchor", "A stable phrase that preserves subject, environment, visual or brand continuity across generation."),
    ("Provenance", "Information about where an asset came from, how it was made and how it may be used."),
    ("Recommendation system", "A system that selects and ranks content according to predicted relevance and interest."),
    ("Safe zone", "The visible area kept clear of interface controls, cropping and essential-text collisions."),
    ("Synthetic media", "Images, video or audio generated or materially altered by AI."),
    ("Text-to-speech", "Technology that generates spoken audio from written text."),
    ("Watch time", "The amount of time viewers spend watching a video, interpreted with reach and duration context."),
]

NEXT_STEPS = dict(
    title="A Practical 30-Day Application Plan",
    items=[
        "Week 1 — approve the brand source pack, audience and content pillars.",
        "Week 2 — script and produce two variants from one evidence-based idea.",
        "Week 3 — publish through the account owner's gate and capture comparable signals.",
        "Week 4 — review production defects and audience response, then choose one controlled improvement.",
    ],
)

THANK_YOU = dict(
    body=(
        "You now have a complete human-led workflow for planning, generating, editing, "
        "publishing and improving short-form video with generative AI."
    ),
    kicker="CREATE WITH PURPOSE · VERIFY WITH CARE · LEARN FROM SIGNALS",
)

TRAINER_TEAM = [
    (
        "Allen Wong",
        "Digital marketing strategist and ACTA-certified trainer with cross-industry experience in data-led campaigns, e-commerce growth and practical AI-assisted marketing.",
    ),
]

ICE_BREAKER = [
    "Your name, role and the short-form channel or audience you work with.",
    "Your current experience with AI assistants, generated media or video editing.",
    "One production bottleneck and one trust risk you want this course to address.",
]

VERSION_HISTORY = [
    (
        "1.0",
        VERSION_DATE,
        "Initial aligned release: PPT, Learner Guide, Lesson Plan and eight connected labs.",
        TRAINER,
    ),
]
