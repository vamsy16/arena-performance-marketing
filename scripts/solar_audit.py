#!/usr/bin/env python3
"""
SOLAR audit runner - generates a solar audit PDF + outreach MD into the solar
folder only. Reuses the existing reportlab engine (scripts/audit_pdf.py) so the
Smart Pursuit branding/layout stays identical, but swaps in:

  - solar folder outputs:  niches/solar/audits/ + niches/solar/outreach/
  - solar default copy:    subsidy / PM Surya Ghar, WhatsApp-first funnel,
                           CPL + cost-per-site-survey + cost-per-install metrics
  - solar quick wins:      subsidy calculator, click-to-WhatsApp, install video proof

USAGE
-----
  # Best quality: a rich lead JSON you (or the agent) filled in
  python scripts/solar_audit.py niches/solar/leads/freyrenergy-com.json

  # By brand slug from the solar daily CSV
  python scripts/solar_audit.py --day 1 --row 0

  # Ad-hoc
  python scripts/solar_audit.py --brand "Fenice Energy" --website feniceenergy.com \
      --city Chennai --segment R --ads 12

Outputs:
  niches/solar/audits/<slug>-solar-audit-report.pdf
  niches/solar/outreach/<slug>-solar-outreach-templates.md
"""
import argparse
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).parent))

import audit_pdf  # noqa: E402
from audit_pdf import generate_audit_pdf, _slug  # noqa: E402

SOLAR = ROOT / "niches" / "solar"
SOLAR_AUDITS = SOLAR / "audits"
SOLAR_OUTREACH = SOLAR / "outreach"
SOLAR_LEADS = SOLAR / "leads"
SOLAR_HISTORY = SOLAR / "data" / "daily_history"
for d in (SOLAR_AUDITS, SOLAR_OUTREACH, SOLAR_LEADS):
    d.mkdir(parents=True, exist_ok=True)

# keep every solar artefact inside niches/solar/
audit_pdf.OUTREACH_DIR = SOLAR_OUTREACH


SEGMENT_NICHE = {
    "R": "Residential Rooftop Solar (PM Surya Ghar / subsidy-driven)",
    "C": "D2C Solar Products (panels / inverters / batteries / water heaters)",
    "B": "Commercial & Industrial Rooftop Solar (C&I EPC)",
    "P": "Solar Channel Partner / Lead Marketplace",
}

SOLAR_DEFAULT_SCORES = {
    "Subsidy & Scheme Clarity": [5, "#F59E0B"],
    "WhatsApp / Speed-to-Lead": [4, "#F59E0B"],
    "Social Proof (Installs)": [3, "#EF4444"],
    "Creative Variety (Video/Reels)": [3, "#EF4444"],
    "Landing Page & Form CRO": [4, "#F59E0B"],
    "Tracking & Retargeting": [3, "#EF4444"],
}

SOLAR_DEFAULT_FINDINGS = [
    "<b>Subsidy story is buried.</b> PM Surya Ghar gives ₹30,000/₹60,000/₹78,000 for 1/2/3 kW - that is the single strongest hook in Indian residential solar and it is not the headline of the ads or the first screen of the site.",
    "<b>No click-to-WhatsApp on the ad itself.</b> In solar, the decision starts as a question (\"kitna kharcha?\", \"kitni chhat chahiye?\"). Every extra form field loses respondents; WhatsApp captures them while intent is hot.",
    "<b>Zero installation proof.</b> Buyers are being asked to spend ₹1.5-3 lakh on something invisible until it is on their roof. No roof photos, no net-meter bills, no customer video = trust gap that price cannot fix.",
    "<b>Form asks for too much too early.</b> Month bill, roof area, ownership proof, address and email before any value is delivered. 3 fields (city, phone, monthly bill) is the benchmark for a solar quote form.",
    "<b>Retargeting is missing for a 30-90 day cycle.</b> Homeowners who clicked do not buy same day. Without a WhatsApp/DPA retargeting sequence, that traffic is being rented, not owned.",
]

SOLAR_DEFAULT_WINS = [
    ("Quick Win 1 - 7 days",
     "Put the subsidy ON the creative and add Click-to-WhatsApp. Ad headline: '3 kW rooftop solar - ₹78,000 subsidy, ₹0 bill for 300 units'. Primary CTA = Send WhatsApp Message. Expected: 25-40% more qualified enquiries at the same spend.",
     "#059669", "#ECFDF5"),
    ("Quick Win 2 - 14 days",
     "Ship a 3-field savings calculator (city, monthly bill, roof type) that shows subsidy + EMI + payback instantly, then asks for the phone number. Capture before the calculator, not after. Expected: 1.5-2x form completion.",
     "#F59E0B", "#FFFBEB"),
    ("Quick Win 3 - 30 days",
     "Build the proof layer: 10 install videos (roof + net meter + customer saying the bill), Google review screenshots in creatives, and a retargeting sequence (video view 50% -> WhatsApp). Expected: cheaper CPL and a higher site-survey-to-order rate.",
     "#6D28D9", "#F5F3FF"),
]

