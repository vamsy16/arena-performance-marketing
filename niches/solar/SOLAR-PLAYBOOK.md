# Solar Vertical — Playbook (Smart Pursuit)

> Separate niche, separate pipeline, same machinery. D2C prospecting keeps running exactly as-is;
> everything solar lives under `niches/solar/`.

---

## 0. Why solar is a different game from D2C

| Factor | D2C (current pipeline) | Solar |
|---|---|---|
| Ticket | ₹500–5,000 | ₹1.5–3 lakh (residential), ₹5L–5Cr (C&I) |
| Decision cycle | Same day – 7 days | 30–90 days, two-step (enquiry → site survey → order) |
| Strongest hook | Discount / BOGO | **Government subsidy + electricity bill** |
| Lead destination | Website checkout | WhatsApp / phone call / form → survey |
| Who answers | Growth manager | Owner / sales head |
| What they judge you on | ROAS | Cost per **site survey** and cost per install |

**The single most important market fact:** PM Surya Ghar (Muft Bijli Yojana) pays **₹30,000 for 1 kW, ₹60,000 for 2 kW, ₹78,000 for 3 kW+**, gives up to **300 free units/month**, and offers collateral-free loans at ~6–7%. Subsidy is credited to the customer's bank account 30–45 days after DISCOM inspection. Any solar ad that does not lead with this number is leaving money on the table — that is your pitch.

**India benchmarks to quote in audits (label them as benchmarks, not guarantees):**

- Meta cost per lead, residential solar: **₹150–450**
- Lead → site survey: **15–20%** typical, 28–35% with fast WhatsApp follow-up
- Site survey → order: **20–25%** typical, 30–35% with EMI + subsidy clarity at survey
- Cost per installed kW won: keep under **₹3,500–5,500/kW**; ₹6,000–9,000/kW means the funnel is leaking
- Seasonality: peaks **Feb–Jun** (summer bills, subsidy push) and **Sep–Oct** (post-monsoon)

---

## 1. Pick ONE segment before you spend a rupee on outreach

| Code | Segment | Who they are | Ticket | Cycle | Your opening angle |
|---|---|---|---|---|---|
| **R** | Residential rooftop EPC / installer | 3–30 person installer companies, owner-led, 1–5 cities | ₹1.5–3L | 30–60 days | "Subsidy-first creative + click-to-WhatsApp = more site surveys at the same spend" |
| **C** | D2C solar products | Panels, inverters, batteries, solar water heaters sold online | ₹8k–1.5L | 7–30 days | "Your catalogue is not in WhatsApp and your ads don't show bundle pricing or EMI" |
| **B** | C&I / industrial rooftop EPC | 20+ people, project sales, big-ticket | ₹5L–5Cr | 90–270 days | "You run broad Meta while C&I buyers need case-study + LinkedIn ABM" |
| **P** | Channel partner / marketplace | Lead aggregators, dealer networks | per-lead | 7–30 days | "Your lead quality/CPL is the product — I can drop your CPL" |

**Recommendation:** start with **R**. Highest volume of pitchable, owner-led businesses, fastest reply, clearest ROI story. Add **C** in month 2 (they already buy performance marketing and judge you on CPL).

---

## 2. Where solar leads actually come from (priority order)

### 2.1 Meta Ad Library — India (your #1 source, ~80% of leads)

Link: `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=IN&search_type=keyword_unordered`

**Search keywords that surface real spenders** (run each, then dump results into `niches/solar/data/real_pool.csv`):

```
solar subsidy          PM Surya Ghar          rooftop solar
solar panel price      solar panel for home   free electricity bill
bijli bill zero        solar installation     solar company <city>
3 kW solar             solar inverter         solar water heater
solar panel dealer     solar rooftop          on grid solar
```

**Qualify a lead (all four):**
1. **5+ active ads** (10+ = serious budget)
2. At least one creative **running 14+ days** (proven spender, not a test)
3. Ad **CTA type**: "Send WhatsApp Message" / "Call now" / Lead form → tells you the funnel
4. **Creative weakness** visible: static posters, no install photos, no customer video, no subsidy number

Reject: national giants with in-house teams (marked `LOW` by `pitch_fit`), chains with a marketing agency already, anything under 3 active ads.

