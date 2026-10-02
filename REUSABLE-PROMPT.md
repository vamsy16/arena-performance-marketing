# REUSABLE PROMPT — Smart Pursuit lead-audit pack (any niche + city)

Paste the block below into a new chat. Change only the two lines marked **«FILL IN»**.

---

## THE PROMPT

```
You are running a Smart Pursuit performance-marketing lead audit pack.

NICHE: «FILL IN»            (e.g. D2C skincare / specialty coffee / solar EPC)
CITY / REGION: «FILL IN»    (e.g. Bengaluru, India)

=== STEP 0 — READ MY REPOS FIRST (do not skip this) ===
I keep my marketing intelligence across many GitHub repos, not just one. Before
planning anything, list them and read the relevant ones:

    gh repo list vamsy16 --limit 200

Then open and REUSE these (they contain the skills, templates and prior work this
job must be built from — do not invent your own method or layout):

  Deliverable home
    vamsy16/arena-performance-marketing     <- the pack is delivered here
      niches/food-bengaluru/                <- last finished pack; match this structure
      partha-dental-skin-hair-clinic-audit.pdf  <- the FORMAT reference; every PDF matches it
      data/seen_leads.json                  <- do-not-repeat registry
      skills/                               <- skills bundled in this repo
      AUDIT-WORKFLOW.md, HOW-TO-RUN-IN-NEW-CHAT.md  <- the established process

  Skill libraries to draw from (read what is relevant to this niche)
    vamsy16/claude-ads                      <- paid-media operations across ad platforms
    vamsy16/performance-marketing           <- performance marketing leads
    vamsy16/marketingskills                 <- CRO, copywriting, SEO, analytics
    vamsy16/claude-seo                      <- SEO/AEO/GEO sub-skills
    vamsy16/coldoutboundskills              <- cold email + outbound sequences
    vamsy16/lead-gen-kit                    <- lead discovery funnel
    vamsy16/lead-scraper                    <- email/phone extraction from sites
    vamsy16/Brand-building-skills           <- strategy, naming, positioning
    vamsy16/smart-pursuit-agency            <- agency playbooks
    vamsy16/arena-* (analytics, cro, content-marketing, email-marketing, gmb,
                    linkedin-marketing, seo-aeo-geo, smm, whatsapp-marketing,
                    youtube-marketing, solar)   <- niche prospecting systems

For each repo you use, say in your final summary WHICH skill you took from where.
If a repo is unreadable or irrelevant, say so instead of silently skipping it.

=== WHAT TO PRODUCE (per lead) ===
- audits/<brand-slug>-paid-media-measurement-audit.pdf   (the report)
- leads/<brand-slug>.json            (all data + contact_source provenance)
- outreach/<brand-slug>-outreach-templates.md   (4 emails: Day 1/3/7/14)
Plus, once for the whole pack:
- ONE master workbook (.xlsx) holding every lead, email, finding, score, source
- VERIFY-THE-DATA.md — every claim mapped to the public URL where I can check it

=== THE PDF FORMAT (match the reference exactly) ===
Page 1  Cover: navy full-bleed, SP mark + wordmark, eyebrow "PAID MEDIA & MEASUREMENT AUDIT",
        brand name, one-line subtitle, 4 white metric cards (gold left border),
        PREPARED FOR box + navy CONTACT box, footer "Smart Pursuit · email · phone  Page N of N"
Page 2  CONTENTS 01-05, then 01 METHOD bullets
Then    02 THE AD ACCOUNT (label/value table) + COVERAGE table
        (surface | MEASURED / NOT MEASURED / UNAVAILABLE | the method used)
Then    03 FINDINGS, ranked by severity — one block per finding:
        severity pill (CRITICAL/HIGH/MEDIUM/LOW/NOTE) + numbered title
        + monospace key:value EVIDENCE block quoting the raw measurement
        + italic analysis sentence
Then    03b EVIDENCE REGISTER — measurement | source | value observed | date
Then    04 OPPORTUNITY SCORE — 5 dimensions x 4 dots, "X / 20", a grade,
        and a QUALIFICATION box ("read this before acting on it")
Then    05 NEXT STEPS — numbered, each labelled LOW EFFORT / UNDER AN HOUR / HALF A DAY
Then    CTA: "Happy to walk through any of this on a short call." + GET IN TOUCH
Then    Closing panel: about this report · how to check it · SP mark

LAYOUT RULES (v3 was rejected for white space — do not repeat it):
- Sections DO NOT start on their own page. They flow continuously. Break only when a
  section genuinely cannot fit: use a CONDITIONAL break, never a forced page break.
- Target 5 pages per audit. No large white gaps; pages fill to the bottom of the frame.
- The Smart Pursuit logo (navy SP mark + gold underline + wordmark) in the top-left
  header of EVERY page, not just the cover.
- Findings: keep chip + title + evidence atomic; let the analysis flow on, so pages pack.
- Tokens: navy #0B1B2B · teal #0E7C7B · gold #F0A500 · panel #F4F7FA · rules #E8EDF3 ·
  muted #94A3B8 · CRITICAL #DC2626 on #FEE2E2 · HIGH #EA580C on #FFEDD5 ·
  MEDIUM #B45309 on #FEF3C7 · Helvetica family, Courier for evidence.

=== DATA RULES (non-negotiable — this is the selling point) ===
1. Every number is a live measurement or the brand's own published figure. No estimates,
   no benchmarks, no projections, no "expected uplift". Ever.
2. Unmeasured values read "unavailable" / "not measured". Never guess to fill a gap, and
   say so explicitly in the report.
3. Never call a tag/pixel ABSENT from one method — write "unconfirmed" unless a second
   method confirms it.
4. Never state spend, ROAS, CPA or conversion rates — no public source exists. Mark
   unavailable and explain why.
5. Date-stamp every measurement and note that ad counts move daily.
6. Before finishing, grep your own output for estimate-type words and confirm every hit
   is a disclaimer, not a claim.

MEASURE FROM (all public, no logins):
- Google Ads Transparency: adstransparency.google.com/?region=IN&domain=<domain>
- Meta Ad Library: facebook.com/ads/library (country India); individual ads at ?id=<library id>
- Site tags / title / footer / structured data: view-source of the brand's own domain
  (Ctrl+F the tag ID)
- Headers, CDN, CORS: securityheaders.com/?q=<domain> or curl -I
- The brand's own contact, FAQ, policy and results pages

=== LEAD RULES ===
- No duplicates: check data/seen_leads.json and every existing niches/ folder first.
- Emails must be crawled from THAT brand's own site / help centre / corporate pages.
  Never generic, guessed, or formation-agent addresses. Record contact_source in the
  lead JSON so provenance is auditable.
- Prefer brands with real paid activity — live creative counts are the proof.

=== WORKING STYLE ===
Take your time — slow is fine, wrong is not. Re-verify your own claims before finishing;
if you find an error in something you already produced, fix it and tell me what changed.
Human tone. No hype, no invented urgency, no AI clichés.

=== DELIVERY ===
The pack lives at niches/<niche>-<city>/ in vamsy16/arena-performance-marketing.
Push it as its own branch and give me the PR compare URL.

Your GitHub token may be READ-ONLY on that repo (403 on push). If so:
  - Stop retrying, and tell me plainly that the push was refused.
  - Give me BOTH options:
      (a) "Reconnect GitHub in Arena and grant access to arena-performance-marketing,
           then I will push it for you" — the agent keeps the branch ready to push.
      (b) A git bundle of the branch written into the workspace, so I can download it
          and push it myself with:
             git clone https://github.com/vamsy16/arena-performance-marketing.git
             cd arena-performance-marketing
             git fetch /path/to/<bundle> <branch>:<branch>
             git push -u origin <branch>
  - Test any commands you give me in a throwaway clone BEFORE sending them.
  - Never say it is delivered until you have CONFIRMED the files exist on the remote
    (check with the GitHub API or git ls-remote).

If the repo already contains an older folder for this niche, REPLACE it in the same
commit (its PDFs are preserved as renames into audits/_previous-*-format/), so there is
no mix of old and new layouts.

=== BEFORE YOU SAY YOU'RE DONE ===
Give me:
- lead count, pages per audit, total pages
- proof the integrity checks passed: no cross-brand leaks, no unsourced numbers,
  every finding present, correct page footers, logo on every page
- the VERIFY-THE-DATA.md path with one example row, so I can see the format
- which skill you used from which repo
- a plain, short list of anything you could NOT verify
```

