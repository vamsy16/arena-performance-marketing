# Solar Audit Checklist (20 minutes per lead)

Copy this into a new file per lead, or just fill the JSON that
`scripts/solar_lead_finder.py` already wrote in `niches/solar/leads/<brand>.json`.

**Brand:** ______________________  **Segment:** R / C / B / P
**City / State:** ________________  **Date audited:** ____________
**Segment ads verified in Meta Ad Library?** YES / NO  (if NO — do not send anything)

---

## A. Ads (Meta Ad Library India, active filter)

- [ ] Live creative count: ______ (screenshot the count)
- [ ] Oldest running creative: ______ days
- [ ] Primary CTA used: WhatsApp / Call / Form / Website
- [ ] Does any creative mention the subsidy number? YES / NO
- [ ] Install photos or customer video present? YES / NO
- [ ] Language of creative (English / Hinglish / regional): ____________
- [ ] Google Ads Transparency (`adstransparency.google.com`): ______ ads

## B. Landing / lead capture

- [ ] Subsidy (₹78,000 / 300 free units) above the fold? YES / NO
- [ ] Savings calculator present and visible on first screen? YES / buried / NO
- [ ] Number of form fields: ______ (target ≤ 3: city, phone, monthly bill)
- [ ] Click-to-WhatsApp on the page? YES / NO
- [ ] EMI / financing visible? YES / NO
- [ ] Mobile load time (4G): ______ s (target < 2.5s)
- [ ] Google rating + review count shown? ______ / ______
- [ ] City-wise landing pages? YES / NO
- [ ] Copyright/footer year current? (stale footer = trust leak)

## C. Follow-up mechanics

- [ ] WhatsApp auto-greeting? YES / NO
- [ ] Package catalogue in WhatsApp Business? YES / NO
- [ ] Reply speed tested (send a test enquiry): ______ min (target < 5)
- [ ] Any follow-up after no reply? YES / NO
- [ ] Site-survey booking flow (calendar / slot / "we'll call you")?

## D. Tracking & retargeting

- [ ] Meta Pixel firing? (Events Manager / pixel helper) YES / NO / can't verify
- [ ] Conversions API (server-side) YES / NO / unknown
- [ ] Google Ads conversion tag YES / NO / unknown
- [ ] WhatsApp / call tracking on ads YES / NO
- [ ] Retargeting audiences live (video 50%, site visitors, form abandoners) YES / NO
- [ ] 30–90 day nurture sequence for the solar decision cycle YES / NO

## E. Verdict

- [ ] Top 3 leaks: 1) ____________________ 2) ____________________ 3) ____________________
- [ ] Lead score /10: ______   ·  pitch_fit: HIGH / MEDIUM / LOW
- [ ] The single line I will open the outreach with: ______________________________
- [ ] Audit PDF generated? `python scripts/solar_audit.py niches/solar/leads/<brand>.json`

---

### Compliance reminder

Never state or imply guaranteed subsidy approval, amount or timeline. Never present
yourself as an MNRE / DISCOM / government representative. Quote only numbers you saw.
