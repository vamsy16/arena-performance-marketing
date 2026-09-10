# Performance Prospecting System

> **Find brands already running performance marketing + Audit them + Write outreach that gets replies.** Built for agencies who pitch active spenders, not beginners.

**For:** `vamsy16` | **Created:** Sept 10, 2026 | **Type:** Agent Skills for Claude Code, Cursor, Codex, Copilot

This repo mixes your existing `marketingskills` (50 skills) + `claude-ads` (34) + `competitor-x-ray` + `funnel-spy` with **4 NEW custom skills** for agency prospecting.

---

## The Problem This Solves

You have 1150 skills across 103 repos (from your Team Playbook), but no workflow that does:

**Find active spenders in Meta Ad Library → Audit their funnel → Write personalized DM**

Old way: Run 6 skills manually (`ads` + `cro` + `analytics` + `competitor-profiling` + `cold-email` + `lead-gen-kit`) and stitch report yourself.

New way: **One command does it all.**

---

## 4 NEW Skills (What This Repo Adds)

### 1. `lead-prospecting` - FIND leads
**When:** "Find D2C brands running ads", "Need list of local businesses spending"

Finds brands actively spending via:
- Meta Ad Library (Country=IN, active filter, keyword search)
- Google Ads Transparency
- Instagram stalking method
- Google Maps + lead-gen-kit

**Output:** 5-10 live leads with Brand, Website/IG, Ad Library Link, Lead Score /10, Destination (Website/WhatsApp/IG)

### 2. `performance-lead-audit` - AUDIT website leads
**When:** "Audit magicbricks.com", "Analyze this lead for outreach"

7-skill teardown that orchestrates your existing skills:
- `ads` + `ad-creative` → Ad Intelligence
- `cro` → Landing Page audit
- `copywriting` → Copy angle audit
- `analytics` + `attribution` → Tracking audit
- `competitor-profiling` + `competitors` + `competitor-x-ray` + `funnel-spy` → Benchmark
- `cold-email` → Outreach personalization

**Output:** 9-point report: Executive Summary (Lead Score /10) + Ad Intel + Creative + Copy + CRO + Tracking + Competitor + 3 Quick Wins + 3 Outreach Templates

### 3. `ig-whatsapp-audit` - AUDIT no-website leads (70% of Indian leads)
**When:** Ad CTA = "Send WhatsApp Message" / "Visit Instagram Profile" / No website

Most local, salon, clinic, real estate broker, coach leads divert to IG/WhatsApp, not website. Instagram IS their landing page. WhatsApp IS their funnel.

Audits:
- Instagram Bio (5-sec test), Highlights (6 needed: Services, Results, Reviews, Price, Location, FAQ), Pinned posts, Reels, Social proof
- WhatsApp: Response time, Auto greeting, Catalog, Quick replies, Follow-up, Payment link
- Tracking gap: No pixel, no retargeting

**Output:** IG Score /10 + WhatsApp funnel audit + 3 Quick Wins (Bio makeover, WhatsApp Business setup, 1-page landing + pixel)

### 4. `outreach-personalizer` - WRITE outreach
**When:** "Write DM for this lead", "Personalize pitch"

Converts any audit into 3 templates:
- **Roast Audit:** "Found 3 leaks costing you money..." (Highest reply rate)
- **Value Loom Script:** 30-sec word-for-word Loom script
- **FOMO:** "Your competitor XYZ is doing X..."

Rules: Never start with "We are agency...", always mention specific finding (active ads count, leak), mention competitor, soft CTA "Want Loom?"

---

## How They Work Together

```mermaid
User: "Find leads" -> lead-prospecting -> List of 10 spenders
User: "Audit zouk.co.in" -> performance-lead-audit -> 9-point report
User: "IG @xyz has no website" -> ig-whatsapp-audit -> IG/WhatsApp report
User: "Write outreach" -> outreach-personalizer -> 3 DM templates
```

---

## Installation

### Option 1: Claude Code / Cursor / Codex (Recommended)

```bash
# Install this new repo
npx skills add vamsy16/performance-prospecting-system

# Also install your base marketingskills (if not already)
npx skills add vamsy16/marketingskills
npx skills add vamsy16/claude-ads
npx skills add vamsy16/competitor-x-ray
npx skills add vamsy16/funnel-spy
```

Then just say naturally:

```
"Find 5 D2C brands running ads in India"
"Audit boat-lifestyle.com for outreach"
"Audit Instagram @drbatras for WhatsApp funnel"
"Write outreach DM for Zouk audit"
```

Agent auto-picks the right skill.

### Option 2: Manual Clone (Global)

