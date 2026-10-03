# -*- coding: utf-8 -*-
"""
Evidence pack BATCH 2 — ten more Bengaluru food leads (added 3 October 2026).

Same rule as the first eleven: every value in this file is a live measurement or
the brand's own published figure. Nothing is estimated. Where a value was not
measured it reads "unavailable" or "not measured".

Measured on 3 October 2026 from:
  - Google Ads Transparency Center (region: India) — advertiser pages and domain pages
  - Meta Ad Library (country: India; active ads; keyword search)
  - The brand's own live HTML and HTTP response headers (captured from a
    GitHub-hosted fetch run on 3 October 2026 — see VERIFY-THE-DATA.md for how to
    reproduce each of these checks yourself)
  - The brand's own published pages (contact, policy, FAQ, footer text)
"""
from evidence_data import METHOD_CORE

CRAWL_DATE = "3 October 2026"


def method(site, extra=None):
    out = [m.format(date=CRAWL_DATE, site=site) for m in METHOD_CORE]
    if extra:
        out.extend(extra)
    return out


GET_IN_TOUCH = "GET IN TOUCH"

E2 = {}

# ------------------------------------------------------------- 1. SMOOR (Bliss Chocolates)
E2["smoor"] = dict(
    brand="SMOOR",
    cover_sub="Paid media and measurement audit. Every number below was read from live advertising and site data on 3 October 2026 — nothing is estimated.",
    metrics=[("22", "GOOGLE CREATIVES LIVE"), ("3", "META ADS VERIFIED BY ID"), ("5", "TAG FAMILIES DETECTED"), ("5", "FINDINGS IN THIS REPORT")],
    prepared_for_name="The SMOOR marketing team",
    prepared_for_line="smoor.in · Bengaluru, Karnataka, India",
    prepared_for_link="Prepared from public data only — no ad-account access was requested or used.",
    method=method("smoor.in"),
    ad_account_sub="Live paid inventory and measurement surface as measured on the crawl date.",
    ad_account=[
        ("Ad platforms observed", "Google (Ads Transparency Center, region India) · Meta (Ad Library, country India)"),
        ("Google creative inventory", "22 creatives live on 3 October 2026 for smoor.in, under Bliss Chocolates India Private Limited (identity verified by Google); the set includes Product Listing Ads"),
        ("Meta ads", "three brand-owned creatives verified by library ID: 1419659120007418 (since 5 August 2026), 1059529900062691 (since 3 August 2026) and 1101131689270428 (since 8 September 2026) — all landing on /pages/corporate-gifting"),
        ("Measurement tags", "Google Tag Manager GTM-WWTJQSR · GA4 G-JKGWG119TH · Google Ads AW-872198756 · Microsoft Clarity · Judge.me"),
        ("Site platform", "Shopify; Cloudflare in front; HSTS present"),
        ("Published contact", "info@smoorchocolates.com (published on the FAQ and privacy-policy pages) · +91 8822201202"),
        ("Paths that work", "/pages/contact-us → 200 · /pages/corporate-gifting → 200 · /pages/store-locator → 200"),
        ("Broken paths observed", "/pages/contact → 404 · /pages/bulk-enquiry → 404 (3 October 2026)"),
        ("Published address", "Bliss Chocolates India Private Limited, No. 1131, 100 Feet Road, Indiranagar Stage II, Sarvagna Nagar, Bengaluru 560038 (store-locator page)"),
        ("Bengaluru relevance", "the store locator lists Bengaluru experience centres and lounges (Indiranagar 560038, Whitefield and others) alongside Mumbai and Chennai"),
        ("Spend · ROAS · CPA", "unavailable (private to the advertiser)"),
        ("Crawl date", CRAWL_DATE),
    ],
    findings=[
        dict(sev="HIGH", title="Two enquiry paths return 404 while the pages that replaced them work",
             evidence="GET https://smoor.in/pages/contact           → 404\nGET https://smoor.in/pages/bulk-enquiry      → 404\nGET https://smoor.in/pages/contact-us        → 200\nGET https://smoor.in/pages/corporate-gifting → 200\n(3 October 2026)",
             reading="Nothing is broken for a customer who follows the current navigation — contact-us and corporate-gifting both load. The problem is every older link, campaign asset and directory listing still pointing at /pages/contact or /pages/bulk-enquiry: those arrive at a 404 on the pages where a buyer was ready to talk. Redirects for the two dead handles are a five-minute fix that recovers traffic you have already paid for."),
        dict(sev="HIGH", title="Product Listing Ads are carrying the account, not search creative",
             evidence="account: 22 creatives, advertiser Bliss Chocolates India Private Limited (Verified)\nPLA sample title: 'Elsa and Anna Cake | Frozen Theme Birthday Cake | Elsa & Anna Kids Designer Cake | Princess Celebration Cake by SMOOR | 1.5 Kg'\nsource: Google Ads Transparency Center, region India, 3 October 2026",
             reading="When Shopping is the visible engine, performance is decided by the feed — titles, images, price and availability — not by the ad copy. This title stacks four near-synonyms, which suggests the feed is being written for matching rather than for the shopper reading it on a phone. A feed pass is usually the cheapest lever in an account like this."),
        dict(sev="MEDIUM", title="Meta is running a corporate-gifting campaign — and the conversion behind it is not visible from outside",
             evidence="library ID 1419659120007418 (since 5 Aug 2026): 'Our handcrafted gourmet chocolates are the perfect way to show appreciation for your teams, clients and partners.' → smoor.in/pages/corporate-gifting\nlibrary ID 1059529900062691 (since 3 Aug 2026): 'Choose hampers that look premium, feel thoughtful, and fit your budget.'\nlibrary ID 1101131689270428 (since 8 Sep 2026): 'Order Premium Corporate Hampers Now'\nlanding page carries a 'Get Quote' call to action; no pixel ID is visible in the storefront HTML because Shopify loads pixel configuration through its web-pixels layer",
             reading="The B2B push is the right instinct for a chocolatier in the Diwali quarter, and the ads land on a page that exists and works. The gap is that a quote request is not an order — and nothing observable from outside confirms that the quote form fires a tracked event. Ask the team one question: which event fires on /pages/corporate-gifting when a form is submitted? If the answer is 'page view', the campaign is being judged on traffic rather than on leads."),
        dict(sev="MEDIUM", title="The live offer has an exception built into it",
             evidence="site banner (verbatim): 'Get Exclusive 10% OFF On The MRP Of All Products, Except Celebration Cakes'\ncategory pages in nav: Signature Cakes · Celebration Cakes · Diwali Special Hampers",
             reading="The exclusion covers exactly the category most people arrive for. A discount with a visible carve-out converts worse than the same discount stated plainly, and it is trivially testable: run the exception-free version on the cake landing pages for two weeks and compare."),
        dict(sev="NOTE", title="The measurement stack is complete — so the 404s are a maintenance problem, not a capability problem",
             evidence="Google Tag Manager: GTM-WWTJQSR\ngoogle tag:        AW-872198756\nga4:               G-JKGWG119TH\nreview platform:   Judge.me\nsession recording: Microsoft Clarity\nall present in the storefront page source, 3 October 2026",
             reading="A tag manager, an analytics property, a conversion tag, a review platform and session recording is a complete small-brand stack. Nothing here needs rebuilding. It also means the two dead enquiry paths are not a budget or tooling failure — they are the result of nobody owning a monthly five-minute check of the paths that paid traffic lands on. That check is the recommendation."),
    ],
    score_dims=[
        ("Measurement integrity", "GTM-WWTJQSR, GA4 and Google Ads tags all confirmed by ID, plus Clarity and Judge.me.", 4),
        ("Conversion observability", "Shopping runs to product pages and Meta to a working gifting page; the B2B quote event is not observable from outside.", 3),
        ("Brand consistency", "Premium brand, consistent storefront, live Diwali merchandising.", 4),
        ("Technical health", "Two 404s on enquiry paths; HSTS present; Cloudflare in front.", 2),
        ("Commercial fit", "Occasion-led gifting brand with a live paid account and obvious feed upside.", 4),
    ],
    grade="A",
    grade_note="a complete measurement stack and a working gifting campaign, held back by maintenance",
    qualification=("This audit reads public surfaces only. Spend, ROAS and conversion volumes are not scored — they are marked unavailable. "
                   "The 22-ad count is a one-day snapshot for the domain and will move as campaigns change. "
                   "The absence of a Meta pixel is reported as 'not observed in the storefront HTML' — a tag can live in a tag manager or an app that a page-source check cannot see."),
    next_steps=[
        ("LOW EFFORT · IMMEDIATE BENEFIT", "Restore the two dead contact paths", "Redirect /pages/contact and /pages/bulk-enquiry to a working enquiry page and put a real corporate-gifting form behind the nav item. This is where your largest order values come from."),
        ("UNDER AN HOUR", "Read the feed, not the ad copy", "Export the Shopping feed and rewrite the five longest titles for a phone screen. The Elsa-and-Anna cake title quoted in this report is the template for what needs shortening."),
        ("HALF A DAY · BIGGEST SINGLE WIN", "Install GTM and a Meta base", "One container plus the Meta pixel and Conversions API unlocks both the marketing calendar (Diwali, Valentine's, Raksha Bandhan) and the retargeting audience you do not currently have."),
    ],
)

