#!/usr/bin/env python3
"""Render the source-checked batch-3 Food/Bengaluru deliverables.

This is intentionally an incremental pack updater. It does NOT call the legacy
build_master_excel.py (which reconstructs only batches 1–2 from old mappings).
Run from anywhere with the repository .venv active:
    python niches/food-bengaluru/scripts/build_batch3_deliverables.py
"""
from __future__ import annotations

import csv
import html
import json
import re
import shutil
import unicodedata
from collections import Counter
from copy import copy
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
DATA_FILE = ROOT / "data" / "batch3_records.json"
WORKBOOK = ROOT / "Food-Bangalore-ALL-IN-ONE.xlsx"
EMAIL_WORKBOOK = ROOT / "Food-Bangalore-EMAILS-ONE-SHEET.xlsx"
BATCH3_EMAIL_WORKBOOK = ROOT / "Food-Bangalore-BATCH-3-EMAILS.xlsx"
EMAIL_CSV = ROOT / "Food-Bangalore-EMAILS-ONE-SHEET.csv"
LEADS_CSV = ROOT / "LEADS-INDEX.csv"
VERIFY_MD = ROOT / "VERIFY-THE-DATA.md"
README_MD = ROOT / "README.md"
ALL_EMAILS_MD = ROOT / "ALL-EMAIL-SEQUENCES.md"
REGISTRY = REPO / "data" / "seen_leads.json"

NAVY = "0B1B2B"
NAVY_2 = "10263A"
TEAL = "0E7C7B"
GOLD = "F0A500"
PANEL = "F4F7FA"
RULE = "E8EDF3"
MUTED = "64748B"
INK = "172533"
WHITE = "FFFFFF"

LEGACY_BATCH1 = {
    "Licious", "Cothas Coffee", "Anand Sweets", "Chai Point",
    "The Baker's Dozen", "Early Foods", "iD Fresh Food",
    "Third Wave Coffee", "Akshayakalpa Organic", "Milky Mist", "Frozen Bottle",
}
LEGACY_BATCH2 = {
    "SMOOR", "Sid's Farm", "Barbeque Nation", "Millet Amma", "Adukale",
    "Organic Mandya", "Pure & Sure", "Eat Better Co", "Brik Oven", "Araku Coffee",
}


def norm_name(value: str) -> str:
    value = unicodedata.normalize("NFKD", str(value)).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", value.casefold())


def norm_domain(value: str) -> str:
    raw = str(value or "").strip()
    if not raw:
        return ""
    if "://" not in raw:
        raw = "https://" + raw
    host = (urlparse(raw).hostname or "").casefold()
    return host[4:] if host.startswith("www.") else host


def vintage_for(brand: str) -> str:
    key = norm_name(brand)
    for b in LEGACY_BATCH1:
        if norm_name(b) == key:
            return "LEGACY — Batch 1; prior snapshot, not revalidated on 04 OCT 2026"
    for b in LEGACY_BATCH2:
        if norm_name(b) == key:
            return "LEGACY — Batch 2; prior snapshot, not revalidated on 04 OCT 2026"
    return "BATCH 3 — source-checked 04 OCT 2026"


def load_data():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Missing source file: {DATA_FILE}")
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    leads = data.get("leads", [])
    assert data.get("batch") == 3, "Expected batch 3 input"
    assert len(leads) == 10, f"Expected 10 leads; found {len(leads)}"
    assert len({x["slug"] for x in leads}) == len(leads), "Duplicate slugs in batch input"
    assert len({norm_name(x["brand"]) for x in leads}) == len(leads), "Duplicate brands in batch input"
    for lead in leads:
        assert lead.get("contact_source"), f"Missing contact provenance: {lead['brand']}"
        assert len(lead.get("outreach", [])) == 4, f"Expected four emails: {lead['brand']}"
        assert len(lead.get("findings", [])) >= 1, f"No findings: {lead['brand']}"
        assert len(lead.get("score_breakdown", [])) == 5, f"Score must have five dimensions: {lead['brand']}"
        assert sum(int(x["score"]) for x in lead["score_breakdown"]) == int(lead["score_20"]), f"Score does not sum: {lead['brand']}"
        assert float(lead["score"]) == float(lead["score_20"]) / 2, f"Score scale mismatch: {lead['brand']}"
        source_ids = {s["id"] for s in lead.get("sources_detail", [])}
        assert source_ids, f"No detailed sources: {lead['brand']}"
        assert len(source_ids) == len(lead["sources_detail"]), f"Duplicate source IDs: {lead['brand']}"
        for finding in lead.get("findings", []):
            assert set(finding.get("source_ids", [])).issubset(source_ids), f"Unresolved finding source: {lead['brand']}"
        for ad in lead.get("ad_evidence", []):
            assert ad.get("library_id") and ad.get("page_id"), f"Missing direct Meta IDs: {lead['brand']}"
            assert ad.get("source_id") in source_ids, f"Unresolved ad source: {lead['brand']}"
            assert ad.get("status", "").startswith("Active"), f"Non-active selected Meta record: {lead['brand']}"
        email = lead.get("contact", {}).get("email", "").casefold()
        source_text = " ".join(
            [lead.get("contact_source", "")]
            + [s.get("observed", "") + " " + s.get("url", "") for s in lead.get("sources_detail", [])]
        ).casefold()
        assert email and email in source_text, f"Published email not present in cited first-party provenance: {lead['brand']}"
    return data


def check_deduplication(leads):
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    known_names = {norm_name(k) for k in registry.get("brands", {})}
    known_domains = {norm_domain(v.get("website", "")) for v in registry.get("brands", {}).values()}
    proposed = {lead["slug"]: lead for lead in leads}
    existing_names, existing_domains = set(), set()
    for folder in (REPO / "niches").glob("*"):
        if not folder.is_dir():
            continue
        for path in (folder / "leads").glob("*.json"):
            try:
                obj = json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:
                raise ValueError(f"Unreadable existing lead file {path}: {exc}")
            # Permit exact current-batch files produced by a prior partial/repeat run,
            # but do not exempt a conflicting lead or a same-name file from another niche.
            expected = proposed.get(path.stem) if folder.resolve() == ROOT.resolve() else None
            if expected and obj.get("batch") == 3 and norm_name(obj.get("brand", "")) == norm_name(expected["brand"]) and norm_domain(obj.get("website", "")) == norm_domain(expected["website"]):
                continue
            if obj.get("brand"):
                existing_names.add(norm_name(obj["brand"]))
            if obj.get("website"):
                existing_domains.add(norm_domain(obj["website"]))
    duplicates = []
    for lead in leads:
        name_key, domain_key = norm_name(lead["brand"]), norm_domain(lead["website"])
        if name_key in known_names or domain_key in known_domains or name_key in existing_names or domain_key in existing_domains:
            duplicates.append((lead["brand"], lead["website"]))
    if duplicates:
        raise ValueError(f"Deduplication failed: {duplicates}")
    return registry


def make_outreach_markdown(lead):
    c = lead["contact"]
    lines = [
        f"# {lead['brand']} — Outreach templates",
        "",
        f"> Batch 3 · drafted from public sources checked 04 Oct 2026. Internal outreach copy; verify the source links again before sending.",
        "> The published route below is a routing contact, not a confirmed media buyer. The sequence makes no private performance claim.",
        "",
        f"**To (published first-party route):** `{c['email']}`  ",
        f"**Contact role:** {c.get('route_role', 'Published general contact; buyer not confirmed')}  ",
        f"**Provenance:** {lead['contact_source']}",
        "",
        "---",
        "",
    ]
    days = ["Day 1", "Day 3", "Day 7", "Day 14"]
    for i, (subject, body) in enumerate(lead["outreach"]):
        lines.extend([
            f"## Email {i + 1} ({days[i]}): {subject}",
            "",
            "```text",
            body.strip(),
            "```",
            "",
        ])
    lines.extend([
        "---",
        "",
        "**Before sending:** re-open the linked ad/source, confirm the offer or creative is still current, and ask for the right owner rather than assuming this route is a buyer.",
        "",
    ])
    return "\n".join(lines)


def write_json_and_outreach(leads):
    for lead in leads:
        (ROOT / "leads" / f"{lead['slug']}.json").write_text(
            json.dumps(lead, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        (ROOT / "outreach" / f"{lead['slug']}-outreach-templates.md").write_text(
            make_outreach_markdown(lead), encoding="utf-8"
        )


def _story_value(s):
    return " ".join(str(s).replace("\n", " ").split())


def _google_card_text(lead):
    status = lead["google_evidence"]["status"]
    detail = lead["google_evidence"]["detail"]
    if status == "NOT MEASURED":
        return "Not measured", "No zero-ad finding is implied"
    if "MIGHTYHIVE" in detail:
        return "Attribution unconfirmed", "Domain query surfaced MIGHTYHIVE entities"
    if "Six domain-query" in detail:
        return "6 domain results", "Curefoods entity; not Krispy-specific"
    return "Checked; attribution unclear", "No brand-specific count reported"


def _local_card_text(lead):
    m = lead.get("market_signal", "")
    if "unconfirmed" in m.casefold() and any(x in m.casefold() for x in ("bengaluru", "bangalore", "blr")):
        return "Outlet unconfirmed", "Selected creative names Bengaluru"
    ad_copy = " ".join(a.get("creative_excerpt", "") for a in lead.get("ad_evidence", [])).casefold()
    if any(x in ad_copy for x in ("bengaluru", "bangalore", "blr")):
        return "City in selected creative", "No audience targeting inferred"
    if any(k in m.casefold() for k in ("bengaluru address", "bengaluru store", "bengaluru corporate office", "bengaluru location", "bangalore address", "bangalore delivery")):
        return "First-party local context", "No ad-targeting inference"
    return "Local context published", "Source and limits noted in report"


def _register_fallback_fonts():
    try:
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        sans = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
        mono = Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf")
        if sans.exists() and "DejaVuSans" not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont("DejaVuSans", str(sans)))
        if mono.exists() and "DejaVuSansMono" not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont("DejaVuSansMono", str(mono)))
    except Exception:
        pass


def pdf_safe(text, mono=False):
    text = html.escape(str(text), quote=False).replace("\n", "<br/>")
    replacement = "DejaVuSansMono" if mono else "DejaVuSans"
    text = text.replace("₹", f"<font name='{replacement}'>₹</font>")
    return text


