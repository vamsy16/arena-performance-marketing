# -*- coding: utf-8 -*-
"""
Smart Pursuit ATTRACTIVE audit PDF (2 pages) - matches the house format used in
away-* repos (metrics row -> YOU vs COMPETITOR -> 3 LEAKS -> 3 QUICK WINS roadmap
-> EXPECTED ROI -> live-data basis -> dark CTA).

Content is built from the repository skills:
  performance-lead-audit orchestrating ads, ad-creative, copywriting, cro,
  analytics/attribution, competitor-profiling, cold-email.
"""
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether)

# ---------------------------------------------------------------- design tokens
NAVY      = colors.HexColor("#0F172A")
NAVY_SOFT = colors.HexColor("#1E293B")
GRAY_TXT  = colors.HexColor("#475569")
GRAY_LT   = colors.HexColor("#F8FAFC")
BORDER    = colors.HexColor("#E2E8F0")
RED       = colors.HexColor("#EF4444")
RED_DARK  = colors.HexColor("#B91C1C")
RED_BG    = colors.HexColor("#FFF1F2")
RED_BRD   = colors.HexColor("#FECDD3")
GREEN     = colors.HexColor("#10B981")
GREEN_DK  = colors.HexColor("#047857")
GREEN_BG  = colors.HexColor("#ECFDF5")
GREEN_BRD = colors.HexColor("#A7F3D0")
AMBER     = colors.HexColor("#F59E0B")
PURPLE_BG = colors.HexColor("#F5F3FF")
PURPLE_DK = colors.HexColor("#5B21B6")

AGENCY   = "SMART PURSUIT"
PHONE    = "7095024220"
EMAIL    = "smartpursuit3@gmail.com"
SKILLS   = "Built with repo skills: performance-lead-audit + ads, ad-creative, copywriting, cro, analytics/attribution, competitor-profiling, cold-email."

def esc(t):
    return (str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace("&amp;b&gt;", "<b>").replace("&amp;/b&gt;", "</b>"))

def _s():
    return {
        "TOPLINE": ParagraphStyle("tl", fontName="Helvetica", fontSize=6.6, leading=8,
                                  textColor=NAVY_SOFT, alignment=TA_LEFT),
        "H1": ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=20, leading=22.5,
                             textColor=NAVY, spaceAfter=1),
        "SUB": ParagraphStyle("sub", fontName="Helvetica", fontSize=8.6, leading=10.6,
                              textColor=GRAY_TXT),
        "METNUM": ParagraphStyle("mn", fontName="Helvetica-Bold", fontSize=19, leading=20,
                                 textColor=NAVY, alignment=TA_CENTER),
        "METLAB": ParagraphStyle("ml", fontName="Helvetica-Bold", fontSize=5.6, leading=7,
                                 textColor=GRAY_TXT, alignment=TA_CENTER),
        "H2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=10.5, leading=12.5,
                             textColor=NAVY, spaceBefore=2, spaceAfter=3),
        "BOXT": ParagraphStyle("bt", fontName="Helvetica-Bold", fontSize=7.4, leading=9,
                               textColor=NAVY),
        "BOXD": ParagraphStyle("bd", fontName="Helvetica", fontSize=7.1, leading=9.1,
                               textColor=GRAY_TXT),
        "LEAKT": ParagraphStyle("lt", fontName="Helvetica-Bold", fontSize=7.6, leading=9.2,
                                textColor=RED_DARK),
        "LEAKD": ParagraphStyle("ld", fontName="Helvetica", fontSize=7.1, leading=9.1,
                                textColor=GRAY_TXT),
        "WINT": ParagraphStyle("wt", fontName="Helvetica-Bold", fontSize=7.6, leading=9.2,
                               textColor=GREEN_DK),
        "WIND": ParagraphStyle("wd", fontName="Helvetica", fontSize=7.1, leading=9.1,
                               textColor=GRAY_TXT),
        "CELL": ParagraphStyle("c", fontName="Helvetica", fontSize=6.8, leading=8.6,
                               textColor=GRAY_TXT),
        "CELLB": ParagraphStyle("cb", fontName="Helvetica-Bold", fontSize=6.9, leading=8.6,
                                textColor=NAVY),
        "BASIS": ParagraphStyle("bs", fontName="Helvetica", fontSize=6.6, leading=8.4,
                                textColor=GRAY_TXT),
        "CTA": ParagraphStyle("cta", fontName="Helvetica-Bold", fontSize=11.5, leading=13.5,
                              textColor=colors.white, alignment=TA_CENTER),
        "CTAB": ParagraphStyle("ctab", fontName="Helvetica", fontSize=8.2, leading=10.4,
                               textColor=colors.HexColor("#E2E8F0"), alignment=TA_CENTER),
        "CTAC": ParagraphStyle("ctac", fontName="Helvetica-Bold", fontSize=9, leading=11,
                               textColor=colors.white, alignment=TA_CENTER),
    }

