"""
Solar bulk audit generator - all leads in niches/solar/solar-leads-all-50-unique.csv.

For every row produces (solar folders only):
    niches/solar/audits/<slug>-solar-audit-report.pdf
    niches/solar/outreach/<slug>-outreach-templates.md

Each audit is personalized from its CSV row (brand, city, segment, ads,
spend, destination + the lead-specific leak) on top of the solar defaults
in scripts/solar_audit.py. Reuses the Smart Pursuit reportlab engine so
branding/layout stays identical to the D2C audits.

Skips brands in SKIP_REGEN (hand-crafted audits - do not overwrite).

Run:  python scripts/batch/solar_all_audits.py
      python scripts/batch/solar_all_audits.py --force   # regenerate even skipped ones
"""
import csv
import html
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import solar_audit  # noqa: E402
from audit_pdf import generate_audit_pdf, _slug  # noqa: E402

CSV_PATH = ROOT / "niches" / "solar" / "solar-leads-all-50-unique.csv"

# Hand-crafted audits - never overwrite with the bulk generator.
SKIP_REGEN = {"fenice-energy"}

SEGMENT_COMPETITORS = {
    "R": [
        ("Competitor", "What they do better", "Signal"),
        ("SolarSquare", "Subsidy + EMI math on the first screen, city landing pages, brand trust",
         "Show subsidy + EMI math above the fold"),
        ("Freyr Energy", "Regional EPC proof, service-network messaging, SunPro+ app",
         "Publish install proof by locality"),
        ("Local MNRE-empanelled installers", "Click-to-WhatsApp + 5-min quote + Google reviews",
         "Speed-to-lead under 5 minutes on WhatsApp"),
    ],
    "C": [
        ("Competitor", "What they do better", "Signal"),
        ("Loom Solar", "D2C panel/inverter bundles, YouTube demo depth, dealer network",
         "Bundle pricing (panel + inverter + battery) in ad copy"),
        ("UTL Solar", "Price-led D2C funnels with WhatsApp ordering",
         "WhatsApp-first ordering for price shoppers"),
        ("Smarten Power Systems", "Product demo videos + inverter/solar combo offers",
         "Demo video > static poster for consideration"),
    ],
    "B": [
        ("Competitor", "What they do better", "Signal"),
        ("Tata Power Solar", "Brand trust + MW-scale case studies + financing tie-ups",
         "C&I buyers need kW-installed proof, not promises"),
        ("Fourth Partner Energy", "C&I case-study library + RESCO/PPA model clarity",
         "Publish 3 sector case studies (warehouse/school/factory)"),
        ("Amp Energy India", "LinkedIn ABM + facility-head targeting",
         "Add a LinkedIn layer for plant/facility heads"),
    ],
}