def make_pdf(lead, total_pages=5, destination=None):
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.pdfbase.pdfmetrics import stringWidth
    from reportlab.platypus import (
        BaseDocTemplate, PageTemplate, Frame, Flowable, Paragraph, Spacer, Table,
        TableStyle, KeepTogether, CondPageBreak, NextPageTemplate, PageBreak,
        HRFlowable,
    )
    from reportlab.lib.utils import ImageReader

    _register_fallback_fonts()
    page_w, page_h = letter
    navy = colors.HexColor("#" + NAVY)
    navy2 = colors.HexColor("#" + NAVY_2)
    teal = colors.HexColor("#" + TEAL)
    gold = colors.HexColor("#" + GOLD)
    panel = colors.HexColor("#" + PANEL)
    rule = colors.HexColor("#" + RULE)
    muted = colors.HexColor("#" + MUTED)
    ink = colors.HexColor("#" + INK)
    white = colors.white
    logo = ROOT / "assets" / "smart-pursuit-logo.png"

    class CoverMarker(Flowable):
        def __init__(self):
            super().__init__()
            self.width = 1
            self.height = 1
        def draw(self):
            pass

    class AuditDoc(BaseDocTemplate):
        def __init__(self, path, total):
            super().__init__(path, pagesize=letter, leftMargin=42, rightMargin=42,
                             topMargin=84, bottomMargin=52, title=f"{lead['brand']} — Paid Media & Measurement Audit",
                             author="Smart Pursuit")
            self.total = total
            cover_frame = Frame(42, 50, page_w - 84, page_h - 100, id="cover",
                                leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
            body_frame = Frame(42, 58, page_w - 84, 620, id="body",
                               leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
            self.addPageTemplates([
                PageTemplate(id="Cover", frames=[cover_frame], onPage=self._cover),
                PageTemplate(id="Body", frames=[body_frame], onPage=self._body),
            ])

        def _cover(self, canv, doc):
            canv.saveState()
            canv.setFillColor(navy)
            canv.rect(0, 0, page_w, page_h, fill=1, stroke=0)
            canv.setFillColor(gold)
            canv.rect(36, 628, 4, 118, fill=1, stroke=0)
            if logo.exists():
                canv.drawImage(str(logo), 55, 666, width=78, height=78, preserveAspectRatio=True, mask="auto")
            canv.setFillColor(gold)
            canv.setFont("Helvetica-Bold", 8)
            canv.drawString(150, 728, "PAID MEDIA & MEASUREMENT AUDIT")
            canv.setFillColor(white)
            brand_size = 27
            while stringWidth(lead["brand"], "Helvetica-Bold", brand_size) > 404 and brand_size > 19:
                brand_size -= 1
            canv.setFont("Helvetica-Bold", brand_size)
            canv.drawString(150, 690, lead["brand"])
            subtitle = Paragraph(pdf_safe(lead.get("headline", "Public-evidence snapshot")), ParagraphStyle(
                "CoverSubtitle", fontName="Helvetica", fontSize=9.2, leading=12.2,
                textColor=colors.HexColor("#D7E2EC"), spaceAfter=0,
            ))
            sw, sh = subtitle.wrap(408, 46)
            subtitle.drawOn(canv, 150, max(643, 654 - sh))
            canv.setFillColor(colors.HexColor("#C5D1DC"))
            canv.setFont("Helvetica-Bold", 7.2)
            canv.drawString(55, 622, "BATCH 3  ·  PUBLIC-EVIDENCE SNAPSHOT  ·  VERIFIED 04 OCT 2026")

            google_value, google_note = _google_card_text(lead)
            local_value, local_note = _local_card_text(lead)
            cards = [
                ("SELECTED META RECORDS", f"{len(lead['ad_evidence'])} selected", "Active on the capture date; not an account-wide total"),
                ("GOOGLE ADS TRANSPARENCY", google_value, google_note),
                ("BENGALURU RELEVANCE", local_value, local_note),
                ("PUBLIC-EVIDENCE FIT", f"{lead['score_20']} / 20", f"{lead['score']} / 10 · triage only, not performance"),
            ]
            card_w, card_h = 252, 74
            positions = [(42, 525), (318, 525), (42, 435), (318, 435)]
            for (label, value, note), (x, y) in zip(cards, positions):
                canv.setFillColor(colors.HexColor("#F4F7FA"))
                canv.roundRect(x, y, card_w, card_h, 7, fill=1, stroke=0)
                canv.setFillColor(gold)
                canv.roundRect(x, y, 4, card_h, 2, fill=1, stroke=0)
                canv.setFillColor(muted)
                canv.setFont("Helvetica-Bold", 6.7)
                canv.drawString(x + 14, y + 56, label)
                value_size = 14 if len(value) < 23 else 11
                canv.setFillColor(navy)
                canv.setFont("Helvetica-Bold", value_size)
                canv.drawString(x + 14, y + 35, value[:42])
                note_para = Paragraph(pdf_safe(note), ParagraphStyle(
                    "CardNote", fontName="Helvetica", fontSize=7.0, leading=8.6,
                    textColor=muted,
                ))
                nw, nh = note_para.wrap(card_w - 27, 20)
                note_para.drawOn(canv, x + 14, y + 7)

            # Boundary statement is intentionally explicit; the cover is not a performance claim.
            canv.setFillColor(colors.HexColor("#18334B"))
            canv.roundRect(42, 350, 528, 56, 7, fill=1, stroke=0)
            canv.setFillColor(gold)
            canv.setFont("Helvetica-Bold", 7.2)
            canv.drawString(56, 385, "SCOPE BOUNDARY")
            boundary = Paragraph(
                "Public pages and selected ad-library records only. Private account spend, ROAS, CPA, conversions, bookings and event firing were not accessed; unmeasured values are not estimated.",
                ParagraphStyle("Boundary", fontName="Helvetica", fontSize=8.0, leading=10.3,
                               textColor=colors.HexColor("#E1EAF1")),
            )
            bw, bh = boundary.wrap(496, 30)
            boundary.drawOn(canv, 56, 360)

            # Prepared-for and agency contact boxes.
            canv.setFillColor(colors.HexColor("#F4F7FA"))
            canv.roundRect(42, 213, 252, 104, 7, fill=1, stroke=0)
            canv.setFillColor(gold)
            canv.roundRect(42, 213, 4, 104, 2, fill=1, stroke=0)
            canv.setFillColor(muted)
            canv.setFont("Helvetica-Bold", 7.2)
            canv.drawString(57, 294, "PREPARED FOR")
            canv.setFillColor(navy)
            canv.setFont("Helvetica-Bold", 15)
            canv.drawString(57, 270, (lead["brand"] + " team")[:36])
            canv.setFont("Helvetica", 8)
            canv.setFillColor(ink)
            canv.drawString(57, 250, "Bengaluru food-lead batch · 03")
            canv.drawString(57, 234, "Source-checked 04 October 2026")

            canv.setFillColor(navy2)
            canv.roundRect(318, 213, 252, 104, 7, fill=1, stroke=0)
            canv.setStrokeColor(gold)
            canv.setLineWidth(1)
            canv.roundRect(318, 213, 252, 104, 7, fill=0, stroke=1)
            canv.setFillColor(gold)
            canv.setFont("Helvetica-Bold", 7.2)
            canv.drawString(333, 294, "CONTACT · SMART PURSUIT")
            canv.setFillColor(white)
            canv.setFont("Helvetica-Bold", 9.2)
            canv.drawString(333, 270, "smartpursuit3@gmail.com")
            canv.setFont("Helvetica", 8.5)
            canv.drawString(333, 250, "7095024220")
            canv.setFillColor(colors.HexColor("#D7E2EC"))
            canv.setFont("Helvetica", 7)
            canv.drawString(333, 231, "Brand-published route is listed inside the report.")

            canv.setStrokeColor(colors.HexColor("#294257"))
            canv.line(42, 54, 570, 54)
            canv.setFillColor(colors.HexColor("#B7C6D3"))
            canv.setFont("Helvetica", 7.2)
            canv.drawString(42, 35, "Smart Pursuit  ·  smartpursuit3@gmail.com  ·  7095024220")
            canv.drawRightString(570, 35, f"Page 1 of {self.total}")
            canv.restoreState()

        def _body(self, canv, doc):
            canv.saveState()
            canv.setFillColor(white)
            canv.rect(0, 0, page_w, page_h, fill=1, stroke=0)
            if logo.exists():
                canv.drawImage(str(logo), 40, 744, width=40, height=40, preserveAspectRatio=True, mask="auto")
            canv.setFillColor(navy)
            canv.setFont("Helvetica-Bold", 7.4)
            canv.drawString(91, 766, "FOOD / BENGALURU  ·  PUBLIC-EVIDENCE AUDIT")
            canv.setFillColor(muted)
            canv.setFont("Helvetica", 7)
            canv.drawRightString(570, 766, f"{lead['brand']}  ·  04 OCT 2026")
            canv.setStrokeColor(rule)
            canv.setLineWidth(0.8)
            canv.line(42, 735, 570, 735)
            canv.line(42, 39, 570, 39)
            canv.setFillColor(muted)
            canv.setFont("Helvetica", 6.8)
            canv.drawString(42, 24, "Smart Pursuit  ·  smartpursuit3@gmail.com  ·  7095024220")
            canv.drawRightString(570, 24, f"Page {doc.page} of {self.total}")
            canv.restoreState()

    # Styles are intentionally compact but readable to target five pages.
    S = {
        "section": ParagraphStyle("Section", fontName="Helvetica-Bold", fontSize=11.0, leading=14,
                                   textColor=navy, spaceBefore=5, spaceAfter=5),
        "body": ParagraphStyle("Body", fontName="Helvetica", fontSize=8.0, leading=10.3,
                                textColor=ink, spaceAfter=3),
        "small": ParagraphStyle("Small", fontName="Helvetica", fontSize=7.25, leading=9.1,
                                 textColor=ink),
        "tiny": ParagraphStyle("Tiny", fontName="Helvetica", fontSize=6.7, leading=8.2,
                                textColor=ink),
        "thead": ParagraphStyle("TableHeader", fontName="Helvetica-Bold", fontSize=6.7, leading=8.2,
                                 textColor=white),
        "label": ParagraphStyle("Label", fontName="Helvetica-Bold", fontSize=7.0, leading=8.5,
                                 textColor=navy),
        "muted": ParagraphStyle("Muted", fontName="Helvetica", fontSize=7.1, leading=8.8,
                                 textColor=muted),
        "findingtitle": ParagraphStyle("FindingTitle", fontName="Helvetica-Bold", fontSize=9.0,
                                        leading=11.2, textColor=navy),
        "evidence": ParagraphStyle("Evidence", fontName="Courier", fontSize=7.0, leading=8.8,
                                    textColor=ink, splitLongWords=1),
        "italic": ParagraphStyle("Italic", fontName="Helvetica-Oblique", fontSize=7.65, leading=9.8,
                                 textColor=muted),
        "callout": ParagraphStyle("Callout", fontName="Helvetica", fontSize=7.8, leading=10.0,
                                   textColor=ink),
        "contents": ParagraphStyle("Contents", fontName="Helvetica", fontSize=7.6, leading=9.2,
                                    textColor=ink),
        "nexttitle": ParagraphStyle("NextTitle", fontName="Helvetica-Bold", fontSize=8.6,
                                     leading=10.2, textColor=navy),
        "next": ParagraphStyle("Next", fontName="Helvetica", fontSize=7.7, leading=9.8,
                               textColor=ink),
        "score": ParagraphStyle("Score", fontName="Helvetica-Bold", fontSize=8.2, leading=10,
                                 textColor=navy),
    }

    def P(text, style="body"):
        return Paragraph(pdf_safe(text), S[style])

    def heading(number, title):
        return Paragraph(
            f"<font color='#{TEAL}'>{html.escape(number)}</font>  <b>{html.escape(title.upper())}</b>",
            S["section"],
        )

    def source_link(url, label="Open source"):
        safe_url = html.escape(str(url), quote=True).replace("&amp;", "&amp;")
        return Paragraph(f"<link href=\"{safe_url}\"><font color=\"#{TEAL}\"><u>{html.escape(label)}</u></font></link>", S["tiny"])

    def status_color(status):
        s = status.upper()
        if "UNAVAILABLE" in s:
            return colors.HexColor("#E2E8F0")
        if "NOT MEASURED" in s or "UNCONFIRMED" in s:
            return colors.HexColor("#FEF3C7")
        return colors.HexColor("#D1FAE5")

    def section_table(rows, widths, header=True, font_style="tiny", repeatRows=1):
        table = Table(rows, colWidths=widths, repeatRows=(repeatRows if header else 0), hAlign="LEFT")
        commands = [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("GRID", (0, 0), (-1, -1), 0.35, rule),
        ]
        if header:
            commands += [
                ("BACKGROUND", (0, 0), (-1, 0), navy),
                ("TEXTCOLOR", (0, 0), (-1, 0), white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ]
        table.setStyle(TableStyle(commands))
        return table

    story = [CoverMarker(), NextPageTemplate("Body"), PageBreak()]

    # CONTENTS + METHOD
    story.append(heading("", "Contents"))
    contents = [
        [P("01  Method", "contents"), P("02  The ad account + coverage", "contents")],
        [P("03  Findings", "contents"), P("03b  Evidence register", "contents")],
        [P("04  Opportunity score", "contents"), P("05  Next steps", "contents")],
    ]
    toc = Table(contents, colWidths=[264, 264], hAlign="LEFT")
    toc.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), panel),
        ("BOX", (0, 0), (-1, -1), 0.45, rule),
        ("INNERGRID", (0, 0), (-1, -1), 0.3, rule),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.extend([toc, Spacer(1, 6), heading("01", "Method"), P(
        "Dated public-evidence snapshot checked 04 October 2026. Meta evidence is cited by individual Library ID and advertiser/page ID; the selected cards are not an account-wide count. Meta search-type parameters can be ignored by the interface, so keyword results are not treated as page or advertiser proof. Bengaluru relevance is based only on explicit creative or first-party material; no audience targeting is inferred.", "body"), P(
        "Contacts and offer details are taken from the brand's own website, help or corporate pages and remain routing contacts unless a buyer role is explicitly published. No private account, booking, order or analytics records were accessed. Spend, ROAS, CPA, conversion outcomes and event firing are marked unavailable or not measured. A public ad card or URL alone does not prove that tracking events fire.", "body"),
    ])

    # THE AD ACCOUNT: concise label/value table.
    story.append(heading("02", "The ad account"))
    meta_summary = "; ".join(
        f"ID {a['library_id']} (started {a.get('started_on', 'not published')})"
        for a in lead.get("ad_evidence", [])
    )
    contact = lead["contact"]
    account_rows = [
        [P("Brand / website", "label"), P(f"{lead['brand']} · {lead['website']}", "small")],
        [P("Local context", "label"), P(lead.get("market_signal", "Not established from reviewed public sources"), "small")],
        [P("Selected Meta records", "label"), P(f"{meta_summary}. Active on 04 Oct 2026; selected records only.", "small")],
        [P("Google Ads", "label"), P(f"{lead['google_evidence']['status']}: {lead['google_evidence']['detail']}", "small")],
        [P("Published contact", "label"), P(f"{contact.get('email','')} · {contact.get('route_role','')} {lead.get('contact_source','')}", "small")],
        [P("Public-evidence fit", "label"), P(f"{lead['score_20']} / 20 · {lead['score']} / 10 · {lead['score_band']}. {lead.get('score_note','')}", "small")],
    ]
    at = Table(account_rows, colWidths=[118, 410], hAlign="LEFT")
    at.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (0, -1), panel),
        ("GRID", (0, 0), (-1, -1), 0.35, rule),
        ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(at)
    story.append(Spacer(1, 5))

    story.append(P("COVERAGE · each line is dated 04 OCT 2026", "label"))
    cov_rows = [[P("Surface", "thead"), P("Status", "thead"), P("Method / boundary", "thead")]]
    for c in lead.get("coverage", []):
        cov_rows.append([
            P(c["surface"], "tiny"), P(c["status"], "tiny"), P(c["method"], "tiny")
        ])
    cov = Table(cov_rows, colWidths=[112, 132, 284], repeatRows=1, hAlign="LEFT")
    cov_commands = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (-1, 0), navy),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("GRID", (0, 0), (-1, -1), 0.35, rule),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]
    for r, c in enumerate(lead.get("coverage", []), start=1):
        cov_commands.append(("BACKGROUND", (1, r), (1, r), status_color(c["status"])))
    cov.setStyle(TableStyle(cov_commands))
    boundary_rows = [
        [P("AD LIBRARY", "label"), P("Selected Library IDs and page identities establish the visible record and copy only; no account-wide inventory or audience targeting is inferred.", "tiny")],
        [P("GOOGLE", "label"), P(lead["google_evidence"]["detail"], "tiny")],
        [P("LOCAL", "label"), P("City relevance comes from the selected creative or first-party material; it does not establish geographic targeting.", "tiny")],
        [P("PRIVATE DATA", "label"), P("Spend, ROAS, CPA, conversion outcomes and event firing are unavailable/not measured unless a source explicitly establishes them.", "tiny")],
    ]
    boundary_table = Table(boundary_rows, colWidths=[98, 430], hAlign="LEFT")
    boundary_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#E8F4F4")),
        ("GRID", (0, 0), (-1, -1), 0.35, rule),
        ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    story.extend([cov, Spacer(1, 5), P("EVIDENCE BOUNDARIES", "label"), boundary_table, Spacer(1, 7)])

    # FINDINGS: title+raw evidence atomic, analysis and next check can flow.
    story.append(CondPageBreak(250))
    story.append(heading("03", "Findings"))
    sev_colors = {
        "CRITICAL": (colors.HexColor("#FEE2E2"), colors.HexColor("#DC2626")),
        "HIGH": (colors.HexColor("#FFEDD5"), colors.HexColor("#EA580C")),
        "MEDIUM": (colors.HexColor("#FEF3C7"), colors.HexColor("#B45309")),
        "LOW": (colors.HexColor("#D1FAE5"), colors.HexColor("#047857")),
        "NOTE": (colors.HexColor("#E2E8F0"), colors.HexColor("#475569")),
    }
    for idx, f in enumerate(lead.get("findings", []), start=1):
        severity = str(f.get("priority", "NOTE")).upper()
        bg, fg = sev_colors.get(severity, sev_colors["NOTE"])
        badge = Table(
            [[P(severity, "label"), P(f"{idx:02d}  {f['title']}", "findingtitle")]],
            colWidths=[68, 460], hAlign="LEFT",
        )
        badge.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (0, 0), bg),
            ("BACKGROUND", (1, 0), (1, 0), panel),
            ("TEXTCOLOR", (0, 0), (0, 0), fg),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("BOX", (0, 0), (-1, -1), 0.45, rule),
            ("INNERGRID", (0, 0), (-1, -1), 0.35, rule),
            ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]))
        evidence_text = (
            f"source_ids: {', '.join(f.get('source_ids', []))}\n"
            f"observed: {f.get('evidence', '')}\n"
            f"checked: 04 OCT 2026"
        )
        evidence_box = Table([[Paragraph(pdf_safe(evidence_text, mono=True), S["evidence"])]], colWidths=[528])
        evidence_box.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
            ("BOX", (0, 0), (-1, -1), 0.4, rule),
            ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]))
        story.append(KeepTogether([badge, evidence_box]))
        story.append(Spacer(1, 3))
        story.append(P(f["analysis"], "italic"))
        story.append(P(f"NEXT CHECK · {f['next_check']}", "small"))
        story.append(Spacer(1, 6))

    # EVIDENCE REGISTER: all cited source records, including first-party contact provenance.
    story.extend([CondPageBreak(100), heading("03b", "Evidence register")])
    ev_rows = [[P("ID / source", "thead"), P("Value observed", "thead"), P("Date", "thead"), P("Link", "thead")]]
    for src in lead.get("sources_detail", []):
        ev_rows.append([
            P(f"{src['id']} · {src['label']}", "tiny"),
            P(src.get("observed", ""), "tiny"),
            P(src.get("verified_on", "2026-10-04"), "tiny"),
            source_link(src["url"], f"Open {src['id']}"),
        ])
    evt = Table(ev_rows, colWidths=[108, 300, 62, 58], repeatRows=1, hAlign="LEFT")
    evt.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (-1, 0), navy), ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("GRID", (0, 0), (-1, -1), 0.35, rule),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, panel]),
    ]))
    story.extend([evt, Spacer(1, 8)])

    # SCORE: public evidence fit only; this is not an efficacy or ROI rating.
    story.extend([CondPageBreak(240), heading("04", "Opportunity score")])
    score_rows = [[P("Dimension", "thead"), P("Score", "thead"), P("Basis", "thead")]]
    for item in lead.get("score_breakdown", []):
        score_rows.append([
            P(item["dimension"], "tiny"),
            P(f"{item['score']} / 4", "score"),
            P(item["basis"], "tiny"),
        ])
    sc = Table(score_rows, colWidths=[148, 52, 328], repeatRows=1, hAlign="LEFT")
    sc.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (-1, 0), navy), ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("GRID", (0, 0), (-1, -1), 0.35, rule),
        ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, panel]),
    ]))
    story.append(sc)
    total_score = Table([[P(f"OVERALL PUBLIC-EVIDENCE FIT  ·  {lead['score_20']} / 20  ·  {lead['score']} / 10  ·  {lead['score_band']}", "score")]], colWidths=[528])
    total_score.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#E8F4F4")),
        ("BOX", (0, 0), (-1, -1), 0.8, teal),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    qualification = Table([[P(
        "QUALIFICATION · Read before acting. This is a triage score of public paid signal, local relevance, public CTA visibility, first-party source coverage and contact-route relevance. It is not an ad-performance, revenue, sales-probability, spend, forecast or ROI score. Private results were not accessed. Scores are not directly comparable with the legacy batches' prior scoring framework.", "callout")]], colWidths=[528])
    qualification.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FFF8E7")),
        ("BOX", (0, 0), (-1, -1), 0.5, gold),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    account_check_rows = [
        [P("Outcome definition", "label"), P("Name the event or business outcome, its counting rule and any deduplication rule before comparing systems.", "tiny")],
        [P("Time window", "label"), P("Use the same date range, timezone and attribution window across any records being reconciled.", "tiny")],
        [P("Path mapping", "label"), P("Trace the selected Library ID through the visible click route to the brand's own booking, enquiry or order record where applicable.", "tiny")],
        [P("Reconciliation", "label"), P("Keep platform, analytics and CRM/order data side by side until event definitions and windows are comparable; do not add incompatible totals.", "tiny")],
    ]
    account_check = Table(account_check_rows, colWidths=[112, 416], hAlign="LEFT")
    account_check.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (0, -1), panel),
        ("GRID", (0, 0), (-1, -1), 0.35, rule),
        ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    score_key_rows = [
        [P("Direct paid signal", "label"), P("A page-resolved active public ad record; not spend or outcome.", "tiny")],
        [P("Bengaluru relevance", "label"), P("Explicit local creative or first-party context; not audience targeting.", "tiny")],
        [P("Public CTA visibility", "label"), P("A visible public next step or destination; not a conversion.", "tiny")],
        [P("First-party coverage", "label"), P("Breadth of official product, store, contact or corporate evidence reviewed.", "tiny")],
        [P("Contact-route relevance", "label"), P("How suitable the published route is for a referral request; no buyer identity is inferred.", "tiny")],
    ]
    score_key = Table(score_key_rows, colWidths=[155, 373], hAlign="LEFT")
    score_key.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"), ("BACKGROUND", (0, 0), (0, -1), panel),
        ("GRID", (0, 0), (-1, -1), 0.35, rule),
        ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    story.extend([Spacer(1, 5), P("SCORING KEY", "label"), score_key, Spacer(1, 6),
                  P("ACCOUNT-SIDE VALIDATION CHECKLIST", "label"), account_check, Spacer(1, 8)])

    # NEXT STEPS + CTA + close; suggested effort labels are operational, not outcome estimates.
    story.extend([CondPageBreak(200), heading("05", "Next steps"), P(
        "Suggested effort labels are planning aids only. First re-open the dated public sources; then use internal account/CRM/order records only if the company chooses to share them.", "muted")])
    ad_ids = ", ".join(a["library_id"] for a in lead.get("ad_evidence", []))
    meta_dates = ", ".join(a.get("started_on", "date not exposed") for a in lead.get("ad_evidence", []))
    step_specs = [
        ("LOW EFFORT", "Route the question", f"Use {contact.get('email','the published contact')} as a routing contact only; ask for the paid-media measurement owner. The published source does not identify this inbox as a buyer."),
        ("UNDER AN HOUR", "Re-open the selected card", f"Recheck Library ID(s) {ad_ids}; the selected records showed start date(s) {meta_dates}. Confirm today's status, page identity, copy, CTA and any currently exposed destination before reusing the observation."),
        ("UNDER AN HOUR", "Complete the finding-specific public check", " ".join(f["next_check"] for f in lead.get("findings", [])[:2])),
        ("HALF A DAY", "Reconcile only with authorized private records", lead.get("findings", [{}])[-1].get("next_check", "") + " If access is authorized, align the event definition, date window, timezone, Library ID and the corresponding booking/order or CRM record. Do not infer an outcome from the public ad card."),
    ]
    for step_index, (effort, title, text) in enumerate(step_specs):
        # A conditional break preserves complete, actionable step cards; the final card and
        # source handoff can continue on page 5 when the prior page is full.
        if step_index == 3:
            story.append(CondPageBreak(240))
        # This is intentional ReportLab markup; P() escapes markup for ordinary text.
        badge = Paragraph(f"<b>{html.escape(effort)}</b>", S["tiny"])
        content = [P(title, "nexttitle"), P(text, "next")]
        row = Table([[badge, content]], colWidths=[100, 428], hAlign="LEFT")
        row.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (0, 0), colors.HexColor("#FEF3C7")),
            ("BACKGROUND", (1, 0), (1, 0), panel),
            ("BOX", (0, 0), (-1, -1), 0.4, rule),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]))
        story.extend([row, Spacer(1, 5)])

    # Compact, source-linked handoff: makes the final page useful as a practical re-check sheet.
    contact_src = next((s for s in lead.get("sources_detail", []) if s["id"] in lead["contact_source_detail"]["source_ids"]), None)
    handoff_route = Paragraph(
        f"{pdf_safe(contact.get('email', ''))} · {pdf_safe(contact.get('phone', ''))}<br/>{pdf_safe(contact.get('route_role', ''))}",
        S["small"],
    )
    handoff_contact = Table([[P("PUBLISHED ROUTE", "label"), handoff_route, source_link(contact_src["url"], "Verify route") if contact_src else P("Source listed in register", "tiny")]], colWidths=[100, 350, 78], hAlign="LEFT")
    handoff_contact.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), colors.HexColor("#E8F4F4")),
        ("BACKGROUND", (1, 0), (-1, -1), panel),
        ("GRID", (0, 0), (-1, -1), 0.4, rule),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.extend([Spacer(1, 4), P("SOURCE LINKS TO REOPEN BEFORE OUTREACH", "label")])
    link_rows = [[P("ID", "thead"), P("Source", "thead"), P("Open", "thead")]]
    for src in lead.get("sources_detail", []):
        source_summary = f"{pdf_safe(src['label'])}<br/><font color='#{MUTED}'>{pdf_safe(src.get('observed',''))}</font>"
        link_rows.append([P(src["id"], "tiny"), Paragraph(source_summary, S["tiny"]), source_link(src["url"], "Open source")])
    link_table = Table(link_rows, colWidths=[42, 404, 82], repeatRows=1, hAlign="LEFT")
    link_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), navy), ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("GRID", (0, 0), (-1, -1), 0.35, rule), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    handoff_rows = [
        [P("EVENT", "label"), P("Which completed customer action is the agreed outcome: order, booking, enquiry, store visit or another defined event?", "tiny")],
        [P("IDENTITY", "label"), P("Which ad/campaign identifier or approved source field links the selected Library ID to the internal record?", "tiny")],
        [P("WINDOW", "label"), P("What date range, timezone, attribution window and counting/deduplication rule apply?", "tiny")],
        [P("SYSTEM", "label"), P("Which account, analytics, CRM, booking or order system is the source of record, and who can verify it?", "tiny")],
    ]
    handoff_check = Table(handoff_rows, colWidths=[72, 456], hAlign="LEFT")
    handoff_check.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#E8F4F4")),
        ("GRID", (0, 0), (-1, -1), 0.35, rule), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    send_check_rows = [
        [P("DATE", "label"), P("Re-open each cited Library ID and update the status/date if the public card has changed.", "tiny")],
        [P("CLAIM", "label"), P("Use only the cited copy or first-party terms; do not infer audience geography, tracking events or private outcomes.", "tiny")],
        [P("ROUTE", "label"), P("Use the published first-party email as a routing contact and ask for the right owner if needed.", "tiny")],
    ]
    send_check = Table(send_check_rows, colWidths=[62, 466], hAlign="LEFT")
    send_check.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#FEF3C7")),
        ("GRID", (0, 0), (-1, -1), 0.35, rule), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    story.extend([handoff_contact, Spacer(1, 6), link_table, Spacer(1, 6),
                  P("IF AN ACCOUNT-SIDE REVIEW IS AUTHORIZED", "label"), handoff_check, Spacer(1, 6),
                  P("OUTREACH CHECK BEFORE SENDING", "label"), send_check, Spacer(1, 6)])

    limits = Table([[P(
        "BEFORE CONCLUDING  ·  Recheck active status and dated copy; do not infer audience targeting from a city name, URL tag or keyword result; treat unmeasured private outcomes as unavailable; treat a published inbox as a route, not proof of the media owner.", "callout")]], colWidths=[528])
    limits.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), panel), ("BOX", (0, 0), (-1, -1), 0.5, rule),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    cta = Table([[Paragraph("<font color='#FFFFFF'><b>Happy to walk through any of this on a short call.</b></font>", S["findingtitle"]),
                  Paragraph("<font color='#FFFFFF'><b>GET IN TOUCH</b><br/>smartpursuit3@gmail.com<br/>7095024220</font>", S["small"])]], colWidths=[320, 208])
    cta.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), navy),
        ("TEXTCOLOR", (0, 0), (-1, -1), white),
        ("BOX", (0, 0), (-1, -1), 0.5, gold),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    close = Table([[P(
        "ABOUT THIS REPORT · Smart Pursuit prepared this dated snapshot from the public sources listed above. The linked sources are the verification route; recheck them because live ad inventory changes. No private account data or client performance result is represented here.", "tiny")]], colWidths=[528])
    close.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#E8F4F4")),
        ("BOX", (0, 0), (-1, -1), 0.4, teal),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    story.extend([Spacer(1, 3), limits, Spacer(1, 5), cta, Spacer(1, 5), close])

    doc = AuditDoc(str(destination), total_pages)
    doc.build(story)


