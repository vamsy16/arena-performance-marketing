# -*- coding: utf-8 -*-
"""
Lead records for BATCH 2 (ten more Food/Bengaluru leads, added 3 October 2026).

Every statement here traces to the same measured evidence that produced the audits
(see batch2_evidence.py and VERIFY-THE-DATA.md). No estimates, no projections, no
spend/ROAS/CPA figures. Emails were crawled from the brand's own pages — the exact
page is recorded in `contact_source` and in the workbook.

`outreach` holds the four-email sequence as (subject, body_html) pairs.
"""

SIGN = "<br/><br/>- Smart Pursuit, Bengaluru | 7095024220 | smartpursuit3@gmail.com"

LEADS2 = {}

# ----------------------------------------------------------------- SMOOR
LEADS2["smoor"] = dict(
    brand="SMOOR", website="smoor.in", instagram="",
    contact=dict(email="info@smoorchocolates.com", phone="+91 8822201202",
                 entity="Bliss Chocolates India Private Limited",
                 address="Bengaluru, Karnataka, India"),
    contact_source="Crawled from smoor.in (FAQ and privacy-policy pages) on 03 Oct 2026; phone +91 8822201202 and the Indiranagar store address from the store-locator page.",
    niche="Premium Chocolates & Gifting", score=8, ads_active=22,
    headline="22 live Google creatives carrying the account, and two enquiry paths that return 404.",
    stats=[["22", "Google creatives live"], ["3", "Meta ads verified by ID"], ["2", "Dead enquiry paths"], ["Bengaluru", "Indiranagar flagship"]],
    ad_intro=("SMOOR sells occasion chocolate — cakes, hampers, corporate gifting — and runs a live Google account of 22 creatives under its "
              "own verified entity, Bliss Chocolates India Private Limited. The visible inventory includes Product Listing Ads, so the shopping "
              "feed is doing real work. On Meta, three creatives were verified by library ID, all pointed at the corporate-gifting page and all "
              "running from early August into September 2026: this is a brand that has decided to sell hampers to companies. The leaks are small "
              "and specific: two enquiry URLs that Google paid traffic may still hit return 404, the PLA titles are written for matching rather "
              "than for a phone screen, and the live offer excludes exactly the category most people arrive for."),
    ad_intelligence=[
        ["Google Ads (verified)", "22 creatives, advertiser Bliss Chocolates India Private Limited (identity verified by Google); inventory includes Product Listing Ads."],
        ["Meta (verified by ID)", "1419659120007418 (running since 5 Aug 2026), 1059529900062691 (3 Aug 2026), 1101131689270428 (8 Sep 2026) — all landing /pages/corporate-gifting."],
        ["Measurement stack", "GTM-WWTJQSR · GA4 G-JKGWG119TH · Google Ads AW-872198756 · Microsoft Clarity · Judge.me."],
        ["Destination audit", "/pages/contact-us and /pages/corporate-gifting return 200; /pages/contact and /pages/bulk-enquiry return 404."],
        ["Offer on site", "'Get Exclusive 10% OFF On The MRP Of All Products, Except Celebration Cakes'."],
    ],
    scores={"Creative Variety": [7, "#F59E0B"], "UGC & Social Proof": [6, "#F59E0B"], "Copy & Hook Strength": [6, "#F59E0B"],
            "Landing Page CRO": [6, "#F59E0B"], "Tracking & CAPI": [7, "#22C55E"], "Retargeting Depth": [5, "#EF4444"]},
    findings=[
        "<b>Two enquiry paths return 404:</b> /pages/contact and /pages/bulk-enquiry are dead while /pages/contact-us and /pages/corporate-gifting work. Every old link, deck and directory listing points at the dead pair.",
        "<b>PLA titles are written for matching, not for people:</b> one live Shopping title stacks four near-synonyms before naming the product ('Elsa and Anna Cake | Frozen Theme Birthday Cake | Elsa & Anna Kids Designer Cake | Princess Celebration Cake by SMOOR | 1.5 Kg'). That is a feed-writing decision, and it is the cheapest lever in the account.",
        "<b>Meta is selling to companies:</b> all three verified creatives land on the corporate-gifting page with a 'Get Quote' call to action — but nothing observable from outside confirms a quote request fires a tracked event.",
        "<b>The offer has an exception built in:</b> 10% off excludes celebration cakes, the category with the highest intent on the site.",
        "<b>The measurement stack is complete:</b> GTM, GA4, Ads tag, Clarity and Judge.me are all present — so the 404s are a maintenance gap, not a capability gap.",
    ],
    competitors=[["Other premium chocolate brands (Bengaluru and national)", "Larger paid footprints and heavier retail presence.", "SMOOR's own experience centres and corporate-gifting page are real assets — put the store network and the entity behind them into the ad copy."],
                 ["Gifting marketplaces and aggregators", "Own the 'corporate gifting' search with landing pages and quote forms.", "SMOOR has the page; it needs the quote event tracked so the channel can be judged on leads."],
                 ["Grocery quick-commerce chocolate aisles", "Win on instant delivery.", "SMOOR wins on occasion quality — say it in the feed titles and the first line of the Meta copy."]],
    wins=[["WIN 1 - Redirect the dead pair", "Point /pages/contact and /pages/bulk-enquiry at the working pages. One afternoon, and it recovers traffic you already paid for.", "#EF4444", "#FEF2F2"],
          ["WIN 2 - Rewrite the five longest PLA titles", "Shorten for a phone screen and lead with the product. Same feed, same spend, clearer listing.", "#F59E0B", "#FFFBEB"],
          ["WIN 3 - Instrument the gifting enquiry", "One event on the corporate-gifting quote form so the B2B push is judged on leads rather than visits.", "#F59E0B", "#FFFBEB"]],
    impact=[["Metric", "Current (live)", "What the fix is", "Why it matters"],
            ["Dead enquiry paths", "2 of 4 return 404", "Redirect to the working pages", "Recovers paid traffic that currently lands on nothing"],
            ["Shopping titles", "Up to 12 words before the product name", "Rewrite the five longest titles", "Better readability on a phone screen"],
            ["Gifting enquiry", "Quote event not observable", "Add one tracked event", "The B2B campaign becomes measurable on leads"]],
    sources=["Google Ads Transparency (region IN), 3 Oct 2026: 22 creatives for smoor.in under Bliss Chocolates India Private Limited (Verified); PLA title captured verbatim.",
             "Meta Ad Library (country IN), 3 Oct 2026: library IDs 1419659120007418, 1059529900062691, 1101131689270428 landing /pages/corporate-gifting.",
             "smoor.in, 3 Oct 2026: tag IDs GTM-WWTJQSR / G-JKGWG119TH / AW-872198756 / Clarity / Judge.me; 404s on /pages/contact and /pages/bulk-enquiry; store locator with Bengaluru addresses; info@smoorchocolates.com."],
    outreach=[
        ["Email 1 (Day 1): 22 live Google ads — and two enquiry pages that go nowhere",
         "Hi team,<br/><br/>I audit paid media for Bengaluru food brands. I went through your live footprint this week: <b>22 Google creatives</b> running under Bliss Chocolates India Private Limited, including Shopping ads, plus three Meta creatives selling corporate gifting into your /pages/corporate-gifting page.<br/><br/>Two things worth ten minutes: /pages/contact and /pages/bulk-enquiry both return 404 today, and your live offer excludes celebration cakes — the category most people arrive for.<br/><br/>The attached Paid Media &amp; Measurement Audit has the full picture, with the URL for every claim." + SIGN],
        ["Email 2 (Day 3): Your Shopping titles are doing too much work",
         "Hi team,<br/><br/>Second thought from the audit. One of your live Shopping titles is: 'Elsa and Anna Cake | Frozen Theme Birthday Cake | Elsa &amp; Anna Kids Designer Cake | Princess Celebration Cake by SMOOR | 1.5 Kg'.<br/><br/>That title is optimised for matching, not for the person reading it on a phone. A feed pass over the five longest titles usually improves click-through before any bid change — and it costs nothing.<br/><br/>Happy to send the rewritten titles as a starting point." + SIGN],
        ["Email 3 (Day 7): You are selling to companies — is the quote tracked?",
         "Hi team,<br/><br/>Third thought. All three of your verified Meta creatives point at the corporate-gifting page and ask for a quote. The page works; the ads are well aimed.<br/><br/>What I cannot see from outside is whether a quote request fires a tracked event. If it does not, that campaign can only ever be judged on clicks. One event on the form makes the whole quarter's gifting push measurable.<br/><br/>Worth a check before the Diwali window closes." + SIGN],
        ["Email 4 (Day 14): Closing the file on SMOOR",
         "Hi team,<br/><br/>Last note from me. The audit's three fixes are deliberately small: redirect two dead enquiry URLs, rewrite the five longest Shopping titles, and put one tracked event behind the corporate-gifting quote form.<br/><br/>If the timing is wrong, no problem — reply 'later' and I will leave it there.<br/><br/>The audit is yours either way." + SIGN],
    ],
)

