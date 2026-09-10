---
name: ig-whatsapp-audit
description: "When the user wants to audit a lead whose Meta ads go to Instagram profile or WhatsApp, not a website. Use when Ad Library shows CTA 'Send WhatsApp Message', 'Visit Instagram Profile', 'Send Message', or no display link. Also use when user says 'Instagram audit', 'WhatsApp funnel audit', 'no website lead', 'IG as landing page'. This skill audits Instagram bio, highlights, feed, and WhatsApp Business setup as a replacement for CRO audit. For website leads, see performance-lead-audit."
metadata:
  version: 2.0.0
---

# Instagram / WhatsApp Diversion Audit

You are auditing leads who run Meta ads but divert to Instagram DM or WhatsApp, not a website. This is 70% of local, coach, salon, clinic, real estate broker, small D2C leads in India.

## When to Use

- Ad Library CTA = "Send WhatsApp Message" / "Visit Instagram Profile" / "Send Message"
- User says "This lead has no website, only Instagram"
- Brand has Instagram but no landing page

**This is NOT a website CRO audit. Instagram IS the landing page. WhatsApp IS the funnel.**

## How to Identify Destination

1. Open Meta Ad Library, look at CTA button
2. "Shop Now"/"Learn More" = Website -> use performance-lead-audit
3. "Send WhatsApp Message" = WhatsApp funnel
4. "Visit Instagram Profile" / No button = Instagram funnel
5. "Send Message" = Messenger funnel

## Audit Framework - 7 Checks

### 1. Ad Intelligence (Skill: ads)
- Active ads count, duration
- If WhatsApp ad running >21 days = profitable but leaking 60% due to no automation
- Creative: UGC vs static poster

### 2. Instagram Profile Audit (Replaces CRO - Skill: cro adapted for IG)

**Bio (5-second test):**
- [ ] Clear what + whom + where? Eg "Skin Clinic Koramangala | Acne | 5000+ patients"
- [ ] CTA + link? Linktree with booking/WhatsApp?
- [ ] Location + contact?

**Highlights (This is their menu - CRITICAL):**
- [ ] Do they have highlights? Ideal 6: Services, Results, Reviews, Price, Location, FAQ
- [ ] Covers professional?
- [ ] Most leads have 0 highlights = HOT opportunity

**Feed (Trust):**
- [ ] 3 Pinned posts? (Offer / Proof / How to book)
- [ ] Recent 9 posts structure? Before/After, Testimonials, Offers, BTS?
- [ ] Reels? Views?
- [ ] Social proof: Comments, tagged posts?

**Story + DM:**
- [ ] Active Stories daily?
- [ ] Highlights with Book Now sticker?
- [ ] Auto-reply in DM? (Test by messaging "Hi")

Score /10:
0-3 = Very weak = HOT LEAD
4-6 = Average = Good lead
7-10 = Strong = Harder to pitch, pitch scaling

### 3. WhatsApp Funnel Audit (If CTA = WhatsApp)

Test yourself: Click ad -> Send "Hi" on WhatsApp, check:

1. Response Time: <5 mins or 5 hours? (Slow = losing 80%)
2. Auto Greeting: WhatsApp Business greeting + Catalog?
3. Catalog: Products/services + prices listed?
4. Quick Replies: Saved replies or typing manually?
5. Follow-up: If no reply, follow up after 1 day?
6. Payment: Payment link or "GPay to this number"?
7. Business API vs personal number?

Common Leaks:
- Personal number, no Business API
- No night auto-reply (leads come at night)
- No catalog (sending images one by one)
- No CRM, leads lost in chat
- No retargeting (no pixel because no website)

### 4. Tracking Gap (Skill: analytics)
- No Pixel, no retargeting, running blind
- Can't know which ad gave sale
- Pitch: "1-page landing page + pixel = track + cut CPL 40%"

### 5. Creative & Copy (Skill: ad-creative + copywriting)
- For IG/WhatsApp leads, creative is EVERYTHING (no website to convince)
- Same static poster for all ads?
- Hook strong? "Acne gone in 7 days" vs "Welcome to our clinic"
- Video testimonials?

### 6. Competitor Benchmark (Skill: competitor-profiling)
Find 2 competitors in same area WITH website + good IG + WhatsApp catalog. Show side-by-side.

### 7. 3 Quick Wins + Outreach (Skill: cold-email)

**WIN 1: Instagram Bio + Highlights Makeover (1 Day)**
"Bio: Welcome -> Acne & Hair Clinic | Koramangala | 5000+ Treated | Book Free Consultation Below. Add 6 highlights + 3 pinned posts = 2x DM conversion"

**WIN 2: WhatsApp Business Setup**
"Setup Business API + auto greeting in 2 mins + catalog + quick replies + night reply = stop losing night leads"

**WIN 3: 1-Page Landing Page + Pixel (Scaler)**
"Ad -> Landing Page (pixel) -> WhatsApp. Now retarget visitors who didn't book + know exact cost per client. Scale from 30k to 1L profitably."

**Outreach Templates:**
- Roast: "No highlights, bio not clear, losing 60% clicks..."
- Value Loom: "I messaged Hi, reply after 3 hours, most clients book whoever replies in 5 mins..."
- FOMO + Tracking: "6 active ads to WhatsApp but no website, can't retarget, losing 70% spend..."

## Input Required

```
Brand: [Name]
Instagram: [instagram.com/...]
Ad Library Link: [facebook.com/ads/library/...]
Destination: WhatsApp / Instagram
What you saw: [e.g., 5 active ads, static, slow reply]
```

## Output Format

# IG/WHATSAPP AUDIT: [Brand]
**Instagram:** [URL] | **Destination:** WhatsApp/IG | **Score:** X/10

### Ad Intelligence
### Instagram Profile Audit (Bio, Highlights, Feed, Reels)
### WhatsApp Funnel Audit
### Tracking Gap
### Creative Audit
### Competitor Benchmark
### 3 Quick Wins
### Outreach Templates

## Related Skills

- `performance-lead-audit`: For website leads
- `lead-prospecting`: To find IG/WhatsApp leads
- `outreach-personalizer`: For DM copy only
