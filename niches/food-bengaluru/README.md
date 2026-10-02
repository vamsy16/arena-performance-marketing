# Food / Bengaluru — Performance Audit Pack (Smart Pursuit)

> Lives inside the **arena-performance-marketing** repo as the Food/Bengaluru niche (moved out of ServiceNowDocs on 02 Oct 2026).
> Format: house **ATTRACTIVE** audit PDF (same family as the GMB/SMM/CRO template PDFs).

**11 leads · 11 audit PDFs · 44 follow-up emails · 1 master Excel · every fact verified live on 02 OCT 2026.**

## Start here

| Path | What it is |
|---|---|
| **`Food-Bangalore-ALL-IN-ONE.xlsx`** | **Everything in one workbook** — 8 sheets: README, Leads, Emails (all 44), Leaks & Roadmap, You vs Competitor, Expected ROI, Audit Basis (sources), Skills Used |
| `audits/*.pdf` | Audit per lead (7-page "Paid Media & Measurement Audit" evidence format; the earlier attractive layout is archived in `audits/_previous-attractive-format/`, the original text layout in `audits/_previous-text-format/`) |
| `ALL-EMAIL-SEQUENCES.md` | All 44 emails in one file (4 per brand: Day 1 / 3 / 7 / 14) |
| `outreach/*-outreach-templates.md` | Per-brand email file |
| `leads/*.json` | Structured lead data incl. `contact_source` (where each email was crawled from) |
| `LEADS-INDEX.csv` | Flat lead table |
| `scripts/` | Rebuild everything: `build_attractive_audits.py` (PDFs), `build_master_excel.py` (Excel), `build_food_leads.py` (leads + text-format archive) |
| `audits/_previous-text-format/` | The earlier 2-page text-style PDFs, kept for reference |

## The 11 leads

| # | Brand | Lead email (crawled from their own properties) | Live Google ads | Score |
|---|-------|-----------------------------------------------|-----------------|-------|
| 1 | Licious | talktous@licious.com | ~300 | 7/10 |
| 2 | Cothas Coffee | customercare@cothas.com | 77 | 7/10 |
| 3 | Anand Sweets | care@anandsweets.net | 58 | 8/10 |
| 4 | Chai Point | customercare@chaipoint.com | 56 | 7/10 |
| 5 | The Baker's Dozen | fresh@thebakersdozen.in | 35 | 7/10 |
| 6 | Early Foods | hello@earlyfoods.com | 30 | 7/10 |
| 7 | iD Fresh Food | customercare@idfreshfood.com | 1 | 8/10 |
| 8 | Third Wave Coffee | orders@thirdwavecoffee.in | 0 | 7/10 |
| 9 | Akshayakalpa Organic | support@akshayakalpa.org | ~400 | 8/10 |
| 10 | Milky Mist | customercare@milkymist.com | 3 | 8/10 |
| 11 | Frozen Bottle | vipul@frozenbottle.in | 11 | 6/10 |

## Skills used to build each audit

`performance-lead-audit` orchestrating: **ads** (Google Ads Transparency + Meta Ad Library live counts, advertiser entities, destinations), **ad-creative** (formats, fatigue, refresh systems), **copywriting** (hook/angle analysis from live ad copy), **cro** (destination-path step count, trust-proof placement), **analytics + attribution** (GTM/GA4/CAPI findings from live HTML), **competitor-profiling / competitors / competitor-x-ray / funnel-spy** (category benchmark rows), **cold-email / outreach-personalizer** (the 4-email sequences), **pdf-report-generator** (the attractive PDF output).

## Data integrity rules

1. **Ad counts** come from Google Ads Transparency (region IN), re-checked on 02 OCT 2026 at generation time (Licious + Anand Sweets re-verified the same day).
2. **Every email** was crawled from the lead's own site/footer/help-centre/corporate pages. `contact_source` in each lead JSON states exactly where. No guessed, generic or formation addresses.
3. **Reporting vs estimates**: reported financials are labelled "reported"; third-party size estimates are labelled as estimates.
4. **What was NOT verified is stated**: e.g. Third Wave's audit says Google is verified at zero and Meta was not checked in that pass; Chai Point's contact_source notes the own-site footer confirmation is still pending.
5. **Live site defects are quoted verbatim** — Akshayakalpa's footer placeholder text and Frozen Bottle's footer 404 were captured from live HTML on 02 OCT 2026.
6. **No duplicates** with the agency's existing 100 D2C leads or the Solar pipeline; the 11 brands are registered in `data/seen_leads.json` (day 3).

## Regenerating

```bash
cd niches/food-bengaluru
pip install --break-system-packages reportlab openpyxl pymupdf
python3 scripts/build_attractive_audits.py    # audits/ (attractive format)
python3 scripts/build_master_excel.py         # Food-Bangalore-ALL-IN-ONE.xlsx
```