# ----------------------------------------------------------------- SID'S FARM
LEADS2["sidsfarm"] = dict(
    brand="Sid's Farm", website="sidsfarm.com", instagram="",
    contact=dict(email="wecare@sidsfarm.com", phone="",
                 entity="Sids Farm Private Limited",
                 address="Hyderabad, Telangana (serves Bengaluru)"),
    contact_source="Crawled from sidsfarm.com (cart and collection pages) on 03 Oct 2026; the address on the privacy-policy and terms pages is in Hyderabad 500085, and the site's location selector lists Bangalore.",
    niche="Farm-Fresh Dairy Subscription", score=8, ads_active=35,
    headline="A subscription dairy running ~200 creatives — with seven trust pages returning 404 and the Meta pixel switched off in the store's own config.",
    stats=[["~200", "Creatives in account"], ["35", "Pointing at the website"], ["7", "Trust pages returning 404"], ["2", "GTM containers loading"]],
    ad_intro=("Sid's Farm sells tested, subscription milk in Bengaluru, Hyderabad, Pune and Vijayawada, and it advertises like a modern subscription "
              "business: roughly 200 creatives in the advertiser account, 35 of them pointed at sidsfarm.com, plus Meta creatives running since "
              "April 2026 that send people to WhatsApp and to the app with proper campaign and ad-ID macros attached. The paid engine is real. "
              "The leak is the storefront underneath it: seven standard paths — contact, FAQ, shipping policy, store locator, bulk and corporate — "
              "all return 404, two Google Tag Manager containers load on the same page, and the store's own configuration reads "
              "meta_pixel_enable: false while Meta ads are live."),
    ad_intelligence=[
        ["Google Ads (verified)", "≈200 creatives in the advertiser account (Sids Farm Private Limited, Verified); 35 creatives point specifically at sidsfarm.com."],
        ["Meta (verified by ID)", "1682864186042714 (since 8 Apr 2026, WhatsApp CTA) · 28227187223577653 (since 17 Aug 2026, 'now with 22g protein', landing app.sidsfarm.com with {{campaign.id}} macros) · 2322194535253458 (since 18 Aug 2026, multiple versions)."],
        ["Measurement stack", "GA4 G-YN4FLEL9J2 · Google Tag Manager GTM-57TDVNH · Google Tag Manager GTM-P4DXD97J · Microsoft Clarity."],
        ["Store config (verbatim)", "container_id: \"GTM-57TDVNH\", measurement_id: \"G-YN4FLEL9J2\", meta_pixel_enable: false, meta_pixel_id: \"\", built_in_conversion_tracking: 0."],
        ["Destination audit", "/pages/faq, /pages/contact, /pages/contact-us, /policies/shipping-policy, /pages/store-locator, /pages/bulk-enquiry, /pages/corporate-gifting — all 404 on 3 Oct 2026."],
    ],
    scores={"Creative Variety": [8, "#22C55E"], "UGC & Social Proof": [6, "#F59E0B"], "Copy & Hook Strength": [8, "#22C55E"],
            "Landing Page CRO": [4, "#EF4444"], "Tracking & CAPI": [4, "#EF4444"], "Retargeting Depth": [6, "#F59E0B"]},
    findings=[
        "<b>Seven trust pages return 404:</b> contact, FAQ, shipping policy, store locator, bulk and corporate-gifting are all dead — every path a cautious first-time subscriber looks for before paying.",
        "<b>Two GTM containers load together:</b> GTM-57TDVNH and GTM-P4DXD97J both appear in the same page source, the classic cause of duplicated purchase or signup events.",
        "<b>The store's own config has the Meta pixel switched off:</b> verbatim, meta_pixel_enable: false with an empty meta_pixel_id — while three Meta creatives run. The pixel could still fire through the GTM container, but the first thing to check is which is true.",
        "<b>Most creative volume never touches the website:</b> ≈165 of ≈200 creatives point elsewhere, consistent with the WhatsApp and app.sidsfarm.com paths seen in the Meta library — good strategy, but website reporting cannot see it.",
        "<b>Meta is being run well:</b> the protein-led copy ('No diet changes. No extra effort. Just your everyday milk, now with 22g protein in every pack.') and the {{campaign.id}}/{{ad.id}} macros on the app landing URL are signs of a team that knows what it is doing.",
    ],
    competitors=[["Regional dairy subscription brands", "Heavy local distribution and retail shelf presence.", "Sid's Farm's testing message and app-based subscription are the differentiators — put the tests in the ad copy, not just the packaging."],
                 ["Quick-commerce dairy (10-minute delivery)", "Win on speed and price comparison.", "Win on provenance and daily testing; the two-hour/instant race is not the one to enter."],
                 ["D2C milk brands with polished storefronts", "Publish FAQ, delivery and contact information where buyers look.", "That is the gap here — four pages of content fix it."]],
    wins=[["WIN 1 - Publish the missing trust pages", "Contact, FAQ and shipping policy are 30-minute pages. They sit directly in front of a subscription decision.", "#EF4444", "#FEF2F2"],
          ["WIN 2 - Settle the container and pixel settings", "Merge the two GTM containers, and confirm whether the store's Meta pixel is intentionally off. Both decide what your reporting can be trusted for.", "#EF4444", "#FEF2F2"],
          ["WIN 3 - One weekly report for the app and the website", "App signups and website orders in one view, so subscription growth is counted once.", "#F59E0B", "#FFFBEB"]],
    impact=[["Metric", "Current (live)", "What the fix is", "Why it matters"],
            ["Trust pages", "7 paths return 404", "Publish contact, FAQ, shipping policy", "Removes friction right before a first payment"],
            ["Tag setup", "Two GTM containers; pixel off in store config", "Merge containers; confirm the pixel decision", "Ends duplicate-event risk and click-only optimisation"],
            ["Reporting scope", "≈165 creatives land off-site", "One combined weekly view", "Subscription growth measured once"]],
    sources=["Google Ads Transparency (region IN), 3 Oct 2026: ≈200 creatives for Sids Farm Private Limited (Verified); 35 pointing at sidsfarm.com.",
             "Meta Ad Library (country IN), 3 Oct 2026: library IDs 1682864186042714, 28227187223577653, 2322194535253458; app.sidsfarm.com landing with utm_source=facebook&utm_medium=paid_social and campaign/ad macros.",
             "sidsfarm.com, 3 Oct 2026: GTM-57TDVNH, GTM-P4DXD97J, G-YN4FLEL9J2, Clarity, meta_pixel_enable: false; seven 404 paths; Bengaluru listed in the location selector; wecare@sidsfarm.com."],
    outreach=[
        ["Email 1 (Day 1): Seven 404s under a paid engine that is working",
         "Hi team,<br/><br/>I audit paid media for Bengaluru food brands. Your paid side is genuinely good: around <b>200 creatives</b> in the account, three Meta creatives verified by ID running since April and August, and an app landing URL with proper campaign macros attached.<br/><br/>Underneath it, seven standard pages return 404 today — contact, FAQ, shipping policy, store locator, bulk and corporate-gifting. For a subscription where the first order is a trust decision, those are the most expensive pages on the site.<br/><br/>The attached audit lists every URL and every measurement." + SIGN],
        ["Email 2 (Day 3): Two settings worth checking today",
         "Hi team,<br/><br/>Two configuration findings from the audit, both verifiable in your own dashboard.<br/><br/>1. Two Google Tag Manager containers load on the same page (GTM-57TDVNH and GTM-P4DXD97J). That pattern normally produces duplicated purchase or signup events.<br/>2. Your store config reads meta_pixel_enable: false with an empty pixel ID — while Meta ads are running. It may be fired through GTM instead, but that is worth knowing for certain.<br/><br/>Both take an hour to settle and both decide whether ROAS discussions are winnable." + SIGN],
        ["Email 3 (Day 7): Your Meta copy is a template for the rest of the category",
         "Hi team,<br/><br/>Third note, this one a compliment. 'No diet changes. No extra effort. Just your everyday milk, now with 22g protein in every pack.' is the right way to sell a subscription — a product change, not a discount.<br/><br/>The same story is missing on the site: the pages that explain testing have no equivalent. If you want, I will map the three pages (testing, delivery, subscription terms) against what your Meta traffic actually asks." + SIGN],
        ["Email 4 (Day 14): Closing the file on Sid's Farm",
         "Hi team,<br/><br/>Wrapping up. The audit comes down to three fixes: publish the four missing trust pages, settle the double container and the pixel setting, and report app and website growth as one number.<br/><br/>No pressure at all — if you would rather just take the page list and run with it internally, that is a perfectly good outcome." + SIGN],
    ],
)

