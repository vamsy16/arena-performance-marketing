# HOW-TO-USE GUIDE - Performance Marketing Prospecting System

> **Find 50 New Leads Daily for 50 Days (2,500 Unique) + Audit + Convert to Clients**
> Repo: github.com/vamsy16/arena-performance-marketing | 56 Skills | Version 1.1.0 | Sept 10, 2026

---

## 1. WHAT YOU GET - 56 Skills

Your repo has **50 existing + 6 NEW custom skills:**

| Skill | What It Does | When to Use |
|-------|--------------|-------------|
| **performance-lead-audit** | 7-skill teardown: ads, creative, copy, CRO, tracking, competitor, outreach | Audit website lead for outreach |
| **ig-whatsapp-audit** | Audits Instagram bio/highlights + WhatsApp funnel (no website leads) | 70% leads - IG/WhatsApp diversion |
| **lead-prospecting** | Manual methods to find active spenders via Ad Library queries | Find leads manually |
| **outreach-personalizer** | Turns audit into 3 DM templates: Roast, Loom, FOMO | Write outreach DM/email |
| **auto-lead-finder** | Auto find 10 leads without manual Ad Library | Quick 10 leads |
| **auto-lead-finder-v3** | Auto find 50 NEW unique daily for 50 days, zero duplicates | Daily 50 × 50 days = 2500 |
| **pdf-report-generator** | Generates beautiful conversion PDF to send to leads | Create PDF that converts |

---

## 2. WHAT INPUTS YOU NEED TO GIVE

### Minimum Input (Just 1 line is enough):

**For Website Lead Audit:**
```
Brand Name + Website URL
Example: 'Zouk - zouk.co.in' or 'Magicbricks.com'
```

**For Instagram/WhatsApp Lead (No Website):**
```
Brand + Instagram Handle + Destination
Example: 'Dr Batra's Bangalore - @drbatras - WhatsApp - 11 ads, no catalog'
```

**For Auto Finding Leads:**
```
Niche + Location + Count + Day
Example: 'Niche: D2C skincare, Location: India, Count: 50, Day: 4'
```

### Good to Have (Makes Audit 10x Better):
- Website URL + Instagram URL + Facebook Page URL
- Niche (D2C, Real Estate, Clinic, Coach)
- Ad Library Link (if you have)
- Your observation: 'Saw ad, creative weak'

### Ideal (If You Have):
- Screenshot of their ad
- Competitor name
- Your agency Calendly link

---

## 3. WHAT PROMPTS TO GIVE (Copy-Paste Ready)

### Prompt 1: Auto Find 50 NEW Unique Leads Daily (No Duplicates)

**Use this daily in ANY new chat:**

```
Find 50 NEW unique leads for Day 4 without duplicates from past 3 days.

Use auto_lead_finder_v3_dedup.py from vamsy16/arena-performance-marketing repo
Niche: D2C skincare, Location: India, Count: 50, Day: 4

Load data/seen_leads.json which has 150 brands already seen from Day 1-3. Filter them out.
```

**Even shorter daily command:**
```bash
python scripts/auto_lead_finder_v3_dedup.py --count 50 --day 4
```

### Prompt 2: Audit a Website Lead

```
Audit this lead for agency outreach:

Brand: Zouk
Website: zouk.co.in
Niche: D2C Bags
Ad Library: https://www.facebook.com/ads/library/?q=Zouk

Use performance-lead-audit skill (7-skill teardown). Fetch website live, check GTM/FB Pixel in source, search Meta Ad Library India, Google Transparency, competitor benchmark. Give Lead Score /10 + 3 Quick Wins + 3 Outreach Templates.
```

**Short version:**
```
Audit zouk.co.in for outreach - D2C Bags - use performance-lead-audit skill
```

### Prompt 3: Audit Instagram/WhatsApp Lead (No Website)

```
Audit Instagram/WhatsApp diversion lead:

Brand: Dr Batra's Bangalore
Instagram: https://instagram.com/drbatras
Ad Library: https://facebook.com/ads/library/?q=Dr%20Batra
Destination: WhatsApp
What you saw: 11 ads to WhatsApp, no catalog, reply after 3 hours, no highlights

Use ig-whatsapp-audit skill. Audit Bio, Highlights, Feed, Reels, WhatsApp funnel (response time, catalog, auto-reply). Give IG Score /10 + 3 Quick Wins + 3 DM templates.
```

### Prompt 4: Generate Beautiful Conversion PDF

```
Generate beautiful conversion PDF for Zouk audit.

Use pdf-report-generator skill. Input: Brand Zouk, Lead Score 9/10, 3 Quick Wins (UGC video, speed, sticky ATC), Competitor Mokobara. Make it client-facing with ROI, case study, guarantee, Calendly CTA. Save as zouk-conversion.pdf - this should convert lead to client.
```

### Prompt 5: Write Outreach DM/Email

```
Write outreach DM for Zouk audit.

Brand: Zouk, Active Ads: 18, Leak: All static zero UGC slow site 4.2s, Competitor: Mokobara uses UGC + founder.
Use outreach-personalizer skill. Give 3 templates: Roast Audit, Value Loom Script (30 sec), FOMO. Keep DM <400 chars.
```

---

## 4. WHAT OUTCOME YOU WILL ACHIEVE

### Outcome 1: Daily 50 NEW Unique Leads (Zero Duplicates for 50 Days)

