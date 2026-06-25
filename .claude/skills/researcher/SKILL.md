---
name: researcher
description: Searches the internet for real, open job postings that match the candidate's qualifications (profile.yml) and interests (prospect.md). Saves results to research_output.md. Use when you need to find new job opportunities.
allowed-tools: WebSearch Read Write Bash
---

You are conducting a targeted job search. Your goal is to find real, currently open job postings that match this candidate's qualifications and interests.

## Step 0: Create Run Folder

Generate a unique run folder name by running:

```bash
python scripts/create_folder.py 
```

Save the printed folder name as the **run folder** (e.g., `runs/20260420_143022_x7k`).

## Step 1: Load Context

Read this files from the project root:
- `prospect.md` — candidate's job interests, target roles, deal-breakers, preferred companies

## Step 2: Run Targeted Web Searches and Build Job List

Using the exa web search tool, execute 6–10 diverse searches to maximize coverage. **Every search call MUST include:**
- `freshness: "72 hours"` — limits results to pages published/indexed in the last 7 days
- `includeDomains: ["job-boards.greenhouse.io", "jobs.lever.co", "builtin.com", "jobs.ashbyhq.com", "climatedraft.org", "wellfound.com", "climatebase.org", "welcometothejungle.com", "idealist.org", "theimpactjob.com", "greenjobs.net", "data.org"]` — targets reliable job boards with accurate posting dates

Use varied queries such as:

- `Senior Machine Learning Engineer remote production LLM RAG open role`
- `Lead ML Engineer LLM RAG remote hiring now`
- `Senior AI Engineer insurtech OR fintech remote apply`
- `Data Scientist production MLOps remote`
- `Machine Learning Engineer remote open role apply now`
- `Senior ML Engineer OR Lead Data Scientist remote job posting`
- `ML Engineer LLM SageMaker remote job`
- Any searches derived from specific companies or industries listed in prospect.md
- You do not need to include compensation targets in the query, but you can include location preferences

For each job found, capture:
- **Title** — exact job title
- **Company** — company name
- **Company Mission** - mission statement from company's website
- **URL** — direct link to the job posting
- **Salary** — if listed (or "Not listed")
- **Location/Remote** — remote, hybrid, or location
- **Key Requirements** — 3–5 bullet points from the job description
- **Years of Experience Required** — number of years experience 
- **Highest Level of Education** — bachelors, masters, phd, or not listed
- **Date Posted** — if visible

Aim for 15–100 unique postings. Prioritize variety (different companies, not 10 from the same company).

For each search, scan the results and extract real, open postings. Skip sponsored content you cannot verify. Skip any result that appears closed or removed.

Never run Exa searches in main context. Always spawn Task agents:
- Agent returns distilled output (brief markdown or compact JSON)
- Main context stays clean regardless of search volume

## Step 3. Refine List
Eliminate jobs that are clearly outside of the user's job preferences (dealbreakers, compensation, location), aiming for 5 to 15 highly qualified leads. 
For each remaining job, perform just one additional web search and web crawls with exa, populating the full job description and filling in any unknown values. 


## Step 4: Save to research_output.md

Write all findings to `<run_folder>/research_output.md` using this format:

```markdown
# Job Research Output
Generated: [today's date]
Source files: prospect.md, profile.yml

## Raw Job List

### 1. [Job Title] — [Company]
- **URL:** [link]
- **Salary:** [amount or "Not listed"]
- **Location:** [remote/hybrid/location]
- **Posted:** [date or "Unknown"]
- **Full Job Description:** - full body of text from job post
- **Years of Experience Required** — number of years experience 
- **Highest Level of Education** — bachelors, masters, phd, or not listed

[repeat for each job...]

## Search Queries Used
[list all queries you ran]
```

## Step 6: Confirm

After saving, tell the user:
- The run folder path (e.g., `runs/20260420_143022_x7k`)
- How many queries were requested
- How many jobs were returned by the query
- How many jobs are in the final output, and why the other ones were eliminated
- That they can now run `/summarizer <run_folder>` to get the top 5 ranked matches
