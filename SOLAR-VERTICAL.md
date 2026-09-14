# Starting a Solar Niche — without disturbing your D2C pipeline

**Short answer: yes, you start it separately, and it is already set up in this repo.**

You do **not** need a new repo, a new chat workflow, or to touch any D2C file. The solar
pipeline is a parallel vertical under `niches/solar/` with its own de-dup memory, its own
lead pool, its own audit runner and its own skill.

---

## 1. Why "separately" is the right call

Your D2C engine keeps one shared de-dup file (`data/seen_leads.json`). If you ran solar
through the same script with a `--niche solar` flag, three things would go wrong:

1. Solar brands would enter the D2C "already seen" list and permanently suppress real D2C leads.
2. `--reset` (needed for a fresh niche) would wipe your 100-brand D2C history.
3. The audit runner writes to the root `audits/` + `outreach/` folders — solar PDFs would mix into D2C client files.

So the system uses **namespacing instead of a flag**: solar writes to `niches/solar/…`,
D2C keeps writing to the root exactly as it does today. Two independent day counters,
two independent brand pools, zero collision.

---

## 2. What you run (copy-paste)

```bash
# ---- D2C (unchanged, keep going) ----
python scripts/auto_lead_finder_v3_dedup.py --count 50 --day 4

# ---- SOLAR (new, parallel) ----
python scripts/solar_lead_finder.py --count 50 --day 1                # 50 solar leads
python scripts/solar_lead_finder.py --count 30 --day 4 --segment R    # residential EPC only
python scripts/solar_lead_finder.py --stats                           # solar + confirms D2C file untouched
python scripts/solar_lead_finder.py --reset                           # solar-only reset

# audit + outreach for a solar lead (writes to niches/solar/ only)
python scripts/solar_audit.py niches/solar/leads/fenice-energy.json
python scripts/solar_audit.py --day 1 --row 0
```

That's it. Four commands and the niche is running.

---

## 3. What already exists in `niches/solar/`

| Path | What it is |
|---|---|
| `niches/solar/data/seen_leads.json` | solar de-dup memory (50 brands from Day 1) |
| `niches/solar/data/daily_history/solar-day-01-2026-09-14-50-leads.csv` | 50 real named Indian solar companies with score, city, segment, CTA, ad-library link |
| `niches/solar/leads/*.json` | one rich JSON per lead, ready for the audit runner |
| `niches/solar/leads/fenice-energy.json` | fully written sample audit input (real site review) |
| `niches/solar/audits/fenice-energy-solar-audit-report.pdf` | **finished sample audit** in the new solar format |
| `niches/solar/outreach/fenice-energy-outreach-templates.md` | 3 solar outreach scripts |
| `niches/solar/SOLAR-PLAYBOOK.md` | segments, Ad Library keyword list, offer math, compliance rules |
| `niches/solar/HOW-TO-RUN.md` | command sheet + isolation map |
| `niches/solar/templates/` | outreach templates, 12-point audit checklist, real-lead CSV template |
| `skills/solar-lead-prospecting/SKILL.md` | new agent skill (added to the plugin manifest) |

Day 1 output includes SolarSquare, Freyr Energy, Fenice Energy, ZunRoof, Oorjan, MYSUN,
Arka Energy, Loom Solar, Smarten, UTL, Emmvee, Swelect and the larger EPCs — each row
tagged `pitch_fit = HIGH / MEDIUM / LOW`. **Skip the `LOW` rows** (Tata Power Solar, Adani
Solar, Waaree etc. have in-house teams — a cold DM is a wasted day).

---

## 4. The solar playbook in five lines

1. **One hook beats everything:** PM Surya Ghar pays **₹78,000** on a 3 kW system + **300 free units/month**. Any solar ad not leading with that number has a leak you can name.
2. **WhatsApp is the funnel.** Enquiries start as "kitna kharcha?" at 9pm — toll-free numbers and 8-field forms kill them.
3. **Target R segment first** (owner-led residential EPCs): fastest reply, clearest ROI, ₹1.5–3L ticket.
4. **Judge by cost per site survey and cost per install** — not CPL. India benchmarks: CPL ₹150–450, lead→survey 15–35%, survey→order 20–35%.
5. **Compliance matters:** never promise subsidy approval/amount/timeline, never pose as MNRE/DISCOM, quote only numbers you verified.

Full detail: `niches/solar/SOLAR-PLAYBOOK.md`.

---

## 5. The daily rhythm (30–45 min/day)

| Time | Action |
|---|---|
| 5 min | `python scripts/solar_lead_finder.py --count 50 --day N` |
| 15 min | Open the CSV → take `pitch_fit = HIGH` rows → verify 10 of them live in Meta Ad Library → paste verified rows into `niches/solar/data/real_pool.csv` |
| 10 min | Audit the 2 best: `python scripts/solar_audit.py niches/solar/leads/<brand>.json` |
| 10 min | Send 5–10 WhatsApp/email messages from `niches/solar/outreach/<brand>-outreach-templates.md` |
| 2 min | `git add niches/solar && git commit && git push` |

Weekly: DMs sent → replies → audits delivered → site surveys booked. Solar reply rates are
lower than D2C but a closed client is 20–50x the value, so track surveys, not replies.

---

## 6. Two honest caveats

1. **Ad counts in the seed rows are estimates.** The companies are real, the ad numbers are
   modelled. Every row says so (`verify` column). Confirm live creatives in Meta Ad Library
   before a number goes into an audit or a message. Rows tagged `pool-placeholder` must be
   replaced with real advertisers before any outreach.
2. **This sandbox can't reach Indian solar websites directly** (outbound HTTP is blocked), so
   the automatic pixel/WhatsApp/tracking check runs only when you or the agent fetch the site
   through the browsing tool. The 12-point checklist in `niches/solar/templates/` covers what
   to look at when it can.

---

## 7. Recommended path

**Week 1:** run solar Days 1–3, verify 30 rows, load them into `real_pool.csv`, audit 6, send 50 outreach messages to R-segment owners, land 1 pilot (₹35–50k, 30-day KPI on site surveys).

**Week 2+:** keep the daily run going, add city-by-city pushes (`--state Karnataka`, `--segment R`), then bring in segment C (D2C solar products) once you have one R-segment case study to show.