# ------------------------------------------------------------- 2. SID'S FARM
E2["sidsfarm"] = dict(
    brand="Sid's Farm",
    cover_sub="Paid media and measurement audit. Every number below was read from live advertising and site data on 3 October 2026 — nothing is estimated.",
    metrics=[("~200", "CREATIVES IN GOOGLE ACCOUNT"), ("35", "CREATIVES POINTING AT .COM"), ("4", "TAG FAMILIES DETECTED"), ("5", "FINDINGS IN THIS REPORT")],
    prepared_for_name="The Sid's Farm marketing team",
    prepared_for_line="sidsfarm.com · Bengaluru, Karnataka, India",
    prepared_for_link="Prepared from public data only — no ad-account access was requested or used.",
    method=method("sidsfarm.com"),
    ad_account_sub="Live paid inventory and measurement surface as measured on the crawl date.",
    ad_account=[
        ("Ad platforms observed", "Google (Ads Transparency Center, region India) · Meta (Ad Library, country India)"),
        ("Google creative inventory", "≈200 creatives in the advertiser account (Sids Farm Private Limited, identity verified by Google) on 3 October 2026; 35 of them point specifically at sidsfarm.com"),
        ("Meta ads", "brand-owned creatives verified by library ID: 1682864186042714 (running since 8 April 2026, WhatsApp-click), 28227187223577653 (since 17 August 2026, app signup), 2322194535253458 (since 18 August 2026)"),
        ("Measurement tags", "GA4 G-YN4FLEL9J2 · Google Tag Manager GTM-57TDVNH · Google Tag Manager GTM-P4DXD97J · Microsoft Clarity · the store's own app config carries meta_pixel_enable: false with an empty meta_pixel_id (verbatim, 3 October 2026)"),
        ("Site platform", "Shopify; Cloudflare in front; HSTS present"),
        ("Published contact", "wecare@sidsfarm.com (published on the cart and collection pages)"),
        ("Published address", "the privacy-policy and terms pages carry a Hyderabad 500085 address — Sid's Farm is headquartered in Hyderabad and serves Bengaluru as a market"),
        ("Bengaluru relevance", "the storefront's location selector lists Bangalore, and the homepage copy reads 'If you're from Hyderabad, Bengaluru, Pune, Vijayawada … Download our app for hassle-free 7AM deliveries'"),
        ("Broken paths observed", "/pages/faq · /pages/contact · /pages/contact-us · /policies/shipping-policy · /pages/store-locator · /pages/bulk-enquiry · /pages/corporate-gifting → all 404 on 3 October 2026"),
        ("Spend · ROAS · CPA", "unavailable (private to the advertiser)"),
        ("Crawl date", CRAWL_DATE),
    ],
    findings=[
        dict(sev="HIGH", title="Seven of the storefront's standard trust pages return 404",
             evidence="GET https://sidsfarm.com/pages/faq                → 404\nGET https://sidsfarm.com/pages/contact            → 404\nGET https://sidsfarm.com/pages/contact-us         → 404\nGET https://sidsfarm.com/policies/shipping-policy → 404\nGET https://sidsfarm.com/pages/store-locator      → 404\nGET https://sidsfarm.com/pages/bulk-enquiry       → 404\nGET https://sidsfarm.com/pages/corporate-gifting  → 404\n(3 October 2026, HTTP status codes as logged)",
             reading="Every path a cautious first-time buyer looks for before paying — how do I reach you, when will it arrive, where are you — is dead. For a subscription product where the first order is a trust decision, this is the most expensive set of pages on the site. Rebuilding them is content work, not engineering work."),
        dict(sev="HIGH", title="Two Google Tag Manager containers are loading on the same storefront",
             evidence="GTM container 1: GTM-57TDVNH\nGTM container 2: GTM-P4DXD97J\nboth present in the same page source, sidsfarm.com, 3 October 2026\nalso present in the same source: GA4 G-YN4FLEL9J2, Microsoft Clarity",
             reading="Two containers is a classic symptom of a migration that never finished, and the usual result is duplicated purchase or signup events — which then makes every ROAS number you read argue with the bank. Confirm which container is live, merge the tags into it, and remove the other. This is an afternoon of work with an outsized effect on reporting trust."),
        dict(sev="MEDIUM", title="Most of the account's creative volume does not point at the website",
             evidence="advertiser account: ≈200 creatives (Sids Farm Private Limited, Verified)\ndomain sidsfarm.com: 35 creatives\nunaccounted:       ≈165 creatives point at other destinations",
             reading="The Meta side shows where they go: WhatsApp click-through creatives and app.sidsfarm.com signup ads with tracking macros attached. That is a deliberate subscription-acquisition strategy — but it also means website-based reporting cannot see most of the programme. If subscription growth is the goal, the measurement plan has to follow the creative into the app, not stop at the website."),
        dict(sev="MEDIUM", title="Meta is already run properly, and it is carrying the response burden",
             evidence="library ID 1682864186042714 — running since 8 April 2026, CTA 'Send WhatsApp message'\nlibrary ID 28227187223577653 — running since 17 August 2026, 'No diet changes. No extra effort. Just your everyday milk, now with 22g protein in every pack'\nlanding: app.sidsfarm.com/?utm_source=facebook&utm_medium=paid_social&campaign_id={{campaign.id}}&ad_id={{ad.id}}…",
             reading="Someone on the team knows what they are doing: the ad copy leads with a product change (22g protein) rather than a discount, and the tracking template passes campaign and ad IDs into the app. The gap is that none of it is joined up to the website's own reporting, so the same customer is counted in two places or in neither."),
        dict(sev="HIGH", title="The store's own configuration has the Meta pixel switched off while Meta ads are live",
             evidence="page source of sidsfarm.com, 3 October 2026 (verbatim):\n  container_id: \"GTM-57TDVNH\", measurement_id: \"G-YN4FLEL9J2\",\n  meta_pixel_enable: false, meta_pixel_id: \"\",\n  built_in_conversion_tracking: 0\nand, from Meta's Ad Library, three brand-owned creatives running since April and August 2026",
             reading="Read exactly: this is one integration — the store's own pixel setting — and it is disabled. The pixel could still be fired through GTM-57TDVNH, whose contents cannot be inspected from outside, so this is 'switched off where we can see it', not 'no measurement anywhere'. But when a brand spends on Meta for months while its storefront config says the pixel is off, the first thing to verify is which of the two is true — because that single setting decides whether the Meta spend can be optimised on purchases or only on clicks. Microsoft Clarity is installed alongside, so the session data to check it already exists."),
    ],
    score_dims=[
        ("Measurement integrity", "GTM, GA4 and Clarity confirmed — but the store's own Meta pixel setting reads disabled, and two GTM containers create duplicate-event risk.", 2),
        ("Conversion observability", "App and WhatsApp paths carry tracking macros; website reporting cannot see them.", 3),
        ("Brand consistency", "Protein-led product message is consistent across ads and app landing page.", 4),
        ("Technical health", "Seven standard paths returning 404 is a live commercial problem.", 2),
        ("Commercial fit", "Subscription dairy with real paid spend and a working Meta engine.", 4),
    ],
    grade="B",
    grade_note="a serious paid engine on a storefront with the basics missing",
    qualification=("Public surfaces only; spend, ROAS and churn are not scored because no public source exists for them. "
                   "The ≈200 creative count is the advertiser-level figure on one day, and the 35 is the subset pointing at sidsfarm.com on the same day. "
                   "Meta counts for this brand term include third-party inventory; only creatives verified on the brand's own page are quoted here."),
    next_steps=[
        ("LOW EFFORT · IMMEDIATE BENEFIT", "Publish the missing trust pages", "Contact, FAQ, shipping policy and store locator — four pages, all currently 404. These sit directly in front of a subscription decision."),
        ("UNDER AN HOUR", "Settle two settings: the double container and the pixel switch", "Confirm which of GTM-57TDVNH / GTM-P4DXD97J is live and merge the tags; then check why the store config reads meta_pixel_enable: false. Duplicate events and a disabled pixel both make every ROAS discussion unwinnable."),
        ("HALF A DAY · BIGGEST SINGLE WIN", "Join the app and the website in one report", "Bring app.sidsfarm.com signups and website orders into a single weekly view so subscription growth is measured once, on one number."),
    ],
)

# ------------------------------------------------------------- 3. BARBEQUE NATION
E2["barbequenation"] = dict(
    brand="Barbeque Nation",
    cover_sub="Paid media and measurement audit. Every number below was read from live advertising and site data on 3 October 2026 — nothing is estimated.",
    metrics=[("19", "GOOGLE CREATIVES IN YOUR ACCOUNT"), ("15", "CREATIVES NOT FROM YOUR ACCOUNT"), ("2", "DIFFERENT CODES IN ONE AD"), ("5", "FINDINGS IN THIS REPORT")],
    prepared_for_name="The Barbeque Nation marketing team",
    prepared_for_line="barbequenation.com · Bengaluru, Karnataka, India",
    prepared_for_link="Prepared from public data only — no ad-account access was requested or used.",
    method=method("barbequenation.com"),
    ad_account_sub="Live paid inventory and measurement surface as measured on the crawl date.",
    ad_account=[
        ("Ad platforms observed", "Google (Ads Transparency Center, region India) · Meta (Ad Library, country India)"),
        ("Google creative inventory", "19 creatives in the advertiser account (UNITED FOODBRANDS LIMITED, identity verified by Google); 34 creatives in total point at barbequenation.com, so a further 15 come from other advertiser accounts"),
        ("Meta ads", "brand-owned creatives verified by library ID: 1629049651915814 (since 13 September 2026, takeaway code SAVE35), 1595578738733856 (since 22 September 2026, pay-day buffet valid to 11 October 2026), 1727327792321770 (since 11 September 2026)"),
        ("Measurement tags", "Google Tag Manager GTM-TF3NNN · Meta's connect.facebook.net script is loaded on the site (the pixel ID itself is not visible in the page source) · Razorpay on the ordering side"),
        ("Site platform", "Cloudflare in front; long-lived cache policy on the marketing pages; HSTS present"),
        ("Published contact", "feedback@barbequenation.com (published on the About-Us and Contact-Us pages) · 08064058059 on the contact page"),
        ("Published address", "Barbeque Nation Hospitality Limited, Saket Callipolis, Units 601 & 602, 6th Floor, Doddakannalli Village, Varthur Hobli, Sarjapur Road, Bengaluru 560035 (contact page)"),
        ("Entity note", "the site footer names Barbeque Nation Hospitality Limited, while Google's advertiser of record for the account is the parent, UNITED FOODBRANDS LIMITED"),
        ("Bengaluru relevance", "the brand's registered office is published on its own contact page in Bengaluru (560035), and the About-Us page references Bangalore"),
        ("Broken paths observed", "/menu · /book-a-table · /locations · /order-online · /terms → all 404 on 3 October 2026 (ads point instead at /ubq-delivery and /deals/unlockspecialdeals)"),
        ("Spend · ROAS · CPA", "unavailable (private to the advertiser)"),
        ("Crawl date", CRAWL_DATE),
    ],
    findings=[
        dict(sev="HIGH", title="Fifteen creatives for your domain are paid for by accounts that are not yours",
             evidence="creatives pointing at barbequenation.com: 34\ncreatives in UNITED FOODBRANDS LIMITED:   19\ndifference:                                15\nsource: Google Ads Transparency Center, region India, 3 October 2026",
             reading="At least one other advertiser is buying traffic that lands on your domain — franchisees, delivery partners or resellers are the usual candidates. Sometimes that is welcome; more often it means brand-name auctions are being contested with your own storefront as the landing page, and your brand terms cost more than they should. It is worth knowing which of your partners is doing it."),
        dict(sev="HIGH", title="The URLs people guess — menu, locations, ordering — all return 404",
             evidence="GET https://www.barbequenation.com/menu         → 404\nGET https://www.barbequenation.com/book-a-table → 404\nGET https://www.barbequenation.com/locations    → 404\nGET https://www.barbequenation.com/order-online → 404\nad destinations observed instead: /ubq-delivery · /deals/unlockspecialdeals",
             reading="Your live ads are pointed at working pages, so the campaigns themselves are fine. The risk is everything outside the campaigns: QR codes, printed collateral, aggregator listings, old blog links and customers typing the obvious URL. Those all dead-end today, and a set of redirects fixes it in an afternoon."),
        dict(sev="MEDIUM", title="Paid social is running as a discount channel while the brand leans on experience",
             evidence="library ID 1629049651915814: 'FLAT 35% OFF on Takeaway Orders! Use code SAVE35'\nlibrary ID 1595578738733856: 'PAY DAY just got tastier! … Unlimited Buffet for 4 … Valid till 11th Oct, 2026 · 080 6405 8053'\nboth on the Barbeque Nation page, active on 3 October 2026",
             reading="Two of the three creatives sampled lead with a percentage off. Barbeque Nation's actual differentiator is the live-grill format and the ambience — the thing a discount does not explain. The coupon also expires (11 October), which means the creative needs replacing on a deadline rather than when the data says so."),
        dict(sev="MEDIUM", title="The takeaway ad's copy and its own creative show two different codes",
             evidence="ad copy (library ID 1629049651915814, running since 13 September 2026):\n  'FLAT 35% OFF on Takeaway Orders! Use code SAVE35 and get an EXTRA 35% Off'\nimage inside the same ad:\n  'BARBEQUENATION.COM — FLAT 35% Off on takeaways — Use Code SAVE5 — Book now'\nlanding page: barbequenation.com/ubq-delivery",
             reading="One of the two codes in this ad is wrong, and only the brand can say which. A customer who types the code they read in the image will either get 5% instead of 35%, or nothing at all — and either way the campaign's numbers will under-report the offer's real pull. It is a single-line creative fix, and it is worth doing before the pay-day offer expires on 11 October."),
        dict(sev="NOTE", title="The public web presence is a marketing site, not the ordering system",
             evidence="marketing pages served from barbequenation.com behind Cloudflare with a long cache policy\nordering references observed: Razorpay, /ubq-delivery\ncontact number quoted in ads: 080 6405 8053",
             reading="Splitting marketing from ordering is normal at this size. It does mean every paid click crosses a domain or a system boundary, so the conversion signal has to be carried deliberately — otherwise paid media gets credited for visits rather than for orders."),
    ],
    score_dims=[
        ("Measurement integrity", "GTM and pixel present on the marketing site; code redemption not visibly instrumented.", 3),
        ("Conversion observability", "Ordering sits behind a separate flow; cross-system attribution needs deliberate setup.", 3),
        ("Brand consistency", "Consistent identity and offer calendar across Google and Meta creative.", 4),
        ("Technical health", "Five conventional paths dead; live campaign destinations are healthy.", 3),
        ("Commercial fit", "Large multi-outlet chain actively running both Google and Meta.", 4),
    ],
    grade="A",
    grade_note="a large, well-run advertiser with structural leaks rather than creative ones",
    qualification=("Public surfaces only; the franchise and partner relationships behind the 15 unexplained creatives cannot be established from outside. "
                   "Spend, ROAS and redemption rates are not scored — no public source exists. Both ad counts are one-day snapshots."),
    next_steps=[
        ("LOW EFFORT · IMMEDIATE BENEFIT", "Redirect the five dead paths", "Menu, locations, booking, ordering and terms should each land somewhere useful. It costs one afternoon and catches every printed or typed link you have ever published."),
        ("UNDER AN HOUR", "Find out who the other 15 creatives belong to", "Pull your domain in Google Ads Transparency and check which other accounts are buying your brand traffic. Depending on who they are, this is either a conversation or a policy."),
        ("HALF A DAY · BIGGEST SINGLE WIN", "Instrument the offer codes", "Push one event per code (SAVE35 and the pay-day offer) into GA4. After that, offer performance is a report rather than an argument."),
    ],
)

