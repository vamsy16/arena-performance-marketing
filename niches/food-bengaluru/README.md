# Food / Bengaluru — Performance Audit Pack (Smart Pursuit)

> Lives inside the **arena-performance-marketing** repo as the Food/Bengaluru niche (moved out of ServiceNowDocs on 02 Oct 2026).

**11 leads · 11 branded audit PDFs · 44 follow-up emails · every number verified live on 02 OCT 2026.**

## What's in here

| Path | What it is |
|---|---|
| `LEADS-INDEX.csv` | Master list: brand, website, niche, score, live Google ad count, crawled lead email, phone, entity, file paths |
| `audits/*.pdf` | 2-page branded audit per lead (same format as the existing Smart Pursuit audits) |
| `outreach/*-outreach-templates.md` | 4-email sequence per brand (Day 1 / 3 / 7 / 14) |
| `ALL-EMAIL-SEQUENCES.md` | **All 44 emails in one file** — easiest place to copy from |
| `leads/*.json` | Structured lead data (source of truth for the PDFs) |
| `scripts/` | Generator: `build_food_leads.py` rebuilds every PDF + outreach file from the lead data |

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

## Data integrity rules used

1. **Every ad count** comes from Google Ads Transparency, re-checked on 02 OCT 2026 (Licious + Anand Sweets re-verified the same day the PDFs were generated).
2. **Every email** was crawled from the lead's own site/footer/help-centre (or their own published corporate page). No guessed or generic/formation addresses.
3. **Third-party estimates are labelled as such** in the audits (e.g. company-size estimates) — sourced facts and reported figures are attributed.
4. **What was NOT verified is stated**: the Third Wave audit says explicitly that Google is verified at zero and Meta was not checked in that pass.
5. **Live site defects are quoted, not invented** — e.g. Akshayakalpa's footer placeholder text and Frozen Bottle's footer 404 were both captured from live HTML on 02 OCT 2026.
6. **No duplicates** with the existing Smart Pursuit lead pool (100 leads checked — none of these 11 brands appear).

## Regenerating

```bash
cd niches/food-bengaluru
pip install --break-system-packages reportlab
python3 scripts/build_food_leads.py     # rewrites leads/, audits/, outreach/
```