```bash
git clone https://github.com/vamsy16/performance-prospecting-system.git ~/.claude/skills/performance-prospecting-system
```

### Option 3: Project-specific

```bash
git clone https://github.com/vamsy16/performance-prospecting-system.git .claude/skills/performance-prospecting-system
```

---

## File Structure

```
performance-prospecting-system/
├── skills/
│   ├── performance-lead-audit/
│   │   └── SKILL.md (7-skill audit, orchestrates ads+cro+analytics+competitor+cold-email)
│   ├── ig-whatsapp-audit/
│   │   └── SKILL.md (IG as landing page + WhatsApp funnel)
│   ├── lead-prospecting/
│   │   └── SKILL.md (Find spenders via Ad Library)
│   └── outreach-personalizer/
│       └── SKILL.md (Roast/Value/FOMO templates)
├── templates/
│   ├── lead-input-template.csv (Bulk list template)
│   ├── magicbricks-audit-report.md (Demo audit - 11M visits, 10/10 lead score)
│   ├── performance-marketing-lead-analysis-kit.md (9-point template)
│   ├── instagram-whatsapp-lead-audit-kit.md (IG/WhatsApp checklist)
│   └── my-analysis-skills-stack.md (7-skill explanation)
├── .claude-plugin/
│   └── marketplace.json (Claude Code plugin manifest)
├── README.md (this file)
└── LICENSE (MIT)
```

---

## Demo: Magicbricks.com Audit

We ran full audit for Magicbricks.com using this system. See `templates/magicbricks-audit-report.md`.

**Lead Score:** 10/10 (enterprise, 11M visits/mo, heavy spender)
**Findings:**
- Ad Intel: Google heavy (80L-1.5Cr/mo est), Meta active, YouTube locality videos
- Creative: Only static/corporate, zero UGC/Reels, same campaign since 2023
- CRO: Homepage 8 filters + 5 CTAs = decision paralysis, slow mobile
- Tracking: GTM-WQW25Z + FB verification present, but generic retargeting
- Competitor: 99acres (12.59M visits), Housing (10.01M), NoBroker (7.02M) - NoBroker better with anti-broker UGC

**Quick Wins:**
1. Hyperlocal Reels + PMax (50 Reels: "2BHK under 80L in [Locality]" in Kannada/Hindi)
2. Abandoned Search Retargeting (User searched 3BHK Marathahalli 1.5-2Cr but didn't contact → WhatsApp + DPA)
3. NRI Funnel (USD pricing, video call tour)

**Outreach Angle for Builders (not Magicbricks itself):**
"Why pay Magicbricks Rs 2500 for shared lead? I'll get exclusive at Rs 900 via own funnel."

---

## Templates Included

- `lead-input-template.csv` - Fill Brand | Website | Instagram | Niche | Ad Link | Notes
- `performance-marketing-lead-analysis-kit.md` - What to give me vs what I deliver
- `instagram-whatsapp-lead-audit-kit.md` - Checklist + DM templates for IG/WhatsApp leads
- `PROMPT-TO-USE-IN-NEW-CHAT.md` - Copy-paste prompt for any new chat

---

## Related Repos (Your Existing 1150 Skills)

This repo is designed to work WITH your existing repos, not replace:

| Repo | Skills | When to use with this |
|------|--------|----------------------|
| `marketingskills` | 50 | Base toolkit: cro, ads, copywriting, analytics |
| `claude-ads` | 34 | Deep paid ops across 12 platforms |
| `competitor-x-ray` | 1 | X-ray competitor ICP/funnel |
| `funnel-spy` | 1 | Walk competitor funnel end-to-end |
| `lead-gen-kit` | 1 | Google Maps lead gen |

Install all: `npx skills add vamsy16/marketingskills vamsy16/claude-ads vamsy16/competitor-x-ray vamsy16/funnel-spy vamsy16/lead-gen-kit vamsy16/performance-prospecting-system`

---

## Contributing

Found a better prospecting query? Better outreach template? Open PR.

## License

MIT - Same as `coreyhaines31/marketingskills`

Built by combining `coreyhaines31/marketingskills` (Corey Haines) + custom prospecting system for `vamsy16` agency.

---

## Quick Start for New Chat

Copy-paste in any new Arena/Claude chat:

```
Run full 7-skill performance marketing audit for [WEBSITE].

Use: Ad Intelligence (Meta Ad Library India + Google Transparency), Creative, Copy, CRO, Tracking (check GTM/FB Pixel in source), Competitor, Outreach.

Give me Lead Score /10 + 3 quick wins + 3 DM templates.

Fetch site live and check Meta Ad Library India.

Website: boat-lifestyle.com
Niche: D2C
My offer: Full-service performance agency
```