# ------------------------------------------------------------- 4. MILLET AMMA
E2["milletamma"] = dict(
    brand="Millet Amma",
    cover_sub="Paid media and measurement audit. Every number below was read from live advertising and site data on 3 October 2026 — nothing is estimated.",
    metrics=[("80", "GOOGLE CREATIVES LIVE"), ("~39", "META ADS FOR BRAND TERM"), ("3", "TAG FAMILIES DETECTED"), ("6", "FINDINGS IN THIS REPORT")],
    prepared_for_name="The Millet Amma marketing team",
    prepared_for_line="milletamma.com · Bengaluru, Karnataka, India",
    prepared_for_link="Prepared from public data only — no ad-account access was requested or used.",
    method=method("milletamma.com"),
    ad_account_sub="Live paid inventory and measurement surface as measured on the crawl date.",
    ad_account=[
        ("Ad platforms observed", "Google (Ads Transparency Center, region India) · Meta (Ad Library, country India)"),
        ("Google creative inventory", "80 creatives live on 3 October 2026 under URBAN MONK PRIVATE LIMITED (identity verified by Google) — the same legal entity named in the site's own terms page — including video, local and display formats"),
        ("Meta ads", "brand-owned creative verified by library ID 1355783896518419 (running since 7 July 2026, Raagi Laddoo, landing milletamma.com/products/ragi-laddo-300g); the keyword count for the brand term is ≈39 and includes unrelated advertisers, so the verified ID is what this report relies on"),
        ("Measurement tags", "GA4 G-WH82716CE0 · GA4 G-N659GJMWCX · Google Ads AW-378561932 · Shopify · Shiprocket"),
        ("Site platform", "Shopify; Cloudflare in front; HSTS present"),
        ("Published contact", "eatright@milletamma.com (cart and collection pages) · orders@milletamma.com (terms-of-service page) · +91 7624979333"),
        ("Published address", "No. 12, K 345, Yemalur Main Road, HAL Airport Area, Bellandur, Bengaluru, Karnataka 560037 (the storefront's 'Get in touch' block)"),
        ("Bengaluru relevance", "the brand's own published address is in Bellandur, Bengaluru 560037"),
        ("Broken paths observed", "/pages/faq · /pages/store-locator · /pages/bulk-enquiry · /pages/corporate-gifting → all 404 on 3 October 2026"),
        ("Spend · ROAS · CPA", "unavailable (private to the advertiser)"),
        ("Crawl date", CRAWL_DATE),
    ],
    findings=[
        dict(sev="HIGH", title="Two GA4 properties are live on the same storefront",
             evidence="analytics id 1: G-WH82716CE0\nanalytics id 2: G-N659GJMWCX\nboth present in the same page source, milletamma.com, 3 October 2026\ngoogle ads tag: AW-378561932 (id=AW-378561932 appears in gtag config)",
             reading="Two measurement IDs means the same session is being counted twice, and whichever report you read will disagree with the other. Usually this is a leftover from a rebuild or an agency handover. Consolidating to one property — with a redirect on the unused ID — restores a single source of truth in an hour."),
        dict(sev="MEDIUM", title="An archived local-ad creative still carries Google's removal notice — and the advertiser's template text",
             evidence="advertiser: URBAN MONK PRIVATE LIMITED (Verified)\ncreative: CR03268659855321202689 — Local Ad Rendering Service\nGoogle's archive states: 'Last shown: Jul 15, 2026' and 'Removed for a policy violation'\nvisible template residue in the same creative: '{KeyWord:Millet Amma}' and '<Rating (Reviews)> · <Distance> · Bengaluru'\nthe ad is not live: Google's archive shows it as removed",
             reading="This is read straight from Google's public archive and is not an accusation — local ads come from store listings and get pulled for all sorts of rendering reasons. What matters is the discipline: the archive is the first thing a curious customer or partner sees, and it currently shows a stopped creative with a template placeholder still visible. Cleaning the local-ad set removes the ambiguity."),
        dict(sev="MEDIUM", title="A permanent discount banner sits above everything",
             evidence="site-wide banner (verbatim, 3 October 2026): 'Our Biggest Sale Yet: Up To 20% Off + Free Prepaid Shipping.'\nobserved on the home, cart, contact, shipping-policy and terms pages",
             reading="A 'biggest sale yet' that never ends teaches the customer to wait for the next one. The offer also does the job of the homepage headline — millets, farm sourcing and the Shark Tank story are stronger reasons to buy than 20% off. Rotate the banner and let the product story breathe; the discount is a lever to keep, not to leave on."),
        dict(sev="MEDIUM", title="Four standard storefront paths return 404",
             evidence="GET https://milletamma.com/pages/faq                → 404\nGET https://milletamma.com/pages/store-locator      → 404\nGET https://milletamma.com/pages/bulk-enquiry       → 404\nGET https://milletamma.com/pages/corporate-gifting  → 404\n(3 October 2026)",
             reading="FAQ and bulk/corporate enquiry are the two that cost money. A millet brand has a natural corporate-gifting and bulk-institutional pitch, and there is currently no page to land it on — while the discount banner does the persuading."),
        dict(sev="LOW", title="Meta creative is running for seven months on one product story",
             evidence="library ID 1355783896518419 — running since 7 July 2026\ncopy: 'A sweet that feels like home, without the refined sugar… Raagi Laddoo is made with raagi, jaggery, Desi Gir cow milk ghee'\nlanding: milletamma.com/products/ragi-laddo-300g",
             reading="A direct-response creative that has survived seven months is doing its job, and the copy is genuinely good — ingredients, no refined sugar, an emotional hook. The risk is fatigue: the same text and image for that long normally means the frequency is high and the incremental reach is low. It is worth systematically rotating the visual while keeping the winning copy."),
        dict(sev="NOTE", title="The Shark Tank credential is a paid-media asset that is not in the paid copy",
             evidence="site footer: 'Watch us on Shark Tank India'\nMeta creative sampled: product story only, no broadcast reference\nGoogle local creative: product story only",
             reading="A national TV credential is free trust and it is currently only on the site. Testing it in the first line of a Meta hook is a small change with a clear read after two weeks."),
    ],
    score_dims=[
        ("Measurement integrity", "Two GA4 properties live at once; Ads tag confirmed.", 2),
        ("Conversion observability", "Shopify plus Shiprocket; Meta creative measurable by ID and landing page.", 3),
        ("Brand consistency", "Strong product story and entity disclosure; discount banner dilutes it.", 3),
        ("Technical health", "Four dead paths; local-ad archive carries a removal notice.", 3),
        ("Commercial fit", "80 live Google creatives plus working Meta, in a category with real tailwind.", 4),
    ],
    grade="B",
    grade_note="the most active account in this batch, with a duplicated measurement layer",
    qualification=("Public surfaces only. The policy-removal notice quoted above is Google's own text on an archived creative — it is reported as an observation, not as a finding against the brand. "
                   "Spend, ROAS and conversion rates are not scored. Both ad counts are one-day snapshots and Meta keyword counts include third-party inventory."),
    next_steps=[
        ("LOW EFFORT · IMMEDIATE BENEFIT", "Consolidate the two GA4 properties", "Pick one, redirect the other, and re-check that events still fire. One hour, and it ends the double-counting."),
        ("UNDER AN HOUR", "Rebuild the four missing pages", "FAQ, store locator, bulk enquiry, corporate gifting. The bulk and corporate pages have direct revenue attached to them."),
        ("HALF A DAY · BIGGEST SINGLE WIN", "Retire the permanent sale banner and test the Shark Tank hook", "Let the product story carry the homepage, and put the broadcast credential into the first line of the next Meta test."),
    ],
)

# ------------------------------------------------------------- 5. ADUKALE
E2["adukale"] = dict(
    brand="Adukale",
    cover_sub="Paid media and measurement audit. Every number below was read from live advertising and site data on 3 October 2026 — nothing is estimated.",
    metrics=[("13", "GOOGLE CREATIVES LIVE"), ("3", "SHOPPING VARIATIONS REMOVED BY GOOGLE"), ("4", "TAG FAMILIES DETECTED"), ("7", "FINDINGS IN THIS REPORT")],
    prepared_for_name="The Adukale marketing team",
    prepared_for_line="adukale.com · Karnataka, India (Bengaluru storefront)",
    prepared_for_link="Prepared from public data only — no ad-account access was requested or used.",
    method=method("adukale.com"),
    ad_account_sub="Live paid inventory and measurement surface as measured on the crawl date.",
    ad_account=[
        ("Ad platforms observed", "Google (Ads Transparency Center, region India) · Meta (Ad Library, country India)"),
        ("Google creative inventory", "13 creatives live on 3 October 2026 under SANKETHI NUTRIMENTS PRIVATE LIMITED (identity verified by Google), including Product Listing Ads and video; the same page paginates the grid as \"1 of 26\" — Google's header count and grid count disagree, so 13 is the account figure and 26 the grid figure, both read on 3 October 2026"),
        ("Meta ads", "0 active ads returned for the brand term (keyword search country India, active-only, 3 October 2026) — a clean zero, with no other advertiser surfacing either; this is one search method, not proof that no Meta activity exists"),
        ("Measurement tags", "GA4 G-X6WD89C59X · GA4 G-66YCE4PEZM · Google Ads AW-812528734 · Microsoft Clarity · Shopify"),
        ("Site platform", "Shopify; Cloudflare in front; HSTS present"),
        ("Published contact", "info@adukale.com (cart and collection pages) · +91 9035462696 · Helpdesk 8AM–8PM, Mon–Sun"),
        ("Published address", "Sankethi Nutriments Pvt. Ltd, 101/4, Block 1, Kannahalli Village, Bengaluru 560091 (cart and footer)"),
        ("Bengaluru relevance", "the brand's published address and helpdesk are in Bengaluru 560091"),
        ("Broken paths observed", "/pages/contact · /pages/faq · /pages/about-us · /pages/store-locator · /pages/bulk-enquiry · /pages/corporate-gifting → all 404 on 3 October 2026"),
        ("Spend · ROAS · CPA", "unavailable (private to the advertiser)"),
        ("Crawl date", CRAWL_DATE),
    ],
    findings=[
        dict(sev="CRITICAL", title="The site now hands every purchase to Amazon",
             evidence="site-wide announcement bar (verbatim, 3 October 2026, present on the home, cart and collection pages):\n'All purchases from this site will now be completed through Amazon. Enjoy the same authentic taste with greater ease.'\nshopify storefront still live at adukale.com with cart and product pages",
             reading="This is the single most important fact about Adukale's paid media: if the storefront routes buying to Amazon, then paid clicks that land on adukale.com either lose the sale or transfer it — and with it the customer record, the repeat-purchase data and the ability to measure any of it. 13 Google creatives are still running to that storefront. Either the ads should point where the purchase now happens, or the site should be rebuilt so it can sell again. Doing neither pays for traffic you cannot convert or measure."),
        dict(sev="HIGH", title="A Shopify template placeholder is visible on the live storefront",
             evidence="rendered pickup block on the live site (verbatim):\n'123 John Doe Street  Your Town, YT 12345  Store Hours Sun: Closed Mon-Fri: 9:00 - 17:00 Sat: 10:00 - 13:00'\nnext to the real pickup point: '155 Madappa Building 1st Main Mallathalli — Free. Usually ready in 24 hrs'\nobserved on the home and collection pages, 3 October 2026",
             reading="A customer checking where to collect their order is shown a fictional address from the theme's demo content. It is a five-minute fix in the theme editor and, until it is fixed, it is the kind of detail that silently kills trust on exactly the page where trust matters most."),
        dict(sev="HIGH", title="Two GA4 properties are live on the same storefront",
             evidence="analytics id 1: G-X6WD89C59X\nanalytics id 2: G-66YCE4PEZM\ngoogle ads tag: AW-812528734\nall present in the same page source, adukale.com, 3 October 2026",
             reading="Same pattern as the placeholder: a build that was changed twice without retiring the old piece. Two GA4 IDs double-count sessions and split conversion history in half, which makes the Amazon question above even harder to answer with data."),
        dict(sev="MEDIUM", title="The footer's email icon is not a mailto link, so clicking it goes nowhere",
             evidence="the address is published correctly and visibly: info@adukale.com (home, cart and collection pages)\nthe icon beside it is coded as (verbatim from the page source):\n  &lt;a href=\"info@adukale.com\" target=\"_blank\"&gt;\nsource: adukale.com page source, 3 October 2026 (Ctrl+F 'href=\"info@adukale.com\"')",
             reading="The address reads correctly, so this is not a typo a customer would notice — but the link has no mailto: prefix, which means a click cannot open a mail client. The site's own 'Email' link is inert on every page it appears. One attribute fixes it, and it is worth checking how many enquiries have been lost to a link that quietly does nothing."),
        dict(sev="MEDIUM", title="Google is running; the Meta library returns nothing for the brand term",
             evidence="google: 13 creatives live (region India), including PLA and video\nmeta:   'No ads match your search criteria' — keyword search 'Adukale', country India, active ads only, 3 October 2026\ntags:   no Meta pixel found in the storefront HTML on the crawl date (a pixel fired by a tag manager or a platform layer would not appear here)",
             reading="Adukale's products — ready-to-cook Karnataka staples, spice mixes, snacks — photograph well and travel well by post, which is precisely what Meta rewards. With no pixel installed, none of that audience can be built. Meta pixel plus catalogue is a half-day job; a catalogue also fixes the Amazon dependency, because a shoppable catalogue can point at whichever checkout you choose."),
        dict(sev="MEDIUM", title="Three Shopping variations carry Google's own removal notice",
             evidence="advertiser: SANKETHI NUTRIMENTS PRIVATE LIMITED (Verified)\ncreative CR11719898640389505025 — Product Listing Ad Rendering Service, 1 of 3 variations:\n  'Buy Sambar Powder | The Best Spice Mix | Adukale'     Removed for a policy violation\n  'Chutney Powder | 200g Pack'                          Removed for a policy violation\n  'Kayi Kodubale | 180g'                                Removed for a policy violation\n'Last shown: Nov 28, 2025' · Shown in India\nsource: Google Ads Transparency Center, region India, re-read on 3 October 2026",
             reading="Google's archive is public, so a prospective customer, a distributor or a journalist can see that three of this brand's Shopping variations were pulled for a policy issue. Google does not state the reason, and none is inferred here. Because the removals are feed-level in most cases (price, availability, landing page, restricted claims), a Merchant Center diagnostics read usually identifies the cause in minutes — and it matters that the shopping engine is the visible one in this account."),
        dict(sev="NOTE", title="Shopping ads are already running, so a product feed exists",
             evidence="PLA observed: 'Buy Rice Idli | Healthy Breakfast | Adukale' — Product Listing Ad Rendering Service\nsource: Google Ads Transparency Center, region India, 3 October 2026",
             reading="The feed already exists and it already carries your product titles. The same feed can power Meta catalogue ads, which makes the parallel channel cheaper to start than it looks."),
    ],
    score_dims=[
        ("Measurement integrity", "GA4 and Ads tags present, but two GA4 properties live at once.", 2),
        ("Conversion observability", "Purchases routed to Amazon; on-site conversion cannot be measured for those paths.", 1),
        ("Brand consistency", "Brand and packaging consistent; the site carries a template placeholder and an email icon that is not clickable.", 3),
        ("Technical health", "Six dead paths, a placeholder address, and a duplicate analytics ID.", 2),
        ("Commercial fit", "Established Karnataka food brand with a live feed and an unbuilt second channel.", 4),
    ],
    grade="C",
    grade_note="the biggest single opportunity here, gated by one routing decision",
    qualification=("Public surfaces only. The Amazon routing statement is quoted verbatim from Adukale's own site — the commercial arrangement behind it is not public and is not assessed here. "
                   "Spend, ROAS and conversion rates are not scored. Ad counts are one-day snapshots, and the empty Meta result is one search method rather than proof of absence."),
    next_steps=[
        ("LOW EFFORT · IMMEDIATE BENEFIT", "Decide where the paid click should end", "If Amazon is the checkout, point the Google ads at the Amazon listing that converts and stop paying to land on a storefront that cannot sell. If the site is staying, the routing needs to change."),
        ("UNDER AN HOUR", "Delete the placeholder pickup address and fix the email icon link", "Theme editor, five minutes each. Both are live customer-facing defects today."),
        ("HALF A DAY · BIGGEST SINGLE WIN", "Install the Meta pixel and connect the existing feed", "The product feed already exists for Google Shopping. Connecting it to a Meta catalogue and pixel opens the second channel without new content work."),
    ],
)

