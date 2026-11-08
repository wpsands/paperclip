# Agent Opportunities

Top 10 plays where SandsDX can take a requirement from a live JD, do the work now with an agent, and send it to the buyer as the hook.

## Method

- Started from 170 requirement themes across 53 JDs (`output/patterns.md`)
- Kept 69 themes that produce a tangible output and appear in 3 or more JDs
- Scored each 1 to 5 on five criteria (max 25)
  - **Agent doable now**: Claude plus Clay, Ahrefs, Semrush and web research can finish it without internal access
  - **Public inputs only**: built from the company's site, content, reviews, SEO data, competitors
  - **Buyer visible**: a VP sees the value in under 2 minutes
  - **Time**: 4 hours or less
  - **Frequency**: share of the family's JDs that ask for it (computed, not judged)
- Bundled overlapping themes into 10 plays
- All 69 scores: `output/opportunity_scores.csv`; scoring script: `scripts/score.py`
- The first four criteria are judgment calls; treat scores as a ranking, not a measurement

## POV

- **Lead with Play 8 (GTM AI agent prototype).** It scores lower on its own (19) but 21 of 42 companies (50%) ask for it across every role family. It is also the closest match to what SandsDX sells. Every other play is a way to prove the agent works
- **Use PMM plays for volume.** Plays 1, 2 and 4 score highest (22 to 23) and cover 13 companies with near zero internal data needs
- **Avoid internal data plays as hooks.** Funnel reporting (80% of Demand Gen JDs), board reporting and forecasting are frequent but need CRM access. Sell those after the hook lands

## The 10 plays

### 1. Positioning and messaging teardown
- **Score**: 23 (agent 5, public 5, visible 5, time 4, frequency 4)
- **JD asks**: "Own product positioning and messaging framework" and "Translate technical capabilities into buyer value stories" (69% of PMM JDs each)
- **Targets (13)**: CertifyOS, Clara, Ethena, Fireworks AI, GC AI, Horizon3.ai, Keyfactor, Morning Consult, Nooks, Overjet, Proof, ROLLER, Synthesia
- **Deliverable**: one page audit of homepage and top 3 product pages against 3 competitors, then a rewritten messaging house (category, value pillars, proof points per persona)
- **Inputs**: their site, competitor sites, G2 reviews, JD language
- **Hook**: "Your PMM JD asks for a messaging framework. Here is a draft built from your site, your reviews and your top 3 competitors."

### 2. Competitive battlecard kit
- **Score**: 22 (sales toolkit), 21 (competitive intel), 20 (market monitoring)
- **JD asks**: battlecards, one pagers, objection guides; competitive intelligence program; market monitoring system
- **Targets (13)**: CertifyOS, Ethena, Fireworks AI, GC AI, Horizon3.ai, Illumio, Keyfactor, Loopio, Morning Consult, Overjet, Proof, ROLLER, Synthesia
- **Deliverable**: battlecards for the top 3 competitors (why we win, landmines, objection handling, pricing notes) plus a weekly competitor monitoring agent
- **Inputs**: competitor sites, pricing pages, G2 and Reddit, changelogs, job posts
- **Hook**: the monitoring agent is the recurring service; the battlecards are the free sample

### 3. ABM target list and plays
- **Score**: 22 (agent 5, public 5, visible 5, time 3, frequency 4)
- **JD asks**: "Build and run tiered ABM programs for buying committees" (60% of Demand Gen JDs)
- **Targets (9)**: Augury, FurtherAI, GC AI, Haus, NexHealth, OpenRouter, Paddle, Simetrik, commercetools
- **Deliverable**: 25 tier 1 accounts from Clay matched to their ICP, the buying committee for each, and a 3 touch play per tier
- **Inputs**: Clay company and contact search, their customer logos, case studies
- **Hook**: hand the VP a list of named accounts they recognize; this lands in seconds

### 4. Category narrative memo
- **Score**: 22 (agent 5, public 5, visible 5, time 4, frequency 3)
- **JD asks**: "Define company and category narrative and point of view" (50% of PMM JDs)
- **Targets (8)**: Ethena, Fireworks AI, GC AI, Horizon3.ai, Loopio, Morning Consult, Rillet, Synthesia
- **Deliverable**: 2 page narrative (old way, shift, new way, proof) plus 3 LinkedIn posts for the founder in that voice
- **Hook**: founders read narrative memos; this routes to the CEO as well as the CMO

