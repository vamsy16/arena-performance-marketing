"""Batch-generate lead JSONs for remaining Day-1 leads."""
import csv, json, os, re, sys
import importlib.util
spec = importlib.util.spec_from_file_location("bt", os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "batch_templates.py"))
bt = importlib.util.module_from_spec(spec); spec.loader.exec_module(bt)
NICHES, BRAND_HARD_FACTS, niche_bucket = bt.NICHES, bt.BRAND_HARD_FACTS, bt.niche_bucket

ROOT = "/home/user/arena-performance-marketing"
CSV  = os.path.join(ROOT, "reports/DAY-1-50-LEADS.csv")
OUT  = os.path.join(ROOT, "leads")
DONE = {"Physics Wallah", "boAt", "Mamaearth", "upGrad", "The Derma Co", "Wakefit"}


def parse_spend_cr(s):
    s = s.lower().replace("cr","").replace("rs","").replace("l","").replace("k","").strip()
    if "-" in s:
        a,b = s.split("-")
        try: return (float(a)+float(b))/2
        except: return 3.0
    try: return float(s)
    except: return 3.0


def build_lead(row):
    brand = row["brand"]
    if brand in DONE: return None
    niche = row["niche"]
    ads = int(row["active_ads"])
    spend = row["spend"]
    destination = row["destination"]
    leak = row["leak"]
    ig = row["instagram"]
    website = row["website"]
    score_csv = int(row["score"])
    base_score = {3:8, 5:7, 7:8}.get(score_csv, 7)
    if brand in ("Clove Dental","Minimalist","Boult Audio"): base_score = 7
    if brand in ("Godrej Properties","Prestige Group"): base_score = 8

    bucket = niche_bucket(niche, brand)
    tpl = NICHES[bucket]
    hard = BRAND_HARD_FACTS.get(brand, {})
    revenue = hard.get("revenue", f"Mid-scale D2C brand in the {niche} segment (est. from ad-spend ratios)")
    competitors = hard.get("competitors", [
        ["Key peer 1", "Strong category D2C peer running heavy UGC and SKU-direct routing.", "Creative/CTR gap is the main opening."],
        ["Key peer 2", "Faster-growing challenger with rapid creative velocity.", "Smaller budget winning on sharper creative."],
        ["Legacy/incumbent", "Offline/incumbent brand with trust halo.", "D2C incumbent under-serving online buyers."]
    ])
    top_concerns = hard.get("top_concerns", "hero SKUs across the catalog")
    structure_extra = hard.get("structure_extra", "")

    funnel_type = ("Lead forms + WhatsApp / callback booking primary" if "Lead Form" in destination or "WhatsApp" in destination
                   else "Shopify/hosted D2C website with direct product purchase")
    platforms_row = tpl["platforms_row"]
    if "WhatsApp" in destination:
        platforms_row = platforms_row.replace("Meta (FB+IG) primary;", "Meta (FB+IG) primary with WhatsApp CTA;")

    sp_val = parse_spend_cr(spend)
    if "L" in spend.upper():
        sp_cr = sp_val / 100.0
        waste_low = round(sp_cr*0.25,2)
        waste_high = round(sp_cr*0.40,2)
        waste_unit = "L"
    else:
        sp_cr = sp_val
        waste_low = round(sp_cr*0.25,1)
        waste_high = round(sp_cr*0.40,1)
        waste_unit = "Cr"

    if ads >= 70 and sp_cr >= 1.0:
        heat = "HOT - high ad volume, mature spend, clear creative/CRO leaks"
    elif ads >= 50:
        heat = "WARM - solid spend with obvious quick wins in creative/CRO"
    else:
        heat = "NURTURE - smaller budget with high-ROI quick fixes"
    if base_score >= 8:
        heat = heat.replace("NURTURE","WARM").replace("WARM","HOT")

    # Build findings
    findings_sev = ["High","High","Medium","Medium"]
    offer_hint = "percentage-off promotions"
    if "75% off" in leak: offer_hint = "flat 75% off"
    elif "50% off" in leak: offer_hint = "up to 50% off"
    elif "249" in leak: offer_hint = "Rs.249 price anchors"
    elif "free" in leak.lower(): offer_hint = "free-gift / giveaway hooks"
    elif "static" in leak.lower(): offer_hint = "product static beauty shots"
    findings = []
    for i,(title,body) in enumerate(tpl["finding_templates"][:4]):
        body = body.replace("{offer}", offer_hint)
        findings.append(f"<b>{title} ({findings_sev[i]}):</b> {body}")
    if leak and leak != "N/A":
        findings[0] = f"<b>Observed signal:</b> {leak}. " + findings[0]

    wins = [list(w) for w in tpl["wins"]]
    impact = [["Metric","Current (est.)","After Wins","Impact"]]
    for r in tpl["impact"]:
        impact.append(list(r))
    if waste_unit == "Cr":
        impact.append(["Ad Spend Wastage", "~30-45%", "~12-18%", f"Saves ~Rs.{waste_low}-{waste_high} Cr/mo"])
    else:
        impact.append(["Ad Spend Wastage", "~30-40%", "~12-18%", f"Saves ~Rs.{int(waste_low*100)}-{int(waste_high*100)} L/mo"])

    ad_intelligence = [
        ["Active platforms", platforms_row],
        ["Active ads count", f"~{ads} live creatives across {top_concerns}."],
        ["Duration signals", tpl["duration"]],
        ["Funnel type", funnel_type],
        ["Budget signal", f"Estimated ~Rs.{spend}/mo ad spend ({bucket.replace('_',' ')} vertical; ~{ads} live ads = {'top/mid-tier' if ads>=50 else 'emerging'} spender in the segment)."],
        ["Campaign structure", tpl["structure_tpl"].format(top_concerns=top_concerns) + (f" {structure_extra}" if structure_extra else "")],
    ]
    scores = {}
    for (label, s) in tpl["score_profile"]:
        color = "#EF4444" if s <= 3 else ("#F59E0B" if s <= 5 else "#10B981")
        scores[label] = [s, color]

    waste_str = f"Rs.{waste_low}-{waste_high} {waste_unit}/mo"
    peer1 = competitors[0][0] if competitors else "key competitor"
    peer2 = competitors[1][0] if len(competitors)>1 else "peers"

    ad_intro = (
        f"{brand} ({website}, Instagram: {ig}) is a prominent Indian {niche.lower()} brand with "
        f"<b>~{ads} active creatives</b> running across Meta in India, spending an estimated "
        f"<b>Rs.{spend}/mo</b>. {revenue}. Three obvious leaks in the funnel:<br/><br/>"
        f"<b>(1) Creative gap</b> - heavy studio/offer creative with thin real-customer UGC, before/after or demo content. "
        f"<b>(2) Copy/CRO gap</b> - headlines lead with price/offer rather than outcome, and ad traffic often lands on collections/offer pages rather than the exact SKU. "
        f"<b>(3) Tracking/retargeting gap</b> - retargeting uses generic creative rather than staged, funnel-matched content; CAPI/return-event wiring is inconsistent. "
        f"These are fixable in 7-14 days. We estimate <b>30-45% of ad spend is leaking</b>; {heat}."
    )

    outreach = [
        [f"Subject A (Roast-Audit): I counted {ads} {brand} ads - 3 leaks costing ~{waste_str}",
         f"Hi {{first_name}},<br/><br/>I went through {website} plus your Meta Ad Library this week. You are running <b>~{ads} ads</b> across {top_concerns} at what looks like Rs.{spend} on Meta. Three leaks are costing an estimated <b>~{waste_str}</b>:<br/><br/>1. <b>Creative is studio/offer-heavy and UGC-thin</b> - real customer before/after, demo, and testimonial Reels are thin, even though UGC outperforms studio creative in {niche.lower()}.<br/>2. <b>Landing/CRO</b> - ad traffic often lands on collections/offer pages rather than the exact SKU; key trust/CTA elements sit below the fold.<br/>3. <b>Retargeting is generic</b> - creative doesn't vary by funnel depth, and CAPI event quality varies.<br/><br/>I put together a 2-page branded audit with screenshots, competitor benchmarks vs {peer1}/{peer2}, and three quick wins (7/10/14 days). Open to sharing it?<br/><br/>Best,<br/>Smart Pursuit | Ph: 7095024220 | smartpursuit3@gmail.com"],
        ["Subject B (Loom Script - 30 sec):",
         f"\"Hey - I recorded a 3-minute screen recording going through your top-spend {brand} creatives on Meta. Three things jumped out: (1) creative is heavy on studio/offer shots and thin on real-customer UGC, (2) ad traffic often lands on collections/offer pages rather than the exact SKU, and (3) retargeting uses generic creative instead of being staged by funnel depth. I have a 2-page audit with 3 quick wins - can I send it over?\"<br/><br/>Best,<br/>Smart Pursuit"],
        [f"Subject C (FOMO): {peer1} is scaling on UGC - {brand} is still leading with offers",
         f"Hi {{first_name}},<br/><br/>{peer1} is scaling hard in {niche.lower()} with UGC-first creative and SKU-direct routing. {brand} has the stronger brand and broader assortment but your Meta creative is still offer/studio-led. The gap is UGC + SKU-direct CRO + staged retargeting, not budget. I put together a 14-day test plan with predicted ROAS lift. Open to sending it over?<br/><br/>Best,<br/>Smart Pursuit | Ph: 7095024220 | smartpursuit3@gmail.com"]
    ]

    return {
        "brand": brand,
        "website": website,
        "instagram": ig,
        "niche": niche,
        "score": base_score,
        "ads_active": ads,
        "spend": f"Rs.{spend}/mo",
        "revenue": revenue,
        "destination": destination + " - " + funnel_type,
        "ad_library_link": row["ad_library_link"],
        "ad_intro": ad_intro,
        "ad_intelligence": ad_intelligence,
        "scores": scores,
        "findings": findings,
        "competitors": [["Competitor","What they do better",f"Signal for {brand}"]] + competitors,
        "wins": wins,
        "impact": impact,
        "outreach": outreach,
        "_heat": heat
    }


with open(CSV) as f:
    rows = list(csv.DictReader(f))

generated = []
for row in rows:
    lead = build_lead(row)
    if lead is None: continue
    slug = re.sub(r"[^a-z0-9]+","-", lead["brand"].lower()).strip("-")
    out_path = os.path.join(OUT, f"{slug}.json")
    with open(out_path, "w") as f:
        json.dump(lead, f, indent=2, ensure_ascii=True)
    generated.append(lead["brand"])

print(f"Generated {len(generated)} lead JSONs:")
for b in generated: print(f"  - {b}")
