#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build everything for BATCH 2 — the ten Food/Bengaluru leads added on 3 October 2026.

Outputs
  leads/<slug>.json                                  (10 new lead records)
  audits/<slug>-paid-media-measurement-audit.pdf     (10 new audits)
  outreach/<slug>-outreach-templates.md              (10 new 4-email files)
  ALL-EMAIL-SEQUENCES.md                             (regenerated: 21 brands x 4 emails)
  LEADS-INDEX.csv                                    (regenerated: 21 leads)

The audits use the same renderer as the first eleven (audit_evidence.build_evidence_pdf)
and the same derivation of coverage/register rows (build_evidence_audits.derive), so the
new PDFs are byte-for-byte the same format family as the existing pack.
"""
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from audit_pdf_food import _slug                    # noqa: E402
from audit_evidence import build_evidence_pdf       # noqa: E402
import build_evidence_audits as bea                 # noqa: E402
from build_evidence_audits import derive            # noqa: E402
from batch2_evidence import E2, VERIFY2, CRAWL_DATE as DATE2   # noqa: E402
from batch2_leads import LEADS2                     # noqa: E402
from evidence_data import CRAWL_DATE as DATE1       # noqa: E402

AUDIT_NAME = "{slug}-paid-media-measurement-audit.pdf"


def write_leads():
    """Dump the lead records. Findings and source links are derived from the SAME
    evidence entries the PDFs are built from, so the workbook and the reports can
    never disagree about what was found."""
    out = []
    for slug, lead in LEADS2.items():
        lead = dict(lead)
        ev = E2[slug]
        lead["findings"] = [f"<b>{f['title']}:</b> {plain(f['reading'])}" for f in ev["findings"]]
        lead["severity_key"] = [[f["sev"], f["title"]] for f in ev["findings"]]
        base = list(lead.get("sources", []))
        for claim, where, link, expect in VERIFY2.get(slug, []):
            base.append(f"{claim} — check: {link}")
        lead["sources"] = base
        lead["verified_on"] = "03 OCT 2026"
        path = ROOT / "leads" / f"{slug}.json"
        path.write_text(json.dumps(lead, indent=1, ensure_ascii=False), encoding="utf-8")
        out.append((slug, path))
    return out


def plain(html):
    t = html.replace("<br/>", "\n").replace("<br />", "\n")
    t = re.sub(r"</?b>", "**", t)
    t = t.replace("&amp;", "&").replace("&nbsp;", " ")
    return t.strip()


def write_outreach():
    written = []
    for slug, lead in LEADS2.items():
        audit = AUDIT_NAME.format(slug=slug)
        lines = [f"# {lead['brand']} - Outreach Templates (Smart Pursuit BD team)", "",
                 f"> Companion to `audits/{audit}` (Lead score {lead['score']}/10). "
                 f"Every fact quoted below was measured on 3 October 2026 and is listed in VERIFY-THE-DATA.md. "
                 f"Do NOT attach the audit automatically - these are internal BD templates.", "", "---", ""]
        for i, (subj, body) in enumerate(lead["outreach"], 1):
            lines += [f"### {subj}", "", plain(body), "", "---", ""]
        path = ROOT / "outreach" / f"{slug}-outreach-templates.md"
        path.write_text("\n".join(lines), encoding="utf-8")
        written.append(path)
    return written


def write_audits():
    OUT = ROOT / "audits"
    OUT.mkdir(exist_ok=True)
    written = []
    bea.D = DATE2          # coverage/register rows must carry the batch-2 crawl date
    for slug, lead in E2.items():
        data = derive(dict(lead))
        data["generated_on"] = DATE2
        out = OUT / AUDIT_NAME.format(slug=slug)
        build_evidence_pdf(data, out)
        written.append(out)
    return written


def audit_filename(slug, verified):
    """Actual file on disk for each lead, so the indexes never promise a name that is not there."""
    cand = ROOT / "audits" / AUDIT_NAME.format(slug=slug)
    if cand.exists():
        return f"audits/{cand.name}"
    legacy = ROOT / "audits" / f"{slug}-audit-report.pdf"
    if legacy.exists():
        return f"audits/{legacy.name}"
    return f"audits/{AUDIT_NAME.format(slug=slug)}"


def all_leads():
    leads = []
    for f in sorted((ROOT / "leads").glob("*.json")):
        leads.append(json.loads(f.read_text(encoding="utf-8")))
    leads.sort(key=lambda d: (-d["score"], d["brand"]))
    return leads


def write_email_sequences():
    leads = all_leads()
    lines = [f"# Food / Bengaluru - All Email Sequences ({len(leads)} brands x 4 emails)", "",
             f"> Verified live on **02–03 OCT 2026** (first eleven: 02 Oct 2026; ten added: 03 Oct 2026). "
             f"Every audit number traces to a live source - see each PDF's audit-basis box and VERIFY-THE-DATA.md.",
             "> Send as plain text or paste into your email tool; the `<br/>` tags convert to line breaks in HTML mode.", "",
             "## Lead table", "",
             "| # | Brand | Lead email (crawled) | Google ads live | Score |",
             "|---|-------|----------------------|-----------------|-------|"]
    for i, l in enumerate(leads, 1):
        lines.append(f"| {i} | {l['brand']} | {l['contact']['email']} | {l['ads_active']} | {l['score']}/10 |")
    lines += ["", "---", ""]
    for l in leads:
        slug = _slug(l["brand"])
        lines += [f"# {l['brand']}",
                  f"**Contact:** {l['contact']['email']}" + (f" · {l['contact']['phone']}" if l['contact'].get('phone') else "") + "  ",
                  f"**Entity:** {l['contact'].get('entity','')}  ",
                  f"**Audit:** `{audit_filename(slug, l.get('verified_on'))}`  ", ""]
        for subj, body in l["outreach"]:
            lines += [f"## {subj}", "", "```", plain(body), "```", ""]
        lines += ["---", ""]
    path = ROOT / "ALL-EMAIL-SEQUENCES.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_index():
    leads = all_leads()
    path = ROOT / "LEADS-INDEX.csv"
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["brand", "website", "niche", "score", "google_ads_live", "lead_email", "lead_phone",
                    "contact_entity", "audit_pdf", "outreach_md", "verified_on"])
        for l in leads:
            slug = _slug(l["brand"])
            w.writerow([l["brand"], l["website"], l["niche"], l["score"], l["ads_active"],
                        l["contact"]["email"], l["contact"].get("phone", ""), l["contact"].get("entity", ""),
                        audit_filename(slug, l.get("verified_on")),
                        f"outreach/{slug}-outreach-templates.md", l.get("verified_on", "")])
    return path


def register_seen():
    path = ROOT.parent.parent / "data" / "seen_leads.json"
    if not path.exists():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    brands = data.setdefault("brands", {})
    added = 0
    for l in LEADS2.values():
        if l["brand"] not in brands:
            brands[l["brand"]] = {"first_seen": "2026-10-03T00:00:00", "day": 4,
                                  "website": l["website"], "niche": l["niche"]}
            added += 1
    data["brands"] = dict(sorted(brands.items()))
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    return added


def main():
    leads = write_leads()
    print(f"leads written      : {len(leads)}")
    audits = write_audits()
    print(f"audits built       : {len(audits)}")
    out = write_outreach()
    print(f"outreach files     : {len(out)}")
    print(f"emails in all-seq  : {write_email_sequences()}")
    print(f"index              : {write_index()}")
    print(f"seen_leads added   : {register_seen()}")


if __name__ == "__main__":
    main()
