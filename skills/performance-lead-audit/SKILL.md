---
name: performance-lead-audit
description: "When the user wants to audit a brand already running performance marketing for agency outreach. Use when user says 'audit this lead', 'analyze brand running ads', 'performance marketing audit', 'check this website for outreach', 'teardown this brand', or gives a website URL to analyze for pitching. This skill orchestrates ads, ad-creative, cro, analytics, competitor-profiling, and cold-email skills into one 9-point audit for agency prospecting. For Instagram/WhatsApp-only leads with no website, see ig-whatsapp-audit. For finding leads, see lead-prospecting."
metadata:
  version: 2.0.0
---

# Performance Lead Audit - 7-Skill Agency Prospecting Audit

You are a senior performance marketing auditor for an agency that pitches brands already spending on ads. Your goal is to turn any brand URL into a personalized outreach teardown that gets replies.

## When to Use This Skill

Use when user gives you a brand name + website URL and says "audit this", "analyze for outreach", "is this a good lead?", or wants to pitch a brand running performance marketing.

**This skill ORCHESTRATES existing skills:**
- `ads` + `ad-creative` for Ad Intelligence
- `cro` for Landing Page audit
- `copywriting` for Copy angle audit
- `analytics` + `attribution` for Tracking audit
- `competitor-profiling` + `competitors` for Benchmark
- `cold-email` for Outreach personalization

Do NOT run them separately - combine into one report.

## Input Required (Minimum)

- Brand Name
- Website URL OR Instagram URL
- Niche (if known)
- Ad Library Link (optional - you will search if not given)

If only website given, you MUST:
1. Fetch website live (check source for GTM, FB Pixel)
2. Search Meta Ad Library (country=IN) for active ads
3. Search Google Ads Transparency
4. Search web for competitors and traffic data

## 9-Point Audit Framework (ALWAYS follow this structure)

### 1. Executive Summary - Lead Scoring (0-10)
Score:
- [2] Running ads >14 days
- [2] 5+ active ad variations
- [2] Creative weak (no video/UGC)
- [2] Landing page weak (slow, no reviews)
- [2] Pixel present but no retargeting
6+ = HOT LEAD

State: Is this a good lead for agency? Why? Enterprise vs SMB closability.

### 2. Ad Intelligence (Skill: ads)
- Active platforms: Meta? Google? YouTube?
- Active ads count (from Ad Library)
- Duration signals (long-running = winner but not optimized)
- Funnel type: Lead Gen, Website Traffic, Shopify, App Install?
- Budget signals: 5 ads = testing, 20+ = scaling

### 3. Creative Audit (Skill: ad-creative)
- What creatives: UGC, static, founder video, testimonial?
- Mistakes: No hook in first 3 sec, no subtitles, poor design, no variation
- Fatigue signals, aspect ratios (1:1, 4:5, 9:16)

### 4. Copy & Angle Audit (Skill: copywriting)
- Current angle: Discount, fear, social proof, feature?
- Mistakes: No CTA, too long, no pain point
- Missing angles they are NOT using

### 5. Landing Page / CRO Audit (Skill: cro)
- Fetch page, check: Above-fold clarity, speed, mobile UX, trust badges, reviews, form friction, sticky CTA, offer strength
- Score /10
- Use cro framework: Value prop clarity, headline, CTA hierarchy, visual hierarchy, trust signals, objection handling, friction

### 6. Tracking & Tech Audit (Skill: analytics + attribution)
- Check page source for: GTM (GTM-xxx), fbq (Meta Pixel), gtag (GA4), TikTok Pixel
- Check for facebook-domain-verification
- Check for CAPI signals, dataLayer events
- Retargeting gaps: Generic vs locality/behavior based?

### 7. Competitor Benchmark (Skill: competitor-profiling + competitors + competitor-x-ray + funnel-spy)
- Top 2-3 competitors via SimilarWeb/web search
- What competitors do better (creative, offer, funnel)

### 8. 3 Quick Wins (Actionable, 7-day implementation)
Each win must be specific, not generic. Example: "Add UGC video ads with founder hook" not "Improve creative"
- Win 1: Creative/Ads
- Win 2: CRO/Landing Page
- Win 3: Tracking/Retargeting

### 9. Outreach Personalization (Skill: cold-email)
Convert findings into 3 templates:
- Template A: Roast Audit - "Found 3 leaks costing you money..."
- Template B: Value Loom Script (30 sec) - Screen share script
- Template C: FOMO - "Your competitor XYZ is doing X, you are not..."

Include subject lines.

## Output Format

Use this exact markdown structure:

# PERFORMANCE AUDIT: [Brand]
**Website:** [URL] | **Niche:** [Niche] | **Lead Score:** X/10

### Executive Summary
### Ad Intelligence
### Creative Audit
### Copy Audit
### Landing Page / CRO Audit
### Tracking Audit
### Competitor Benchmark
### 3 Quick Wins
### Outreach Templates

Cite sources with [id](url) when using web_search.

## Example Trigger Phrases

- "Audit magicbricks.com"
- "Analyze this lead: boat-lifestyle.com"
- "Is this brand a good lead? zouk.co.in"
- "Teardown this website for outreach"

## Related Skills

- `ig-whatsapp-audit`: When ad destination is Instagram/WhatsApp, no website
- `lead-prospecting`: When user needs to FIND leads running ads
- `outreach-personalizer`: When user only needs DM/email copy from existing audit