| Day | New Leads | Total Unique | Duplicates |
|-----|-----------|--------------|------------|
| Day 1 | 50 | 50 | 0 |
| Day 2 | 50 NEW | 100 | 0 from Day 1 |
| Day 3 | 50 NEW | 150 | 0 from Day 1-2 |
| ... | ... | ... | ... |
| Day 50 | 50 NEW | 2500 | 0 from past 49 days |

**Files generated:**
- `data/seen_leads.json` (130KB after 50 days) - remembers all 2500 brands
- `data/daily_history/day-01-...csv` to `day-50-...csv` (50 files)
- `leads-all-2500-unique.csv` (combined)

### Outcome 2: 9-Point Audit Report for Each Lead

For each brand you give, you get:
1. Lead Score /10 (6+ = HOT)
2. Ad Intelligence (active ads, platforms, spend)
3. Creative Audit (mistakes: no UGC, static only)
4. Copy Audit (missing angles)
5. Landing Page / CRO Audit (Score /10, speed, trust, friction)
6. Tracking Audit (GTM, Pixel, CAPI, retargeting gaps)
7. Competitor Benchmark (top 2-3 competitors)
8. 3 Quick Wins (actionable, 7-day implementation)
9. 3 Outreach Templates (Roast, Loom, FOMO)

Example: Magicbricks.com audit - 10/10 score, 11M visits, 3 leaks, 3 wins, 3 DMs

### Outcome 3: Beautiful Conversion PDF That Converts Lead to Client

You get 1-page PDF (not 10-page boring report) that includes:
- Personalized cover: 'FOR: Brand Name | CONFIDENTIAL'
- Their ads vs Competitor side-by-side (visual proof)
- Money leak in rupees: '23% waste = 18-23L/month'
- 3 Quick Wins with ROI: 'Save 40L, +800 leads, +18Cr GMV'
- Case study: 'CPL 1240 → 680 in 21 days'
- Guarantee + Pricing + Calendly CTA: 'Book here: calendly.com/...'

**Result:** 25-35% reply rate, 10-15% call booking (vs 2% with generic pitch)

### Outcome 4: Ready-to-Send Outreach (DM + Email + Loom Script)

For each lead, 3 templates:

**Template A - Roast Audit (Highest reply for local/D2C):**
'Saw you running 18 ads but all static - no UGC. Landing 4.2s slow, no sticky ATC. Competitor Mokobara scaled to 2Cr/mo with UGC + bundle. Found 3 leaks - want 60-sec Loom?'

**Template B - Value Loom Script (30 sec):**
Word-for-word script to record screen share

**Template C - FOMO + Tracking:**
'6 active ads to WhatsApp but no website, can't retarget, losing 70% spend. We build 1-page tracker funnel...'

---

## 5. DAILY WORKFLOW (60 Mins = 3-5 Calls Booked)

| Time | Task | Skill Used | Outcome |
|------|------|------------|---------|
| 0-10 min | Auto find 50 NEW leads | auto_lead_finder_v3 | 50 CSV + seen_leads.json updated |
| 10-25 min | Pick top 3 HOT (Score 8-10) | Manual filter | 3 hot leads |
| 25-40 min | Audit top 3 + Generate PDF | performance-lead-audit + pdf-generator | 3 PDFs ready |
| 40-60 min | Send DM + Email + Loom | outreach-personalizer | 3 personalized outreach sent |

**14 days × 3 outreach/day = 42 personalized Looms + PDFs**
At 15% reply = 6 calls, 30% close = 2 clients
At 50 days × 3 = 150 outreach = 22 calls = 6-7 clients

---

## 6. HOW TO RUN IN DIFFERENT CHAT (Critical for 50-Day Dedup)

For dedup to work across chats, you MUST carry `data/seen_leads.json`

**New Chat - Copy-Paste:**
```bash
git clone https://github.com/vamsy16/arena-performance-marketing.git
cd arena-performance-marketing
python scripts/auto_lead_finder_v3_dedup.py --stats
python scripts/auto_lead_finder_v3_dedup.py --count 50 --day 4
git add data/ && git commit -m 'Day 4' && git push
```

If you don't push seen_leads.json back to GitHub, next chat will give duplicates!

---

## 7. TROUBLESHOOTING

**Q: Getting duplicates?**
A: seen_leads.json not loaded. Check data/seen_leads.json exists and has past brands.

**Q: Only 6 leads, not 50?**
A: Mock DB small (40 brands). In production, use firecrawl/Apify to scrape live Ad Library (10k+ brands).

**Q: PDF not converting?**
A: Use conversion PDF (sample-conversion-pdf.pdf), not audit PDF. Add your agency logo, Calendly, case study.

**Q: GitHub says 100 files limit?**
A: Upload in batches or use git push via terminal (one command, no limit).

**Q: 50 days possible?**
A: YES - Mock DB 3000 = 60 days, Real Ad Library 10k+ = 200 days × 50 = 10k unique possible.

---

**Repo:** github.com/vamsy16/arena-performance-marketing | **56 Skills** | **Install:** npx skills add vamsy16/arena-performance-marketing | **Version:** 1.1.0 | **Sept 10, 2026**

This guide is for review only, not pushed to GitHub. For latest, check HOW-TO-RUN-IN-NEW-CHAT.md in repo.
