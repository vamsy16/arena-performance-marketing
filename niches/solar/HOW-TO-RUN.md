# How to run the Solar vertical (without touching D2C)

Everything solar writes inside **`niches/solar/`**. Everything D2C keeps writing to
`data/`, `audits/`, `outreach/`, `leads/`, `reports/` exactly as before.

---

## 1. Daily lead run

```bash
# Solar Day 1
python scripts/solar_lead_finder.py --count 50 --day 1

# Solar Day 2 (auto-excludes Day 1)
python scripts/solar_lead_finder.py --count 50 --day 2

# Segment-focused run (recommended after day 3)
python scripts/solar_lead_finder.py --count 30 --day 4 --segment R
python scripts/solar_lead_finder.py --count 25 --day 4 --segment C --state Karnataka

# Check state
python scripts/solar_lead_finder.py --stats

# Start over (solar files only — D2C seen file is never touched)
python scripts/solar_lead_finder.py --reset
```

Outputs:

| File | What it is |
|---|---|
| `niches/solar/data/daily_history/solar-day-01-YYYY-MM-DD-50-leads.csv` | that day's 50 leads |
| `niches/solar/data/seen_leads.json` | solar de-dup memory (independent of D2C) |
| `niches/solar/solar-leads-all-N-unique.csv` | all solar leads so far, combined |
| `niches/solar/leads/<brand>.json` | one rich JSON per lead, ready for the audit step |

---

## 2. Add real leads you found yourself (makes the list better every day)

Create/append `niches/solar/data/real_pool.csv` (header below, see
`templates/real_pool-template.csv`). Rows here are treated as **real** and are served
**first** in each run:

```csv
brand,website,instagram,segment,city,state,capacity,active_ads,destination,spend_est,leak
Prisha Solar,prishasolar.in,@prishasolar,R,Bengaluru,Karnataka,3-10 kW,9,WhatsApp,1-3L/mo,form asks 8 fields
```

Then just run the finder as usual — your verified rows come out on top, tagged
`data_source=real-pool`.

---

### Note on enriched lead JSONs

The finder writes `niches/solar/leads/<brand>.json` **once**, when the brand is first
discovered. If you enrich one (like `fenice-energy.json`) and later run `--reset`, the
finder will overwrite it on re-discovery — so save enriched versions as
`<brand>-rich.json`. `solar_audit.py` accepts any filename.

### Readable lead list

`niches/solar/DAY-1-LEADS.md` — all 50 Day-1 leads in a clickable table (Ad Library + website
links), grouped into PITCH FIRST (18) / SECOND WAVE (12) / SKIP (20).

### Curated starting shortlist

`niches/solar/START-HERE-10-leads.csv` — the 10 `pitch_fit = HIGH` leads from Day 1,
sorted by score, ready to verify + pitch this week.

---

## 3. Audit a lead → PDF + outreach templates

```bash
# Best quality: rich JSON (edit the one the finder wrote, add real findings)
python scripts/solar_audit.py niches/solar/leads/fenice-energy.json

# Straight from the daily CSV
python scripts/solar_audit.py --day 1 --row 0

# Ad-hoc
python scripts/solar_audit.py --brand "Fenice Energy" --website feniceenergy.com \
    --city Chennai --segment R --ads 12
```

Outputs (**solar folders only**):

- `niches/solar/audits/<brand>-solar-audit-report.pdf` — 2–3 page client-facing audit (Smart Pursuit branding, subsidy-first findings)
- `niches/solar/outreach/<brand>-outreach-templates.md` — 3 internal outreach scripts

The D2C runner `python scripts/run_audit.py ...` is unchanged and still writes to
`audits/` + `outreach/`.

---

## 4. Why nothing can collide

| Concern | D2C pipeline | Solar pipeline |
|---|---|---|
| De-dup memory | `data/seen_leads.json` (100 brands, Days 1–2) | `niches/solar/data/seen_leads.json` |
| Daily CSVs | `data/daily_history/day-NN-*.csv` | `niches/solar/data/daily_history/solar-day-NN-*.csv` |
| Combined CSV | `leads-all-N-unique.csv` (repo root) | `niches/solar/solar-leads-all-N-unique.csv` |
| Lead JSONs | `leads/*.json` | `niches/solar/leads/*.json` |
| Audit PDFs | `audits/` | `niches/solar/audits/` |
| Outreach MDs | `outreach/` | `niches/solar/outreach/` |
| Runner script | `scripts/auto_lead_finder_v3_dedup.py`, `scripts/run_audit.py` | `scripts/solar_lead_finder.py`, `scripts/solar_audit.py` |
| Day counter | Day 1 → 50, 100 (independent) | Day 1 → 50, 100 (independent) |
| Brand pool | 3,000+ mock D2C/biotech/real-estate brands | ~610 solar companies (seed + regional) |

Two shells, side by side, no shared state:

```bash
python scripts/auto_lead_finder_v3_dedup.py --count 50 --day 4   # D2C  (unchanged)
python scripts/solar_lead_finder.py        --count 50 --day 1   # Solar
```

`--reset` on the solar script only deletes `solar-day-*.csv`, `solar-leads-all-*.csv`
and `niches/solar/data/seen_leads.json`.

---

## 5. Push it (so the next chat remembers)

```bash
git add niches/solar scripts/solar_lead_finder.py scripts/solar_audit.py
git commit -m "Solar: day N leads + audits"
git push origin arena/01a09e59-arena-performance-marketing
```

The solar de-dup file travels with the repo, so any new chat/clone continues
solar from where you stopped — with zero effect on the D2C day counter.

---

## 6. Copy-paste prompt for any new chat

```
Solar niche. Use the isolated solar pipeline in this repo (never touch the D2C data/):

1. python scripts/solar_lead_finder.py --stats
2. python scripts/solar_lead_finder.py --count 50 --day <N> --segment R
3. For the top 10 rows: fetch the website + Meta Ad Library India (active filter) and
   confirm the ads we're claiming are real. Then load verified rows into
   niches/solar/data/real_pool.csv.
4. Audit the best 2: python scripts/solar_audit.py niches/solar/leads/<brand>.json
5. Rewrite the outreach in the audit for that specific brand:
   3 messages, under 120 words, subsidy angle + one verified leak, soft CTA ("want the audit?").
```

---

## 7. What the finder already gave you

- **`niches/solar/leads/`** — 50 real named Indian solar companies (SolarSquare, Freyr, Fenice, ZunRoof, Oorjan, MYSUN, Arka, Loom Solar, Smarten, UTL, Emmvee, Swelect, plus the large EPCs). Ad counts are **estimates** — verify before outreach.
- **`pitch_fit` column** tells you which ones to skip (`LOW` = in-house team, e.g. Tata Power Solar, Adani Solar, Waaree).
- **`niches/solar/audits/fenice-energy-solar-audit-report.pdf`** — a completed sample audit built from a real site review, so you can see the output format before you run your own.

**Golden rule:** outreach only to rows you have personally confirmed live in Meta Ad
Library. The script supplies structure and de-duplication — verification is yours.