### 2.2 Google Ads Transparency — for C&I and D2C products

`https://adstransparency.google.com/?region=IN&domain=<their-domain>` — 10+ ads means real spend. Also search `solar installer <city>`, `solar panel price`, `PM Surya Ghar subsidy`.

### 2.3 Local installer directories — the volume pool

- `pmsuryaghar.gov.in` — MNRE-empanelled vendor list by state (these vendors *cannot* advertise subsidy offers without approval, which is exactly the pain you solve)
- Loom Solar's "find an installer" directory (thousands of Indian rooftop installers), Justdial / IndiaMART / SolarClue listings, local solar association member lists
- Action: pull names → check each in Ad Library → only ad-active ones enter `real_pool.csv`

### 2.4 Instagram / YouTube installers

Search `solar installation <city>`, `rooftop solar <city>`, `#solarindia`. Installers posting install reels but running no ads = "you have proof, you just aren't paying to show it" pitch.

### 2.5 Google Maps + ad check

Scrape "solar panel dealer <city>" → for each, check Ad Library → ad-active only.

---

## 3. Scoring and data honesty (baked into the script)

Every row carries:

- `score` (1–10) — WhatsApp/lead-form destination, 5+ and 15+ active ads, subsidy/WhatsApp/UGC leak in the finding, video/testimonial gap, capacity, real-data bonus
- `pitch_fit` — `HIGH` (owner-led EPC / D2C), `MEDIUM` (C&I, marketplace), `LOW` (**do not cold pitch** — in-house teams)
- `data_source` — `seed-real` (company is real; **ad counts are estimates**), `pool-placeholder` (**replace the name**), `real-pool` (**you verified it**)
- `verify` — the instruction for that row

**Golden rule: outreach only goes to rows you have personally seen live in Meta Ad Library.** The script gives you structure and de-duplication; it cannot verify ad counts from this sandbox. Never quote an unverified number to a client.

---

## 4. Solar audit checklist (12 checks, 20 minutes per lead)

1. **Subsidy above the fold?** ₹78,000 / 300 free units / PM Surya Ghar named on the first screen of site AND in the ad creative
2. **Click-to-WhatsApp on the ad?** Or does it push to a website/form/toll-free number?
3. **Speed-to-lead**: is there auto-greeting, catalogue, and a reply within 5 minutes?
4. **Proof layer**: install photos/videos, net-meter bills, customer testimonials, city-wise install count
5. **Calculator placement**: is the savings/subsidy calculator the hero CTA or buried in the footer?
6. **Form fields**: count them. More than 3 (city, phone, monthly bill) kills completion
7. **EMI / financing visible?** Solar is a financing decision for most middle-income buyers
8. **Reviews**: Google rating + count shown in creatives, or hidden on an About page?
9. **Retargeting**: any sequence across 30–90 days (video view → WhatsApp → survey offer)?
10. **City/local pages**: separate landing pages for each city served, or one homepage for all?
11. **Tracking**: Meta Pixel + CAPI (server-side), Google Ads conversion, call/WhatsApp tracking — same discipline as D2C, usually weaker here
12. **Channel partner program**: existing GreenPartner/ambassador programs — amplify with a paid partner track at zero CPL

Run the automated version:

```bash
python scripts/solar_audit.py niches/solar/leads/<brand>.json
# or from the daily list
python scripts/solar_audit.py --day 1 --row 0
```

Outputs land in `niches/solar/audits/` (client-facing PDF) and `niches/solar/outreach/` (internal templates).

---

## 5. Offer and pricing math for solar

**What solar clients actually buy:** creative + WhatsApp automation + landing page + retargeting, priced against **cost per site survey**, not impressions.

**Example unit economics (residential, 3 kW):**

```
System price            ₹1,60,000      (subsidy ₹78,000 goes to customer's bank)
Gross margin @22%       ₹35,000        ← what you are competing against for attention
CPL                     ₹300
Lead → survey           @12%           → ₹2,500 per survey
Survey → order          @25%           → ₹10,000 per install
```

