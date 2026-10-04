# Food / Bengaluru — Smart Pursuit paid-media evidence pack

> **51 leads total:** 21 legacy leads (Batches 1–2) and 30 source-checked leads across Batches 3–5. Batch 5 adds 10 leads, checked 04 Oct 2026; earlier batches and records are preserved. The 21 legacy leads were not revalidated in this update.

## Start here

| Path | Contents / status |
|---|---|
| `Food-Bangalore-ALL-IN-ONE.xlsx` | Master workbook with 51 leads, 204 emails, findings, scores, source links, coverage, and batch/data status. Legacy ROI content remains archived and is not a current forecast. |
| `Food-Bangalore-BATCH-3-EMAILS.xlsx` | Preserved one-sheet export of the 10 Batch 3 leads. |
| `Food-Bangalore-BATCH-4-EMAILS.xlsx` | Preserved one-sheet export of the 10 Batch 4 leads with Subject, Body 1–4, and audit attachment name. |
| `Food-Bangalore-BATCH-5-EMAILS.xlsx` | New one-sheet export of the 10 Batch 5 leads with Subject, Body 1–4, and audit attachment name. |
| `audits/*-paid-media-measurement-audit.pdf` | 51 per-lead PDFs. Batch 3, Batch 4 and Batch 5 reports are checked for exactly five pages; previous formats are preserved and not revalidated here. |
| `VERIFY-THE-DATA.md` | Claim-to-public-URL rows for prior batches plus Batch 5 findings, exact ad cards, Google caveats, source register and contact provenance. |
| `ALL-EMAIL-SEQUENCES.md` | 204 email messages across the preserved batches; Batch 5 adds 40 new messages. |
| `outreach/*-outreach-templates.md` | Per-lead, four-touch email files; Batch 5 routes and contact provenance are explicit. |
| `leads/*.json` | 51 structured lead records. Batch 5 JSON includes contact provenance, direct Meta IDs, source map, findings, score bases and four outreach emails. |
| `LEADS-INDEX.csv` | Flat index for all 51 leads, with batch vintage and Google status caveats. |
| `data/batch3_records.json` / `data/batch4_records.json` / `data/batch5_records.json` | Canonical source records for Batches 3–5; Batch 5 stores source notes, findings, score bases and email briefs used by the builder. |
| `data/seen_leads.json` | Updated deduplication registry; 151 registered brands after Batch 5. |
| `scripts/build_batch3_deliverables.py` | Preserved incremental Batch 3 builder. |
| `scripts/build_batch4_deliverables.py` | Preserved Batch 4 one-time incremental append builder; do not rerun against the completed pack. |
| `scripts/build_batch5_deliverables.py` | Batch 5 one-time incremental append builder; the duplicate guard blocks another run against the completed pack. Do not run legacy-only `build_master_excel.py`. |

## Batch history and data vintage

| Batch | Leads | Snapshot | Status |
|---|---:|---|---|
| Batch 1 | 11 | 02 Oct 2026 | Legacy snapshot; preserved, not rechecked on 04 Oct. |
| Batch 2 | 10 | 03 Oct 2026 | Legacy snapshot; preserved, not rechecked on 04 Oct. |
| Batch 3 | 10 | 04 Oct 2026 | Source-checked public-evidence batch; preserved. |
| Batch 4 | 10 | 04 Oct 2026 | Preserved source-checked batch; one selected evidence-led audit per lead. |
| Batch 5 | 10 | 04 Oct 2026 | New source-checked batch; one selected evidence-led audit per lead. |

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


## Batch 5 — new leads

| Brand | Published first-party route | Google evidence status | Public-evidence fit |
|---|---|---|---:|
| NATUF | `hello@natuf.in` | CHECKED — one domain result under verified Ardelle Foods Private Limited; opened creative does not establish a NATUF tie; not counted as NATUF activity | 8.0 / 10 |
| Swish Now | `support@justswish.in` | CHECKED — no domain-query results (not proof of no activity) | 7.0 / 10 |
| Thalairaj Biryani | `thalairajbiryani@gmail.com` | CHECKED — no domain-query results (not proof of no activity) | 8.5 / 10 |
| Tuk Tuk Thai India | `Tuktukthaiind@gmail.com` | CHECKED — no domain-query results (not proof of no activity) | 8.0 / 10 |
| Chelvies Coffee | `info@chelviescoffee.com` | CHECKED — no domain-query results (not proof of no activity) | 8.5 / 10 |
| Liliyum Patisserie Cafe | `support@liliyum.com` | CHECKED — brand-specific archive creative; last shown 03 Oct 2026 and marked removed for a policy violation; not current activity | 9.0 / 10 |
| Fish Mart | `holdingscitrine@gmail.com` | CHECKED — no domain-query results (not proof of no activity) | 8.5 / 10 |
| Mixnosh Art Cafe | `mixnosharts@gmail.com` | CHECKED — no domain-query results (not proof of no activity) | 9.0 / 10 |
| The Cuisine Story | `cuisinestory.info@gmail.com` | CHECKED — no domain-query results (not proof of no activity) | 8.5 / 10 |
| Sawadee | `thethaivegankitchen5@gmail.com` | CHECKED — no domain-query results (not proof of no activity) | 8.5 / 10 |