def build_lead(row: dict) -> dict:
    brand = row["brand"].strip()
    website = row.get("website", "").strip()
    segment = (row.get("segment", "R") or "R").strip().upper()
    city = row.get("city", "").strip() or "your city"
    state = row.get("state", "").strip()
    ads = row.get("active_ads", "0") or "0"
    spend = row.get("spend_est", "") or "N/A"
    destination = row.get("destination", "") or "Website"
    leak = (row.get("leak", "") or "").strip()
    pitch_fit = row.get("pitch_fit", "").strip()
    try:
        score = int(row.get("score") or 7)
    except ValueonieError:
        score = 7
    try:
        ads_n = int(ads)
    except ValueError:
        ads_n = 0

    niche = solar_audit.SEGMENT_NICHE.get(segment, "Rooftop Solar")
    leak_html = html.escape(leak) if leak else "funnel gaps detailed below"
    seg_line = {
        "R": "residential rooftop (PM Surya Ghar subsidy-driven)",
        "C": "D2C solar products (panels / inverters / batteries)",
        "B": "commercial & industrial rooftop (C&I EPC)",
    }.get(segment, "rooftop solar")

    lead = {
        "brand": brand,
        "website": website,
        "instagram": row.get("instagram", ""),
        "segment": segment,
        "niche": niche,
        "score": score,
        "ads_active": ads_n,
        "spend": spend,
        "city": city,
        "state": state,
        "destination": destination,
        "pitch_fit": pitch_fit,
        "ad_library_link": row.get("ad_library_link", ""),
        "leak": leak,
    }
    lead = solar_audit.apply_solar_defaults(lead)

    # ---- Personalize on top of the solar defaults ----
    lead["ad_intro"] = (
        f"<b>{html.escape(brand)}</b> ({html.escape(website)}) is a {seg_line} advertiser in "
        f"{html.escape(city)}{', ' + html.escape(state) if state else ''}, running an estimated "
        f"<b>~{ads_n} active Meta creatives</b> at ~<b>{html.escape(spend)}/mo</b>, with ads pointing to "
        f"{html.escape(destination)}.<br/><br/>"
        f"<b>Lead-specific flag from the Ad Library scan:</b> {leak_html}.<br/><br/>"
        f"On top of that, the classic solar leaks apply: the PM Surya Ghar subsidy (up to "
        f"<b>Rs.78,000</b> + 300 free units/month) is not the campaign headline, the CTA pushes to a "
        f"long form instead of Click-to-WhatsApp, and installation proof (roof photos, net-meter bills, "
        f"customer video) is thin while buyers commit Rs.1.5-3 lakh on trust.<br/><br/>"
        f"All fixable inside 7-14 days. <i>Ad counts are estimates from the Ad Library signature - "
        f"verify live counts before quoting them to the client.</i>"
    )

    if leak:
        lead["findings"] = [
            f"<b>Verified for {html.escape(brand)}:</b> {leak_html}."
        ] + list(lead["findings"])

    lead["competitors"] = [tuple(r) for r in SEGMENT_COMPETITORS.get(segment, SEGMENT_COMPETITORS["R"])]

    agency = lead.get("agency_name", "Smart Pursuit")
    subj_a, body_a = lead["outreach"][0]
    body_a = body_a + (
        f"\n\nP.S. One flag specific to {brand}: {leak}" if leak else ""
    )
    subj_c, body_c = lead["outreach"][2]
    lead["outreach"] = [
        (f"Subject A (Roast-Audit): {brand} - {leak[:80]}" if leak else subj_a, body_a),
        lead["outreach"][1],
        (subj_c, body_c + f"\n\nRef: {brand} ({website}), {city} - verified in Meta Ad Library India."),
    ]
    return lead


def main() -> None:
    force = "--force" in sys.argv
    if not CSV_PATH.exists():
        raise SystemExit(f"CSV not found: {CSV_PATH}")
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8", newline="")))
    print(f"Loaded {len(rows)} leads from {CSV_PATH.name}")

    done = skipped = failed = 0
    for r in rows:
        brand = (r.get("brand") or "").strip()
        if not brand:
            continue
        slug = _slug(brand)
        out_pdf = solar_audit.SOLAR_AUDITS / f"{slug}-solar-audit-report.pdf"
        if slug in SKIP_REGEN and out_pdf.exists() and not force:
            print(f"SKIP (hand-crafted, use --force to overwrite): {brand}")
            skipped += 1
            continue
        try:
            lead = build_lead(r)
            pdf, md = generate_audit_pdf(lead, out_pdf=out_pdf)
            print(f"OK  {brand:28s} score {lead['score']}/10 -> {Path(pdf).name} | {Path(md).name}")
            done += 1
        except Exception as e:  # noqa: BLE001 - bulk run must continue
            print(f"FAIL {brand}: {e}")
            failed += 1

    print("=" * 64)
    print(f"DONE: {done} generated | {skipped} skipped (hand-crafted) | {failed} failed")
    print(f"PDFs in niches/solar/audits/:     {len(list(solar_audit.SOLAR_AUDITS.glob('*.pdf')))}")
    print(f"MDs  in niches/solar/outreach/:   {len(list(solar_audit.SOLAR_OUTREACH.glob('*.md')))}")


if __name__ == "__main__":
    main()