# ----------------------------------------------------------------- BARBEQUE NATION
LEADS2["barbequenation"] = dict(
    brand="Barbeque Nation", website="barbequenation.com", instagram="",
    contact=dict(email="feedback@barbequenation.com", phone="08064058059",
                 entity="United Foodbrands Limited (site: Barbeque Nation Hospitality Limited)",
                 address="Saket Callipolis, Units 601 & 602, 6th Floor, Doddakannalli Village, Varthur Hobli, Sarjapur Road, Bengaluru 560035"),
    contact_source="Crawled from barbequenation.com (About-Us, Contact-Us and FAQ pages) on 03 Oct 2026; the registered office and phone number are published on the contact page.",
    niche="Casual Dining & Takeaway", score=8, ads_active=34,
    headline="Fifteen of the 34 creatives pointing at your domain are paid for by accounts that are not yours — and one live ad shows two different discount codes.",
    stats=[["34", "Creatives pointing at the domain"], ["19", "In your own account"], ["15", "From other accounts"], ["3", "Meta ads verified by ID"]],
    ad_intro=("Barbeque Nation is the largest advertiser in this batch in absolute terms: 34 creatives point at barbequenation.com, of which only 19 sit "
              "in the United Foodbrands Limited account (verified by Google) — the other 15 come from somewhere else, which is worth a conversation with "
              "partners or franchisees. On Meta, brand-owned creatives were verified by ID: a takeaway offer launched on 13 September, a pay-day buffet "
              "campaign valid to 11 October, and a multi-version creative from 11 September. The takeaway ad is also the clearest single defect in this "
              "batch: its copy says SAVE35 while the image inside the same ad says SAVE5."),
    ad_intelligence=[
        ["Google Ads (verified)", "19 creatives in the UNITED FOODBRANDS LIMITED account (Verified); 34 creatives point at barbequenation.com in total — a 15-creative gap."],
        ["Meta (verified by ID)", "1629049651915814 (since 13 Sep 2026, takeaway SAVE35 → /ubq-delivery) · 1595578738733856 (since 22 Sep 2026, pay-day buffet valid to 11 Oct 2026 → /deals/unlockspecialdeals) · 1727327792321770 (since 11 Sep 2026, multiple versions)."],
        ["Measurement stack", "Google Tag Manager GTM-TF3NNN · Meta's connect.facebook.net script loaded (pixel ID not visible in the page source) · Razorpay on the ordering side."],
        ["Destination audit", "/menu, /book-a-table, /locations, /order-online and /terms all return 404; the live ad destinations /ubq-delivery and /deals/unlockspecialdeals work."],
        ["Code mismatch", "Ad copy: 'Use code SAVE35'; image inside the same ad: 'Use Code SAVE5'."],
    ],
    scores={"Creative Variety": [7, "#F59E0B"], "UGC & Social Proof": [7, "#F59E0B"], "Copy & Hook Strength": [6, "#F59E0B"],
            "Landing Page CRO": [7, "#22C55E"], "Tracking & CAPI": [6, "#F59E0B"], "Retargeting Depth": [7, "#22C55E"]},
    findings=[
        "<b>Fifteen creatives point at your domain from accounts that are not yours:</b> 34 domain-level creatives against 19 in the United Foodbrands account. Normally that means franchise, partner or reseller buying — worth knowing who.",
        "<b>Five conventional paths return 404:</b> /menu, /book-a-table, /locations, /order-online and /terms are dead, while the ad destinations themselves work. Printed material, QR codes and old links all funnel into those dead URLs.",
        "<b>One live ad carries two different codes:</b> the copy reads 'Use code SAVE35' and the image inside the same ad reads 'Use Code SAVE5'. One of them is costing somebody a surprise at checkout.",
        "<b>Paid social is discount-led while the brand is experience-led:</b> two of the three verified creatives lead with a percentage off, and one expires on 11 October — so the creative needs replacing on a deadline rather than on data.",
        "<b>Measurement basics are in place:</b> GTM-TF3NNN, Meta's script and Razorpay are all present — the gap is that offer codes are not visibly instrumented, so an offer's effect cannot be separated from the campaign's.",
    ],
    competitors=[["Other buffet and grill chains", "Frequent discount-led advertising with coupon codes.", "Barbeque Nation's live-grill format and ambience are the differentiator; discount-led creative hands the comparison to price."],
                 ["Delivery-first brands in the same cities", "Own the takeaway occasion with a frictionless ordering flow.", "The /ubq-delivery landing page works — put the offer code consistency and the tracked redemption behind it."],
                 ["Independent BBQ restaurants", "Local store presence and word of mouth.", "Store-level ads with a direct booking path are available and not being used in the visible set."]],
    wins=[["WIN 1 - Fix the code mismatch", "Align the image and the copy on the running takeaway ad. One line, and it stops under-reporting the offer.", "#EF4444", "#FEF2F2"],
          ["WIN 2 - Redirect the five dead paths", "Menu, locations, booking, ordering and terms should each land somewhere sensible for every QR code and old link in circulation.", "#F59E0B", "#FFFBEB"],
          ["WIN 3 - Instrument the offer codes", "One event per code so offers are judged on redemptions rather than on order counts.", "#F59E0B", "#FFFBEB"]],
    impact=[["Metric", "Current (live)", "What the fix is", "Why it matters"],
            ["Offer codes", "SAVE35 in copy, SAVE5 in the image", "Align the creative", "One code, one expectation at checkout"],
            ["Conventional paths", "5 return 404", "Redirect each to the live page", "Recovers printed and typed traffic"],
            ["Domain-level creatives", "15 not in your account", "Identify the buying accounts", "Clarifies who is contesting your brand terms"]],
    sources=["Google Ads Transparency (region IN), 3 Oct 2026: 19 creatives in the UNITED FOODBRANDS LIMITED account (Verified); 34 domain-level creatives for barbequenation.com.",
             "Meta Ad Library (country IN), 3 Oct 2026: library IDs 1629049651915814 (copy and image both captured), 1595578738733856, 1727327792321770.",
             "barbequenation.com, 3 Oct 2026: GTM-TF3NNN, connect.facebook.net, Razorpay; 404s on five conventional paths; feedback@barbequenation.com and the Bengaluru 560035 registered office on the contact page."],
    outreach=[
        ["Email 1 (Day 1): 15 creatives on your domain that are not yours (and a code mismatch)",
         "Hi team,<br/><br/>I audit paid media for Bengaluru food brands. Two findings from this week's live data:<br/><br/>1. <b>34 creatives point at barbequenation.com</b>, but only 19 sit in the United Foodbrands account — the other 15 come from other accounts. Usually franchise or partner buying, but worth knowing.<br/>2. Your running takeaway ad says 'Use code SAVE35' in the copy and 'Use Code SAVE5' in the image inside the same ad.<br/><br/>The attached audit documents both, with the URLs to check them yourself." + SIGN],
        ["Email 2 (Day 3): Five URLs your printed material probably still points at",
         "Hi team,<br/><br/>Second note. /menu, /locations, /book-a-table, /order-online and /terms all return 404 today. Your ad destinations are fine — /ubq-delivery and /deals/unlockspecialdeals both work — but every QR code, menu card and old blog link that uses the conventional URLs dead-ends.<br/><br/>A set of redirects fixes it in an afternoon and costs nothing." + SIGN],
        ["Email 3 (Day 7): Your offers are not visible in your own reporting",
         "Hi team,<br/><br/>Third note, about measurement rather than creative. You have a tag manager, Meta's script and Razorpay in place — a sound stack. What I cannot see from outside is any event tied to the offer codes (SAVE35, or the pay-day offer expiring 11 October).<br/><br/>Without that, an offer can only be judged by counting orders, which cannot separate the offer's effect from the campaign's. One dataLayer push per code settles it permanently." + SIGN],
        ["Email 4 (Day 14): Closing the file on Barbeque Nation",
         "Hi team,<br/><br/>Final note. The audit's three fixes are: align the code in the takeaway ad, redirect the five dead paths, and instrument offer-code redemption.<br/><br/>We work with F&amp;B brands across Bengaluru. If a short call on any of the three is useful, I am happy to make time — and if not, the audit stands on its own." + SIGN],
    ],
)

# ----------------------------------------------------------------- MILLET AMMA
LEADS2["milletamma"] = dict(
    brand="Millet Amma", website="milletamma.com", instagram="",
    contact=dict(email="eatright@milletamma.com", phone="+91 7624979333",
                 entity="Urban Monk Private Limited",
                 address="No. 12, K 345, Yemalur Main Road, HAL Airport Area, Bellandur, Bengaluru 560037"),
    contact_source="Crawled from milletamma.com (cart and collection pages: eatright@ and the Bengaluru address; terms-of-service page: orders@) on 03 Oct 2026.",
    niche="Millets & Healthy Foods", score=8, ads_active=80,
    headline="The most active paid account in this batch: 80 live Google creatives — and a Google local ad left in the archive with its template placeholders still showing.",
    stats=[["80", "Google creatives live"], ["2", "GA4 properties loading"], ["5", "Tag families detected"], ["Bengaluru", "Bellandur HQ"]],
    ad_intro=("Millet Amma has the highest creative count in this batch: 80 live creatives under its verified entity, Urban Monk Private Limited — which is also "
              "the name on the site's own terms page, so the entity chain is clean. The account runs video and local formats as well as standard display. "
              "The measurable defects are specific: a local-ad creative still visible in Google's archive carries the template strings '{KeyWord:Millet Amma}' "
              "and '<Rating (Reviews)> · <Distance> · Bengaluru' with 'Last shown: Jul 15, 2026' and Google's 'Removed for a policy violation' notice, and the "
              "storefront loads two GA4 properties at once while a permanent 'biggest sale yet' banner does the brand's persuading for it."),
    ad_intelligence=[
        ["Google Ads (verified)", "80 creatives under URBAN MONK PRIVATE LIMITED (Verified), including video and Local Ad Rendering Service creatives."],
        ["Archived local ad (verbatim)", "Creative CR03268659855321202689: '{KeyWord:Millet Amma}', '<Rating (Reviews)> · <Distance> · Bengaluru', '<Open Hours>', 'No 12', 'Last shown: Jul 15, 2026', 'Format: Text', 'Removed for a policy violation'."],
        ["Meta (verified by ID)", "≈39 results for the brand term; brand-owned creative 1355783896518419 running since 7 Jul 2026 (Ragi Laddoo) landing milletamma.com/products/ragi-laddo-300g."],
        ["Measurement stack", "Google Tag Manager GTM-KXRPQ8B · GA4 G-WH82716CE0 · GA4 G-N659GJMWCX · Google Ads AW-378561932 · Microsoft Clarity · Shiprocket · Klaviyo."],
        ["Site-wide offer", "'Our Biggest Sale Yet: Up To 20% Off + Free Prepaid Shipping.'"],
    ],
    scores={"Creative Variety": [8, "#22C55E"], "UGC & Social Proof": [7, "#F59E0B"], "Copy & Hook Strength": [7, "#F59E0B"],
            "Landing Page CRO": [6, "#F59E0B"], "Tracking & CAPI": [5, "#EF4444"], "Retargeting Depth": [6, "#F59E0B"]},
    findings=[
        "<b>A local-ad creative in Google's public archive still shows template placeholders:</b> '{KeyWord:Millet Amma}', '<Rating (Reviews)> · <Distance> · Bengaluru', '<Open Hours>', with 'Last shown: Jul 15, 2026' and Google's 'Removed for a policy violation' notice. This is read from Google's own archive — the fix is a clean local-ad set.",
        "<b>Two GA4 properties load on the same storefront:</b> G-WH82716CE0 and G-N659GJMWCX, which double-counts sessions and splits conversion history.",
        "<b>The permanent sale banner:</b> 'Our Biggest Sale Yet: Up To 20% Off + Free Prepaid Shipping.' runs site-wide and does the work the brand story should do — a 'biggest ever' sale that never ends teaches customers to wait.",
        "<b>Four standard paths return 404:</b> /pages/faq, /pages/store-locator, /pages/bulk-enquiry and /pages/corporate-gifting — the last two are where institutional and gifting revenue would live.",
        "<b>The Meta creative is working, and it is seven months old:</b> 'A sweet that feels like home, without the refined sugar… Raagi Laddoo' has run since 7 July 2026. Good copy; likely high frequency by now.",
        "<b>The Shark Tank credential is on the storefront and not in the ads:</b> the site footer says 'Watch us on Shark Tank India'; the paid copy sampled does not.",
    ],
    competitors=[["Millet and healthy-snack D2C brands", "Discount-led feeds and heavy influencer content.", "Millet Amma's ingredient story (raagi, jaggery, ghee) and the Shark Tank credential are stronger trust assets than a discount."],
                 ["Quick-commerce millet aisles", "Instant availability.", "Own the 'why millets' story in video where the account already invests."],
                 ["Regional millet brands with retail distribution", "Shelf presence and price points.", "Direct-to-consumer subscription mechanics are available and unused."]],
    wins=[["WIN 1 - Consolidate the two GA4 properties", "One property, one redirect, one source of truth. One hour, and it ends the double-counting.", "#EF4444", "#FEF2F2"],
          ["WIN 2 - Rebuild the four missing pages", "FAQ, store locator, bulk and corporate gifting. The last two carry revenue.", "#EF4444", "#FEF2F2"],
          ["WIN 3 - Refresh the local-ad set and rotate the winning creative", "Clean the archived local ads, and put the Shark Tank line into the first line of the next Meta test while the current creative rests.", "#F59E0B", "#FFFBEB"]],
    impact=[["Metric", "Current (live)", "What the fix is", "Why it matters"],
            ["Analytics", "2 GA4 properties", "Consolidate to one", "Reports stop disagreeing"],
            ["Store pages", "4 return 404", "Publish FAQ, locator, bulk, gifting", "Recovers high-intent demand"],
            ["Creative", "One Meta creative since 7 Jul 2026", "Rotate the visual, keep the copy", "Fights fatigue without losing a winner"]],
    sources=["Google Ads Transparency (region IN), 3 Oct 2026: 80 creatives under URBAN MONK PRIVATE LIMITED (Verified); local-ad creative CR03268659855321202689 captured verbatim with 'Last shown: Jul 15, 2026' and the policy-removal notice.",
             "Meta Ad Library (country IN), 3 Oct 2026: ≈39 results; brand creative 1355783896518419 (since 7 Jul 2026) landing the Ragi Laddoo product page.",
             "milletamma.com, 3 Oct 2026: GTM-KXRPQ8B, G-WH82716CE0, G-N659GJMWCX, AW-378561932, Clarity; sale banner verbatim; four 404 paths; eatright@milletamma.com and the Bellandur address."],
    outreach=[
        ["Email 1 (Day 1): 80 live ads — and one of them left in Google's archive with placeholders showing",
         "Hi team,<br/><br/>I audit paid media for Bengaluru food brands, and your account stands out: <b>80 live Google creatives</b> under Urban Monk Private Limited, with video and local formats in the mix.<br/><br/>One thing worth fixing fast: a local-ad creative in Google's public archive still shows the template strings '{KeyWord:Millet Amma}' and '&lt;Rating (Reviews)&gt; · &lt;Distance&gt; · Bengaluru', last shown 15 July. Anyone can open it.<br/><br/>The attached audit has that URL plus every measurement behind it." + SIGN],
        ["Email 2 (Day 3): Two analytics properties are counting the same visitors",
         "Hi team,<br/><br/>Second finding, this one numerical. Your storefront loads two GA4 properties at once — G-WH82716CE0 and G-N659GJMWCX — alongside your Ads tag. Two properties means every session is counted twice and no report agrees with another.<br/><br/>Consolidating to one is an hour of work with an infrastructure-grade payoff: one number everyone can argue with." + SIGN],
        ["Email 3 (Day 7): Your best trust asset is not in your ads",
         "Hi team,<br/><br/>Third note. Your footer says 'Watch us on Shark Tank India'. Your paid creative says 'A sweet that feels like home, without the refined sugar' — which is genuinely good copy, but it is not the credential.<br/><br/>National-TV proof in the first line of a hook is a cheap test with a clear read after two weeks. Worth trying before the festive season." + SIGN],
        ["Email 4 (Day 14): Closing the file on Millet Amma",
         "Hi team,<br/><br/>Wrapping up. The audit comes down to: consolidate the two GA4 properties, rebuild four missing pages (FAQ, store locator, bulk, corporate gifting), and refresh the local-ad set.<br/><br/>If you would like help on the measurement side first — the fastest of the three — reply and I will send a step-by-step." + SIGN],
    ],
)

