# Verify the data — every claim, and where to check it

Every number in the 21 audits came from a public surface that you (or the lead) can open.
This file maps each claim to the exact place it was read: the first eleven audits on
**2 October 2026**, the ten added leads on **3 October 2026**.

Three ground rules used throughout:

- If a value could not be measured, the audit says **unavailable** or **not measured** — it is never estimated.
- A tag is only described as absent when a second method confirmed it; otherwise the audit says **unconfirmed**.
- Spend, ROAS and CPA are **never** stated, because no public source exists for them.

## The four verification routes

| Route | What it proves | How to use it |
|---|---|---|
| Google Ads Transparency Center | Live Google creative counts per domain | Open `adstransparency.google.com`, set the region to **India**, and enter the brand domain |
| Meta Ad Library | Live Meta ads per brand term, plus individual creatives by ID | Open `facebook.com/ads/library`, set country to **India**, search the brand name; a specific ad opens at `?id=<library id>` |
| The brand's own site | Tag IDs, title tags, footers, structured data, broken pages | Open the page, press **Ctrl+U** (view source), then **Ctrl+F** for the ID or string quoted in the audit |
| Response headers | HSTS, cache-control, CDN, server stack, CORS | `securityheaders.com/?q=<domain>` or a terminal: `curl -I https://<domain>` |

## What cannot be verified by anyone outside the company

