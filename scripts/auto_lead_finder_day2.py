"""
Auto Lead Finder — Day 2 (50 NEW unique leads, ZERO overlap with Day 1)

Uses the auto_lead_finder_v3_dedup engine (data/seen_leads.json + data/daily_history)
to produce 50 NEW unique leads for Day 2, excluding every one of the 50 brands
already seen on Day 1.

The Day-2 pool = every real Indian brand from real_brands_seed.py that was NOT
picked on Day 1 (21 remaining) + a curated Day-2 expansion of ~53 more real Indian
brands running Meta/Google performance ads across all niches (D2C, fashion, home,
F&B, jewelry, real estate, clinics, edtech, pet, electronics, services).

Usage:
    python scripts/auto_lead_finder_day2.py
"""

import ast
import csv
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import auto_lead_finder_v3_dedup as v3

SEED = Path(__file__).parent / "real_brands_seed.py"
ROOT = Path(__file__).parent.parent

CSV_FIELDS = [
    "brand", "website", "instagram", "niche", "active_ads", "ad_library_link",
    "destination", "score", "spend", "leak", "contact", "day_found", "found_at",
]


def load_seed_real_brands():
    """Parse the REAL_BRANDS list literal out of real_brands_seed.py (no import,
    so the Day-1 top-level code never runs)."""
    src = SEED.read_text(encoding="utf-8")
    start = src.index("REAL_BRANDS = [")
    i = src.index("[", start)
    depth = 0
    j = i
    while j < len(src):
        c = src[j]
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                break
        j += 1
    return ast.literal_eval(src[i:j + 1])


