"""Shared niche templates and brand hard-facts for batch lead generation."""

NICHES = {
    "skincare_beauty": {
        "platforms_row": "Meta (FB+IG) primary; Google Shopping + Search for ingredient/SKU keywords; Amazon/Flipkart/Nykaa marketplaces; quick commerce growing share.",
        "duration": "Evergreen hero SKUs run 45-90 days; new launches run 14-21 day influencer bursts; sale days (EOSS, BBD) drive heavy offer creative leading to promo fatigue.",
        "finding_templates": [
            ("Creative leak", "Ad mix leans heavy on product beauty-shots and promo announcements ('{offer}'); real-customer before/after transformation, texture demos and 30-day result Reels are thin. Beauty benchmarks show before/after UGC delivers 2.3x higher ROAS than brand creative (Agora 2025), and ingredient close-ups + texture-demo reels are the highest-CTR format in Indian skincare."),
            ("Copy leak - promo anchoring", "Headlines over-index on price/offer ('{offer}') rather than skin-outcome (clearer skin in X days, reduced pigmentation, glow). High %-off promos train buyers to deal-hunt on a replenishment category (serums/sunscreens have 30-90 day repeat). Outcome-first hooks lift CTR 40%+."),
            ("Landing page leak", "PDPs lead with offer banners and product shots; texture GIFs, in-use demo videos, day-by-day result carousels and routine-bundling sit below the fold. Sticky mobile ATC often lacks star rating + review count + FOMO (X bought in last 24h)."),
            ("Tracking & retargeting leak", "Retargeting uses generic brand creative instead of SKU-specific before/after per funnel stage (PDP-no-ATC, ATC-no-purchase, replenishment at 30/60/90 days, cross-sell). CAPI quality varies; many brands optimize to ViewContent/AddToCart rather than Purchase events.")
        ],
        "wins": [
            ("WIN 1 - Creative: 25-30 Real-Customer Transformation UGC Reels",
             "Shoot 25-30 vertical Reels monthly: before/after 14/28-day journeys (specific concern + day-stamp), texture/application demos ('sinks in 30s', 'no white cast'), ingredient-explainers with a derm/formulator, AM/PM routine clips, and micro-creator first-impression clips (10K-100K). Replace 35-40% of studio/promo creatives. Expected: CTR +35-55%, CPA -25-35%.",
             "#10B981", "#E6FBF3"),
            ("WIN 2 - CRO: Outcome-First PDPs + Routine Bundles + Sticky Social-Proof ATC",
             "On top 10 SKUs: move hero banner from offer to an outcome statement; add texture GIF, 15s in-use video and day-1/7/14/28 result strip above the fold; sticky mobile ATC with price, star rating, review count, 'X bought in 24h'; concern-specific routine bundles at ~10% bundle discount to lift AOV; route ad traffic to concern landing pages, not generic collections. Expected: PDP CVR +30-45%, AOV +20-25%.",
             "#F59E0B", "#FEF6E1"),
            ("WIN 3 - Tracking: CAPI Hardening + SKU-Specific Replenishment Retargeting",
             "Audit Meta CAPI server-side for ViewContent/ATC/InitiateCheckout/Purchase with dedup. Build 4 SKU-specific retargeting audiences with creative matched to each stage; replenishment reminders at 30/60/90 days per SKU lifecycle; subscribe-and-save for replenishment SKUs. Expected: retargeting ROAS +50-80%, repeat +15-25%.",
             "#4C27E0", "#EDE8FF"),
        ],
        "impact": [
            ["CTR (Meta)", "0.9-1.3%", "1.5-2.1%", "+40-55%"],
            ["PDP CVR", "2.0-2.7%", "2.8-3.9%", "+30-45%"],
            ["Cost Per Purchase", "Baseline = 100", "63-75", "-25-37%"],
        ],
        "score_profile": [("Creative Variety",4),("UGC & Social Proof",2),("Copy & Hook Strength",4),("Landing Page CRO",4),("Tracking & CAPI",5),("Retargeting Depth",3)],
        "structure_tpl": "SKU/concern-siloed campaigns ({top_concerns}); promo bursts around sale days; influencer/derm-KOL rotation in bursts; Advantage+ Shopping in use but creative refresh cadence is slow."
    },
    "fashion": {
        "platforms_row": "Meta (FB+IG) primary with heavy Reels; Google Shopping; Myntra/Ajio/Flipkart; own Shopify/custom D2C.",
        "duration": "Evergreen hero categories run 30-60 days; merch/drop culture runs 7-14 day launch bursts; seasonal collections rotate creative monthly.",
        "finding_templates": [
            ("Creative leak", "Ad mix is heavy on flat product-on-model studio shots and offer hooks ('up to X% off', 'from Rs.Y'). Real-customer try-on, day-in-the-life outfit, fit-test and 'how I styled it' UGC is thin. Try-on + 'real body' Reels consistently outperform studio creative 1.6-2x on Meta."),
            ("Copy leak - generic", "Headlines lead with price/drop rather than outfit outcomes, fabric-story or occasion ('Brunch look in 2 minutes', 'Stain-proof shirt for work'). Drop-chasers have lower LTV than outfit/category lovers."),
            ("Landing page leak", "PDPs lead with product-on-model hero; fabric close-up video, fit guide on the product page, size-chart inline on ATC, and 'customers also wore' outfit-builder sit below the fold. Size-related returns are the #1 P&L leak in fashion, worsened when fit info isn't above ATC."),
            ("Tracking & retargeting leak", "Retargeting uses generic collection ads; browse-abandonment pools aren't segmented by category viewed so retargeting creative is mismatched. Return/refund events are rarely sent via CAPI to suppress high-return audiences.")
        ],
        "wins": [
            ("WIN 1 - Creative: 25 Real-Customer Try-On + Styling UGC Reels",
             "Shoot 25 vertical Reels monthly: real-body try-on in 3 sizes, day-in-the-life styling (office, brunch, date, college), fabric close-up demos ('stretches 2x', 'breathable in 40C'), wash/wear durability tests, and creator 'how I styled it' OOTDs. Micro-creators (10K-100K) over macro. Expected: CTR +35-50%, CPAddToCart -20-30%.",
             "#10B981", "#E6FBF3"),
            ("WIN 2 - CRO: Fit-Info-First PDPs + Size Inline on ATC + Outfit Builder",
             "On top SKUs add fit-model stats (height, size worn) and fabric stretch/wash video above the fold; inline size-chart + 'fits TTS/large/small' customer votes inside ATC; sticky mobile ATC with size + review count + 'X bought today'; 'Complete the look' outfit builder with tiered discount (15% off 1, 20% off 2, 25% off 3). Expected: PDP CVR +25-35%, return rate -10-15%, AOV +15-20%.",
             "#F59E0B", "#FEF6E1"),
            ("WIN 3 - Tracking: CAPI with Return-Event Suppression + Category-Staged Retargeting",
             "Upgrade CAPI server-side for ViewContent/ATC/InitiateCheckout/Purchase AND Refund/Return events to suppress high-return cohorts. Build 5 retargeting pools by category viewed with matched creative; VIP 3+ order early-access + referral. Expected: retargeting ROAS +50-70%, repeat +15-20%.",
             "#4C27E0", "#EDE8FF"),
        ],
        "impact": [
            ["CTR (Meta)", "0.9-1.3%", "1.4-2.0%", "+35-50%"],
            ["PDP CVR", "2.0-2.8%", "2.6-3.6%", "+25-35%"],
            ["Return Rate", "Baseline = 100", "85-90", "-10-15% (fit info)"],
            ["Cost Per Purchase", "Baseline = 100", "68-80", "-20-32%"],
        ],
        "score_profile": [("Creative Variety",4),("UGC & Social Proof",2),("Copy & Hook Strength",4),("Landing Page CRO",4),("Tracking & CAPI",5),("Retargeting Depth",3)],
        "structure_tpl": "Category-siloed ({top_concerns}); drop/launch campaigns; influencer seeding; Advantage+ Shopping in use but creative refresh is studio-heavy."
    },
    "audio_wearables": {
        "platforms_row": "Meta (FB+IG) primary - Advantage+ Shopping; YouTube Shorts; Google Search brand/product keywords; Amazon/Flipkart marketplaces.",
        "duration": "Evergreen hero SKUs run 60-90 days; new product launches run 14-21 day heavy-pulse bursts with celebrity/influencer seeding; sale days drive offer creative.",
        "finding_templates": [
            ("Creative leak", "Ads over-index on polished product renders and spec-sheet frames ('40hr battery', 'ANC', 'IPX7'); real-customer unboxing, sound/drop/sweat torture-test, and real-use commute/gym Reels are thin. Wearables benchmarks show real-use demo UGC outperforms studio renders 2-3x in 2026."),
            ("Copy leak - spec wars", "Headlines lead with specs rather than use-case outcomes ('ANC that cancels metro noise', 'Battery that lasts your whole work week + weekend')."),
            ("Landing page leak", "PDPs lead with offer + lifestyle gallery; close-up fit/wear demos, unboxing video, sound-test comparison clips and 'why we win vs competitor X' sit below the fold."),
            ("Tracking & retargeting leak", "Catalog/dynamic ads use generic product frames; retargeting doesn't vary creative by funnel depth. Competitor conquesting is underused.")
        ],
        "wins": [
            ("WIN 1 - Creative: 20 Real-Customer Unbox + Torture-Test UGC Reels",
             "Shoot 20 vertical Reels monthly: unboxing + first-sound-reaction, torture tests (drop/sweat/water), commute/office/gym real-use, comparison clips vs same-price rivals, and 'why I switched' testimonials. 40% UGC vs studio/spec. Expected: CTR +35-50%, CPA -20-30%.",
             "#10B981", "#E6FBF3"),
            ("WIN 2 - CRO: SKU-Direct PDPs with Sticky Use-Case Proof",
             "Route ad traffic to SKU PDPs; add unboxing/demo video above fold, sticky mobile ATC with price+offer+star+review count, and a 3-row 'Real use cases' strip (commute/gym/calls) with clips. Bundle/accessory upsell (case+charger) at 10% off. Expected: CVR +25-35%, AOV +15%.",
             "#F59E0B", "#FEF6E1"),
            ("WIN 3 - Tracking: CAPI Hardening + SKU Retargeting + Competitor Conquesting",
             "Audit CAPI server-side with dedup. 4 retargeting pools (PDP-no-ATC, ATC, checkout drop, purchasers). Competitor-conquesting targeting rival brand engagers with 'why we win' creative. Expected: retargeting ROAS +40-60%.",
             "#4C27E0", "#EDE8FF"),
        ],
        "impact": [
            ["CTR (Meta)", "1.0-1.4%", "1.5-2.0%", "+35-50%"],
            ["PDP CVR", "1.8-2.4%", "2.4-3.2%", "+25-35%"],
            ["Cost Per Purchase", "Baseline = 100", "70-80", "-20-30%"],
        ],
        "score_profile": [("Creative Variety",4),("UGC & Social Proof",2),("Copy & Hook Strength",5),("Landing Page CRO",4),("Tracking & CAPI",5),("Retargeting Depth",3)],
        "structure_tpl": "SKU-siloed ({top_concerns}); launch-burst campaigns; celebrity/influencer rotation; Advantage+ Shopping in use; catalog ads heavy."
    },
    "home_furniture": {
        "platforms_row": "Meta (FB+IG) primary; Google Search; YouTube unboxing/assembly; marketplaces; company-owned stores for omnichannel.",
        "duration": "Sale-period creative runs in 7-14 day bursts; evergreen hero SKUs run 60-90 days; new launches get 2-3 week windows.",
        "finding_templates": [
            ("Creative leak", "Ads lean on studio product beauty-shots and offer banners ('up to X% off'). Customer unboxing, assembly-day, room-before/after makeover, and durability-test Reels are thin. High-ticket once-in-5-10-years purchases convert best on real-customer proof (1.6-2.2x CVR lift from UGC)."),
            ("Copy leak - offer first", "Headlines lead with %off rather than trust signals that close high-ticket purchases (free returns, warranty, trial, free installation, no-cost EMI)."),
            ("Landing page leak", "PDPs lead with price + gallery; assembly video, 360/AR view, in-room real-customer photos, warranty/trial explainer and delivery/install timelines sit below the fold. Sale traffic often routes to generic collections/alloffers pages."),
            ("Tracking & retargeting leak", "Furniture consideration is 14-60 days; retargeting windows are too short (7 days) and creative stays sale/generic instead of layering proof. Omnichannel store visits from Meta ads are underutilized.")
        ],
        "wins": [
            ("WIN 1 - Creative: 20 Customer Unboxing + Makeover UGC Reels",
             "Shoot 20 vertical Reels monthly: unboxing+assembly vlog, room-makeover before/after, durability tests, family reactions, and 6/12-month owner updates. 30 home-decor micro-creators/month. Expected: CTR +35-50%, CPA -20-30%.",
             "#10B981", "#E6FBF3"),
            ("WIN 2 - CRO: SKU-Direct PDPs with Sticky Trust Bar + AR/360 + Nearest-Store Try",
             "Route 80%+ of ad traffic to SKU PDPs; sticky bar 'Free Delivery & Install | Trial/Warranty | No Cost EMI'; 30s unboxing/assembly hero video + 360 view; customer room-photo carousel above ATC; 'try at nearest store' by pincode; AR 'view in room' where available. Expected: PDP CVR +25-40%, bounce -15%.",
             "#F59E0B", "#FEF6E1"),
            ("WIN 3 - Tracking: CAPI + 14/30/60-Day Staged Retargeting + Omnichannel Store Visits",
             "Audit CAPI; 5 retargeting layers (1-7d unboxing+price, 7-21d reviews+warranty, 21-45d offer+chat, cart abandoners install reminder, past buyers cross-sell). Meta Store Visit objective within 25km; LAL from >Rs.30K AOV buyers. Expected: retargeting ROAS +50-80%, store visits +30-50%.",
             "#4C27E0", "#EDE8FF"),
        ],
        "impact": [
            ["CTR (Meta)", "0.8-1.2%", "1.2-1.8%", "+35-50%"],
            ["PDP CVR", "1.4-2.0%", "1.9-2.8%", "+25-40%"],
            ["Cost Per Order", "Baseline = 100", "72-82", "-18-28%"],
        ],
        "score_profile": [("Creative Variety",4),("UGC & Social Proof",3),("Copy & Hook Strength",4),("Landing Page CRO",4),("Tracking & CAPI",5),("Retargeting Depth",3)],
        "structure_tpl": "Category-siloed ({top_concerns}); sale burst campaigns; product-lifestyle hero shots; omnichannel creative underutilized."
    },
    "edtech": {
        "platforms_row": "Meta (FB+IG) primary; YouTube; Google Search program/brand keywords; LinkedIn for B2B/executive; lead form and brochure/counselor-call CTAs.",
        "duration": "Evergreen programs run 60-90 days; new cohorts/batches run 14-21 day bursts; sale/scholarship periods drive offer creative.",
        "finding_templates": [
            ("Creative leak", "Creative leans on faculty/brand hero shots, brochures, and 'Admissions Open' announcements. Student-outcome UGC (salary hike, promotion, placement stories, day-in-the-life after course) is thin; outcome UGC drives 2-3x higher lead-to-call conversion vs brochure/brand ads."),
            ("Lead-form quality leak", "Primary CTA is often a brochure download or multi-field form behind a lead magnet. Industry-wide, brochure-gated leads produce 18-28% counselor-call show-rate vs 40-55% for qualified outcome-led funnels. Forms rarely use Meta 'Higher Intent' type."),
            ("Landing page leak", "Landing pages are generic per program category; placement stats, hiring partners, graduate testimonials and EMI calculator sit below the fold; primary CTA is 'Download Brochure' instead of calendar-book."),
            ("Tracking & retargeting leak", "CAPI fires on form-submit rather than qualified-lead (counselor-call complete) or enrollment events. Retargeting pools are brochure-openers with generic creative instead of layered proof (salary jump, hiring partners, EMI, Q&A, urgency).")
        ],
        "wins": [
            ("WIN 1 - Creative: 25-30 Alumni-Outcome UGC Reels",
             "Shoot 25-30 vertical Reels monthly featuring real alumni: salary-hike story (before/after CTC), promotion/career-switch, hiring-manager/mentor cred, student day-in-the-life, live-project snippets. Number-hook in first 3s. Replace 40% of brochure/faculty creative. Expected: CTR +35-55%, CPL -25-35%, lead-to-call +40-70%.",
             "#10B981", "#E6FBF3"),
            ("WIN 2 - CRO: Higher-Intent Lead Forms + Program-Specific LPs with Placement Proof",
             "Switch to Higher Intent form type with review step; 1-2 qualifying questions (work experience, target intake); 3 pre-filled fields. Program-specific LPs with sticky CTA, placement stat above fold (avg. CTC hike, hiring partners, placements), 3 alumni videos, EMI calc, calendar-book CTA. Expected: lead-to-call +40-60%, qualified CVR +30-50%.",
             "#F59E0B", "#FEF6E1"),
            ("WIN 3 - Tracking: CAPI Wired to Qualified-Lead + Enrollment + Layered Retargeting",
             "Fire CAPI for QualifiedLead (call completed) and Enrollment (fee paid), with CRM loopback. 4 retargeting layers: page-view->outcome+hiring, form-fill-no-call->EMI/objections, call-no-enroll->Q&A+urgency, alumni->referral. 24h incomplete-form WA/email reminder. Expected: recapture 15-25%, CAC -20% within 30 days.",
             "#4C27E0", "#EDE8FF"),
        ],
        "impact": [
            ["CPL (qualified lead)", "Baseline = 100", "65-75", "-25-35%"],
            ["Lead-to-call show-rate", "18-28%", "40-55%", "+40-60%"],
            ["Lead-to-enrollment", "Baseline = 100", "120-135", "+20-35%"],
        ],
        "score_profile": [("Creative Variety",4),("UGC & Social Proof",2),("Copy & Hook Strength",4),("Landing Page CRO",3),("Tracking & CAPI",5),("Retargeting Depth",3)],
        "structure_tpl": "Program-siloed campaigns; brochure/lead-magnet; scholarship/admission bursts; faculty/KOL rotation; lead-form primary."
    },
    "food_beverage": {
        "platforms_row": "Meta (FB+IG) primary; YouTube Shorts; Google Search; marketplaces (Amazon/Flipkart/Blinkit/Instamart); quick commerce critical for impulse.",
        "duration": "Evergreen hero SKUs run 45-60 days; new flavour/launch bursts 10-21 days; festive/seasonal gifting drives heavy rotation.",
        "finding_templates": [
            ("Creative leak", "Ads lean on product beauty-shots and packaging hero frames ('now Rs.X', 'pack of Y'). Taste-test reaction, recipe/ritual integration, and first-bite UGC is thin. F&B benchmarks show real taste-test and ritual Reels deliver 1.7x+ lift over studio."),
            ("Copy leak - feature-led", "Headlines lead with price/offer/pack-size rather than taste, ingredient or ritual outcome ('made with real almonds', 'guilt-free 4pm snack')."),
            ("Landing page leak", "PDPs lead with offer+pack shots; taste/close-up video, ingredient sourcing, '5 ways to eat' recipes, and subscription/save sit below the fold. Sticky ATC lacks social proof."),
            ("Tracking & retargeting leak", "Retargeting uses generic creative; flavour-specific audiences aren't segmented; subscribe-and-save / replenishment loops underused; quick-commerce deep-links not prioritized.")
        ],
        "wins": [
            ("WIN 1 - Creative: 25 Taste-Test + Ritual UGC Reels",
             "25 vertical Reels/month: honest first-bite/sip reaction, recipe/ritual integration (pre-workout, 4pm slump, kid's tiffin, post-dinner), taste-comparison vs competition, sourcing demos, micro-creator taste-tests. Replace 35% of studio. Expected: CTR +35-50%, CPA -20-30%.",
             "#10B981", "#E6FBF3"),
            ("WIN 2 - CRO: Taste/Video-First PDPs + Ritual Bundles + Subscribe-Save",
             "10s taste/close-up hero video above fold; '5 ways to enjoy' recipe block; ritual bundles (morning/evening/office) at 10% off; subscribe-save 10-15% for replenishment SKUs; sticky ATC with rating+repeat-buyer %. Expected: CVR +25-40%, AOV/retention +20%.",
             "#F59E0B", "#FEF6E1"),
            ("WIN 3 - Tracking: Flavour-Specific Retargeting + Quick-Commerce Deep Links + Replenishment",
             "Flavour-specific retargeting audiences; quick-commerce deep-links (Blinkit/Instamart/Swiggy Instamart) in retargeting creative; replenishment reminders at consumption cycle (15/30d) with subscribe-save. Expected: repeat +20-30%, retargeting ROAS +50%.",
             "#4C27E0", "#EDE8FF"),
        ],
        "impact": [
            ["CTR (Meta)", "1.0-1.4%", "1.5-2.1%", "+35-50%"],
            ["PDP CVR", "2.2-3.0%", "2.9-4.1%", "+25-40%"],
            ["Cost Per Purchase", "Baseline = 100", "70-80", "-20-30%"],
        ],
        "score_profile": [("Creative Variety",4),("UGC & Social Proof",3),("Copy & Hook Strength",4),("Landing Page CRO",4),("Tracking & CAPI",5),("Retargeting Depth",3)],
        "structure_tpl": "SKU/flavour-siloed; launch bursts around new flavours/variants; influencer seeding; quick-commerce offers; Advantage+ Shopping in use."
    },
    "jewelry": {
        "platforms_row": "Meta (FB+IG) primary; Google Search; YouTube; marketplaces; omnichannel stores (try-before-buy / home-trial).",
        "duration": "Evergreen collections run 45-90 days; festive/Valentine's/Akshaya Tritiya run 2-4 week bursts; new collection drops 14-21 days.",
        "finding_templates": [
            ("Creative leak", "Ads lean on model-with-product studio shots and offer hooks (X% off making charges). Real-customer try-on, occasion-styling, close-up craftsmanship and heirloom-story Reels are thin. Jewelry is a high-trust emotional purchase where real-women UGC drives significant lift."),
            ("Copy leak - discount-led", "Headlines lead with %off/making-charge waiver instead of design story, craftsmanship, certification (BIS Hallmark, diamond cert), occasion, or try-before-buy."),
            ("Landing page leak", "PDPs lead with price+gallery; certification badges, AR try-on / 360 view, video on skin, and customer try-on photos sit below fold. Free home-trial / 30-day return isn't anchored above ATC. Many ads route to collection pages."),
            ("Tracking & retargeting leak", "Consideration cycle is long (bridal 30-90d); retargeting windows short; creative doesn't layer proof (certs -> craft -> real bride -> offer -> urgency). Store-visit/home-trial booking objectives underused.")
        ],
        "wins": [
            ("WIN 1 - Creative: 25 Real-Customer Try-On + Occasion Styling UGC Reels",
             "25 Reels/month: real women try-on + sparkle in different lights, occasion styling (wedding/office/brunch/gifting), heirloom stories, craftsmanship/karigar close-ups, 'how I picked my wedding set' testimonials. Pair every offer ad with UGC variant. Expected: CTR +30-45%, CPLead -20-30%.",
             "#10B981", "#E6FBF3"),
            ("WIN 2 - CRO: SKU-Direct + AR Try-On + Certification/Trust-First PDPs",
             "Route SKU-direct; sticky trust bar ('BIS Hallmarked | Certified Diamonds | 30-Day Return | Free Home Try-On'); AR try-on/360 video hero; customer real-photo carousel + on-skin video; 'Book Home Trial' CTA alongside Buy Now. Expected: PDP CVR +25-40%, add-to-home-trial +40%.",
             "#F59E0B", "#FEF6E1"),
            ("WIN 3 - Tracking: CAPI + Long-Window Staged Retargeting + Store Visit / Home-Trial Objectives",
             "Fire CAPI for ViewContent/ATC/Checkout/Purchase and HomeTrialBooked. Retargeting layers 7/21/45/90d with staged proof. Enable Meta Store Visit and Home-Trial-Book objectives within geo. LAL from high-AOV buyers. Expected: retargeting ROAS +50-70%, home-trial bookings +30-50%.",
             "#4C27E0", "#EDE8FF"),
        ],
        "impact": [
            ["CTR (Meta)", "0.8-1.2%", "1.2-1.7%", "+30-45%"],
            ["PDP CVR", "1.3-1.8%", "1.7-2.5%", "+25-40%"],
            ["Cost Per Qualified Lead", "Baseline = 100", "72-80", "-20-28%"],
        ],
        "score_profile": [("Creative Variety",4),("UGC & Social Proof",3),("Copy & Hook Strength",4),("Landing Page CRO",4),("Tracking & CAPI",5),("Retargeting Depth",3)],
        "structure_tpl": "Collection-siloed ({top_concerns}); festive bursts; gifting campaigns; model-led creative heavy; AR try-on underused in paid."
    },
    "mens_grooming": {
        "platforms_row": "Meta (FB+IG) primary; YouTube Shorts; Google Search; marketplaces; D2C website.",
        "duration": "Hero SKUs run 45-90 days; new launches (fragrance/skincare) get 2-3 week influencer bursts; sale days drive offer creative.",
        "finding_templates": [
            ("Creative leak", "Ads over-index on hero/product-pack studio shots and brand ambassador frames, with heavy machismo tropes. Real-customer before/after (beard growth, oil control, fragrance longevity), texture/demo, and grooming-ritual UGC is thin."),
            ("Copy leak - generic", "Headlines lean 'X% off' / 'Beard like a boss' rather than specific outcomes ('72hr fragrance', 'beard dandruff gone in 14 days', 'oil control till end of workday')."),
            ("Landing page leak", "PDPs lead with brand imagery and offer; texture demo video, ingredient callouts, before/after photos and usage-routine sit below the fold."),
            ("Tracking & retargeting leak", "Retargeting is generic-brand; concern/SKU-specific retargeting (beard -> oil+wash combo) underused; replenishment reminders at consumption cycle missing.")
        ],
        "wins": [
            ("WIN 1 - Creative: 25 Real-Result UGC Reels",
             "25 Reels/month: 30-day beard-growth/health journeys, fragrance longevity tests (workday/gym/night out), texture/sink-in demos, grooming-routine integration, SO-reaction clips. Replace 40% of studio. Expected: CTR +35-50%, CPA -20-30%.",
             "#10B981", "#E6FBF3"),
            ("WIN 2 - CRO: Outcome-first PDPs + Grooming-Routine Bundles",
             "15s texture/use demo above fold; outcome strip ('24hr oil control', '72hr fragrance'); routine combos (oil+wash, face wash+moisturizer+sunscreen) at 15% off; sticky ATC with rating+reviews. Expected: CVR +25-35%, AOV +20%.",
             "#F59E0B", "#FEF6E1"),
            ("WIN 3 - Tracking: CAPI + Concern-Specific Retargeting + Replenishment",
             "Concern/SKU-view retargeting with matched creative; replenishment reminders at 30/60/90 days; cross-sell routine to single-SKU buyers. Expected: retargeting ROAS +50-70%, repeat +20%.",
             "#4C27E0", "#EDE8FF"),
        ],
        "impact": [
            ["CTR (Meta)", "0.9-1.3%", "1.4-2.0%", "+35-50%"],
            ["PDP CVR", "1.8-2.5%", "2.4-3.3%", "+25-35%"],
            ["Cost Per Purchase", "Baseline = 100", "70-80", "-20-30%"],
        ],
        "score_profile": [("Creative Variety",4),("UGC & Social Proof",3),("Copy & Hook Strength",4),("Landing Page CRO",4),("Tracking & CAPI",5),("Retargeting Depth",3)],
        "structure_tpl": "SKU-siloed ({top_concerns}); ambassador/influencer burst; promo-sale creative heavy; Advantage+ in use."
    },
    "clinics": {
        "platforms_row": "Meta (FB+IG) primary with lead forms + WhatsApp CTA; Google Search for treatment/doctor near-me; local inventory ads; retargeting to lead-openers.",
        "duration": "Evergreen treatments run 45-60 days; bridal/seasonal offers run 2-4 week bursts; new clinic launches get geo bursts.",
        "finding_templates": [
            ("Creative leak", "Ads lean on offer ('50% off first sitting', 'free consultation') and doctor-portrait static frames. Treatment-journey educational Reels (how it works, PRP process, day-by-day recovery) are thin. Meta prohibits dramatic before/after in medical, but educational + soft-progress content is allowed and drives 2-3x higher lead quality."),
            ("Lead form leak", "Primary CTA is a generic 'Book Free Consultation' with name+phone, no qualifying questions (concern, timeline). Sales teams burn cycles on tire-kickers. WhatsApp routes to generic numbers with 2hr+ reply SLAs."),
            ("Tracking leak", "Lead-to-consultation-attended and treatment-purchased events rarely sent back; CAPI is typically just form-submit so algorithm optimizes volume not quality. Multi-location brands serve generic creative vs nearest-clinic dynamic."),
            ("Retargeting leak", "Retargeting creative is offer-generic; FAQ/objection-handler sequences (pain, downtime, cost, safety, doctor creds) for 7-21d consideration missing. Leads not called within 30 min - the highest-conversion window.")
        ],
        "wins": [
            ("WIN 1 - Creative: 20 Educational + Soft-Journey Reels",
             "20 Meta-compliant Reels/month: doctor explains treatment (safety/downtime), first-person day-of/day-3/day-7 patient experience vlogs (no dramatic before/after), FAQ clips (does it hurt, permanent, who avoid), clinic-tour/behind-the-scenes. Replace 40% offer static. Expected: CPL -15-25%, lead quality +30%.",
             "#10B981", "#E6FBF3"),
            ("WIN 2 - CRO: Qualified Lead Forms + WhatsApp Business API with 5-min Routing",
             "Higher-Intent forms with 1 qualifying MCQ (primary concern/timeline); auto-route WA responses to the correct clinic with 5-min SLA via WA Business API+CRM; auto-reply with doctor profile+clinic rating+address. Expected: lead-to-consult show-rate +30-50%.",
             "#F59E0B", "#FEF6E1"),
            ("WIN 3 - Tracking: CAPI to Consultation-Attended + Treatment-Purchased + Geo-Routed Creative",
             "Fire CAPI for FormSubmit/ConsultBooked/ConsultAttended/TreatmentPurchased. Dynamic creative by nearest clinic; 3 retargeting layers (1-7d doctor+FAQ, 7-21d offer+proof, 21-45d bridal/seasonal urgency). <30-min lead callback SLA. Expected: cost-per-paying-patient -25-40%.",
             "#4C27E0", "#EDE8FF"),
        ],
        "impact": [
            ["CPL", "Baseline = 100", "75-85", "-15-25%"],
            ["Lead-to-consult show-rate", "30-40%", "45-60%", "+30-50%"],
            ["Cost Per Patient", "Baseline = 100", "60-75", "-25-40%"],
        ],
        "score_profile": [("Creative Variety",4),("UGC & Social Proof",3),("Copy & Hook Strength",4),("Landing Page CRO",4),("Tracking & CAPI",4),("Retargeting Depth",3)],
        "structure_tpl": "Treatment-siloed campaigns; offer-led bursts; location-targeted by clinic; lead-form/WhatsApp primary; creative mostly static-offer."
    },
    "real_estate": {
        "platforms_row": "Meta (FB+IG) primary with lead forms; Google Search; YouTube property tours; LinkedIn for premium.",
        "duration": "Project launches run 4-8 week bursts; ongoing inventory campaigns steady; festival/year-end offers 2-3 weeks.",
        "finding_templates": [
            ("Creative leak", "Ads are brochure/render-heavy - project hero shots, floor plans, discount headlines. Real resident/owner stories, drone site-progress, sample-flat walkthroughs (not polished renders), and neighborhood-lifestyle Reels are thin. Real-estate UGC typically drives 2x higher lead quality."),
            ("Lead form leak", "Forms ask name+phone+email with no qualifying questions (budget, possession timing, BHK). Sales teams chase tire-kickers; brochure downloads treated as leads. Site-visit-booking as CTA underused vs 'Download Brochure'."),
            ("Tracking leak", "CAPI rarely wired to site-visit-attended or booking; algorithm optimizes to brochure-download volume, not serious buyers. No CRM feedback loop on closed-won."),
            ("Retargeting leak", "Consideration 60-180 days; retargeting windows short, creative same as cold. Layered proof (lifestyle -> sample flat -> pricing/EMI -> urgency by tower) missing.")
        ],
        "wins": [
            ("WIN 1 - Creative: 15 Site-Progress + Resident-Story + Sample-Flat Walkthrough Reels",
             "15 Reels/month: drone site-progress updates, raw sample-flat walkthrough (not just renders), neighborhood lifestyle (schools/metro/mall), resident testimonials, RERA/pricing explainer from sales head. Replace 40% brochure/render. Expected: CPL -20% but lead-to-site-visit +50%.",
             "#10B981", "#E6FBF3"),
            ("WIN 2 - CRO: Site-Visit-Book CTA + Qualifying Forms + Virtual Tour Landing Page",
             "Primary CTA = 'Book Site Visit' / 'Book Virtual Tour'; 2 qualifiers (BHK preference, possession timeline); auto-WA with Maps link, sales rep name, sample-flat video instantly. Project-specific LPs with real walkthrough hero, pricing/EMI calc, RERA number - not brochure pages. Expected: lead-to-site-visit +40-60%.",
             "#F59E0B", "#FEF6E1"),
            ("WIN 3 - Tracking: CAPI to Site-Visit + Booking + 60/90/180-Day Retargeting",
             "Fire CAPI for Lead/SiteVisitBooked/SiteVisitAttended/Token-Booking. 4 retargeting layers over 60/120/180d: 0-14d walkthrough, 14-45d lifestyle+neighborhood, 45-90d pricing-EMI+offer, 90-180d urgency (tower closing). LAL from actual bookers. Expected: cost-per-booking -30-45%.",
             "#4C27E0", "#EDE8FF"),
        ],
        "impact": [
            ["CPL (qualified)", "Baseline = 100", "80-90", "-10-20%"],
            ["Lead-to-site-visit", "15-25%", "25-40%", "+40-60%"],
            ["Cost Per Booking", "Baseline = 100", "55-70", "-30-45%"],
        ],
        "score_profile": [("Creative Variety",4),("UGC & Social Proof",2),("Copy & Hook Strength",4),("Landing Page CRO",3),("Tracking & CAPI",4),("Retargeting Depth",2)],
        "structure_tpl": "Project-siloed; launch bursts heavy on brochure/renders; lead-form primary; CRM follow-up inconsistent."
    },
    "wellness": {
        "platforms_row": "Meta (FB+IG) primary; Google Search; YouTube; marketplaces; own D2C.",
        "duration": "Hero SKUs run 45-60 days; new launches (flavours/formats) 14-21 day bursts; new-year/summer peaks drive bursts.",
        "finding_templates": [
            ("Creative leak", "Ads lean on packaging/product shots + generic 'high protein' / 'transform yourself' headlines. Real 60/90-day transformation, taste-test, and 'how I use this daily' UGC is thin; before/after Reels drive highest ROAS in wellness."),
            ("Copy leak", "Generic 'best protein' / 'X g protein' claims don't connect to lifestyle outcomes (post-workout recovery, fat loss, busy-morning smoothie)."),
            ("Landing page leak", "PDPs lead with product+offer; taste close-up, mixing demo, third-party lab-test badges, real transformation photos sit below fold. Sticky ATC lacks social proof."),
            ("Tracking & retargeting leak", "Retargeting generic; flavour-specific audiences missing; subscribe-and-save / replenishment loops underused.")
        ],
        "wins": [
            ("WIN 1 - Creative: 25 Transformation + Taste-Test UGC Reels",
             "25 Reels/month: real 60/90d transformations (fitness/energy/skin-hair), honest taste-test reactions (not scripted), how-I-use (post-gym shake, smoothie, office snack), founder/ingredient deep-dives. Expected: CTR +35-50%, CPA -20-30%.",
             "#10B981", "#E6FBF3"),
            ("WIN 2 - CRO: Demo + Lab-Test PDPs with Sticky Social Proof + Subscribe-Save",
             "Mixing/demo hero video + third-party lab-cert badges above fold; sticky ATC with rating + 'X bought this week'; flavour bundles at 10% off; subscribe-save 15% off. Expected: CVR +25-35%, AOV +15-20%.",
             "#F59E0B", "#FEF6E1"),
            ("WIN 3 - Tracking: CAPI + Flavour-Specific Retargeting + Replenishment at Consumption Cycle",
             "Flavour-specific retargeting; replenishment reminders at 20/40d (size-dependent) with subscribe-save; cross-sell stacks (protein+shaker+multi). Expected: repeat +20-30%, retargeting ROAS +50%.",
             "#4C27E0", "#EDE8FF"),
        ],
        "impact": [
            ["CTR (Meta)", "0.9-1.3%", "1.4-2.0%", "+35-50%"],
            ["PDP CVR", "1.9-2.6%", "2.5-3.5%", "+25-35%"],
            ["Cost Per Purchase", "Baseline = 100", "70-80", "-20-30%"],
        ],
        "score_profile": [("Creative Variety",4),("UGC & Social Proof",3),("Copy & Hook Strength",4),("Landing Page CRO",4),("Tracking & CAPI",5),("Retargeting Depth",3)],
        "structure_tpl": "SKU/flavour-siloed; influencer seeding around fitness creators; launch bursts; Advantage+ Shopping in use."
    },
    "fitness": {
        "platforms_row": "Meta (FB+IG) primary; YouTube; Google Search; app install campaigns; WhatsApp/CRM for class-booking.",
        "duration": "Evergreen class/subscription creatives 30-60 days; new year/summer peaks 4-6 weeks; new centre openings geo bursts.",
        "finding_templates": [
            ("Creative leak", "Ads lean on trainer/instructor portraits and offer ('First class free', 'X% off annual'). Real member-transformation (90-day weight loss/strength), class-energy, and post-workout UGC is thin - yet member-story UGC converts highest in fitness."),
            ("Copy leak", "Generic 'get fit' / 'join now' leads don't identify specific starting points ('haven't worked out in 2 years', 'lost 8kg with 3 classes a week', 'post-pregnancy comeback')."),
            ("Landing/trial leak", "Landing pages push annual membership first; trial-class CTA is buried. Lead forms don't qualify (goal, preferred time, experience)."),
            ("Tracking & retargeting leak", "CAPI fires on lead/trial only, not paid membership. Retargeting generic instead of layered by trial stage.")
        ],
        "wins": [
            ("WIN 1 - Creative: 25 Member-Transformation + Class-Energy UGC Reels",
             "25 Reels/month: real 90d transformations (specific before/after), class-energy clips (raw, not staged), 'first week back' comeback stories, trainer quick-tips. Replace 40% of studio-portrait creative. Expected: trial CPL -25-35%, trial-to-membership +20%.",
             "#10B981", "#E6FBF3"),
            ["WIN 2 - CRO: Trial-Book First CTA + Qualifying Form + Class-Specific Landing",
             "'Book FREE Trial Class' primary CTA; Higher-Intent form with 2 qualifiers (fitness goal, preferred time); route to class-specific landing (yoga/strength/HIIT) matching ad creative not generic home; auto-WA with trainer+address instantly. Expected: trial booking +30-50%, show-rate +20%.",
             "#F59E0B", "#FEF6E1"],
            ["WIN 3 - Tracking: CAPI on Trial-Attended + Membership-Joined + Staged Retargeting",
             "Fire CAPI for TrialBooked/TrialAttended/MembershipJoined/Renewal. Retargeting layers: page-no-trial->class energy+offer; booked-trial->reminder+what-to-bring; attended-no-join->results+offer; lapsed (60+d)->comeback. LAL from 6+mo tenure members. Expected: cost-per-paid-member -25-40%.",
             "#4C27E0", "#EDE8FF"],
        ],
        "impact": [
            ["CPL (trial)", "Baseline = 100", "70-80", "-20-30%"],
            ["Trial-to-membership", "25-35%", "35-50%", "+30-50%"],
            ["Cost Per Member", "Baseline = 100", "60-75", "-25-40%"],
        ],
        "score_profile": [("Creative Variety",4),("UGC & Social Proof",2),("Copy & Hook Strength",4),("Landing Page CRO",3),("Tracking & CAPI",4),("Retargeting Depth",3)],
        "structure_tpl": "Center/class-siloed; new-year/summer bursts; offer-led free-trial creative; app install + lead form mix."
    }
}

