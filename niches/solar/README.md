# Solar Vertical 🌞

Isolated prospecting pipeline for the **solar niche**. The D2C pipeline in the repo
root is untouched and keeps running in parallel.

| | |
|---|---|
| **Find leads** | `python scripts/solar_lead_finder.py --count 50 --day 1` |
| **Audit a lead** | `python scripts/solar_audit.py niches/solar/leads/<brand>.json` |
| **Stats** | `python scripts/solar_lead_finder.py --stats` |
| **Full commands** | [`HOW-TO-RUN.md`](HOW-TO-RUN.md) |
| **Strategy** | [`SOLAR-PLAYBOOK.md`](SOLAR-PLAYBOOK.md) |
| **Templates** | [`templates/`](templates) — outreach, audit checklist, real-lead CSV |

## What's in here

```
niches/solar/
├── SOLAR-PLAYBOOK.md            # market math, segments, lead sources, offers, compliance
├── HOW-TO-RUN.md                # copy-paste commands + isolation map
├── data/
│   ├── seen_leads.json          # solar-only de-dup memory
│   ├── daily_history/           # solar-day-NN-*.csv
│   └── real_pool.csv            # (create it) leads YOU verified — served first
├── leads/                       # one rich JSON per lead (feeds the audit script)
├── audits/                      # generated solar audit PDFs
├── outreach/                    # generated internal outreach templates
└── templates/
    ├── solar-outreach-templates.md
    ├── solar-audit-checklist.md
    └── real_pool-template.csv
```

## The 3 numbers that run this niche

- **₹78,000** — max PM Surya Ghar subsidy (3 kW+), the strongest hook in Indian residential solar
- **300 units** — free electricity/month the scheme promises
- **₹150–450** — India benchmark Meta CPL for residential solar; audit clients against cost per **site survey**, not CPL alone

## Start here (30 minutes)

```bash
# 1. Solar day 1
python scripts/solar_lead_finder.py --count 50 --day 1

# 2. Open the CSV, take the 10 rows marked pitch_fit = HIGH
#    Verify each in Meta Ad Library (active filter) — do not skip this
open niches/solar/data/daily_history/       # or your file browser
# 3. Save the verified ones into niches/solar/data/real_pool.csv (see templates/)

# 4. Audit your best lead
python scripts/solar_audit.py --day 1 --row 0

# 5. Send the WhatsApp template from niches/solar/outreach/<brand>-outreach-templates.md
```

**Not sure who to pitch?** `pitch_fit` in the CSV says it: `HIGH` = owner-led EPC or
D2C product brand, `MEDIUM` = C&I/marketplace, `LOW` = in-house team, skip.