# ----------------------------------------------------------------- ADUKALE
LEADS2["adukale"] = dict(
    brand="Adukale", website="adukale.com", instagram="",
    contact=dict(email="info@adukale.com", phone="+91 9035462696",
                 entity="Sankethi Nutriments Private Limited",
                 address="101/4, Block 1, Kannahalli Village, Bengaluru 560091"),
    contact_source="Crawled from adukale.com (cart, home and collection pages) on 03 Oct 2026; the footer carries the Bengaluru address, the helpdesk number and info@adukale.com (with a malformed mailto alongside it).",
    niche="Ready-to-Cook & Karnataka Foods", score=7, ads_active=13,
    headline="The site now tells customers to buy on Amazon — while 13 Google creatives still land on it.",
    stats=[["13", "Google creatives live"], ["3", "Shopping ads pulled by Google"], ["2", "GA4 properties loading"], ["Bengaluru", "Kannahalli Village HQ"]],
    ad_intro=("Adukale sells Karnataka kitchen staples — sambar and chutney powders, kodubale, ready mixes — from a real Bengaluru address (Sankethi Nutriments "
              "Private Limited, Kannahalli Village), and runs 13 live Google creatives including Shopping ads. Two things make this audit unusual. First, a "
              "site-wide announcement says 'All purchases from this site will now be completed through Amazon', which means every paid click that lands on "
              "adukale.com either loses the sale or hands the customer record to Amazon. Second, three Product Listing Ads sampled in Google's archive show "
              "'Last shown: Nov 28, 2025' with Google's 'Removed for a policy violation' notice — feed-level problems that are usually fixable in Merchant "
              "Center. The storefront also shows a Shopify template placeholder — '123 John Doe Street, Your Town, YT 12345' — in its pickup block."),
    ad_intelligence=[
        ["Google Ads (verified)", "13 creatives under SANKETHI NUTRIMENTS PRIVATE LIMITED (Verified); pagination shows '1 of 26'."],
        ["Shopping feed (verbatim)", "PLAs 'Buy Sambar Powder | The Best Spice Mix | Adukale', 'Chutney Powder | 200g Pack', 'Kayi Kodubale | 180g' — 'Last shown: Nov 28, 2025', 'Removed for a policy violation' (1 of 3 variations shown)."],
        ["Meta ads", "0 active ads returned for the brand term (keyword search, country India, active-only)."],
        ["Measurement stack", "GA4 G-X6WD89C59X · GA4 G-66YCE4PEZM · Google Ads AW-812528734 · Microsoft Clarity · Shopify."],
        ["Site-wide announcement (verbatim)", "'All purchases from this site will now be completed through Amazon. Enjoy the same authentic taste with greater ease.'"],
        ["Placeholder defect (verbatim)", "'123 John Doe Street Your Town, YT 12345' in the pickup block, next to the real pickup point at 155 Madappa Building, 1st Main, Mallathalli."],
    ],
    scores={"Creative Variety": [6, "#F59E0B"], "UGC & Social Proof": [6, "#F59E0B"], "Copy & Hook Strength": [5, "#EF4444"],
            "Landing Page CRO": [4, "#EF4444"], "Tracking & CAPI": [4, "#EF4444"], "Retargeting Depth": [4, "#EF4444"]},
    findings=[
        "<b>The site hands every purchase to Amazon:</b> the announcement bar says all purchases will be completed through Amazon, while 13 Google creatives still land on adukale.com. Either the ads should point where the purchase happens, or the site should sell again — doing neither pays for traffic you cannot convert or measure.",
        "<b>Three Shopping ads are pulled with a policy notice:</b> the Samber/Chutney/Kodubale PLAs show 'Last shown: Nov 28, 2025' and 'Removed for a policy violation' — normally a feed-level issue (price, availability or landing-page mismatch) resolved in Merchant Center.",
        "<b>A template placeholder is visible on the live store:</b> '123 John Doe Street, Your Town, YT 12345' sits in the pickup block where a real customer checks where to collect their order.",
        "<b>Two GA4 properties load at once:</b> G-X6WD89C59X and G-66YCE4PEZM — double-counted sessions and split history.",
        "<b>The footer's email link is malformed:</b> 'nfo@adukale.com' appears in the mailto alongside the correct info@adukale.com.",
        "<b>Google is running, Meta is not:</b> no Meta ads and no Meta pixel observed — for a brand whose products photograph well and ship by post, that is the cheapest untested channel available, and the product feed needed to run it already exists.",
    ],
    competitors=[["Other Karnataka ready-mix and spice brands", "Similar product ranges at similar prices.", "Adukale's brand and packaging are strong; the missing pieces are a working checkout path and a second channel."],
                 ["Marketplace sellers of the same category", "Own the product search and the delivery promise.", "If Amazon is the checkout, point paid traffic there deliberately and track it; if not, rebuild the on-site path."],
                 ["D2C spice brands with meta catalogues", "Retarget browsers and sell bundles.", "The feed already exists for Shopping — the same feed powers a Meta catalogue."]],
    wins=[["WIN 1 - Decide where the paid click ends", "If Amazon is the checkout, send the ads there and track it. If the site is selling, change the message and make the cart the destination.", "#EF4444", "#FEF2F2"],
          ["WIN 2 - Clean the storefront's public defects", "Delete the placeholder pickup address and fix the mailto. Both are five-minute edits visible to customers today.", "#EF4444", "#FEF2F2"],
          ["WIN 3 - Fix the feed and open Meta", "Resolve the Merchant Center policy issues on the pulled PLAs, then connect the same feed to a Meta catalogue with a pixel.", "#F59E0B", "#FFFBEB"]],
    impact=[["Metric", "Current (live)", "What the fix is", "Why it matters"],
            ["Purchase path", "Site routes buyers to Amazon", "Decide and align the ad destination", "Paid clicks stop landing on a dead end"],
            ["Shopping ads", "3 PLAs pulled for policy", "Merchant Center feed fix", "Products return to Shopping"],
            ["Storefront trust", "Placeholder address and broken mailto", "Theme edits", "Removes two visible defects"]],
    sources=["Google Ads Transparency (region IN), 3 Oct 2026: 13 creatives under SANKETHI NUTRIMENTS PRIVATE LIMITED (Verified); three PLAs captured verbatim with 'Last shown: Nov 28, 2025' and the policy-removal notice.",
             "Meta Ad Library (country IN), 3 Oct 2026: no ads match the brand term.",
             "adukale.com, 3 Oct 2026: Amazon announcement bar verbatim; '123 John Doe Street' pickup placeholder; 'nfo@adukale.com' mailto; G-X6WD89C59X, G-66YCE4PEZM, AW-812528734; Bengaluru 560091 address and helpdesk number."],
    outreach=[
        ["Email 1 (Day 1): Your ads still land on a site that sends buyers to Amazon",
         "Hi team,<br/><br/>I audit paid media for Bengaluru food brands. Your storefront now says: 'All purchases from this site will now be completed through Amazon.' At the same time, <b>13 Google creatives</b> are live for adukale.com.<br/><br/>That combination has an obvious cost: paid clicks that either lose the sale or hand your customer record to Amazon. The attached audit lays out the two clean ways to resolve it.<br/><br/>Everything in it is dated and sourced." + SIGN],
        ["Email 2 (Day 3): Three Shopping ads are pulled — and that is usually fixable in a day",
         "Hi team,<br/><br/>Second finding. One of your archived Shopping ads shows 'Last shown: Nov 28, 2025', with all three of its variations carrying Google's notice 'Removed for a policy violation': Sambar Powder, Chutney Powder 200g and Kayi Kodubale 180g.<br/><br/>PLA removals are usually feed-level — price, availability or a landing-page mismatch — and are resolved in Merchant Center. Worth knowing, because Shopping is the visible engine in your account." + SIGN],
        ["Email 3 (Day 7): Two visible defects on the live storefront",
         "Hi team,<br/><br/>Third note, and these are two five-minute fixes on live pages. Your pickup block still shows the Shopify template address: '123 John Doe Street, Your Town, YT 12345', next to your real pickup point at Mallathalli.<br/><br/>And the email icon in your footer is coded without a mailto: prefix (verbatim: &lt;a href=\"info@adukale.com\"&gt;), so a click cannot open a mail client. The address reads correctly, which is why nobody has noticed." + SIGN],
        ["Email 4 (Day 14): Closing the file on Adukale",
         "Hi team,<br/><br/>Last note. The audit boils down to one decision — where the paid click should end while Amazon is the checkout — plus three small fixes (placeholder address, mailto, Merchant Center feed).<br/><br/>If a 20-minute call on the routing question would help, I am happy to make time. Otherwise the audit is yours to use internally." + SIGN],
    ],
)

