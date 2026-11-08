"""Phase 4: build output/patterns.md from requirements + theme maps."""
import csv, glob, re, collections as C

req = {r["row_id"]: r for r in csv.DictReader(open("data/requirements.csv"))}
comp = {r["company"]: r for r in csv.DictReader(open("data/companies.csv"))}
url = {}
for f in glob.glob("data/jds/*.md"):
    m = re.search(r"^- url: (.*)$", open(f).read(), re.M)
    url[f.split("/")[-1]] = m.group(1).strip()

FAM = [("pmm", "Product Marketing"), ("dg", "Digital / Demand Gen"), ("cs", "Customer Success"), ("revops", "RevOps")]
jds_by_fam = C.defaultdict(set)
for r in req.values():
    jds_by_fam[r["role_family"]].add(r["jd_file"])
ALL_JDS = {r["jd_file"] for r in req.values()}

def band(c):
    f = comp.get(c, {}).get("total_funding", "")
    if f in ("$1M-$5M", "$5M-$10M", "$10M-$25M", "$25M-$50M"): return "Raised under $50M"
    if f in ("$50M-$100M",): return "Raised $50M to $100M"
    if f in ("$100M-$250M", "$250M+"): return "Raised $100M+"
    return "Funding unknown"

def jd_company(j):
    return next(r["company"] for r in req.values() if r["jd_file"] == j)

def pct(n, d): return f"{round(100*n/d)}%"

out = ["# GTM Director JD Patterns", "",
       f"- Sample: {len(ALL_JDS)} director level GTM job descriptions from {len({r['company'] for r in req.values()})} B2B SaaS companies",
       f"- Requirements extracted: {len(req)}",
       "- Pulled 2026-11-08 from each company's Greenhouse, Lever or Ashby job board",
       "- Count = number of JDs that include the theme at least once (not number of bullets)",
       "- Source JDs: `data/jds/`; row level data: `data/requirements.csv`", ""]

theme_rows = {}
for slug, fam in FAM:
    themes = {t["theme_id"]: t for t in csv.DictReader(open(f"data/themes_{slug}.csv"))}
    m = list(csv.DictReader(open(f"data/themes_{slug}_map.csv")))
    by = C.defaultdict(set)
    for x in m:
        by[x["theme_id"]].add(req[x["row_id"]]["jd_file"])
    n = len(jds_by_fam[fam])
    ranked = sorted(by.items(), key=lambda kv: -len(kv[1]))
    out += [f"## {fam} ({n} JDs)", "", "| # | Requirement theme | JDs | Share | Category | Output | Example JDs |", "|---|---|---|---|---|---|---|"]
    for i, (tid, js) in enumerate(ranked[:15], 1):
        t = themes[tid]
        ex = ", ".join(f"[{jd_company(j)}]({url[j]})" for j in sorted(js)[:3])
        out.append(f"| {i} | {t['theme']} | {len(js)} | {pct(len(js), n)} | {t['category']} | {t['deliverable_type']} | {ex} |")
        theme_rows[(fam, t["theme"])] = js
    out.append("")

# tools & metrics
tools, mets = C.Counter(), C.Counter()
for j in ALL_JDS:
    rs = [r for r in req.values() if r["jd_file"] == j]
    for t in {t.strip() for r in rs for t in r["tools_named"].split(";") if t.strip()}: tools[t] += 1
    for t in {t.strip().lower() for r in rs for t in r["metric_named"].split(";") if t.strip()}: mets[t] += 1
N = len(ALL_JDS)
out += ["## Tools named", "", "| Tool | JDs | Share |", "|---|---|---|"] + [f"| {k} | {v} | {pct(v,N)} |" for k, v in tools.most_common(15)] + [""]
out += ["## Metrics named", "", "| Metric | JDs | Share |", "|---|---|---|"] + [f"| {k} | {v} | {pct(v,N)} |" for k, v in mets.most_common(15)] + [""]

# AI
p = re.compile(r"\bAI\b|\bLLMs?\b|\bagentic\b|\bagents?\b|Claude|ChatGPT|\bGPT\b|n8n|automat", re.I)
ai = {r["jd_file"] for r in req.values() if p.search(r["requirement"]) or p.search(r["tools_named"])}
out += ["## AI and automation", "", f"- {len(ai)} of {N} JDs ({pct(len(ai),N)}) mention AI, agents or automation in a requirement"]
for fam in jds_by_fam:
    a = len(ai & jds_by_fam[fam]); n = len(jds_by_fam[fam])
    out.append(f"- {fam}: {a} of {n} ({pct(a,n)})")
out.append("")

# builder vs leader
def sig(j):
    c = C.Counter(r["seniority_signal"] for r in req.values() if r["jd_file"] == j and r["seniority_signal"] != "none")
    return c.most_common(1)[0][0] if c else "none"
out += ["## Builder vs leader", "", "| Role family | Builder | Leader | JDs |", "|---|---|---|---|"]
for fam in jds_by_fam:
    s = C.Counter(sig(j) for j in jds_by_fam[fam])
    out.append(f"| {fam} | {s['builder']+s['both']} | {s['leader']} | {len(jds_by_fam[fam])} |")
out.append("")

# by funding
out += ["## By funding raised (proxy for stage)", "", "Clay does not give round names, so total funding raised stands in for stage.", "",
        "| Funding band | JDs | Builder share | AI mention share | Pipeline named |", "|---|---|---|---|---|"]
bands = C.defaultdict(set)
for j in ALL_JDS: bands[band(jd_company(j))].add(j)
pipe = {r["jd_file"] for r in req.values() if "pipeline" in r["metric_named"].lower()}
for b in ["Raised under $50M", "Raised $50M to $100M", "Raised $100M+", "Funding unknown"]:
    js = bands[b]
    if not js: continue
    bl = sum(1 for j in js if sig(j) in ("builder", "both"))
    out.append(f"| {b} | {len(js)} | {pct(bl,len(js))} | {pct(len(ai&js),len(js))} | {pct(len(pipe&js),len(js))} |")
out.append("")

open("output/patterns_data.md", "w").write("\n".join(out))
print("\n".join(out))
