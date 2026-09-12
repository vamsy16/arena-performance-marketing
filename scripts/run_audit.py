#!/usr/bin/env python3
"""
One-command runner: given a brand name (slug) or a path to a leads CSV row index,
generate audit PDF + outreach MD using the reusable audit_pdf engine.

Usage:
  # Generate audit from a saved lead JSON file:
  python scripts/run_audit.py leads/physics-wallah.json

  # Generate audit for the Nth lead in the daily CSV:
  python scripts/run_audit.py --day 1 --row 0
  (row 0 = first lead, Physics Wallah)

  # Quick ad-hoc audit (minimal):
  python scripts/run_audit.py --brand "BoAt" --website boat-lifestyle.com --niche "D2C Audio" --ads 140 --spend "Rs.5-10 Cr"

Outputs:
  audits/<brand-slug>-audit-report.pdf
  outreach/<brand-slug>-outreach-templates.md
"""
import argparse, csv, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from audit_pdf import generate_audit_pdf, _slug, ROOT

def load_from_csv(day: int, row: int) -> dict:
    """Load a lead from a daily_history CSV and return a lead dict skeleton."""
    hist = ROOT / "data" / "daily_history"
    files = sorted(hist.glob(f"day-{day:02d}-*-leads.csv"))
    if not files:
        raise FileNotFoundError(f"No Day {day} CSV found in {hist}")
    csv_path = files[-1]
    with open(csv_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if row >= len(rows):
        raise IndexError(f"Row {row} out of range (CSV has {len(rows)} rows)")
    r = rows[row]
    return {
        "brand": r["brand"],
        "website": r["website"],
        "instagram": r.get("instagram",""),
        "niche": r.get("niche",""),
        "score": int(r.get("score", 7)),
        "ads_active": int(r.get("active_ads", 20)),
        "spend": r.get("spend", ""),
        "destination": r.get("destination", "Website"),
        "ad_library_link": r.get("ad_library_link",""),
        "leak": r.get("leak",""),
    }

def main():
    ap = argparse.ArgumentParser(description="Generate Smart Pursuit audit PDF for a lead")
    ap.add_argument("json", nargs="?", help="Path to lead JSON file (in leads/)")
    ap.add_argument("--day", type=int, help="Day number (pull from data/daily_history)")
    ap.add_argument("--row", type=int, default=0, help="Row index in CSV (default 0 = first)")
    ap.add_argument("--brand")
    ap.add_argument("--website")
    ap.add_argument("--niche", default="")
    ap.add_argument("--score", type=int, default=7)
    ap.add_argument("--ads", type=int, dest="ads_active", default=20)
    ap.add_argument("--spend", default="")
    ap.add_argument("--revenue", default="")
    args = ap.parse_args()

    if args.json:
        lead = json.loads(Path(args.json).read_text())
    elif args.day is not None:
        lead = load_from_csv(args.day, args.row)
    elif args.brand and args.website:
        lead = {
            "brand": args.brand, "website": args.website,
            "niche": args.niche, "score": args.score,
            "ads_active": args.ads_active, "spend": args.spend,
            "revenue": args.revenue,
        }
    else:
        ap.error("Provide either a JSON path, --day/--row, or --brand + --website")

    pdf, md = generate_audit_pdf(lead)
    print(f"Audit PDF:  {pdf}")
    print(f"Outreach:   {md}")
    print(f"Brand:      {lead['brand']}  (score {lead.get('score',7)}/10)")

if __name__ == "__main__":
    main()