def generate_pdfs(leads):
    import pymupdf as fitz
    audit_dir = ROOT / "audits"
    audit_dir.mkdir(exist_ok=True)
    for lead in leads:
        out = audit_dir / f"{lead['slug']}-paid-media-measurement-audit.pdf"
        temp = out.with_suffix(".layout-check.pdf")
        make_pdf(lead, total_pages=99, destination=temp)
        with fitz.open(temp) as pdf:
            page_count = len(pdf)
        make_pdf(lead, total_pages=page_count, destination=out)
        temp.unlink(missing_ok=True)
        print(f"PDF {out.name}: {page_count} pages, {out.stat().st_size:,} bytes")


def _md_table(text_rows):
    def esc(v):
        return str(v).replace("|", "\\|").replace("\n", " ")
    lines = ["| Claim in the audit | Where to check it | Link | What you should see |",
             "|---|---|---|---|"]
    for row in text_rows:
        lines.append("| " + " | ".join(esc(x) for x in row) + " |")
    return "\n".join(lines)


def build_verify_batch_section(leads):
    out = [
        "\n\n## Batch 3 — Food / Bengaluru (source check: 04 October 2026)\n",
        "\nThis is a dated public-evidence snapshot. Meta claims below are tied to individual Library IDs and a displayed page identity; keyword/unordered results are not treated as proof of page ownership or targeting. Google queries marked **NOT MEASURED** are verification starting points only and do not imply zero ads. The audience geography, private spend, ROAS, CPA, orders, bookings and conversion outcomes were not accessed.\n",
    ]
    for lead in leads:
        out.append(f"\n### {lead['brand']}\n\nSite: `{lead['website']}` · checked 04 October 2026 · Batch 3\n\n")
        rows = []
        # Each claim in findings is mapped to every source ID cited by that finding.
        srcmap = {s["id"]: s for s in lead.get("sources_detail", [])}
        for ad in lead.get("ad_evidence", []):
            src = srcmap[ad["source_id"]]
            rows.append((
                f"Meta Ad Library ID {ad['library_id']} — active record; started {ad.get('started_on','not stated')}",
                f"Meta Ad Library · {ad.get('page_name','advertiser page')} · Library ID and page ID",
                f"[{src['url']}]({src['url']})",
                f"{ad.get('status','')}; page label `{ad.get('page_name','')}`; selected copy: {ad.get('creative_excerpt','')}; CTA: {ad.get('cta','')}; destination status: {ad.get('destination_status','')}",
            ))
        for finding in lead.get("findings", []):
            linked = [srcmap[x] for x in finding.get("source_ids", []) if x in srcmap]
            for src in linked:
                rows.append((
                    finding["title"],
                    f"{src['label']} ({src['id']})",
                    f"[{src['url']}]({src['url']})",
                    f"Evidence: {finding['evidence']} Analysis boundary: {finding['analysis']} Next check: {finding['next_check']}",
                ))
        # Add the full first-party/source observations, including contact provenance and ad IDs.
        used = {(r[1].split("(")[-1].rstrip(")") if "(" in r[1] else "") for r in rows}
        for src in lead.get("sources_detail", []):
            rows.append((
                f"Source register {src['id']} — {src['label']}",
                src["source_type"],
                f"[{src['url']}]({src['url']})",
                src.get("observed", ""),
            ))
        if lead.get("google_evidence"):
            g = lead["google_evidence"]
            rows.append((
                f"Google Ads Transparency status: {g['status']}",
                "Google Ads Transparency Center · India region · domain view",
                f"[{g.get('url','')}]({g.get('url','')})",
                g.get("detail", ""),
            ))
        rows.append((
            "Private performance / tracking measures",
            "Not publicly available from the sources in this snapshot",
            "—",
            "Spend, ROAS, CPA, orders/conversions and event firing were not accessed or estimated. The report labels these unavailable/not measured; no performance value is inferred from ad status, click path or creative copy.",
        ))
        rows.append((
            "Public-evidence fit score",
            "Scoring note and five-dimension breakdown in the report and lead JSON",
            f"[`leads/{lead['slug']}.json`](leads/{lead['slug']}.json)",
            f"{lead['score_20']} / 20 ({lead['score']} / 10), triage only. Dimensions and bases are recorded in the JSON; this is not an ROI, performance or revenue score.",
        ))
        out.append(_md_table(rows))
        out.append("\n\n**Contact provenance:** " + lead["contact_source"] + "\n")
    return "".join(out)


