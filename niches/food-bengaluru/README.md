# Food / Bengaluru — Performance Audit Pack (Smart Pursuit)

> Lives inside the **arena-performance-marketing** repo as the Food/Bengaluru niche.
> Format: Smart Pursuit **Paid Media & Measurement Audit** (evidence format — measured values only).

**21 leads · 21 audit PDFs · 84 follow-up emails · 1 master Excel · every fact verified live on 02–03 OCT 2026.**

| Batch | Leads | Verified on | Notes |
|---|---|---|---|
| Batch 1 | 11 | 02 OCT 2026 | Original pack (Licious, Cothas, Anand Sweets, Chai Point, The Baker's Dozen, Early Foods, iD Fresh Food, Third Wave Coffee, Akshayakalpa, Milky Mist, Frozen Bottle) |
| Batch 2 | 10 | 03 OCT 2026 | Added 3 Oct 2026: SMOOR, Sid's Farm, Barbeque Nation, Millet Amma, Adukale, Organic Mandya, Pure & Sure, Eat Better Co, Brik Oven, Araku Coffee |

## Start here

| Path | What it is |
|---|---|
| **`Food-Bangalore-ALL-IN-ONE.xlsx`** | **Everything in one workbook — 14 sheets**: README, Leads, Emails (all 84), Leaks & Roadmap, You vs Competitor, Expected ROI, Audit Basis (sources), Skills Used, Findings (severity+evidence), Opportunity Score, Coverage (measured vs not), Evidence Register, Verify These (links), Cannot be verified |
| `audits/*-paid-media-measurement-audit.pdf` | One audit per lead — 21 files, all in the canonical Smart Pursuit name (5–6 pages: cover metrics with the logo, contents + method, live ad account, severity-ranked findings with the raw measurement quoted, coverage, evidence register, opportunity score /20, qualification, next steps) |
| `VERIFY-THE-DATA.md` | Every claim in every audit, mapped to the exact public URL where you can check it yourself |
| `ALL-EMAIL-SEQUENCES.md` | All 84 emails in one file (4 per brand: Day 1 / 3 / 7 / 14) |
| `outreach/*-outreach-templates.md` | Per-brand email file |
| `leads/*.json` | Structured lead data incl. `contact_source` (the exact page each email was crawled from) |
| `LEADS-INDEX.csv` | Flat lead table (21 rows) |
| `assets/` | **Brand asset — put the real Smart Pursuit logo here** as `smart-pursuit-logo.png` and every audit + the workbook picks it up on regeneration (see `assets/README.md`) |
| `scripts/` | Rebuild everything: `build_batch2.py` (batch-2 leads + audits + outreach + indexes), `build_evidence_audits.py` (batch-1 audits), `build_master_excel.py`, `build_verify_guide.py` |

## The 21 leads

| # | Brand | Lead email (crawled from their own properties) | Live Google ads | Score |
|---|-------|-----------------------------------------------|-----------------|-------|
| 1 | Akshayakalpa Organic | support@akshayakalpa.org | 400 | 8/10 |
| 2 | Anand Sweets | care@anandsweets.net | 58 | 8/10 |
| 3 | Barbeque Nation | feedback@barbequenation.com | 34 | 8/10 |
| 4 | Milky Mist | customercare@milkymist.com | 3 | 8/10 |
| 5 | Millet Amma | eatright@milletamma.com | 80 | 8/10 |
| 6 | Organic Mandya | support@organicmandya.com | 67 | 8/10 |
| 7 | SMOOR | info@smoorchocolates.com | 22 | 8/10 |
| 8 | Sid's Farm | wecare@sidsfarm.com | 35 | 8/10 |
| 9 | iD Fresh Food | customercare@idfreshfood.com | 1 | 8/10 |
| 10 | Adukale | info@adukale.com | 13 | 7/10 |
| 11 | Araku Coffee | customercare@arakuoriginals.com | ~200 | 7/10 |
| 12 | Brik Oven | theteam@brikoven.com | 25 | 7/10 |
| 13 | Chai Point | customercare@chaipoint.com | 56 | 7/10 |
| 14 | Cothas Coffee | customercare@cothas.com | 77 | 7/10 |
| 15 | Early Foods | hello@earlyfoods.com | 30 | 7/10 |
| 16 | Eat Better Co | care@eatbetterco.com | 29 | 7/10 |
| 17 | Licious | talktous@licious.com | ~300 | 7/10 |
| 18 | Pure & Sure | info@pureandsure.in | 37 | 7/10 |
| 19 | The Baker's Dozen | fresh@thebakersdozen.in | 35 | 7/10 |
| 20 | Third Wave Coffee | orders@thirdwavecoffee.in | 0 | 7/10 |
| 21 | Frozen Bottle | vipul@frozenbottle.in | 11 | 6/10 |

## Skills used to build each audit

`performance-lead-audit` orchestrating: **ads** (Google Ads Transparency + Meta Ad Library live counts, advertiser entities, destinations), **ad-creative** (formats, fatigue, refresh systems), **copywriting** (hook/angle analysis from live ad copy), **cro** (destination-path and defect audit), **analytics + attribution** (GTM/GA4/Ads/pixel findings from live HTML), **competitor-profiling** (category comparison rows), **cold-email / outreach-personalizer** (the 4-email sequences), **pdf-report-generator** (the audit PDF output).

## Data integrity rules (applied to every lead)

1. **Ad counts** come from Google Ads Transparency (region IN) and Meta Ad Library (country IN), read on the crawl date and re-checked at generation time. Where the platform's own header and pagination disagree, both figures are reported — they answer different questions.
2. **Every email** was crawled from the lead's own site, footer, cart or policy pages. `contact_source` in each lead JSON names the exact page. No guessed, generic or formation addresses.
3. **No projections.** The audits contain measured values only. Where something could not be measured it reads *unavailable* or *not measured* — never zero, never estimated. Spend, ROAS, CPA and conversion rates are never stated. No ROI projection is made for the ten batch-2 leads.
4. **A tag is never called absent from one method.** If a pixel or tag is not visible in the page source, the audit says so and explains that it could still fire through a tag manager or platform layer.
5. **Live defects are quoted verbatim**, with the URL or page-source string needed to reproduce them.
6. **No duplicates** with the agency's existing pipelines — all 21 brands are registered in `data/seen_leads.json`.

## Honest notes about batch 2

- **Nine of the ten batch-2 brands are Bengaluru-based or have a verifiable Bengaluru presence** (published Bengaluru addresses, store locators, the brand's own Bangalore delivery or founder campus copy — each cited in the audit and in `VERIFY-THE-DATA.md`). **Eat Better Co is the exception**: its own contact page publishes a Jaipur registered address and a pan-India corporate-gifting operation, so it is labelled that way rather than presented as a Bengaluru brand.
- **Meta keyword counts are noisy.** Keyword searches return unrelated advertisers, so the audits quote brand-owned creatives by library ID and running-since date, and mark the rest *not measured* rather than citing a keyword count.
- **Some archived Google creatives display Google's removal notice.** Where that appears it is quoted as Google's own archive text on that creative, with the date it was last shown — not as a finding against the brand.

## Regenerating

```bash
cd niches/food-bengaluru
pip install --break-system-packages reportlab openpyxl pymupdf
python3 scripts/build_batch2.py            # batch-2 leads, audits, outreach, ALL-EMAIL-SEQUENCES.md, LEADS-INDEX.csv
python3 scripts/build_evidence_audits.py   # batch-1 audits (if needed)
# (the real logo in assets/ is applied automatically by both audit builders)
python3 scripts/build_verify_guide.py      # VERIFY-THE-DATA.md (all 21)
python3 scripts/build_master_excel.py      # Food-Bangalore-ALL-IN-ONE.xlsx
```
