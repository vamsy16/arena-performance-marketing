# -*- coding: utf-8 -*-
"""
Verification guide builder.

Produces VERIFY-THE-DATA.md — for every claim in the 11 audits, the exact public
surface where you can check it yourself, with the value you should expect to see.

Nothing here is generated from estimates: each row names a live URL plus the value
that was observed on 2 October 2026. Where a claim cannot be checked by a third
party (spend, ROAS, CPA), the row says so.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATE = "2 October 2026"

G  = "https://adstransparency.google.com/?region=IN&domain={d}"          # Google, India
ML = "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=IN&q={q}&search_type=keyword_unordered"
MID = "https://www.facebook.com/ads/library/?id={i}"                      # a specific Meta ad
SRC = "https://{d}"                                                       # view-source

# ---------------------------------------------------------------------------
# claim, where to check (surface), exact link, expected result
# ---------------------------------------------------------------------------
ROWS = {
"licious": [
 ("≈300 live Google creatives", "Google Ads Transparency Center (region: India)", G.format(d="licious.in"), "The page header reads approximately 300 ads, under Delightful Gourmet Pvt Ltd (Verified)."),
 ("≈550 live Meta ads", "Meta Ad Library (country: India)", ML.format(q="Licious"), "Around 550 results for the brand term."),
 ("Meta library ID 983369480870934", "Meta Ad Library — the ad itself", MID.format(i="983369480870934"), "The specific Licious ad referenced in the audit, with its running-since date."),
 ("GTM-KVBCJN · GA4 G-YN0TX18PEE · Ads AW-871318622", "licious.in page source", SRC.format(d="licious.in"), "Open the page, press Ctrl+U (view source), then Ctrl+F each ID. All four appear, including Meta pixel 378591842535023."),
 ("FY25 revenue ≈Rs 795 Cr, loss ≈Rs 218.3 Cr", "licious.in — published company results", "https://www.licious.in/", "Published in the company's reported FY25 results. This is a third-party reported figure, quoted as reported."),
 ("talktous@licious.com", "licious.in support / contact page", "https://www.licious.in/", "Publish in the site's contact or help section."),
],
"akshayakalpa-organic": [
 ("≈400 live Google creatives", "Google Ads Transparency Center (region: India)", G.format(d="akshayakalpa.org"), "Around 400 creatives — the largest paid footprint in this set."),
 ("3 live Meta creatives from the brand page", "Meta Ad Library (country: India)", ML.format(q="Akshayakalpa"), "Three creatives from the Akshayakalpa page; the audit cites their running-since dates."),
 ("Meta IDs 2186726058790625 · 935934206094801 · 958522520368361", "Meta Ad Library — individual ads", MID.format(i="935934206094801"), "Opens the creative running since 19 May 2026. Swap the id for either of the other two."),
 ("Swiggy Instamart runs Akshayakalpa product creative", "Meta Ad Library", MID.format(i="3384075765110108"), "A Swiggy Instamart placement featuring Akshayakalpa paneer, 9 variants. This is third-party distribution, not the brand's own account."),
 ("Contact Us page shows '0123.456.789 - 2 Queen Street, California'", "akshayakalpa.org/contact-us", "https://akshayakalpa.org/contact-us", "The placeholder text sits at the top of the Contact Us page. Note the contrast: the homepage footer carries the correct Tiptur, Karnataka address, which is why the audit names the exact page."),
 ("No cache-control, no HSTS", "Response headers of akshayakalpa.org", "https://securityheaders.com/?q=akshayakalpa.org", "Or from a terminal: curl -I https://akshayakalpa.org — neither header comes back."),
 ("support@akshayakalpa.org", "akshayakalpa.org FAQ and privacy policy", "https://akshayakalpa.org/", "The only official address the brand publishes."),
],
"anand-sweets": [
 ("58 live Google creatives", "Google Ads Transparency Center (region: India)", G.format(d="anandsweets.in"), "Around 58 creatives."),
 ("OpenAI ads pixel MsnBMqKgkHz42jqdSfTfFQ", "anandsweets.in page source", SRC.format(d="anandsweets.in"), "Ctrl+U then Ctrl+F 'MsnBMqKgkHz42jqdSfTfFQ' — the OpenAI advertising pixel is in the storefront source."),
 ("HSTS, CSP, X-Frame-Options all present", "Response headers", "https://securityheaders.com/?q=anandsweets.in", "All four header families return a pass — the strongest posture in this set."),
 ("4.4 rating from 250 reviews", "anandsweets.in structured data", SRC.format(d="anandsweets.in"), "Ctrl+F 'aggregateRating' in the page source."),
 ("care@anandsweets.net", "anandsweets.in footer / contact", "https://www.anandsweets.in/", "Published in the site footer."),
],
"chai-point": [
 ("56 live Google creatives", "Google Ads Transparency Center (region: India)", G.format(d="chaipoint.com"), "Around 56 creatives, under Mountain Trail Foods."),
 ("GA4 G-EN77D2S0YH on the site root", "chaipoint.com page source", SRC.format(d="chaipoint.com"), "Ctrl+U then Ctrl+F 'G-EN77D2S0YH'."),
 ("900,000+ cups a day · 150+ stores · 8,100+ workplaces", "chaipoint.com structured data (JSON-LD)", SRC.format(d="chaipoint.com"), "Ctrl+F 'cups' or '900' in the page source; the figures are in the machine-readable JSON-LD block."),
 ("Static build on Amazon S3 + CloudFront", "Response headers", "https://securityheaders.com/?q=chaipoint.com", "Server headers show cloudfront and S3 asset hosting."),
 ("customercare@chaipoint.com", "Chai Point help centre", "https://shop.chaipoint.com/", "Published on the order site's help section."),
],
"the-baker-s-dozen": [
 ("35 live Google creatives", "Google Ads Transparency Center (region: India)", G.format(d="thebakersdozen.in"), "Around 35 creatives."),
 ("GTM-MQQF2MXB · Ads AW-618150299", "thebakersdozen.in page source", SRC.format(d="thebakersdozen.in"), "Ctrl+F each ID in the page source."),
 ("Meta pixel 3996239487069441", "thebakersdozen.in page source", SRC.format(d="thebakersdozen.in"), "Ctrl+F '3996239487069441'."),
 ("No HSTS, no cache-control, no security headers", "Response headers", "https://securityheaders.com/?q=thebakersdozen.in", "Most or all headers return a fail."),
 ("fresh@thebakersdozen.in", "thebakersdozen.in/contact-us", "https://thebakersdozen.in/contact-us", "Published on the contact page."),
],
"cothas-coffee": [
 ("77 live Google creatives", "Google Ads Transparency Center (region: India)", G.format(d="cothas.com"), "Around 77 creatives, under Freeflow Creative Services."),
 ("Tag layer unconfirmed", "Chrome DevTools on cothas.com", SRC.format(d="cothas.com"), "This is the one claim you can settle in a browser: open DevTools → Network, filter 'collect' or 'gtm', and reload. If tags fire, the audit's 'unconfirmed' wording is exactly right — and the fix is simply to confirm it."),
 ("customercare@cothas.com", "cothas.com/pages/contact-us", "https://cothas.com/pages/contact-us", "Published on the contact page."),
 ("Founded 1948, Jigani facility", "Cothas Coffee — own pages", "https://cothas.com/", "Stated on the brand's own site."),
],
"early-foods": [
 ("30 live Google creatives", "Google Ads Transparency Center (region: India)", G.format(d="earlyfoods.com"), "Around 30 creatives."),
 ("Shopify theme 124761112618 behind Cloudflare", "Response headers + page source", SRC.format(d="earlyfoods.com"), "Cloudflare reported in the server headers; the theme ID appears in the storefront source."),
 ("hello@earlyfoods.com", "earlyfoods.com", "https://earlyfoods.com/", "Published on the site."),
],
"id-fresh-food": [
 ("1 live Google creative", "Google Ads Transparency Center (region: India)", G.format(d="idfreshfood.com"), "A single creative — the finding that drives this audit."),
 ("Access-Control-Allow-Origin: *", "Response headers", "https://securityheaders.com/?q=idfreshfood.com", "Or: curl -I https://idfreshfood.com — the wildcard CORS header is returned."),
 ("LiteSpeed cache HIT", "Response headers", "https://securityheaders.com/?q=idfreshfood.com", "The cache header reports a hit, confirming the cache layer works."),
 ("customercare@idfreshfood.com", "idfreshfood.com/contact-us", "https://idfreshfood.com/contact-us", "Published on the contact page."),
 ("FY25 revenue ≈Rs 681.4 Cr, PAT ≈Rs 25.87 Cr", "Published FY25 results as reported", "https://idfreshfood.com/", "Figures are quoted as reported, not audited by us."),
],
"third-wave-coffee": [
 ("Title tag is the domain string", "thirdwavecoffeeroasters.com page source", SRC.format(d="thirdwavecoffeeroasters.com"), "Ctrl+U and look at the first line inside <head>: the title reads 'www.thirdwavecoffeeroasters.com' instead of the brand name."),
 ("0 live Google creatives", "Google Ads Transparency Center (region: India)", G.format(d="thirdwavecoffeeroasters.com"), "No creatives are returned for the domain. The audit states this as measured on one day for this domain, not as a claim about the whole account."),
 ("orders@thirdwavecoffee.in", "thirdwavecoffee.in/pages/contact", "https://thirdwavecoffee.in/pages/contact", "Published on the contact page."),
],
"frozen-bottle": [
 ("11 live Google creatives", "Google Ads Transparency Center (region: India)", G.format(d="frozenbottle.com"), "Around 11 creatives."),
 ("A stale FAQ URL returns 404", "frozenbottle.com/pages/faq vs the live /pages/faqs", "https://frozenbottle.com/pages/faq", "The singular URL returns 'not found'. The working FAQ is the plural one: frozenbottle.com/pages/faqs — the audit states both, so you can see exactly what is and is not broken."),
 ("vipul@frozenbottle.in", "frozenbottle.com footer (partnership section)", "https://frozenbottle.com/", "Published under collaboration and partnership in the footer."),
],
"milky-mist": [
 ("3 live Google creatives", "Google Ads Transparency Center (region: India)", G.format(d="milkymist.com"), "Around 3 creatives."),
 ("Wix behind Varnish", "Response headers", "https://securityheaders.com/?q=milkymist.com", "Server headers show Varnish and Wix identifiers."),
 ("customercare@milkymist.com", "milkymist.com/reach-us", "https://milkymist.com/reach-us", "Published on the reach-us page."),
],
}

NOT_VERIFIABLE = [
 ("Ad spend (Rs/month)", "No public source exists. Ad platforms do not disclose spend for commercial advertisers."),
 ("ROAS and CPA", "Only visible inside the advertiser's own ad accounts and analytics."),
 ("Conversion rates", "Private to the advertiser."),
 ("Internal revenue splits by channel", "Private to the advertiser."),
]

HEAD = """# Verify the data — every claim, and where to check it

