# Food / Bengaluru — Smart Pursuit paid-media evidence pack

> **66 leads total:** 21 legacy leads (Batches 1–2) and 45 source-checked leads across Batches 3–7. Batch 7 adds 6 qualified leads, checked 06 Oct 2026 (working target: 10); earlier batches and records are preserved. The 21 legacy leads were not revalidated in this update.

## Start here

| Path | Contents / status |
|---|---|
| `Food-Bangalore-ALL-IN-ONE.xlsx` | Master workbook with 66 leads, 264 emails, findings, scores, source links, coverage, and batch/data status. Legacy ROI content remains archived and is not a current forecast. |
| `Food-Bangalore-BATCH-3-EMAILS.xlsx` | Preserved one-sheet export of the 10 Batch 3 leads. |
| `Food-Bangalore-BATCH-4-EMAILS.xlsx` | Preserved one-sheet export of the 10 Batch 4 leads with Subject, Body 1–4, and audit attachment name. |
| `Food-Bangalore-BATCH-5-EMAILS.xlsx` | Preserved one-sheet export of the 10 Batch 5 leads with Subject, Body 1–4, and audit attachment name. |
| `Food-Bangalore-BATCH-6-EMAILS.xlsx` | Preserved one-sheet export of the 9 retained Batch 6 leads with Subject, Body 1–4, and audit attachment name. |
| `Food-Bangalore-BATCH-7-EMAILS.xlsx` | New one-sheet export of the six retained Batch 7 leads with Subject, Body 1–4, audit attachment, day-level source IDs, and linked contact provenance/caveats. |
| `audits/*-paid-media-measurement-audit.pdf` | 66 per-lead PDFs. Batch 3–6 five-page reports are preserved; Batch 7 has 6 source-linked audits with page counts, footer numbering and logo presence checked during generation. |
| `VERIFY-THE-DATA.md` | Claim-to-public-URL rows for prior batches plus Batch 5–7 findings, exact ad cards, Google caveats, source register and contact provenance. |
| `ALL-EMAIL-SEQUENCES.md` | 264 email messages across the preserved batches; Batch 7 adds 24 new messages. |
| `outreach/*-outreach-templates.md` | Per-lead, four-touch email files; Batch 5–7 routes and contact provenance are explicit, including the partial The Kind email caveat. |
| `leads/*.json` | 66 structured lead records. Batch 7 JSON includes contact provenance, direct Meta IDs, source map, findings, score bases and four outreach emails. |
| `LEADS-INDEX.csv` | Flat index for all 66 leads, with batch vintage and Google status caveats. |
| `data/batch3_records.json` / `data/batch4_records.json` / `data/batch5_records.json` / `data/batch6_records.json` / `data/batch7_records.json` | Canonical source records for Batches 3–7; Batch 7 stores source notes, findings, score bases, exclusions and email briefs used by the builder. |
| `data/seen_leads.json` | Updated deduplication registry; 166 registered brands after Batch 7. |
| `scripts/build_batch3_deliverables.py` | Preserved incremental Batch 3 builder. |
| `scripts/build_batch4_deliverables.py` | Preserved Batch 4 one-time incremental append builder; do not rerun against the completed pack. |
| `scripts/build_batch5_deliverables.py` | Preserved Batch 5 one-time incremental append builder; do not rerun against the completed pack. |
| `scripts/build_batch6_deliverables.py` | Preserved Batch 6 one-time incremental append builder; do not rerun against its completed pack. |
| `scripts/build_batch7_deliverables.py` | Batch 7 one-time incremental append builder; preflight blocks duplicate brands/artifacts. Do not run legacy-only `build_master_excel.py`. |

## Batch history and data vintage

| Batch | Leads | Snapshot | Status |
|---|---:|---|---|
| Batch 1 | 11 | 02 Oct 2026 | Legacy snapshot; preserved, not rechecked on 04 Oct. |
| Batch 2 | 10 | 03 Oct 2026 | Legacy snapshot; preserved, not rechecked on 04 Oct. |
| Batch 3 | 10 | 04 Oct 2026 | Source-checked public-evidence batch; preserved. |
| Batch 4 | 10 | 04 Oct 2026 | Preserved source-checked batch; one selected evidence-led audit per lead. |
| Batch 5 | 10 | 04 Oct 2026 | Preserved source-checked batch; one selected evidence-led audit per lead. |
| Batch 6 | 9 | 05 Oct 2026 | Preserved source-checked batch; one selected evidence-led audit per lead. |
| Batch 7 | 6 | 06 Oct 2026 | New source-checked batch; one selected evidence-led audit per lead; working target 10, no padding. |

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


