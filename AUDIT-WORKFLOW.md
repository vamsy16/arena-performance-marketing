# Performance Marketing Audit Workflow (Smart Pursuit)

50-day lead-finding + audit + outreach system. 50 new unique leads per day (2,500 total).
Zero duplicates via `data/seen_leads.json`.

## Repository Structure

```
scripts/
  auto_lead_finder_v3_dedup.py  # Core dedup engine (run daily)
  real_brands_seed.py            # Seeds 70+ real Indian brands into the pool
  audit_pdf.py                   # Reusable branded PDF generator (module)
  run_audit.py                   # One-command audit runner (CLI)
data/
  seen_leads.json                # All brands ever found (dedup database)
  daily_history/                 # Day-by-day CSVs of 50 leads
leads/                           # Per-lead JSON data files (rich audit data)
  physics-wallah.json            # Example - full audit data for Lead #1
audits/                          # Generated audit PDFs live here
outreach/                        # Generated outreach email templates (internal BD)
reports/                         # Combined CSVs across days
skills/                          # Reusable skill playbooks (audit, cro, ads, etc.)
```

## Step 1 - Find 50 new unique leads for Day N

```bash
# Clear seen_leads.json only on Day 1 (fresh start)
echo '{"brands":{},"total_found":0,"daily_log":[]}' > data/seen_leads.json

# Day 1
python scripts/real_brands_seed.py        # seeds real brands, runs day 1

# Days 2-50 (uses dedup engine, excludes all prior days)
python scripts/auto_lead_finder_v3_dedup.py --count 50 --day 2
python scripts/auto_lead_finder_v3_dedup.py --count 50 --day 3
# ... up to day 50
```

Day-1 output: `data/daily_history/day-01-YYYY-MM-DD-50-leads.csv` (50 rows, unique brands, sorted by ad volume).

## Step 2 - Audit a lead (PDF + Outreach MD)

You can audit a lead three ways:

### A. From a rich lead JSON (best quality, full customization)

Create a file in `leads/<brand-slug>.json` (use `leads/physics-wallah.json` as a template) with exec summary, ad intelligence, scores, findings, competitors, 3 quick wins, impact table, outreach templates. Then:

```bash
python scripts/run_audit.py leads/physics-wallah.json
```

Generates:
- `audits/physics-wallah-audit-report.pdf` (2-page Smart Pursuit branded PDF)
- `outreach/physics-wallah-outreach-templates.md` (3 outreach emails, internal use)

### B. Quick audit from the daily CSV (row index)

```bash
# Audit the very first lead in Day 1 CSV
python scripts/run_audit.py --day 1 --row 0    # Physics Wallah
python scripts/run_audit.py --day 1 --row 1    # boAt
python scripts/run_audit.py --day 1 --row 2    # Mamaearth
```

Produces a skeleton PDF (intelligent defaults; you'll want to add richer findings/competitors/wins via the JSON method for best results).

### C. Ad-hoc quick audit

```bash
python scripts/run_audit.py --brand "BoAt" --website boat-lifestyle.com \
  --niche "D2C Audio" --ads 140 --spend "Rs.5-10 Cr"
```

## Step 3 - Review, push, send

1. Open `audits/<brand>-audit-report.pdf` and review.
2. Push to GitHub.
3. Use outreach templates from `outreach/<brand>-outreach-templates.md` to send via email/WhatsApp.

## PDF Template (Smart Pursuit Branding)

Every generated PDF contains these sections, in this order, on exactly 2 pages:

1. **Cover band** - "We Found 3 Leaks Costing You ~40% of Ad Spend" + lead score badge (0-10)
2. **Quick stats bar** - active ads, spend, niche, revenue
3. **Executive Summary** - purple box with the 3 key leaks
4. **Ad Intelligence** - platforms, ad count, funnel type, budget
5. **Score bars** - 6 dimensions (Creative, UGC, Copy, CRO, Tracking, Retargeting) with red/orange color coding
6. **Findings bullets** - creative/copy/CRO/tracking leaks
7. **Competitor Benchmark** - 3 competitors, what they do better, signal for the brand
8. **3 Quick Wins** (7-day) - green/orange/purple boxes with expected CTR/CVR lifts
9. **Expected Impact table** - CTR, CVR, CPA, spend savings
10. **CTA Box** - Smart Pursuit 14-day sprint offer, phone + email

Outreach templates are ALWAYS a separate file in `outreach/` - never included in the client-facing PDF.

## Agency Details (edit in audit_pdf.py if needed)

- Name: Smart Pursuit
- Phone: 7095024220
- Email: smartpursuit3@gmail.com

Override per-lead by passing `agency_name`, `agency_phone`, `agency_email` in the lead JSON.