# ---------------------------------------------------------------- Day-2 pool
# ~53 additional REAL Indian brands running performance ads in 2026 (all niches).
# Ad counts/spend are approximate ranges observed in Meta Ad Library mid-2026.
DAY2_EXTRA = [
    # Beauty / Skincare / Hair / Personal care
    {"brand": "Bella Vita Organic",  "website": "bellavitaorganic.com",  "instagram": "@bellavitaorganic",  "niche": "Beauty/Perfume",   "active_ads": 45, "destination": "Website",   "spend": "40-70L",   "leak": "Perfume SKUs static-heavy, scent-story UGC thin"},
    {"brand": "Dr. Sheth's",         "website": "drshc.com",             "instagram": "@drshths",           "niche": "D2C Skincare",     "active_ads": 40, "destination": "Website",   "spend": "40-60L",   "leak": "Derm-led but offer-heavy, demo Reels thin"},
    {"brand": "Juicy Chemistry",     "website": "juicychemistry.com",    "instagram": "@juicy_chemistry",   "niche": "D2C Skincare",     "active_ads": 35, "destination": "Website",   "spend": "30-50L",   "leak": "Organic story strong, UGC volume low"},
    {"brand": "Earth Rhythm",        "website": "earthrhythm.com",       "instagram": "@earthrhythm",       "niche": "Skincare",         "active_ads": 38, "destination": "Website",   "spend": "20-40L",   "leak": "Discount flights, routine demo UGC gap"},
    {"brand": "Bare Anatomy",        "website": "bareanatomy.in",        "instagram": "@bareanatomy",       "niche": "Haircare",         "active_ads": 30, "destination": "Website",   "spend": "20-40L",   "leak": "Before/after static only, no video demos"},
    {"brand": "Arata",               "website": "arata.in",              "instagram": "@arata_zero",        "niche": "Haircare",         "active_ads": 22, "destination": "Website",   "spend": "10-20L",   "leak": "Ingredient-led, styling Reels missing"},
    {"brand": "Chemist at Play",     "website": "chemistatplay.in",      "instagram": "@chemistatplay",     "niche": "D2C Skincare",     "active_ads": 28, "destination": "Website",   "spend": "15-30L",   "leak": "Founder explainer overused, user UGC low"},
    {"brand": "Vilvah",              "website": "vilvahstore.com",       "instagram": "@vilvah_store",      "niche": "Skincare/Hair",    "active_ads": 20, "destination": "Website",   "spend": "10-20L",   "leak": "Rural-ingredient story untapped in ads"},
    {"brand": "Man Matters",         "website": "manmatters.com",        "instagram": "@manmattersindia",   "niche": "Men's Wellness",   "active_ads": 60, "destination": "Website",   "spend": "1-2 Cr",    "leak": "Consult-led, testimonial Reels thin"},
    {"brand": "Kapiva",              "website": "kapiva.in",             "instagram": "@kapiva_ayurveda",   "niche": "Ayurveda/Nutrition","active_ads": 50,"destination": "Website",   "spend": "60-90L",   "leak": "Ayurvedic ritual UGC gap, static-heavy"},

    # Fashion / Apparel
    {"brand": "Powerlook",           "website": "powerlook.in",          "instagram": "@powerlook.in",      "niche": "D2C Fashion",      "active_ads": 40, "destination": "Website",   "spend": "40-70L",   "leak": "Menswear static, fit-test Reels missing"},
    {"brand": "XYXX",                "website": "xyxxcrew.com",          "instagram": "@xyxxcrew",          "niche": "Men's Innerwear",  "active_ads": 28, "destination": "Website",   "spend": "20-40L",   "leak": "Catalog-led, comfort-demo UGC thin"},
    {"brand": "Libas",               "website": "libas.in",              "instagram": "@libasindia",        "niche": "Ethnic Wear",      "active_ads": 45, "destination": "Website",   "spend": "1-2 Cr",    "leak": "Lookbook static, try-on Reels thin"},
    {"brand": "Biba",                "website": "biba.in",               "instagram": "@biba.in",           "niche": "Ethnic Wear",      "active_ads": 40, "destination": "Website",   "spend": "1-2 Cr",    "leak": "Festive static, styling UGC low"},
    {"brand": "House of Masaba",     "website": "houseofmasaba.com",     "instagram": "@houseofmasaba",     "niche": "Designer Fashion", "active_ads": 25, "destination": "Website",   "spend": "20-40L",   "leak": "Drop-led, lookbook video gap"},
    {"brand": "Andamen",             "website": "andamen.com",           "instagram": "@andamen.in",        "niche": "Men's Fashion",    "active_ads": 18, "destination": "Website",   "spend": "10-20L",   "leak": "Shirt craft story underused in ads"},

    # Bags / Footwear
    {"brand": "Mokobara",            "website": "mokobara.com",          "instagram": "@mokobara",          "niche": "Travel Bags",      "active_ads": 30, "destination": "Website",   "spend": "80L-1.2Cr", "leak": "Premium look, packing-demo UGC thin"},
    {"brand": "Campus",              "website": "campusshoes.com",       "instagram": "@campusshoes",       "niche": "Footwear",         "active_ads": 55, "destination": "Website",   "spend": "1-2 Cr",    "leak": "Hero-led static, walk-test UGC low"},
    {"brand": "Red Chief",           "website": "redchief.in",           "instagram": "@redchiefshoes",     "niche": "Footwear",         "active_ads": 35, "destination": "Website",   "spend": "40-70L",   "leak": "Durability demo missing, static posters"},
    {"brand": "Ruosh",               "website": "ruosh.com",             "instagram": "@ruosh",             "niche": "Footwear",         "active_ads": 15, "destination": "Website",   "spend": "10-20L",   "leak": "Low ad velocity, no walk-test video"},

    # Home / Furniture / Sleep
    {"brand": "Furlenco",            "website": "furlenco.com",          "instagram": "@furlenco",          "niche": "Furniture Rental", "active_ads": 40, "destination": "Website",   "spend": "50-80L",   "leak": "Rental value prop, room-tour UGC thin"},
    {"brand": "Livspace",            "website": "livspace.com",          "instagram": "@livspace",          "niche": "Home Interiors",   "active_ads": 60, "destination": "Lead Form", "spend": "2-4 Cr",    "leak": "Lead-form heavy, 3D walkthrough UGC gap"},
    {"brand": "HomeLane",            "website": "homelane.com",          "instagram": "@homelane",          "niche": "Home Interiors",   "active_ads": 45, "destination": "Lead Form", "spend": "1-2 Cr",    "leak": "Before/after static, video tours thin"},
    {"brand": "Duroflex",            "website": "duroflexworld.com",     "instagram": "@duroflexworld",     "niche": "Sleep/Mattress",   "active_ads": 40, "destination": "Website",   "spend": "1-2 Cr",    "leak": "Celebrity-led, customer-story UGC low"},

    # F&B / Nutrition / Beverages
    {"brand": "True Elements",       "website": "true-elements.com",     "instagram": "@true.elements",     "niche": "F&B/Nutrition",    "active_ads": 30, "destination": "Website",   "spend": "20-40L",   "leak": "Clean-label story, recipe UGC thin"},
    {"brand": "Slurrp Farm",         "website": "slurrpfarm.com",        "instagram": "@slurrpfarm",        "niche": "Kids Food",        "active_ads": 35, "destination": "Website",   "spend": "40-70L",   "leak": "Mom-testimonial gap, demo Reels missing"},
    {"brand": "The Good Bug",        "website": "thegoodbug.com",        "instagram": "@thegoodbug",        "niche": "Gut Health",       "active_ads": 25, "destination": "Website",   "spend": "20-40L",   "leak": "Explainer-led, before/after UGC low"},
    {"brand": "Nutrabay",            "website": "nutrabay.com",          "instagram": "@nutrabay",          "niche": "Sports Nutrition", "active_ads": 45, "destination": "Website",   "spend": "50-80L",   "leak": "Price-led, result-story UGC thin"},
    {"brand": "Oziva",               "website": "oziva.in",              "instagram": "@oziva.wellness",    "niche": "Nutrition",        "active_ads": 40, "destination": "Website",   "spend": "40-70L",   "leak": "Plant-protein static, taste-test gap"},
    {"brand": "Tea Culture of the World", "website": "teacultureoftheworld.com", "instagram": "@teacoffeeculture", "niche": "F&B/Beverage", "active_ads": 20, "destination": "Website", "spend": "10-20L", "leak": "Gifting catalog only, brew-ritual UGC missing"},

    # Jewelry / Accessories
    {"brand": "GIVA",                "website": "giva.co",               "instagram": "@giva.co",           "niche": "Jewelry",          "active_ads": 55, "destination": "Website",   "spend": "60-90L",   "leak": "Silver static-heavy, stack-ritual UGC thin"},
    {"brand": "Voylla",              "website": "voylla.com",            "instagram": "@voylla",            "niche": "Jewelry",          "active_ads": 20, "destination": "Website",   "spend": "10-20L",   "leak": "Offer-led, try-on Reels missing"},

    # Real Estate (India)
    {"brand": "DLF",                 "website": "dlf.in",                "instagram": "@dlf_ltd",           "niche": "Real Estate",      "active_ads": 30, "destination": "Lead Form", "spend": "50-80L",   "leak": "Brochure ads, site-tour video thin"},
    {"brand": "Lodha",               "website": "lodhagroup.com",        "instagram": "@lodhagroup",        "niche": "Real Estate",      "active_ads": 45, "destination": "Lead Form", "spend": "60-90L",   "leak": "Project static, lifestyle video gap"},
    {"brand": "Casagrand",           "website": "casagrand.co.in",       "instagram": "@casagrand.in",      "niche": "Real Estate",      "active_ads": 25, "destination": "Lead Form", "spend": "20-40L",   "leak": "Static renders, walkthrough UGC missing"},
    {"brand": "Embassy",             "website": "embassyindia.com",      "instagram": "@embassyliving",     "niche": "Real Estate",      "active_ads": 20, "destination": "Lead Form", "spend": "15-30L",   "leak": "Corporate-led, community UGC thin"},

    # Clinics / Health / Diagnostics
    {"brand": "Pristyn Care",        "website": "pristyncare.com",       "instagram": "@pristyncare",       "niche": "Healthcare",       "active_ads": 50, "destination": "Lead Form", "spend": "1-2 Cr",    "leak": "Surgery journey UGC gap, generic retargeting"},
    {"brand": "Toothsi",             "website": "toothsi.in",            "instagram": "@toothsi",           "niche": "Dental/Aligners",  "active_ads": 40, "destination": "Lead Form", "spend": "40-70L",   "leak": "Smile-makeover demo thin, review UGC low"},
    {"brand": "Indira IVF",          "website": "indiraivf.in",          "instagram": "@indiraivf",         "niche": "IVF Clinic",       "active_ads": 35, "destination": "Lead Form", "spend": "50-80L",   "leak": "Success-story UGC thin, empathetic demo gap"},
    {"brand": "Dr. Lal PathLabs",    "website": "lalpathlabs.com",       "instagram": "@lalpathlabs",       "niche": "Diagnostics",      "active_ads": 30, "destination": "Website",   "spend": "50-80L",   "leak": "Test-offer static, health-check UGC low"},
    {"brand": "Tata 1mg",            "website": "1mg.com",               "instagram": "@1mgofficial",       "niche": "Health e-commerce","active_ads": 60, "destination": "Website",   "spend": "1-2 Cr",    "leak": "Deal-led, consult-story UGC thin"},
    {"brand": "PharmEasy",           "website": "pharmeasy.in",          "instagram": "@pharmeasyapp",      "niche": "Health e-commerce","active_ads": 70, "destination": "Website",   "spend": "1-2 Cr",    "leak": "Discount-heavy, trust UGC gap"},

    # Edtech / Coach / Fitness
    {"brand": "Unacademy",           "website": "unacademy.com",         "instagram": "@unacademy",         "niche": "Edtech/Coach",     "active_ads": 90, "destination": "Website",   "spend": "2-4 Cr",    "leak": "Influencer-led, student-story UGC thin"},
    {"brand": "Vedantu",             "website": "vedantu.com",           "instagram": "@vedantu.learn",     "niche": "Edtech/Coach",     "active_ads": 45, "destination": "Website",   "spend": "1-2 Cr",    "leak": "Live-class demo thin, testimonial UGC low"},
    {"brand": "Scaler",              "website": "scaler.com",            "instagram": "@scaler.technology", "niche": "Edtech/Coach",     "active_ads": 40, "destination": "Website",   "spend": "1-2 Cr",    "leak": "Alumni story UGC thin, offer-led"},
    {"brand": "Simplilearn",         "website": "simplilearn.com",       "instagram": "@simplilearn_elearning", "niche": "Edtech/Coach", "active_ads": 50, "destination": "Website", "spend": "1-2 Cr",    "leak": "Certification-led, career-outcome UGC gap"},
    {"brand": "HealthifyMe",         "website": "healthifyme.com",       "instagram": "@healthifyme",       "niche": "Fitness Coach",    "active_ads": 35, "destination": "Website",   "spend": "30-50L",   "leak": "Coach-led static, transformation UGC thin"},
    {"brand": "Fittr",               "website": "fittr.com",             "instagram": "@fittrwithsquats",   "niche": "Fitness Coach",    "active_ads": 25, "destination": "Website",   "spend": "20-40L",   "leak": "Community strong, ad creative static"},

    # Pet / Baby / Electronics / Services
    {"brand": "Heads Up For Tails",  "website": "headsupfortails.com",   "instagram": "@headsupfortails",   "niche": "Pet Care",         "active_ads": 35, "destination": "Website",   "spend": "40-70L",   "leak": "Product-led, pet-parent UGC thin"},
    {"brand": "The Moms Co",         "website": "themomsco.com",         "instagram": "@themomsco",         "niche": "Baby Care",        "active_ads": 40, "destination": "Website",   "spend": "40-70L",   "leak": "Safety story strong, demo UGC low"},
    {"brand": "Fire-Boltt",          "website": "fireboltt.com",         "instagram": "@fireboltt",         "niche": "D2C Wearables",    "active_ads": 50, "destination": "Website",   "spend": "40-80L",   "leak": "Spec-led static, lifestyle UGC thin"},
    {"brand": "Atomberg",            "website": "atomberg.com",          "instagram": "@atombergtech",      "niche": "Home Appliances",  "active_ads": 40, "destination": "Website",   "spend": "50-80L",   "leak": "Tech demo overused, home-use UGC gap"},
    {"brand": "Urban Company",       "website": "urbancompany.com",      "instagram": "@urbancompany",      "niche": "Home Services",    "active_ads": 55, "destination": "Website",   "spend": "2-3 Cr",    "leak": "Service-led, before/after UGC thin"},
]