SOLAR_DEFAULT_IMPACT = [
    ("Cost per lead (Meta)", "Rs.250-450", "Rs.150-250", "~40% cheaper"),
    ("Lead -> site survey", "15-20%", "28-35%", "Faster, WhatsApp-first follow-up"),
    ("Site survey -> order", "20-25%", "30-35%", "Proof + EMI clarity at survey"),
    ("Cost per installed kW won", "Rs.6,000-9,000", "Rs.3,500-5,500", "Same budget, more installs"),
]

SOLAR_DEFAULT_OUTREACH = [
    ("Subject A (Roast-Audit): your rooftop solar ads leave the ₹78,000 subsidy on the table",
     "Hi,\n\nI spent 30 minutes on your Meta ad library and {website}. I found 3 leaks that are costing you enquiries:\n"
     "1. The ads never lead with PM Surya Ghar subsidy (₹78,000 on a 3 kW) - that is the strongest hook in the market right now.\n"
     "2. CTA goes to a long form instead of click-to-WhatsApp, so 'kitna kharcha hoga?' questions die in the funnel.\n"
     "3. No installation proof - roof photos, net-meter bills, customer video - while competitors show it.\n\n"
     "I have a 2-page confidential audit with the fix for each. Shall I WhatsApp it to you? (1 message, no call.)\n\n- {agency}"),
    ("Subject B (WhatsApp / Loom - 30 sec)",
     "\"Hi {brand} team - I recorded a 3-minute walkthrough of your ad -> landing page -> form flow showing where the site-survey requests are leaking. "
     "Want me to send the link on WhatsApp? You can watch it and decide, no call needed.\""),
    ("Subject C (FOMO): what the top rooftop installers in {city} are doing differently",
     "Hi,\n\nWhile auditing rooftop solar funnels in {city}, I found the fastest-growing installers do 4 things you currently don't:\n"
     "1. Subsidy-first creative (₹78,000 / 300 free units).\n2. Click-to-WhatsApp as primary CTA - not a lead form.\n"
     "3. WhatsApp Business with package catalogue + auto-greeting, so nothing is missed after 6pm.\n"
     "4. Retargeting sequence that runs for 60 days (solar is a 2-3 month decision).\n\n"
     "3 of these can be live in 7 days. Want the 1-page plan?\n\n- {agency}"),
]


def load_from_solar_csv(day: int, row: int) -> dict:
    files = sorted(SOLAR_HISTORY.glob(f"solar-day-{day:02d}-*.csv"))
    if not files:
        raise FileNotFoundError(f"No solar Day {day} CSV in {SOLAR_HISTORY}")
    rows = list(csv.DictReader(open(files[-1], encoding="utf-8")))
    r = rows[row]
    return {
        "brand": r["brand"], "website": r.get("website", ""),
        "instagram": r.get("instagram", ""),
        "niche": SEGMENT_NICHE.get(r.get("segment", "R"), "Solar"),
        "score": int(r.get("score") or 7),
        "ads_active": int(r.get("active_ads") or 0),
        "spend": r.get("spend_est", ""),
        "city": r.get("city", ""), "state": r.get("state", ""),
        "destination": r.get("destination", ""),
        "pitch_fit": r.get("pitch_fit", ""),
        "ad_library_link": r.get("ad_library_link", ""),
        "leak": r.get("leak", ""),
    }


