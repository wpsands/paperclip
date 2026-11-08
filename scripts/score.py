"""Phase 5: score deliverable themes. Scores 1-5: agent doable now, public inputs only,
buyer visible in under 2 min, deliverable in 4 hours or less. Frequency is computed from JD share."""
import csv, collections as C
S = {  # theme_id: (agent, public, visible, time)
"dg_T11":(3,1,4,3),"revops_T13":(2,1,2,1),"cs_T06":(4,3,3,3),"pmm_T01":(5,5,5,4),"pmm_T03":(5,5,5,4),
"revops_T02":(4,3,5,3),"revops_T12":(3,2,2,3),"cs_T11":(4,3,3,4),"dg_T22":(4,3,4,3),"dg_T05":(5,5,5,3),
"pmm_T06":(3,3,3,2),"revops_T15":(2,1,4,3),"revops_T06":(2,1,3,1),"dg_T12":(2,1,3,2),"dg_T02":(4,4,4,3),
"dg_T16":(3,2,2,3),"pmm_T04":(5,5,5,4),"pmm_T21":(3,2,2,4),"pmm_T02":(5,5,5,4),"dg_T03":(2,1,3,3),
"dg_T10":(3,4,3,3),"cs_T05":(3,2,3,3),"cs_T04":(4,4,4,3),"cs_T08":(3,3,4,3),"cs_T03":(4,3,3,3),
"cs_T24":(2,1,3,3),"revops_T08":(4,4,4,3),"revops_T07":(3,2,3,3),"revops_T28":(2,1,3,3),"revops_T27":(2,1,2,2),
"revops_T10":(2,1,3,2),"pmm_T16":(3,3,3,3),"pmm_T09":(4,4,5,3),"pmm_T26":(5,5,4,4),"dg_T04":(4,4,4,4),
"cs_T18":(4,3,4,3),"pmm_T05":(3,3,3,3),"pmm_T08":(5,5,5,4),"pmm_T40":(3,3,3,3),"pmm_T07":(3,4,3,3),
"dg_T21":(3,2,3,3),"dg_T15":(5,4,5,4),"dg_T25":(3,3,3,3),"revops_T01":(4,4,5,4),"revops_T14":(2,1,2,1),
"revops_T09":(2,2,2,3),"revops_T16":(2,1,3,3),"pmm_T22":(4,3,4,3),"pmm_T20":(2,2,3,3),"cs_T10":(2,1,3,3),
"dg_T06":(5,5,5,4),"dg_T14":(3,2,3,3),"dg_T07":(5,5,5,4),"dg_T19":(3,2,3,3),"dg_T17":(3,3,3,3),
"dg_T13":(3,2,3,3),"pmm_T11":(4,5,4,3),"pmm_T19":(3,3,4,2),"pmm_T25":(3,3,2,3),"cs_T21":(2,1,2,3),
"cs_T23":(1,1,2,1),"cs_T09":(2,1,3,3),"cs_T20":(3,2,3,2),"cs_T07":(4,3,4,4),"dg_T08":(3,3,3,3),
"dg_T09":(4,4,4,4),"dg_T28":(4,4,4,3),"pmm_T18":(3,3,4,3),
}
FAM = {"pmm":"Product Marketing","dg":"Digital / Demand Gen","cs":"Customer Success","revops":"RevOps"}
req = {r["row_id"]: r for r in csv.DictReader(open("data/requirements.csv"))}
n = {s: len({r["jd_file"] for r in req.values() if r["role_family"] == f}) for s, f in FAM.items()}
rows = []
for s, f in FAM.items():
    th = {t["theme_id"]: t for t in csv.DictReader(open(f"data/themes_{s}.csv"))}
    by = C.defaultdict(set)
    for m in csv.DictReader(open(f"data/themes_{s}_map.csv")):
        by[m["theme_id"]].add(req[m["row_id"]]["company"])
    for tid, sc in S.items():
        if not tid.startswith(s + "_"): continue
        share = len(by[tid]) / n[s]
        freq = 5 if share >= .7 else 4 if share >= .55 else 3 if share >= .45 else 2 if share >= .3 else 1
        rows.append({"theme_id": tid, "role_family": f, "theme": th[tid]["theme"], "jds": len(by[tid]), "family_jds": n[s],
                     "share": f"{round(100*share)}%", "agent": sc[0], "public": sc[1], "visible": sc[2], "time": sc[3],
                     "frequency": freq, "total": sum(sc) + freq, "companies": "; ".join(sorted(by[tid]))})
rows.sort(key=lambda r: (-r["total"], -r["jds"]))
w = csv.DictWriter(open("output/opportunity_scores.csv", "w", newline=""), fieldnames=list(rows[0]))
w.writeheader(); w.writerows(rows)
for r in rows[:20]: print(r["total"], r["theme_id"], r["theme"], r["share"], "|", r["companies"])
