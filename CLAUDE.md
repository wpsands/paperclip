# CLAUDE.md

GTM Job Description Mining for SandsDX Pitches

## Mission

- Find 50 B2B SaaS companies from Series A to midmarket that are hiring director level GTM roles
- Pull those job descriptions and break them into specific requirements
- Find the patterns that show up across companies
- Pick out the requirements an AI agent can deliver today
- Do the work for each target company before reaching out
- Send the finished work to the VP or C level buyer as the hook for SandsDX services

## Point of View

- A job post is the company telling you, in writing, what it needs and what it will pay for
- A director role costs $180K to $300K or more fully loaded and takes 3 to 6 months to fill
- Finished work from week one beats a pitch deck
- The pitch: "Your JD asks for X. Here it is, done. Let me run the rest while you hire, or instead of hiring."

## Target Companies

- B2B SaaS only
- Funding from Series A to Series D, or bootstrapped midmarket
- 50 to 1,000 employees
- About $5M to $150M ARR, estimated where it isn't reported
- At least one open director level GTM role posted in the last 60 days
- Skip agencies, consultancies, staffing firms, and B2C companies

## Target Roles

- Director of Digital Marketing, Demand Gen, or Growth
- Director of Product Marketing
- Director of Customer Success
- Director of RevOps, Sales Ops, or GTM Ops
- Include Head of and Sr Director titles that have the same scope

## Sources

- Job boards: Greenhouse, Lever, Ashby, Workable, company careers pages, LinkedIn Jobs, Wellfound
- Funding and size: Crunchbase, PitchBook, LinkedIn company pages, press releases
- Connected tools to use first: Clay (company and contact search), Ahrefs and Semrush (site and SEO baselines), Google Drive (save outputs)
- Save the source URL and date pulled for every job description

## Workflow

### Phase 1: Company List

- Build `data/companies.csv` with these fields: company, url, stage, last round, employees, ARR estimate, open GTM roles, source links
- Hit 50 companies with a roughly even split across the 4 role families
- Every row needs a source link

### Phase 2: Collect JDs

- Save each JD as raw text in `data/jds/{company}_{role}.md`
- Add a header with the title, URL, date posted, date pulled, location, and salary band if listed

### Phase 3: Extract Requirements

- Split each JD into single requirements in `data/requirements.csv`
- Fields: company, role family, requirement text, category, deliverable type, tools named, metric named, seniority signal
- Categories: strategy, execution, analytics, content, ops and systems, team leadership, cross functional
- Deliverable type: document, analysis, campaign, system build, process, recurring report

### Phase 4: Pattern Analysis

- Count how often each requirement shows up overall and within each role family
- Find the top 15 requirements per role family
- Track how often each tool is named (HubSpot, Salesforce, Gong, Clay, etc.)
- Track how often each metric is named (pipeline, NRR, CAC, win rate, etc.)
- Note differences by funding stage
- Write up the findings in `output/patterns.md` with counts, percentages, and links to the source JDs

### Phase 5: Agent Opportunity Scoring

- Score each common requirement from 1 to 5 on the 5 criteria below
- **Agent doable now:** can Claude plus the connected tools finish it without access inside the company?
- **Public inputs only:** can it be built from the company's website, content, reviews, SEO data, and competitors?
- **Buyer visible:** would a VP see the value in under 2 minutes?
- **Time to deliver:** can it be done in 4 hours or less?
- **Frequency:** what share of the 50 JDs ask for it?
- List the top 10 in `output/opportunities.md`, each with the reason it scored that way and a sample deliverable

Examples of work an agent can probably do:

- Competitive positioning and battlecards (PMM)
- Messaging and narrative audit of the website (PMM)
- SEO and content gap audit (Digital)
- Paid search competitor teardown (Digital)
- ICP and account tiering model (RevOps)
- Funnel and conversion benchmark brief (RevOps)
- Customer health score framework and churn signal map from public reviews (CS)
- Onboarding journey audit (CS)

### Phase 6: Execute Proof of Work

- For each target company, build 1 deliverable that matches a requirement in its own JD
- Use only public data, and cite every source
- Save to `output/proof/{company}.md`, and use the `sandsdx-design` skill when a polished version is needed

### Phase 7: Pitch

- Find the VP or C level buyer for the role (CMO, CRO, VP Marketing, VP CS, VP RevOps) using Clay
- Draft outreach with the `sandsdx-voice` skill
- Quote the line from the JD, link the finished deliverable, and give one next step
- Save as drafts only and never send without approval
- Track it all in `output/pitch_tracker.csv` with company, buyer, title, LinkedIn URL, requirement, deliverable link, status

## Output Rules

- Bullets the user can copy and paste
- Keep it short with no filler
- No dashes in prose
- Put commas only where they're needed
- Back every claim with data and a source link
- Give a point of view and the reasoning behind it, not only a summary
- Mark estimates as estimates

## Guardrails

- Use only public information about target companies
- Never send emails, messages, or connection requests without explicit approval
- Don't contact more than 1 person per company until the user approves
- Don't make up company data, quotes, or metrics
- Respect the terms of service of each site, and use APIs and connectors before scraping

## Definition of Done

- 50 companies in `data/companies.csv`, each with a source
- 50 or more JDs saved in `data/jds/`
- `output/patterns.md` with counts and citations
- `output/opportunities.md` with the top 10 scored opportunities
- At least 5 proof of work deliverables in `output/proof/`
- At least 5 pitch drafts with matching rows in `output/pitch_tracker.csv`