| Item | Why |
|---|---|
| Ad spend (Rs/month) | No public source exists. Ad platforms do not disclose spend for commercial advertisers. |
| ROAS and CPA | Only visible inside the advertiser's own ad accounts and analytics. |
| Conversion rates | Private to the advertiser. |
| Internal revenue splits by channel | Private to the advertiser. |
| Meta ad inventory for four batch-2 brands (Pure & Sure, Eat Better Co, Brik Oven, Araku Coffee) | Their brand terms return unrelated advertisers in the Meta Ad Library, so no brand-specific Meta count is reported. The audits say NOT MEASURED rather than quoting a noisy number. |
| Google's own header count vs its grid count | On several accounts Google's header figure and its pagination disagree (for example Adukale 13 vs 26, Barbeque Nation 19 vs 34, Sid's Farm ~200 vs 35 across account and domain views). Both figures are shown with the date; Google does not publish a reconciliation. |
| Checkout, order and payment flows | Behind the storefront root; not crawled for any lead. Stated as NOT MEASURED in every coverage table. |
| Proof that a tag fires (or does not fire) | Page-source inspection shows what is configured in the HTML. A tag loaded through a tag manager or a platform layer can be invisible to that method, so the audits never call a tag absent. |

---

## Per-lead checklists


### Licious

Site: `licious.in` · measured 2 October 2026

| Claim in the audit | Where to check it | Link | What you should see |
|---|---|---|---|
| ≈300 live Google creatives | Google Ads Transparency Center (region: India) | [https://adstransparency.google.com/?region=IN&domain=licious.in](https://adstransparency.google.com/?region=IN&domain=licious.in) | The page header reads approximately 300 ads, under Delightful Gourmet Pvt Ltd (Verified). |
| ≈550 live Meta ads | Meta Ad Library (country: India) | [https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=IN&q=Licious&search_type=keyword_unordered](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=IN&q=Licious&search_type=keyword_unordered) | Around 550 results for the brand term. |
| Meta library ID 983369480870934 | Meta Ad Library — the ad itself | [https://www.facebook.com/ads/library/?id=983369480870934](https://www.facebook.com/ads/library/?id=983369480870934) | The specific Licious ad referenced in the audit, with its running-since date. |
| GTM-KVBCJN · GA4 G-YN0TX18PEE · Ads AW-871318622 | licious.in page source | [https://licious.in](https://licious.in) | Open the page, press Ctrl+U (view source), then Ctrl+F each ID. All four appear, including Meta pixel 378591842535023. |
| FY25 revenue ≈Rs 795 Cr, loss ≈Rs 218.3 Cr | licious.in — published company results | [https://www.licious.in/](https://www.licious.in/) | Published in the company's reported FY25 results. This is a third-party reported figure, quoted as reported. |
| talktous@licious.com | licious.in support / contact page | [https://www.licious.in/](https://www.licious.in/) | Publish in the site's contact or help section. |

### Akshayakalpa Organic

Site: `akshayakalpa.org` · measured 2 October 2026

| Claim in the audit | Where to check it | Link | What you should see |
|---|---|---|---|
| ≈400 live Google creatives | Google Ads Transparency Center (region: India) | [https://adstransparency.google.com/?region=IN&domain=akshayakalpa.org](https://adstransparency.google.com/?region=IN&domain=akshayakalpa.org) | Around 400 creatives — the largest paid footprint in this set. |
| 3 live Meta creatives from the brand page | Meta Ad Library (country: India) | [https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=IN&q=Akshayakalpa&search_type=keyword_unordered](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=IN&q=Akshayakalpa&search_type=keyword_unordered) | Three creatives from the Akshayakalpa page; the audit cites their running-since dates. |
| Meta IDs 2186726058790625 · 935934206094801 · 958522520368361 | Meta Ad Library — individual ads | [https://www.facebook.com/ads/library/?id=935934206094801](https://www.facebook.com/ads/library/?id=935934206094801) | Opens the creative running since 19 May 2026. Swap the id for either of the other two. |
| Swiggy Instamart runs Akshayakalpa product creative | Meta Ad Library | [https://www.facebook.com/ads/library/?id=3384075765110108](https://www.facebook.com/ads/library/?id=3384075765110108) | A Swiggy Instamart placement featuring Akshayakalpa paneer, 9 variants. This is third-party distribution, not the brand's own account. |
| Contact Us page shows '0123.456.789 - 2 Queen Street, California' | akshayakalpa.org/contact-us | [https://akshayakalpa.org/contact-us](https://akshayakalpa.org/contact-us) | The placeholder text sits at the top of the Contact Us page. Note the contrast: the homepage footer carries the correct Tiptur, Karnataka address, which is why the audit names the exact page. |
| No cache-control, no HSTS | Response headers of akshayakalpa.org | [https://securityheaders.com/?q=akshayakalpa.org](https://securityheaders.com/?q=akshayakalpa.org) | Or from a terminal: curl -I https://akshayakalpa.org — neither header comes back. |
| support@akshayakalpa.org | akshayakalpa.org FAQ and privacy policy | [https://akshayakalpa.org/](https://akshayakalpa.org/) | The only official address the brand publishes. |

### Anand Sweets

Site: `anandsweets.in` · measured 2 October 2026

| Claim in the audit | Where to check it | Link | What you should see |
|---|---|---|---|
| 58 live Google creatives | Google Ads Transparency Center (region: India) | [https://adstransparency.google.com/?region=IN&domain=anandsweets.in](https://adstransparency.google.com/?region=IN&domain=anandsweets.in) | Around 58 creatives. |
| OpenAI ads pixel MsnBMqKgkHz42jqdSfTfFQ | anandsweets.in page source | [https://anandsweets.in](https://anandsweets.in) | Ctrl+U then Ctrl+F 'MsnBMqKgkHz42jqdSfTfFQ' — the OpenAI advertising pixel is in the storefront source. |
| HSTS, CSP, X-Frame-Options all present | Response headers | [https://securityheaders.com/?q=anandsweets.in](https://securityheaders.com/?q=anandsweets.in) | All four header families return a pass — the strongest posture in this set. |
| 4.4 rating from 250 reviews | anandsweets.in structured data | [https://anandsweets.in](https://anandsweets.in) | Ctrl+F 'aggregateRating' in the page source. |
| care@anandsweets.net | anandsweets.in footer / contact | [https://www.anandsweets.in/](https://www.anandsweets.in/) | Published in the site footer. |

### Chai Point

Site: `chaipoint.com` · measured 2 October 2026

| Claim in the audit | Where to check it | Link | What you should see |
|---|---|---|---|
| 56 live Google creatives | Google Ads Transparency Center (region: India) | [https://adstransparency.google.com/?region=IN&domain=chaipoint.com](https://adstransparency.google.com/?region=IN&domain=chaipoint.com) | Around 56 creatives, under Mountain Trail Foods. |
| GA4 G-EN77D2S0YH on the site root | chaipoint.com page source | [https://chaipoint.com](https://chaipoint.com) | Ctrl+U then Ctrl+F 'G-EN77D2S0YH'. |
| 900,000+ cups a day · 150+ stores · 8,100+ workplaces | chaipoint.com structured data (JSON-LD) | [https://chaipoint.com](https://chaipoint.com) | Ctrl+F 'cups' or '900' in the page source; the figures are in the machine-readable JSON-LD block. |
| Static build on Amazon S3 + CloudFront | Response headers | [https://securityheaders.com/?q=chaipoint.com](https://securityheaders.com/?q=chaipoint.com) | Server headers show cloudfront and S3 asset hosting. |
| customercare@chaipoint.com | Chai Point help centre | [https://shop.chaipoint.com/](https://shop.chaipoint.com/) | Published on the order site's help section. |

### The Baker's Dozen

Site: `thebakersdozen.in` · measured 2 October 2026

| Claim in the audit | Where to check it | Link | What you should see |
|---|---|---|---|
| 35 live Google creatives | Google Ads Transparency Center (region: India) | [https://adstransparency.google.com/?region=IN&domain=thebakersdozen.in](https://adstransparency.google.com/?region=IN&domain=thebakersdozen.in) | Around 35 creatives. |
| GTM-MQQF2MXB · Ads AW-618150299 | thebakersdozen.in page source | [https://thebakersdozen.in](https://thebakersdozen.in) | Ctrl+F each ID in the page source. |
| Meta pixel 3996239487069441 | thebakersdozen.in page source | [https://thebakersdozen.in](https://thebakersdozen.in) | Ctrl+F '3996239487069441'. |
| No HSTS, no cache-control, no security headers | Response headers | [https://securityheaders.com/?q=thebakersdozen.in](https://securityheaders.com/?q=thebakersdozen.in) | Most or all headers return a fail. |
| fresh@thebakersdozen.in | thebakersdozen.in/contact-us | [https://thebakersdozen.in/contact-us](https://thebakersdozen.in/contact-us) | Published on the contact page. |

### Cothas Coffee

Site: `cothas.com` · measured 2 October 2026

| Claim in the audit | Where to check it | Link | What you should see |
|---|---|---|---|
| 77 live Google creatives | Google Ads Transparency Center (region: India) | [https://adstransparency.google.com/?region=IN&domain=cothas.com](https://adstransparency.google.com/?region=IN&domain=cothas.com) | Around 77 creatives, under Freeflow Creative Services. |
| Tag layer unconfirmed | Chrome DevTools on cothas.com | [https://cothas.com](https://cothas.com) | This is the one claim you can settle in a browser: open DevTools → Network, filter 'collect' or 'gtm', and reload. If tags fire, the audit's 'unconfirmed' wording is exactly right — and the fix is simply to confirm it. |
| customercare@cothas.com | cothas.com/pages/contact-us | [https://cothas.com/pages/contact-us](https://cothas.com/pages/contact-us) | Published on the contact page. |
| Founded 1948, Jigani facility | Cothas Coffee — own pages | [https://cothas.com/](https://cothas.com/) | Stated on the brand's own site. |

### Early Foods

Site: `earlyfoods.com` · measured 2 October 2026

| Claim in the audit | Where to check it | Link | What you should see |
|---|---|---|---|
| 30 live Google creatives | Google Ads Transparency Center (region: India) | [https://adstransparency.google.com/?region=IN&domain=earlyfoods.com](https://adstransparency.google.com/?region=IN&domain=earlyfoods.com) | Around 30 creatives. |
| Shopify theme 124761112618 behind Cloudflare | Response headers + page source | [https://earlyfoods.com](https://earlyfoods.com) | Cloudflare reported in the server headers; the theme ID appears in the storefront source. |
| hello@earlyfoods.com | earlyfoods.com | [https://earlyfoods.com/](https://earlyfoods.com/) | Published on the site. |

### iD Fresh Food

Site: `idfreshfood.com` · measured 2 October 2026

| Claim in the audit | Where to check it | Link | What you should see |
|---|---|---|---|
| 1 live Google creative | Google Ads Transparency Center (region: India) | [https://adstransparency.google.com/?region=IN&domain=idfreshfood.com](https://adstransparency.google.com/?region=IN&domain=idfreshfood.com) | A single creative — the finding that drives this audit. |
| Access-Control-Allow-Origin: * | Response headers | [https://securityheaders.com/?q=idfreshfood.com](https://securityheaders.com/?q=idfreshfood.com) | Or: curl -I https://idfreshfood.com — the wildcard CORS header is returned. |
| LiteSpeed cache HIT | Response headers | [https://securityheaders.com/?q=idfreshfood.com](https://securityheaders.com/?q=idfreshfood.com) | The cache header reports a hit, confirming the cache layer works. |
| customercare@idfreshfood.com | idfreshfood.com/contact-us | [https://idfreshfood.com/contact-us](https://idfreshfood.com/contact-us) | Published on the contact page. |
| FY25 revenue ≈Rs 681.4 Cr, PAT ≈Rs 25.87 Cr | Published FY25 results as reported | [https://idfreshfood.com/](https://idfreshfood.com/) | Figures are quoted as reported, not audited by us. |

### Third Wave Coffee

Site: `thirdwavecoffeeroasters.com` · measured 2 October 2026

| Claim in the audit | Where to check it | Link | What you should see |
|---|---|---|---|
| Title tag is the domain string | thirdwavecoffeeroasters.com page source | [https://thirdwavecoffeeroasters.com](https://thirdwavecoffeeroasters.com) | Ctrl+U and look at the first line inside <head>: the title reads 'www.thirdwavecoffeeroasters.com' instead of the brand name. |
| 0 live Google creatives | Google Ads Transparency Center (region: India) | [https://adstransparency.google.com/?region=IN&domain=thirdwavecoffeeroasters.com](https://adstransparency.google.com/?region=IN&domain=thirdwavecoffeeroasters.com) | No creatives are returned for the domain. The audit states this as measured on one day for this domain, not as a claim about the whole account. |
| orders@thirdwavecoffee.in | thirdwavecoffee.in/pages/contact | [https://thirdwavecoffee.in/pages/contact](https://thirdwavecoffee.in/pages/contact) | Published on the contact page. |

### Frozen Bottle

Site: `frozenbottle.com` · measured 2 October 2026

| Claim in the audit | Where to check it | Link | What you should see |
|---|---|---|---|
| 11 live Google creatives | Google Ads Transparency Center (region: India) | [https://adstransparency.google.com/?region=IN&domain=frozenbottle.com](https://adstransparency.google.com/?region=IN&domain=frozenbottle.com) | Around 11 creatives. |
| A stale FAQ URL returns 404 | frozenbottle.com/pages/faq vs the live /pages/faqs | [https://frozenbottle.com/pages/faq](https://frozenbottle.com/pages/faq) | The singular URL returns 'not found'. The working FAQ is the plural one: frozenbottle.com/pages/faqs — the audit states both, so you can see exactly what is and is not broken. |
| vipul@frozenbottle.in | frozenbottle.com footer (partnership section) | [https://frozenbottle.com/](https://frozenbottle.com/) | Published under collaboration and partnership in the footer. |

### Milky Mist

Site: `milkymist.com` · measured 2 October 2026

| Claim in the audit | Where to check it | Link | What you should see |
|---|---|---|---|
| 3 live Google creatives | Google Ads Transparency Center (region: India) | [https://adstransparency.google.com/?region=IN&domain=milkymist.com](https://adstransparency.google.com/?region=IN&domain=milkymist.com) | Around 3 creatives. |
| Wix behind Varnish | Response headers | [https://securityheaders.com/?q=milkymist.com](https://securityheaders.com/?q=milkymist.com) | Server headers show Varnish and Wix identifiers. |
| customercare@milkymist.com | milkymist.com/reach-us | [https://milkymist.com/reach-us](https://milkymist.com/reach-us) | Published on the reach-us page. |

### SMOOR

Site: `smoor.in` · measured 3 October 2026

| Claim in the audit | Where to check it | Link | What you should see |
|---|---|---|---|
| 22 live Google creatives | Google Ads Transparency Center (region: India) — domain view | [https://adstransparency.google.com/?region=IN&domain=smoor.in](https://adstransparency.google.com/?region=IN&domain=smoor.in) | The page header reads '22 ads', under Bliss Chocolates India Private Limited (Verified). |
| The Product Listing Ad title quoted in this report | Google Ads Transparency Center — the advertiser page | [https://adstransparency.google.com/advertiser/AR02616125499809726465?region=IN](https://adstransparency.google.com/advertiser/AR02616125499809726465?region=IN) | One of the creatives is a Product Listing Ad titled 'Elsa and Anna Cake | Frozen Theme Birthday Cake | … by SMOOR | 1.5 Kg'. |
| Meta creative 1419659120007418 (since 5 August 2026, corporate gifting) | Meta Ad Library — the ad itself | [https://www.facebook.com/ads/library/?id=1419659120007418](https://www.facebook.com/ads/library/?id=1419659120007418) | Active; page run by SMOOR Chocolates; landing smoor.in/pages/corporate-gifting. Keyword searches are noisy, so this creative is cited by library ID rather than by a keyword count. |
| Meta creative 1059529900062691 (since 3 August 2026) | Meta Ad Library — the ad itself | [https://www.facebook.com/ads/library/?id=1059529900062691](https://www.facebook.com/ads/library/?id=1059529900062691) | Active on the crawl date; same campaign, same destination page. |
| Meta creative 1101131689270428 (since 8 September 2026) | Meta Ad Library — the ad itself | [https://www.facebook.com/ads/library/?id=1101131689270428](https://www.facebook.com/ads/library/?id=1101131689270428) | Active on the crawl date; same campaign, same destination page. |
| GA4 G-JKGWG119TH · Google Ads AW-872198756 | smoor.in page source | [https://smoor.in](https://smoor.in) | Open the page, press Ctrl+U (view source), then Ctrl+F each ID — both appear. |
| /pages/contact and /pages/bulk-enquiry return 404 while /pages/contact-us works | smoor.in — the URLs themselves (or any HTTP status checker) | [https://smoor.in/pages/contact](https://smoor.in/pages/contact) | Type the URL: 404. Change it to /pages/contact-us: the contact page loads. |
| info@smoorchocolates.com | smoor.in — FAQ and privacy-policy pages | [https://smoor.in/pages/faq](https://smoor.in/pages/faq) | Published on the FAQ page; the phone number +91 8822201202 appears in the storefront header. |
| Bengaluru stores and the registered entity | smoor.in — store locator | [https://smoor.in/pages/store-locator](https://smoor.in/pages/store-locator) | Lists SMOOR Experience Centre Indiranagar (No. 1131, 100 Feet Road, Indiranagar Stage II, Bengaluru 560038) among other locations, under Bliss Chocolates India Private Limited. |

### Sid's Farm

Site: `sidsfarm.com` · measured 3 October 2026

| Claim in the audit | Where to check it | Link | What you should see |
|---|---|---|---|
| ≈200 creatives in the advertiser account | Google Ads Transparency Center — advertiser page | [https://adstransparency.google.com/advertiser/AR10174224753343070209?region=IN](https://adstransparency.google.com/advertiser/AR10174224753343070209?region=IN) | The header reads approximately 200 ads under Sids Farm Private Limited (Verified). |
| 35 creatives point at sidsfarm.com | Google Ads Transparency Center — domain view | [https://adstransparency.google.com/?region=IN&domain=sidsfarm.com](https://adstransparency.google.com/?region=IN&domain=sidsfarm.com) | The domain view header reads '35 ads'. |
| Meta creative library ID 1682864186042714 (WhatsApp click-through) | Meta Ad Library — the ad itself | [https://www.facebook.com/ads/library/?id=1682864186042714](https://www.facebook.com/ads/library/?id=1682864186042714) | A Sid's Farm ad on the page 'Sid's Farm' (facebook.com/sidsfarmpure), running since 8 April 2026, with a WhatsApp CTA. |
| Meta creative library ID 28227187223577653 and its landing URL | Meta Ad Library — the ad itself | [https://www.facebook.com/ads/library/?id=28227187223577653](https://www.facebook.com/ads/library/?id=28227187223577653) | The '22g protein' ad, running since 17 August 2026, landing app.sidsfarm.com with utm_source=facebook and {{campaign.id}} macros. |
| Two GTM containers and four tag families on one storefront | sidsfarm.com page source | [https://sidsfarm.com](https://sidsfarm.com) | Ctrl+F for GTM-57TDVNH, GTM-P4DXD97J, G-YN4FLEL9J2 and connect.facebook.net — all four appear. |
| Seven storefront paths return 404 | sidsfarm.com — the URLs themselves | [https://sidsfarm.com/pages/faq](https://sidsfarm.com/pages/faq) | Try /pages/faq, /pages/contact, /policies/shipping-policy, /pages/store-locator — each returns 404. |
| wecare@sidsfarm.com | sidsfarm.com — cart and collection pages | [https://sidsfarm.com/collections/all](https://sidsfarm.com/collections/all) | Published in the footer of the storefront pages. |
| Bengaluru is a served market | sidsfarm.com — the location selector and homepage copy | [https://sidsfarm.com](https://sidsfarm.com) | The 'Select Location' control lists Bangalore, and the homepage reads 'If you're from Hyderabad, Bengaluru, Pune, Vijayawada …'. |

### Barbeque Nation

Site: `barbequenation.com` · measured 3 October 2026

| Claim in the audit | Where to check it | Link | What you should see |
|---|---|---|---|
| 19 creatives in the advertiser account | Google Ads Transparency Center — advertiser page | [https://adstransparency.google.com/advertiser/AR07883744464190046209?region=IN](https://adstransparency.google.com/advertiser/AR07883744464190046209?region=IN) | The header reads '19 ads' under UNITED FOODBRANDS LIMITED (Verified). |
| 34 creatives point at the domain — 15 more than the account holds | Google Ads Transparency Center — domain view | [https://adstransparency.google.com/?region=IN&domain=barbequenation.com](https://adstransparency.google.com/?region=IN&domain=barbequenation.com) | The domain view header reads '34 ads', and Google notes the domain includes results for multiple advertiser accounts. |
| Meta creative library ID 1629049651915814 (SAVE35 takeaway offer) | Meta Ad Library — the ad itself | [https://www.facebook.com/ads/library/?id=1629049651915814](https://www.facebook.com/ads/library/?id=1629049651915814) | Barbeque Nation's own page, running since 13 September 2026, 'FLAT 35% OFF on Takeaway Orders' with code SAVE35, landing /ubq-delivery. |
| Meta creative library ID 1595578738733856 (pay-day buffet, valid to 11 October 2026) | Meta Ad Library — the ad itself | [https://www.facebook.com/ads/library/?id=1595578738733856](https://www.facebook.com/ads/library/?id=1595578738733856) | The pay-day offer ad, running since 22 September 2026, landing /deals/unlockspecialdeals. |
| GTM-TF3NNN · Meta pixel · Razorpay | barbequenation.com page source | [https://barbequenation.com](https://barbequenation.com) | Ctrl+F each string in view source — the container ID, connect.facebook.net and Razorpay references all appear. |
| /menu, /book-a-table, /locations, /order-online, /terms return 404 | barbequenation.com — the URLs themselves | [https://barbequenation.com/menu](https://barbequenation.com/menu) | Each returns 404, while the ad destinations /ubq-delivery and /deals/unlockspecialdeals load. |
| feedback@barbequenation.com | barbequenation.com — About-Us and Contact-Us pages | [https://barbequenation.com/contact-us](https://barbequenation.com/contact-us) | Published on the contact page, with the registered office address in Bengaluru 560035 and the number 08064058059. |
| Two different legal names — the site's and the advertiser's | barbequenation.com footer vs Google Ads Transparency | [https://adstransparency.google.com/advertiser/AR07883744464190046209?region=IN](https://adstransparency.google.com/advertiser/AR07883744464190046209?region=IN) | The site names Barbeque Nation Hospitality Limited; Google's advertiser of record is the parent, UNITED FOODBRANDS LIMITED. |

### Millet Amma

Site: `milletamma.com` · measured 3 October 2026

| Claim in the audit | Where to check it | Link | What you should see |
|---|---|---|---|
| 80 live Google creatives | Google Ads Transparency Center — advertiser page | [https://adstransparency.google.com/advertiser/AR06400845011688095745?region=IN](https://adstransparency.google.com/advertiser/AR06400845011688095745?region=IN) | The header reads '80 ads' under URBAN MONK PRIVATE LIMITED (Verified). |
| The legal entity on the site matches the verified advertiser | milletamma.com — terms and conditions page | [https://milletamma.com/policies/terms-of-service](https://milletamma.com/policies/terms-of-service) | The footer reads 'Copyright © 2026 URBAN MONK PRIVATE LIMITED, All Rights Reserved.' |
| The archived local-ad creative and its removal notice | Google Ads Transparency Center — the creative itself | [https://adstransparency.google.com/advertiser/AR06400845011688095745/creative/CR03268659855321202689?region=IN](https://adstransparency.google.com/advertiser/AR06400845011688095745/creative/CR03268659855321202689?region=IN) | Google's archive shows 'Last shown: Jul 15, 2026' and 'Removed for a policy violation' on this local ad, with the template text '{KeyWord:Millet Amma}' still visible. |
| Meta creative library ID 1355783896518419 (Ragi Laddoo, since 7 July 2026) | Meta Ad Library — the ad itself | [https://www.facebook.com/ads/library/?id=1355783896518419](https://www.facebook.com/ads/library/?id=1355783896518419) | On the Millet Amma page, landing milletamma.com/products/ragi-laddo-300g. |
| Two GA4 properties live at once | milletamma.com page source | [https://milletamma.com](https://milletamma.com) | Ctrl+F for G-WH82716CE0 and G-N659GJMWCX — both appear in the same page source, alongside AW-378561932. |
| The site-wide sale banner | milletamma.com — any storefront page | [https://milletamma.com](https://milletamma.com) | The announcement bar reads 'Our Biggest Sale Yet: Up To 20% Off + Free Prepaid Shipping.' |
| eatright@milletamma.com · orders@milletamma.com · +91 7624979333 | milletamma.com — cart, collection and terms pages | [https://milletamma.com/cart](https://milletamma.com/cart) | eatright@ appears on the cart and collection pages; orders@ appears on the terms-of-service page; the phone number appears in the storefront. |
| The Bengaluru address | milletamma.com — the 'Get in touch' block on the cart page | [https://milletamma.com/cart](https://milletamma.com/cart) | Reads No. 12, K 345, Yemalur Main Road, HAL Airport Area, Bellandur, Bengaluru, Karnataka 560037. |

### Adukale

Site: `adukale.com` · measured 3 October 2026

| Claim in the audit | Where to check it | Link | What you should see |
|---|---|---|---|
| 13 live Google creatives | Google Ads Transparency Center (region: India) — domain view | [https://adstransparency.google.com/?region=IN&domain=adukale.com](https://adstransparency.google.com/?region=IN&domain=adukale.com) | The header reads '13 ads' under SANKETHI NUTRIMENTS PRIVATE LIMITED (Verified), including a Product Listing Ad titled 'Buy Rice Idli | Healthy Breakfast | Adukale'. |
| The Amazon routing announcement | adukale.com — home and cart pages | [https://adukale.com](https://adukale.com) | The announcement bar reads 'All purchases from this site will now be completed through Amazon. Enjoy the same authentic taste with greater ease.' |
| The placeholder pickup address on the live site | adukale.com — home or collection pages | [https://adukale.com](https://adukale.com) | Ctrl+F for '123 John Doe' — the pickup block shows '123 John Doe Street, Your Town, YT 12345' next to the real pickup point at 155 Madappa Building, Mallathalli. |
| The email icon that is not a mailto link | adukale.com — page source | [https://adukale.com](https://adukale.com) | Ctrl+F for 'href="info@adukale.com"' — the address is correct and visible; the link around the icon has no mailto: prefix. |
| Three Shopping variations with Google's removal notice | Google Ads Transparency Center — the ad itself | [https://adstransparency.google.com/advertiser/AR18362132152826462209/creative/CR11719898640389505025?region=IN](https://adstransparency.google.com/advertiser/AR18362132152826462209/creative/CR11719898640389505025?region=IN) | The ad detail page shows 'Last shown: Nov 28, 2025' and 'Removed for a policy violation' on all three variations (Sambar Powder, Chutney Powder 200g, Kayi Kodubale 180g). |
| Two GA4 properties and one Ads tag | adukale.com page source | [https://adukale.com](https://adukale.com) | Ctrl+F for G-X6WD89C59X, G-66YCE4PEZM and AW-812528734 — all three appear. |
| No Meta ads active for the brand term | Meta Ad Library (country: India, active ads) | [https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=IN&q=Adukale&search_type=keyword_unordered](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=IN&q=Adukale&search_type=keyword_unordered) | The page shows 'No ads match your search criteria' for this term. |
| info@adukale.com · +91 9035462696 | adukale.com — cart and collection pages | [https://adukale.com/cart](https://adukale.com/cart) | Published in the storefront, with the Bengaluru 560091 address (Sankethi Nutriments Pvt. Ltd, Kannahalli Village) and a helpdesk window of 8AM–8PM, Mon–Sun. |

### Organic Mandya

Site: `organicmandya.com` · measured 3 October 2026

| Claim in the audit | Where to check it | Link | What you should see |
|---|---|---|---|
| 69 creatives in the advertiser account | Google Ads Transparency Center — advertiser page | [https://adstransparency.google.com/advertiser/AR08930861279116001281?region=IN](https://adstransparency.google.com/advertiser/AR08930861279116001281?region=IN) | The header reads '69 ads' under MANDYA ORGANIC FOODS PRIVATE LIMITED (Verified). |
| 67 creatives point at organicmandya.com | Google Ads Transparency Center — domain view | [https://adstransparency.google.com/?region=IN&domain=organicmandya.com](https://adstransparency.google.com/?region=IN&domain=organicmandya.com) | The domain view header reads '67 ads'. |
| The two-hour delivery promise | organicmandya.com — the announcement bar | [https://organicmandya.com](https://organicmandya.com) | The bar reads '2-hr delivery in Bengaluru, Hyderabad & Mysuru — ₹49 delivery charge on orders under ₹500, FREE above ₹500'. |
| Meta creative library ID 1432155482101394 (since 13 September 2026) | Meta Ad Library — the ad itself | [https://www.facebook.com/ads/library/?id=1432155482101394](https://www.facebook.com/ads/library/?id=1432155482101394) | On the Organic Mandya page, landing the millet-upma collection. |
| Custom dataLayer event names and GA4 G-MHKC4DNNH3 | organicmandya.com page source | [https://organicmandya.com](https://organicmandya.com) | Ctrl+F for gtm-promo, gtm-creative, gtm-position and G-MHKC4DNNH3 — all appear, alongside AW-16535163896. |
| /pages/faq, /pages/bulk-enquiry and /pages/corporate-gifting return 404 | organicmandya.com — the URLs themselves | [https://organicmandya.com/pages/faq](https://organicmandya.com/pages/faq) | Each returns 404. |
| support@organicmandya.com · +91 9590922000 | organicmandya.com — cart and collection pages | [https://organicmandya.com/cart](https://organicmandya.com/cart) | Published in the storefront; the phone number is also in the announcement bar. |

### Pure & Sure

Site: `pureandsure.in` · measured 3 October 2026

| Claim in the audit | Where to check it | Link | What you should see |
|---|---|---|---|
| 37 live Google creatives | Google Ads Transparency Center (region: India) — domain view | [https://adstransparency.google.com/?region=IN&domain=pureandsure.in](https://adstransparency.google.com/?region=IN&domain=pureandsure.in) | The header reads '37 ads' under Phalada Organic Consumer Products Private Limited (Verified). |
| The 'sag_organic' campaign tag on paid Shopping clicks | Google Ads Transparency Center — the advertiser page, then an ad's destination URL | [https://adstransparency.google.com/advertiser/AR04550905857457520641?region=IN](https://adstransparency.google.com/advertiser/AR04550905857457520641?region=IN) | The organic ghee ad's landing URL ends with utm_medium=product_sync&utm_source=google&utm_campaign=sag_organic. |
| GA4 G-VGC836EHVF · GTM-KP8NPFKZ · AW-16785598661 · Meta pixel | pureandsure.in page source | [https://pureandsure.in](https://pureandsure.in) | Ctrl+F each ID — all four appear. |
| Free shipping above ₹500 | pureandsure.in — site banner | [https://pureandsure.in](https://pureandsure.in) | The banner reads 'Free Shipping on orders above ₹500'. |
| /pages/contact-us returns 404 while /pages/contact works | pureandsure.in — the URLs themselves | [https://pureandsure.in/pages/contact](https://pureandsure.in/pages/contact) | Try both: /pages/contact loads, /pages/contact-us returns 404. |
| info@pureandsure.in · care@pureandsure.in · 1800 121 0369 | pureandsure.in — contact, shipping-policy, cart pages | [https://pureandsure.in/pages/contact](https://pureandsure.in/pages/contact) | info@ is on the contact and shipping pages; care@ is on the cart and collection pages. |
| The Bengaluru registered address | pureandsure.in — footer of the cart and collection pages | [https://pureandsure.in/cart](https://pureandsure.in/cart) | Reads Phalada Organic Consumer Products Pvt Ltd, 92/5, Kannalli Village, Seegehalli, Magadi Main Road, Bangalore 560091. |

### Eat Better Co

Site: `eatbetterco.com` · measured 3 October 2026

| Claim in the audit | Where to check it | Link | What you should see |
|---|---|---|---|
| 29 creatives live for the domain; 27 in the advertiser account | Google Ads Transparency Center — domain and advertiser views | [https://adstransparency.google.com/?region=IN&domain=eatbetterco.com](https://adstransparency.google.com/?region=IN&domain=eatbetterco.com) | The domain view reads '29 ads'; the advertiser page (EAT BETTER VENTURES PRIVATE LIMITED, Verified) reads '27 ads'. |
| Discount values as low as −1%, −2% and −6% in the Shopping feed | Google Ads Transparency Center — the advertiser page | [https://adstransparency.google.com/advertiser/AR17084581177009897473?region=IN](https://adstransparency.google.com/advertiser/AR17084581177009897473?region=IN) | The Product Listing Ad titles carry the discount badges, landing on /products/ URLs with variant parameters. |
| GA4 G-90QE4TSKTH · Google Ads AW-610414449 | eatbetterco.com page source | [https://eatbetterco.com](https://eatbetterco.com) | Ctrl+F both IDs — they appear. |
| Published shipping terms (free above ₹500, prepaid ₹49, COD ₹79, 3 working days) | eatbetterco.com — shipping policy and FAQ | [https://eatbetterco.com/policies/shipping-policy](https://eatbetterco.com/policies/shipping-policy) | The policy page states the thresholds; the contact page states the 3-working-day delivery window. |
| care@eatbetterco.com (contact/refund pages) and connect@gottaeatbetter.com (privacy/shipping pages) | eatbetterco.com — policy pages | [https://eatbetterco.com/policies/privacy-policy](https://eatbetterco.com/policies/privacy-policy) | Each address appears on the pages named; the company name in the site title is 'Eat Better Co - As seen on Shark Tank'. |
| Five storefront paths return 404 | eatbetterco.com — the URLs themselves | [https://eatbetterco.com/pages/faq](https://eatbetterco.com/pages/faq) | Try /pages/faq, /pages/about-us, /pages/contact, /pages/store-locator, /pages/bulk-enquiry — each returns 404, while /pages/contact-us works. |
| The Jaipur registered address (the Bengaluru-relevance note) | eatbetterco.com — contact page | [https://eatbetterco.com/pages/contact-us](https://eatbetterco.com/pages/contact-us) | Reads Eat Better Ventures Pvt Ltd, A1/A2, Vastushree Colony, 100 Feet Road, Manyawas, Mansarovar, Jaipur, Rajasthan 302020 — which is why this lead is labelled pan-India rather than Bengaluru-based. |
| The corporate-gifting figures quoted in this audit | eatbetterco.com — corporate gifting page | [https://eatbetterco.com/pages/corporate-gifting](https://eatbetterco.com/pages/corporate-gifting) | The page states '10 LAKH+ hampers delivered pan-India', '500+ corporates & organizations' and '25 hampers designs this Diwali', with hampers from ₹249 to ₹2,499. |

### Brik Oven

Site: `brikoven.com` · measured 3 October 2026

| Claim in the audit | Where to check it | Link | What you should see |
|---|---|---|---|
| 42 creatives in the advertiser account | Google Ads Transparency Center — advertiser page | [https://adstransparency.google.com/advertiser/AR15322972474807681025?region=IN](https://adstransparency.google.com/advertiser/AR15322972474807681025?region=IN) | The header reads '42 ads' under Brik Oven Pvt Ltd (Verified). |
| 25 creatives point at brikoven.com | Google Ads Transparency Center — domain view | [https://adstransparency.google.com/?region=IN&domain=brikoven.com](https://adstransparency.google.com/?region=IN&domain=brikoven.com) | The domain view header reads '25 ads', and the visible set is Local store ads for Palace Road, Whitefield, Koramangala and Manyata Business Park. |
| The third-party reservation widget on a live local ad | Google Ads Transparency Center — the advertiser page | [https://adstransparency.google.com/advertiser/AR15322972474807681025?region=IN](https://adstransparency.google.com/advertiser/AR15322972474807681025?region=IN) | The Manyata Business Park local ad in this account shows 'Book now • widget.reservego.co/' as its call to action. |
| The stopped store creative | Google Ads Transparency Center — the creative itself | [https://adstransparency.google.com/advertiser/AR15322972474807681025/creative/CR16763555951004352513?region=IN](https://adstransparency.google.com/advertiser/AR15322972474807681025/creative/CR16763555951004352513?region=IN) | Google's archive states 'Last shown: Jul 23, 2026' for the Palace Road breakfast creative. |
| GTM-PMCQMP4 · GA4 G-6HE7Y2G8N3 · Squarespace | brikoven.com page source | [https://brikoven.com](https://brikoven.com) | Ctrl+F each — the container ID, measurement ID and Squarespace assets all appear. |
| theteam@brikoven.com | brikoven.com — contact block | [https://brikoven.com](https://brikoven.com) | Published in the site's contact block next to the social links. |
| The four Bengaluru outlets | brikoven.com — the Locations block on the home page | [https://brikoven.com](https://brikoven.com) | Lists Church Street (560001), Indiranagar (560038), Palace Road (560001) and Koramangala (560034), each with its own phone number. |
| Eight conventional paths return 404 | brikoven.com — the URLs themselves | [https://brikoven.com/contact-us](https://brikoven.com/contact-us) | Try /contact-us, /menu, /book-a-table, /locations, /order-online — each returns 404. |

### Araku Coffee

Site: `arakucoffee.in` · measured 3 October 2026

| Claim in the audit | Where to check it | Link | What you should see |
|---|---|---|---|
| ≈200 live Google creatives | Google Ads Transparency Center (region: India) — domain view | [https://adstransparency.google.com/?region=IN&domain=arakucoffee.in](https://adstransparency.google.com/?region=IN&domain=arakucoffee.in) | The header reads approximately 200 ads under Araku Originals Pvt Ltd (Verified). |
| Shopping ads running with 'sag_organic' campaign tagging | Google Ads Transparency Center — the advertiser page | [https://adstransparency.google.com/advertiser/AR16285151475322060801?region=IN](https://adstransparency.google.com/advertiser/AR16285151475322060801?region=IN) | Product Listing Ads for the Moka Pot and the Chemex land on product URLs whose tracking ends with utm_campaign=sag_organic. |
| Local ads for the café alongside store product ads | Google Ads Transparency Center — the advertiser page | [https://adstransparency.google.com/advertiser/AR16285151475322060801?region=IN](https://adstransparency.google.com/advertiser/AR16285151475322060801?region=IN) | The account shows a local 'ARAKU Coffee' listing with Directions/Reserve CTAs together with Shopping ads for equipment. |
| GA4 G-L4DG6J5D15 · AW-11305512148 · Razorpay | arakucoffee.in page source | [https://arakucoffee.in](https://arakucoffee.in) | Ctrl+F each string — the IDs and the Razorpay reference appear. |
| customercare@arakuoriginals.com · +91 9000394000 | arakucoffee.in — site footer | [https://arakucoffee.in](https://arakucoffee.in) | Both appear in the footer, next to '© Araku Originals Pvt Ltd., 2026'. |
| The Bangalore flagship and training campus | arakucoffee.in — homepage copy and meta description | [https://arakucoffee.in](https://arakucoffee.in) | The page reads 'India's first premier SCA training campus … now in the heart of Bangalore', and the meta description names flagships in Mumbai, Bangalore & Paris. |
| Meta results for the brand term include other businesses | Meta Ad Library (country: India) | [https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=IN&q=Araku Coffee&search_type=keyword_unordered](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=IN&q=Araku Coffee&search_type=keyword_unordered) | The first page shows third-party placements (for example a Siemens Home workshop featuring Araku Coffee) rather than brand-owned creatives. |

---

If any value above no longer matches what you see, that is expected for live ad inventory — campaign counts move daily. Re-run the check and note the new value: the audits are dated snapshots by design.
