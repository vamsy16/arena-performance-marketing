# Food / Bengaluru — Smart Pursuit paid-media evidence pack

> **41 leads total:** 21 legacy leads (Batches 1–2), 10 Batch 3 leads, and 10 new Batch 4 leads. Batch 4 was source-checked 04 Oct 2026; earlier batches and records are preserved. The 21 legacy leads were not revalidated in this update.

## Start here

| Path | Contents / status |
|---|---|
| `Food-Bangalore-ALL-IN-ONE.xlsx` | Master workbook with 41 leads, 164 emails, findings, scores, source links, coverage, and batch/data status. Legacy ROI content remains archived and is not a current forecast. |
| `Food-Bangalore-BATCH-3-EMAILS.xlsx` | Preserved one-sheet export of the 10 Batch 3 leads. |
| `Food-Bangalore-BATCH-4-EMAILS.xlsx` | New one-sheet export of the 10 Batch 4 leads with Subject, Body 1–4, and audit attachment name. |
| `audits/*-paid-media-measurement-audit.pdf` | 41 per-lead PDFs. Batch 3 and Batch 4 reports are checked for exactly five pages; previous formats are preserved and not revalidated here. |
| `VERIFY-THE-DATA.md` | Claim-to-public-URL rows for prior batches plus the new Batch 4 findings, source register and contact provenance. |
| `ALL-EMAIL-SEQUENCES.md` | 164 email messages across the preserved batches; Batch 4 adds 40 new messages. |
| `outreach/*-outreach-templates.md` | Per-lead, four-touch email files; Batch 4 routes and contact provenance are explicit. |
| `leads/*.json` | 41 structured lead records. Batch 4 JSON includes contact provenance, direct Meta IDs, source map, findings, score bases and four outreach emails. |
| `LEADS-INDEX.csv` | Flat index for all 41 leads, with batch vintage and Google status caveats. |
| `data/batch3_records.json` / `data/batch4_records.json` | Canonical source records for the two source-checked batches; Batch 4 stores the source notes, findings, score bases and email briefs used by the builder. |
| `data/seen_leads.json` | Updated deduplication registry; 141 registered brands after Batch 4. |
| `scripts/build_batch3_deliverables.py` | Preserved incremental Batch 3 builder. |
| `scripts/build_batch4_deliverables.py` | Batch 4 one-time incremental append builder; the duplicate guard blocks another run against the completed pack. Do not run legacy-only `build_master_excel.py`. |

## Batch history and data vintage

| Batch | Leads | Snapshot | Status |
|---|---:|---|---|
| Batch 1 | 11 | 02 Oct 2026 | Legacy snapshot; preserved, not rechecked on 04 Oct. |
| Batch 2 | 10 | 03 Oct 2026 | Legacy snapshot; preserved, not rechecked on 04 Oct. |
| Batch 3 | 10 | 04 Oct 2026 | Source-checked public-evidence batch; preserved. |
| Batch 4 | 10 | 04 Oct 2026 | New source-checked batch; one selected evidence-led audit per lead. |

## Batch 3 — preserved source-checked leads

| Brand | Published route | Google evidence status | Public-evidence fit |
|---|---|---|---:|
| Aubree | `connect@aubree.in` | NOT MEASURED | 8.5 / 10 |
| Nandhana Palace | `customerservices@nandhanahotels.com` | NOT MEASURED | 7.5 / 10 |
| Byg Brewski | `gm.sjp@bygbrewski.com` | NOT MEASURED | 9.0 / 10 |
| Hatti Kaapi | `info@hattikaapi.in` | NOT MEASURED | 9.0 / 10 |
| MTR Foods | `mediacell@orklaindia.com` | NOT MEASURED | 8.5 / 10 |
| Popeyes India | `wecare@popeyes.in` | NOT MEASURED | 8.0 / 10 |
| Sagar Ratna | `customercare@sagarratna.in` | NOT MEASURED | 7.5 / 10 |
| McDonald's India | `corpcomm@mcdonaldsindia.com` | NOT MEASURED | 8.5 / 10 |
| Starbucks India | `contact@tatastarbucks.com` | CHECKED — attribution not established | 7.0 / 10 |
| Krispy Kreme India | `manish.ramu@curefoods.in` | CHECKED — domain results associated with Curefoods; product attribution not established | 8.5 / 10 |

## Batch 4 — new leads

| Brand | Published first-party route | Google evidence status | Public-evidence fit |
|---|---|---|---:|
| Theobroma | `marketing@theobroma.in` | CHECKED — current brand-specific activity not established | 9.0 / 10 |
| The Belgian Waffle Co. | `marketing@bloombay.in` | CHECKED — current brand-specific activity not established | 8.0 / 10 |
| Behrouz Biryani | `help@behrouzbiryani.com` | CHECKED — current brand-specific activity not established | 8.5 / 10 |
| Bakingo | `care@bakingo.com` | CHECKED — current brand-specific activity not established | 8.5 / 10 |
| Taco Bell India | `tacobellcare@burmanhospitality.com` | CHECKED — current brand-specific activity not established | 8.5 / 10 |
| Wow! Momo | `info@wowmomo.co.in` | CHECKED — no domain-query results (not proof of no activity) | 8.0 / 10 |
| Polar Bear | `polarbear@polarbear.co.in` | CHECKED — no domain-query results (not proof of no activity) | 8.0 / 10 |
| Jumboking | `customersupport@jumboking.co.in` | CHECKED — current brand-specific activity not established | 8.5 / 10 |
| Swiggy | `akanksha.j@swiggy.in` | CHECKED — no Swiggy consumer-brand Google creative established | 9.0 / 10 |
| Chaayos | `letstalk@chaayos.com` | CHECKED — no domain-query results (not proof of no activity) | 8.5 / 10 |

