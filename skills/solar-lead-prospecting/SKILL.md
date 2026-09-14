---
name: solar-lead-prospecting
description: "When the user wants to find, qualify, audit or pitch SOLAR companies (rooftop solar EPC, solar installers, solar panel/inverter D2C brands, C&I solar EPCs, solar channel partners/marketplaces) as agency leads. Use when user says 'solar leads', 'solar niche', 'rooftop solar clients', 'find solar installers running ads', 'solar agency prospecting', 'PM Surya Ghar leads', or gives a solar brand to audit. This is an isolated vertical: it must NEVER write to the D2C files (data/seen_leads.json, data/daily_history/, audits/, outreach/, leads/). For D2C brands use lead-prospecting / performance-lead-audit instead."
metadata:
  version: 1.0.0
---

# Solar Lead Prospecting — isolated vertical

You run the solar pipeline. Everything you create goes under `niches/solar/`.
The D2C pipeline (`data/seen_leads.json`, `data/daily_history/`, `audits/`,
`outreach/`, `leads/`, `scripts/auto_lead_finder_v3_dedup.py`, `scripts/run_audit.py`)
is **off-limits** — never reset it, never write into it, never run its audit script
on a solar brand.

## Hard rules

1. Lead generation: `python scripts/solar_lead_finder.py --count 50 --day N [--segment R|C|B|P] [--state <State>]`
2. Audits: `python scripts/solar_audit.py niches/solar/leads/<brand>.json` (or `--day N --row R`).
   Never `scripts/run_audit.py` for a solar lead.
3. De-dup state is `niches/solar/data/seen_leads.json` — push it with the repo.
4. **Verify before you pitch.** The finder's `seed-real` rows are real companies with
   *estimated* ad counts. Confirm live creatives in Meta Ad Library India (active filter)
   before any number appears in an audit or a message. Rows tagged `pool-placeholder`
   must be replaced with real advertisers before use.
5. Never promise subsidy approval/amount/timeline; never present yourself as MNRE /
   DISCOM / government. Use "eligible for up to ₹78,000".

## Workflow

### 1. Find leads
```bash
python scripts/solar_lead_finder.py --stats                  # where the solar pipeline stands
python scripts/solar_lead_finder.py --count 50 --day <N> --segment R
```
Rank by `score`, filter by `pitch_fit = HIGH`, ignore `LOW` (in-house marketing teams).

### 2. Verify (agent does this, not the user)
For each of the top rows:
- Fetch the website → check subsidy above the fold, WhatsApp CTA, form field count, calculator placement, EMI, reviews, install proof
- Check Meta Ad Library India link in the row (or `web_search` the brand + "ads library")
- Optionally Google Ads Transparency via `adstransparency.google.com/?region=IN&domain=<domain>`
- Write verified numbers back into the row; put confirmed leads in `niches/solar/data/real_pool.csv`

### 3. Audit + outreach
```bash
python scripts/solar_audit.py niches/solar/leads/<brand>.json
```
Then tighten the generated files for that specific brand:
- PDF → `niches/solar/audits/<brand>-solar-audit-report.pdf` (client-facing: 3 leaks, scores, 3 quick wins, impact table)
- MD → `niches/solar/outreach/<brand>-outreach-templates.md` (internal: 3 messages, <120 words, one verified leak, soft CTA)

### 4. References
- `niches/solar/SOLAR-PLAYBOOK.md` — segments, lead sources with exact Ad Library keywords, offer/pricing math, compliance
- `niches/solar/HOW-TO-RUN.md` — command sheet + isolation map
- `niches/solar/templates/solar-audit-checklist.md` — 12-point solar audit
- `niches/solar/templates/solar-outreach-templates.md` — WhatsApp/email/LinkedIn copy per segment

## Solar-specific knowledge you must apply

- **Hook:** PM Surya Ghar — ₹30,000 (1 kW) / ₹60,000 (2 kW) / ₹78,000 (3 kW+), up to 300 free units/month, ~6–7% collateral-free loans, subsidy credited 30–45 days after DISCOM inspection.
- **Buyer behaviour:** enquiries start as WhatsApp questions ("kitna kharcha?"), decision takes 30–90 days, two-step sale (enquiry → site survey → order).
- **Real KPI:** cost per **site survey** and cost per install — not CPL alone.
- **Benchmarks (India):** Meta CPL ₹150–450; lead→survey 15–20% (28–35% with <5 min WhatsApp reply); survey→order 20–25%.
- **Seasons:** Feb–Jun and Sep–Oct peaks.
- **Segments:** R residential EPC (best first target), C D2C products, B C&I, P channel partners.
