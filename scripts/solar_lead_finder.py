#!/usr/bin/env python3
"""
SOLAR vertical lead finder - isolated from the D2C pipeline.

WHY THIS FILE EXISTS
--------------------
The D2C system (scripts/auto_lead_finder_v3_dedup.py) writes to:
    data/seen_leads.json
    data/daily_history/*.csv
    leads-all-<N>-unique.csv

This solar runner NEVER touches those files. It writes only to:
    niches/solar/data/seen_leads.json
    niches/solar/data/daily_history/*.csv
    niches/solar/leads-all-<N>-unique.csv

So you can run D2C (Day 4, Day 5, ... Day 50) and Solar (Day 1, Day 2, ...)
in parallel with zero cross-contamination and zero duplicate-suppression clashes.

USAGE
-----
  python scripts/solar_lead_finder.py --count 50 --day 1
  python scripts/solar_lead_finder.py --count 50 --day 2
  python scripts/solar_lead_finder.py --count 30 --day 3 --segment R      # residential EPC only
  python scripts/solar_lead_finder.py --count 30 --day 3 --segment C      # D2C solar products
  python scripts/solar_lead_finder.py --count 25 --day 3 --state Karnataka
  python scripts/solar_lead_finder.py --stats
  python scripts/solar_lead_finder.py --reset                              # solar only

SEGMENTS
--------
  R = Residential rooftop EPC / installer (highest volume of small spenders)
  C = D2C solar products (panels, inverters, batteries, solar water heaters)
  B = B2B / C&I / industrial & commercial rooftop EPC (bigger ticket, longer cycle)
  P = Channel partner / marketplace / aggregator (leads sold to installers)
"""

import argparse
import csv
import json
import random
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOLAR_DIR = ROOT / "niches" / "solar"
SEEN_FILE = SOLAR_DIR / "data" / "seen_leads.json"
HISTORY_DIR = SOLAR_DIR / "data" / "daily_history"
LEADS_DIR = SOLAR_DIR / "leads"
for d in (SEEN_FILE.parent, HISTORY_DIR, LEADS_DIR):
    d.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------------------------------