# ----------------------------------------------------------------- ORGANIC MANDYA
LEADS2["organicmandya"] = dict(
    brand="Organic Mandya", website="organicmandya.com", instagram="",
    contact=dict(email="support@organicmandya.com", phone="+91 95909 22000",
                 entity="Mandya Organic Foods Private Limited",
                 address="Mandya, Karnataka (2-hour delivery in Bengaluru, Hyderabad & Mysuru)"),
    contact_source="Crawled from organicmandya.com (cart and collection pages) on 03 Oct 2026; the phone number and the 2-hour Bengaluru delivery promise are published in the site's announcement bar.",
    niche="Organic Grocery & Farm Produce", score=8, ads_active=67,
    headline="A two-hour delivery promise that never appears in the ads, and a Google account 35× the size of its Meta presence.",
    stats=[["67", "Creatives point at the domain"], ["69", "In the advertiser account"], ["~2", "Meta active results"], ["2-hr", "Bengaluru delivery promise"]],
    ad_intro=("Organic Mandya sells organic staples direct from Karnataka farmers and runs 69 creatives in its verified advertiser account, with 67 pointing "
              "at organicmandya.com. Its most valuable asset is not in the ads at all: the site promises two-hour delivery in Bengaluru, Hyderabad and Mysuru "
              "(₹49 under ₹500, free above) and three-to-five day delivery nationally. That is a scare asset in the organic category, and the Google creative "
              "sampled leads with product instead — 'organic rajmudi rice (rajamudi) — karnataka's heritage red rice'. The measurement side has clearly been "
              "built with care: a GTM container pushing custom events (gtm-promo, gtm-creative, gtm-position). On Meta, the brand has about two live results "
              "against Google's 69 — a ratio, not a strategy."),
    ad_intelligence=[
        ["Google Ads (verified)", "69 creatives in the MANDYA ORGANIC FOODS PRIVATE LIMITED account (Verified); 67 creatives point at organicmandya.com; pagination shows '18 of 80'."],
        ["Ad copy sampled (verbatim)", "'organic rajmudi rice (rajamudi) - karnataka's heritage red rice' — display URL www.organicmandya.com."],
        ["Meta (verified by ID)", "≈2 active results for the brand term; brand-owned creative 1432155482101394 running since 13 Sep 2026 landing the millet-upma collection page."],
        ["Measurement stack", "Google Tag Manager GTM-5CDCGR4B · GA4 G-MHKC4DNNH3 · Google Ads AW-16535163896 · custom dataLayer events gtm-meta, gtm-promo, gtm-creative, gtm-position, gtm-destination · Microsoft Clarity · Shiprocket."],
        ["Delivery promise (verbatim)", "'2-hr delivery in Bengaluru, Hyderabad & Mysuru — ₹49 delivery charge on orders under ₹500, FREE above ₹500'; all-India 3–5 days, ₹149 under ₹2000, free above."],
    ],
    scores={"Creative Variety": [7, "#F59E0B"], "UGC & Social Proof": [6, "#F59E0B"], "Copy & Hook Strength": [7, "#F59E0B"],
            "Landing Page CRO": [6, "#F59E0B"], "Tracking & CAPI": [6, "#F59E0B"], "Retargeting Depth": [5, "#EF4444"]},
    findings=[
        "<b>The two-hour promise is missing from the ads:</b> Bengaluru/Hyderabad/Mysuru same-day-speed delivery is the strongest claim the brand owns, and the paid creative sampled sells rice instead. One hook test against the current product-led creative answers it.",
        "<b>Google is doing all the work:</b> 69 creatives in the account against roughly two Meta results. The one Meta creative that exists points at a category collection rather than a single product — the right instinct, never scaled.",
        "<b>The dataLayer is built and not yet mapped:</b> custom events (gtm-promo, gtm-creative, gtm-destination) exist in the page; importing them as GA4 key events and Ads conversions is configuration, not development.",
        "<b>Three standard paths return 404:</b> /pages/faq, /pages/bulk-enquiry and /pages/corporate-gifting — the bulk and corporate order types are exactly where five-figure orders come from.",
        "<b>The platform's own two counts differ slightly:</b> 69 creatives in the advertiser account against 67 at domain level. Worth knowing before either number is quoted in a board deck.",
    ],
    competitors=[["Organic D2C brands with national reach", "Large paid footprints and subscription models.", "Two-hour delivery in three cities is a promise most of them cannot make — lead with it."],
                 ["Quick-commerce grocery", "Win on speed for a narrow basket.", "Compete on provenance and price-per-kilo, not on the ten-minute race."],
                 ["Local organic stores", "Physical trust and immediate availability.", "The delivery promise plus the farmer story is the digital equivalent of that trust."]],
    wins=[["WIN 1 - Put the two-hour promise into the ad copy", "One hook test against the current product-led creative. Nothing new needs to be true — it is already published on your site.", "#EF4444", "#FEF2F2"],
          ["WIN 2 - Map the dataLayer to conversions", "gtm-promo, gtm-creative and gtm-destination already fire. Importing them is an hour of configuration.", "#F59E0B", "#FFFBEB"],
          ["WIN 3 - Build the corporate-gifting page and scale Meta collections", "One page for the highest-value order type, plus collection-level Meta ads using the catalogue you already have.", "#F59E0B", "#FFFBEB"]],
    impact=[["Metric", "Current (live)", "What the fix is", "Why it matters"],
            ["Ad hooks", "Product-led copy", "Test the two-hour promise", "Uses a claim competitors cannot match"],
            ["Measurement", "Custom events not mapped", "Import as key events/conversions", "Campaign decisions gain a signal"],
            ["Channel mix", "69 Google creatives vs ~2 Meta results", "Scale collection ads", "Second channel, existing catalogue"]],
    sources=["Google Ads Transparency (region IN), 3 Oct 2026: 69 creatives under MANDYA ORGANIC FOODS PRIVATE LIMITED (Verified); 67 at domain level; ad text captured verbatim.",
             "Meta Ad Library (country IN), 3 Oct 2026: ≈2 active results; brand creative 1432155482101394 (since 13 Sep 2026) landing the millet-upma collection.",
             "organicmandya.com, 3 Oct 2026: GTM-5CDCGR4B, G-MHKC4DNNH3, AW-16535163896, dataLayer events, Clarity; delivery promise verbatim; three 404 paths; support@organicmandya.com."],
    outreach=[
        ["Email 1 (Day 1): You have the best delivery promise in the category — and none of your ads say it",
         "Hi team,<br/><br/>I audit paid media for Bengaluru food brands. Your site promises <b>2-hour delivery in Bengaluru, Hyderabad and Mysuru</b> (₹49 under ₹500, free above). Your live Google creative — I captured 'organic rajmudi rice (rajamudi) — karnataka's heritage red rice' — sells the product instead.<br/><br/>You own a claim most organic brands cannot make. The attached audit shows where it is missing and what to test first." + SIGN],
        ["Email 2 (Day 3): 69 Google creatives, and roughly two Meta results",
         "Hi team,<br/><br/>Second finding. Your Google account holds 69 creatives. On Meta, the brand term returns about two active results — one of them yours, pointing at a category collection.<br/><br/>Collection-level ads against a visual grocery catalogue is exactly the right structure for a basket business. Two ads is a test that was never scaled; the attached audit describes the first three campaigns I would run." + SIGN],
        ["Email 3 (Day 7): Your custom dataLayer is doing nothing yet",
         "Hi team,<br/><br/>Third note, and it is a compliment with a gap attached. Your storefront pushes custom events called gtm-promo, gtm-creative, gtm-position and gtm-destination. Someone built a real measurement plan.<br/><br/>None of it changes your reports until those events are mapped to GA4 key events and imported into Google Ads. That is configuration, not development — and it is the difference between guessing and knowing which collection earns its spend." + SIGN],
        ["Email 4 (Day 14): Closing the file on Organic Mandya",
         "Hi team,<br/><br/>Wrapping up. Three moves: put the two-hour promise into the ad copy, map the dataLayer events into conversions, and give corporate gifting a page.<br/><br/>If the corporate-gifting idea interests you, I can share the page structure we use — it is the fastest of the three to prove out." + SIGN],
    ],
)

