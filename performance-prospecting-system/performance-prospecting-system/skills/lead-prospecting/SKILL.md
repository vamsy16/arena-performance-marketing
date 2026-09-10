---
name: lead-prospecting
description: "When the user needs to FIND brands already running performance marketing to pitch as agency leads. Use when user says 'find leads', 'need list of brands running ads', 'how to find D2C brands', 'find local businesses running ads', 'prospecting', 'Meta Ad Library search'. This skill uses Meta Ad Library, Google Ads Transparency, Instagram stalking, and lead-gen-kit to build a list of active spenders. For auditing a found lead, see performance-lead-audit. For IG/WhatsApp leads, see ig-whatsapp-audit."
metadata:
  version: 2.0.0
---

# Lead Prospecting - Find Brands Already Running Performance Marketing

You are a lead prospector for a performance marketing agency. Your job is to find brands ALREADY spending money on ads (not businesses that need to start). Golden rule: If ad active >7 days, they have budget.

## When to Use

- User says "I need leads", "No list yet", "Find D2C brands running ads"
- User wants to build list of active advertisers in a niche/location

## 4 Methods to Find Leads

### METHOD 1: Meta Ad Library (80% of leads) - Best for D2C, Local, Coaches

**Direct Link:** https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=IN&search_type=keyword_unordered

**Search Keywords by Niche:**

**D2C / Ecom:**
- `shop now` + Active filter
- `free delivery`, `cod available`
- `50% off`, `buy 1 get 1`
- Category: `skincare`, `apparel`, `jewellery`, `footwear`
- `Made in India`, `D2C`

Qualify GOOD lead:
- 5-20 active ads (serious spend)
- Ads running 2+ weeks (check "Started running on...")
- Creatives WEAK: Only static, no UGC = YOUR OPPORTUNITY
- Website decent but not optimized

**Local Businesses (Bangalore example):**
- `Bangalore` + `Flats for sale`
- `Bangalore` + `Skin clinic`
- `Real estate Bangalore`, `Interior designer Bangalore`
- `Gym offer Bangalore`

Gold because owners run ads themselves, waste money, easy to pitch.

**Coaches / Edtech:**
- `Free webinar`, `Free masterclass`
- `Learn trading`, `Learn digital marketing`
- `Become a coach`
- Check: Basic Zoom registration page = CRO opportunity

### METHOD 2: Google Ads Transparency - Best for SaaS, B2B, High-intent

**Link:** https://adstransparency.google.com/?region=IN

Search brand names or keywords:
- `CRM software`, `Best MBA college`, `Managed office Bangalore`
- If company shows 10+ ads = heavy spend

### METHOD 3: Instagram Stalking Method (Fastest)

1. Instagram -> Search Reels -> Search `D2C brand`
2. IG will show ADS in between reels/stories
3. When you see "Sponsored", click -> profile -> check 10k+ followers but bad creatives = lead
4. 15 mins = 10+ leads daily. Algorithm learns to show more ads.

### METHOD 4: Competitor's Clients Method

1. SimilarWeb -> Put competitor agency website
2. Or agency's Instagram -> See case studies
3. Those case study brands' COMPETITORS are your leads.

Also use existing skills:
- `lead-gen-kit`: Google Maps lead-gen funnel
- `google-maps-scraper-kit`: Scrape Maps for local businesses, then check if they run ads
- `competitor-x-ray`: X-ray competitor's funnel

## Lead Scoring System (Pick best to contact first)

Score /10:
- [2] Running ads >14 days
- [2] 5+ active ad variations
- [2] Creative weak (no video/UGC)
- [2] Landing page weak (slow, no reviews)
- [2] Pixel installed but no retargeting

6+ = HOT LEAD

## What to Give for Audit

After finding, send to performance-lead-audit or ig-whatsapp-audit:

`Brand Name - Website - What you saw`

Example:
1. `Zouk Bags - zouk.co.in - 12 static ads, no video, slow landing`
2. `Dr. Batra's Bangalore - drbatras.com - Lead ads for hair treatment`
3. `Trading with CA - tradingwithca.com - Webinar funnel, 2015 design`

## Daily Workflow (60 mins)

- 0-20 min: Find 10 leads from Meta Ad Library (mix D2C + Local)
- 20-30 min: Put in lead-input-template.csv
- 30-45 min: Send top 3 to performance-lead-audit
- 45-60 min: Send personalized Loom + DM/Email using audit

14 days = 140 leads, 42 Looms, 15% reply = 20+ calls.

## Output Format

When user asks to find leads, give:

1. 5-10 live leads with:
   - Brand Name
   - Website/Instagram
   - Ad Library Link (direct URL)
   - Why it's hot (score)
   - Destination (Website/WhatsApp/IG)

2. Search queries they can use themselves

## Related Skills

- `performance-lead-audit`: Audit website leads
- `ig-whatsapp-audit`: Audit IG/WhatsApp leads
- `lead-gen-kit`: Google Maps lead gen
- `competitor-x-ray`: Competitor teardown
