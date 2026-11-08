# Fireworks AI: Proof of Work

- Prepared: 2026-11-08 by SandsDX
- Plays: 2 (Competitive battlecard kit) and a short Play 1 (Positioning read)
- Inputs: public data only. Tools used: Clay (company search for Fireworks, Together AI, Baseten, Groq), WebSearch (one run per query on 2026-11-08, US). No internal Fireworks data
- Every price below is a public list price or a third party tracker figure. Fireworks negotiates enterprise terms, so treat all of it as list, not street

## 1. What this answers

**Head of Product Marketing** ([JD](https://jobs.ashbyhq.com/fireworks/d5063bc9-d2ac-4ee4-9e0c-23ea74ad83b2), posted 2026-08-06)
- "You own the competitive program: battlecards, win/loss analysis, deal support for top opportunities, and the systematic feedback loop into Product." → Sections 4 and 5
- "Fluency in competitive analysis and the ability to teach reps to position against incumbents and challengers" → objections and landmines per card
- "Success is measured by whether sales reps, prospects, analysts, and press all describe Fireworks in a consistent way." → Sections 2 and 6
- "Win rates against priority competitors trend up quarter over quarter across all three priority segments" → segment notes per card

**Head of GTM Strategy & Ops, Global Partnerships** ([JD](https://jobs.ashbyhq.com/fireworks/637ac49a-7ff1-4791-8e59-598a991bcde5), posted 2026-10-19)
- "Define requirements for partner dashboards, forecasting views and alerts with GTM Analytics and GTM Engineering, and push for automation of weekly reporting." → Section 5
- "Use AI and agentic tooling in everyday work, and help partnerships and sales teams do the same." → Section 5

**Head of GTM Strategy and Planning** ([JD](https://jobs.ashbyhq.com/fireworks/66663e61-2849-4aa1-ba89-3a51ccd31aef), posted 2026-10-12)
- "scenario models that show the tradeoffs between headcount, pipeline, compute supply, productivity, and revenue before decisions are made" → Section 5 feeds competitor GPU and token price moves into those models

---

## 2. Play 1: How Fireworks positions itself today

| Layer | Exact public wording | Source |
|---|---|---|
| Corporate (2026) | "Fireworks is the platform for specialized intelligence, enabling companies to build, train, and serve AI models tailored to their own data, workflows, and products." | All 3 JDs, About Us |
| Series D release | "Fireworks is the platform for specialized intelligence, enabling companies such as Doximity, Revolut, and Shopify to train and serve models tailored to their own data, workflows, and use cases." | [Firmus newsroom](https://firmus.co/newsroom/fireworks-partners-with-firmus-ai-cloud-to-scale-specialized-intelligence), [Fortune press release feed](https://fortune.com/press-releases/fireworks-raises-1-5b-series-d-reaches-1b-arr-2026-07-16/) |
| CEO line | "General intelligence will be abundant. Specialized intelligence will be the moat." | Attributed by [The Next Web](https://thenextweb.com/news/fireworks-1-5-billion-series-d-specialized-intelligence). Not matched to the release text; verify before reuse |
| Proof stat | More than 95% of tokens served come from models specialized on customer data (company reported) | [Fireworks blog](https://fireworks.ai/blog/series-d-announcement) |
| LinkedIn (still live per Clay, 2026-11-08) | "Fireworks is the fastest way to build, tune, and scale AI on open models." and "delivering 15× faster speed, 4× lower latency, and 4× more concurrency than closed models" | Clay company record (LinkedIn description) |
| Product blog | Fastest provider across top open models among GPU based providers, citing Artificial Analysis (self reported) | [Fireworks blog](https://fireworks.ai/blog/blazing-fast-inference-on-top-oss-models) |
| Investor framing | "platform for specialized intelligence and low-cost token production" | [Menlo Ventures](https://menlovc.com/?p=21843) |

- **Scale (company reported)**: $1B+ annualized revenue run rate, 40T+ tokens a day, $1.505B Series D at $17.5B led by Atreides, Index and TCV on 2026-07-16 ([Fortune feed](https://fortune.com/press-releases/fireworks-raises-1-5b-series-d-reaches-1b-arr-2026-07-16/), [Orrick](https://orrick.com/en/News/2026/07/Fireworks-AI-Closes-Over-1-5-Billion-in-Series-D-Funding))
- **Headcount**: 448 (Clay). Together AI 445, Baseten 487, Groq 313 (Clay). Same size class, so this is a narrative fight more than a scale fight
- **Read**: three stories are live at once. Corporate says specialized intelligence. LinkedIn and the product blog say fastest. The investor says low cost tokens. Buyers who land on third party comparison pages only see the last two, and on speed and price Groq, Together and smaller hosts can always find a model where they win
- **Point of view**: "specialized intelligence" is the only claim no competitor in this set can copy quickly, because the 95% stat is behavior data. Every battlecard below steers the deal from tokens per dollar toward cost and quality of a tuned model in production

---

## 3. Competitor selection: who buyers compare Fireworks to

| Competitor | Head to head evidence (2026-11-08) | Why it makes the top 3 |
|---|---|---|
| **Together AI** | 19 "Fireworks vs Together" result pages in one search incl. [CostBench](https://www.costbench.com/compare/fireworks-ai-vs-together-ai/), [metavert](https://metavert.io/together-ai-vs-fireworks-ai), [Northflank](https://www.plushcap.com/content/northflank/blog/northflank-fireworks-ai-vs-together-ai-which-platform-fits-your-stack); #2 on [DigitalOcean's Fireworks alternatives list](https://www.digitalocean.com/resources/articles/fireworks-ai-alternatives) | Same buyer, same open models, overlapping logos (Cursor is named by both) |
| **Baseten** | Baseten runs its own [Baseten vs Fireworks AI page](https://www.baseten.co/compare/fireworks-ai); also [Morph](https://www.morphllm.com/comparisons/fireworks-vs-baseten), [CB Insights](https://www.cbinsights.com/compare/baseten-vs-fireworks-ai) | The only competitor actively attacking Fireworks by name on its own domain |
| **Groq** | [Morph](https://www.morphllm.com/comparisons/fireworks-vs-groq), [pricepertoken](https://pricepertoken.com/endpoints/compare/fireworks-vs-groq), [CostBench](https://www.costbench.com/compare/groq-vs-fireworks-ai/), [pkgpulse three way](https://www.pkgpulse.com/guides/groq-vs-together-ai-vs-fireworks-ai-llm-inference-apis-2026) | Owns the "fastest" word Fireworks still uses on LinkedIn |

- **Watch list, not carded**: DeepInfra, Modal, RunPod (DigitalOcean list), Featherless (runs a [Fireworks alternative page](https://featherless.ai/competitor/fireworks-ai-alternative) built on model retirement), self hosted vLLM ([Toolradar](https://toolradar.com/tools/fireworks-ai/alternatives))
- **Not found**: no "Fireworks vs X" page on fireworks.ai in search results. Competitors and aggregators define the comparison today

---

## 4. Play 2: Battlecards

### 4a. Together AI

**Their positioning**
- "Together AI is the AI Native Cloud, purpose-built for AI engineers and researchers with a full suite of tooling across inference, model shaping, and pre-training" (Clay, LinkedIn description)
- Sells the full stack: serverless inference, dedicated endpoints, on demand GPU clusters, "massive-scale AI factories" (Clay)
- $800M Series C at $8.3B post money, led by Aramco Ventures, 2026-07-01 ([Las Vegas Sun / Business Wire](https://lasvegassun.com/news/2026/jul/01/together-ai-raises-800-million-at-83-billion-valua/))
- Logos claimed: Cursor, Decagon, ElevenLabs, AI21, Hedra, Cartesia, Salesforce, Zoom, Zomato (Clay)

**Where Fireworks wins**
- Specialization proof: 95% of tokens on customized models (company reported, [blog](https://fireworks.ai/blog/series-d-announcement)). Together sells "model shaping" but publishes no comparable stat (none found)
- Long generation throughput: a Jan 2026 benchmark cited by [metavert](https://metavert.io/together-ai-vs-fireworks-ai) puts Fireworks at 165.7 tok/s, about double Together's sustained rate (third party, single benchmark)
- Catalog breadth: 200 models on Fireworks vs 73 on Together per a [pricing aggregator](https://www.morphllm.com/comparisons/fireworks-vs-together) (count changes weekly)
- Enterprise channel: Fireworks is GA on Microsoft Foundry since 2026-06-02 with 26 open models, billed through Azure ([Azure](https://azure.microsoft.com/en-au/products/ai-foundry/models/fireworks-ai), [Unite.AI](https://unite.ai/microsoft-opens-26-open-models-to-startups-through-fireworks-ai-on-foundry/)). Together has no equal listing in results found

**Where Fireworks loses or is at risk**
- Raw GPU hours: Fireworks H100 on demand $8.00/hr ([pricing](https://www.fireworks.ai/pricing)) vs Together dedicated H100 $5.49/hr and reserved clusters from $3.59/hr ([UsagePricing](https://usagepricing.com/blueprint/together-ai)). Fireworks lists about 46% higher per H100 hour (estimate from list prices)
- Training and research story: Together pitches pre training and GPU clusters, which pulls in research heavy AI natives
- Shared logo: Cursor appears on both customer lists, so "we power Cursor" is not a differentiator on its own

**Landmines to set**
- "Ask them what share of tokens on their platform run on models tuned to customer data, and for one production example." (Fireworks: 95%)
- "Ask for throughput on your longest generation workload, not a short prompt benchmark."
- "Ask whether you can buy it through your existing Azure commit." (Foundry GA)

**Top 3 objections**

| Objection | Response | Proof |
|---|---|---|
| "Together's GPUs are cheaper per hour." | Compare cost per useful token at your latency target, not cost per GPU hour. Fireworks sells tuned throughput; a cheaper idle GPU still bills | Long generation benchmark ([metavert](https://metavert.io/together-ai-vs-fireworks-ai)); dedicated GPUs on these platforms bill while idle ([CloudZero on Together](https://cloudzero.com/blog/together-ai-pricing)) |
| "Together does inference and training in one place too." | Fireworks runs managed fine tuning, RFT and a Training API next to serving, so the tuned model ships on the same stack it was trained on | [Fine tuning and eval](https://fireworks.ai/solutions/fine-tuning-evaluation), [RFT docs](https://docs.fireworks.ai/fine-tuning/how-rft-works.md) |
| "Cursor uses Together." | Cursor also uses Fireworks for Fast Apply at about 1,000 tokens/sec via speculative decoding. Serious AI natives run more than one vendor; win the latency critical path | [Case study listing](https://www.casestudies.com/company/fireworks-ai) |

**Pricing notes (sourced)**
- Together H100: $5.49/hr dedicated on demand, from $3.59/hr reserved ([UsagePricing](https://usagepricing.com/blueprint/together-ai)). Other trackers show $2.99 to $6.49 ([CloudZero](https://cloudzero.com/blog/together-ai-pricing), [eesel](https://www.eesel.ai/pt/blog/precos-together-ai)); figures conflict
- Together fine tuning: about $3 per 1M training tokens (third party, [Morph](https://www.morphllm.com/together-ai-pricing))
- Batch on both: about 50% of serverless ([Morph on Fireworks](https://www.morphllm.com/fireworks-ai-pricing))

### 4b. Baseten

**Their positioning**
- "Inference is everything." and "out-of-the-box global availability with 99.99% of uptime" (Clay, LinkedIn description)
- "the platform for mission-critical inference" ([Business Wire, 2025](https://www.businesswire.com/news/home/20250905680113/en))
- Own comparison page says Baseten wins "when performance, reliability, and transparency matter" and that Fireworks does not publish uptime for dedicated deployments ([baseten.co](https://www.baseten.co/compare/fireworks-ai))
- $1.5B Series F at about $13B, 2026-06-22 ([Converge Digest](https://convergedigest.com/baseten-raises-1-5-billion-to-expand-ai-inference-infrastructure/?amp=1)). Reported talks at about $30B (Bloomberg via [FourWeekMBA](https://fourweekmba.com/ai-baseten-set-for-a-30-billion-valuation-2-3x-its-june-mark/), unconfirmed)
- Claimed scale: 1B+ inference calls a day across 87 clusters and 18 clouds; Abridge and OpenEvidence as anchor healthcare logos ([Baseten about](https://www.baseten.co/about/), [Pulse 2.0](https://pulse2.com/baseten-300-million-5-billion-valuation/))

**Where Fireworks wins**
- Serverless first: per token APIs across 200+ models with no GPU to size ([Morph](https://www.morphllm.com/comparisons/fireworks-vs-baseten)). Baseten's center of gravity is dedicated deployments billed per GPU minute per replica ([DigitalOcean](https://www.digitalocean.com/resources/articles/baseten-alternatives))
- Disclosed traction: $1B+ run rate and 40T+ tokens a day (company reported). One analysis says Fireworks has "the best combination of disclosed revenue, production traffic, custom-model usage, customers, and technical breadth" ([New Market Pitch](https://newmarketpitch.com/blogs/news/ai-infrastructure-inference-startup))
- Tuning loop: managed fine tuning plus RFT on the same platform that serves. Baseten Training is newer (closed beta in 2025, [Baseten](https://www.baseten.co/blog/introducing-model-apis-and-training/))

**Where Fireworks loses or is at risk**
- Reliability narrative: Fireworks docs say multi tenant serverless has no latency or availability SLAs ([docs](https://docs.fireworks.ai/faq-new/deployment-infrastructure/is-latency-guaranteed-for-serverless-models)), and on demand is "subject to capacity constraints" ([docs](https://docs.fireworks.ai/guides/inference-introduction)). Baseten leads with 99.99%
- Regulated buyers: Baseten's healthcare logos and VPC story ([Sacra](https://sacra.com/chat/h/9e693601-2de8-4507-8bb1-8c27a8d3bf96/)) aim at the Enterprise segment the PMM JD names
- Baseten owns the comparison SERP on its own domain; Fireworks has no reply page

**Landmines to set**
- "Ask whether 99.99% is a contractual SLA with service credits, or a marketing number, and which product it covers." ([Lyceum](https://lyceum.technology/magazine/fireworks-vs-baseten-choosing-an-inference-deployment-platform/): dedicated capacity is not itself an uptime guarantee)
- "Ask what you pay per replica at 3am when traffic is zero and scale to zero is off."
- "Ask to see the tuned model training and serving on one bill."

**Top 3 objections**

| Objection | Response | Proof |
|---|---|---|
| "Baseten guarantees 99.99%. Fireworks has no SLA." | Serverless is the dev tier. Production runs on dedicated or reserved capacity with contract terms. Put the SLA in the order form and compare credits line by line | [Fireworks docs](https://docs.fireworks.ai/faq-new/deployment-infrastructure/is-latency-guaranteed-for-serverless-models); needs a published enterprise SLA page (gap, Section 6) |
| "Baseten has dedicated GPUs from $0.63/hr." | That entry rate is a small GPU. Compare on the GPU your model needs and on tokens per second per dollar after optimization | [Morph](https://www.morphllm.com/comparisons/fireworks-vs-baseten) |
| "Baseten is more transparent." | Fireworks publishes per minute GPU rates, regional premiums and per model token prices on one page | [Pricing](https://www.fireworks.ai/pricing) |

**Pricing notes (sourced)**
- Baseten dedicated GPUs from $0.63/hr, 10+ clouds, scale to zero ([Morph](https://www.morphllm.com/comparisons/fireworks-vs-baseten))
- Billed per GPU minute per replica, which sets a cost floor for high availability ([DigitalOcean](https://www.digitalocean.com/resources/articles/baseten-alternatives))
- Model APIs per token on a curated set ([Baseten](https://www.baseten.co/blog/introducing-model-apis-and-training/)); per model rates not pulled

### 4c. Groq

**Their positioning**
- "Groq was built from the silicon up to deliver the world's fastest inference at scale" on its own LPU chip (Clay, LinkedIn description)
- Nvidia took a non exclusive license to Groq IP, reported at about $20B, Dec 2025. GroqCloud continues as an independent company ([Constellation Research](https://www.constellationr.com/insights/news/nvidias-groq-deal-acquisition-acquihire-or-creative-licensing-deal), [Business Standard](https://www.business-standard.com/world-news/nvidia-biggest-deal-groq-assets-ai-inference-chips-acquisition-cloud-125122500207_1.html))
- Now a neocloud: $650M raise in mid 2026, targeting 200 MW by end of 2027 ([PYMNTS](https://www.pymnts.com/news/investment-tracker/2026/groq-seeks-650-million-amid-shift-to-ai-inference-neocloud-business/), [AI Weekly](https://aiweekly.co/node/3410))

**Where Fireworks wins**
- Breadth: 204 models on Fireworks vs 16 on Groq ([CostBench](https://www.costbench.com/compare/groq-vs-fireworks-ai/), aggregator count)
- Customization: Groq is pitched for fixed single model workloads; Fireworks for fine tuning, varied models and enterprise deployment ([Morph](https://www.morphllm.com/comparisons/fireworks-vs-groq))
- Vendor continuity: founder and core engineers moved to Nvidia, a new CEO runs the remaining company, and regulators are reviewing the deal structure ([GovConWire](https://www.govconwire.com/?p=340592), [Constellation](https://www.constellationr.com/blog-news/insights/nvidias-groq-deal-acquisition-acquihire-or-creative-licensing-deal)). Fair to raise as a question, not an attack

**Where Fireworks loses or is at risk**
- Time to first token: one comparison puts Groq at 10 to 20ms vs Fireworks 40 to 80ms on a 7B model ([Morph](https://www.morphllm.com/comparisons/fireworks-vs-groq)). Third party, but it is the number buyers see
- Headline price on shared models: across 12 shared models Groq was cheaper on 8, Fireworks on 3 ([pricepertoken](https://pricepertoken.com/endpoints/compare/fireworks-vs-groq)). Llama 70B: Fireworks $0.90/1M vs Groq $0.59 in / $0.79 out (third party)
- Fireworks' own LinkedIn says "fastest". That fight is against a chip company. Fireworks should not pick it

**Landmines to set**
- "Ask whether they can serve your fine tuned weights, and at what context length."
- "Ask which models you can run today and how fast new open models arrive."
- "Ask what changed in their roadmap and support since the Nvidia license."

**Top 3 objections**

| Objection | Response | Proof |
|---|---|---|
| "Groq is faster." | On a stock small model at first token, often yes. On your tuned model at production context, test it. Specialized beats generic for quality per dollar | 95% specialized tokens ([blog](https://fireworks.ai/blog/series-d-announcement)); Notion cut latency from 2s to 350ms with smaller tuned models ([case study](https://www.casestudies.com/company/fireworks-ai/case-study/how-notion-cuts-latency-4x-and-scales-enterprise-ai-workflows-with-fireworks-ai)) |
| "Groq is cheaper per token." | On 8 of 12 shared models, list price says yes. A tuned smaller model on Fireworks can replace a larger generic one, which moves the bill more than a few cents per million | [pricepertoken](https://pricepertoken.com/endpoints/compare/fireworks-vs-groq); Notion example above |
| "Nvidia backs Groq now." | Nvidia licensed the IP and is also a Fireworks investor (JD About Us). The question is who runs your workload for three years | [Constellation](https://www.constellationr.com/insights/news/nvidias-groq-deal-acquisition-acquihire-or-creative-licensing-deal) |

**Pricing notes (sourced, third party)**
- gpt-oss-120b $0.15 in / $0.60 out; Llama 3.3 70B $0.59 / $0.79; Kimi K2 $1.00 / $3.00 per 1M ([Morph](https://www.morphllm.com/groq-pricing), [eesel](https://eesel.ai/blog/groq-pricing))
- 50% batch and cached token discounts on the Developer plan ([Morph](https://www.morphllm.com/groq-pricing))

### 4d. Fireworks pricing context reps must know

- On demand GPUs: H100 $8.00/hr, B200 $13.00, GB300 $20.00; region restricted at 1.5x ([pricing](https://www.fireworks.ai/pricing))
- H100 rose 14% and B200 30% effective 2026-09-01 ([UsagePricing](https://www.usagepricing.com/blueprint/activity/fireworks-ai-2026-08-12-gpu-price-increase))
- 2026-10-22: nine models left the serverless price card, the $1 signup credit was dropped and Fire Pass closed to new subscribers ([UsagePricing](https://www.usagepricing.com/blueprint/activity/fireworks-ai-2026-10-22-nine-serverless-models-dropped), [signup credit](https://www.usagepricing.com/blueprint/activity/fireworks-ai-2026-10-22-signup-credit-dropped), [Fire Pass](https://www.usagepricing.com/blueprint/activity/fireworks-ai-2026-10-22-fire-pass-closed))
- Featherless already markets against this: "The Fireworks AI alternative that doesn't retire your model" ([Featherless](https://featherless.ai/competitor/fireworks-ai-alternative))
- **Point of view**: Fireworks is raising GPU prices and trimming the free tier while competitors sell cheaper hours. That is the right move for a specialization story and the wrong move for a "fastest and cheapest" story. The cards above only work if the narrative is the first one

---

## 5. Spec: weekly competitor monitoring agent

**Goal**: every Monday, a diff of what Together AI, Baseten, Groq and the watch list changed last week, and which battlecard line it breaks

| Source watched | Signal | How |
|---|---|---|
| Competitor pricing pages plus UsagePricing and PricingSaaS trackers | GPU $/hr, per model token price, batch and cache discounts, free tier changes | Weekly fetch, diff against last snapshot |
| Model catalogs and changelogs | New open model day one availability, model retirements | Count models per vendor; flag who served a new release first |
| Competitor compare and alternatives pages (baseten.co/compare, featherless.ai) | New pages naming Fireworks, changed claims | Search for "Fireworks" on competitor domains |
| Artificial Analysis and third party benchmarks | Speed, TTFT, price per model per provider | Pull leaderboard rows for the top 10 Fireworks models |
| Funding, M&A, exec moves (press, Clay) | Rounds, valuations, acquisitions, regulatory news | Clay company records plus news search |
| Cloud marketplaces (Azure Foundry, AWS, GCP) | New listings or co sell programs | Listing search by vendor |
| Job posts (Ashby, Greenhouse, LinkedIn) | New GTM or field teams by region or segment | Count new roles by family and city |
| Reddit, Hacker News, G2, X | Outage complaints, switching stories, price complaints | Keyword search per vendor |
| Search and AI answers | Who ranks and gets cited for "Fireworks vs X" and "best inference provider" | 20 prompts weekly; named and cited share |

**Output**
- One page Monday digest: top 5 changes ranked by deal impact, each with source link, date and the battlecard row to update
- Redlined battlecards: proposed edits as tracked changes for PMM approval
- Alert within 24 hours for price cuts over 10%, a new "vs Fireworks" page, or a model retirement on Fireworks that a competitor markets against
- CSV log for win/loss tagging and for the planning team's compute supply and price scenarios

**JD lines it maps to**
- PMM: "You own the competitive program: battlecards, win/loss analysis, deal support for top opportunities, and the systematic feedback loop into Product."
- Partnerships: "Define requirements for partner dashboards, forecasting views and alerts with GTM Analytics and GTM Engineering, and push for automation of weekly reporting." (marketplace signals)
- Partnerships: "Use AI and agentic tooling in everyday work, and help partnerships and sales teams do the same."
- Planning: "scenario models that show the tradeoffs between headcount, pipeline, compute supply, productivity, and revenue before decisions are made" (competitor GPU and token prices as inputs)

**Effort**: about 4 hours to stand up the first run, then about 30 minutes a week of human review (estimate)

---

## 6. Positioning gaps

- **Three stories in market**: specialized intelligence (corporate), fastest (LinkedIn and product blog), low cost tokens (investor). The PMM JD measures success by consistent description. Update the LinkedIn description first; it is the text Clay and other data vendors copy into every buyer tool
- **No owned comparison pages**: Baseten publishes "Baseten vs Fireworks AI" and Featherless publishes a Fireworks alternative page. No fireworks.ai comparison page was found. Ship honest "Fireworks vs Together / Baseten / Groq" pages framed on specialization, not speed
- **Reliability is undefended**: docs state serverless has no latency or availability SLA. Baseten leads with 99.99%. Publish an enterprise reliability page with dedicated and reserved SLA terms
- **Model retirement needs a policy message**: nine serverless models left the card on 2026-10-22 and a competitor already markets on it. Publish a model lifecycle policy (notice period, migration path to tuned or dedicated) and turn churn into "we move you to the next best model"
- **Segment proof is thin outside AI natives**: the JD names AI-Native, Digital-Native and Enterprise. Public case detail found covers Notion and Cursor. Uber, Shopify, Revolut and Doximity appear as logos without public case detail. Foundry GA is the enterprise wedge; pair it with one enterprise reference story

---

## 7. Hook for outreach (3 bullets)

- Your PMM JD asks for battlecards and reps who can position against challengers. Three cards are inside (Together AI, Baseten, Groq) with landmines, objections and sourced list prices
- Baseten already runs a "Baseten vs Fireworks AI" page that leads on 99.99% uptime, and your docs say serverless has no SLA. Fireworks has no reply page. That is the first deal you lose this quarter
- Your partnerships and planning JDs ask for automated weekly reporting and compute price scenarios. The monitoring agent spec covers both and can run every Monday starting next week

---

## Data notes

- **Clay**: company search on 4 domains returned descriptions, headcount and revenue bands. Clay's Fireworks funding band ($50M to $100M) is stale and not used
- **WebSearch only**: direct page fetches were blocked, so quotes come from search snippets of the named URLs. Re-check exact wording on live pages before external use
- **Conflicting third party data**: token prices, GPU rates and latency figures disagree across aggregators (examples noted inline). Fireworks list prices come from its pricing page; competitor prices are mostly trackers
- **Not sourced**: win rates, deal data, G2 review counts (PeerSpot shows no ratings for either Fireworks or Together), Reddit threads naming Fireworks (none returned), Ahrefs and Semrush (not tried for this play)
- **Unverified and not used**: a [DeployBase claim](https://deploybase.ai/articles/together-ai-vs-fireworks-pricing-speed-and-benchmark) that Together is 2.25x cheaper; reported Fireworks talks at $30B to $40B