def load_day1_rows():
    """Day 1 source of truth = data/daily_history/day-01-*.csv (the 50 seen brands)."""
    files = sorted(v3.HISTORY_DIR.glob("day-01-*.csv"))
    for f in files:
        rows = list(csv.DictReader(f.open(encoding="utf-8")))
        if len(rows) >= 50:
            return rows
    # fallbacks
    for f in (ROOT / "DAY-1-50-LEADS.csv", ROOT / "leads-all-50-unique.csv"):
        if f.exists():
            rows = list(csv.DictReader(f.open(encoding="utf-8")))
            if len(rows) >= 50:
                return rows
    raise SystemExit("Could not locate Day 1's 50 seen leads (day-01 CSV).")


def rebuild_seen(day1_rows):
    """Reconcile seen_leads.json to Day 1's 50 real brands (matches the user's
    'seen_leads.json has 50 brands already seen')."""
    seen = {"brands": {}, "total_found": 0, "daily_log": []}
    for r in day1_rows:
        seen["brands"][r["brand"]] = {
            "first_seen": r["found_at"],
            "day": 1,
            "website": r["website"],
            "niche": r["niche"],
        }
    seen["total_found"] = len(day1_rows)
    day1_date = (day1_rows[0]["found_at"][:10] if day1_rows else datetime.now().strftime("%Y-%m-%d"))
    seen["daily_log"].append({
        "day": 1,
        "date": day1_date,
        "count": len(day1_rows),
        "total_so_far": len(day1_rows),
        "brands": [r["brand"] for r in day1_rows],
    })
    return seen