# 1. REAL SEED - named Indian solar companies that are known advertisers or
#    known solar spenders. `data_source=seed-real` means the COMPANY is real;
#    the ad counts are ESTIMATES and must be verified in Meta Ad Library /
#    Google Ads Transparency before you pitch. Never quote an unverified number.
# --------------------------------------------------------------------------
SEED_REAL = [
    # --- R: residential rooftop EPC / installer brands ---
    ("SolarSquare", "solarsquare.in", "@solarsquare_india", "R", "Mumbai", "Maharashtra", "3-10 kW"),
    ("Freyr Energy", "freyrenergy.com", "@freyr_energy", "R", "Hyderabad", "Telangana", "3-10 kW"),
    ("ZunRoof", "zunroof.com", "@zunroof", "R", "Gurugram", "Haryana", "2-10 kW"),
    ("Oorjan Cleantech", "oorjan.com", "@oorjan_cleantech", "R", "Mumbai", "Maharashtra", "3-10 kW"),
    ("Fenice Energy", "feniceenergy.com", "@feniceenergy", "R", "Chennai", "Tamil Nadu", "3-5 kW"),
    ("MYSUN", "mysun.co", "@mysunindia", "R", "New Delhi", "Delhi", "3-10 kW"),
    ("Arka Energy", "arkaenergy.com", "@arkaenergy", "R", "Bengaluru", "Karnataka", "3-10 kW"),
    ("Gensol Engineering", "gensol.in", "@gensolengineering", "B", "Ahmedabad", "Gujarat", "10 kW-1 MW"),
    ("Sunlit Future", "sunlitfuture.com", "@sunlitfuture", "R", "Auroville", "Tamil Nadu", "1-10 kW"),
    ("Swelect Energy Systems", "swelect.com", "@swelectenergy", "C", "Chennai", "Tamil Nadu", "1-100 kW"),
    ("Emmvee Solar", "emmvee.com", "@emmveesolar", "C", "Bengaluru", "Karnataka", "1-100 kW"),
    ("Fourth Partner Energy", "fourthpartner.co", "@fourthpartnerenergy", "B", "Hyderabad", "Telangana", "50 kW-5 MW"),
    ("CleanMax Solar", "cleanmax.com", "@cleanmax_solar", "B", "Mumbai", "Maharashtra", "100 kW-10 MW"),
    ("Amplus Solar", "amplussolar.com", "@amplus.solar", "B", "Gurugram", "Haryana", "100 kW-10 MW"),
    ("Sunsure Energy", "sunsureenergy.com", "@sunsureenergy", "B", "New Delhi", "Delhi", "100 kW-10 MW"),
    ("SunSource Energy", "sunsourceenergy.com", "@sunsourceenergy", "B", "Noida", "Uttar Pradesh", "100 kW-10 MW"),
    ("Mahindra Susten", "mahindrasusten.com", "@mahindra_susten", "B", "Mumbai", "Maharashtra", "1 MW+"),
    ("Amp Energy India", "ampenergyindia.com", "@ampenergyindia", "B", "New Delhi", "Delhi", "1 MW+"),
    ("Radiance Renewables", "radiancerenewables.com", "@radiance_renewables", "B", "Mumbai", "Maharashtra", "1 MW+"),
    ("Hero Future Energies", "herofutureenergies.com", "@herofutureenergies", "B", "New Delhi", "Delhi", "1 MW+"),
    ("Ayana Renewable Power", "ayanarenewable.com", "@ayanarenewable", "B", "Bengaluru", "Karnataka", "1 MW+"),

    # --- C: D2C / retail solar products (panels, inverters, batteries, heaters) ---
    ("Loom Solar", "loomsolar.com", "@loomsolar", "C", "Faridabad", "Haryana", "1-10 kW"),
    ("Smarten Power Systems", "smarten.in", "@smartensolar", "C", "Gurugram", "Haryana", "1-10 kW"),
    ("UTL Solar", "utlsolar.com", "@utlsolar", "C", "New Delhi", "Delhi", "1-10 kW"),
    ("Su-Kam Power Systems", "sukam.com", "@sukampower", "C", "Gurugram", "Haryana", "1-10 kW"),
    ("Livguard Solar", "livguard.com", "@livguard", "C", "Gurugram", "Haryana", "1-10 kW"),
    ("Microtek Solar", "microtekdirect.com", "@microtek_india", "C", "New Delhi", "Delhi", "1-10 kW"),
    ("Luminous Solar", "luminousindia.com", "@luminousindia", "C", "Gurugram", "Haryana", "1-10 kW"),
    ("Exide Solar", "exideindustries.com", "@exideindustries", "C", "Kolkata", "West Bengal", "1-10 kW"),
    ("Okaya Power", "okaya.co.in", "@okayapower", "C", "New Delhi", "Delhi", "1-10 kW"),
    ("Nuetech Solar", "nuetechsolar.com", "@nuetechsolar", "C", "Bengaluru", "Karnataka", "solar water heater"),
    ("Sudarshan Saur", "sudarshansaur.com", "@sudarshansaur", "C", "Pune", "Maharashtra", "solar water heater"),
    ("Racold Solar", "racold.com", "@racoldindia", "C", "Mumbai", "Maharashtra", "solar water heater"),
    ("V-Guard Solar", "vguard.in", "@vguardindia", "C", "Kochi", "Kerala", "1-10 kW"),
    ("Solar Universe India", "solaruniverseindia.com", "@solaruniverseindia", "C", "New Delhi", "Delhi", "1-10 kW"),
    ("SolarClue", "solarclue.com", "@solarclue", "P", "Jaipur", "Rajasthan", "marketplace"),

    # --- Module / cell / inverter manufacturers who also run rooftop channels ---
    ("Tata Power Solar", "tatapowersolar.com", "@tatapowersolar", "B", "Bengaluru", "Karnataka", "all"),
    ("Adani Solar", "adanisolar.com", "@adanisolar", "B", "Ahmedabad", "Gujarat", "all"),
    ("Waaree Energies", "waaree.com", "@waareeenergies", "B", "Mumbai", "Maharashtra", "all"),
    ("Vikram Solar", "vikramsolar.com", "@vikramsolar", "B", "Kolkata", "West Bengal", "all"),
    ("Servotech Renewable", "servotechindia.com", "@servotechindia", "B", "New Delhi", "Delhi", "all"),
    ("Goldi Solar", "goldisolar.com", "@goldisolar", "B", "Surat", "Gujarat", "all"),
    ("RenewSys India", "renewsys.com", "@renewsys", "B", "Bengaluru", "Karnataka", "all"),
    ("Premier Energies", "premierenergies.in", "@premierenergies", "B", "Hyderabad", "Telangana", "all"),
    ("Rayzon Solar", "rayzonsolar.com", "@rayzonsolar", "B", "Surat", "Gujarat", "all"),
    ("Jakson Solar", "jaksonsolar.com", "@jakson_solar", "B", "Noida", "Uttar Pradesh", "all"),
    ("Gautam Solar", "gautamsolar.com", "@gautamsolar", "B", "New Delhi", "Delhi", "all"),
    ("Insolation Energy", "insolationenergy.in", "@insolationenergy", "B", "Jaipur", "Rajasthan", "all"),
    ("Navitas Solar", "navitassolar.in", "@navitassolar", "B", "Surat", "Gujarat", "all"),
    ("Solex Energy", "solexenergy.com", "@solexenergy", "B", "Surat", "Gujarat", "all"),
    ("Shakti Pumps Solar", "shaktipumps.com", "@shaktipumps", "B", "Pithampur", "Madhya Pradesh", "solar pump"),
    ("CRI Pumps Solar", "cripumps.com", "@cripumps", "B", "Coimbatore", "Tamil Nadu", "solar pump"),
    ("Sungrow India", "sungrowpower.com", "@sungrow", "B", "Bengaluru", "Karnataka", "inverters"),
]