def append_verify_guide(leads):
    existing = VERIFY_MD.read_text(encoding="utf-8")
    marker = "## Batch 3 — Food / Bengaluru (source check: 04 October 2026)"
    if marker in existing:
        existing = existing[:existing.index(marker)].rstrip()
    combined = existing.rstrip() + build_verify_batch_section(leads)
    VERIFY_MD.write_text(combined.rstrip() + "\n", encoding="utf-8")


def build_all_email_appendix(leads):
    parts = [
        "\n\n---\n\n# Batch 3 — Food / Bengaluru (checked 04 Oct 2026)\n\n",
        "> Ten new leads · 40 messages · four-step sequence (Day 1 / 3 / 7 / 14). All factual openers are tied to the cited public evidence in `VERIFY-THE-DATA.md`. Published contact routes are not presumed to be media buyers.\n\n",
    ]
    for lead in leads:
        parts.append(f"## {lead['brand']}\n\n")
        parts.append(f"**Published route:** `{lead['contact']['email']}` · {lead['contact'].get('route_role','')}\n\n")
        parts.append(f"**Contact provenance:** {lead['contact_source']}\n\n")
        for i, (subject, body) in enumerate(lead["outreach"], 1):
            day = ["Day 1", "Day 3", "Day 7", "Day 14"][i - 1]
            parts.append(f"### Email {i} ({day}) — {subject}\n\n```text\n{body.strip()}\n```\n\n")
    return "".join(parts).rstrip() + "\n"