def apply_solar_defaults(lead: dict) -> dict:
    # solar-specific branding line (D2C default stays untouched in audit_pdf.py)
    lead.setdefault("agency_tagline", "Performance Marketing for Rooftop Solar &amp; Solar EPC Brands")
    lead.setdefault("revenue", "Not disclosed (private EPC / installer)")
    lead.setdefault("niche", SEGMENT_NICHE.get(str(lead.get("segment", "R")).upper(), "Rooftop Solar"))
    lead.setdefault("scores", SOLAR_DEFAULT_SCORES)
    lead.setdefault("findings", SOLAR_DEFAULT_FINDINGS)
    lead.setdefault("wins", SOLAR_DEFAULT_WINS)
    lead.setdefault("impact", SOLAR_DEFAULT_IMPACT)
    brand = lead["brand"]
    city = lead.get("city", "your city")
    agency = lead.get("agency_name", "Smart Pursuit")
    lead.setdefault("outreach", [(s.format(website=lead.get("website", ""), brand=brand, city=city, agency=agency),
                                  b.format(website=lead.get("website", ""), brand=brand, city=city, agency=agency))
                                 for s, b in SOLAR_DEFAULT_OUTREACH])
    if "ad_intro" not in lead:
        lead["ad_intro"] = (
            f"<b>{brand}</b> ({lead.get('website','')}) operates in the Indian rooftop solar market, where "
            f"PM Surya Ghar (up to <b>Rs.78,000 subsidy</b> + 300 free units/month) has shifted buyer intent from "
            f"'someday' to 'this quarter'. We reviewed the ad library, the landing page and the enquiry flow.<br/><br/>"
            f"<b>Three leaks stand out:</b> (1) the subsidy - the strongest hook in this category - is not the headline "
            f"of the campaign; (2) the ad CTA pushes to a long form instead of Click-to-WhatsApp, so high-intent "
            f"questions (price, roof area, EMI) are lost; (3) there is almost no installation proof (roof photos, "
            f"net-meter bills, customer video) while solar buyers commit Rs.1.5-3 lakh on trust.<br/><br/>"
            f"All three are fixable inside 7-14 days. <i>Numbers below are estimates from the Ad Library signature - "
            f"verify live counts before quoting them to the client.</i>"
        )
    if "ad_intelligence" not in lead:
        lead["ad_intelligence"] = [
            ("Active platforms", "Meta (FB + IG) primary for residential; Google Search/PMax on 'solar panel price', 'solar subsidy', '<city> solar installer'; IndiaMART/Justdial for lead supply."),
            ("Active ads (est.)", f"~{lead.get('ads_active', 'N/A')} creatives by signature. Verify in Meta Ad Library India (active filter) before pitching."),
            ("Funnel type", f"Primary destination: {lead.get('destination', 'Website / WhatsApp')}. Residential solar benchmarks: WhatsApp or 3-field form beats long forms."),
            ("Seasonality", "Peaks Feb-Jun (summer bills, subsidy push) and Sep-Oct (post-monsoon). Diwali-final-quarter is a strong instalment push."),
            ("Budget signal", f"{lead.get('spend', 'N/A')} estimated monthly. Any installer running 10+ live creatives has budget for a retainer."),
            ("Benchmark to quote", "India solar CPL on Meta: Rs.150-450 residential; qualified site survey Rs.800-1,500; close ~1 in 4-6 surveys."),
        ]
    if "competitors" not in lead:
        lead["competitors"] = [
            ("SolarSquare", "Brand-level trust + financing/EMI messaging + city landing pages", "Show subsidy + EMI math on the first screen"),
            ("Freyr Energy", "Regional EPC proof and service network messaging", "Publish install proof by locality"),
            ("Local MNRE-empanelled installers", "Click-to-WhatsApp + fast quote + Google reviews", "Speed-to-lead under 5 minutes on WhatsApp"),
        ]
    return lead


def main():
    ap = argparse.ArgumentParser(description="Generate a Smart Pursuit SOLAR audit PDF + outreach MD")
    ap.add_argument("json", nargs="?", help="Path to a solar lead JSON")
    ap.add_argument("--day", type=int)
    ap.add_argument("--row", type=int, default=0)
    ap.add_argument("--brand")
    ap.add_argument("--website")
    ap.add_argument("--city", default="")
    ap.add_argument("--segment", default="R")
    ap.add_argument("--ads", type=int, dest="ads_active", default=0)
    ap.add_argument("--score", type=int, default=7)
    a = ap.parse_args()

    if a.json:
        lead = json.loads(Path(a.json).read_text())
    elif a.day is not None:
        lead = load_from_solar_csv(a.day, a.row)
    elif a.brand and a.website:
        lead = {"brand": a.brand, "website": a.website, "city": a.city,
                "segment": a.segment, "ads_active": a.ads_active, "score": a.score,
                "niche": SEGMENT_NICHE.get(a.segment, "Rooftop Solar")}
    else:
        ap.error("Provide a JSON path, --day/--row, or --brand + --website")

    lead = apply_solar_defaults(lead)
    slug = _slug(lead["brand"])
    out_pdf = SOLAR_AUDITS / f"{slug}-solar-audit-report.pdf"
    pdf, md = generate_audit_pdf(lead, out_pdf=out_pdf)
    print(f"Solar audit PDF : {pdf}")
    print(f"Solar outreach  : {md}")
    print(f"Brand           : {lead['brand']} (score {lead.get('score', 7)}/10, {lead.get('pitch_fit', 'fit not set')})")


if __name__ == "__main__":
    main()