At ₹10,000 cost per install against ₹35,000 gross margin, the client can still scale — **but only if the funnel is tight**. Cut CPL to ₹200 and lift lead→survey to 30% and CPA falls to ~₹2,700. That is the whole pitch: *"Same budget, 3x more installs."*

**Package ladder that works in this market:**

| Package | Price/mo | Deliverable | 30-day KPI you commit to |
|---|---|---|---|
| Pilot (30 days) | ₹35,000–50,000 | Subsidy-first creative batch (6 ads), click-to-WhatsApp, WhatsApp Business setup, retargeting | CPL and site-survey count vs their current baseline |
| Growth | ₹75,000–1,25,000 | + city landing pages, 60-day retargeting sequence, install-video production, CRM/WhatsApp flows | Cost per survey, survey→order |
| Performance | Retainer + per-install bonus | Full funnel ownership | Cost per install under ₹4,000/kW won |

**Risk reversal that closes solar clients:** offer the pilot partially performance-based — e.g. "₹35k, and if CPL doesn't drop below X in 30 days, month 2 is free." Solar owners respond to that far better than to decks.

---

## 6. Outreach angles that get replies in solar

| Angle | One-line opener |
|---|---|
| **Subsidy omission** | "Your homepage doesn't say ₹78,000. Freyr and SolarSquare lead with the number — you lead with 'go green'." |
| **WhatsApp leak** | "You're paying for clicks and sending them to a toll-free number. Solar questions arrive at 9pm on WhatsApp." |
| **Form friction** | "Your form asks 8 things before it gives anything back. Three fields (city, phone, bill) beat it every time." |
| **Proof gap** | "You have installs across 100 cities and none of them are in the ad. Buyers commit ₹2 lakh on trust." |
| **City FOMO** | "The top 3 installers in <city> all run subsidy-first creative + WhatsApp CTA. You don't." |
| **Partner lever** | "Your GreenPartner program is a free lead source you're not paying to amplify." |

Language rule: **Hinglish/regional copy for R** (owner reads WhatsApp, not email decks), **English for C and B**. Keep the first message under 120 words and end with a permission question ("Want me to WhatsApp the 2-page audit?"), never a meeting request.

Full templates: `niches/solar/templates/solar-outreach-templates.md`.

---

## 7. Compliance and honesty rules (read before you send anything)

1. **Never promise subsidy approval, amount or timeline.** It is a government scheme; approval flows through `pmsuryaghar.gov.in` and the DISCOM. Say "eligible for up to ₹78,000", never "you will get ₹78,000".
2. **Do not present yourself as government / MNRE / DISCOM.** No use of the scheme logo as if official, no "authorised by PM Surya Ghar".
3. **Do not promise DISCOM net-metering timelines** (real-world 15–45 days, varies by state).
4. **Quote only verified numbers.** Ad counts, spend and revenue in your audits must come from something you saw (Ad Library, the site) — mark estimates as estimates.
5. **Never claim competitor results you can't see.** "Freyr leads with ₹1 lakh savings" is verifiable from their homepage; "Freyr's CPL is ₹180" is not.
6. Client results: only publish case studies you have data for. Solar buyers ask other owners — a false claim travels fast in a city's installer community.

---

## 8. The 40-day rollout

| Days | What you do | Output |
|---|---|---|
| 1–3 | Run the finder, verify top 30 rows live in Ad Library, load them into `real_pool.csv` | 30 verified leads |
| 4–10 | Audit 2/day (10 audits), send 10 outreach/day for R segment | 10 PDF audits, first replies |
| 11–20 | City-by-city push (`--state`, `--segment R`), add city landing page as the free hook | 100 leads, 2 pilot clients targeted |
| 21–40 | Monthly retainer outreach to C segment + channel partners; keep dedup running daily | 500+ solar leads tracked, 2–4 pilots live |

Weekly scoreboard: DMs sent → replies → audits sent → calls booked → pilots closed. Solar reply rates are lower than D2C but deal value is 20–50x — judge the pipeline on **surveys booked**, not reply count.

---

**Related:** `niches/solar/HOW-TO-RUN.md` (commands), `skills/solar-lead-prospecting/SKILL.md` (agent skill), `niches/solar/templates/` (outreach + checklist + CSV templates).