# --------------------------------------------------------------------------
# 2. POOL GENERATOR - fills out regional capacity so 50/day x 40 days is
#    mathematically possible while you replace these with real Ad Library
#    pulls. data_source=pool-placeholder => the NAME IS A PLACEHOLDER.
#    Replace it before outreach. The scoring/fields are what matter here.
# --------------------------------------------------------------------------
CITY_STATE = [
    ("Mumbai", "Maharashtra"), ("Pune", "Maharashtra"), ("Nashik", "Maharashtra"),
    ("Nagpur", "Maharashtra"), ("Thane", "Maharashtra"), ("Kolhapur", "Maharashtra"),
    ("Aurangabad", "Maharashtra"), ("New Delhi", "Delhi"), ("Gurugram", "Haryana"),
    ("Noida", "Uttar Pradesh"), ("Ghaziabad", "Uttar Pradesh"), ("Faridabad", "Haryana"),
    ("Jaipur", "Rajasthan"), ("Jodhpur", "Rajasthan"), ("Udaipur", "Rajasthan"),
    ("Kota", "Rajasthan"), ("Ahmedabad", "Gujarat"), ("Surat", "Gujarat"),
    ("Vadodara", "Gujarat"), ("Rajkot", "Gujarat"), ("Bhavnagar", "Gujarat"),
    ("Bengaluru", "Karnataka"), ("Mysuru", "Karnataka"), ("Hubballi", "Karnataka"),
    ("Mangaluru", "Karnataka"), ("Hyderabad", "Telangana"), ("Warangal", "Telangana"),
    ("Vijayawada", "Andhra Pradesh"), ("Visakhapatnam", "Andhra Pradesh"),
    ("Chennai", "Tamil Nadu"), ("Coimbatore", "Tamil Nadu"), ("Madurai", "Tamil Nadu"),
    ("Salem", "Tamil Nadu"), ("Tiruchirappalli", "Tamil Nadu"), ("Kochi", "Kerala"),
    ("Thiruvananthapuram", "Kerala"), ("Kozhikode", "Kerala"), ("Kolkata", "West Bengal"),
    ("Siliguri", "West Bengal"), ("Patna", "Bihar"), ("Muzaffarpur", "Bihar"),
    ("Lucknow", "Uttar Pradesh"), ("Kanpur", "Uttar Pradesh"), ("Varanasi", "Uttar Pradesh"),
    ("Bareilly", "Uttar Pradesh"), ("Indore", "Madhya Pradesh"), ("Bhopal", "Madhya Pradesh"),
    ("Jabalpur", "Madhya Pradesh"), ("Gwalior", "Madhya Pradesh"), ("Raipur", "Chhattisgarh"),
    ("Bhubaneswar", "Odisha"), ("Cuttack", "Odisha"), ("Guwahati", "Assam"),
    ("Chandigarh", "Chandigarh"), ("Ludhiana", "Punjab"), ("Amritsar", "Punjab"),
    ("Jalandhar", "Punjab"), ("Dehradun", "Uttarakhand"), ("Panaji", "Goa"),
    ("Ranchi", "Jharkhand"), ("Jammu", "Jammu & Kashmir"), ("Srinagar", "Jammu & Kashmir"),
]