# ------------------------------------------------------------- 6. ORGANIC MANDYA
E2["organicmandya"] = dict(
    brand="Organic Mandya",
    cover_sub="Paid media and measurement audit. Every number below was read from live advertising and site data on 3 October 2026 — nothing is estimated.",
    metrics=[("69", "CREATIVES IN GOOGLE ACCOUNT"), ("~2", "META ADS FOR BRAND TERM"), ("3", "TAG FAMILIES DETECTED"), ("5", "FINDINGS IN THIS REPORT")],
    prepared_for_name="The Organic Mandya marketing team",
    prepared_for_line="organicmandya.com · Karnataka, India",
    prepared_for_link="Prepared from public data only — no ad-account access was requested or used.",
    method=method("organicmandya.com"),
    ad_account_sub="Live paid inventory and measurement surface as measured on the crawl date.",
    ad_account=[
        ("Ad platforms observed", "Google (Ads Transparency Center, region India) · Meta (Ad Library, country India)"),
        ("Google creative inventory", "69 creatives in the advertiser account (MANDYA ORGANIC FOODS PRIVATE LIMITED, identity verified by Google); 67 creatives point specifically at organicmandya.com"),
        ("Meta ads", "≈2 results for the brand term; brand-owned creative verified: library ID 1432155482101394, running since 13 September 2026, landing organicmandya.com/collections/gluten-free-upma-rava-millet-rava-for-healthy-upma"),
        ("Measurement tags", "GA4 G-MHKC4DNNH3 · Google Ads AW-16535163896 · Shopify with a custom dataLayer (events observed: gtm-meta, gtm-promo, gtm-creative, gtm-position, gtm-destination)"),
        ("Site platform", "Shopify; Cloudflare in front; HSTS present"),
        ("Published contact", "support@organicmandya.com (cart and collection pages) · +91 95909 22000"),
        ("Bengaluru relevance", "the site's own announcement bar leads with Bengaluru: '2-hr delivery in Bengaluru, Hyderabad & Mysuru'"),
        ("Delivery promise published", "2-hour delivery in Bengaluru, Hyderabad & Mysuru — ₹49 under ₹500, free above ₹500 · 3–5 day delivery all India — ₹149 under ₹2000, free above ₹2000"),
        ("Broken paths observed", "/pages/faq · /pages/bulk-enquiry · /pages/corporate-gifting → all 404 on 3 October 2026"),
        ("Spend · ROAS · CPA", "unavailable (private to the advertiser)"),
        ("Crawl date", CRAWL_DATE),
    ],
    findings=[
        dict(sev="HIGH", title="You have a two-hour delivery promise and it is nowhere in the paid inventory",
             evidence="published promise (verbatim from the live site, 3 October 2026):\n'2-hr delivery in Bengaluru, Hyderabad & Mysuru — ₹49 delivery charge on orders under ₹500, FREE above ₹500'\nGoogle creatives sampled: product-led (e.g. 'organic rajmudi rice (rajamudi) — karnataka's heritage red rice')\naccount: 69 creatives, of which 67 point at organicmandya.com",
             reading="Two-hour delivery of organic staples is a genuinely scarce promise in this category — it is the kind of thing quick-commerce charges a premium for. Right now the ads sell rice; the promise sells the store. A hook built on 'organic, at your door in two hours' is testable against the current product-led creative in a fortnight, and it uses an asset that is already paid for."),
        dict(sev="MEDIUM", title="Google is doing almost all the work; Meta is close to unused",
             evidence="google: 69 creatives in the advertiser account\nmeta:   ≈2 active results for the brand term, one of them the brand's own creative (library ID 1432155482101394, since 13 September 2026)\nratio:  roughly 35:1",
             reading="The Meta creative that does exist is well made and points at a category collection rather than a single product, which is the right instinct for a grocery basket. Two ads, though, is a test that was never scaled. Given how visual the product range is, this is the clearest underused channel in the account."),
        dict(sev="MEDIUM", title="Paid traffic and the dataLayer are speaking two different languages",
             evidence="dataLayer event names observed in the page source: gtm-meta · gtm-promo · gtm-creative · gtm-position · gtm-destination\nGA4 property: G-MHKC4DNNH3\nGoogle Ads: AW-16535163896",
             reading="Custom event names like these are a sign that someone built a careful measurement plan. The value only lands when each event is mapped to a GA4 key event and imported into Google Ads as a conversion. Until that mapping is done, the plan exists in the page and not in the reports."),
        dict(sev="MEDIUM", title="Three standard paths return 404, including the one corporate buyers look for",
             evidence="GET https://organicmandya.com/pages/faq               → 404\nGET https://organicmandya.com/pages/bulk-enquiry      → 404\nGET https://organicmandya.com/pages/corporate-gifting → 404\n(3 October 2026)",
             reading="Bulk and corporate gifting are the two order types most likely to be worth five figures, and both dead-end. For a brand with a farmer story and a co-operative structure, a corporate gifting page writes itself — and it is exactly the kind of order that pays for the paid media that finds it."),
        dict(sev="NOTE", title="The Google count differs slightly between the account and the domain view",
             evidence="advertiser account (MANDYA ORGANIC FOODS PRIVATE LIMITED): 69 creatives\ndomain view (organicmandya.com):                        67 creatives\ndifference:                                             2",
             reading="A two-creative difference is normally a destination change — ads that used to point at the site and now point elsewhere, or the reverse. It is a small reminder that the platform's own counts answer slightly different questions, and worth knowing before those numbers are quoted in a board deck."),
    ],
    score_dims=[
        ("Measurement integrity", "GA4, Ads tag and a purpose-built dataLayer; mapping to key events not confirmed.", 3),
        ("Conversion observability", "Shopify with published delivery SLAs; Meta barely tested.", 3),
        ("Brand consistency", "Clear farmer-to-family story carried across the site.", 4),
        ("Technical health", "Three dead paths; HSTS present; cache policy not set on the storefront.", 3),
        ("Commercial fit", "Active Google account plus a scarce delivery promise and untapped Meta inventory.", 4),
    ],
    grade="A",
    grade_note="strong measurement instincts and a wasted differentiator",
    qualification=("Public surfaces only. The 69 and 67 counts come from two different views of the same platform on the same day and are reported as measured, not reconciled. "
                   "Spend, ROAS and delivery-SLA compliance are not scored — no public source exists for them."),
    next_steps=[
        ("LOW EFFORT · IMMEDIATE BENEFIT", "Put the two-hour promise into the ad copy", "One hook test against the current product-led creative. The claim is already published on your site, so nothing new needs to be true."),
        ("UNDER AN HOUR", "Map the dataLayer events to GA4 key events", "gtm-promo, gtm-creative and gtm-destination exist already. Importing them as conversions is configuration, not development."),
        ("HALF A DAY · BIGGEST SINGLE WIN", "Build the corporate-gifting page and scale Meta collection ads", "One page for the highest-value order type, plus collection-level Meta ads against the visual catalogue you already have."),
    ],
)

