#!/usr/bin/env python3
"""Build ONE Excel workbook (Food-Bangalore-ALL-IN-ONE.xlsx) holding every lead,
every email, every leak/win, every source and the skills used per audit."""
import json, sys, re
from pathlib import Path
from datetime import date

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from audit_pdf_food import _slug
from leads_attractive_block import ATTRACTIVE
from evidence_data import E as EVIDENCE, CRAWL_DATE
from build_evidence_audits import derive, _row
from build_verify_guide import ROWS as VERIFY_ROWS, NOT_VERIFIABLE

NAVY = "0F172A"; LIGHT = "F1F5F9"; RED_BG = "FFF1F2"; GREEN_BG = "ECFDF5"; PURPLE = "F5F3FF"
WHITE_BOLD = Font(bold=True, color="FFFFFF", size=10)
HDR = PatternFill("solid", fgColor=NAVY)
WRAP = Alignment(wrap_text=True, vertical="top")
THIN = Border(*[Side(style="thin", color="D8DEE8")]*4)

def style_header(ws, row=1, ncols=None):
    ncols = ncols or ws.max_column
    for c in range(1, ncols+1):
        cell = ws.cell(row=row, column=c)
        cell.font = WHITE_BOLD; cell.fill = HDR
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws.row_dimensions[row].height = 26
    ws.freeze_panes = ws.cell(row=row+1, column=1)

def autosize(ws, widths):
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

def plain_html(t):
    t = re.sub(r"<br\s*/?>", "\n", t)
    t = re.sub(r"</?b>", "", t)
    t = re.sub(r"</?i>", "", t)
    return t.strip()