### 5. ICP and segment messaging
- **Score**: 20
- **JD asks**: "Define ICP, segmentation and segment specific messaging" (33% of Demand Gen JDs)
- **Targets (5)**: GC AI, Haus, Legora, NexHealth, Paddle
- **Deliverable**: ICP from their public customer logos enriched in Clay (size, industry, stack), 3 segments, one message per segment

### 6. SEO and AI search visibility audit
- **Score**: 20
- **JD asks**: "Own SEO, AEO and content led organic acquisition"
- **Targets (4)**: Cloudinary, OpenRouter, Simetrik, accessiBe
- **Deliverable**: keyword and content gap vs 3 competitors (Ahrefs or Semrush), plus how often ChatGPT and Perplexity cite them for their category prompts
- **Note**: OpenRouter's JD asks for "a working point of view on AEO and ChatGPT driven search"

### 7. Website conversion audit
- **Score**: 20
- **JD asks**: "Own website conversion and CRO testing"
- **Targets (4)**: FurtherAI, OpenRouter, Simetrik, accessiBe
- **Deliverable**: top 10 conversion fixes on homepage, pricing and demo pages, with 3 A/B test briefs

### 8. GTM AI agent prototype (lead play)
- **Score**: 19 (RevOps agents), 19 (AI roadmap), 18 (AI in demand gen)
- **JD asks**: "Build AI agents and automations for GTM workflows" (56% of RevOps JDs), "Apply AI and automation to demand gen workflows" (60% of Demand Gen JDs), plus AI workflow asks in PMM and CS
- **Targets (21)**: ArmorCode, Broccoli AI, CertifyOS, Clara, Cloudinary, DISQO, Deepgram, Fireworks AI, GC AI, Haus, Illumio, Klue, Kontakt.io, Morning Consult, NexHealth, OpenRouter, Overjet, Paddle, Simetrik, Synthesia, commercetools
- **Deliverable**: a working account research agent run on 10 of their target accounts (firmographics, trigger events, likely pain, first line), plus a 1 page AI roadmap for their GTM team
- **Sharpest fits**: Morning Consult ("Ship AI agents and automations across scoring, routing, enrichment, QA, and reporting"), Deepgram (Director, GTM Engineering), Kontakt.io ("build automations, AI agents, data workflows")
- **Hook**: "Your JD asks the hire to build GTM agents. Here is one running on your accounts."

### 9. Paid media competitor teardown
- **Score**: 18
- **JD asks**: "Plan and optimize paid and third party media campaigns" (40% of Demand Gen JDs)
- **Targets (6)**: FurtherAI, GC AI, Haus, OpenRouter, Simetrik, accessiBe
- **Deliverable**: competitor paid search and ad copy teardown (Semrush), 5 keyword gaps, 3 ad concepts

### 10. CS onboarding and QBR kit
- **Score**: 18 (onboarding), 18 (QBRs), 16 (health scoring)
- **JD asks**: onboarding for time to value (46%), success plans and QBRs (62%), health scoring (23%) of CS JDs
- **Targets (11)**: ArmorCode, Culture Amp, DualEntry, GoLinks, Neara, OpenRouter, Overjet, PermitFlow, Semperis, Socket, Veracode
- **Deliverable**: onboarding journey audit from their docs and trial, a QBR template tied to their product's value metrics, and a churn signal map from public reviews
- **Note**: CS is the most leader heavy family (9 of 13 JDs); pitch as "your new director starts with this on day one"

## Honorable mention

- **Win/loss from public reviews** (score 18): synthesize G2, Capterra and Reddit into win themes and loss themes. Targets: CertifyOS, Fireworks AI, GC AI, Nooks, Overjet, Proof, ROLLER

## Best first targets

Companies that appear in 3 or more plays, so one research pass feeds several hooks:

- **GC AI**: plays 1, 2, 3, 4, 5, 8, 9 (hiring PMM, Demand Gen and RevOps directors at once)
- **OpenRouter**: plays 3, 6, 7, 8, 9, 10
- **Simetrik**: plays 3, 6, 7, 8, 9
- **Fireworks AI**: plays 1, 2, 4, 8 (three director GTM roles open)
- **Overjet**: plays 1, 2, 8, 10
- **Morning Consult**: plays 1, 2, 4, 8
- **accessiBe**: plays 6, 7, 9 (hiring a 6 month temporary Head of Demand Gen, so already buying interim help)