# ------------------------------------------------------------- 7. PURE & SURE (PHALADA)
E2["pureandsure"] = dict(
    brand="Pure & Sure",
    cover_sub="Paid media and measurement audit. Every number below was read from live advertising and site data on 3 October 2026 — nothing is estimated.",
    metrics=[("37", "GOOGLE CREATIVES LIVE"), ("4", "MEASUREMENT TAGS DETECTED"), ("1", "FEED TAGGING BUG FOUND"), ("5", "FINDINGS IN THIS REPORT")],
    prepared_for_name="The Pure & Sure marketing team",
    prepared_for_line="pureandsure.in · Bengaluru, Karnataka, India",
    prepared_for_link="Prepared from public data only — no ad-account access was requested or used.",
    method=method("pureandsure.in"),
    ad_account_sub="Live paid inventory and measurement surface as measured on the crawl date.",
    ad_account=[
        ("Ad platforms observed", "Google (Ads Transparency Center, region India) · Meta (Ad Library, country India)"),
        ("Google creative inventory", "37 creatives live on 3 October 2026 under Phalada Organic Consumer Products Private Limited (identity verified by Google), including Shopping and video"),
        ("Meta ads", "NOT MEASURED — the keyword search for the brand term returns ~37,000 unrelated results (both words are generic), so no brand-specific inventory is reported here; the storefront does carry Meta pixel 903483430574351, initialised in the page source on 3 October 2026"),
        ("Measurement tags", "GA4 G-VGC836EHVF · Google Tag Manager GTM-KP8NPFKZ · Google Ads AW-16785598661 · Meta pixel 903483430574351 (fbq init, visible in the page source)"),
        ("Site platform", "Shopify; Cloudflare in front; HSTS present"),
        ("Published contact", "info@pureandsure.in (contact and shipping-policy pages) · care@pureandsure.in (cart and collection pages) · 1800 121 0369"),
        ("Published address", "Phalada Organic Consumer Products Pvt Ltd, 92/5, Kannalli Village, Seegehalli, Magadi Main Road, Bangalore 560091 (footer of the cart and collection pages)"),
        ("Published offer", "Free shipping on orders above ₹500 (site banner, 3 October 2026)"),
        ("Broken paths observed", "/pages/contact-us → 404 · /pages/about-us → 404 · /pages/store-locator → 404 · /pages/bulk-enquiry → 404 · /pages/corporate-gifting → 404 · (/pages/contact works)"),
        ("Bengaluru relevance", "the brand's published address is in Bangalore 560091 (Magadi Main Road)"),
        ("Spend · ROAS · CPA", "unavailable (private to the advertiser)"),
        ("Crawl date", CRAWL_DATE),
    ],
    findings=[
        dict(sev="HIGH", title="Automatic feed tagging is overwriting your campaign reporting",
             evidence="PLA landing URL captured in the ad archive (verbatim):\nhttps://pureandsure.in/products/organic-desi-ghee-500ml?variant=47115633492123&country=IN&currency=INR&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic\ncampaign parameter observed: utm_campaign=sag_organic",
             reading="Google's automatic feed tagging is writing 'sag_organic' into the campaign field of every Shopping click. In GA4, that traffic will be filed as an 'organic' campaign — which means your paid Shopping investment is indistinguishable from search traffic in reports, and any channel comparison built on those reports is wrong. It is a five-minute change in the feed's tracking settings, and it is the difference between trusting your own dashboard and not."),
        dict(sev="MEDIUM", title="Meta is unmeasurable by brand term, and the pixel is the only clue",
             evidence="meta search 'Pure and Sure' (country India, active): ~37,000 results, first page entirely unrelated advertisers\nstorefront: Meta pixel present; GA4 G-VGC836EHVF; GTM-KP8NPFKZ; Ads AW-16785598661\nconclusion: no brand-specific Meta count could be read on 3 October 2026",
             reading="It is honestly not possible to say from outside how much Meta inventory Pure & Sure runs, because the brand name is made of two generic words. Rather than guess, this audit marks it not measured. What can be said: the pixel is installed, so if Meta campaigns are running, the audiences exist. A clean read needs the account's own figures."),
        dict(sev="MEDIUM", title="Conventional paths are dead in a way that suggests a platform rebuild",
             evidence="GET https://pureandsure.in/pages/contact-us  → 404\nGET https://pureandsure.in/pages/about-us    → 404\nGET https://pureandsure.in/pages/contact     → 200 (works)\nGET https://pureandsure.in/pages/store-locator → 404\n(3 October 2026)",
             reading="The pattern — 'contact' works, 'contact-us' does not — is what happens when a Shopify theme is replaced and the old handles are never redirected. Redirects are cheap insurance: they also recover any paid or organic traffic that was pointed at the old URLs."),
        dict(sev="LOW", title="Two published support addresses on the same site",
             evidence="address 1: info@pureandsure.in (contact and shipping-policy pages)\naddress 2: care@pureandsure.in (cart and collection pages)\ntoll-free: 1800 121 0369",
             reading="Two addresses is fine if someone owns both. It is a problem if a customer writes to one and waits. Standard practice: one canonical address on every page, with the second as an alias that forwards into the same inbox."),
        dict(sev="NOTE", title="The catalogue is being led by a new product, and the feed carries it well",
             evidence="site banner: 'Introducing Low GI Sonamasuri Rice — Buy Now'\nsite banner: '100% Organic Foods Delivered Directly' and 'Free Shipping on orders above ₹500'\nPLA sample: 'Organic Ghee | Premium A…' landing on a product page with a variant parameter",
             reading="Low-GI rice, organic ghee and a ₹500 free-shipping threshold is a coherent, premium-led catalogue, and the Shopping feed is picking products up cleanly. The measurement fix above is what will let the team see which of these products actually earns the spend."),
    ],
    score_dims=[
        ("Measurement integrity", "GA4, GTM, Ads tag and Meta pixel all present; feed tagging corrupts campaign data.", 3),
        ("Conversion observability", "Shopify storefront and pixel in place; Meta spend not publicly readable.", 3),
        ("Brand consistency", "Organic, premium-led positioning carried consistently.", 4),
        ("Technical health", "Several dead paths but a working contact page; HSTS present.", 3),
        ("Commercial fit", "Established organic FMCG brand with an active Google account.", 3),
    ],
    grade="B",
    grade_note="a healthy stack with one reporting setting that quietly invalidates channel comparisons",
    qualification=("Public surfaces only; Meta is explicitly marked not measured rather than estimated, because the brand term returns unrelated inventory. "
                   "Spend, ROAS and conversion rates are not scored. The 37-creative count is a one-day snapshot."),
    next_steps=[
        ("LOW EFFORT · IMMEDIATE BENEFIT", "Turn off 'sag_organic' auto-tagging in the feed", "It takes minutes and it is currently filing paid Shopping clicks as organic traffic in your analytics."),
        ("UNDER AN HOUR", "Redirect the old page handles", "contact-us, about-us and store-locator should all point somewhere useful instead of returning 404."),
        ("HALF A DAY · BIGGEST SINGLE WIN", "Get a clean Meta read and decide the channel question", "Pull the last 90 days of Meta spend and results from the account, and compare it with the Google figures you can already see. Then decide whether Meta deserves more than the pixel."),
    ],
)

# ------------------------------------------------------------- 8. EAT BETTER CO
E2["eatbetterco"] = dict(
    brand="Eat Better Co",
    cover_sub="Paid media and measurement audit. Every number below was read from live advertising and site data on 3 October 2026 — nothing is estimated.",
    metrics=[("29", "GOOGLE CREATIVES LIVE"), ("-1%", "SMALLEST DISCOUNT IN THE FEED"), ("1", "FORM-LEVEL PIXEL CONFIG"), ("6", "FINDINGS IN THIS REPORT")],
    prepared_for_name="The Eat Better Co marketing team",
    prepared_for_line="eatbetterco.com · Jaipur, Rajasthan, India (pan-India delivery)",
    prepared_for_link="Prepared from public data only — no ad-account access was requested or used.",
    method=method("eatbetterco.com"),
    ad_account_sub="Live paid inventory and measurement surface as measured on the crawl date.",
    ad_account=[
        ("Ad platforms observed", "Google (Ads Transparency Center, region India) · Meta (Ad Library, country India)"),
        ("Google creative inventory", "29 creatives live on 3 October 2026 for eatbetterco.com under EAT BETTER VENTURES PRIVATE LIMITED (identity verified by Google); the advertiser account holds 27, and the sampled set is dominated by Product Listing Ads"),
        ("Meta ads", "NOT MEASURED — the phrase is built from generic words and the keyword search returns ~1,200 unrelated results, so no brand-specific inventory is reported here; the enquiry form does carry Meta pixel 3182482251838473 with a custom Lead event (page source, 3 October 2026)"),
        ("Measurement tags", "GA4 G-90QE4TSKTH · Google Ads AW-610414449 · Shopify · a Meta pixel ID (3182482251838473) is configured inside an embedded form on the storefront, with a custom Lead event on submit, and Judge.me is installed"),
        ("Site platform", "Shopify; Cloudflare in front; HSTS present"),
        ("Published contact", "care@eatbetterco.com (contact-us and refund-policy pages) · connect@gottaeatbetter.com (privacy and shipping-policy pages) · +91 9829188706"),
        ("Published address", "Eat Better Ventures Pvt Ltd, A1/A2, Vastushree Colony, 100 Feet Road, Manyawas, Mansarovar, Jaipur, Rajasthan 302020 (contact page)"),
        ("Paths that work", "/pages/contact-us → 200 · /pages/corporate-gifting → 200 · /policies/shipping-policy → 200"),
        ("Published shipping terms", "free above ₹500 · prepaid shipping ₹49 · cash-on-delivery ₹79 · 'Most orders are delivered within 3 working days'"),
        ("Corporate-gifting page (the brand's own published figures)", "'10 LAKH+ hampers delivered pan-India · 500+ corporates & organizations · 25 hamper designs this Diwali', with hampers from ₹249 to ₹2,499"),
        ("Bengaluru relevance", "not claimed by the brand: the site publishes a Jaipur registered address and a national corporate-gifting page ('send to one office or a thousand people across the country'); no Bengaluru-specific statement appears in the 3 October 2026 capture. Listed and labelled honestly rather than presented as a Bengaluru brand."),
        ("Broken paths observed", "/pages/contact → 404 · /pages/faq → 404 · /pages/about-us → 404 · /pages/store-locator → 404 · /pages/bulk-enquiry → 404"),
        ("Spend · ROAS · CPA", "unavailable (private to the advertiser)"),
        ("Crawl date", CRAWL_DATE),
    ],
    findings=[
        dict(sev="HIGH", title="Your Shopping feed is advertising discounts of 1%, 2% and 6%",
             evidence="PLA badges captured from the ad archive (verbatim): '[-1%]' (quinoa chilli lime namkeen), '[-6%]' (better trail mix 100g), '[-2%]' (sweet crunchy nut mix 100g), '[-2%]' (ragi chips bundle)\nlanding URLs (verbatim, a Google ad click):\n  https://eatbetterco.com/products/quinoa-chilli-lime-healthy-namkeen?…&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic\nadvertiser: EAT BETTER VENTURES PRIVATE LIMITED (Verified) · 27 creatives in the account, 29 pointing at the domain\nsource: Google Ads Transparency Center, region India, 3 October 2026",
             reading="A '1% off' badge in a discovery feed does active harm: it reads as a discount and delivers a rounding error, which trains shoppers to scroll past the listing. Either the feed should show no discount at that level, or the price should be repositioned so the badge is meaningful. This is a feed-level change and it affects every Shopping impression."),
        dict(sev="HIGH", title="The support email on your policy pages belongs to a different domain",
             evidence="contact-us and refund-policy pages: care@eatbetterco.com\nprivacy-policy and shipping-policy pages: connect@gottaeatbetter.com\nstorefront: eatbetterco.com ('Eat Better Co - As seen on Shark Tank')",
             reading="A customer who checks your refund policy and then writes to connect@gottaeatbetter.com has been sent to a domain they have never heard of — and if that domain's SPF/DKIM records are not aligned, some of those replies will land in spam. Standard practice is one support address on the store's own domain, with the second as a forwarding alias."),
        dict(sev="MEDIUM", title="Cash on delivery costs the customer ₹30 more than prepaid — and the ads do not say so",
             evidence="published terms (verbatim): 'Shipping is free for orders above Rs 500. Pre-paid shipping is Rs 49. Cash On Delivery shipping is Rs 79.'\nad inventory sampled: product and price messaging only; no shipping or COD terms observed in the captured creatives",
             reading="COD is the bigger margin risk (returns-to-origin) and the higher fee is a sensible nudge — but a nudge only works if the buyer sees it before they choose. Putting 'free shipping over ₹500' into the ad copy does two things at once: it raises average order value and it moves the payment choice in your favour."),
        dict(sev="MEDIUM", title="Five standard paths return 404 on a Shark Tank-credentialed store",
             evidence="GET https://eatbetterco.com/pages/faq          → 404\nGET https://eatbetterco.com/pages/about-us     → 404\nGET https://eatbetterco.com/pages/contact      → 404\nGET https://eatbetterco.com/pages/store-locator → 404\nGET https://eatbetterco.com/pages/bulk-enquiry → 404\n(3 October 2026)",
             reading="National-TV exposure sends people looking for the brand's story and its people. Right now the two obvious URLs for that — about-us and faq — do not exist. The contact page that does work is the only one of the set, so at least support can be reached."),
        dict(sev="MEDIUM", title="Two measurement details decide what the paid data can actually tell you",
             evidence="feed tagging (verbatim from a Google ad click):\n  …quinoa-chilli-lime-healthy-namkeen?…&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic\nembedded form configuration in the storefront source (verbatim):\n  \"facebook_pixel_id\":\"3182482251838473\"\n  after_submit_script: \"if (typeof fbq !== 'undefined') { fbq('trackCustom', 'Lead'); } else { console.warn('Meta Pixel not loaded on this page'); }\"\n  after_submit_url: \"https://eatbetterco.com/collections/diwali-gift-hampers-2026-collection\"",
             reading="Two separate things. First, the Shopping feed is writing 'sag_organic' into the campaign field, so every paid Shopping click is filed as organic traffic in GA4 — the channel comparison cannot be right while that is true. Second, a Meta pixel and a Lead event exist, but inside one embedded form rather than across the store: the form redirects to your Diwali hampers collection, which strongly suggests it is the enquiry form for that campaign. It works — but a Lead event that fires only from one form is a single point of failure, and it means the pixel cannot see any other page of the store."),
        dict(sev="NOTE", title="'As seen on Shark Tank' is doing the positioning work on the storefront only",
             evidence="site title tag (verbatim): 'Eat Better Co - As seen on Shark Tank'\nPLA titles sampled: product-led, no broadcast reference",
             reading="The credential is the strongest short trust signal available to a snack brand entering a crowded healthy-snacking category. It appears in the browser tab and nowhere in the advertising captured here. That is a cheap A/B test with a clear hypothesis behind it."),
    ],
    score_dims=[
        ("Measurement integrity", "GA4 and Google Ads tags confirmed; no GTM container observed.", 3),
        ("Conversion observability", "Shopify with published shipping and COD terms; Meta not readable publicly.", 3),
        ("Brand consistency", "Strong credential, but two email domains in one funnel.", 3),
        ("Technical health", "Five dead paths; contact page live; HSTS present.", 2),
        ("Commercial fit", "Feed-driven D2C snack brand with a TV credential and clear feed upside.", 4),
    ],
    grade="B",
    grade_note="a feed-first account where small feed decisions do large amounts of work",
    qualification=("Public surfaces only; Meta is marked not measured rather than estimated, because the brand term returns unrelated inventory. "
                   "Spend, ROAS and COD share are not scored — no public source exists. Ad counts are one-day snapshots."),
    next_steps=[
        ("LOW EFFORT · IMMEDIATE BENEFIT", "Clean the sub-10% discounts out of the feed", "A 1% badge is worse than no badge. Either remove the discount display at that level or reprice so the badge means something."),
        ("UNDER AN HOUR", "Put one support address on every page", "Align the policy pages to care@eatbetterco.com and set the other address to forward."),
        ("HALF A DAY · BIGGEST SINGLE WIN", "Put the Shark Tank credential and the ₹500 threshold into the ad copy", "Two lines of copy testable against the current product-led creative, aimed at both trust and average order value."),
    ],
)