def build_readme(leads):
    rows = [
        "# Food / Bengaluru — Smart Pursuit paid-media evidence pack",
        "",
        "> **31 leads total:** 21 legacy records (previously captured 02–03 Oct 2026) plus 10 new Batch 3 leads source-checked 04 Oct 2026. The 21 legacy leads were not revalidated in this update. Batch 3 follows the evidence-only rules below.",
        "",
        "## Start here",
        "",
        "| Path | Contents / status |",
        "|---|---|",
        "| `Food-Bangalore-ALL-IN-ONE.xlsx` | Master workbook with 31 leads, 124 emails, findings, scores, source links, coverage, and a batch-vintage index. The historical ROI sheet is renamed **Legacy ROI Archive** and flagged as unverified; do not treat it as a current forecast. |",
        "| `Food-Bangalore-BATCH-3-EMAILS.xlsx` | One-sheet export of the 10 new Batch 3 leads using the requested eight columns: Brand name, Email, Subject, Body 1–4, and Attachment Name. |",
        "| `audits/*-paid-media-measurement-audit.pdf` | 31 per-lead PDFs. Batch 3 PDFs are exactly 5 pages each; existing Batch 1/2 PDFs are preserved in their prior formats and are not revalidated here. |",
        "| `VERIFY-THE-DATA.md` | Claim-to-source rows for Batch 1/2 plus the new Batch 3 source register and findings. |",
        "| `ALL-EMAIL-SEQUENCES.md` | All 124 email messages; Batch 3 adds 40 messages across ten leads. |",
        "| `outreach/*-outreach-templates.md` | Per-lead, four-email files; Batch 3 contact provenance included. |",
        "| `leads/*.json` | 31 structured lead files. Batch 3 JSON includes `contact_source`, contact source IDs, source register, findings, score bases and four emails. |",
        "| `LEADS-INDEX.csv` | Flat index for all 31 leads; Batch 3 Google status is explicitly not measured or unattributed where applicable. |",
        "| `data/batch3_records.json` | Canonical source record for the ten new leads. |",
        "| `data/seen_leads.json` | Updated deduplication registry and daily log, reconciled to 131 registered brands. |",
        "| `scripts/build_batch3_deliverables.py` | Incremental Batch 3 builder. Do **not** run the legacy-only `scripts/build_master_excel.py` to rebuild Batch 3. |",
        "",
        "## Batch history and data vintage",
        "",
        "| Batch | Leads | Snapshot | Status |",
        "|---|---:|---|---|",
        "| Batch 1 | 11 | 02 Oct 2026 | Legacy snapshot; preserved, not rechecked on 04 Oct. |",
        "| Batch 2 | 10 | 03 Oct 2026 | Legacy snapshot; preserved, not rechecked on 04 Oct. |",
        "| Batch 3 | 10 | 04 Oct 2026 | New source-checked batch; one selected evidence-led audit per lead. |",
        "",
        "## Batch 3 — new leads",
        "",
        "| Brand | Published email route | Google Ads status | Public-evidence fit |",
        "|---|---|---|---:|",
    ]
    for l in leads:
        rows.append(f"| {l['brand']} | `{l['contact']['email']}` | {l['google_evidence']['status']} | {l['score']} / 10 |")
    rows.extend([
        "",
        "## Evidence and scoring limits",
        "",
        "- The score is a five-dimension **public-evidence fit /20** (displayed /10) for lead triage only. It is not performance, revenue, probability, spend, forecast, conversion or ROI.",
        "- Meta citations use selected Library IDs and page IDs. A selected active card is not an account-wide inventory count. Keyword/unordered results are not treated as page ownership or ad targeting proof.",
        "- Google status is **NOT MEASURED** unless the lead JSON and guide say a domain query was checked. Where results are surfaced under another entity, attribution is recorded as unconfirmed, not as brand activity or absence.",
        "- Lead-local evidence is explicit in the creative or first-party material; no city targeting is inferred. Sagar Ratna's Bengaluru outlet remains **unconfirmed** from the locator content reviewed.",
        "- Contact email addresses were taken from the brand's own official web/help/corporate property. These are routing contacts, not verified paid-media buyers. Starbucks' dynamic first-party contact pages returned a fetch error; their official indexed content was captured and is flagged in the report.",
        "- Spend, ROAS, CPA, conversions, orders/bookings and event firing are unavailable/not measured. No estimates, benchmarks, projections or uplift claims are used in Batch 3.",
        "- The old workbook's **Legacy ROI Archive** is retained only for traceability. Its historic projections were not revalidated and are not part of Batch 3 evidence.",
        "- Ad inventory can change after the dated 04 Oct 2026 snapshot; re-open the source link before acting.",
        "",
        "## Rebuild Batch 3",
        "",
        "```bash",
        ".venv/bin/python niches/food-bengaluru/scripts/build_batch3_deliverables.py",
        "```",
        "",
        "The script validates source references, email provenance, score arithmetic, uniqueness against the registry and existing niche lead files, appends rather than rebuilds the legacy workbook, and renders the Batch 3 PDFs and exports.",
        "",
    ])
    return "\n".join(rows)


def _style_new_row(ws, row_idx, template_row=None):
    if template_row is None:
        template_row = max(1, row_idx - 1)
    for col in range(1, ws.max_column + 1):
        src = ws.cell(template_row, col)
        dst = ws.cell(row_idx, col)
        if src.has_style:
            dst._style = copy(src._style)
        if src.number_format:
            dst.number_format = src.number_format
        dst.alignment = copy(src.alignment)