# ----------------------------------------------------------------- PURE & SURE
LEADS2["pureandsure"] = dict(
    brand="Pure & Sure", website="pureandsure.in", instagram="",
    contact=dict(email="info@pureandsure.in", phone="1800 121 0369",
                 entity="Phalada Organic Consumer Products Private Limited",
                 address="92/5, Kannalli Village, Seegehalli, Magadi Main Road, Bangalore 560091"),
    contact_source="Crawled from pureandsure.in (contact and shipping-policy pages: info@; cart and collection pages: care@ and the Bengaluru address) on 03 Oct 2026.",
    niche="Organic FMCG & Grocery", score=7, ads_active=37,
    headline="Every Shopping click is being filed as organic traffic — a five-minute feed setting that quietly invalidates channel reporting.",
    stats=[["37", "Google creatives live"], ["4", "Measurement tags detected"], ["1", "Feed tagging bug"], ["Bengaluru", "Magadi Main Road HQ"]],
    ad_intro=("Pure & Sure (Phalada Organic) is one of the older organic FMCG operations in Karnataka: 37 live creatives under its verified entity, a full tag "
              "stack (GTM, GA4, Ads, Meta pixel and Judge.me), free shipping over ₹500 and a catalogue led by a new product launch — Low GI Sonamasuri rice. "
              "The findings are precise rather than dramatic. The Shopping feed is tagging every paid click with 'sag_organic' in the campaign field, which files "
              "paid traffic as organic in analytics. Two conventional page handles return 404 — the classic symptom of a theme rebuild without redirects. And the "
              "brand publishes two support addresses on different pages, which is fine only if somebody owns both."),
    ad_intelligence=[
        ["Google Ads (verified)", "37 creatives under Phalada Organic Consumer Products Private Limited (Verified); pagination shows '4 of 74'."],
        ["Feed tagging (verbatim)", "Landing URL from the Organic Ghee ad: …pureandsure.in/products/organic-desi-ghee-500ml?…&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic"],
        ["Measurement stack", "GA4 G-VGC836EHVF · Google Tag Manager GTM-KP8NPFKZ · Google Ads AW-16785598661 · Meta pixel 903483430574351 · Judge.me."],
        ["Destination audit", "/pages/contact-us, /pages/about-us, /pages/store-locator, /pages/bulk-enquiry and /pages/corporate-gifting return 404; /pages/contact works."],
        ["Site offers and range", "'Introducing Low GI Sonamasuri Rice — Buy Now' · '100% Organic Foods Delivered Directly' · 'Free Shipping on orders above ₹500'."],
    ],
    scores={"Creative Variety": [6, "#F59E0B"], "UGC & Social Proof": [6, "#F59E0B"], "Copy & Hook Strength": [6, "#F59E0B"],
            "Landing Page CRO": [6, "#F59E0B"], "Tracking & CAPI": [6, "#F59E0B"], "Retargeting Depth": [5, "#EF4444"]},
    findings=[
        "<b>Every Shopping click is filed under 'sag_organic':</b> the feed's tracking template writes sag_organic into the campaign field, so paid Shopping traffic is reported as organic in GA4 — until this changes, any channel comparison built on those reports is wrong.",
        "<b>Five conventional paths return 404:</b> /pages/contact-us, /pages/about-us, /pages/store-locator, /pages/bulk-enquiry and /pages/corporate-gifting — the signature of a theme rebuild without redirects, and an easy way to lose traffic from third-party links.",
        "<b>Two published support addresses:</b> info@ on the contact and shipping pages, care@ on the cart and collection pages. Fine if both reach the same inbox; a customer-experience risk if not.",
        "<b>Meta is unreadable from outside:</b> the brand term returns tens of thousands of unrelated results, so no brand-specific Meta count could be taken. The audit records this as not measured rather than guessing.",
        "<b>The tag stack is complete and healthy:</b> GTM, GA4, Ads, Meta pixel and Judge.me are all present — the fix list here is configuration, not infrastructure.",
    ],
    competitors=[["Organic pantry brands with national retail", "Shelf presence and price-led promotions.", "Pure & Sure's farm-to-brand story and the Low GI launch give it something specific to own."],
                 ["Quick-commerce organic aisles", "Instant availability for small baskets.", "Compete on range depth and price-per-kilo, and make the ₹500 free-shipping threshold do the basket-building."],
                 ["Regional Karnataka organic brands", "Local trust and distribution.", "Own the traceability story — Phalada's own 'Journey of Organic Food' content already exists."]],
    wins=[["WIN 1 - Turn off the sag_organic campaign tag", "Minutes of work in the feed settings; it is currently mislabelling paid clicks as organic traffic.", "#EF4444", "#FEF2F2"],
          ["WIN 2 - Redirect the dead handles", "contact-us, about-us, store-locator, bulk and corporate-gifting should each land on the working page.", "#F59E0B", "#FFFBEB"],
          ["WIN 3 - Get a clean Meta read and decide the channel question", "Pull 90 days from the account and compare it with the Google numbers you can already see, then decide Meta's share.", "#F59E0B", "#FFFBEB"]],
    impact=[["Metric", "Current (live)", "What the fix is", "Why it matters"],
            ["Channel reporting", "Paid Shopping tagged sag_organic", "Correct the feed tracking template", "Paid and organic stop being confused"],
            ["Destination paths", "5 return 404", "Redirect to equivalent live pages", "Third-party and printed links keep working"],
            ["Support", "2 addresses published", "Alias one to the other", "Customers reach a human either way"]],
    sources=["Google Ads Transparency (region IN), 3 Oct 2026: 37 creatives under Phalada Organic Consumer Products Private Limited (Verified); the Organic Ghee landing URL captured verbatim with sag_organic tagging.",
             "pureandsure.in, 3 Oct 2026: G-VGC836EHVF, GTM-KP8NPFKZ, AW-16785598661, Meta pixel 903483430574351; free-shipping banner; five 404 paths; info@, care@ and the Bengaluru 560091 address.",
             "Meta Ad Library (country IN), 3 Oct 2026: brand term returns unrelated inventory — recorded as not measured, not as zero."],
    outreach=[
        ["Email 1 (Day 1): Your Shopping clicks are being reported as organic traffic",
         "Hi team,<br/><br/>I audit paid media for Bengaluru food brands. One finding from your live data that is worth fixing this week: your Shopping feed's tracking template writes <b>utm_campaign=sag_organic</b> into every paid click — I captured it on your Organic Ghee landing URL.<br/><br/>In GA4 that traffic is filed as organic, so your paid Shopping investment currently looks like free traffic. The attached audit shows the exact URL and the fix." + SIGN],
        ["Email 2 (Day 3): The 404s that follow a theme rebuild",
         "Hi team,<br/><br/>Second finding. Five conventional paths return 404 today: /pages/contact-us, /pages/about-us, /pages/store-locator, /pages/bulk-enquiry and /pages/corporate-gifting — while /pages/contact works.<br/><br/>That pattern is normal after a rebuild and invisible until a partner, a press link or a customer types the obvious URL. Redirects are an afternoon and permanent." + SIGN],
        ["Email 3 (Day 7): Two support addresses, one question",
         "Hi team,<br/><br/>Third note, quick. Your contact and shipping pages publish info@pureandsure.in; your cart and collection pages publish care@pureandsure.in.<br/><br/>That is fine if both forward into one inbox — less fine if a customer writes to the wrong one and waits. Worth a two-minute check inside the team." + SIGN],
        ["Email 4 (Day 14): Closing the file on Pure &amp; Sure",
         "Hi team,<br/><br/>Wrapping up. Three moves: fix the sag_organic tag, redirect the five dead handles, and get a clean read on Meta so the channel question can be answered with numbers.<br/><br/>If a short call on the reporting fix would be useful, I am happy to walk your team through the five-minute change." + SIGN],
    ],
)

# ----------------------------------------------------------------- EAT BETTER CO
LEADS2["eatbetterco"] = dict(
    brand="Eat Better Co", website="eatbetterco.com", instagram="",
    contact=dict(email="care@eatbetterco.com", phone="+91 9829188706",
                 entity="Eat Better Ventures Private Limited",
                 address="A1/A2, Vastushree Colony, 100 Feet Road, Manyawas, Mansarovar, Jaipur, Rajasthan 302020"),
    contact_source="Crawled from eatbetterco.com (contact-us and refund-policy pages: care@ and the registered address; privacy and shipping pages: connect@) on 03 Oct 2026.",
    niche="Healthy Snacks & Corporate Gifting", score=7, ads_active=29,
    headline="Shopping ads advertising discounts of 1%, 2% and 6% — and a support address on a different domain.",
    stats=[["29", "Google creatives live"], ["-1%", "Smallest discount in feed"], ["10 lakh+", "Hampers (brand's figure)"], ["6", "Findings in this report"]],
    ad_intro=("Eat Better Co (Eat Better Ventures Private Limited) sells healthy snacks and Diwali hampers from Jaipur, and its paid engine is feed-led: 27 "
              "creatives in the account, 29 pointing at eatbetterco.com, dominated by Product Listing Ads. The most quotable finding is in those listings — "
              "titles carrying discount badges of −1%, −2% and −6%, which read as a discount and deliver a rounding error. The site is doing more things right "
              "than wrong: a corporate-gifting page that publishes 10 lakh+ hampers delivered pan-India for 500+ organisations, a Meta pixel configured inside "
              "its enquiry form with a Lead event on submit, and a Shark Tank credential in the title tag. The gaps are consistency: two support addresses on "
              "two different domains, five dead conventional paths, and a cash-on-delivery fee the ads never mention."),
    ad_intelligence=[
        ["Google Ads (verified)", "27 creatives in the EAT BETTER VENTURES PRIVATE LIMITED account (Verified); 29 creatives at domain level; pagination shows '3 of 54'."],
        ["Feed detail (verbatim)", "PLA badges '[-1%]' (quinoa chilli lime namkeen), '[-6%]' (better trail mix 100g), '[-2%]' (sweet crunchy nut mix 100g), '[-2%]' (ragi chips bundle); landing URLs carry utm_campaign=sag_organic."],
        ["Measurement stack", "GA4 G-90QE4TSKTH · Google Ads AW-610414449 · Shopify · Judge.me · Meta pixel 3182482251838473 configured inside an embedded form with fbq('trackCustom','Lead') on submit."],
        ["Published shipping terms", "Free above ₹500 · prepaid shipping ₹49 · cash-on-delivery ₹79 · 'Most orders are delivered within 3 working days'."],
        ["Corporate gifting (brand's figures)", "'10 LAKH+ hampers delivered pan-India · 500+ corporates & organizations · 25 hamper designs this Diwali', hampers from ₹249 to ₹2,499."],
    ],
    scores={"Creative Variety": [7, "#F59E0B"], "UGC & Social Proof": [6, "#F59E0B"], "Copy & Hook Strength": [6, "#F59E0B"],
            "Landing Page CRO": [7, "#22C55E"], "Tracking & CAPI": [5, "#EF4444"], "Retargeting Depth": [5, "#EF4444"]},
    findings=[
        "<b>The feed advertises discounts of 1%, 2% and 6%:</b> a '[-1%]' badge reads as an offer and delivers a rounding error, training shoppers to scroll past the listing. Either remove the discount display at that level or reprice so the badge means something.",
        "<b>Two support addresses on two domains:</b> care@eatbetterco.com on the contact and refund pages, connect@gottaeatbetter.com on the privacy and shipping pages — a customer following your own policy pages writes to a domain they have never heard of.",
        "<b>The feed's tracking template writes sag_organic into the campaign field:</b> the same pattern found on other accounts in this batch — paid Shopping clicks are filed as organic traffic in GA4.",
        "<b>Five conventional paths return 404:</b> /pages/contact, /pages/faq, /pages/about-us, /pages/store-locator, /pages/bulk-enquiry — while /pages/contact-us and /pages/corporate-gifting work.",
        "<b>Cash on delivery costs ₹30 more, and the ads never say so:</b> free above ₹500, prepaid ₹49, COD ₹79 — the fee is a sensible nudge only if the buyer sees it before choosing.",
        "<b>The Shark Tank credential sits in the browser tab:</b> the site title reads 'Eat Better Co - As seen on Shark Tank'; the paid creative sampled does not mention it, and it is the strongest short trust signal the brand has.",
    ],
    competitors=[["Wellness snack brands with heavy Meta presence", "Influencer-led creative and brand-building spend.", "The Shark Tank credential plus the hampers' corporate proof is a differentiated story that is currently only on the site."],
                 ["Millet and 'no-palm-oil' snack challengers", "Ingredient-led positioning and aggressive discounting.", "Do not match the discount; match the ingredient claim and the corporate track record of 10 lakh+ hampers."],
                 ["Gifting aggregators in the Diwali quarter", "Own the corporate gifting search with quote forms.", "Eat Better's own gifting page is strong — it needs the enquiry event tracked and the domain story cleaned up."]],
    wins=[["WIN 1 - Clean the sub-10% discounts out of the feed", "Remove the badge or reprice. A 1% badge is worse than no badge.", "#EF4444", "#FEF2F2"],
          ["WIN 2 - One support address on every page", "Align the policy pages to care@eatbetterco.com and forward the other address into the same inbox.", "#F59E0B", "#FFFBEB"],
          ["WIN 3 - Put the credential and the threshold into the copy", "Shark Tank proof and 'free shipping over ₹500' in the ad copy: trust and basket size in one test.", "#F59E0B", "#FFFBEB"]],
    impact=[["Metric", "Current (live)", "What the fix is", "Why it matters"],
            ["Feed badges", "[-1%], [-2%], [-6%]", "Remove or reprice", "Listings stop advertising rounding errors"],
            ["Support", "2 domains in one funnel", "One address, one alias", "Customers reach the brand, not a stranger"],
            ["Ad copy", "Product-led only", "Add credential and free-shipping threshold", "Trust and average order value in one change"]],
    sources=["Google Ads Transparency (region IN), 3 Oct 2026: 27 creatives in the EAT BETTER VENTURES PRIVATE LIMITED account (Verified); 29 at domain level; PLA badges and landing URLs captured verbatim.",
             "eatbetterco.com, 3 Oct 2026: G-90QE4TSKTH, AW-610414449, Judge.me; Meta pixel 3182482251838473 and fbq Lead event inside the embedded form; shipping terms verbatim; five 404 paths; corporate-gifting page figures verbatim; Jaipur registered address and care@/connect@ addresses."],
    outreach=[
        ["Email 1 (Day 1): Your Shopping feed is advertising 1% off",
         "Hi team,<br/><br/>I audit paid media for food brands. Running through your live Shopping ads this week, three stood out: four of them carry discount badges: <b>[-1%]</b> on quinoa namkeen, <b>[-2%]</b> on the sweet crunchy nut mix and again on a ragi bundle, and <b>[-6%]</b> on trail mix 100g.<br/><br/>A 1% badge reads as an offer and delivers a rounding error. Either removing the badge or repricing fixes it, and both are feed-level decisions made once.<br/><br/>The attached audit shows the listings and everything else I measured." + SIGN],
        ["Email 2 (Day 3): Your policy pages send customers to a different domain",
         "Hi team,<br/><br/>Second finding. Your contact and refund pages publish care@eatbetterco.com; your privacy and shipping pages publish connect@gottaeatbetter.com.<br/><br/>A customer who reads your shipping policy and then writes to that address has been sent to a domain they have never seen. One canonical address with the other as a forwarding alias solves it in minutes." + SIGN],
        ["Email 3 (Day 7): You have a Meta Lead event — inside one form",
         "Hi team,<br/><br/>Third note, and it is a good sign with a caveat. Your enquiry form is configured with a Meta pixel (3182482251838473) and fires a custom Lead event on submit, then sends people to your Diwali hampers collection.<br/><br/>That works — but a Lead event that fires from one form only is a single point of failure, and it means the pixel cannot see any other page. The attached audit explains the two ways to extend it." + SIGN],
        ["Email 4 (Day 14): Closing the file on Eat Better Co",
         "Hi team,<br/><br/>Last note from me. The audit's three moves: clean the sub-10% discounts out of the feed, put one support address across the site, and test the Shark Tank line plus the ₹500 free-shipping threshold in the ad copy.<br/><br/>No reply needed if the timing is wrong — the audit is yours either way." + SIGN],
    ],
)