## Batch 6 — new leads

| Brand | Published first-party route | Google evidence status | Public-evidence fit |
|---|---|---|---:|
| NIKAA Briyani | `feedback@nikaabriyani.com` | CHECKED — one result under verified NONVEE FOODS PRIVATE LIMITED; opened creative last shown 10 Feb 2026 and marked removed; current NIKAA-specific Google activity not established | 8.0 / 10 |
| Black Pearl Barbeque | `info@blackpearlmarathahalli.com` | CHECKED — no domain-query results (not proof of no activity) | 9.0 / 10 |
| Suvaii | `info@suvaii.in` | CHECKED — no domain-query results (not proof of no activity) | 9.5 / 10 |
| Gold Coins Club & Resort | `bookings@goldcoinsresort.in` | CHECKED — one result under verified advertiser Gold Coin Club; opened creative last shown 25 Sep 2026 and marked removed; resort-brand Google activity not established | 9.5 / 10 |
| Paint the Town Restaurant | `paint.the.town.workshop@gmail.com` | CHECKED — no domain-query results (not proof of no activity) | 9.5 / 10 |
| Chutney Chang | `chutneychangmr@fusionfoods.co.in` | CHECKED — no domain-query results (not proof of no activity) | 8.0 / 10 |
| Xin by MindEscapes | `enquiry@xinbymindescapes.com` | CHECKED — zero domain-query results (not proof of no activity) | 9.0 / 10 |
| Roast Aroma | `Orders.rcbkitchens@gmail.com` | CHECKED — no domain-query results (not proof of no activity) | 9.5 / 10 |
| AN’s Events & Caterers | `anusumesh.2009@gmail.com` | CHECKED — no domain-query results (not proof of no activity) | 8.5 / 10 |

### Batch 6 evidence and scope notes

- Working target: 10. 9 leads were retained after source, contact and duplicate checks; the shortfall was not filled with a weak or unresolved candidate.
- All 9 selected Meta individual cards displayed the named page/card, Sponsored and Active labels, a start date and Library ID when checked 05 Oct 2026. One selected record is not an account-wide count; public inventory may change daily.
- The candidates were checked against `data/seen_leads.json`, existing niche lead JSON/CSV files and niche-local registries. No duplicate name/domain was found.
- Cafe Luma Haus was excluded: its individually resolved active card describes a private rooftop in Koramangala, while its own site locates its cafe/event route in Madiwala/BTM Layout and does not confirm a Koramangala venue. The source links and third-party listing limitation are recorded in `VERIFY-THE-DATA.md`; it is not in the lead JSON, workbook or registry.
- Chutney Chang's official Page About provides a first-party email and location. Its linked Fusion Foods page returned HTTP 500; the reachable Page About, not an index-only corporate email, is used for contact provenance.
- Xin's own contact page publishes a Koramangala registered-office address and brand enquiry email; the registered office is not described as an outlet. Roast Aroma's official site and selected ad both identify Banashankari 6th Stage.
- NIKAA and Gold Coins Google domain queries returned company/advertiser results that were not tied to an accessible brand-identifying creative; no brand-specific current Google activity is asserted. Other Google zero-result queries are not proof of no activity.
- Public creative prices/counts (including ₹299, 75+ and BOGO wording) are advertiser statements, not independently verified current offers, menu counts or outcomes. Spend, ROAS, CPA, orders, bookings, conversions, site tags and event firing remain unavailable/not measured.
- Scores are public-evidence fit only (/20, displayed /10), with five recorded bases. They are not performance, revenue, likelihood, spend, forecast or ROI scores.

### Step 0 — Batch 6 repositories and skills reviewed