def append_xlsx_row(ws, values, hyperlinks=None):
    row_idx = ws.max_row + 1
    template = max(2, row_idx - 1)
    _style_new_row(ws, row_idx, template)
    for col, value in enumerate(values, start=1):
        cell = ws.cell(row_idx, col, value)
        cell.alignment = copy(cell.alignment)
        cell.alignment = cell.alignment.copy(wrap_text=True, vertical="top")
        if hyperlinks and col in hyperlinks:
            cell.hyperlink = hyperlinks[col]
            cell.style = "Hyperlink"
    return row_idx


def add_vintage_column(ws, brand_col=1, title="Batch / data vintage", min_row=2):
    col = ws.max_column + 1
    header = ws.cell(1, col, title)
    if col > 1 and ws.cell(1, col - 1).has_style:
        header._style = copy(ws.cell(1, col - 1)._style)
    header.font = copy(header.font)
    header.font = header.font.copy(bold=True, color="FFFFFF")
    header.fill = copy(ws.cell(1, 1).fill)
    header.alignment = header.alignment.copy(wrap_text=True, vertical="center")
    for r in range(min_row, ws.max_row + 1):
        brand = ws.cell(r, brand_col).value
        cell = ws.cell(r, col)
        if brand:
            cell.value = vintage_for(str(brand))
        else:
            cell.value = "General note / cross-pack"
        cell.alignment = cell.alignment.copy(wrap_text=True, vertical="top")
    ws.column_dimensions[chr(64 + col)].width = 34 if col <= 26 else 34
    return col


def add_excel_source_hyperlink(cell, url):
    cell.hyperlink = url
    cell.style = "Hyperlink"