---

## What you hand over

| # | What | Why |
|---|---|---|
| 1 | **Niche** | e.g. "D2C skincare", "specialty coffee", "solar EPC" |
| 2 | **City / region** | e.g. "Bengaluru", "Hyderabad", "all India" |

That's it — the reference PDF, the skills, the format and the dedupe registry all live in
your repos, and Step 0 tells the agent to go read them.

Optional extras that sharpen the output:

- **How many leads** (default 10–15), or a **specific competitor** to benchmark against
- **Extra exclusions** beyond `seen_leads.json` — e.g. "we already pitched X and Y"
- A **different format reference**: attach it and say *"this replaces the Partha format"*,
  otherwise the agent will try to blend the two

## Gotchas the new chat will hit

- **Agent can't push to `arena-performance-marketing`** — it's read-only for Arena's GitHub
  connection. The DELIVERY section covers both routes: reconnect, or hand you a bundle.
  If the agent starts retrying failing pushes, tell it to switch routes.
- **Stale `main` causes merge conflicts** — always `git fetch origin` and branch from
  `origin/main` *before* copying files in.
- **Fetched branches need `origin/main` locally** — `git fetch origin` before `git checkout`.
- **Layout regressions** (white space creeping back) come from findings being one unbreakable
  block — the LAYOUT RULES section is the fix.
- **Old PDFs linger** after a format change; the DELIVERY section tells the agent to remove
  the previous folder in the same commit.
