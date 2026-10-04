# Food / Bengaluru — Smart Pursuit paid-media evidence pack

> **31 leads total:** 21 legacy records (previously captured 02–03 Oct 2026) plus 10 new Batch 3 leads source-checked 04 Oct 2026. The 21 legacy leads were not revalidated in this update. Batch 3 follows the evidence-only rules below.

## Start here

| Path | Contents / status |
|---|---|
| `Food-Bangalore-ALL-IN-ONE.xlsx` | Master workbook with 31 leads, 124 emails, findings, scores, source links, coverage, and a batch-vintage index. The historical ROI sheet is renamed **Legacy ROI Archive** and flagged as unverified; do not treat it as a current forecast. |
| `Food-Bangalore-BATCH-3-EMAILS.xlsx` | One-sheet export of the 10 new Batch 3 leads using the requested eight columns: Brand name, Email, Subject, Body 1–4, and Attachment Name. |
| `audits/*-paid-media-measurement-audit.pdf` | 31 per-lead PDFs. Batch 3 PDFs are exactly 5 pages each; existing Batch 1/2 PDFs are preserved in their prior formats and are not revalidated here. |
| `VERIFY-THE-DATA.md` | Claim-to-source rows for Batch 1/2 plus the new Batch 3 source register and findings. |
| `ALL-EMAIL-SEQUENCES.md` | All 124 email messages; Batch 3 adds 40 messages across ten leads. |
| `outreach/*-outreach-templates.md` | Per-lead, four-email files; Batch 3 contact provenance included. |
| `leads/*.json` | 31 structured lead files. Batch 3 JSON includes `contact_source`, contact source IDs, source register, findings, score bases and four emails. |
| `LEADS-INDEX.csv` | Flat index for all 31 leads; Batch 3 Google status is explicitly not measured or unattributed where applicable. |
| `data/batch3_records.json` | Canonical source record for the ten new leads. |
| `data/seen_leads.json` | Updated deduplication registry and daily log, reconciled to 131 registered brands. |
| `scripts/build_batch3_deliverables.py` | Incremental Batch 3 builder. Do **not** run the legacy-only `scripts/build_master_excel.py` to rebuild Batch 3. |

## Batch history and data vintage

| Batch | Leads | Snapshot | Status |
|---|---:|---|---|
| Batch 1 | 11 | 02 Oct 2026 | Legacy snapshot; preserved, not rechecked on 04 Oct. |
| Batch 2 | 10 | 03 Oct 2026 | Legacy snapshot; preserved, not rechecked on 04 Oct. |
| Batch 3 | 10 | 04 Oct 2026 | New source-checked batch; one selected evidence-led audit per lead. |

## Batch 3 — new leads

| Brand | Published email route | Google Ads status | Public-evidence fit |
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

## Evidence and scoring limits

- The score is a five-dimension **public-evidence fit /20** (displayed /10) for lead triage only. It is not performance, revenue, probability, spend, forecast, conversion or ROI.
- Meta citations use selected Library IDs and page IDs. A selected active card is not an account-wide inventory count. Keyword/unordered results are not treated as page ownership or ad targeting proof.
- Google status is **NOT MEASURED** unless the lead JSON and guide say a domain query was checked. Where results are surfaced under another entity, attribution is recorded as unconfirmed, not as brand activity or absence.
- Lead-local evidence is explicit in the creative or first-party material; no city targeting is inferred. Sagar Ratna's Bengaluru outlet remains **unconfirmed** from the locator content reviewed.
- Contact email addresses were taken from the brand's own official web/help/corporate property. These are routing contacts, not verified paid-media buyers. Starbucks' dynamic first-party contact pages returned a fetch error; their official indexed content was captured and is flagged in the report.
- Spend, ROAS, CPA, conversions, orders/bookings and event firing are unavailable/not measured. No estimates, benchmarks, projections or uplift claims are used in Batch 3.
- The old workbook's **Legacy ROI Archive** is retained only for traceability. Its historic projections were not revalidated and are not part of Batch 3 evidence.
- Ad inventory can change after the dated 04 Oct 2026 snapshot; re-open the source link before acting.

## Rebuild Batch 3

```bash
.venv/bin/python niches/food-bengaluru/scripts/build_batch3_deliverables.py
```

The script validates source references, email provenance, score arithmetic, uniqueness against the registry and existing niche lead files, appends rather than rebuilds the legacy workbook, and renders the Batch 3 PDFs and exports.