## Evidence and scoring limits

- The five-dimension public-evidence-fit score is triage only (/20, displayed /10), not performance, revenue, probability, spend, forecast, conversion or ROI.
- Each selected Meta card was individually opened on 04 Oct 2026. Reports record the named page, Sponsored and Active status, start date and direct Library ID/link. One selected card is not an account-wide inventory count; live inventory can change.
- Google Ads Transparency views are India-region any-time/domain queries. Mixed advertiser results, previews and zero-result queries do not establish current brand activity or its absence. No brand-specific current Google activity is claimed without an individual creative tied to brand and advertiser.
- Bengaluru context comes from explicit first-party material. It does not prove ad audience targeting. Spend, ROAS, CPA, orders/bookings, conversions, site tags/pixels and event firing are unavailable/not measured unless a separate check is cited; no estimates, benchmarks or uplift claims are used.
- Published email addresses are first-party routing contacts, not verified paid-media buyers. Taco Bell's official routing email is published by master franchisee Burman Hospitality, whose form includes a Marketing and Media category; its Bengaluru locator content was available only in first-party search-index snippets because the direct fetch returned HTTP 500. Polar Bear's displayed customer-care address differs from its mailto target; verify before sending.
- Locality / destination caveats: Taco Bell India's direct locator fetch returned HTTP 500; its Bengaluru outlet evidence is from first-party indexed snippets only. The Belgian Waffle Co.'s indexed Bengaluru locator snippets could not be reopened (deep links returned 404), and its selected Maps short link resolved to an unrelated place; Chaayos' Dine@99 Maps short link returned Dynamic Link Not Found; Swiggy is a delivery platform, not a restaurant, and its selected card's rendered restaurant-listing destination varied across captures (Ludhiana in the latest fetch; Mumbai in a prior capture); Wow! Momo's selected offer names other cities; Jumboking's selected card is Kolkata-specific.
- Batch 3's Sagar Ratna locator uncertainty and Starbucks dynamic contact-page fetch caveat remain documented in the prior section of `VERIFY-THE-DATA.md`; those records were not revalidated in Batch 4.
- The workbook's Legacy ROI Archive is retained only for traceability and is not a current forecast.

## Step 0 — repositories and skills reviewed

- **Used — `vamsy16/arena-performance-marketing`:** the `REUSABLE-PROMPT.md` playbook and bundled `skills/ads`, `skills/attribution`, `skills/analytics`, and `skills/cold-email` informed the evidence boundaries, event/measurement vocabulary and concise four-touch outreach. The bundled `skills/auto-lead-finder` and `skills/lead-prospecting` were reviewed but not run because their generated/keyword-based pools and estimated scoring conflict with the live-evidence rules.
- **Used in part — `vamsy16/claude-ads`:** `skills/ads-audit` and `skills/ads-attribution` were read for source lineage, evidence coverage, missing-inputs and attribution boundaries. Their authenticated account-audit procedures were not represented as completed because no private account exports were available.
- **Used — `vamsy16/marketingskills`:** `skills/analytics` informed the distinction between event definitions and observed event firing; no tag/pixel absence is claimed.
- **Reviewed, not run — `vamsy16/coldoutboundskills`:** `skills/cold-email-starter-kit` and `skills/campaign-copywriting` were checked. The infrastructure/launch and interactive approval flows were not part of the request; the local cold-email skill was used for the prepared source-led sequence.
- **No usable skill / not used:** `vamsy16/performance-marketing`, `vamsy16/lead-scraper`, and `vamsy16/smart-pursuit-agency` had no usable `SKILL.md` in the inspected trees. `vamsy16/lead-gen-kit` contains a Google Maps scraping funnel, irrelevant to this manually verified ad-library/first-party workflow. `claude-seo` and `Brand-building-skills` were outside scope. `arena-solar` was empty; other `arena-*` repos covered unrelated verticals or workflows and were not run. `arena-analytics` was not used because its prospecting/roadmap workflow includes unsupported projections that conflict with the user's rules.

## Batch 4 builder (one-time append)

```bash
.venv/bin/python niches/food-bengaluru/scripts/build_batch4_deliverables.py
```

The one-time run validated unique names/domains against the root and niche-local registries, every existing `niches/*/leads/*.json`, and niche CSV inventories; it checked contact/source provenance, score arithmetic and finding source IDs, then appended the new PDFs and exports without reconstructing earlier workbook rows. The duplicate guard intentionally rejects another run against this completed registry/workbook. To regenerate, restore the pre-Batch-4 pack state first.
