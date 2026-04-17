---
name: orchestrator
description: Runs the full job search pipeline end-to-end: searches the internet for matching jobs (researcher), then scores and ranks the top 5 matches (summarizer), then emails the digest (emailer). Produces research_output.md, top5_matches.md, and sends an email.
allowed-tools: WebSearch Read Write Bash
---

Run the three pipeline skills in sequence. Complete each fully before starting the next.

1. Read `.claude/skills/researcher/SKILL.md` and follow its instructions exactly.
2. Read `.claude/skills/summarizer/SKILL.md` and follow its instructions exactly.
3. Read `.claude/skills/emailer/SKILL.md` and follow its instructions exactly.