Every number in the 11 audits came from a public surface that you (or the lead) can open.
This file maps each claim to the exact place it was read on **{date}**.

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
{notverifiable}

---

## Per-lead checklists

"""


def main():
    out = ROOT / "VERIFY-THE-DATA.md"
    body = [HEAD.format(date=DATE,
                        notverifiable="\n".join(f"| {a} | {b} |" for a, b in NOT_VERIFIABLE))]
    from evidence_data import E
    for slug, lead in E.items():
        body.append(f"### {lead['brand']}\n")
        body.append(f"Site: `{lead['prepared_for_line'].split('·')[0].strip()}` · "
                    f"measured {DATE}\n")
        body.append("| Claim in the audit | Where to check it | Link | What you should see |")
        body.append("|---|---|---|---|")
        for claim, where, link, expect in ROWS[slug]:
            body.append(f"| {claim} | {where} | [{link}]({link}) | {expect} |")
        body.append("")
    body.append("---\n")
    body.append("If any value above no longer matches what you see, that is expected for live ad "
                "inventory — campaign counts move daily. Re-run the check and note the new value: "
                "the audits are dated snapshots by design.\n")
    out.write_text("\n".join(body), encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size/1024:.0f} KB)")
    return ROWS


if __name__ == "__main__":
    main()