BRAND_HARD_FACTS = {
    "Just Herbs": {
        "revenue": "~Rs.120-150 Cr ARR (est.); ayurvedic/natural skincare founded 2002 by Arush Chopra; Fireside Ventures-backed; expanding offline + international",
        "structure_extra": "Ayurvedic/heritage positioning (100% natural, ayurvedic-classified); frequent 50-75% off flash sales contributing to promo fatigue; strong on marketplaces (Nykaa, Myntra)",
        "competitors": [
            ["Forest Essentials", "Premium ayurvedic heritage; strong offline + gift sets; 50+ retail stores.", "Just Herbs competes on accessibility but doesn't leverage its ayurvedic heritage sharply enough in ads."],
            ["Plum Goodness", "Clean-beauty positioning; strong loyalty; vegan/cruelty-free messaging.", "Plum's founder-videos + ingredient education outperform Just Herbs' offer-first hooks."],
            ["mCaffeine", "Coffee-scent hero; +31% branded search momentum (HQ Index); strong texture-demo UGC.", "Texture/ingredient demo Reels are the category benchmark Just Herbs isn't matching."]
        ],
        "top_concerns": "ayurvedic skin/haircare, natural actives, clean beauty"
    },
    "Bewakoof": {
        "revenue": "~Rs.400-500 Cr FY25 (est.); founded 2012 by Prabhkiran Singh; D2C graphic-tee/casual-wear pioneer; college/GenZ audience; own print-on-demand manufacturing",
        "structure_extra": "Graphic-tee/pop-culture merch heavy (Bollywood, Marvel, anime, college collabs); frequent 'under Rs.499' sale bursts; app-first push.",
        "competitors": [
            ["The Souled Store", "Licensed merch (Disney, Marvel, IPL); 82 ads; community design contests.", "Direct graphic-tee rival outspending on licensed IP UGC."],
            ["Urban Monkey", "Streetwear; creator/skater subculture UGC; GenZ tribe building.", "Streetwear credibility Bewakoof's generic tee ads don't build."],
            ["Snitch", "Smart-casual menswear; 75 ads; fast-fashion refresh; strong fit-test content.", "Menswear adjacent with sharper fit-demo creative."]
        ],
        "top_concerns": "graphic tees, casual wear, GenZ fashion, pop-culture merch"
    },
    "SUGAR Cosmetics": {
        "revenue": "~Rs.250-300 Cr ARR (est.); founded 2012 by Vineeta Singh; omnichannel (45K+ retail points); Sequoia/Elevation-backed; lip product hero",
        "structure_extra": "Lipstick hero; 'Made in India' positioning; Rs.249 entry SKU price-anchor; heavy creator collabs; Shark Tank/IP branding.",
        "competitors": [
            ["Kay Beauty", "Katrina Kaif; premium influencer positioning; +22% branded search (HQ Index); Nykaa-distributed.", "Celebrity-founder gaining share on creator-tutorial Reels."],
            ["Swiss Beauty", "Value price anchor; mass distribution; 44 ads; volume play.", "Value end competing on price + new-shade drops."],
            ["MARS Cosmetics", "GenZ/value positioning; 40 ads; free-gift mechanic; fast SKU launches.", "Volume GenZ rival eating entry-price share."]
        ],
        "top_concerns": "lipsticks, matte lipsticks, makeup, cosmetics, kohl"
    },
    "BlueStone": {
        "revenue": "~Rs.900-1,000 Cr FY25 (est.); founded 2011 by Gaurav Kushwaha; omnichannel (175+ stores); Ratan Tata-backed; 30-day return; home trial; BIS Hallmark",
        "structure_extra": "Omnichannel 175+ stores; free home-trial; heavy bridal and everyday collections; gifting bursts; AR try-on available but underused in paid.",
        "competitors": [
            ["CaratLane", "Tanishq/Tata-backed; 70 ads; omnichannel trust; strong offline retail.", "Tata/Tanishq trust halo CaratLane leverages."],
            ["Melorra", "Everyday-wear diamond; lightweight designs for working women; app-first.", "Everyday GenZ positioning."],
            ["Tanishq", "Legacy trust; massive retail; bridal dominance.", "Incumbent with 70+ years trust."]
        ],
        "top_concerns": "gold, diamond, bridal jewelry, rings, earrings, necklaces"
    },
    "The Souled Store": {
        "revenue": "~Rs.350-400 Cr ARR (est.); founded 2012; licensed merchandise leader (Disney, Marvel, WB, IPL, Netflix)",
        "structure_extra": "Official licensing (Disney, Marvel, WB, Netflix, IPL, anime); pop-culture drops; fandom-led community; MW/W/kids expansion.",
        "competitors": [
            ["Bewakoof", "Graphic-tee D2C pioneer; 90 ads; college/GenZ; own prints.", "Original graphic-print rival."],
            ["Urban Monkey", "Streetwear/GenZ; creator/skater UGC; community drops.", "Subculture UGC The Souled Store's licensed-IP creative can feel corporate vs."],
            ["Redwolf", "Indie music/subculture tees; niche audience.", "Indie credibility, smaller spend."]
        ],
        "top_concerns": "graphic tees, official merch, licensed merchandise, pop culture"
    },
    "Noise": {
        "revenue": "~Rs.1,439 Cr FY25 (IDC); founded 2014 by Amit & Gaurav Khatri; smartwatch leader (~27% share IDC); TWS/buds/smart rings",
        "structure_extra": "Smartwatch #1 by volume in India; celebrity endorsements (Virat Kohli); heavy new-model launch bursts; GoNoise app; budget-mid price points.",
        "competitors": [
            ["boAt", "#1 TWS/wearables by share (27.6% wearables/36.8% TWS per IDC); Rs.3,100 Cr FY25.", "Primary rival outspending on UGC/launch."],
            ["Boult Audio", "10.8% YoY wearables growth; 55 ads; budget leader.", "Budget end eating share on price+UGC."],
            ["Fire-Boltt", "+49.3% smartwatch growth; aggressive pricing; heavy Amazon.", "Mass price warrior with rapid launches."]
        ],
        "top_concerns": "smartwatches, TWS earbuds, smart rings, fitness bands"
    },
    "Cult.fit": {
        "revenue": "~Rs.550 Cr FY26 (est.); founded 2016 by Mukesh Bansal (Myntra); omnichannel fitness (300+ centers); Cure.fit + Eat.fit ecosystem",
        "structure_extra": "Subscription fitness 300+ centers; group-class focus (Strength, HRX, Yoga, Boxing); app-based workouts; healthcare + food ecosystem.",
        "competitors": [
            ["Anytime Fitness / Gold's Gym", "Global franchises; strong PT/offline.", "Traditional offline rivals."],
            ["Fittr", "Online-only coaching; strong transformation UGC; community-led.", "Online UGC specialist with sharper before/after."],
            ["HealthifyMe", "App-first AI coaching; higher app-store presence.", "App/AI weight-loss rival."]
        ],
        "top_concerns": "gym, group fitness, strength, yoga, HRX, workout classes"
    },
    "Beardo": {
        "revenue": "~Rs.200-250 Cr ARR (est.); founded 2016; acquired by Marico; beard-care pioneer; expanded to perfumes/skincare/hair",
        "structure_extra": "Marico-owned; machismo 'Beardo' persona; perfume hero (Godfather, Don); SKU expansion to face-wash/sunscreen/serum.",
        "competitors": [
            ["The Man Company", "Premium men's grooming; 52 ads; clean-ingredient; fragrance focus.", "Direct D2C rival with cleaner ingredient storytelling."],
            ["Bombay Shaving Company", "Shaving heritage; grooming routines; strong unboxing UGC; subscription.", "Routine + shaving demo creative."],
            ["Ustraa", "Dabur-backed; volume play; wide SKU; strong offline.", "Dabur distribution + mass pricing."]
        ],
        "top_concerns": "beard oil, beard growth, men's perfume, fragrance"
    },
    "Snitch": {
        "revenue": "~Rs.200 Cr ARR (est.); founded 2019 by Siddharth R. Dungarwal; menswear smart-casual; fast-fashion; 48hr dispatch",
        "structure_extra": "Menswear smart-casual; rapid SKU refresh; affordable price points; aggressive Reels ads; shirts/trousers/blazers hero.",
        "competitors": [
            ["Bewakoof / Souled Store", "Casual/graphic-tee; broader audience.", "Casual end of menswear."],
            ["DaMENSCH", "Premium menswear innerwear/essentials; 45 ads; fabric-tech.", "Premium essentials with stronger fabric UGC."],
            ["Rare Rabbit", "Premium menswear; higher price; designer positioning.", "Premium/designer adjacent."]
        ],
        "top_concerns": "shirts, trousers, smart casual, blazers, menswear"
    },
    "Country Delight": {
        "revenue": "~Rs.1,200-1,300 Cr FY25 (est.); founded 2013 by Chakradhar Gade; subscription milk/daily essentials; 10+ cities; own sourcing/testing",
        "structure_extra": "Subscription milk delivery app-led; bread/eggs/ghee/grocery expansion; 'test-kitchen' quality story; doorstep morning delivery; wallet/subscription.",
        "competitors": [
            ["Milkbasket", "Daily grocery micro-delivery; subscription.", "Micro-delivery subscription rival."],
            ["Amul / Mother Dairy", "Legacy dairy; massive offline; trust halo.", "Heritage brands."],
            ["BigBasket/BB Now", "Quick-commerce groceries.", "Quick-commerce impulse."]
        ],
        "top_concerns": "milk, dairy, subscription milk, bread, eggs"
    },
    "mCaffeine": {
        "revenue": "~Rs.300+ Cr ARR; founded 2016; IPL/Elevation-backed; coffee-scent hero; +31% branded search (HQ Index)",
        "structure_extra": "Coffee-scent positioning hero; strong texture-demo UGC (body scrub, latte moisturizer); haircare/shower expansion; international presence.",
        "competitors": [
            ["Mamaearth", "Honasa; Rs.1,200 Cr; wider portfolio; influencer-heavy.", "Parent-group brand with broader portfolio."],
            ["Plum Goodness", "Clean beauty; 60 ads; strong loyalty.", "Clean-beauty competitor."],
            ["Minimalist (HUL)", "Ingredient-% hero; HUL distribution; 550K searches/mo.", "Ingredient-trust rival."]
        ],
        "top_concerns": "coffee body scrub, caffeine skincare, latte moisturizer"
    },
    "The Sleep Company": {
        "revenue": "~Rs.400-500 Cr ARR (est.); founded 2019 by Ankit Garg; SmartGRID patented tech; premium mattresses (Rs.24-32K queen); Priyanka Chopra brand ambassador",
        "structure_extra": "SmartGRID patent; heavy demo-video creative (egg-drop, pressure-test); premium pricing; 100-night trial; omnichannel experience stores.",
        "competitors": [
            ["Wakefit", "#1 D2C mattress; ~Rs.1,375 Cr FY26; 201 stores; orthopedic hero.", "Primary D2C rival with 2-3x revenue and omnichannel scale."],
            ["SleepyCat", "Value (~Rs.12K queen); AirGen memory foam; strong unboxing UGC.", "Value end with unboxing creative."],
            ["Flo", "Ortho/Painrelease; strong back-pain outcome Reels.", "Back-pain outcome positioning."]
        ],
        "top_concerns": "SmartGRID mattress, premium mattress, orthopedic mattress"
    },
    "CaratLane": {
        "revenue": "~Rs.2,500-3,000 Cr FY25 (est.); Tata/Tanishq subsidiary; 200+ stores; omnichannel; everyday-wear diamond",
        "structure_extra": "Tata/Tanishq subsidiary; omnichannel 200+ stores; everyday-wear lightweight diamond; try-at-home; trust + affordability.",
        "competitors": [
            ["BlueStone", "Omnichannel online-first; 85 ads; 175 stores; home-trial.", "Online-first rival with similar omnichannel play."],
            ["Tanishq", "Tata parent; massive offline bridal; legacy trust.", "Sister brand with stronger bridal pull."],
            ["Melorra", "Everyday-wear diamond; app-first; GenZ working-women.", "Everyday GenZ digital rival."]
        ],
        "top_concerns": "diamond jewellery, rings, earrings, solitaire, Tanishq"
    },
    "Oliva Skin & Hair": {
        "revenue": "~Rs.300-400 Cr ARR (est.); 75+ clinics across 23 cities; founded 2009; hair transplant/skin/laser/aesthetics",
        "structure_extra": "Multi-city dermatology chain (75 clinics, 23 cities); high-ticket hair transplant; laser hair removal; skin; doctor-led; lead-form/WhatsApp.",
        "competitors": [
            ["Kaya Clinic", "Legacy derm chain (Marico); 50 ads; wider presence.", "Incumbent with legacy."],
            ["VLCC Wellness", "Multi-category wellness/slimming/skin; 45 ads; national.", "Wellness+beauty combo chain."],
            ["Cure.fit / Cult.fit", "Fitness + primary care crossover.", "Digital health platform."]
        ],
        "top_concerns": "hair transplant, laser hair removal, acne, skin, dermatologist"
    },
    "Wow Skin Science": {
        "revenue": "~Rs.300-400 Cr ARR (est.); founded 2013; apple-cider-vinegar hero; onion hair oil mass-market; wide SKU; FMCG/offline expansion",
        "structure_extra": "Onion shampoo/hair oil + apple-cider-vinegar hero; strong offline/FMCG expansion; heavy Amazon; value mass-market.",
        "competitors": [
            ["Mamaearth", "Honasa; Rs.1,200 Cr; wider portfolio; influencer-heavy.", "Portfolio/FMCG rival."],
            ["mCaffeine", "Coffee-scent hero; +31% momentum; texture UGC.", "Niche-ingredient rival gaining share."],
            ["Ponds/Lakme (HUL)", "Mass FMCG legacy; enormous distribution.", "Mass incumbents."]
        ],
        "top_concerns": "onion hair oil, apple cider vinegar, shampoo, skincare"
    },
    "The Whole Truth": {
        "revenue": "~Rs.100-150 Cr ARR (est.); founded 2019 by Shashank Mehta; clean-label protein bars/chocolate/snacks; 'no nasties' ingredient transparency",
        "structure_extra": "Clean-label protein bars and chocolate; 'no sugar alcohol, no artificial sweeteners'; ingredient-led; strong founder storytelling; subscription snack packs.",
        "competitors": [
            ["Yoga Bar", "Bar/nutrition mass-play; 60 ads; broader distribution.", "Mass muesli/bar rival."],
            ["RiteBite Max Protein", "Mass protein bar; offline distribution; lower price.", "Mass volume rival."],
            ["Happilo", "Dry-fruit/snack; 42 ads; healthy snacking.", "Adjacent healthy snacking."]
        ],
        "top_concerns": "protein bars, clean chocolate, healthy snacks, no added sugar"
    },
    "Plum Goodness": {
        "revenue": "~Rs.250-300 Cr ARR (est.); founded 2013 by Shankar Prasad; clean-beauty / vegan / cruelty-free; body/skin/haircare; Unilever Ventures",
        "structure_extra": "Clean-beauty vegan/cruelty-free positioning; strong 'Plum Perks' loyalty; body-wash/mist/serum; Nykaa/offline expansion.",
        "competitors": [
            ["mCaffeine", "Coffee-scent; +31% search; texture UGC.", "Niche-ingredient rival."],
            ["Minimalist (HUL)", "Ingredient-% hero; HUL distribution.", "FMCG-backed rival."],
            ["Foxtale", "Creator-led skincare; $56.8M Series C; 38 ads.", "Creator-led fast grower."]
        ],
        "top_concerns": "clean beauty, vegan, body wash, serum, moisturizer"
    },
    "Yoga Bar": {
        "revenue": "~Rs.250-300 Cr ARR (est.); founded 2014; muesli/protein/breakfast bars; acquired by ITC in 2023",
        "structure_extra": "ITC-owned since 2023; breakfast bars/muesli/protein bars; strong modern-trade + D2C; healthy breakfast.",
        "competitors": [
            ["The Whole Truth", "Clean-label protein bars; ingredient transparency; D2C.", "Clean-label D2C rival."],
            ["RiteBite / MuscleBlaze", "Sports nutrition mass-play.", "Mass protein rivals."],
            ["Happilo", "Dry fruit/snack; 42 ads; premium gifting.", "Premium healthy snacks."]
        ],
        "top_concerns": "muesli, protein bars, breakfast bars, healthy snacking"
    },
    "Clove Dental": {
        "revenue": "~Rs.400-500 Cr (est.); 250+ clinics across India; dental chain; founded 2011; Sequoia/Chiratae-backed; lead-form + WhatsApp primary",
        "structure_extra": "250+ clinics dental chain (Delhi NCR, Bengaluru, Mumbai, Hyderabad); implants/ortho/cosmetic/pediatric; WhatsApp booking with known 2hr reply SLA.",
        "competitors": [
            ["Sabka Dentist", "Mass-priced dental; 100+ clinics; volume play.", "Mass dental rival."],
            ["Apollo Dental / Max", "Hospital-anchored trust chains.", "Hospital-trust rivals."],
            ["Local independent dentists", "Market ~85% unbranded.", "Fragmented share."]
        ],
        "top_concerns": "dental implants, root canal, braces, aligners, teeth whitening"
    }
}

def niche_bucket(niche, brand):
    n = niche.lower()
    if "skincare" in n or "beauty" in n or "cosmetic" in n: return "skincare_beauty"
    if "fashion" in n or "athleisure" in n or "bag" in n: return "fashion"
    if "audio" in n or "wearable" in n or "electronics" in n: return "audio_wearables"
    if "home" in n or "furniture" in n: return "home_furniture"
    if "edtech" in n or "coach" in n: return "edtech"
    if "f&b" in n or "food" in n or "dairy" in n or "nutrition" in n or "beverage" in n or "snack" in n: return "food_beverage"
    if "jewel" in n: return "jewelry"
    if "grooming" in n: return "mens_grooming"
    if "clinic" in n or "dental" in n: return "clinics"
    if "real estate" in n: return "real_estate"
    if "wellness" in n or "health" in n: return "wellness"
    if "fitness" in n: return "fitness"
    return "skincare_beauty"
