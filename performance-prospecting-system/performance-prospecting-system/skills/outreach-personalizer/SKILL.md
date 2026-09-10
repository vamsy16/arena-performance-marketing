---
name: outreach-personalizer
description: "When the user has already audited a lead and needs personalized outreach copy that gets replies. Use when user says 'write DM', 'write cold email', 'outreach template', 'personalize pitch', 'Loom script'. This skill converts audit findings (from performance-lead-audit or ig-whatsapp-audit) into 3 high-converting outreach angles: Roast Audit, Value Loom, and FOMO. For full audit, see performance-lead-audit. For IG/WhatsApp leads, see ig-whatsapp-audit."
metadata:
  version: 2.0.0
---

# Outreach Personalizer - Turn Audit into Replies

You convert a performance marketing audit into personalized outreach that does NOT sound like "We are a performance agency".

## When to Use

- User has audit report and says "Write DM for this lead"
- User says "Personalize outreach", "Cold email", "Loom script"

## Input Required

- Brand Name
- Audit findings (from performance-lead-audit or ig-whatsapp-audit)
- 3 Quick Wins
- Competitor name (if any)

## 3 Outreach Frameworks (ALWAYS give all 3)

### TEMPLATE A: Roast Audit (Highest reply rate for local/D2C)

Structure: Observation + Specific leak + Competitor doing better + Soft CTA

Example:
"Saw you running 18 ads but all static - no video/UGC. Your landing page takes 4.2s to load, no sticky ATC. Your competitor GlowCo scaled to 2Cr/mo by switching to UGC + bundle offer. Found 3 leaks in your funnel - want 60-sec Loom?"

Rules:
- Mention exact active ads count
- Mention specific leak (not generic)
- Mention competitor name
- End with Loom offer, not call

Subject lines:
- "3 leaks in [Brand]'s funnel"
- "Your 12 ads vs [Competitor]'s 12"
- "Quick teardown - [Brand]"

### TEMPLATE B: Value-First Loom Script (30 sec)

Structure for video:
0-5 sec: Hook - "Saw your ad for [Product]..."
5-15 sec: 1-2 specific observations - "You have 12 static ads, no video, landing slow..."
15-25 sec: 1 quick win + social proof - "We fixed this for [Similar Brand], CPL dropped from 450 to 180..."
25-30 sec: CTA - "Want full teardown?"

Provide full word-for-word script user can read while recording Loom.

### TEMPLATE C: FOMO + Tracking Angle (Best for SaaS/B2B/Coaches)

Structure: Spend signal + Tracking gap + Solution

Example:
"You have 6 active ads to WhatsApp but no website, so you can't retarget people who clicked but didn't message - losing 70% of spend. We build 1-page tracker funnel: ad -> landing (pixel) -> WhatsApp. Now you can retarget + know which ad gave sale. Can I show how [Similar Business] did it?"

## Rules for All Templates

- NEVER start with "We are performance marketing agency..."
- ALWAYS mention specific finding from audit (active ads count, creative type, speed, etc.)
- ALWAYS mention competitor if available
- Keep DM <400 characters, Email <80 words
- End with soft CTA: "Want Loom?" / "Can I send teardown?" not "Book a call"

## Output Format

# OUTREACH FOR: [Brand]

### Template A: Roast Audit (DM - Short)
[Copy]
Subject: [3 options]

### Template B: Value Loom Script (30 sec)
[Script with timestamps]

### Template C: FOMO / Tracking Angle (Email)
[Copy]
Subject: [3 options]

### Personalization Tokens
- Brand: [Name]
- Active Ads: [Count]
- Leak 1: [Specific]
- Competitor: [Name]

## Related Skills

- `performance-lead-audit`: Full website lead audit
- `ig-whatsapp-audit`: IG/WhatsApp lead audit
- `cold-email`: B2B cold outreach sequences (existing skill)
- `copywriting`: For rewriting
