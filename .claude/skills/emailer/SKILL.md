---
name: emailer
description: Sends an email digest to jhquilty99@gmail.com with the top 3 job matches from top5_matches.md. Uses Gmail SMTP with a GMAIL_APP_PASSWORD env var. Run after /summarizer or /orchestrator.
allowed-tools: Read Write Bash
---

You are preparing and sending a job search results digest email. You handle all formatting; the Python script only handles delivery.

## Parameters

The first argument is the **run folder path** (e.g., `runs/20260420_143022_x7k`).  
If no argument was provided, ask the user: "Which run folder should I email? (e.g., `runs/20260420_143022_x7k`)"

---

## Step 1: Check GMAIL_APP_PASSWORD

Run:

```bash
python -c "import os; from dotenv import load_dotenv; from pathlib import Path; load_dotenv(Path('scripts/send_email.py').parent.parent / '.env'); print('SET' if os.environ.get('GMAIL_APP_PASSWORD') else 'MISSING')"
```

If the output is `MISSING`, stop and print:

> **Email not sent — GMAIL_APP_PASSWORD is not set.**
>
> Add it to your `.env` file:
> ```
> GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx
> ```
> Get one at myaccount.google.com/apppasswords (requires 2-Step Verification).

---

## Step 2: Read and summarize top5_matches.md

Read `<run_folder>/top5_matches.md`. If it doesn't exist, stop and print:
> **Email not sent — `<run_folder>/top5_matches.md` not found. Run `/summarizer <run_folder>` or `/orchestrator` first.**

Extract and understand:
- The generated date and number of jobs evaluated
- The top 3 jobs: title, company, company mission, score, URL, salary, location, why it's a strong match, honest gaps

---

## Step 3: Write email_draft.json

Write `<run_folder>/email_draft.json` with this exact structure:

```json
{
  "subject": "Job Search Results — [generated date] — [N jobs evaluated]",
  "plain": "[plain text body — see format below]",
  "html": "[HTML body — see format below]"
}
```

### Plain text format

```
Job Search Results
Generated: [date]
Jobs evaluated: [N]

TOP 3 HIGHLIGHTS
================

#1 — [score] | [title] at [company]
URL: [url]
Salary: [salary] | Location: [location]
Why: [2-sentence summary of why it's a strong match]
Gap: [1-sentence honest gap]

#2 — ...

#3 — ...

Full analysis with all 5 jobs: top5_matches.md
---
Sent by your Claude Code job search pipeline.
```

### HTML format

Use inline styles throughout. Max width 700px, centered, Arial font, 24px padding, `color:#1a1a1a`.

**Header block:**
- `<h2>` "Job Search Results", margin 0
- `<p>` with generated date and jobs-evaluated count in `color:#555;font-size:14px`

**Summary table** (all 3 jobs, `font-size:13px`, `border-collapse:collapse`, full width, `margin-bottom:28px`):
- Header row: `background:#f5f5f5`
- Columns: #, Score (bold), Role (hyperlinked in `color:#0066cc`), Company, Salary, Location
- Alternate rows: white / `background:#fafafa`

**Per-job cards** (one per job, `margin-bottom:24px`):

Each card is a `<div>` with a 4px left border, light tinted background, and 12px 16px padding. Use these colors by rank:
- #1: border `#0066cc`, background `#f7f9ff` (blue)
- #2: border `#27ae60`, background `#f7fff9` (green)
- #3: border `#e67e22`, background `#fffbf5` (orange)

Inside each card:
- `<h3>` with rank, score, title, company (`font-size:16px`, margin `0 0 6px 0`)
- `<p>` with URL (linked), salary, location — `font-size:13px`
- `<p>` company mission in italic grey (`color:#555;font-size:13px`)
- `<p>` **Why:** plain text explanation (`font-size:13px`)
- `<p>` **Gap:** in `color:#c0392b;font-size:13px`

**Footer:** `<p>` in `color:#999;font-size:12px`, top border `1px solid #eee`, padding-top 12px:
`"Full analysis (all 5 jobs + STAR experience mapping): top5_matches.md · Sent by your Claude Code job search pipeline."`

---

## Step 4: Send the email

Run:

```bash
python scripts/send_email.py <run_folder>/email_draft.json
```

On success, report: `Email sent to jhquilty99@gmail.com — "[subject]"`

On any error, print the full error message.