# ------------------------------------------------------------- 9. BRIK OVEN
E2["brikoven"] = dict(
    brand="Brik Oven",
    cover_sub="Paid media and measurement audit. Every number below was read from live advertising and site data on 3 October 2026 — nothing is estimated.",
    metrics=[("42", "CREATIVES IN GOOGLE ACCOUNT"), ("17", "CREATIVES POINT OFF-DOMAIN"), ("2", "TAG FAMILIES DETECTED"), ("5", "FINDINGS IN THIS REPORT")],
    prepared_for_name="The Brik Oven marketing team",
    prepared_for_line="brikoven.com · Bengaluru, Karnataka, India",
    prepared_for_link="Prepared from public data only — no ad-account access was requested or used.",
    method=method("brikoven.com"),
    ad_account_sub="Live paid inventory and measurement surface as measured on the crawl date.",
    ad_account=[
        ("Ad platforms observed", "Google (Ads Transparency Center, region India) · Meta (Ad Library, country India)"),
        ("Google creative inventory", "42 creatives in the advertiser account (Brik Oven Pvt Ltd, identity verified by Google); 25 creatives point specifically at brikoven.com, and the visible set is dominated by Local store ads for Palace Road, Whitefield, Koramangala and Manyata Business Park"),
        ("Meta ads", "NOT MEASURED — the brand-term search returns ~27 results whose first page is entirely unrelated advertisers, so brand-owned inventory could not be confirmed by this method"),
        ("Measurement tags", "Google Tag Manager GTM-PMCQMP4 · GA4 G-6HE7Y2G8N3 · Meta pixel 428743468014315 (fbq init visible in the page source) · Squarespace storefront"),
        ("Site platform", "Squarespace; HSTS present"),
        ("Published contact", "theteam@brikoven.com (published on the site's contact block)"),
        ("Published address", "outlets on the home page: #19 Church St., Bangalore 560001 · 872/A HAL 2nd Stage, 80 Ft Road, Bangalore 560038 · Prestige Trade Tower, Palace Road, Bengaluru 560001 · Prem Chambers, Jyoti Nivas College Rd, Koramangala, Bengaluru 560034 — each with its own phone number"),
        ("Bengaluru relevance", "four Bengaluru outlets are published with full addresses and phone numbers, and the live Google local ads are store-level ads for those outlets"),
        ("Reservation path", "Local ads offer 'Book now' via widget.reservego.co — a third-party reservation widget"),
        ("Broken paths observed", "/contact-us · /about-us · /faq · /menu · /book-a-table · /locations · /order-online · /privacy-policy · /terms → all 404 on 3 October 2026 (nine paths)"),
        ("Spend · ROAS · CPA", "unavailable (private to the advertiser)"),
        ("Crawl date", CRAWL_DATE),
    ],
    findings=[
        dict(sev="HIGH", title="Your reservation click leaves your domain and lands in a third-party widget",
             evidence="Local ad creative (verbatim from the ad archive):\n'Wood-Fired Pizza Near You — Discover Neapolitan sourdough pizzas …'\nCTA target shown: 'Book now • widget.reservego.co/'\nstore: Brik Oven — Woodfired Pizzas (Manyata Business Park)\nsource: Google Ads Transparency Center, region India, 3 October 2026",
             reading="Every booking made through that widget is a customer relationship held by someone else: the booking data, the ability to remarket to a no-show list, and the measurement of which store the ad actually filled. A direct booking path on brikoven.com — even a simple form that emails the store — puts that data back in your hands and makes store-level ROAS readable."),
        dict(sev="HIGH", title="Eight conventional paths, including the contact page, return 404",
             evidence="GET https://brikoven.com/contact-us  → 404\nGET https://brikoven.com/menu        → 404\nGET https://brikoven.com/book-a-table → 404\nGET https://brikoven.com/locations   → 404\nGET https://brikoven.com/order-online → 404\n(plus /about-us, /faq, /terms — all 404 on 3 October 2026)",
             reading="Brik Oven's search traffic is overwhelmingly intent-led — 'pizza near me', 'book a table', store names. People who arrive by typing or by an old link hit dead pages, and those are exactly the visitors most likely to book. Redirects to the working sections (menu, reservations, stores) are an afternoon of work and they recover traffic the paid campaigns are already paying to create."),
        dict(sev="MEDIUM", title="Seventeen creatives in the account point somewhere other than the website",
             evidence="advertiser account: 42 creatives\ndomain brikoven.com: 25 creatives\ndifference: 17\nsource: Google Ads Transparency Center, region India, 3 October 2026",
             reading="The difference is consistent with store-level ads and third-party reservation destinations rather than a leak — but it does mean the account's centre of gravity is not the website, and website analytics can only ever see part of what paid media does. Worth mapping deliberately rather than discovering later."),
        dict(sev="MEDIUM", title="At least one store creative has stopped serving",
             evidence="creative CR16763555951004352513 (Brik Oven — Woodfired Pizzas, Palace Road)\narchive states: 'Last shown: Jul 23, 2026' and 'Format: Text'\nthe same creative promotes 'Smoked Ham Bagel Mornings — Sourdough sandwiches, bagels & toasties. Open 8AM-11AM daily'",
             reading="Store-level ads need a cadence, because a breakfast ad that stopped in July is still visible in the public archive in October while the stores keep trading. A monthly review of which local ads are live — and a decision on whether to keep breakfast creative running — is the difference between a maintained account and a set-and-forget one."),
        dict(sev="NOTE", title="The stack is clean and the breakfast launch is being advertised properly",
             evidence="GTM-PMCQMP4 and GA4 G-6HE7Y2G8N3 both present on brikoven.com, 3 October 2026\nlocal ad copy: 'Sourdough Breakfast at Brik — Egg salad bagels, ham melts, fig toasties. Breakfast all day, no lines.' (Prestige Trade Tower)",
             reading="A tag manager container, a GA4 property and specific store-level copy about a specific daypart is a more disciplined setup than most restaurant groups run. The quick wins here are about keeping it current, not rebuilding it."),
    ],
    score_dims=[
        ("Measurement integrity", "GTM and GA4 present on the site; store-level ad data sits partly off-domain.", 3),
        ("Conversion observability", "Reservations through a third-party widget; store-level ROAS hard to attribute.", 2),
        ("Brand consistency", "Distinctive brand voice carried into store-level ad copy.", 4),
        ("Technical health", "Eight dead paths including contact and locations.", 2),
        ("Commercial fit", "Multi-outlet group actively running local store ads across Bengaluru.", 4),
    ],
    grade="B",
    grade_note="well-run local advertising losing its data at the last click",
    qualification=("Public surfaces only. The archive's 'removed for a policy violation' line appears on some local-ad creatives in Google's rendering; it is not read here as a brand finding. "
                   "Spend, ROAS and cover counts are not scored. Ad counts are one-day snapshots and Meta keyword results include unrelated advertisers."),
    next_steps=[
        ("LOW EFFORT · IMMEDIATE BENEFIT", "Redirect the dead paths to the working sections", "Contact, menu, reservations, locations and ordering should each land on the section that exists. One afternoon."),
        ("UNDER AN HOUR", "Review which store creatives are still live", "Check the Palace Road breakfast creative — the archive shows it stopped in July while the stores kept trading."),
        ("HALF A DAY · BIGGEST SINGLE WIN", "Own the reservation path", "Put a booking form on brikoven.com so bookings, no-shows and store-level attribution stay with you instead of the widget."),
    ],
)

# ------------------------------------------------------------- 10. ARAKU COFFEE
E2["arakucoffee"] = dict(
    brand="Araku Coffee",
    cover_sub="Paid media and measurement audit. Every number below was read from live advertising and site data on 3 October 2026 — nothing is estimated.",
    metrics=[("~200", "GOOGLE CREATIVES LIVE"), ("1", "FEED TAGGING BUG FOUND"), ("2", "TAG FAMILIES DETECTED"), ("5", "FINDINGS IN THIS REPORT")],
    prepared_for_name="The Araku Coffee marketing team",
    prepared_for_line="arakucoffee.in · Bengaluru, Karnataka, India",
    prepared_for_link="Prepared from public data only — no ad-account access was requested or used.",
    method=method("arakucoffee.in"),
    ad_account_sub="Live paid inventory and measurement surface as measured on the crawl date.",
    ad_account=[
        ("Ad platforms observed", "Google (Ads Transparency Center, region India) · Meta (Ad Library, country India)"),
        ("Google creative inventory", "≈200 creatives live on 3 October 2026 under Araku Originals Pvt Ltd (identity verified by Google), spanning Shopping, Local and video formats"),
        ("Meta ads", "NOT MEASURED — the brand-term search returns ~86 results dominated by third-party and partner placements (a partner workshop ad carrying the brand hashtag, a separately-trading café), so brand-owned inventory could not be confirmed by this method"),
        ("Measurement tags", "GA4 G-L4DG6J5D15 · Google Ads AW-11305512148 · Microsoft Clarity · Shopify · Razorpay"),
        ("Site platform", "Shopify; Cloudflare in front; HSTS present; cache-control on the storefront is private/no-store"),
        ("Published contact", "customercare@arakuoriginals.com · +91 9000394000 (both in the site footer)"),
        ("Shopping feed tagging observed", "utm_medium=product_sync · utm_source=google · utm_content=sag_organic · utm_campaign=sag_organic on product landing URLs"),
        ("Bengaluru relevance", "the homepage meta description reads 'ARAKU is India's first coffee to shape the complete seed-to-cup journey with flagships in Mumbai, Bangalore & Paris', and the same page carries 'India's first premier SCA training campus … now in the heart of Bangalore'"),
        ("Broken paths observed", "/contact-us · /about-us · /faq · /menu · /locations · /book-a-table · /order-online · /privacy-policy · /terms → all 404 on 3 October 2026 (nine paths; the store's information architecture uses different handles, and contact details are published in the footer)"),
        ("Spend · ROAS · CPA", "unavailable (private to the advertiser)"),
        ("Crawl date", CRAWL_DATE),
    ],
    findings=[
        dict(sev="HIGH", title="Every Shopping click is being filed under 'sag_organic'",
             evidence="PLA landing URL captured in the ad archive (verbatim):\nhttps://www.arakucoffee.in/products/timemore-basic-3-0-electronic-espresso-scale?…&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic\nadvertiser: Araku Originals Pvt Ltd (Verified) · ≈200 creatives live",
             reading="The feed is tagging paid Shopping traffic with the campaign name 'sag_organic'. In GA4 that traffic is reported as organic, so the account cannot see what Shopping actually earns — and at roughly two hundred creatives, that is a lot of spend being reported as free. Fixing the feed's tracking template is a minutes-long change with immediate effect on every report the team reads."),
        dict(sev="MEDIUM", title="The storefront's URL structure is non-standard, so conventional links break",
             evidence="GET https://www.arakucoffee.in/contact-us → 404\nGET https://www.arakucoffee.in/about-us   → 404\nGET https://www.arakucoffee.in/faq        → 404\nGET https://www.arakucoffee.in/menu       → 404\nfooter carries: customercare@arakuoriginals.com · +91 9000394000\n(3 October 2026)",
             reading="Ad destinations observed in the archive are product URLs, which work — so paid traffic is safe. The risk is everything off-campaign: press coverage, retail partners, café signage and customers typing obvious addresses. Standard redirects from the conventional handles to the real ones remove that risk permanently."),
        dict(sev="MEDIUM", title="Café and e-commerce are running in the same account without separation",
             evidence="Local ads observed: 'ARAKU Coffee' store listing with Directions / Reserve / call CTAs\nShopping ads observed: 'ARAKU Moka Pot', 'Chemex Coffee Maker 6 cup' — Product Listing Ads\nboth live in the same advertiser account, 3 October 2026",
             reading="Two very different businesses — a café visit and a packaged-coffee order — share one advertiser account and one set of conversion actions. Unless the café and the store have separate conversion definitions, the account cannot tell whether a rupee of spend bought a cup or a bag, which makes budget decisions between them arbitrary."),
        dict(sev="MEDIUM", title="On Meta, the brand term is being crowded by other businesses",
             evidence="meta results for 'Araku Coffee' (country India, active): 86, first page dominated by third-party placements\nobserved examples: a Siemens Home workshop featuring Araku Coffee; a separate café trading as 'ARAKU HOUSE'\nno brand-owned creative could be verified on the first page, 3 October 2026",
             reading="A distinctive brand name is an asset, and it is being spent by others on Meta: a partner using the name in a workshop promotion and a similarly named café in another state. Neither is hostile and neither is confirmed as a problem — but it does mean brand-term searches on Meta return someone else's business before yours, and that is worth a look at the account level."),
        dict(sev="NOTE", title="Razorpay and a clean tag base are in place across the store",
             evidence="RAZORPAY present in the storefront HTML\nGA4 G-L4DG6J5D15 and Google Ads AW-11305512148 confirmed by ID\nfooter: © Araku Originals Pvt Ltd., 2026",
             reading="The measurement base and the payment stack are in place, and the entity disclosure on the site matches the verified advertiser — which is exactly what a brand with a co-operative origin story needs in order to be credible. The work here is in reporting hygiene, not rebuilding."),
    ],
    score_dims=[
        ("Measurement integrity", "GA4 and Ads tags confirmed; feed tagging mislabels paid traffic as organic.", 2),
        ("Conversion observability", "Razorpay in place; café and e-commerce conversions not separable from outside.", 2),
        ("Brand consistency", "Strong, distinctive brand with matching verified advertiser identity.", 4),
        ("Technical health", "Conventional paths 404; storefront cache-control set to no-store.", 3),
        ("Commercial fit", "≈200 live creatives across Shopping, Local and video.", 4),
    ],
    grade="B",
    grade_note="a large, well-stocked account whose reporting is undermined by one feed setting",
    qualification=("Public surfaces only. Meta results for this brand term include other businesses using similar names; nothing here should be read as a claim about those businesses. "
                   "Spend, ROAS and café sell-through are not scored — no public source exists. Ad counts are one-day snapshots."),
    next_steps=[
        ("LOW EFFORT · IMMEDIATE BENEFIT", "Fix the 'sag_organic' campaign tag in the feed", "Until this changes, every Shopping click is recorded as organic traffic and the channel comparison is misleading."),
        ("UNDER AN HOUR", "Add redirects from the conventional URL handles", "contact-us, about-us, faq and menu should land on the pages that exist, for every offline and third-party link in circulation."),
        ("HALF A DAY · BIGGEST SINGLE WIN", "Separate café and e-commerce conversions", "Two conversion actions, two views of spend, and a defensible budget split between the store and the cafés."),
    ],
)