NAME_PATTERNS = [
    "{city} Solar Solutions", "{city} Solar Power", "{city} Green Energy",
    "{city} Solar EPC", "{city} Rooftop Solar", "Shree Surya Solar {city}",
    "Surya Urja {city}", "GreenGhar Solar {city}", "Urja Solar {city}",
    "SolarSetu {city}", "WattSaver Solar {city}", "SunGhar Energy {city}",
    "SolarYatra {city}", "Rooftop Mitra {city}", "NexGen Solar {city}",
    "EcoWatt Solar {city}", "SolTech {city}", "KilowattKart {city}",
    "{city} Solar Mart", "Aditya Solar {city}", "Bharat Solar {city}",
    "SunShakti Energy {city}", "PowerGhar Solar {city}", "SolarSewa {city}",
    "{city} Solar Care", "GreenVolt Solar {city}", "SunRise Solartech {city}",
    "Aarambh Solar {city}", "SunKranti Energy {city}", "SolarDhruv {city}",
]

LEAKS_R = [
    "Ad CTA goes to homepage, not a subsidy calculator / 3-field quote form",
    "No WhatsApp click-to-chat on ads - loses 40%+ of inbound",
    "Zero installation video / customer testimonial in creatives",
    "No EMI or subsidy explainer above the fold",
    "Form asks 8+ fields (bill amount, roof area, phone, email, address) - drop-off",
    "Google reviews strong but not shown in creatives",
    "No retargeting sequence for people who filled half the form",
    "Owned by one founder page - no dedicated solar brand page, thin social proof",
    "Runs generic 'Save electricity' ads - no PM Surya Ghar subsidy hook",
    "Landing page loads 4s+ on mobile 4G",
    "Static poster creatives only - stock images, no roof before/after",
    "No lead-capture before 'Check my savings' calculator (traffic wasted)",
    "No Google Business Profile posts for local pack",
    "Uses shared WhatsApp number - no auto-greeting, no catalogue of packages",
]
LEAKS_C = [
    "No bundle pricing (panel + inverter + battery) in ad copy",
    "Product page has no subsidy eligibility note for residential buyers",
    "Zero UGC / unboxing reels - all studio product shots",
    "No COD / EMI visibility in ads",
    "Catalogue not in WhatsApp Business - buyers ask price in DMs manually",
    "No retargeting for cart abandoners (solar products have 30-60 day cycle)",
    "Shipping/delivery timeline hidden - key objection unanswered",
    "Amazon/Flipkart listings not linked from ads (trust gap)",
]
LEAKS_B = [
    "Zero case-study / kW-installed proof in ads - C&I buyers need references",
    "No ROI / payback calculator gated behind form on site",
    "No LinkedIn ABM layer while running broad Meta",
    "No case-study PDF or site-survey scheduler for facility heads",
    "Ads target homeowners while also bidding on C&I keywords - wasted budget",
]
DESTINATIONS = ["WhatsApp", "Website", "Lead Form", "Phone Call"]

EST_ADS = {"R": (0, 28), "C": (0, 45), "B": (0, 60), "P": (0, 20)}


def _slug_site(name: str, city: str) -> str:
    s = "".join(ch for ch in name.lower() if ch.isalnum() or ch == " ").strip()
    s = s.replace(" ", "")
    city_slug = city.lower().replace(" ", "")
    return f"{s[:22]}.in" if city_slug in s else f"{s[:18]}{city_slug[:8]}.in"


EXTRA_POOL_FILE = SOLAR_DIR / "data" / "real_pool.csv"


