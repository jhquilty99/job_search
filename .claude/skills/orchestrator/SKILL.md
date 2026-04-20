---
name: orchestrator
description: Runs the full job search pipeline end-to-end: searches the internet for matching jobs (researcher), then scores and ranks the top 5 matches (summarizer), then emails the digest (emailer). Produces research_output.md, top5_matches.md, and sends an email.
allowed-tools: WebSearch Read Write Bash
---

Run the three pipeline skills in sequence. Complete each fully before starting the next.

## Step 0: Generate Run Folder

Before running any skill, generate a unique run folder name by running:

```bash
python scripts/create_folder.py
```

Save the printed value as the **run folder** for this entire pipeline run (the script creates the folder automatically).

## Steps 1–3: Run Pipeline

1. Read `.claude/skills/researcher/SKILL.md` and follow its instructions exactly, but **skip its Step 0** — use the run folder you already generated above.
2. Read `.claude/skills/summarizer/SKILL.md` and follow its instructions exactly. The run folder argument is `<run_folder>`.
3. Read `.claude/skills/emailer/SKILL.md` and follow its instructions exactly. The run folder argument is `<run_folder>`.