- **Used — `vamsy16/arena-performance-marketing` (deliverable home):** `REUSABLE-PROMPT.md` and the current Food/Bengaluru pack structure; the incremental B5 builder was copied and adapted. Bundled `skills/performance-lead-audit` supplied the source-led audit framing only; its numerical budget/lead thresholds were not used. Bundled `skills/cold-email` informed concise, low-friction follow-ups with a distinct reason to reply. `skills/pdf-report-generator` was reviewed but its 1–2-page ROI/guarantee format was not used; the required five-page `REUSABLE-PROMPT.md` layout and current pack builder take precedence. `skills/outreach-personalizer` templates were not used because their example formats call for unsupported counts, competitor claims or performance metrics.
- **Used — `vamsy16/claude-ads` @ `669c7608ecb50dd95c941a71fa3ca0a1c0e40512`:** [`skills/ads-research`](https://github.com/vamsy16/claude-ads/blob/main/skills/ads-research/SKILL.md) for primary-source/date lineage and unsupported-claim demotion; [`skills/ads-audit`](https://github.com/vamsy16/claude-ads/blob/main/skills/ads-audit/SKILL.md) for evidence coverage, missing inputs and unknown/partial boundaries. No authenticated account audit is represented as completed.
- **Used — `vamsy16/marketingskills` @ `59d5112e61fd9b043cb3c97d5551f7044d184ad0`:** [`skills/analytics`](https://github.com/vamsy16/marketingskills/blob/main/skills/analytics/SKILL.md) for event-definition/measurement boundaries; [`skills/attribution`](https://github.com/vamsy16/marketingskills/blob/main/skills/attribution/SKILL.md) to avoid treating an ad/click path as a conversion; and `skills/ads/references/audit-guardrails.md` for separating evidence coverage from account health and keeping unknowns out of pass/fail scores.
- **Used — `vamsy16/smart-pursuit-agency` @ `40e070ceaaf632790a03a644e6d3eb7a5dce40b2`:** `agency-skills-repo/agency-skills/01-sales-bd/lead-generation-prospecting.md` for a specific, verifiable observation in outreach; `agency-skills-repo/agency-skills/04-service-delivery/ppc-paid-media.md` for its warning not to present generated CPC/CPM/conversion benchmarks as fact. These are plain Markdown playbooks, not `SKILL.md` files.
- **Reviewed, not used — `vamsy16/coldoutboundskills`:** `skills/campaign-copywriting` requires staged user approvals and campaign proof/context that were not needed for this prepared sequence; no sending/launch tools were run. `vamsy16/arena-email-marketing` was inspected, but its sample outreach contains unsupported traffic/revenue/guarantee claims and its sequence skill targets lifecycle flows, so neither was copied.
- **Reviewed, not used — `vamsy16/arena-analytics`:** `skills/analytics-audit` depends on private account measurements and includes projected uplift/ROAS claims that conflict with this public-only brief. No such projection or audit was copied.
- **No usable skill / not used:** `vamsy16/performance-marketing` has a README and prompt/script files but no relevant `SKILL.md`; its scripts/prompts were not run. `vamsy16/lead-scraper` has no `SKILL.md` and implements automated Maps discovery/enrichment; it was not run. `vamsy16/lead-gen-kit` provides a Maps-scraping funnel, not this already-selected, hand-verified advertiser workflow; it was not run. `vamsy16/claude-seo`, `vamsy16/Brand-building-skills`, and `arena-cro`, `arena-content-marketing`, `arena-gmb`, `arena-linkedin-marketing`, `arena-seo-aeo-geo`, `arena-smm`, `arena-whatsapp-marketing`, `arena-youtube-marketing`, and `arena-solar` were irrelevant to this Food/Bengaluru paid-ad/contact audit. The bundled legacy `AUDIT-WORKFLOW.md` and `HOW-TO-RUN-IN-NEW-CHAT.md` describe mock/generated lead pools and estimated performance claims; none of those scripts or claims was run or reused.

### Batch 6 builder (one-time append)

```bash
.venv/bin/python niches/food-bengaluru/scripts/build_batch6_deliverables.py
```

The builder appends rows and files to the existing pack, validates first-party contact provenance and finding/source IDs, checks duplicates across existing niches, allows the evidence-qualified count to remain below the ten-lead working target, and verifies five-page PDF output. It intentionally rejects a second run against the completed registry/workbook.


## Batch 7 — new leads

| Brand | Published first-party route | Google evidence status | Public-evidence fit |
|---|---|---|---:|
| GO DESi | `welovetalking@godesi.in` | CHECKED — 22 any-time domain-query results; opened verified Haystack agency creative CR08057425657375752193, last shown 15 Sep 2026 and removed; no GO DESi creative tie established | 9.5 / 10 |
| Boba Bhaii | `care@bobabhai.com` | CHECKED — no domain-query results (not proof of no activity) | 9.0 / 10 |
| Deliciae | `info@deliciaecakes.com` | CHECKED — 92 any-time domain-query results; opened verified Deliciae advertiser creative CR12610092193726595073, last shown 05 Oct 2026 and removed; archive evidence only, not a current-active label | 9.0 / 10 |
| United Telugu Kitchens | `gm@telugukitchens.com` | CHECKED — no domain-query results (not proof of no activity) | 8.5 / 10 |
| The Kind Roastery and Brew Room | `thekindindia@gmail.com` (re-open before sending) | CHECKED — no domain-query results (not proof of no activity) | 8.0 / 10 |
| La Pino'z Pizza | `support@lapinozpizza.in` | CHECKED — 23 any-time domain-query results; opened verified COPENHAGEN HOSPITALITY creative CR00331488745591144449 names La Pino'z and was last shown 05 Oct 2026; last-shown is not a current-active label | 9.0 / 10 |

### Batch 7 evidence and scope notes

- Working target: 10. 6 leads were retained after individual Meta-card, first-party contact, Bengaluru-context and duplicate checks; no weaker candidate was used to fill the shortfall.
- All 6 selected Meta cards were opened individually on 06 Oct 2026 and displayed the named page, Sponsored and Active labels, start date and direct Library ID. One card is not an account-wide count; public inventory can change.
- Duplicate checks include `data/seen_leads.json` and every existing `niches/` folder's lead JSON, CSV indexes and niche-local registries. No duplicate name/domain was found among the six retained brands.
- The Kind: the official-domain indexed `/shop/` Get in Touch snippet showed `thekindindia@gmail.com`, but direct page fetch redirected and did not expose it. Re-open the live official page before sending; the contact is not a confirmed media buyer.
- United Telugu Kitchens' `gm@telugukitchens.com` is published on its Catering page specifically for catering enquiries. La Pino'z lists `support@lapinozpizza.in` for customer support and `info@lapinozpizza.in` for franchise enquiries. Other published inboxes are routing contacts only; no paid-media owner was identified.
- GO DESi's opened Google result names verified agency Haystack Marketing Services and does not expose a GO DESi creative tie. Deliciae's brand-named verified Google creative is removed and last shown 05 Oct; La Pino'z's brand-named creative under verified advertiser COPENHAGEN HOSPITALITY was last shown 05 Oct and is not labelled Active. These are not current-active Google claims. Zero-result domain queries do not prove no ads.
- The Happy Screens was excluded because the official offer and opened ad foreground private-theatre and celebration booking; food is supporting. It is not included as a lead, score, email target or registry entry; the scope decision and source links are in `VERIFY-THE-DATA.md` and the master workbook.
- All prices, product details, offers and quality/volume claims shown in creatives are advertiser copy unless explicitly stated otherwise; they were not independently verified as current terms or outcomes. Spend, ROAS, CPA, order/booking outcomes, tags/pixels, audience geography and event firing remain unavailable/not measured.
- Scores are public-evidence fit only (/20, displayed /10) with five recorded bases; they are not performance, revenue, likelihood, spend, projections, benchmarks, expected uplift or ROI.

### Step 0 — repository inventory and skill dispositions for Batch 7

The required `gh repo list vamsy16 --limit 200` inventory was run on 06 Oct 2026 before Batch 7 qualification. The returned descriptions were screened for the task-relevant libraries below. The existing six batches were the pack baseline; the one-time `build_batch6_deliverables.py` was reviewed but was not rerun. Batch 7 was appended to the existing pack without replacing earlier folders or records.

- **Used — this repository, `vamsy16/arena-performance-marketing`:** `REUSABLE-PROMPT.md`, `AUDIT-WORKFLOW.md`, `HOW-TO-RUN-IN-NEW-CHAT.md`, the Food/Bengaluru README, existing records, registry, workbook conventions and the Batches 1–6 archive. The bundled `skills/performance-lead-audit` was used only for evidence-led audit framing; `skills/ads`, `skills/analytics` and `skills/attribution` informed the public-data, event-measurement and attribution boundaries; `skills/cold-email` and its `follow-up-sequences.md` and `personalization.md` references informed concise, source-specific Day 1/3/7/14 emails. `skills/lead-prospecting` and `skills/pdf-report-generator` were reviewed; generated lead pools, local score thresholds, benchmark/ROI/guarantee examples and any conflicting PDF layout were not used. The pack's required PDF format and this incremental archive take precedence.
- **Used — `vamsy16/claude-ads` @ `669c7608ecb50dd95c941a71fa3ca0a1c0e40512`:** `skills/ads-research` for dated primary-source lineage and `skills/ads-audit` for evidence coverage and unknown/partial boundaries. No authenticated account audit is claimed.
- **Used — `vamsy16/marketingskills` @ `59d5112e61fd9b043cb3c97d5551f7044d184ad0`:** `skills/ads/references/audit-guardrails.md` to keep evidence coverage separate from account health and to keep unknowns out of pass/fail conclusions. The analytics/attribution guidance also supports the limits already recorded above; no account-level conversion or attribution claim is made.
- **Used — `vamsy16/smart-pursuit-agency` @ `40e070ceaaf632790a03a644e6d3eb7a5dce40b2`:** `agency-skills-repo/agency-skills/01-sales-bd/lead-generation-prospecting.md` for a specific, verifiable observation in each email; `agency-skills-repo/agency-skills/04-service-delivery/ppc-paid-media.md` for the warning not to present generated CPC/CPM/conversion benchmarks as fact. These are Markdown playbooks, not `SKILL.md` files.
- **Reviewed, not used — `vamsy16/coldoutboundskills`:** the outbound/campaign-copywriting material was reviewed, but its campaign approval and proof/context workflow was not needed for these prepared emails; no sending or launch tools were used.
- **Reviewed, not used — `vamsy16/arena-email-marketing` @ `8f9671be60944d23914c0077e67b101bbac25d67`:** `skills/email-sequence-generator` targets lifecycle/Klaviyo flows and the sample material includes unsupported traffic/revenue/performance claims. Neither was copied for this B2B prospecting sequence.
- **Reviewed, not used — `vamsy16/arena-analytics` @ `d05faa536865fb9d77c54afc76d36ba3dc8685f8` and `vamsy16/arena-analytics-marketing` @ `d547d0de363a427a478138f0dcd82b03b0d99846`:** both `skills/analytics-audit` materials require private account measurements and include unsupported projected ROAS/data-loss claims; no such claims or audits were reused.
- **No usable skill / not run — `vamsy16/performance-marketing`:** the repository had no relevant `SKILL.md`; its lead-finding scripts/prompts were not used. **No usable skill / not run — `vamsy16/lead-scraper`:** no `SKILL.md`; its Google Maps/site-enrichment workflow is not this manually verified ad-card workflow. **Not used — `vamsy16/lead-gen-kit`, `vamsy16/google-maps-scraper` and `vamsy16/google-maps-scraper-kit`:** Maps discovery/enrichment rather than the required first-party contact plus individually inspected paid-ad card; none was run.
- **Irrelevant to this Food/Bengaluru paid-media and direct-contact task:** `vamsy16/claude-seo`, `vamsy16/Brand-building-skills`, `vamsy16/agency-agents`, `vamsy16/arena-cro`, `vamsy16/arena-content-marketing`, `vamsy16/arena-gmb`, `vamsy16/arena-linkedin-marketing`, `vamsy16/arena-seo-aeo-geo`, `vamsy16/arena-smm`, `vamsy16/arena-whatsapp-marketing` and `vamsy16/arena-youtube-marketing`. `vamsy16/arena-solar` was listed as empty and its GitHub API contents request returned HTTP/API 409, so no skill was available. `vamsy16/arena-skill` is a generic answer-bracket skill, not a marketing evidence or prospecting skill. Inventory entries described as software/frameworks, AI infrastructure, design/engineering skill sets, video/media tools, documentation or unrelated personal projects were not used; no relevant paid-media/contact skill was identified in them.
- **Reviewed, not reused — root reference PDF `partha-dental-skin-hair-clinic-audit.pdf`:** the seven-page legacy report was inspected for archive context only. Its account-specific metrics, tracking findings and performance claims were not applicable to these Food/Bengaluru prospects and were not copied; Batch 7 follows the existing niche pack format and cites only its own source checks.
- **Workflow exclusion:** the bundled legacy `AUDIT-WORKFLOW.md` and `HOW-TO-RUN-IN-NEW-CHAT.md` contain mock/generated lead-pool and estimated-performance examples. They were read for process context, but those scripts and claims will not be run or copied. Batch 7 uses independently checked live public sources and records unknowns rather than estimates.

### Batch 7 builder (one-time append)

```bash
.venv/bin/python niches/food-bengaluru/scripts/build_batch7_deliverables.py
```

The incremental builder appends to the master workbook, email exports, source index, lead/outreach folders, verification guide and registry. It refuses duplicate records and pre-existing Batch 7 output files; the data builder preserves earlier batches and creates no estimated metrics.