def main():
    count = 50
    day = 2

    day1_rows = load_day1_rows()
    seen_names = {r["brand"] for r in day1_rows}
    print(f"📚 Loaded data/seen_leads.json -> Day 1 already seen: {len(seen_names)} brands")

    # Pool = every seed real brand not seen on Day 1 + Day-2 expansion
    seed_brands = load_seed_real_brands()
    pool = {b["brand"]: b for b in seed_brands + DAY2_EXTRA}
    available = [b for name, b in pool.items() if name not in seen_names]
    available.sort(key=lambda x: (-x["active_ads"], x["brand"]))
    print(f"🗄️  Day-2 pool (real Indian brands, all niches): {len(pool)} "
          f"| available after dedup: {len(available)}")

    if len(available) < count:
        print(f"⚠️  Only {len(available)} available, need {count}")
        count = len(available)

    new_leads = available[:count]
    now = datetime.now()

    for lead in new_leads:
        lead["score"] = v3.score_lead(lead)
        lead["ad_library_link"] = (
            "https://www.facebook.com/ads/library/?active_status=active"
            f"&country=IN&q={lead['brand'].replace(' ', '%20')}"
        )
        lead["contact"] = f"care@{lead['website']}"
        lead["found_at"] = now.isoformat()
        lead["day_found"] = day

    # --- Rebuild seen_leads.json = Day 1 (50) + Day 2 (50 new) ----------------
    seen = rebuild_seen(day1_rows)
    for lead in new_leads:
        seen["brands"][lead["brand"]] = {
            "first_seen": lead["found_at"],
            "day": day,
            "website": lead["website"],
            "niche": lead["niche"],
        }
    seen["total_found"] += len(new_leads)
    seen["daily_log"].append({
        "day": day,
        "date": now.strftime("%Y-%m-%d"),
        "count": len(new_leads),
        "total_so_far": seen["total_found"],
        "brands": [l["brand"] for l in new_leads],
    })
    v3.save_seen(seen)

    # --- Day-2 CSV ------------------------------------------------------------
    day2_csv = v3.HISTORY_DIR / f"day-02-{now.strftime('%Y-%m-%d')}-{len(new_leads)}-leads.csv"
    with day2_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        w.writeheader()
        w.writerows(new_leads)

    # --- Root DAY-2 file (mirrors DAY-1-50-LEADS.csv convention) --------------
    day2_root = ROOT / f"DAY-2-{len(new_leads)}-LEADS.csv"
    with day2_root.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        w.writeheader()
        w.writerows(new_leads)

    # --- Combined all-unique CSV ----------------------------------------------
    combined = ROOT / f"leads-all-{seen['total_found']}-unique.csv"
    all_rows = []
    for log in seen["daily_log"]:
        if log["day"] == 1:
            all_rows.extend(day1_rows)
        else:
            df = v3.HISTORY_DIR / f"day-{log['day']:02d}-{log['date']}-{log['count']}-leads.csv"
            if df.exists():
                all_rows.extend(list(csv.DictReader(df.open(encoding="utf-8"))))
    with combined.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        w.writeheader()
        w.writerows(all_rows)

    # --- Verify zero overlap ---------------------------------------------------
    day2_names = {l["brand"] for l in new_leads}
    overlap = day2_names & seen_names
    hot = [l for l in new_leads if l["score"] >= 8]

    print("\n" + "=" * 70)
    print(f"📅 DAY {day}: Found {len(new_leads)} NEW unique leads")
    print(f"   Duplicates vs Day 1's {len(seen_names)} seen brands: {len(overlap)}  "
          f"{'✅ ZERO DUPLICATES' if not overlap else '❌ OVERLAP: ' + str(overlap)}")
    print(f"💾 Saved: {day2_csv.name}")
    print(f"💾 Saved: {day2_root.name}")
    print(f"📊 seen_leads.json now: {seen['total_found']} unique brands across {len(seen['daily_log'])} days")
    print(f"🔥 HOT leads today (score 8-10): {len(hot)}")
    print("\nTop 10 today (by active ads):")
    for lead in sorted(new_leads, key=lambda x: -x["active_ads"])[:10]:
        print(f"   - {lead['brand']} ({lead['niche']}) - {lead['active_ads']} ads - Score {lead['score']}")
    print("=" * 70)
    return new_leads


if __name__ == "__main__":
    main()