def build_master_workbook(data, leads):
    from openpyxl import load_workbook
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter

    wb = load_workbook(WORKBOOK)
    required = {"README", "Leads", "Emails", "Findings (severity+evidence)", "Opportunity Score",
                "Coverage (measured vs not)", "Evidence Register", "Verify These (links)",
                "Audit Basis (sources)", "Emails (one sheet)", "Expected ROI"}
    assert required.issubset(set(wb.sheetnames)), f"Workbook structure changed: missing {required - set(wb.sheetnames)}"
    if "Batch & Data Status" in wb.sheetnames:
        raise RuntimeError("Batch 3 appears already applied; refusing duplicate workbook append")

    # Preserve historical projections without presenting them as current evidence.
    roi = wb["Expected ROI"]
    roi.title = "Legacy ROI Archive"
    roi.insert_rows(1, 2)
    roi.merge_cells(start_row=1, start_column=1, end_row=1, end_column=max(5, roi.max_column))
    roi.cell(1, 1).value = "ARCHIVED LEGACY PROJECTIONS — not revalidated; not a current forecast; do not reuse as evidence."
    roi.cell(1, 1).font = Font(bold=True, color="FFFFFF", size=11)
    roi.cell(1, 1).fill = PatternFill("solid", fgColor="9B1C1C")
    roi.cell(1, 1).alignment = Alignment(wrap_text=True, vertical="center")
    roi.row_dimensions[1].height = 30
    roi.merge_cells(start_row=2, start_column=1, end_row=2, end_column=max(5, roi.max_column))
    roi.cell(2, 1).value = "Retained for traceability only from prior workbook versions. Batch 3 contains no spend, ROAS, CPA, conversion, uplift or ROI projections."
    roi.cell(2, 1).font = Font(italic=True, color="7F1D1D", size=9)
    roi.cell(2, 1).fill = PatternFill("solid", fgColor="FEF2F2")
    roi.cell(2, 1).alignment = Alignment(wrap_text=True, vertical="center")
    roi.row_dimensions[2].height = 28
    roi.freeze_panes = "A4"
    roi.sheet_view.showGridLines = False

    # Append the ten new leads; keep existing 21 untouched except for an explicit vintage field.
    ws = wb["Leads"]
    if ws.cell(1, 16).value is None:
        ws.cell(1, 16).value = "Batch / data vintage"
        ws.cell(1, 16)._style = copy(ws.cell(1, 15)._style)
        ws.column_dimensions[get_column_letter(16)].width = 34
    for r in range(2, ws.max_row + 1):
        brand = ws.cell(r, 2).value
        ws.cell(r, 16).value = vintage_for(str(brand)) if brand else ""
        ws.cell(r, 16).alignment = Alignment(wrap_text=True, vertical="top")
    lead_start = ws.max_row + 1
    for idx, l in enumerate(leads, start=lead_start - 1):
        s = l["slug"]
        contact = l["contact"]
        values = [
            idx, l["brand"], l["website"], l.get("instagram", ""), l["niche"], l["score"],
            l["ads_active"], contact.get("email", ""), contact.get("phone", ""),
            contact.get("entity", ""), contact.get("address", ""), l["contact_source"],
            f"audits/{s}-paid-media-measurement-audit.pdf",
            f"outreach/{s}-outreach-templates.md", l["verified_on"],
            "BATCH 3 — source-checked 04 OCT 2026",
        ]
        append_xlsx_row(ws, values)
    ws.auto_filter.ref = f"A1:P{ws.max_row}"

    # Append all forty email messages to the six-column detail sheet.
    ws = wb["Emails"]
    if ws.cell(1, 7).value is None:
        ws.cell(1, 7).value = "Batch / data vintage"
        ws.cell(1, 7)._style = copy(ws.cell(1, 6)._style)
        ws.column_dimensions[get_column_letter(7)].width = 34
    for r in range(2, ws.max_row + 1):
        ws.cell(r, 7).value = vintage_for(str(ws.cell(r, 1).value))
        ws.cell(r, 7).alignment = Alignment(wrap_text=True, vertical="top")
    for l in leads:
        for n, (subject, body) in enumerate(l["outreach"], start=1):
            day = ["Day 1", "Day 3", "Day 7", "Day 14"][n - 1]
            append_xlsx_row(ws, [l["brand"], n, day, subject, body.strip(), l["contact"]["email"], "BATCH 3 — checked 04 OCT 2026"])
    ws.auto_filter.ref = f"A1:G{ws.max_row}"

    # Finding rows retain raw evidence, analysis and the specific next check.
    ws = wb["Findings (severity+evidence)"]
    if ws.cell(1, 7).value is None:
        ws.cell(1, 7).value = "Next check"
        ws.cell(1, 7)._style = copy(ws.cell(1, 6)._style)
        ws.column_dimensions[get_column_letter(7)].width = 70
    if ws.cell(1, 8).value is None:
        ws.cell(1, 8).value = "Batch / data vintage"
        ws.cell(1, 8)._style = copy(ws.cell(1, 6)._style)
        ws.column_dimensions[get_column_letter(8)].width = 34
    for r in range(2, ws.max_row + 1):
        ws.cell(r, 8).value = vintage_for(str(ws.cell(r, 1).value))
        ws.cell(r, 8).alignment = Alignment(wrap_text=True, vertical="top")
    for l in leads:
        for n, f in enumerate(l["findings"], start=1):
            append_xlsx_row(ws, [l["brand"], n, f.get("priority", "NOTE").upper(), f["title"], f["evidence"], f["analysis"], f["next_check"], "BATCH 3 — checked 04 OCT 2026"])
    ws.auto_filter.ref = f"A1:H{ws.max_row}"

    # Score breakdown is explicitly a public-evidence-fit score, not a performance score.
    ws = wb["Opportunity Score"]
    if ws.cell(1, 8).value is None:
        ws.cell(1, 8).value = "Batch / data vintage"
        ws.cell(1, 8)._style = copy(ws.cell(1, 7)._style)
        ws.column_dimensions[get_column_letter(8)].width = 34
    for r in range(2, ws.max_row + 1):
        ws.cell(r, 8).value = vintage_for(str(ws.cell(r, 1).value))
        ws.cell(r, 8).alignment = Alignment(wrap_text=True, vertical="top")
    for l in leads:
        for item in l["score_breakdown"]:
            append_xlsx_row(ws, [l["brand"], item["dimension"], item["score"], item["basis"], l["score_20"], l["score_band"], l["score_note"], "BATCH 3 — checked 04 OCT 2026"])
    ws.auto_filter.ref = f"A1:H{ws.max_row}"

    # Coverage table.
    ws = wb["Coverage (measured vs not)"]
    if ws.cell(1, 6).value is None:
        ws.cell(1, 6).value = "Batch / data vintage"
        ws.cell(1, 6)._style = copy(ws.cell(1, 5)._style)
        ws.column_dimensions[get_column_letter(6)].width = 34
    for r in range(2, ws.max_row + 1):
        ws.cell(r, 6).value = vintage_for(str(ws.cell(r, 1).value))
        ws.cell(r, 6).alignment = Alignment(wrap_text=True, vertical="top")
    for l in leads:
        for c in l["coverage"]:
            append_xlsx_row(ws, [l["brand"], c["surface"], c["status"], c["method"], c["date"], "BATCH 3 — checked 04 OCT 2026"])
    ws.auto_filter.ref = f"A1:F{ws.max_row}"

    # Evidence register.
    ws = wb["Evidence Register"]
    if ws.cell(1, 6).value is None:
        ws.cell(1, 6).value = "Batch / data vintage"
        ws.cell(1, 6)._style = copy(ws.cell(1, 5)._style)
        ws.column_dimensions[get_column_letter(6)].width = 34
    for r in range(2, ws.max_row + 1):
        ws.cell(r, 6).value = vintage_for(str(ws.cell(r, 1).value))
        ws.cell(r, 6).alignment = Alignment(wrap_text=True, vertical="top")
    for l in leads:
        srcmap = {s["id"]: s for s in l["sources_detail"]}
        for ad in l.get("ad_evidence", []):
            src = srcmap[ad["source_id"]]
            observed = f"{ad['status']}; started {ad.get('started_on','not stated')}; page {ad.get('page_name','')}; copy: {ad.get('creative_excerpt','')}; CTA: {ad.get('cta','')}; destination: {ad.get('destination_status','')}"
            append_xlsx_row(ws, [l["brand"], f"Meta Library ID {ad['library_id']}", src["url"], observed, "04 OCT 2026", "BATCH 3 — checked 04 OCT 2026"])
            add_excel_source_hyperlink(ws.cell(ws.max_row, 3), src["url"])
        for src in l.get("sources_detail", []):
            append_xlsx_row(ws, [l["brand"], f"{src['id']} — {src['label']}", src["url"], src.get("observed", ""), src.get("verified_on", "2026-10-04"), "BATCH 3 — checked 04 OCT 2026"])
            add_excel_source_hyperlink(ws.cell(ws.max_row, 3), src["url"])
    ws.auto_filter.ref = f"A1:F{ws.max_row}"

    # Audit basis: one row per source with its exact URL included.
    ws = wb["Audit Basis (sources)"]
    if ws.cell(1, 3).value is None:
        ws.cell(1, 3).value = "Batch / data vintage"
        ws.cell(1, 3)._style = copy(ws.cell(1, 2)._style)
        ws.column_dimensions[get_column_letter(3)].width = 34
    for r in range(2, ws.max_row + 1):
        ws.cell(r, 3).value = vintage_for(str(ws.cell(r, 1).value))
        ws.cell(r, 3).alignment = Alignment(wrap_text=True, vertical="top")
    for l in leads:
        for src in l.get("sources_detail", []):
            text = f"{src['id']} — {src['label']}. Observed: {src.get('observed','')} URL: {src['url']}"
            row = append_xlsx_row(ws, [l["brand"], text, "BATCH 3 — checked 04 OCT 2026"])
            ws.cell(row, 2).hyperlink = src["url"]
            ws.cell(row, 2).style = "Hyperlink"
    ws.auto_filter.ref = f"A1:C{ws.max_row}"

    # Claim-by-claim links, plus one row per source so provenance is preserved.
    ws = wb["Verify These (links)"]
    if ws.cell(1, 6).value is None:
        ws.cell(1, 6).value = "Batch / data vintage"
        ws.cell(1, 6)._style = copy(ws.cell(1, 5)._style)
        ws.column_dimensions[get_column_letter(6)].width = 34
    for r in range(2, ws.max_row + 1):
        ws.cell(r, 6).value = vintage_for(str(ws.cell(r, 1).value))
        ws.cell(r, 6).alignment = Alignment(wrap_text=True, vertical="top")
    for l in leads:
        srcmap = {s["id"]: s for s in l.get("sources_detail", [])}
        for src in l.get("sources_detail", []):
            row = append_xlsx_row(ws, [l["brand"], f"{src['id']} — {src['label']}", src["source_type"], src["url"], src.get("observed", ""), "BATCH 3 — checked 04 OCT 2026"], hyperlinks={4: src["url"]})
        for f in l.get("findings", []):
            for sid in f.get("source_ids", []):
                src = srcmap[sid]
                row = append_xlsx_row(ws, [l["brand"], f["title"], f"Supporting finding source {sid}", src["url"], f"{f['evidence']} Analysis: {f['analysis']} Next check: {f['next_check']}", "BATCH 3 — checked 04 OCT 2026"], hyperlinks={4: src["url"]})
    ws.auto_filter.ref = f"A1:F{ws.max_row}"

    # Multi-email export in the master workbook.
    ws = wb["Emails (one sheet)"]
    if ws.cell(1, 9).value is None:
        ws.cell(1, 9).value = "Batch / data vintage"
        ws.cell(1, 9)._style = copy(ws.cell(1, 8)._style)
        ws.column_dimensions[get_column_letter(9)].width = 34
    for r in range(2, ws.max_row + 1):
        ws.cell(r, 9).value = vintage_for(str(ws.cell(r, 1).value))
        ws.cell(r, 9).alignment = Alignment(wrap_text=True, vertical="top")
    for l in leads:
        subjects = "\n".join(f"{day}: {x[0]}" for day, x in zip(["Day 1", "Day 3", "Day 7", "Day 14"], l["outreach"]))
        bodies = [x[1].strip() for x in l["outreach"]]
        append_xlsx_row(ws, [l["brand"], l["contact"]["email"], subjects, *bodies, f"{l['slug']}-paid-media-measurement-audit.pdf", "BATCH 3 — checked 04 OCT 2026"])
    ws.auto_filter.ref = f"A1:I{ws.max_row}"

    # Archive the previous ROI sheet explicitly; also label legacy alternative/roadmap notes.
    for title in ("Leaks & Roadmap", "You vs Competitor"):
        if title in wb.sheetnames:
            sh = wb[title]
            add_vintage_column(sh, brand_col=1)

    # Add method notes for the evidence-only batch without altering legacy skill rows.
    ws = wb["Skills Used"]
    for values in [
        ["Batch 3 public-source QA", "claude-ads / ads-audit; ads-attribution", "Scoped claims to selected, page-resolved public records; recorded source IDs, dates, attribution limits and missing private inputs. No platform performance score was inferred."],
        ["Batch 3 contact provenance", "lead-scraper contact-enrichment principle; official brand pages only", "Each new email is tied to an official brand/help/corporate URL in contact_source and source IDs; no third-party or guessed contact was used."],
        ["Batch 3 outreach", "coldoutboundskills / cold-email-starter-kit; campaign-copywriting", "Four concise Day 1/3/7/14 messages per lead; personalization uses only checked public copy and asks for routing rather than assuming a buyer."],
        ["Batch 3 evidence boundary", "marketingskills / analytics; claude-ads / ads-attribution", "Private account, booking, order and event data are marked unavailable/not measured; no projection, conversion benchmark or assumed tracking event."],
    ]:
        append_xlsx_row(ws, values)

    # A visible one-row-per-lead batch-vintage index makes mixed historical/new sheets explicit.
    status = wb.create_sheet("Batch & Data Status")
    status.append(["Brand", "Batch", "Snapshot date", "Status", "Audit / scoring basis", "Notes"])
    legacy_order = []
    if "Leads" in wb.sheetnames:
        leads_sheet = wb["Leads"]
        for r in range(2, leads_sheet.max_row + 1):
            brand = leads_sheet.cell(r, 2).value
            if brand:
                legacy_order.append((brand, leads_sheet.cell(r, 15).value))
    for brand, vdate in legacy_order:
        if not any(norm_name(brand) == norm_name(x) for x in (LEGACY_BATCH1 | LEGACY_BATCH2)):
            continue
        batch = "Batch 1" if any(norm_name(brand) == norm_name(x) for x in LEGACY_BATCH1) else "Batch 2"
        status.append([brand, batch, vdate, "LEGACY — not revalidated on 04 OCT 2026", "Prior report format / prior scoring; not directly comparable to Batch 3", "Existing data retained; refer to its dated audit and source guide."])
    for l in leads:
        status.append([l["brand"], "Batch 3", "04 OCT 2026", "NEW — source-checked 04 OCT 2026", "5-page evidence-only audit; public-evidence fit /20 and /10", "Ad status and public pages are dated snapshots; private outcomes not measured."])
    for cell in status[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor=NAVY)
        cell.alignment = Alignment(wrap_text=True, vertical="center")
    status.row_dimensions[1].height = 28
    for row in status.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.border = Border(bottom=Side(style="hair", color="D8DEE8"))
        if str(row[3].value).startswith("LEGACY"):
            row[3].fill = PatternFill("solid", fgColor="FEF3C7")
        else:
            row[3].fill = PatternFill("solid", fgColor="D1FAE5")
    for c, width in enumerate([25, 12, 18, 38, 56, 70], 1):
        status.column_dimensions[get_column_letter(c)].width = width
    status.freeze_panes = "A2"
    status.auto_filter.ref = status.dimensions
    status.sheet_view.showGridLines = False

    # Rewrite the README sheet; preserve any embedded logo at D2 if present.
    ws = wb["README"]
    for row in ws.iter_rows():
        for cell in row:
            cell.value = None
    readme_rows = [
        ["SMART PURSUIT — FOOD / BENGALURU EVIDENCE PACK", ""],
        ["31 leads · 31 reports · 124 email messages. Batch 3 adds 10 new leads checked on 04 OCT 2026; earlier records remain legacy snapshots.", ""],
        ["DATA VINTAGE", ""],
        ["Batch 1 + Batch 2", "21 prior leads captured 02–03 OCT 2026. Not revalidated in this Batch 3 update. The per-row vintage column and Batch & Data Status sheet mark this clearly."],
        ["Batch 3", "10 new leads, source-checked 04 OCT 2026. Ten new 5-page evidence-focused audit PDFs, 40 new emails, 30 findings and five-dimension public-evidence-fit scores."],
        ["Score comparability", "Batch 3 public-evidence-fit score is triage only (five dimensions, /20, displayed /10). Do not compare it with the legacy opportunity scores."],
        ["Workbook inventory", "Leads · Emails · Findings · Opportunity Score · Coverage · Evidence Register · Verify These · Audit Basis · 1-sheet email export · Batch & Data Status."],
        ["Legacy ROI content", "Expected ROI has been renamed Legacy ROI Archive and is flagged unverified/not a current forecast. No Batch 3 projections are added."],
        ["Lead and source integrity", "Every Batch 3 email route is tied to a first-party URL in contact_source; each ad claim has a direct Library ID/page ID source. See the Verify These sheet and VERIFY-THE-DATA.md."],
        ["Limits", "Spend, ROAS, CPA, conversion outcomes and event firing are unavailable/not measured unless explicitly sourced. No estimate, benchmark or expected-uplift claim is made for Batch 3."],
        ["Meta scope", "Selected active cards only; not account-wide totals. Keyword/unordered search results do not prove page ownership or targeting. Inventory changes daily."],
        ["Local scope", "City relevance comes from explicit creative or first-party material; no audience geography is inferred. Sagar Ratna's current Bengaluru outlet is unconfirmed from the locator content reviewed."],
        ["Source index", "All 10 Batch 3 leads, evidence, contacts, findings, scores, and email copy are present in the workbook. `Batch & Data Status` marks all 31 records."],
        ["Build", "Use niches/food-bengaluru/scripts/build_batch3_deliverables.py. Do not run the legacy-only build_master_excel.py to rebuild this mixed workbook."],
    ]
    for r, row in enumerate(readme_rows, start=1):
        for c, value in enumerate(row, start=1):
            ws.cell(r, c, value)
    ws["A1"].font = Font(bold=True, size=14, color=NAVY)
    for r in range(2, len(readme_rows) + 1):
        ws.cell(r, 1).font = Font(bold=True, color=TEAL if r in (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14) else NAVY)
        ws.cell(r, 2).alignment = Alignment(wrap_text=True, vertical="top")
    for r in range(1, len(readme_rows) + 1):
        ws.row_dimensions[r].height = 34 if r > 2 else 28
    ws.column_dimensions["A"].width = 28
    ws.column_dimensions["B"].width = 108
    ws.sheet_view.showGridLines = False

    # Make other sheet titles and headers explicit; preserve prior rows as archived snapshots.
    wb.calculation.fullCalcOnLoad = True
    wb.calculation.forceFullCalc = True
    wb.save(WORKBOOK)