# ---------------------------------------------------------------------------
# VERIFY ROWS — each claim mapped to the exact public surface where it can be checked
# ---------------------------------------------------------------------------
G = "https://adstransparency.google.com/?region=IN&domain={d}"
ADV = "https://adstransparency.google.com/advertiser/{a}?region=IN"
CR = "https://adstransparency.google.com/advertiser/{a}/creative/{c}?region=IN"
ML = "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=IN&q={q}&search_type=keyword_unordered"
MID = "https://www.facebook.com/ads/library/?id={i}"
SRC = "https://{d}"

VERIFY2 = {
"smoor": [
 ("22 live Google creatives", "Google Ads Transparency Center (region: India) — domain view", G.format(d="smoor.in"), "The page header reads '22 ads', under Bliss Chocolates India Private Limited (Verified)."),
 ("The Product Listing Ad title quoted in this report", "Google Ads Transparency Center — the advertiser page", ADV.format(a="AR02616125499809726465"), "One of the creatives is a Product Listing Ad titled 'Elsa and Anna Cake | Frozen Theme Birthday Cake | … by SMOOR | 1.5 Kg'."),
 ("Meta creative 1419659120007418 (since 5 August 2026, corporate gifting)", "Meta Ad Library — the ad itself", MID.format(i="1419659120007418"), "Active; page run by SMOOR Chocolates; landing smoor.in/pages/corporate-gifting. Keyword searches are noisy, so this creative is cited by library ID rather than by a keyword count."),
 ("Meta creative 1059529900062691 (since 3 August 2026)", "Meta Ad Library — the ad itself", MID.format(i="1059529900062691"), "Active on the crawl date; same campaign, same destination page."),
 ("Meta creative 1101131689270428 (since 8 September 2026)", "Meta Ad Library — the ad itself", MID.format(i="1101131689270428"), "Active on the crawl date; same campaign, same destination page."),
 ("GA4 G-JKGWG119TH · Google Ads AW-872198756", "smoor.in page source", SRC.format(d="smoor.in"), "Open the page, press Ctrl+U (view source), then Ctrl+F each ID — both appear."),
 ("/pages/contact and /pages/bulk-enquiry return 404 while /pages/contact-us works", "smoor.in — the URLs themselves (or any HTTP status checker)", "https://smoor.in/pages/contact", "Type the URL: 404. Change it to /pages/contact-us: the contact page loads."),
 ("info@smoorchocolates.com", "smoor.in — FAQ and privacy-policy pages", SRC.format(d="smoor.in/pages/faq"), "Published on the FAQ page; the phone number +91 8822201202 appears in the storefront header."),
 ("Bengaluru stores and the registered entity", "smoor.in — store locator", SRC.format(d="smoor.in/pages/store-locator"), "Lists SMOOR Experience Centre Indiranagar (No. 1131, 100 Feet Road, Indiranagar Stage II, Bengaluru 560038) among other locations, under Bliss Chocolates India Private Limited."),
],
"sidsfarm": [
 ("≈200 creatives in the advertiser account", "Google Ads Transparency Center — advertiser page", ADV.format(a="AR10174224753343070209"), "The header reads approximately 200 ads under Sids Farm Private Limited (Verified)."),
 ("35 creatives point at sidsfarm.com", "Google Ads Transparency Center — domain view", G.format(d="sidsfarm.com"), "The domain view header reads '35 ads'."),
 ("Meta creative library ID 1682864186042714 (WhatsApp click-through)", "Meta Ad Library — the ad itself", MID.format(i="1682864186042714"), "A Sid's Farm ad on the page 'Sid's Farm' (facebook.com/sidsfarmpure), running since 8 April 2026, with a WhatsApp CTA."),
 ("Meta creative library ID 28227187223577653 and its landing URL", "Meta Ad Library — the ad itself", MID.format(i="28227187223577653"), "The '22g protein' ad, running since 17 August 2026, landing app.sidsfarm.com with utm_source=facebook and {{campaign.id}} macros."),
 ("Two GTM containers and four tag families on one storefront", "sidsfarm.com page source", SRC.format(d="sidsfarm.com"), "Ctrl+F for GTM-57TDVNH, GTM-P4DXD97J, G-YN4FLEL9J2 and connect.facebook.net — all four appear."),
 ("Seven storefront paths return 404", "sidsfarm.com — the URLs themselves", SRC.format(d="sidsfarm.com/pages/faq"), "Try /pages/faq, /pages/contact, /policies/shipping-policy, /pages/store-locator — each returns 404."),
 ("wecare@sidsfarm.com", "sidsfarm.com — cart and collection pages", SRC.format(d="sidsfarm.com/collections/all"), "Published in the footer of the storefront pages."),
 ("Bengaluru is a served market", "sidsfarm.com — the location selector and homepage copy", SRC.format(d="sidsfarm.com"), "The 'Select Location' control lists Bangalore, and the homepage reads 'If you're from Hyderabad, Bengaluru, Pune, Vijayawada …'."),
],
"barbequenation": [
 ("19 creatives in the advertiser account", "Google Ads Transparency Center — advertiser page", ADV.format(a="AR07883744464190046209"), "The header reads '19 ads' under UNITED FOODBRANDS LIMITED (Verified)."),
 ("34 creatives point at the domain — 15 more than the account holds", "Google Ads Transparency Center — domain view", G.format(d="barbequenation.com"), "The domain view header reads '34 ads', and Google notes the domain includes results for multiple advertiser accounts."),
 ("Meta creative library ID 1629049651915814 (SAVE35 takeaway offer)", "Meta Ad Library — the ad itself", MID.format(i="1629049651915814"), "Barbeque Nation's own page, running since 13 September 2026, 'FLAT 35% OFF on Takeaway Orders' with code SAVE35, landing /ubq-delivery."),
 ("Meta creative library ID 1595578738733856 (pay-day buffet, valid to 11 October 2026)", "Meta Ad Library — the ad itself", MID.format(i="1595578738733856"), "The pay-day offer ad, running since 22 September 2026, landing /deals/unlockspecialdeals."),
 ("GTM-TF3NNN · Meta pixel · Razorpay", "barbequenation.com page source", SRC.format(d="barbequenation.com"), "Ctrl+F each string in view source — the container ID, connect.facebook.net and Razorpay references all appear."),
 ("/menu, /book-a-table, /locations, /order-online, /terms return 404", "barbequenation.com — the URLs themselves", SRC.format(d="barbequenation.com/menu"), "Each returns 404, while the ad destinations /ubq-delivery and /deals/unlockspecialdeals load."),
 ("feedback@barbequenation.com", "barbequenation.com — About-Us and Contact-Us pages", SRC.format(d="barbequenation.com/contact-us"), "Published on the contact page, with the registered office address in Bengaluru 560035 and the number 08064058059."),
 ("Two different legal names — the site's and the advertiser's", "barbequenation.com footer vs Google Ads Transparency", ADV.format(a="AR07883744464190046209"), "The site names Barbeque Nation Hospitality Limited; Google's advertiser of record is the parent, UNITED FOODBRANDS LIMITED."),
],
"milletamma": [
 ("80 live Google creatives", "Google Ads Transparency Center — advertiser page", ADV.format(a="AR06400845011688095745"), "The header reads '80 ads' under URBAN MONK PRIVATE LIMITED (Verified)."),
 ("The legal entity on the site matches the verified advertiser", "milletamma.com — terms and conditions page", SRC.format(d="milletamma.com/policies/terms-of-service"), "The footer reads 'Copyright © 2026 URBAN MONK PRIVATE LIMITED, All Rights Reserved.'"),
 ("The archived local-ad creative and its removal notice", "Google Ads Transparency Center — the creative itself", CR.format(a="AR06400845011688095745", c="CR03268659855321202689"), "Google's archive shows 'Last shown: Jul 15, 2026' and 'Removed for a policy violation' on this local ad, with the template text '{KeyWord:Millet Amma}' still visible."),
 ("Meta creative library ID 1355783896518419 (Ragi Laddoo, since 7 July 2026)", "Meta Ad Library — the ad itself", MID.format(i="1355783896518419"), "On the Millet Amma page, landing milletamma.com/products/ragi-laddo-300g."),
 ("Two GA4 properties live at once", "milletamma.com page source", SRC.format(d="milletamma.com"), "Ctrl+F for G-WH82716CE0 and G-N659GJMWCX — both appear in the same page source, alongside AW-378561932."),
 ("The site-wide sale banner", "milletamma.com — any storefront page", SRC.format(d="milletamma.com"), "The announcement bar reads 'Our Biggest Sale Yet: Up To 20% Off + Free Prepaid Shipping.'"),
 ("eatright@milletamma.com · orders@milletamma.com · +91 7624979333", "milletamma.com — cart, collection and terms pages", SRC.format(d="milletamma.com/cart"), "eatright@ appears on the cart and collection pages; orders@ appears on the terms-of-service page; the phone number appears in the storefront."),
 ("The Bengaluru address", "milletamma.com — the 'Get in touch' block on the cart page", SRC.format(d="milletamma.com/cart"), "Reads No. 12, K 345, Yemalur Main Road, HAL Airport Area, Bellandur, Bengaluru, Karnataka 560037."),
],
"adukale": [
 ("13 live Google creatives", "Google Ads Transparency Center (region: India) — domain view", G.format(d="adukale.com"), "The header reads '13 ads' under SANKETHI NUTRIMENTS PRIVATE LIMITED (Verified), including a Product Listing Ad titled 'Buy Rice Idli | Healthy Breakfast | Adukale'."),
 ("The Amazon routing announcement", "adukale.com — home and cart pages", SRC.format(d="adukale.com"), "The announcement bar reads 'All purchases from this site will now be completed through Amazon. Enjoy the same authentic taste with greater ease.'"),
 ("The placeholder pickup address on the live site", "adukale.com — home or collection pages", SRC.format(d="adukale.com"), "Ctrl+F for '123 John Doe' — the pickup block shows '123 John Doe Street, Your Town, YT 12345' next to the real pickup point at 155 Madappa Building, Mallathalli."),
 ("The email icon that is not a mailto link", "adukale.com — page source", SRC.format(d="adukale.com"), "Ctrl+F for 'href=\"info@adukale.com\"' — the address is correct and visible; the link around the icon has no mailto: prefix."),
 ("Three Shopping variations with Google's removal notice", "Google Ads Transparency Center — the ad itself", CR.format(a="AR18362132152826462209", c="CR11719898640389505025"), "The ad detail page shows 'Last shown: Nov 28, 2025' and 'Removed for a policy violation' on all three variations (Sambar Powder, Chutney Powder 200g, Kayi Kodubale 180g)."),
 ("Two GA4 properties and one Ads tag", "adukale.com page source", SRC.format(d="adukale.com"), "Ctrl+F for G-X6WD89C59X, G-66YCE4PEZM and AW-812528734 — all three appear."),
 ("No Meta ads active for the brand term", "Meta Ad Library (country: India, active ads)", ML.format(q="Adukale"), "The page shows 'No ads match your search criteria' for this term."),
 ("info@adukale.com · +91 9035462696", "adukale.com — cart and collection pages", SRC.format(d="adukale.com/cart"), "Published in the storefront, with the Bengaluru 560091 address (Sankethi Nutriments Pvt. Ltd, Kannahalli Village) and a helpdesk window of 8AM–8PM, Mon–Sun."),
],
"organicmandya": [
 ("69 creatives in the advertiser account", "Google Ads Transparency Center — advertiser page", ADV.format(a="AR08930861279116001281"), "The header reads '69 ads' under MANDYA ORGANIC FOODS PRIVATE LIMITED (Verified)."),
 ("67 creatives point at organicmandya.com", "Google Ads Transparency Center — domain view", G.format(d="organicmandya.com"), "The domain view header reads '67 ads'."),
 ("The two-hour delivery promise", "organicmandya.com — the announcement bar", SRC.format(d="organicmandya.com"), "The bar reads '2-hr delivery in Bengaluru, Hyderabad & Mysuru — ₹49 delivery charge on orders under ₹500, FREE above ₹500'."),
 ("Meta creative library ID 1432155482101394 (since 13 September 2026)", "Meta Ad Library — the ad itself", MID.format(i="1432155482101394"), "On the Organic Mandya page, landing the millet-upma collection."),
 ("Custom dataLayer event names and GA4 G-MHKC4DNNH3", "organicmandya.com page source", SRC.format(d="organicmandya.com"), "Ctrl+F for gtm-promo, gtm-creative, gtm-position and G-MHKC4DNNH3 — all appear, alongside AW-16535163896."),
 ("/pages/faq, /pages/bulk-enquiry and /pages/corporate-gifting return 404", "organicmandya.com — the URLs themselves", SRC.format(d="organicmandya.com/pages/faq"), "Each returns 404."),
 ("support@organicmandya.com · +91 9590922000", "organicmandya.com — cart and collection pages", SRC.format(d="organicmandya.com/cart"), "Published in the storefront; the phone number is also in the announcement bar."),
],
"pureandsure": [
 ("37 live Google creatives", "Google Ads Transparency Center (region: India) — domain view", G.format(d="pureandsure.in"), "The header reads '37 ads' under Phalada Organic Consumer Products Private Limited (Verified)."),
 ("The 'sag_organic' campaign tag on paid Shopping clicks", "Google Ads Transparency Center — the advertiser page, then an ad's destination URL", ADV.format(a="AR04550905857457520641"), "The organic ghee ad's landing URL ends with utm_medium=product_sync&utm_source=google&utm_campaign=sag_organic."),
 ("GA4 G-VGC836EHVF · GTM-KP8NPFKZ · AW-16785598661 · Meta pixel", "pureandsure.in page source", SRC.format(d="pureandsure.in"), "Ctrl+F each ID — all four appear."),
 ("Free shipping above ₹500", "pureandsure.in — site banner", SRC.format(d="pureandsure.in"), "The banner reads 'Free Shipping on orders above ₹500'."),
 ("/pages/contact-us returns 404 while /pages/contact works", "pureandsure.in — the URLs themselves", SRC.format(d="pureandsure.in/pages/contact"), "Try both: /pages/contact loads, /pages/contact-us returns 404."),
 ("info@pureandsure.in · care@pureandsure.in · 1800 121 0369", "pureandsure.in — contact, shipping-policy, cart pages", SRC.format(d="pureandsure.in/pages/contact"), "info@ is on the contact and shipping pages; care@ is on the cart and collection pages."),
 ("The Bengaluru registered address", "pureandsure.in — footer of the cart and collection pages", SRC.format(d="pureandsure.in/cart"), "Reads Phalada Organic Consumer Products Pvt Ltd, 92/5, Kannalli Village, Seegehalli, Magadi Main Road, Bangalore 560091."),
],
"eatbetterco": [
 ("29 creatives live for the domain; 27 in the advertiser account", "Google Ads Transparency Center — domain and advertiser views", G.format(d="eatbetterco.com"), "The domain view reads '29 ads'; the advertiser page (EAT BETTER VENTURES PRIVATE LIMITED, Verified) reads '27 ads'."),
 ("Discount values as low as −1%, −2% and −6% in the Shopping feed", "Google Ads Transparency Center — the advertiser page", ADV.format(a="AR17084581177009897473"), "The Product Listing Ad titles carry the discount badges, landing on /products/ URLs with variant parameters."),
 ("GA4 G-90QE4TSKTH · Google Ads AW-610414449", "eatbetterco.com page source", SRC.format(d="eatbetterco.com"), "Ctrl+F both IDs — they appear."),
 ("Published shipping terms (free above ₹500, prepaid ₹49, COD ₹79, 3 working days)", "eatbetterco.com — shipping policy and FAQ", SRC.format(d="eatbetterco.com/policies/shipping-policy"), "The policy page states the thresholds; the contact page states the 3-working-day delivery window."),
 ("care@eatbetterco.com (contact/refund pages) and connect@gottaeatbetter.com (privacy/shipping pages)", "eatbetterco.com — policy pages", SRC.format(d="eatbetterco.com/policies/privacy-policy"), "Each address appears on the pages named; the company name in the site title is 'Eat Better Co - As seen on Shark Tank'."),
 ("Five storefront paths return 404", "eatbetterco.com — the URLs themselves", SRC.format(d="eatbetterco.com/pages/faq"), "Try /pages/faq, /pages/about-us, /pages/contact, /pages/store-locator, /pages/bulk-enquiry — each returns 404, while /pages/contact-us works."),
 ("The Jaipur registered address (the Bengaluru-relevance note)", "eatbetterco.com — contact page", SRC.format(d="eatbetterco.com/pages/contact-us"), "Reads Eat Better Ventures Pvt Ltd, A1/A2, Vastushree Colony, 100 Feet Road, Manyawas, Mansarovar, Jaipur, Rajasthan 302020 — which is why this lead is labelled pan-India rather than Bengaluru-based."),
 ("The corporate-gifting figures quoted in this audit", "eatbetterco.com — corporate gifting page", SRC.format(d="eatbetterco.com/pages/corporate-gifting"), "The page states '10 LAKH+ hampers delivered pan-India', '500+ corporates & organizations' and '25 hampers designs this Diwali', with hampers from ₹249 to ₹2,499."),
],
"brikoven": [
 ("42 creatives in the advertiser account", "Google Ads Transparency Center — advertiser page", ADV.format(a="AR15322972474807681025"), "The header reads '42 ads' under Brik Oven Pvt Ltd (Verified)."),
 ("25 creatives point at brikoven.com", "Google Ads Transparency Center — domain view", G.format(d="brikoven.com"), "The domain view header reads '25 ads', and the visible set is Local store ads for Palace Road, Whitefield, Koramangala and Manyata Business Park."),
 ("The third-party reservation widget on a live local ad", "Google Ads Transparency Center — the advertiser page", ADV.format(a="AR15322972474807681025"), "The Manyata Business Park local ad in this account shows 'Book now • widget.reservego.co/' as its call to action."),
 ("The stopped store creative", "Google Ads Transparency Center — the creative itself", CR.format(a="AR15322972474807681025", c="CR16763555951004352513"), "Google's archive states 'Last shown: Jul 23, 2026' for the Palace Road breakfast creative."),
 ("GTM-PMCQMP4 · GA4 G-6HE7Y2G8N3 · Squarespace", "brikoven.com page source", SRC.format(d="brikoven.com"), "Ctrl+F each — the container ID, measurement ID and Squarespace assets all appear."),
 ("theteam@brikoven.com", "brikoven.com — contact block", SRC.format(d="brikoven.com"), "Published in the site's contact block next to the social links."),
 ("The four Bengaluru outlets", "brikoven.com — the Locations block on the home page", SRC.format(d="brikoven.com"), "Lists Church Street (560001), Indiranagar (560038), Palace Road (560001) and Koramangala (560034), each with its own phone number."),
 ("Eight conventional paths return 404", "brikoven.com — the URLs themselves", SRC.format(d="brikoven.com/contact-us"), "Try /contact-us, /menu, /book-a-table, /locations, /order-online — each returns 404."),
],
"arakucoffee": [
 ("≈200 live Google creatives", "Google Ads Transparency Center (region: India) — domain view", G.format(d="arakucoffee.in"), "The header reads approximately 200 ads under Araku Originals Pvt Ltd (Verified)."),
 ("Shopping ads running with 'sag_organic' campaign tagging", "Google Ads Transparency Center — the advertiser page", ADV.format(a="AR16285151475322060801"), "Product Listing Ads for the Moka Pot and the Chemex land on product URLs whose tracking ends with utm_campaign=sag_organic."),
 ("Local ads for the café alongside store product ads", "Google Ads Transparency Center — the advertiser page", ADV.format(a="AR16285151475322060801"), "The account shows a local 'ARAKU Coffee' listing with Directions/Reserve CTAs together with Shopping ads for equipment."),
 ("GA4 G-L4DG6J5D15 · AW-11305512148 · Razorpay", "arakucoffee.in page source", SRC.format(d="arakucoffee.in"), "Ctrl+F each string — the IDs and the Razorpay reference appear."),
 ("customercare@arakuoriginals.com · +91 9000394000", "arakucoffee.in — site footer", SRC.format(d="arakucoffee.in"), "Both appear in the footer, next to '© Araku Originals Pvt Ltd., 2026'."),
 ("The Bangalore flagship and training campus", "arakucoffee.in — homepage copy and meta description", SRC.format(d="arakucoffee.in"), "The page reads 'India's first premier SCA training campus … now in the heart of Bangalore', and the meta description names flagships in Mumbai, Bangalore & Paris."),
 ("Meta results for the brand term include other businesses", "Meta Ad Library (country: India)", ML.format(q="Araku Coffee"), "The first page shows third-party placements (for example a Siemens Home workshop featuring Araku Coffee) rather than brand-owned creatives."),
],
}


# ---------------------------------------------------------------------------
# Normalisation: give every lead the row label that the shared report builder
# looks up ("Google creatives live"), taken from its own measured inventory row.
# ---------------------------------------------------------------------------
for _slug, _lead in E2.items():
    _rows = _lead["ad_account"]
    if not any(k.lower().startswith("google creatives live") for k, _ in _rows):
        _inv = next((v for k, v in _rows if k.lower().startswith("google creative inventory")), None)
        if _inv:
            _rows.insert(0, ("Google creatives live", _inv))
    _lead.setdefault("generated_on", CRAWL_DATE)


# ---------------------------------------------------------------------------
# Keys are remapped to the pack's own slug convention (audit_pdf_food._slug) so
# file names, the workbook and the lead index all agree.
# ---------------------------------------------------------------------------
from audit_pdf_food import _slug as _mk_slug  # noqa: E402

SLUG_REMAP = {k: _mk_slug(v["brand"]) for k, v in E2.items()}
E2 = {SLUG_REMAP[k]: v for k, v in E2.items()}
VERIFY2 = {SLUG_REMAP[k]: v for k, v in VERIFY2.items()}
