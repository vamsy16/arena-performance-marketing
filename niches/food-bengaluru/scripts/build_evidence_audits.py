#!/usr/bin/env python3
"""Build the 11 Smart Pursuit Paid Media & Measurement audits (7-page evidence format).

Coverage and register rows are derived from the same measured ad_account rows that
appear in the report, so nothing can drift between the two pages.
"""
from pathlib import Path
import sys, shutil, re

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from audit_evidence import build_evidence_pdf          # noqa: E402
from evidence_data import E, CRAWL_DATE                # noqa: E402

OUT = ROOT / "audits"
PREV = ROOT / "audits" / "_previous-attractive-format"
D = CRAWL_DATE

PLATFORM_SRC = "Live HTTP response of the site root"
PLATFORM_ITEM = "Site platform and headers"
TAG_ITEM = "Measurement tags on the site root"
TAG_SRC = "HTML inspection of the site root"
META_SRC = "Meta Ad Library (country India)"
GOOG_SRC = "Google Ads Transparency Center (region India)"


def _row(rows, *labels):
    """Label-priority lookup: the first label that matches any row wins."""
    for lb in labels:
        for k, v in rows:
            if lb.lower() in k.lower():
                return v
    return None


def derive(lead):
    rows = lead["ad_account"]
    site = lead["prepared_for_line"].split("·")[0].strip().split("  ")[0].strip()
    google = _row(rows, "Google creatives live", "Ad platforms observed", "Google ads transparency") or "not measured"
    google = " ".join(google.split())
    if "·" in google:                      # "Google (≈400 creatives, region India) · Meta (...)"
        google = google.split("·")[0].strip()
    if google.lower().startswith("google (") and google.endswith(")"):
        google = google[len("google ("):-1].strip()
    meta = _row(rows, "Meta ads", "Meta library", "Third-party distribution")
    tags = _row(rows, "Measurement tags", "Title tag observed") or "not measured"
    platform = _row(rows, "Site platform") or "not measured"
    contact = _row(rows, "Published contact") or "none published on the pages reviewed"
    fin = (_row(rows, "Published FY25") or _row(rows, "Published") or _row(rows, "Brand heritage")
           or _published(lead) or "not used in this report")

    lead["coverage"] = [
        ("Google creative inventory", f"MEASURED — {_num(google)}", GOOG_SRC + ", " + D),
        ("Meta ad inventory", ("MEASURED — verified ad by ad" if meta and ("verified" in meta.lower() or "started" in meta.lower())
                               else ("MEASURED — " + _num(meta)) if meta else "NOT MEASURED"),
         META_SRC + ", " + D if meta else "no inventory returned for the brand term on the crawl date"),
        ("Measurement tags", ("MEASURED — " + (_short(tags))) if "unconfirmed" not in tags.lower() and "not measured" not in tags.lower() and "not performed" not in tags.lower()
         else "NOT MEASURED", TAG_SRC + ", " + D),
        (PLATFORM_ITEM, "MEASURED", PLATFORM_SRC + ", " + D),
        ("Checkout and order flow", "NOT MEASURED", "outside the site root; not crawled"),
        ("Ad spend, ROAS, CPA", "UNAVAILABLE", "private to the advertiser; no public source"),
        ("Published commercial figures", "MEASURED" if fin != "not used in this report" else "NOT APPLICABLE",
         "the brand's own published pages and results, as reported" if fin != "not used in this report" else "no published figure is quoted in this report"),
    ]
    lead["register"] = [
        ("Google creatives", GOOG_SRC, google, D),
        ("Meta ads", META_SRC, (" ".join(meta.split()) if meta else "no inventory returned for the brand term"), D),
        (TAG_ITEM, TAG_SRC, tags, D),
        (PLATFORM_ITEM, PLATFORM_SRC, platform, D),
        ("Published contact", "The brand's own contact and policy pages", contact, D),
        ("Ad spend / ROAS / CPA", "No public source exists", "unavailable — not estimated", D),
        ("Published commercial figures", "The brand's own published pages and results", fin, D),
    ]
    return lead


def _num(s):
    import re
    m = re.search(r"(≈?\s?\d[\d,\.]*)", s.replace("Rs ", ""))
    return (m.group(1).replace("≈", "").strip() if m else "count recorded")


def _short(s, n=62):
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0] + " …"


def _published(lead):
    """First 'published ...' evidence line recorded anywhere in this lead's findings."""
    for f in lead["findings"]:
        for line in f["evidence"].split("\n"):
            s = line.strip()
            if s.lower().startswith("published") and any(ch.isdigit() for ch in s):
                return s
    return None


def main():
    OUT.mkdir(exist_ok=True)
    PREV.mkdir(exist_ok=True)
    for old in OUT.glob("*.pdf"):
        if old.name.endswith("-audit-report.pdf"):
            shutil.move(str(old), str(PREV / old.name))

    for slug, lead in E.items():
        lead = derive(dict(lead))
        lead["generated_on"] = CRAWL_DATE
        out = OUT / f"{slug}-paid-media-measurement-audit.pdf"
        build_evidence_pdf(lead, out)
        print(f"built: {out.name}  ({out.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    main()
