# OpenRouter: Proof of Work

- Prepared: 2026-11-08 by SandsDX
- Plays: 6 (SEO and AI search visibility audit) and 8 (GTM AI agent prototype)
- Inputs: public data only. Tools used: Clay (company search, Semrush traffic enrichment), WebSearch. Ahrefs and the Semrush MCP were tried and failed (see Data notes)

## 1. What this answers

**Director, Growth Marketing** ([JD](https://jobs.ashbyhq.com/openrouter/9c1cb711-cd17-4d07-9be5-f122c0a865b9), posted 2026-07-24)
- "Own the AEO/SEO roadmap for openrouter.ai: classic organic search plus answer-engine visibility" → Play 6
- "You've owned or directed SEO for a technical product, and you have a working point of view on AEO: what changes when the search result is a ChatGPT answer." → Play 6, AEO point of view
- "Support enterprise demand gen as an execution and thought partner: MQL/MQA generation programs" → Play 8, account research agent

**Director, Customer Success** ([JD](https://jobs.ashbyhq.com/openrouter/c0ae7a38-cd46-4bc8-b0d2-3b38cac5a424), posted 2026-10-23)
- "Develop AI-powered workflows, customer intelligence, and lifecycle programs that proactively identify risks, uncover growth opportunities, and deliver personalized engagement at scale." → Play 8
- "Define and execute a Customer Success strategy that scales through intelligent systems, automation, and high-impact customer engagement rather than proportional headcount growth." → Play 8 roadmap
- Nice to have: "Experience building AI agents, automated customer lifecycle programs, or intelligent customer engagement workflows." → Play 8

---

## 2. Play 6: SEO and AI search visibility audit

### 2a. Competitor set (verified)

- **Portkey** (portkey.ai): AI gateway, guardrails, governance. Now "A Palo Alto Networks Company" (Clay); acquisition reported closed 2026 ([intelligencecommunitynews](https://intelligencecommunitynews.com/palo-alto-acquires-portkey/))
- **LiteLLM** (litellm.ai): open source gateway, "55k+ GitHub stars", YC backed (Clay company description)
- **Together AI** (together.ai): inference cloud, 445 employees, $250M+ raised (Clay)
- Dropped **Martian**: Clay now describes it as a research team focused on "understanding machine intelligence", not a router. Its site traffic is 6,115 (Clay/Semrush), so it is not a search competitor
- Also showing up in category results: Vercel AI Gateway, Cloudflare AI Gateway, Bifrost by Maxim AI, LLM Gateway (llmgateway.io), Requesty ([DigitalOcean list](https://www.digitalocean.com/resources/articles/openrouter-alternatives), [Braintrust list](https://www.braintrust.dev/articles/openrouter-alternatives-2026))

### 2b. Organic baseline

| Domain | Est. monthly site traffic (Semrush via Clay enrichment, pulled 2026-11-08) | Other public data |
|---|---|---|
| openrouter.ai | 36,097,415 | Semrush public page: 7.11M visits Nov 2025 ([Semrush](https://cw.semrush.com/website/openrouter.ai/overview)). Semrush competitor page: 19.38M visits, Authority Score 51, undated ([Semrush](https://www.semrush.com/website/chat.openai.com/competitors/)) |
| together.ai | 1,204,023 | |
| litellm.ai | 498,596 | Docs traffic on other hosts may not be counted |
| portkey.ai | 106,949 | |
| withmartian.com | 6,115 | Dropped from set |

- **Read**: OpenRouter has about 30x Together AI's traffic and about 340x Portkey's (Clay/Semrush estimates). Most of that is product use, model pages and brand demand, not category search. Clay does not split organic from direct, so treat this as total traffic
- **Not sourced**: organic keyword counts, top pages and Domain Rating. Ahrefs returned "Insufficient plan" and the Semrush MCP did not expose its report tools. The third party traffic figures also conflict: Similarweb via aipure about 8M, Toolmage 16.8M, Indexator 17.9M ([aipure](https://aipure.ai/products/openrouter), [Toolmage](https://www.toolmage.com/vi/tool/openrouter/))
- **Point of view**: the brand is huge but category search belongs to someone else. Every gap below is a non branded query where Portkey, LiteLLM or Bifrost content ranks and openrouter.ai does not appear

### 2c. Content gaps (SERP proxy)

Method: one WebSearch per query on 2026-11-08, noting which domains appeared in the returned sources. This tool has no search volume data, so it is a proxy for gaps, not a keyword gap report.

| # | Query / topic | Who shows up | openrouter.ai in sources? |
|---|---|---|---|
| 1 | what is an LLM gateway | [portkey.ai blog](https://portkey.ai/blog/what-is-an-llm-gateway), Arize, TrueFoundry, Maxim, Langfuse | No |
| 2 | how to route between OpenAI and Anthropic (fallback) | [Portkey docs on GitHub](https://github.com/Portkey-AI/docs/blob/v2/product/ai-gateway-streamline-llm-integrations/fallbacks.md), Helicone, [LangSmith](https://docs.langchain.com/langsmith/llm-gateway-fallbacks) | No, even though [openrouter.ai/docs/guides/routing/model-fallbacks](https://openrouter.ai/docs/guides/routing/model-fallbacks) exists |
| 3 | LLM fallback when OpenAI API is down | Vellum, Maxim, a [dev.to post using LiteLLM fallbacks](https://dev.to/jayrai/how-i-added-llm-fallback-to-my-openai-app-in-10-minutes-3d35) | No |
| 4 | handle 429 rate limits, load balance keys | [Portkey docs](https://docs.portkey.ai/docs/cookbooks/tackling-rate-limiting), Requesty, Maxim | No (only a third party [Smithery skill](https://smithery.ai/skills/jeremylongshore/openrouter-load-balancing)) |
| 5 | track LLM spend per user/team, budget limits | [portkey.ai blog](https://portkey.ai/blog/budget-limits-and-alerts-in-llm-apps), llmgateway.io, Maxim, agentgateway | No |
| 6 | LLM semantic caching | [Portkey blog](https://blog.portkey.ai/blog/reducing-llm-costs-and-latency-semantic-cache), Percona, Maxim | No |
| 7 | LLM guardrails / PII redaction gateway | [Portkey docs](https://portkey.ai/docs/aigw/product/guardrails/pii-redaction.md), Requesty, TrueFoundry, Maxim | No |
| 8 | zero data retention LLM API | [llmgateway.io](https://llmgateway.io/enterprise/zero-data-retention), Eden AI, Prem AI | No, even though the [enterprise page](https://openrouter.ai/enterprise) offers ZDR enforcement |
| 9 | best AI gateway for enterprise cost control and governance | Maxim/Bifrost (many pages), Kong, Portkey, LiteLLM, [CloudNuro buyer's guide](https://www.cloudnuro.ai/blog/ai-gateway-buyers-guide-2026-kong-vs-portkey-vs-litellm-vs-truefoundry) | Not named |
| 10 | LLM API pricing comparison per million tokens | [BenchLM](https://benchlm.ai/md/blog/posts/llm-pricing-2026.md), Fungies, [CostBench](https://www.costbench.com/software/llm-api-providers/) | No, though OpenRouter publishes live pricing for 400+ models |
| 11 | OpenRouter alternatives (brand defense) | 30+ third party pages: [DigitalOcean](https://www.digitalocean.com/resources/articles/openrouter-alternatives), [Braintrust](https://www.braintrust.dev/articles/openrouter-alternatives-2026), [llmgateway.io](https://llmgateway.io/blog/openrouter-alternatives), [Opper](https://opper.ai/blog/openrouter-alternatives) | No owned page |
| 12 | LiteLLM vs Portkey vs OpenRouter | Third party only. OpenRouter described as "basic routing" and best "for experimentation" ([itsourcecode](https://itsourcecode.com/web-dev/llm-router-portkey-vs-litellm-vs-openrouter/), [zenn](https://zenn.dev/agdexai/articles/llm-gateway-comparison-2026)) | No owned page |
| 13 | cheapest way to access Claude, GPT and Gemini with one key | Resellers and dev.to posts ([example](https://dev.to/xujfcn/cheapest-way-to-access-gpt-5-and-claude-api-in-2026-pricing-breakdown-1c23)) | No |
| 14 | Duplicate copies of OpenRouter docs | Mirror domains serve copies of OpenRouter pages: [api.ifq.ai](https://api.ifq.ai/blog/insights/model-routing/), [api3.shopot.ai](https://api3.shopot.ai/blog/insights/model-routing/), [just-ai.com](https://openrouter-gw-kz.just-ai.com/blog/insights/model-routing/), [sslip.io](https://2.26.113.50.sslip.io/enterprise) | Dilutes citations |

- **Pattern**: Portkey's own domain shows up in 5 of 6 governance and reliability queries (1, 4, 5, 6, 7). OpenRouter shows up in 0. These are enterprise jobs to be done, and they map to the 25% enterprise demand gen part of the growth role
- **Positioning risk**: third party comparisons frame OpenRouter as the tool for experimentation, with LiteLLM or Portkey for production. Portkey now has Palo Alto Networks behind its governance story

### 2d. AI search visibility: 10 buyer prompts

- **Proxy**: Ahrefs Brand Radar returned "Insufficient plan" on 2026-11-08. These are WebSearch results run once on 2026-11-08 as a stand in for ChatGPT/Perplexity answers. Answer engines pull from similar web sources, but this is not a measured citation share
- "Named" means OpenRouter appears in the answer. "Cited" means an openrouter.ai URL appears in the returned sources

| # | Prompt | Named? | Cited? | Who is cited instead |
|---|---|---|---|---|
| 1 | best LLM gateway 2026 | Yes, as the "managed" pick | No | dev.to (Bifrost team posts), [Inworld](https://inworld.ai/resources/best-llm-gateways), [Contabo](https://contabo.com/blog/best-llm-gateways/) |
| 2 | how to route between OpenAI and Anthropic API fallback | No | No | Portkey docs, LangSmith, Helicone |
| 3 | unified API for multiple LLM providers | Yes, via a Braintrust article | No | [Braintrust](https://www.braintrust.dev/articles/best-unified-llm-api-providers-2026), LiteLLM, PyPI packages |
| 4 | cheapest way to access Claude GPT and Gemini with one API key | Yes, "close to official rates (small markup)" | No | Resellers, dev.to |
| 5 | LLM fallback when OpenAI API is down best practice | No | No | Vellum, Maxim, LiteLLM example |
| 6 | LiteLLM vs Portkey vs OpenRouter | Yes, framed as basic routing | No | dev.to, itsourcecode, zenn |
| 7 | best AI gateway for enterprise LLM cost control and governance | No | No | Maxim/Bifrost, Kong, Portkey, LiteLLM |
| 8 | LLM API pricing comparison per million tokens 2026 | No | No | BenchLM, Fungies, CostBench |
| 9 | which LLM is best for coding agents usage rankings | Yes, as the source for real usage rankings | No (named, not linked) | Vellum, pricepertoken, LLM Reference |
| 10 | how to use open source models like DeepSeek and Qwen via API in production | Yes, next to Together and Fireworks | No | Alibaba Cloud, BytePlus, tkmxai |

- **Score (proxy)**: named in 6 of 10. Own URL cited in 0 of 10. The brand is known, but the domain is not the source
- **Best signal**: prompt 9. When the question is about real usage, OpenRouter is the authority. Its rankings and the [a16z State of AI 100T token study](https://www.a16z.com/state-of-ai) ([arXiv](https://arxiv.org/abs/2601.10088)) are data that no competitor has

### 2e. AEO point of view: 5 actions ranked by impact

My view: in an AI answer there is no position 1 to 10, just cited or not cited. The engine cites pages that answer the question directly, with numbers, on a stable URL. OpenRouter has the best data in the category and publishes it as product UI, not as answers. Fix that first.

1. **Turn usage data into citable answer pages** (highest impact). Publish monthly pages such as "Most used models for coding agents, by tokens" with a date, a table, method notes and a stable URL. Prompt 9 shows engines already treat OpenRouter as the usage authority. It is the one moat Portkey and LiteLLM cannot copy
2. **Rank the docs you already have for non branded jobs.** Fallbacks, provider routing, ZDR and BYOK are documented but do not surface for gap queries 2, 3, 4, 5 and 8. Add one guide page per job, titled with the buyer's words ("Fallback from OpenAI to Anthropic in 3 lines"), with code first and comparison second. These are the enterprise queries where Portkey ranks today
3. **Own the comparison and alternatives SERP.** Publish an honest "OpenRouter vs LiteLLM vs Portkey" page and an "OpenRouter alternatives" page that says when not to use OpenRouter. Engines quote fair comparisons. Today 30+ competitor pages define OpenRouter as "for experimentation"
4. **Put enterprise trust in Q&A form.** SSO/SCIM, ZDR per model group, BYOK allowances and data policies are on the [enterprise](https://openrouter.ai/enterprise) and [pricing](https://openrouter.ai/pricing) pages. Restate them as FAQ blocks that answer "is X safe for regulated data". This goes straight at the "basic routing" framing and the [TrueFoundry critique](https://www.truefoundry.com/de/blog/openrouter-reviews)
5. **Protect citations from mirrors and measure monthly.** Mirror domains republish the docs (gap 14). Keep canonicals and the existing [llms-full.txt](https://openrouter.ai/docs/llms-full.txt), file removals where the terms allow, and track these 10 prompts every month in Brand Radar or a similar tool so AEO gets a number like paid does

---

## 3. Play 8: GTM AI agent prototype

### 3a. ICP from public evidence

- **Scale**: "More than 10 million users and 250k+ apps process 200T+ tokens on the platform every month, nearly all of it starting in self-serve" (Growth JD)
- **Segments named**: "AI-native startups, enterprises, and strategic customers" (CS JD)
- **Visible app customers**: Framer has a public [app page](https://openrouter.ai/apps/framer) (search snippet: #6 daily rank, 520B tokens in 30 days). Replit has a [community guide in the docs](https://openrouter.ai/docs/guides/community/replit). A third party vendor blog lists Replit, Blackbox AI, Kilo Code, Framer and NIST (secondary, unverified)
- **Enterprise pull**: SSO/SCIM, ZDR enforcement and BYOK on the [enterprise page](https://openrouter.ai/enterprise). Series B investors include ServiceNow Ventures, MongoDB Ventures and Snowflake ([report](https://feedbagel.com/post/techcrunchcom-39))
- **Workloads**: agentic, multi step inference, with open weight models gaining share ([State of AI study](https://arxiv.org/abs/2601.10088))
- **ICP used for the agent run**:
  - AI native product or SaaS company shipping LLM features, 10 to 500 employees
  - Workloads that need 2+ model vendors or open weight models (cost tiers, fallback, compliance)
  - Trigger in the last 6 months: funding, agent launch, enterprise or regulated expansion
  - Disqualifier: self hosted only. Example: Longeye raised a $20M Series A in Oct 2026 but describes "secure, self-hosted AI" (Clay), so it was dropped
  - Fit types: **Buyer** (routes its own inference) or **Partner** (integration, supply or channel)

### 3b. Account research agent: run by hand on 10 accounts

- Steps: Clay firmographics, then WebSearch for the trigger and source, then a multi model pain hypothesis, then a first line
- Pain lines are **hypotheses** drawn from public product descriptions, not confirmed usage
- Revenue bands are Clay estimates

**1. Casap** (casap.ai) | Buyer
- Firmographics: New York, 69 employees, revenue est. $10M to $25M (Clay)
- Trigger: $56M Series B led by Base10, 2026-10-28. Expanding from disputes into collections and claims ([FinTech Futures](https://www.fintechfutures.com/venture-capital-funding/casap-bags-56m-series-b))
- Likely pain: more agent types per bank, each needing explainable and auditable decisions. Banks will want provider pinning and ZDR routing
- First line: "Moving from disputes into collections and claims means more agents per bank, and every bank will ask which model saw its data."

**2. Larridin** (larridin.com) | Buyer and partner
- Firmographics: San Francisco, 26 employees (Clay)
- Trigger: $30M Series A led by Pelion, 2026-11-02 ([SiliconANGLE](https://siliconangle.com/2026/11/02/vcs-bet-30m-on-larridins-ability-to-help-enterprises-demonstrate-ais-value-for-money/))
- Likely pain: sells "ROI on token spend" (Clay description), which needs normalized cost data across providers
- First line: "You measure ROI on token spend for G2000 buyers. Normalized cost and usage data across 400+ models could be the cleanest input you have."

**3. Finpilot** (finpilot.ai) | Buyer
- Firmographics: Seattle, 11 employees (Clay)
- Trigger: $10M Series A led by Lobby Capital, 2026-11-04, to expand agent capabilities ([GeekWire](https://www.geekwire.com/2026/finpilot-raises-10m-for-ai-agents-that-handle-the-grunt-work-for-institutional-investors/))
- Likely pain: research, reporting and diligence agents over long documents. Cheap models for extraction, frontier models for reasoning, and data controls for pension and endowment clients
- First line: "Pension and endowment clients will ask where their documents go. ZDR routing per model answers that before procurement asks."

**4. Otter.ai** (otter.ai) | Buyer
- Firmographics: Mountain View, 305 employees, revenue est. $75M to $200M (Clay); 35M+ users (company description)
- Trigger: $320M from General Catalyst's Customer Value Fund, 2026-10-20, for enterprise expansion ([The Next Web](https://thenextweb.com/news/otter-ai-320m-general-catalyst))
- Likely pain: summaries at very high volume make unit cost per meeting the margin lever. Enterprise push adds SSO and data retention questions
- First line: "Across a billion meetings, the cost of each summary drives gross margin. Routing each task to the cheapest model that passes is the fastest lever."

**5. Niteshift** (niteshift.dev) | Buyer
- Firmographics: New York, 8 employees (Clay)
- Trigger: $7M seed led by Greylock, 2026-06-10. Model agnostic cloud supporting Claude Code, Codex, OpenCode and Pi ([Dealroom](https://app.dealroom.co/news/note/niteshift-raises-7m-seed-to-give-coding-agents-a-model-agnostic-cloud)). Older trigger
- Likely pain: anti lock in is the pitch, so customers want any model without extra keys and invoices
- First line: "Your pitch is no model lock in. One key and one bill across every model makes that true for your customers on day one."

**6. Solidroad** (solidroad.com) | Buyer
- Firmographics: San Francisco and Dublin, 43 employees (Clay); customers include OURA, Chime, Crypto.com (Clay)
- Trigger: $25M Series A led by Hedosophia, 2026-04-16 ([The Next Web](https://thenextweb.com/news/solidroad-25-million-series-a-ai-customer-support-qa)). Older trigger
- Likely pain: scoring every support conversation is a high volume eval workload. Cheap models score, strong models judge edge cases
- First line: "Reviewing every conversation is an inference bill that grows with your customers' volume. Tiered routing keeps QA margin flat."

**7. Omnichat** (omnichat.ai) | Buyer
- Firmographics: Hong Kong; 5,000+ brands (company claim). Not found in Clay
- Trigger: $10M Series A led by Openspace Capital, 2026-10-27, to scale Omni AI Agents and expand globally ([press release](https://kyodonewsprwire.jp/release/202610278750))
- Likely pain: marketing, sales and service agents across Asian markets. Multilingual quality varies by model and region
- First line: "Scaling Omni AI Agents across markets means the best model for Thai support may not be the best one for Japanese sales."

**8. Daytona** (daytona.com) | Partner
- Firmographics: San Francisco, 78 employees (Clay)
- Trigger: $60M Series B at a $1B valuation led by FirstMark Growth, 2026-10-20 ([tech.eu](https://tech.eu/2026/10/20/daytona-hits-1b-valuation-with-60m-series-b-for-ai-agent-cloud//))
- Likely pain: agents run in Daytona sandboxes and every one of them calls a model. An integration makes the default path one key for any model
- First line: "Every agent in a Daytona sandbox calls a model. A native OpenRouter path removes the first setup step for your users."

**9. Trajectory** (trajectory.ai) | Partner (supply)
- Firmographics: San Francisco, 17 employees (Clay)
- Trigger: $45M Series A led by Sequoia at a $300M valuation, 2026-11-02. Post trains open source models for Harvey, Rogo and Decagon ([CityBiz](https://www.citybiz.co/article/928378/trajectory-pushes-ai-self-learning-with-45m-funding-led-by-sequoia))
- Likely pain: tuned open models need a serving and distribution path, plus baselines against frontier models
- First line: "Harvey and Rogo already run your post trained open models. A listing puts them in front of 250k+ apps that pick models by price and quality."

**10. Rein Security** | Partner (guardrails)
- Firmographics: New York and Tel Aviv, founded 2024 ([SecurityWeek](https://securityweek.com/rein-security-raises-25-million-to-guard-ai-agents-at-runtime)). Clay domain match failed
- Trigger: $25M Series A co-led by Glilot and Sienna, 2026-10-08
- Likely pain: runtime security for enterprise agents needs visibility into model traffic across providers. The gateway is the natural enforcement point
- First line: "Your runtime guardrails need to see every model call. The gateway is where that traffic already meets."

- **Next run**: add the buying committee per account with Clay contact search (CTO, Head of AI or Platform), then score fit 1 to 5. Not done here per the guardrail of 1 contact per company

### 3c. One page AI roadmap: 5 agents for Growth and CS

| # | Agent | What it does | Inputs | Output | JD line it answers |
|---|---|---|---|---|---|
| 1 | AEO monitor | Runs 50 category prompts weekly across ChatGPT, Perplexity and Google AI and logs named and cited share against Portkey, LiteLLM and Vercel | Prompt set, Brand Radar or answer engine APIs, competitor list | Weekly visibility scorecard plus the pages to fix next | Growth: "Own the AEO/SEO roadmap for openrouter.ai: classic organic search plus answer-engine visibility" |
| 2 | Usage to content engine | Turns rankings and token data into dated answer pages and model comparison tables every month | Rankings, model pricing, release notes | Draft pages for human review, refreshed on a schedule | Growth: "a working point of view on AEO: what changes when the search result is a ChatGPT answer" |
| 3 | Account research agent (this prototype) | Watches funding and launch news, filters to ICP, writes the brief and the first line | Clay, news search, signup domain matched to company | Daily list of scored accounts for enterprise sales and MQA programs | Growth: "Support enterprise demand gen as an execution and thought partner: MQL/MQA generation programs" |
| 4 | Consumption health agent | Flags accounts by token trend, model mix shift, error rates and spend versus credits; drafts the CSM note | Inference usage, billing, support tickets | Daily risk and expansion list with the reason and the suggested play | CS: "Use product telemetry, inference usage, customer feedback, and business signals to drive proactive engagement" |
| 5 | Self serve lifecycle agent | Personalized onboarding and expansion nudges for thousands of small accounts (first credit, second model, ZDR, BYOK) | Signup data, first calls, model choice | Triggered emails and in app tips, with holdout groups for incrementality | CS: "scales through intelligent systems, automation, and high-impact customer engagement rather than proportional headcount growth"; Growth: "first credit purchase, and expanding usage" |

---

## 4. Hook for outreach (3 bullets)

- Your growth JD asks for a working point of view on AEO. In a 10 prompt proxy test OpenRouter was named in 6 answers and cited by URL in 0. Portkey's own domain appeared in 5 of 6 governance and reliability queries
- OpenRouter has data no competitor has (real usage across 400+ models), but it lives in product UI, not in pages AI engines can cite. Five ranked fixes are inside
- Your CS JD asks for AI powered workflows that scale without proportional headcount. The account research agent already ran on 10 named accounts with October and November triggers, plus a 5 agent roadmap mapped to both JDs

---

## Data notes

- **Ahrefs**: Brand Radar citation tools and the Domain Rating list returned "Insufficient plan". No Ahrefs doc tool or Site Explorer tools were exposed. No Ahrefs data is used
- **Semrush MCP**: discovery tools responded, but `get_report_schema` and `execute_report` were not available, so no keyword, top page or Authority Score pulls. Traffic figures come from Semrush through Clay's Website Traffic enrichment
- **Gaps and AI visibility** come from one WebSearch run per query on 2026-11-08 (US). They are a proxy with no search volumes. Re-run in Ahrefs or Semrush before quoting externally
- **Unverified**: a [Multiples.vc](https://multiples.vc/private-comps/openrouter) listing claims Stripe acquired OpenRouter in Aug 2026. No other source confirms it, so it is not used