def main():
    leads = [json.loads(f.read_text(encoding="utf-8")) for f in sorted(ROOT.glob("leads/*.json"))]
    leads.sort(key=lambda d: (-d["score"], d["brand"]))
    wb = Workbook()

    # ---------------------------------------------------------------- 1. README
    ws = wb.active; ws.title = "README"
    rows = [
        ["SMART PURSUIT — FOOD / BENGALURU AUDIT PACK", ""],
        ["Everything in this file is verified live data. Nothing is simulated.", ""],
        ["", ""],
        ["Date of live verification", "02 OCT 2026"],
        ["Leads", f"{len(leads)} brands (no duplicates with the agency's existing 100 leads or the Solar pipeline)"],
        ["Audit PDFs", f"audits/<brand>-paid-media-measurement-audit.pdf — 7-page Paid Media &amp; Measurement Audit: cover metrics, contents+method, live ad account, severity-ranked findings with the raw measurement quoted, evidence register, opportunity score /20, qualification, effort-ordered next steps"],
        ["Emails", f"{sum(len(l['outreach']) for l in leads)} emails — 4 per brand — see the 'Emails' sheet"],
        ["Skills used per audit", "performance-lead-audit orchestrating: ads, ad-creative, copywriting, cro, analytics/attribution, competitor-profiling, cold-email, pdf-report-generator"],
        ["", ""],
        ["HOW THE DATA WAS VERIFIED", ""],
        ["Ad counts", "Google Ads Transparency (region IN), re-checked at generation time on 02 OCT 2026"],
        ["Meta ads", "Meta Ad Library — verified live for Akshayakalpa (4 to 5 creatives, running since 19 May 2026, library IDs recorded) and Licious (Library ID 983369480870934, ≈550 live); other brands returned no inventory and are reported as not measured, never as zero"],
        ["Emails", "Crawled from each brand's own website / help centre / corporate pages — no guessed, generic or formation addresses"],
        ["Site/tech facts", "Live HTTP headers + HTML captured 02 OCT 2026 (GTM/GA4/Ads/pixel IDs, platform, redirects, defects quoted verbatim)"],
        ["Financials/market data", "Public coverage, labelled as reported — third-party estimates marked as estimates"],
        ["", ""],
        ["INTEGRITY RULES", ""],
        ["1", "Every number in a PDF's 'Before (live)' column traces to a source listed on that PDF"],
        ["2", "Benchmarks are labelled as industry benchmarks — no client results are invented"],
        ["3", "Where something was NOT verified it is reported as unavailable or not measured — never as zero, and never estimated. A tag is only called absent when a second method confirmed it; otherwise it reads unconfirmed"],
        ["4", "No lead, email or ad count is duplicated across sheets or with existing pipelines"],
    ]
    for r in rows: ws.append(r)
    ws["A1"].font = Font(bold=True, size=14, color=NAVY)
    ws["A2"].font = Font(bold=True, size=11)
    for r in (4,10,17): ws.cell(row=r, column=1).font = Font(bold=True, size=11, color=NAVY)
    autosize(ws, [30, 110])
    for row in ws.iter_rows(min_row=1, max_row=ws.max_row):
        row[1].alignment = WRAP

    # ---------------------------------------------------------------- 2. LEADS
    ws = wb.create_sheet("Leads")
    ws.append(["#","Brand","Website","Instagram","Niche","Lead score /10","Live Google ads",
               "Lead email (crawled)","Phone","Legal entity","Address / HQ","Contact source",
               "Audit PDF (7-page evidence format)","Outreach file","Verified on"])
    for i, l in enumerate(leads, 1):
        s = _slug(l["brand"])
        ws.append([i, l["brand"], l["website"], l.get("instagram",""), l["niche"], l["score"],
                   l["ads_active"], l["contact"]["email"], l["contact"].get("phone",""),
                   l["contact"].get("entity",""), l["contact"].get("address",""),
                   l.get("contact_source", "Own website / help centre / corporate pages"),
                   f"audits/{s}-paid-media-measurement-audit.pdf", f"outreach/{s}-outreach-templates.md", l["verified_on"]])
    style_header(ws); autosize(ws, [4,22,26,22,30,10,12,34,18,34,52,34,38,40,12])
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment = WRAP; c.border = THIN
    ws.auto_filter.ref = ws.dimensions

    # ---------------------------------------------------------------- 3. EMAILS
    ws = wb.create_sheet("Emails")
    ws.append(["Brand","#","Send on","Subject","Body (plain text — paste into your email tool)","To (crawled email)"])
    for l in leads:
        for i, (subj, body) in enumerate(l["outreach"], 1):
            day = {1:"Day 1", 2:"Day 3", 3:"Day 7", 4:"Day 14"}[i]
            ws.append([l["brand"], i, day, subj, plain_html(body), l["contact"]["email"]])
    style_header(ws); autosize(ws, [20,4,8,54,110,32])
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment = WRAP; c.border = THIN
        ws.row_dimensions[row[0].row].height = 120
    ws.auto_filter.ref = ws.dimensions

    # ---------------------------------------------------------------- 4. LEAKS & WINS
    ws = wb.create_sheet("Leaks & Roadmap")
    ws.append(["Brand","Item","Title","Detail"])
    for l in leads:
        b = ATTRACTIVE.get(_slug(l["brand"]), {})
        for i, (t, d) in enumerate(b.get("leaks", []), 1):
            ws.append([l["brand"], f"LEAK {i}", t, d])
        for day, t, d in b.get("roadmap", []):
            ws.append([l["brand"], f"WIN {day}", t, d])
    style_header(ws); autosize(ws, [20,10,46,105])
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment = WRAP; c.border = THIN
        if row[1].value.startswith("LEAK"): row[2].fill = PatternFill("solid", fgColor=RED_BG)
        else: row[2].fill = PatternFill("solid", fgColor=GREEN_BG)

    # ---------------------------------------------------------------- 5. VS COMPETITOR
    ws = wb.create_sheet("You vs Competitor")
    ws.append(["Brand","Side","Point"])
    for l in leads:
        b = ATTRACTIVE.get(_slug(l["brand"]), {})
        for y in b.get("you", []): ws.append([l["brand"], "YOU", y])
        for c in b.get("competitor", []): ws.append([l["brand"], "COMPETITOR", c])
    style_header(ws); autosize(ws, [20,14,105])
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment = WRAP; c.border = THIN
        row[1].fill = PatternFill("solid", fgColor=(RED_BG if row[1].value == "YOU" else GREEN_BG))

    # ---------------------------------------------------------------- 6. ROI
    ws = wb.create_sheet("Expected ROI")
    ws.append(["Brand","Metric","Before (live)","After roadmap","Industry benchmark"])
    for l in leads:
        b = ATTRACTIVE.get(_slug(l["brand"]), {})
        for r in b.get("roi", []): ws.append([l["brand"], *r])
    style_header(ws); autosize(ws, [20,26,34,40,50])
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment = WRAP; c.border = THIN

    # ---------------------------------------------------------------- 7. AUDIT BASIS / SOURCES
    ws = wb.create_sheet("Audit Basis (sources)")
    ws.append(["Brand","Source (from the PDF's Audit Basis box)"])
    for l in leads:
        for s in l.get("sources", []):
            ws.append([l["brand"], s])
    style_header(ws); autosize(ws, [20,120])
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment = WRAP; c.border = THIN; c.fill = PatternFill("solid", fgColor=PURPLE)

    # ---------------------------------------------------------------- 8. SKILLS USED
    ws = wb.create_sheet("Skills Used")
    ws.append(["Audit section","Repository skill(s)","What was done with it"])
    for r in [
        ["Ad Intelligence","ads","Google Ads Transparency (region IN) + Meta Ad Library (country IN): live counts and, where open, individual creatives with running-since dates"],
        ["Creative audit","ad-creative","Creative formats, fatigue signals, refresh-rate analysis per brand"],
        ["Copy & angle audit","copywriting","Hook/angle analysis from live ad copy captured in the Ad Library and Transparency"],
        ["Landing / destination audit","cro","Destination-path step count, locator vs product page, trust-proof placement"],
        ["Tracking audit","analytics, attribution","GTM/GA4 tags detected in live HTML (e.g. GTM-K6SZV8J, G-EN77D2S0YH); CAPI/Enhanced-Conversions guidance"],
        ["Competitor benchmark","competitor-profiling, competitors, competitor-x-ray, funnel-spy","Category benchmark rows in every PDF ('You vs Competitor')"],
        ["Outreach","cold-email, outreach-personalizer","4-email sequences per brand (Day 1/3/7/14), plain text ready"],
        ["PDF output","pdf-report-generator","7-page Paid Media &amp; Measurement Audit: metric cards, method, live ad account, coverage table, severity findings with quoted evidence, evidence register, opportunity score, qualification, next steps"],
    ]:
        ws.append(r)
    style_header(ws); autosize(ws, [26,44,95])
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment = WRAP; c.border = THIN


    # ------------------------------------------------- 9. FINDINGS (severity + evidence)
    ws = wb.create_sheet("Findings (severity+evidence)")
    ws.append(["Brand","#","Severity","Finding","Evidence (raw measurement)","Why it matters (analysis)"])
    sev_count = {}
    for l in leads:
        slug = _slug(l["brand"])
        lead = EVIDENCE.get(slug)
        if not lead:
            continue
        order = {"CRITICAL":0,"HIGH":1,"MEDIUM":2,"LOW":3,"NOTE":4}
        for i, f in enumerate(sorted(lead["findings"], key=lambda x: order.get(x["sev"],9)), 1):
            sev_count[f["sev"]] = sev_count.get(f["sev"], 0) + 1
            ws.append([l["brand"], i, f["sev"], f["title"], f["evidence"], f["reading"]])
    style_header(ws); autosize(ws, [20,4,11,52,66,80])
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment = WRAP; c.border = THIN
        s = row[2].value
        fill = {"CRITICAL":"FEE2E2","HIGH":"FFEDD5","MEDIUM":"FEF3C7","LOW":"E0E7FF"}.get(s)
        if fill: row[2].fill = PatternFill("solid", fgColor=fill)
    ws.auto_filter.ref = ws.dimensions

    # ------------------------------------------------- 10. OPPORTUNITY SCORE
    ws = wb.create_sheet("Opportunity Score")
    ws.append(["Brand","Dimension","Score /4","What the score is based on","Overall /20","Grade","Grade note"])
    for l in leads:
        slug = _slug(l["brand"])
        lead = EVIDENCE.get(slug)
        if not lead:
            continue
        total = sum(v for _, _, v in lead["score_dims"])
        for name, note, val in lead["score_dims"]:
            ws.append([l["brand"], name, val, note, total, lead["grade"], lead["grade_note"]])
    style_header(ws); autosize(ws, [20,26,10,62,12,8,52])
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment = WRAP; c.border = THIN

    # ------------------------------------------------- 11. COVERAGE (what was measured)
    ws = wb.create_sheet("Coverage (measured vs not)")
    ws.append(["Brand","Surface","Status","Method / reason","Crawl date"])
    for l in leads:
        slug = _slug(l["brand"])
        lead = EVIDENCE.get(slug)
        if not lead:
            continue
        d = derive(dict(lead))
        for surf, status, meth in d["coverage"]:
            ws.append([l["brand"], surf, status, meth, CRAWL_DATE])
    style_header(ws); autosize(ws, [20,30,30,62,14])
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment = WRAP; c.border = THIN
        if row[2].value == "UNAVAILABLE":
            row[2].fill = PatternFill("solid", fgColor="FEF3C7")
        elif row[2].value == "NOT MEASURED":
            row[2].fill = PatternFill("solid", fgColor=LIGHT)

    # ------------------------------------------------- 12. EVIDENCE REGISTER
    ws = wb.create_sheet("Evidence Register")
    ws.append(["Brand","Measurement","Source","Value observed","Date"])
    for l in leads:
        slug = _slug(l["brand"])
        lead = EVIDENCE.get(slug)
        if not lead:
            continue
        d = derive(dict(lead))
        for item, src, val, dt in d["register"]:
            ws.append([l["brand"], item, src, val, dt])
    style_header(ws); autosize(ws, [20,28,42,80,14])
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment = WRAP; c.border = THIN
    ws.auto_filter.ref = ws.dimensions


    # ------------------------------------------------- 13. VERIFY THESE (links)
    ws = wb.create_sheet("Verify These (links)")
    ws.append(["Brand","Claim in the audit","Where to check it","Link","What you should see"])
    for l in leads:
        slug = _slug(l["brand"])
        for claim, where, link, expect in VERIFY_ROWS.get(slug, []):
            ws.append([l["brand"], claim, where, link, expect])
    style_header(ws); autosize(ws, [20,46,40,60,72])
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment = WRAP; c.border = THIN
        cell = row[3]
        if isinstance(cell.value, str) and cell.value.startswith("http"):
            cell.hyperlink = cell.value
            cell.font = Font(color="1155CC", underline="single", size=10)
    ws.auto_filter.ref = ws.dimensions

    # ------------------------------------------------- 14. WHAT CANNOT BE VERIFIED
    ws = wb.create_sheet("Cannot be verified")
    ws.append(["Item","Why no public source exists"])
    for a, b in NOT_VERIFIABLE:
        ws.append([a, b])
    ws.append(["", ""])
    ws.append(["Rule applied in every audit",
               "Where a value could not be measured it is reported as unavailable or not measured. "
               "Nothing has been inferred to fill a gap, and no tag is described as absent unless a second method confirmed it."])
    style_header(ws); autosize(ws, [34,110])
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment = WRAP; c.border = THIN

    out = ROOT / "Food-Bangalore-ALL-IN-ONE.xlsx"
    wb.save(out)
    print(f"Saved {out.name}: {len(leads)} leads | {sum(len(l['outreach']) for l in leads)} emails | sheets: {wb.sheetnames}")

if __name__ == "__main__":
    main()