# ----------------------------------------------------------------- BRIK OVEN
LEADS2["brikoven"] = dict(
    brand="Brik Oven", website="brikoven.com", instagram="",
    contact=dict(email="theteam@brikoven.com", phone="",
                 entity="Brik Oven Pvt Ltd", address="Four Bengaluru outlets: Church Street, Indiranagar, Palace Road, Koramangala"),
    contact_source="Crawled from brikoven.com (contact block and the outlets block on the home page) on 03 Oct 2026; each outlet's address and phone number are published on the home page.",
    niche="Pizzerias & Casual Dining", score=7, ads_active=25,
    headline="Well-run local store ads for four Bengaluru outlets — with the last click handed to a third-party reservation widget.",
    stats=[["42", "Creatives in Google account"], ["25", "Pointing at brikoven.com"], ["17", "Creatives off-domain"], ["4", "Bengaluru outlets"]],
    ad_intro=("Brik Oven runs the most disciplined restaurant advertising in this batch: 42 creatives in the advertiser account, 25 pointed at brikoven.com, "
              "with store-level Local Ad Rendering Service creatives for its Bengaluru outlets — Manyata Business Park and Palace Road verified in the archive, "
              "each with directions, call, reserve and order actions. The tag base is sound (GTM-PMCQMP4, GA4 G-6HE7Y2G8N3, plus a Meta pixel). Two leaks matter. "
              "The reservation click leaves the domain for a third-party widget (widget.reservego.co), so the booking data and the store-level attribution sit "
              "with someone else. And nine conventional paths — including /contact-us, /menu, /book-a-table and /locations — return 404 on a Squarespace store "
              "whose paid traffic is dominated by 'pizza near me' intent."),
    ad_intelligence=[
        ["Google Ads (verified)", "42 creatives under Brik Oven Pvt Ltd (Verified); 25 creatives point at brikoven.com."],
        ["Local ads (verbatim)", "'Brik Oven - Woodfired Pizzas (Manyata Business Park)' → 'Wood-Fired Pizza Near You — Discover Neapolitan sourdough pizzas…' with CTA 'Book now • widget.reservego.co/'."],
        ["Archived creative (verbatim)", "Creative CR16763555951004352513: 'Last shown: Jul 23, 2026', 'Format: Text', 'Smoked Ham Bagel Mornings — Sourdough sandwiches, bagels & toasties. Open 8AM-11AM daily at Brik Oven.' (Palace Road); a second local ad carries 'Sourdough Breakfast at Brik … Prestige Trade Tower'."],
        ["Measurement stack", "Google Tag Manager GTM-PMCQMP4 · GA4 G-6HE7Y2G8N3 · Meta pixel 428743468014315 · Squarespace."],
        ["Destination audit", "/contact-us, /about-us, /faq, /menu, /book-a-table, /locations, /order-online, /privacy-policy and /terms all return 404."],
    ],
    scores={"Creative Variety": [7, "#F59E0B"], "UGC & Social Proof": [8, "#22C55E"], "Copy & Hook Strength": [7, "#F59E0B"],
            "Landing Page CRO": [4, "#EF4444"], "Tracking & CAPI": [6, "#F59E0B"], "Retargeting Depth": [5, "#EF4444"]},
    findings=[
        "<b>The reservation click leaves your domain:</b> the Manyata Business Park local ad offers 'Book now • widget.reservego.co/'. Every booking made there is a customer relationship held by someone else — booking data, no-show remarketing and store-level attribution included.",
        "<b>Nine conventional paths return 404:</b> /contact-us, /about-us, /faq, /menu, /book-a-table, /locations, /order-online, /privacy-policy and /terms — on a business whose search demand is overwhelmingly 'pizza near me' and store names.",
        "<b>Seventeen creatives in the account point off-domain:</b> 42 creatives against 25 pointing at brikoven.com, consistent with store-level and third-party destinations — the account's centre of gravity is not the website, so website analytics can only ever see part of what paid media does.",
        "<b>A store creative stopped serving in July:</b> the Palace Road breakfast creative shows 'Last shown: Jul 23, 2026' while the stores keep trading — a monthly review of live local ads keeps the set current.",
        "<b>The tag base is sound and the brand voice is strong:</b> GTM, GA4 and a Meta pixel are in place, and the ad copy ('Egg salad bagels, ham melts, fig toasties. Breakfast all day, no lines.') is specific, confident and store-level — better than most restaurant groups manage.",
    ],
    competitors=[["Other Bengaluru pizza and casual-dining groups", "Heavier brand-level spend and delivery-app visibility.", "Brik Oven's store-level ad set is more precise; it needs an owned booking path to convert that precision into data."],
                 ["Delivery aggregators", "Own the 'order online' moment.", "There is no direct ordering path on the site today — one is the difference between a customer and a transaction."],
                 ["Neighbourhood sourdough and bakery cafés", "Local proximity and morning trade.", "The breakfast daypart is already advertised; keep those creatives current and give them a landing page."]],
    wins=[["WIN 1 - Redirect the nine dead paths", "Contact, menu, reservations, locations and ordering should each land on the section that exists. One afternoon.", "#EF4444", "#FEF2F2"],
          ["WIN 2 - Own the reservation path", "A booking form on brikoven.com keeps bookings, no-shows and store-level attribution with you instead of the widget.", "#EF4444", "#FEF2F2"],
          ["WIN 3 - Review the live local-ad set monthly", "Check which store creatives are still serving — the Palace Road breakfast ad stopped in July while the store kept trading.", "#F59E0B", "#FFFBEB"]],
    impact=[["Metric", "Current (live)", "What the fix is", "Why it matters"],
            ["Reservations", "Third-party widget", "On-site booking form", "You keep the booking data and can remarket"],
            ["Conventional paths", "9 return 404", "Redirect to live sections", "Captures 'near me' and old-link traffic"],
            ["Local ads", "One store creative stopped in July", "Monthly live-ad review", "The archive stays current"]],
    sources=["Google Ads Transparency (region IN), 3 Oct 2026: 42 creatives under Brik Oven Pvt Ltd (Verified); 25 pointed at brikoven.com; the Manyata Business Park local ad and creative CR16763555951004352513 captured verbatim.",
             "brikoven.com, 3 Oct 2026: GTM-PMCQMP4, G-6HE7Y2G8N3, Meta pixel 428743468014315, Squarespace; nine 404 paths; four Bengaluru outlets with addresses and phones; theteam@brikoven.com."],
    outreach=[
        ["Email 1 (Day 1): Your store ads are excellent — and the booking click leaves your domain",
         "Hi team,<br/><br/>I audit paid media for Bengaluru food brands. Your local ads are the best-constructed set I have seen this month: store-level creatives for Manyata Business Park and Palace Road with directions, call and reserve actions.<br/><br/>One structural problem: the reservation CTA goes to widget.reservego.co — so the booking data, the no-show list and the store-level attribution belong to the widget, not to you. The attached audit explains what moving it back would give you." + SIGN],
        ["Email 2 (Day 3): Nine URLs your customers type, all returning 404",
         "Hi team,<br/><br/>Second finding. /contact-us, /menu, /book-a-table, /locations and /order-online all return 404 today (along with about-us, faq, privacy-policy and terms).<br/><br/>Your paid traffic is driven by store-level intent — people looking for pizza near a specific outlet. Those are exactly the visitors most likely to book, and today the obvious URLs dead-end. Redirects are an afternoon's work." + SIGN],
        ["Email 3 (Day 7): The Palace Road breakfast ad stopped in July",
         "Hi team,<br/><br/>Third note. Google's archive shows your Palace Road breakfast creative — 'Smoked Ham Bagel Mornings — Sourdough sandwiches, bagels &amp; toasties. Open 8AM-11AM daily' — with 'Last shown: Jul 23, 2026'.<br/><br/>The creative is good; it just is not running while the stores are. A monthly five-minute review of which store ads are live keeps the set earning." + SIGN],
        ["Email 4 (Day 14): Closing the file on Brik Oven",
         "Hi team,<br/><br/>Wrapping up. Two moves matter most here: put a booking form on your own domain, and redirect the nine dead paths. After that, a monthly review keeps the local-ad set current.<br/><br/>If a short call on the booking flow would be useful, I can bring the structure we use for restaurant groups." + SIGN],
    ],
)