def load_extra_pool():
    """Real leads YOU find in Meta Ad Library / Google Maps go here.
    niches/solar/data/real_pool.csv with header:
      brand,website,instagram,segment,city,state,capacity,active_ads,destination,spend_est,leak
    Rows are treated as real (never placeholder) and are served FIRST in each day's run.
    """
    rows = []
    if not EXTRA_POOL_FILE.exists():
        return rows
    with open(EXTRA_POOL_FILE, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r.get("brand"):
                continue
            rows.append({
                "brand": r["brand"].strip(),
                "website": r.get("website", "").strip(),
                "instagram": r.get("instagram", "").strip(),
                "segment": (r.get("segment") or "R").strip().upper()[:1],
                "city": r.get("city", "").strip(),
                "state": r.get("state", "").strip(),
                "capacity": r.get("capacity", "").strip(),
                "active_ads": int(r.get("active_ads") or 0),
                "destination": r.get("destination", "WhatsApp").strip(),
                "spend_est": r.get("spend_est", "").strip(),
                "leak": r.get("leak", "Verify funnel manually").strip(),
                "data_source": "real-pool",
                "verify": "you added this - verified by you",
            })
    return rows


def build_pool(seed: int = 20260914):
    rng = random.Random(seed)
    pool = load_extra_pool()

    # 1) real seed rows
    for brand, site, ig, seg, city, state, kva in SEED_REAL:
        pool.append({
            "brand": brand, "website": site, "instagram": ig, "segment": seg,
            "city": city, "state": state, "capacity": kva,
            "active_ads": rng.randint(*EST_ADS[seg]),
            "destination": rng.choice(DESTINATIONS),
            "spend_est": rng.choice(["<1L/mo", "1-3L/mo", "3-8L/mo", "8-20L/mo", "20L+/mo"]),
            "leak": rng.choice(LEAKS_R if seg == "R" else LEAKS_C if seg == "C" else LEAKS_B),
            "data_source": "seed-real",
            "verify": "check Meta Ad Library before outreach",
        })

    # 2) regional placeholder pool (capacity only - replace with real pulls)
    for city, state in CITY_STATE:
        patterns = rng.sample(NAME_PATTERNS, k=min(9, len(NAME_PATTERNS)))
        for pat in patterns:
            name = pat.format(city=city)
            seg = rng.choices(["R", "C", "B", "P"], weights=[62, 16, 16, 6])[0]
            pool.append({
                "brand": name,
                "website": _slug_site(name, city),
                "instagram": "@" + "".join(ch for ch in name.lower() if ch.isalnum())[:18],
                "segment": seg,
                "city": city,
                "state": state,
                "capacity": rng.choice(["1-3 kW", "3-5 kW", "5-10 kW", "10-50 kW", "50-100 kW"]),
                "active_ads": rng.randint(*EST_ADS[seg]),
                "destination": rng.choice(DESTINATIONS),
                "spend_est": rng.choice(["<50k/mo", "50k-1L/mo", "1-3L/mo", "3-8L/mo"]),
                "leak": rng.choice(LEAKS_R if seg == "R" else LEAKS_C if seg == "C" else LEAKS_B),
                "data_source": "pool-placeholder",
                "verify": "PLACEHOLDER name - replace with a real Ad Library advertiser",
            })

    # dedupe by brand name
    seen, out = set(), []
    for row in pool:
        if row["brand"] in seen:
            continue
        seen.add(row["brand"])
        out.append(row)
    return out


# Brands with in-house marketing teams / procurement-driven sales. A cold
# "we found 3 leaks" DM will not land here - listed so you don't waste a day.
ENTERPRISE = {
    "Tata Power Solar", "Adani Solar", "Waaree Energies", "Vikram Solar",
    "CleanMax Solar", "Mahindra Susten", "Amp Energy India", "Radiance Renewables",
    "Hero Future Energies", "Ayana Renewable Power", "Fourth Partner Energy",
    "Amplus Solar", "RenewSys India", "Premier Energies", "Sungrow India",
    "Exide Solar", "Luminous Solar", "Racold Solar", "Loom Solar", "Livguard Solar",
}


def pitch_fit(lead) -> str:
    b = lead["brand"]
    if b in ENTERPRISE:
        return "LOW - in-house team, do not cold pitch"
    if lead["segment"] == "R":
        return "HIGH - owner-led local EPC, lead volume = revenue, fast reply"
    if lead["segment"] == "C":
        return "HIGH - D2C performance-led, judges you on CPL/ROAS"
    if lead["segment"] == "P":
        return "MEDIUM - marketplace, wants cheaper lead supply"
    return "MEDIUM - C&I, longer cycle, needs case-study + ABM angle"


SEGMENT_LABEL = {
    "R": "Residential rooftop EPC",
    "C": "D2C solar products",
    "B": "B2B / C&I rooftop EPC",
    "P": "Channel partner / marketplace",
}


def load_seen():
    if SEEN_FILE.exists():
        return json.loads(SEEN_FILE.read_text())
    return {"brands": {}, "total_found": 0, "daily_log": [], "vertical": "solar"}


def save_seen(data):
    data["vertical"] = "solar"
    SEEN_FILE.write_text(json.dumps(data, indent=2))


def score_lead(lead):
    """Solar-specific scoring. Different from D2C: subsidy angle + WhatsApp +
    capacity value matter more than raw ad count."""
    s = 0
    if lead["destination"] in ("WhatsApp", "Lead Form"):
        s += 2
    if lead["active_ads"] >= 5:
        s += 2
    if lead["active_ads"] >= 15:
        s += 1
    low = lead["leak"].lower()
    if "whatsapp" in low or "subsidy" in low or "ugc" in low:
        s += 2
    if "video" in low or "testimonial" in low:
        s += 1
    if lead["segment"] in ("C", "R"):
        s += 1
    if "10-50" in lead["capacity"] or "50-100" in lead["capacity"] or "kW-1 MW" in lead["capacity"]:
        s += 1
    if lead["data_source"] in ("seed-real", "real-pool"):
        s += 1
    return max(1, min(10, s))


def find_new_leads(count=50, day=1, segment="ALL", state="ALL"):
    pool = build_pool()
    seen_data = load_seen()
    seen = set(seen_data["brands"].keys())

    print(f"SOLAR | Day {day} | Target: {count} NEW unique leads")
    print(f"Already seen in solar DB: {len(seen)} brands")
    print(f"Solar pool size: {len(pool)} (seed-real + regional placeholders)")

    available = [l for l in pool if l["brand"] not in seen]
    if segment != "ALL":
        available = [l for l in available if l["segment"] == segment.upper()]
    if state != "ALL":
        available = [l for l in available if l["state"].lower() == state.lower()]

    if len(available) < count:
        print(f"WARNING: only {len(available)} rows match this filter.")

    random.shuffle(available)
    # keep real seed rows well represented: sort them first, then fill
    reals = [l for l in available if l["data_source"] == "real-pool"] + \
            [l for l in available if l["data_source"] == "seed-real"]
    placeholders = [l for l in available if l["data_source"] != "seed-real"]
    new_leads = (reals + placeholders)[:count]

    for lead in new_leads:
        lead["score"] = score_lead(lead)
        q = lead["brand"].replace(" ", "+")
        lead["ad_library_link"] = (
            "https://www.facebook.com/ads/library/?active_status=active&ad_type=all"
            f"&country=IN&search_type=keyword_unordered&q={q}"
        )
        lead["google_ads_link"] = f"https://adstransparency.google.com/?region=IN&domain={lead['website']}"
        lead["pm_surya_ghar_vendor_check"] = "https://pmsuryaghar.gov.in/ (verify empanelled vendor status)"
        lead["pitch_fit"] = pitch_fit(lead)
        lead["found_at"] = datetime.now().isoformat()
        lead["day_found"] = day

        seen_data["brands"][lead["brand"]] = {
            "first_seen": datetime.now().isoformat(),
            "day": day,
            "city": lead["city"],
            "state": lead["state"],
            "segment": lead["segment"],
        }
        # rich per-lead json for the audit step
        (LEADS_DIR / f"{lead['brand'].lower().replace(' ', '-')}.json").write_text(
            json.dumps({k: v for k, v in lead.items()}, indent=2)
        )

    seen_data["total_found"] += len(new_leads)
    seen_data["daily_log"].append({
        "day": day,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "count": len(new_leads),
        "total_so_far": seen_data["total_found"],
        "segment_filter": segment,
        "state_filter": state,
        "brands": [l["brand"] for l in new_leads],
    })
    save_seen(seen_data)

    fields = ["brand", "website", "instagram", "segment", "segment_label", "city", "state",
              "capacity", "active_ads", "destination", "spend_est", "score", "pitch_fit", "leak",
              "ad_library_link", "google_ads_link", "pm_surya_ghar_vendor_check",
              "data_source", "verify", "day_found", "found_at"]
    rows = []
    for l in new_leads:
        r = dict(l)
        r["segment_label"] = SEGMENT_LABEL.get(l["segment"], l["segment"])
        rows.append({k: r.get(k, "") for k in fields})

    csv_path = HISTORY_DIR / f"solar-day-{day:02d}-{datetime.now().strftime('%Y-%m-%d')}-{len(rows)}-leads.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    # combined solar CSV (own file, never the D2C one)
    all_rows = []
    for log in seen_data["daily_log"]:
        f_ = HISTORY_DIR / f"solar-day-{log['day']:02d}-{log['date']}-{log['count']}-leads.csv"
        if f_.exists():
            all_rows.extend(list(csv.DictReader(open(f_, encoding="utf-8"))))
    combined = SOLAR_DIR / f"solar-leads-all-{seen_data['total_found']}-unique.csv"
    if all_rows:
        with open(combined, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=all_rows[0].keys())
            w.writeheader()
            w.writerows(all_rows)

    print(f"\nDay {day}: {len(new_leads)} new solar leads (0 duplicates across {len(seen)} seen brands)")
    print(f"Daily CSV : {csv_path}")
    print(f"Combined  : {combined}")
    print(f"Lead JSONs: {LEADS_DIR}/ (feed these to scripts/solar_audit.py)")
    hot = [l for l in new_leads if l["score"] >= 8]
    print(f"HOT leads today (8-10): {len(hot)}")
    print("\nTop 5 today:")
    for l in sorted(new_leads, key=lambda x: x["score"], reverse=True)[:5]:
        print(f"  - {l['brand']} | {SEGMENT_LABEL[l['segment']]} | {l['city']}, {l['state']}"
              f" | ads~{l['active_ads']} | {l['destination']} | score {l['score']}")

    real_ct = sum(1 for l in new_leads if l["data_source"] in ("seed-real", "real-pool"))
    print(f"\nData quality: {real_ct} real named companies, {len(new_leads)-real_ct} pool placeholders.")
    print("  -> Send outreach ONLY to rows you have verified live in Meta Ad Library.")
    return new_leads


def show_stats():
    d = load_seen()
    print("\nSOLAR VERTICAL - DEDUP STATS (isolated from D2C)")
    print(f"Total unique solar brands: {d['total_found']}")
    print(f"Days run: {len(d['daily_log'])}")
    for log in d["daily_log"][-10:]:
        print(f"  Solar Day {log['day']} ({log['date']}): {log['count']} leads"
              f" | segment={log.get('segment_filter','ALL')} state={log.get('state_filter','ALL')}")
    if SEEN_FILE.exists():
        print(f"\nSolar seen file: {SEEN_FILE} ({SEEN_FILE.stat().st_size/1024:.1f} KB)")
    d2c = ROOT / "data" / "seen_leads.json"
    if d2c.exists():
        try:
            n = json.loads(d2c.read_text()).get("total_found", 0)
            print(f"D2C seen file (untouched): {d2c} ({n} brands)")
        except Exception:
            pass
    print(f"History dir: {HISTORY_DIR} ({len(list(HISTORY_DIR.glob('*.csv')))} files)")
    seg_counts = {}
    for v in d["brands"].values():
        seg_counts[v["segment"]] = seg_counts.get(v["segment"], 0) + 1
    if seg_counts:
        print("Segment split:", ", ".join(f"{SEGMENT_LABEL.get(k,k)}={v}" for k, v in sorted(seg_counts.items())))


def reset_solar():
    if SEEN_FILE.exists():
        SEEN_FILE.unlink()
    for f in HISTORY_DIR.glob("solar-day-*.csv"):
        f.unlink()
    for f in SOLAR_DIR.glob("solar-leads-all-*-unique.csv"):
        f.unlink()
    print("Solar reset done. D2C data/seen_leads.json was NOT touched.")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Solar vertical lead finder - isolated from the D2C pipeline")
    p.add_argument("--count", type=int, default=50)
    p.add_argument("--day", type=int, default=1)
    p.add_argument("--segment", default="ALL", help="ALL | R | C | B | P")
    p.add_argument("--state", default="ALL", help="e.g. Karnataka, Gujarat")
    p.add_argument("--stats", action="store_true")
    p.add_argument("--reset", action="store_true")
    a = p.parse_args()

    if a.stats:
        show_stats()
    elif a.reset:
        reset_solar()
    else:
        find_new_leads(count=a.count, day=a.day, segment=a.segment, state=a.state)
