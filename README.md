# C1373---Generative-AI-for-Video-Creation

Single-source NON-WSQ courseware for **Generative AI for Video Creation (C1373)**.

The repository generates and keeps aligned:

- Trainer slide deck (`.pptx`) and learner slides (`.pdf`)
- Learner Guide (`.docx`, `.pdf`, and Markdown mirror)
- Lesson Plan (`.docx` and `.pdf`)
- Eight connected hands-on labs and their synthetic support files

Course outline: https://www.tertiarycourses.com.sg/generative-ai-for-video-creation.html

## Build

From Git Bash on Windows:

```bash
COURSE_REPO="$(pwd)" bash ".agents/skills/non-wsq-courseware-build/build/build_courseware.sh"
```

The content source is:

- `.agents/skills/non-wsq-courseware-build/build/course_data.py`
- `.agents/skills/non-wsq-courseware-build/build/data_domain1.py` through `data_domain4.py`

## Quality check

```bash
python ".agents/skills/non-wsq-courseware-qa/scan_prohibited.py" .
```

Generated learner-facing files are published only after the mechanical, structural, alignment, and visual checks pass.