def _box(rows, bg, brd, width=186*mm):
    t = Table(rows, colWidths=[width])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("BOX", (0,0), (-1,-1), 0.6, brd),
        ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 3.5), ("BOTTOMPADDING", (0,0), (-1,-1), 3.5),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    return t

def build_pdf(lead: dict, out_pdf: Path) -> Path:
    S = _s()
    L = lead
    stats = L.get("stats", [])
    story = []

    # ---------------- header
    top = (f"FOR: <b>{esc(L['brand']).upper()}</b> &nbsp;•&nbsp; {esc(L.get('niche',''))} "
           f"&nbsp;•&nbsp; CONFIDENTIAL PERFORMANCE AUDIT &nbsp;•&nbsp; {AGENCY}")
    story.append(Paragraph(top, S["TOPLINE"]))
    story.append(Spacer(1, 2.2*mm))
    story.append(Paragraph(esc(L["headline"]), S["H1"]))
    sub = (f"We found <b>3 leaks</b> costing you ad efficiency + conversions &nbsp;•&nbsp; "
           f"Lead score <b>{L.get('score','?')}/10 HOT</b> &nbsp;•&nbsp; {L.get('roadmap_days', 14)}-Day Fix Roadmap")
    story.append(Paragraph(sub, S["SUB"]))
    story.append(Spacer(1, 3*mm))

    # ---------------- metrics row (4 boxes, last is navy score)
    cells = []
    for i, (num, lab) in enumerate(stats[:3]):
        cells.append(Table([[Paragraph(esc(num), S["METNUM"])],
                            [Paragraph(esc(lab).upper(), S["METLAB"])]],
                           colWidths=[42*mm],
                           style=TableStyle([
                               ("BACKGROUND", (0,0), (-1,-1), colors.white),
                               ("BOX", (0,0), (-1,-1), 0.7, BORDER),
                               ("TOPPADDING", (0,0), (-1,0), 4), ("BOTTOMPADDING", (0,0), (-1,0), 0),
                               ("TOPPADDING", (0,1), (-1,1), 0), ("BOTTOMPADDING", (0,1), (-1,1), 4),
                               ("LEFTPADDING", (0,0), (-1,-1), 2), ("RIGHTPADDING", (0,0), (-1,-1), 2),
                           ])))
    score_cell = Table([[Paragraph(f"<font color='#FFFFFF'>{L.get('score','?')}/10</font>", S["METNUM"])],
                        [Paragraph("<font color='#CBD5E1'>LEAD SCORE</font>", S["METLAB"])]],
                       colWidths=[42*mm],
                       style=TableStyle([
                           ("BACKGROUND", (0,0), (-1,-1), NAVY),
                           ("TOPPADDING", (0,0), (-1,0), 4), ("BOTTOMPADDING", (0,0), (-1,0), 0),
                           ("TOPPADDING", (0,1), (-1,1), 0), ("BOTTOMPADDING", (0,1), (-1,1), 4),
                       ]))
    row = Table([[cells[0], cells[1], cells[2], score_cell]],
                colWidths=[45*mm, 45*mm, 45*mm, 45*mm])
    row.setStyle(TableStyle([("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 0),
                             ("VALIGN", (0,0), (-1,-1), "MIDDLE")]))
    story.append(row)
    story.append(Spacer(1, 4*mm))

    # ---------------- YOU vs COMPETITOR
    story.append(Paragraph(f"YOU vs COMPETITOR ({esc(L.get('vs_who','category leaders'))})", S["H2"]))
    you_rows = [[Paragraph(f"<font color='#FFFFFF'><b>YOU</b> — {esc(L['brand'])}</font>", S["BOXT"])]]
    for b in L.get("you", []):
        you_rows.append([Paragraph("&#9642; " + esc(b), S["BOXD"])])
    comp_rows = [[Paragraph(f"<font color='#FFFFFF'><b>COMPETITOR</b> — {esc(L.get('vs_who','category leaders'))}</font>", S["BOXT"])]]
    for b in L.get("competitor", []):
        comp_rows.append([Paragraph("&#9642; " + esc(b), S["BOXD"])])
    you_box = Table(you_rows, colWidths=[91*mm], style=TableStyle([
        ("BACKGROUND", (0,0), (0,0), RED),
        ("BACKGROUND", (0,1), (0,-1), RED_BG),
        ("BOX", (0,0), (-1,-1), 0.6, RED_BRD),
        ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 3), ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("VALIGN", (0,0), (-1,-1), "TOP")]))
    comp_box = Table(comp_rows, colWidths=[91*mm], style=TableStyle([
        ("BACKGROUND", (0,0), (0,0), GREEN),
        ("BACKGROUND", (0,1), (0,-1), GREEN_BG),
        ("BOX", (0,0), (-1,-1), 0.6, GREEN_BRD),
        ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 3), ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("VALIGN", (0,0), (-1,-1), "TOP")]))
    vs = Table([[you_box, comp_box]], colWidths=[94*mm, 94*mm])
    vs.setStyle(TableStyle([("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 0),
                            ("VALIGN", (0,0), (-1,-1), "TOP")]))
    story.append(vs)
    story.append(Spacer(1, 4*mm))

    # ---------------- 3 LEAKS
    story.append(Paragraph("3 LEAKS WE FOUND (live-verified)", S["H2"]))
    for i, (t, d) in enumerate(L.get("leaks", [])[:3], 1):
        story.append(KeepTogether(_box(
            [[Paragraph(f"LEAK {i}: {esc(t)}", S["LEAKT"])], [Paragraph(esc(d), S["LEAKD"])]],
            RED_BG, RED_BRD)))
        story.append(Spacer(1, 1.6*mm))

    # ---------------- 3 QUICK WINS
    story.append(Spacer(1, 1.6*mm))
    story.append(Paragraph(f"3 QUICK WINS ({L.get('roadmap_days',14)}-DAY ROADMAP) → FIX LEAKS + LOWER CPA",
                           S["H2"]))
    for day, t, d in L.get("roadmap", [])[:3]:
        story.append(KeepTogether(_box(
            [[Paragraph(f"{esc(day)}: {esc(t)}", S["WINT"])], [Paragraph(esc(d), S["WIND"])]],
            GREEN_BG, GREEN_BRD)))
        story.append(Spacer(1, 1.6*mm))

    # ---------------- EXPECTED ROI (page 2)
    from reportlab.platypus import PageBreak
    story.append(PageBreak())
    story.append(Paragraph(f"EXPECTED ROI IN {L.get('roadmap_days',14)} DAYS", S["H2"]))
    hdr = ["METRIC", "BEFORE (LIVE)", f"AFTER {L.get('roadmap_days',14)} DAYS", "INDUSTRY BENCHMARK"]
    rows = [[Paragraph(f"<font color='#FFFFFF'><b>{h}</b></font>", S["CELLB"]) for h in hdr]]
    for r in L.get("roi", [])[:4]:
        rows.append([Paragraph(esc(r[0]), S["CELLB"]), Paragraph(esc(r[1]), S["CELL"]),
                     Paragraph(esc(r[2]), S["CELL"]), Paragraph(esc(r[3]), S["CELL"])])
    rt = Table(rows, colWidths=[46*mm, 46*mm, 46*mm, 48*mm])
    rt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), NAVY),
        ("BACKGROUND", (0,1), (-1,-1), GRAY_LT),
        ("BOX", (0,0), (-1,-1), 0.6, BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.4, BORDER),
        ("LEFTPADDING", (0,0), (-1,-1), 5), ("RIGHTPADDING", (0,0), (-1,-1), 5),
        ("TOPPADDING", (0,0), (-1,-1), 3.5), ("BOTTOMPADDING", (0,0), (-1,-1), 3.5),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    story.append(rt)
    story.append(Paragraph(
        "Benchmarks are published industry ranges (e.g. e-commerce landing-page lift), labelled as such - "
        "no client results are invented. Your numbers are the live-verified values in the BEFORE column.",
        S["BASIS"]))
    story.append(Spacer(1, 4*mm))

    # ---------------- AUDIT BASIS
    if L.get("sources"):
        story.append(Paragraph("AUDIT BASIS — LIVE DATA CHECKED ON " + L.get("verified_on", ""), S["H2"]))
        src = [[Paragraph("&#9642; " + esc(x), S["BASIS"])] for x in L["sources"]]
        st = Table(src, colWidths=[186*mm], style=TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), PURPLE_BG),
            ("BOX", (0,0), (-1,-1), 0.6, colors.HexColor("#DDD6FE")),
            ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
            ("TOPPADDING", (0,0), (-1,-1), 1.4), ("BOTTOMPADDING", (0,0), (-1,-1), 1.4)]))
        story.append(st)
        story.append(Spacer(1, 1.6*mm))
        story.append(Paragraph(SKILLS, S["BASIS"]))
        story.append(Spacer(1, 3.5*mm))

    # ---------------- guarantee + CTA
    story.append(Paragraph(
        "<b>Our commitment:</b> if the agreed fixes are implemented with us and the primary metric "
        "(CPA or landing conversion) has not improved within the roadmap window, we work the next two weeks free.",
        S["BASIS"]))
    story.append(Spacer(1, 3.5*mm))
    cta = Table([
        [Paragraph("READY TO FIX THESE 3 LEAKS?", S["CTA"])],
        [Paragraph(f"{esc(L['brand'])} — book a 15-minute call. We will walk your 3 leaks, the "
                   f"{L.get('roadmap_days',14)}-day roadmap, and record a 3-minute Loom of your funnel.", S["CTAB"])],
        [Paragraph(f"Call / WhatsApp: {PHONE} &nbsp;|&nbsp; Email: {EMAIL}", S["CTAC"])],
        [Paragraph("— Smart Pursuit Performance Team", S["CTAB"])],
    ], colWidths=[186*mm])
    cta.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), NAVY),
        ("TOPPADDING", (0,0), (-1,0), 7), ("BOTTOMPADDING", (0,-1), (-1,-1), 7),
        ("TOPPADDING", (0,1), (-1,-1), 2), ("BOTTOMPADDING", (0,0), (-1,-2), 2),
    ]))
    story.append(cta)

    # ---------------- doc
    def footer(canv, doc):
        canv.saveState()
        canv.setFont("Helvetica", 6.4)
        canv.setFillColor(GRAY_TXT)
        canv.drawCentredString(A4[0]/2, 7*mm,
            f"Prepared by {AGENCY.title()}  |  Ph: {PHONE}  |  Email: {EMAIL}  |  "
            f"Confidential audit for {L['brand']}  |  Live data verified {L.get('verified_on','')}  |  Page {doc.page}")
        canv.restoreState()

    doc = BaseDocTemplate(str(out_pdf), pagesize=A4,
                          leftMargin=12*mm, rightMargin=12*mm, topMargin=10*mm, bottomMargin=12*mm,
                          title=f"{L['brand']} - Performance Audit by Smart Pursuit",
                          author="Smart Pursuit")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=footer)])
    doc.build(story)
    return out_pdf