### Batch 5 evidence and scope notes

- Scores are public-evidence fit only (/20, displayed /10); they are not performance, revenue, spend, likelihood, projections, benchmarks or expected uplift. Public ad cards were re-opened on 04 Oct 2026; counts and visible versions can change daily.
- All ten leads have a selected individual Meta card shown Active and Sponsored on the capture date. Several direct URL responses also showed an unavailable/unpublished advertiser-page header while the exact card itself still rendered Active/Sponsored; those records are described card-by-card, not as proof of a functioning page or an account-wide inventory.
- Chelvies Coffee: direct card ID 1448800300746966 was visible with Bengaluru copy, Active/Sponsored status and start date in the direct advertiser-page results; a standalone fetch of that card URL returned HTTP 403. Both the direct card link and the accessible advertiser-page result are recorded in the audit and verification register.
- Fish Mart: the chosen published route, `holdingscitrine@gmail.com`, appeared in indexed contact/structured-data snippets on Fish Mart's own homepage/categories pages; static text extraction did not render the email. Verify the published route before sending. The advertiser-card label is `Quick Fish Shoppe`, linked to the Fish Mart Facebook page; no separate legal entity is inferred.
- Tuk Tuk Thai: `Tuktukthaiind@gmail.com` is printed on the official India Contact Us page under Sama Hospitality LLP. The page's Instagram link and the selected ad's Instagram handle differ; no profile equivalence is asserted. An additional indexed `Digital...` address was not used because it was not shown on the opened contact page.
- Meta's surrounding page response for Liliyum, Mixnosh Art Cafe and The Cuisine Story said the page was unpublished or deleted, while each directly opened individual card still rendered Active/Sponsored details. The reports cite that distinction; no broader page or account status is inferred.
- Google: the NATUF `.com` domain query returned a result under verified Ardelle Foods Private Limited, but the opened creative did not establish a NATUF tie. Liliyum's individual creative names Liliyum/Bengaluru and was last shown 03 Oct 2026; Google's page marked it removed for a policy violation. It is archive evidence, not a current Google-active claim. The other eight candidate-domain queries returned zero results, which is not proof of no activity.
- The Cuisine Story's selected card copy states an offer validity through 15 Oct 2026; that is the card's dated copy, not a separately validated current offer or performance result. Sawadee's first-party homepage says the Indiranagar restaurant is planned to open in November 2026; it is not described as already open.
- Website tags, pixels and event firing were not measured for these leads. No absence claim is made; private spend, ROAS, CPA, orders/bookings and conversion outcomes remain unavailable.
- Scope decision: Domino's India was not added because the official Jubilant FoodWorks profile lists Domino's and Popeyes among its franchise brands, while the existing pack records Popeyes India under Jubilant FoodWorks Limited. To avoid repeating the same corporate outreach group, the batch uses other brands. Check the [official JFL company profile](https://www.jubilantfoodworks.com/about-us/company-profile) and the existing Popeyes row in `LEADS-INDEX.csv`.

### Step 0 — Batch 5 skill and workflow review

- **Used — `vamsy16/marketingskills` at commit `59d5112e61fd9b043cb3c97d5551f7044d184ad0`:** `skills/analytics` for measurement/event-firing limits; `skills/attribution` for the boundary between public ad presence and conversion attribution; and `skills/cold-email` plus its follow-up-sequences reference for concise, low-friction Day 1/3/7/14 follow-ups.
- **Reused — `vamsy16/arena-performance-marketing`:** the root `REUSABLE-PROMPT.md`, Food/Bengaluru pack structure and the incremental Batch 4 builder as the starting template. `AUDIT-WORKFLOW.md` and `HOW-TO-RUN-IN-NEW-CHAT.md` describe older mock/generated pools and estimated claims; those scripts and claims were not run or copied.
- Other repositories marked irrelevant or without a usable skill in the preserved Step 0 review above were not re-inspected or relied on for Batch 5. The only external skills used for this batch are listed above.

### Batch 5 builder (one-time append)

```bash
.venv/bin/python niches/food-bengaluru/scripts/build_batch5_deliverables.py
```

This one-time append checked candidate names/domains against the root registry, every existing niche lead JSON/CSV and niche-local registries; it validates source/contact provenance, finding source IDs, score arithmetic and five-page PDF layout. The duplicate guard intentionally rejects a second run against the completed Batch 5 pack. Do not rerun the Batch 4 builder or reconstruct the workbook with the legacy-only script.