def update_email_exports(leads):
    from openpyxl import load_workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter

    # Append to the existing standalone email workbook, preserving old messages.
    wb = load_workbook(EMAIL_WORKBOOK)
    ws = wb["Emails"]
    if ws.cell(1, 9).value is None:
        ws.cell(1, 9).value = "Batch / data vintage"
        ws.cell(1, 9)._style = copy(ws.cell(1, 8)._style)
        ws.column_dimensions[get_column_letter(9)].width = 34
    for r in range(2, ws.max_row + 1):
        ws.cell(r, 9).value = vintage_for(str(ws.cell(r, 1).value))
        ws.cell(r, 9).alignment = Alignment(wrap_text=True, vertical="top")
    for l in leads:
        subjects = "\n".join(f"{day}: {item[0]}" for day, item in zip(["Day 1", "Day 3", "Day 7", "Day 14"], l["outreach"]))
        bodies = [item[1].strip() for item in l["outreach"]]
        append_xlsx_row(ws, [l["brand"], l["contact"]["email"], subjects, *bodies, f"{l['slug']}-paid-media-measurement-audit.pdf", "BATCH 3 — checked 04 OCT 2026"])
    ws.auto_filter.ref = f"A1:I{ws.max_row}"
    wb.save(EMAIL_WORKBOOK)

    # CSV is a flat export of the same one-row-per-brand sequence sheet.
    all_rows = []
    for l in leads:
        subjects = "\n".join(f"{day}: {item[0]}" for day, item in zip(["Day 1", "Day 3", "Day 7", "Day 14"], l["outreach"]))
        bodies = [item[1].strip() for item in l["outreach"]]
        all_rows.append([l["brand"], l["contact"]["email"], subjects, *bodies, f"{l['slug']}-paid-media-measurement-audit.pdf", "BATCH 3 — checked 04 OCT 2026"])
    with EMAIL_CSV.open("r", newline="", encoding="utf-8-sig") as f:
        old = list(csv.reader(f))
    if old and len(old[0]) == 9 and any("BATCH 3 — checked 04 OCT 2026" in row for row in old[1:]):
        raise RuntimeError("Batch 3 email CSV rows already exist; refusing duplicate append")
    if old and len(old[0]) == 8:
        old[0].append("Batch / data vintage")
        for row in old[1:]:
            if len(row) == 8:
                row.append(vintage_for(row[0]))
    with EMAIL_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(old)
        writer.writerows(all_rows)


def build_batch3_email_workbook(leads):
    """Write a clean, one-sheet Batch 3 email export with the requested 8 columns."""
    import math
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.worksheet.table import Table, TableStyleInfo

    wb = Workbook()
    ws = wb.active
    ws.title = "Batch 3 Email Sequences"
    headers = [
        "Brand name", "Email", "Subject", "Body 1", "Body 2", "Body 3", "Body 4", "Attachment Name",
    ]
    ws.append(headers)
    days = ["Day 1", "Day 3", "Day 7", "Day 14"]
    for lead in leads:
        subjects = "\n".join(f"{day}: {item[0]}" for day, item in zip(days, lead["outreach"]))
        bodies = [str(item[1]).replace("\r\n", "\n").strip() for item in lead["outreach"]]
        ws.append([
            lead["brand"], lead["contact"]["email"], subjects, *bodies,
            f"{lead['slug']}-paid-media-measurement-audit.pdf",
        ])

    widths = {"A": 25, "B": 36, "C": 48, "D": 64, "E": 64, "F": 64, "G": 64, "H": 52}
    for col, width in widths.items():
        ws.column_dimensions[col].width = width
    navy_fill = PatternFill("solid", fgColor=NAVY)
    white_bold = Font(name="Aptos", size=10, bold=True, color=WHITE)
    body_font = Font(name="Aptos", size=10, color=INK)
    brand_font = Font(name="Aptos", size=10, bold=True, color=TEAL)
    edge = Side(style="hair", color=RULE)
    cell_border = Border(bottom=edge, right=edge)
    for cell in ws[1]:
        cell.fill = navy_fill
        cell.font = white_bold
        cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        cell.border = Border(bottom=Side(style="medium", color=GOLD))
    ws.row_dimensions[1].height = 30
    for row_index in range(2, ws.max_row + 1):
        max_lines = 1
        for col_index in range(1, 9):
            cell = ws.cell(row_index, col_index)
            cell.font = brand_font if col_index == 1 else body_font
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            cell.border = cell_border
            text = str(cell.value or "")
            width = widths[ws.cell(1, col_index).column_letter]
            chars_per_line = max(24, int(width * 1.08))
            visual_lines = sum(
                max(1, math.ceil(len(line) / chars_per_line))
                for line in text.replace("\r\n", "\n").split("\n")
            )
            max_lines = max(max_lines, visual_lines)
        ws.row_dimensions[row_index].height = min(420, max(150, max_lines * 12 + 18))

    ws.freeze_panes = "C2"
    ws.auto_filter.ref = f"A1:H{ws.max_row}"
    ws.sheet_view.showGridLines = False
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.tabColor = TEAL
    table = Table(displayName="Batch3EmailSequence", ref=f"A1:H{ws.max_row}")
    table.tableStyleInfo = TableStyleInfo(
        name="TableStyleMedium2", showFirstColumn=False, showLastColumn=False,
        showRowStripes=True, showColumnStripes=False,
    )
    ws.add_table(table)
    wb.properties.title = "Food / Bengaluru — Batch 3 Email Sequences"
    wb.properties.subject = "Ten source-checked Batch 3 leads with four outreach emails each"
    wb.properties.creator = "Smart Pursuit"
    wb.save(BATCH3_EMAIL_WORKBOOK)


def update_leads_csv(leads):
    rows = []
    with LEADS_CSV.open("r", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)
    if any(norm_name(r.get("brand", "")) in {norm_name(l["brand"]) for l in leads} for r in rows):
        raise RuntimeError("Batch 3 brand already exists in LEADS-INDEX.csv")
    if "batch" not in fieldnames:
        fieldnames.append("batch")
    if "data_vintage" not in fieldnames:
        fieldnames.append("data_vintage")
    for row in rows:
        row["batch"] = "Batch 1" if any(norm_name(row.get("brand", "")) == norm_name(x) for x in LEGACY_BATCH1) else "Batch 2"
        row["data_vintage"] = vintage_for(row.get("brand", ""))
    for l in leads:
        rows.append({
            "brand": l["brand"], "website": l["website"], "niche": l["niche"],
            "score": l["score"], "google_ads_live": l["ads_active"],
            "lead_email": l["contact"]["email"], "lead_phone": l["contact"].get("phone", ""),
            "contact_entity": l["contact"].get("entity", ""),
            "audit_pdf": f"audits/{l['slug']}-paid-media-measurement-audit.pdf",
            "outreach_md": f"outreach/{l['slug']}-outreach-templates.md",
            "verified_on": l["verified_on"], "batch": "Batch 3",
            "data_vintage": "BATCH 3 — source-checked 04 OCT 2026",
        })
    with LEADS_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def reconcile_registry(leads, registry):
    brands = registry.setdefault("brands", {})
    now_entries = []
    for l in leads:
        key = l["brand"]
        assert key not in brands, f"Registry already contains {key}"
        entry = {
            "first_seen": "2026-10-04T00:00:00",
            "day": 5,
            "website": l["website"],
            "niche": f"Food/Bengaluru/{l['niche']}",
        }
        brands[key] = entry
        now_entries.append(key)
    # Reconcile the previously missing Batch 2 entry in the daily log, then log Batch 3.
    daily = registry.setdefault("daily_log", [])
    if not any(int(x.get("day", -1)) == 4 for x in daily):
        daily.append({
            "day": 4, "date": "2026-10-03", "niche": "Food/Bengaluru",
            "count": 10, "total_so_far": 121,
            "brands": ["SMOOR", "Sid's Farm", "Barbeque Nation", "Millet Amma", "Adukale", "Organic Mandya", "Pure & Sure", "Eat Better Co", "Brik Oven", "Araku Coffee"],
            "note": "Reconciled from Batch 2 brand entries already present in brands; prior daily_log had omitted this entry.",
        })
    if not any(int(x.get("day", -1)) == 5 for x in daily):
        daily.append({
            "day": 5, "date": "2026-10-04", "niche": "Food/Bengaluru",
            "count": len(now_entries), "total_so_far": len(brands), "brands": now_entries,
        })
    registry["total_found"] = len(brands)
    REGISTRY.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def validate_emails_and_sources(leads):
    for l in leads:
        emails = l["outreach"]
        assert len(emails) == 4
        # Support route must remain inside email copy and match the public source record.
        assert l["contact"]["email"] in l["contact_source"]
        for subj, body in emails:
            assert "smartpursuit3@gmail.com" in body and "7095024220" in body, l["brand"]
        # No performance outcome or forecast is permitted as a claim. These terms may appear
        # only in explicit not-measured/unavailable guardrails.
        for subj, body in emails:
            text = (subj + " " + body).casefold()
            for forbidden in ("expected roi", "guaranteed roas", "increase roas by", "reduce cpa by", "conversion rate will"):
                assert forbidden not in text, f"Unpermitted claim in {l['brand']}: {forbidden}"


def main():
    data = load_data()
    leads = data["leads"]
    registry = check_deduplication(leads)
    validate_emails_and_sources(leads)

    write_json_and_outreach(leads)
    generate_pdfs(leads)
    append_verify_guide(leads)
    all_email_text = ALL_EMAILS_MD.read_text(encoding="utf-8")
    email_marker = "\n\n---\n\n# Batch 3 — Food / Bengaluru (checked 04 Oct 2026)"
    if email_marker in all_email_text:
        all_email_text = all_email_text[:all_email_text.index(email_marker)].rstrip()
    ALL_EMAILS_MD.write_text(all_email_text + build_all_email_appendix(leads), encoding="utf-8")
    build_master_workbook(data, leads)
    update_email_exports(leads)
    build_batch3_email_workbook(leads)
    update_leads_csv(leads)
    reconcile_registry(leads, registry)
    README_MD.write_text(build_readme(leads), encoding="utf-8")

    print(f"Rendered {len(leads)} leads, {len(leads) * 4} emails, {len(leads)} PDFs.")
    print(f"Updated master workbook: {WORKBOOK}")
    print(f"Updated registry: {len(registry['brands'])} unique entries.")


if __name__ == "__main__":
    main()