# ----------------------------------------------------------------- ARAKU COFFEE
LEADS2["arakucoffee"] = dict(
    brand="Araku Coffee", website="arakucoffee.in", instagram="",
    contact=dict(email="customercare@arakuoriginals.com", phone="+91 9000394000",
                 entity="Araku Originals Pvt Ltd", address="Flagships in Mumbai, Bangalore & Paris (per the brand's own site copy)"),
    contact_source="Crawled from arakucoffee.in (the site footer on the home page) on 03 Oct 2026; the footer carries the brand's telephone number and customercare@arakuoriginals.com.",
    niche="Specialty Coffee", score=7, ads_active=200,
    headline="Around 200 live creatives — and every Shopping click filed as organic traffic.",
    stats=[["~200", "Google creatives live"], ["4", "Measurement tags detected"], ["sag_organic", "Campaign tag on paid clicks"], ["Bangalore", "Flagship & training campus"]],
    ad_intro=("Araku Coffee is the largest advertiser in this batch by creative volume: approximately 200 live creatives under Araku Originals Pvt Ltd (verified), "
              "spanning Shopping, Local and video formats. The account runs a Moka Pot and a Chemex Coffee Maker as Product Listing Ads alongside store "
              "listings with directions and reserve actions — a blend of e-commerce and café marketing in one advertiser. The measurement base is in place "
              "(GA4, Google Ads, Clarity, Razorpay). The defect is a feed setting: every Shopping click is tagged utm_campaign=sag_organic, so paid traffic is "
              "filed as organic traffic in analytics, and at this creative volume that is a lot of spend being reported as free."),
    ad_intelligence=[
        ["Google Ads (verified)", "≈200 creatives under Araku Originals Pvt Ltd (Verified); pagination shows '4 of 80' and '8 of 80'."],
        ["Creatives sampled (verbatim)", "'ARAKU Moka Pot' and 'Chemex Coffee Maker 6 cup' (Product Listing Ads, 'Araku Coffee India'); a Local Ad Rendering Service listing for 'ARAKU Coffee' offering 'Carefully Brewed Pour-Overs' with Directions / Start / Reserve actions."],
        ["Feed tagging (verbatim)", "Landing URL from the Timemore scale ad: …arakucoffee.in/products/timemore-basic-3-0-electronic-espresso-scale?…&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic"],
        ["Measurement stack", "GA4 G-L4DG6J5D15 · Google Ads AW-11305512148 · Microsoft Clarity · Shopify · Razorpay."],
        ["Meta", "86 keyword matches for the brand term, first page dominated by third-party placements (a Siemens Home workshop featuring Araku Coffee; a separately-trading 'ARAKU HOUSE' café); brand-owned creatives not confirmed on the first page."],
    ],
    scores={"Creative Variety": [8, "#22C55E"], "UGC & Social Proof": [7, "#F59E0B"], "Copy & Hook Strength": [7, "#F59E0B"],
            "Landing Page CRO": [6, "#F59E0B"], "Tracking & CAPI": [5, "#EF4444"], "Retargeting Depth": [6, "#F59E0B"]},
    findings=[
        "<b>Every Shopping click is filed under 'sag_organic':</b> the feed's tracking template writes sag_organic into the campaign field, so paid traffic appears as organic in GA4. At roughly 200 live creatives, that is a lot of spend reported as free — and it is a minutes-long fix in the feed settings.",
        "<b>Café and e-commerce run in one account without visible separation:</b> Local store listings with Directions/Reserve and Shopping ads for brewers sit side by side, making it hard to tell whether a rupee bought a cup or a bag.",
        "<b>Meta is crowded by other businesses:</b> the first page of brand-term results is dominated by third-party placements — a partner workshop using the name and a separately-trading café. Neither is hostile, but brand search on Meta returns someone else's business first.",
        "<b>Conventional paths are not the ones your site uses:</b> /contact-us, /about-us, /faq, /menu and /locations all return 404 — the store's real architecture differs, so third-party and printed links need redirects to land anywhere useful.",
        "<b>The stack is solid and the identity chain matches:</b> GA4 and the Ads tag are confirmed by ID, Razorpay and Clarity are present, and the footer's '© Araku Originals Pvt Ltd' matches Google's verified advertiser — exactly what a brand with a co-operative origin story needs to be credible.",
    ],
    competitors=[["Specialty roasters with Bangalore cafés", "Owner-led storytelling and subscription clubs.", "Araku's seed-to-cup and plantation story is stronger; the paid account has the volume to tell it, the reporting just cannot see it clearly."],
                 ["Home-brewing equipment retailers", "Own the 'moka pot', 'chemex', 'espresso scale' searches.", "Araku is already bidding there — separate those campaigns from the café so both can be judged."],
                 ["Third parties using the brand name", "Ride the brand's search equity on Meta.", "Worth a look at the account level to see whether partner placements are intended."]],
    wins=[["WIN 1 - Fix the sag_organic campaign tag", "Minutes in the feed settings; until then every Shopping click is reported as organic traffic.", "#EF4444", "#FEF2F2"],
          ["WIN 2 - Separate café and e-commerce conversions", "Two conversion actions, two views of spend, a defensible budget split between the store and the cafés.", "#F59E0B", "#FFFBEB"],
          ["WIN 3 - Add redirects from the conventional handles", "contact-us, about-us, faq, menu and locations should land on the pages that exist — for every third-party and printed link in circulation.", "#F59E0B", "#FFFBEB"]],
    impact=[["Metric", "Current (live)", "What the fix is", "Why it matters"],
            ["Channel reporting", "Paid Shopping tagged sag_organic", "Correct the feed tracking", "Paid performance becomes visible"],
            ["Café vs store", "One account, one conversion view", "Separate conversion actions", "Budget decisions stop being arbitrary"],
            ["URL handling", "Conventional paths 404", "Redirects to real pages", "Off-campaign links keep working"]],
    sources=["Google Ads Transparency (region IN), 3 Oct 2026: ≈200 creatives under Araku Originals Pvt Ltd (Verified); Moka Pot and Chemex PLAs and the café Local Ad Listing captured verbatim; Timemore landing URL with sag_organic tagging.",
             "arakucoffee.in, 3 Oct 2026: G-L4DG6J5D15, AW-11305512148, Clarity, Razorpay; footer with customercare@arakuoriginals.com, +91-9000394000 and '© Araku Originals Pvt Ltd., 2026'; homepage copy naming flagships in Mumbai, Bangalore & Paris.",
             "Meta Ad Library (country IN), 3 Oct 2026: 86 keyword matches, first page third-party — recorded as not confirmed for the brand's own creatives."],
    outreach=[
        ["Email 1 (Day 1): ~200 live creatives — and every Shopping click filed as organic",
         "Hi team,<br/><br/>I audit paid media for Bengaluru food and beverage brands. Your account is the largest I looked at this week: <b>~200 live creatives</b> under Araku Originals Pvt Ltd, including Shopping ads for the Moka Pot and the Chemex, plus café listings with reserve actions.<br/><br/>One reporting problem sits underneath all of it: every Shopping click carries utm_campaign=sag_organic, so GA4 files your paid traffic as organic. The attached audit shows the exact URL and the fix." + SIGN],
        ["Email 2 (Day 3): Your cafés and your store share one advertiser account",
         "Hi team,<br/><br/>Second finding. In the same account I can see a local listing for 'ARAKU Coffee' with Directions and Reserve, and Shopping ads for brewing equipment landing on product pages.<br/><br/>Two different businesses, one set of conversions — which means nobody can say whether a rupee bought a café visit or a bag of beans. Separating the conversion actions takes an afternoon and makes your budget conversations evidence-based." + SIGN],
        ["Email 3 (Day 7): On Meta, your brand name returns somebody else's business first",
         "Hi team,<br/><br/>Third note, and it is delicate. Searching your brand term on Meta surfaces third-party placements ahead of your own — a partner workshop carrying the name, and a separately-trading café. Neither looks hostile, but it means brand search on Meta is not currently yours.<br/><br/>Worth a look at the account level together with whoever manages partner activity." + SIGN],
        ["Email 4 (Day 14): Closing the file on Araku Coffee",
         "Hi team,<br/><br/>Wrapping up. The audit's three moves: correct the sag_organic tag in the feed, separate café and e-commerce conversions, and add redirects from the conventional URL handles.<br/><br/>The first is a few minutes of work with immediate effect on every report your team reads. Happy to walk someone through it if useful." + SIGN],
    ],
)


# ---------------------------------------------------------------------------
# Key the lead records by the pack's slug convention (audit_pdf_food._slug).
# ---------------------------------------------------------------------------
from audit_pdf_food import _slug as _mk_slug  # noqa: E402

LEADS2 = {_mk_slug(v["brand"]): v for v in LEADS2.values()}
