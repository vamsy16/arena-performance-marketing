---
name: auto-lead-finder
description: "When user wants to automatically find brands running performance marketing without manually going to Meta Ad Library or Google Ads Transparency. Use when user says 'auto find leads', 'scrape ad library', 'give me leads automatically', 'find brands running ads without manual search'. This skill automates lead discovery using firecrawl, scraping, and APIs. For manual methods, see lead-prospecting. After finding, use performance-lead-audit to audit."
metadata:
  version: 1.0.0
---

# Auto Lead Finder - Automated Ad Library Scraping

You automatically find brands running performance marketing WITHOUT user going to Meta Ad Library or Google Transparency manually.

## Problem with Manual

Meta Ad Library and Google Transparency require:
- Manual keyword search
- JS-heavy pages that block simple fetch
- No bulk export
- Time consuming (30 mins for 10 leads)

## Automated Solution (What This Skill Does)

### Method 1: Firecrawl + Apify (Recommended - Works Now)

Use existing skills from vamsy16 account:
- `firecrawl` - LLM-ready scraping at scale, handles JS
- `crawl4ai` - Alternative scraper
- `Scrapling` - Cloudflare bypass for blocked sites

**Workflow:**
1. User gives niche + location: e.g., "D2C skincare India" or "Real estate Bangalore"
2. You generate 10 search queries (e.g., "shop now", "free delivery", "Bangalore flats for sale")
3. Use firecrawl to scrape Meta Ad Library search results:
   ```
   firecrawl scrape https://www.facebook.com/ads/library/?active_status=active&country=IN&q=skincare
   ```
4. Extract: Brand Name, Active Ads Count, Ad Library Link, Creative Type
5. Use web_search to enrich: Website, Instagram, traffic data
6. Score leads 0-10 and output CSV

**Existing skill to use:** `firecrawl` (from your 1150 skills) - handles JS rendering, bypasses blocks

### Method 2: Google Maps + Ad Check (For Local Leads)

Use `lead-gen-kit` + `google-maps-scraper-kit`:
1. Scrape Google Maps for "Skin clinic Bangalore" -> 100 businesses with website/IG
2. For each, check Meta Ad Library via API/search if they run ads
3. Filter only those with active ads = HOT leads

This is automated - no manual Ad Library browsing.

### Method 3: BuiltWith + Ad Tech Detection

Use `firecrawl` to check website source for:
- Meta Pixel (fbq)
- GTM
- Google Ads tag

If Pixel present = they run ads = lead.

### Output Format (Automated)

When user says "Find 10 D2C leads automatically", you output:

```csv
Brand,Website,Instagram,Active Ads,Ad Library Link,Destination,Lead Score,Why Hot
Zouk,zouk.co.in,@zouk,12,https://facebook.com/ads/library/?q=Zouk,Website,8,12 static ads, no video, slow site
Dr Batra's,drbatras.com,@drbatras,8,https://...,WhatsApp,9,8 ads to WhatsApp, no catalog, slow reply
```

And save to `leads-found-2026-09-10.csv`

## What You Need From User

- Niche: D2C / Local / Coach / SaaS
- Location: India / Bangalore / Pan-India
- Count: How many leads? (5, 10, 20)

Example triggers:
- "Auto find 10 D2C brands running ads in India"
- "Give me 15 real estate builders in Bangalore running Meta ads without me going to Ad Library"
- "Scrape Ad Library for skincare brands"

## Limitations & Honest Note

- Meta Ad Library is JS-heavy and blocks simple fetch (we saw this when fetching magicbricks.com Ad Library page - returned empty). Need firecrawl or Apify actor (apify.com has `meta-ad-library-scraper`)
- Google Transparency also JS-heavy
- Best automation: Use Apify's Meta Ad Library scraper (paid, $5-10 for 1000 ads) + firecrawl for enrichment
- For now, this skill gives you semi-automated workflow: generates queries + scrapes where possible + enriches via web_search

## Future: Full Automation Script

We can build Python script that:
1. Takes niche + location
2. Calls Apify API for Ad Library
3. Enriches with website fetch + pixel check
4. Scores leads
5. Outputs CSV + starts performance-lead-audit for top 3

See `scripts/auto_lead_finder.py` (to be built)

## Related Skills

- `lead-prospecting`: Manual methods + search queries (this skill automates it)
- `performance-lead-audit`: Audit found leads
- `ig-whatsapp-audit`: Audit IG/WhatsApp leads
- `firecrawl`: JS scraping
- `lead-gen-kit`: Maps lead gen
