# -*- coding: utf-8 -*-
"""
Smart Pursuit "Paid Media & Measurement Audit" generator.
Matches the house evidence-only format (7 pages): navy cover with metric cards,
contents + method, live ad-account table, severity-ranked findings with the raw
measurement quoted, opportunity score (5 dims x 4 = 20), qualification, and
effort-ordered next steps.

Everything printed must come from a real measurement recorded in the lead data.
"""
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether, PageBreak,
                                NextPageTemplate, CondPageBreak, Image)

# ------------------------------------------------------------------ tokens
NAVY      = colors.HexColor("#0B1B2B")
TEAL      = colors.HexColor("#0E7C7B")
TEAL_LT   = colors.HexColor("#8FD6D4")
AMBER     = colors.HexColor("#F0A500")
BG_LT     = colors.HexColor("#F4F7FA")
BORDER    = colors.HexColor("#E8EDF3")
MUTED     = colors.HexColor("#5F6B7A")
MUTED_2   = colors.HexColor("#93A6BA")
SUB       = colors.HexColor("#C6D3E0")
WHITE     = colors.white

SEV = {
    "CRITICAL": (colors.HexColor("#FEE2E2"), colors.HexColor("#DC2626"), colors.HexColor("#DC2626")),
    "HIGH":     (colors.HexColor("#FFEDD5"), colors.HexColor("#EA580C"), colors.HexColor("#EA580C")),
    "MEDIUM":   (colors.HexColor("#FEF3C7"), colors.HexColor("#B45309"), colors.HexColor("#F59E0B")),
    "LOW":      (colors.HexColor("#E0E7FF"), colors.HexColor("#4338CA"), colors.HexColor("#6366F1")),
    "NOTE":     (colors.HexColor("#E8EDF3"), colors.HexColor("#475569"), colors.HexColor("#94A3B8")),
}

AGENCY = "Smart Pursuit"
TOTAL = [7]   # page total used in the footer; corrected by a second pass if needed
EMAIL  = "smartpursuit3@gmail.com"
PHONE  = "7095024220"

def _s():
    return {
        "cover_eyebrow": ParagraphStyle("ce", fontName="Helvetica-Bold", fontSize=8.6, leading=10,
                                        textColor=AMBER, charSpace=1.6),
        "cover_title":   ParagraphStyle("ct", fontName="Helvetica-Bold", fontSize=27, leading=30,
                                        textColor=WHITE),
        "cover_sub":     ParagraphStyle("cs", fontName="Helvetica", fontSize=9.6, leading=13,
                                        textColor=SUB),
        "logo":          ParagraphStyle("lg", fontName="Helvetica-Bold", fontSize=11.4, leading=12.5,
                                        textColor=WHITE),
        "logo_sub":      ParagraphStyle("ls", fontName="Helvetica", fontSize=8.4, leading=10,
                                        textColor=colors.HexColor("#93A6BA")),
        "cardnum":       ParagraphStyle("cn", fontName="Helvetica-Bold", fontSize=19, leading=21,
                                        textColor=NAVY),
        "cardlab":       ParagraphStyle("cl", fontName="Helvetica-Bold", fontSize=6.2, leading=8,
                                        textColor=MUTED, charSpace=0.8),
        "pf_h":          ParagraphStyle("ph", fontName="Helvetica-Bold", fontSize=6.4, leading=8,
                                        textColor=MUTED_2, charSpace=1.2),
        "pf_t":          ParagraphStyle("pt", fontName="Helvetica-Bold", fontSize=10.5, leading=13,
                                        textColor=NAVY),
        "pf_b":          ParagraphStyle("pb", fontName="Helvetica", fontSize=8.0, leading=11,
                                        textColor=MUTED),
        "ct_h":          ParagraphStyle("ch", fontName="Helvetica-Bold", fontSize=6.4, leading=8,
                                        textColor=TEAL_LT, charSpace=1.2),
        "ct_b":          ParagraphStyle("cb", fontName="Helvetica", fontSize=8.6, leading=11.5,
                                        textColor=colors.HexColor("#E6EDF4")),
        "eyebrow":       ParagraphStyle("ey", fontName="Helvetica-Bold", fontSize=7.8, leading=9.5,
                                        textColor=TEAL, charSpace=1.4),
        "h1":            ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=17, leading=19.5,
                                        textColor=NAVY),
        "toc_num":       ParagraphStyle("tn", fontName="Helvetica-Bold", fontSize=11, leading=13,
                                        textColor=TEAL),
        "toc_t":         ParagraphStyle("tt", fontName="Helvetica-Bold", fontSize=9.6, leading=12,
                                        textColor=NAVY),
        "toc_d":         ParagraphStyle("td", fontName="Helvetica", fontSize=8.2, leading=10.5,
                                        textColor=MUTED),
        "body":          ParagraphStyle("bd", fontName="Helvetica", fontSize=8.6, leading=11.4,
                                        textColor=colors.HexColor("#334155")),
        "kv":            ParagraphStyle("kv", fontName="Helvetica-Bold", fontSize=8.6, leading=11.4,
                                        textColor=NAVY),
        "finding_t":     ParagraphStyle("ft", fontName="Helvetica-Bold", fontSize=10.3, leading=12.4,
                                        textColor=NAVY),
        "evidence":      ParagraphStyle("ev", fontName="Courier", fontSize=7.2, leading=9.5,
                                        textColor=colors.HexColor("#475569")),
        "interp":        ParagraphStyle("ip", fontName="Helvetica-Oblique", fontSize=8.3, leading=10.7,
                                        textColor=colors.HexColor("#334155")),
        "score_t":       ParagraphStyle("st", fontName="Helvetica-Bold", fontSize=9.4, leading=11.5,
                                        textColor=NAVY),
        "score_d":       ParagraphStyle("sd", fontName="Helvetica", fontSize=7.8, leading=10,
                                        textColor=MUTED),
        "overall":       ParagraphStyle("ov", fontName="Helvetica-Bold", fontSize=16, leading=18,
                                        textColor=WHITE),
        "overall_sub":   ParagraphStyle("os", fontName="Helvetica", fontSize=7.4, leading=9.5,
                                        textColor=SUB),
        "qual_b":        ParagraphStyle("qb", fontName="Helvetica", fontSize=8.4, leading=11.4,
                                        textColor=colors.HexColor("#7C2D12")),
        "step_ey":       ParagraphStyle("se", fontName="Helvetica-Bold", fontSize=6.6, leading=8.4,
                                        textColor=TEAL, charSpace=1.1),
        "step_t":        ParagraphStyle("stt", fontName="Helvetica-Bold", fontSize=9.6, leading=12,
                                        textColor=NAVY),
        "step_d":        ParagraphStyle("std", fontName="Helvetica", fontSize=8.3, leading=11,
                                        textColor=colors.HexColor("#334155")),
        "cta_t":         ParagraphStyle("ctt", fontName="Helvetica-Bold", fontSize=15, leading=17.5,
                                        textColor=WHITE),
        "cta_b":         ParagraphStyle("ctb", fontName="Helvetica", fontSize=8.6, leading=11.5,
                                        textColor=SUB),
        "foot":          ParagraphStyle("fo", fontName="Helvetica", fontSize=7.0, leading=9,
                                        textColor=MUTED_2),
    }

# --------------------------------------------------------------- brand asset
# Drop the real logo at  niches/food-bengaluru/assets/smart-pursuit-logo.png
# (jpg/jpeg also work). If it is not there, the drawn SP mark is used instead,
# so the reports always build. A wide file (aspect >= 2.0) is treated as a full
# lockup: it is placed on its own, without repeating the "SMART PURSUIT" text.
ASSETS = Path(__file__).resolve().parent.parent / "assets"


def logo_asset():
    for name in ("smart-pursuit-logo.png", "smart-pursuit-logo.jpg", "smart-pursuit-logo.jpeg",
                 "smart-pursuit-logo.PNG", "smart-pursuit-logo.JPG", "smart-pursuit-logo.JPEG"):
        p = ASSETS / name
        if p.exists():
            return p
    return None


def logo_is_lockup(path):
    """True when the file already contains the SMART PURSUIT wordmark, so the report
    must not set the name again beside it.

    Priority: the sidecar file  assets/<logo-name>.mode.txt  (contents: lockup|mark)
    if it exists, otherwise a wide file (aspect >= 2.0) is assumed to be a lockup.
    """
    side = Path(str(path).rsplit(".", 1)[0] + ".mode.txt")
    if side.exists():
        return side.read_text(encoding="utf-8", errors="ignore").strip().lower().startswith("lockup")
    from reportlab.lib.utils import ImageReader
    iw, ih = ImageReader(str(path)).getSize()
    return (iw / float(ih)) >= 2.0


def _logo_box(path, max_h, max_w):
    """Fit the file into max_w x max_h, preserving its aspect ratio."""
    from reportlab.lib.utils import ImageReader
    iw, ih = ImageReader(str(path)).getSize()
    h = max_h
    w = h * iw / float(ih)
    if w > max_w:
        w = max_w
        h = w * ih / float(iw)
    return w, h, logo_is_lockup(path)


def _sp_logo(size=9.5):
    """Smart Pursuit mark — the supplied logo if present, else the drawn SP mark."""
    path = logo_asset()
    if path:
        w, h, wide = _logo_box(path, 16*mm, 46*mm)
        img = Image(str(path), width=w, height=h, mask="auto")
        img.hAlign = "LEFT"          # line the mark up with the cover text below it
        return img
    t = Table([[Paragraph(f"<font color='#FFFFFF'><b>SP</b></font>",
                          ParagraphStyle("sp", fontName="Helvetica-Bold", fontSize=size, leading=size+2,
                                         textColor=WHITE, alignment=TA_CENTER))]],
              colWidths=[12*mm], rowHeights=[12*mm])
    t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#12324A")),
                           ("BOX", (0,0), (-1,-1), 0.7, TEAL),
                           ("VALIGN", (0,0), (-1,-1), "MIDDLE")]))
    return t

def _rule(w=186*mm, c=None, h=0.6):
    c = c or BORDER
    t = Table([[""]], colWidths=[w], rowHeights=[h])
    t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), c),
                           ("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 0)]))
    return t

def build_evidence_pdf(lead: dict, out_pdf: Path) -> Path:
    """Build the report; the footer total is corrected by a second pass if needed."""
    TOTAL[0] = 7
    doc = _render(lead, out_pdf)
    if doc.page != TOTAL[0]:
        TOTAL[0] = doc.page
        doc = _render(lead, out_pdf)
    return out_pdf


def _render(lead: dict, out_pdf: Path):
    S = _s()
    L = lead
    story = []

    # ================================================== PAGE 1 — cover
    story.append(Spacer(1, 6*mm))
    _lp = logo_asset()
    if _lp and _logo_box(_lp, 16*mm, 46*mm)[2]:
        hdr = Table([[_sp_logo()]], colWidths=[70*mm])
    else:
        hdr = Table([[_sp_logo(), Paragraph("SMART PURSUIT", S["logo"])]],
                    colWidths=[16*mm, 60*mm])
    hdr.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                             ("LEFTPADDING", (0,0), (-1,-1), 0)]))
    hdr.hAlign = "LEFT"          # platypus tables centre by default; the cover must line up left
    story.append(hdr)
    story.append(Spacer(1, 1.5*mm))
    story.append(Paragraph("Performance Marketing &amp; Growth Audits", S["logo_sub"]))
    story.append(Spacer(1, 24*mm))
    story.append(Paragraph(L.get("cover_eyebrow", "PAID MEDIA &amp; MEASUREMENT AUDIT"), S["cover_eyebrow"]))
    story.append(Spacer(1, 3.5*mm))
    story.append(Paragraph(L["brand"], S["cover_title"]))
    story.append(Spacer(1, 3.5*mm))
    story.append(Paragraph(L["cover_sub"], S["cover_sub"]))
    story.append(Spacer(1, 6*mm))

    cards = []
    for num, lab in L["metrics"]:
        inner = Table([[Paragraph(str(num), S["cardnum"])], [Paragraph(lab.upper(), S["cardlab"])]],
                      colWidths=[42*mm])
        inner.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), WHITE),
            ("LINEBEFORE", (0,0), (0,-1), 2.4, AMBER),
            ("TOPPADDING", (0,0), (-1,0), 4), ("BOTTOMPADDING", (0,0), (-1,0), 0),
            ("TOPPADDING", (0,1), (-1,1), 1), ("BOTTOMPADDING", (0,1), (-1,1), 5),
            ("LEFTPADDING", (0,0), (-1,-1), 6),
        ]))
        cards.append(inner)
    row = Table([cards], colWidths=[45.5*mm]*4)
    row.setStyle(TableStyle([("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 0)]))
    story.append(row)

    # bottom band: prepared-for + contact
    story.append(Spacer(1, 46*mm))
    pf = [[Paragraph("PREPARED FOR", S["pf_h"])],
          [Paragraph(L["prepared_for_name"], S["pf_t"])],
          [Paragraph(L["prepared_for_line"], S["pf_b"])],
          [Paragraph(L.get("prepared_for_link", ""), S["pf_b"])]]
    pf_t = Table(pf, colWidths=[90*mm])
    pf_t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#EDF2F7")),
                              ("LEFTPADDING", (0,0), (-1,-1), 7), ("RIGHTPADDING", (0,0), (-1,-1), 7),
                              ("TOPPADDING", (0,0), (-1,0), 6), ("BOTTOMPADDING", (0,-1), (-1,-1), 7),
                              ("TOPPADDING", (0,1), (-1,-1), 1), ("BOTTOMPADDING", (0,0), (-1,-2), 1)]))
    ct = [[Paragraph("CONTACT", S["ct_h"])],
          [Paragraph(f"{EMAIL}&nbsp; · &nbsp;{PHONE}", S["ct_b"])],
          [Paragraph(f"Report generated {L['generated_on']}", S["logo_sub"])]]
    ct_t = Table(ct, colWidths=[90*mm])
    ct_t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#10293F")),
                              ("BOX", (0,0), (-1,-1), 0.6, colors.HexColor("#1E3A52")),
                              ("LEFTPADDING", (0,0), (-1,-1), 7), ("RIGHTPADDING", (0,0), (-1,-1), 7),
                              ("TOPPADDING", (0,0), (-1,0), 6), ("BOTTOMPADDING", (0,-1), (-1,-1), 7),
                              ("TOPPADDING", (0,1), (-1,-1), 1), ("BOTTOMPADDING", (0,0), (-1,-2), 1)]))
    band = Table([[pf_t, ct_t]], colWidths=[93*mm, 93*mm])
    band.setStyle(TableStyle([("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 0)]))
    story.append(band)
    story.append(NextPageTemplate("body"))
    story.append(PageBreak())

    # ================================================== PAGE 2 — contents + method + ad account
    story.append(Paragraph("CONTENTS", S["eyebrow"]))
    story.append(Paragraph("What is in this report", S["h1"]))
    story.append(Spacer(1, 1.2*mm)); story.append(_rule(38*mm, AMBER, 1.1)); story.append(Spacer(1, 4*mm))
    toc = [("01", "How this audit was produced", "Sources, method and the limits of what was measured"),
           ("02", "The ad account", L.get("ad_account_sub", "Live paid inventory as scraped on the crawl date")),
           ("03", f"Findings", f"{len(L['findings'])} issues, each with the measurement behind it"),
           ("04", "Opportunity score", "Five weighted dimensions, scored from measured values only"),
           ("05", "Suggested next steps", "Ordered by effort against likely impact")]
    for n, t, d in toc:
        r = Table([[Paragraph(n, S["toc_num"]), Paragraph(t, S["toc_t"])],
                   ["", Paragraph(d, S["toc_d"])]], colWidths=[12*mm, 174*mm])
        r.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), BG_LT if n in ("01","03","05") else WHITE),
                               ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
                               ("TOPPADDING", (0,0), (-1,0), 4), ("BOTTOMPADDING", (0,-1), (-1,-1), 4),
                               ("TOPPADDING", (0,1), (-1,1), 0), ("BOTTOMPADDING", (0,0), (-1,0), 0)]))
        story.append(r); story.append(Spacer(1, 1.6*mm))

    story.append(Spacer(1, 5*mm))
    story.append(Paragraph("01 METHOD", S["eyebrow"]))
    story.append(Paragraph("How this audit was produced", S["h1"]))
    story.append(Spacer(1, 1.2*mm)); story.append(_rule(38*mm, AMBER, 1.1)); story.append(Spacer(1, 3.5*mm))
    for b in L["method"]:
        story.append(Paragraph("• " + b, S["body"]))
        story.append(Spacer(1, 1.6*mm))

    story.append(CondPageBreak(34*mm))
    story.append(Spacer(1, 6*mm))

    # ================================================== ad account + coverage
    story.append(Paragraph("02 LIVE PAID INVENTORY DATA", S["eyebrow"]))
    story.append(Paragraph("The ad account", S["h1"]))
    story.append(Spacer(1, 1.2*mm)); story.append(_rule(38*mm, AMBER, 1.1)); story.append(Spacer(1, 3*mm))
    for k, v in L["ad_account"]:
        r = Table([[Paragraph(k, S["body"]), Paragraph(v, S["kv"])]], colWidths=[56*mm, 130*mm])
        r.setStyle(TableStyle([("LINEBELOW", (0,0), (-1,-1), 0.5, BORDER),
                               ("LEFTPADDING", (0,0), (-1,-1), 0),
                               ("TOPPADDING", (0,0), (-1,-1), 3.5), ("BOTTOMPADDING", (0,0), (-1,-1), 3.5),
                               ("VALIGN", (0,0), (-1,-1), "TOP")]))
        story.append(r)

    story.append(CondPageBreak(52*mm))
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph("COVERAGE", S["eyebrow"]))
    story.append(Paragraph("What was measured, and what was not", S["h1"]))
    story.append(Spacer(1, 1.2*mm)); story.append(_rule(38*mm, AMBER, 1.1)); story.append(Spacer(1, 3*mm))
    hdr = Table([[Paragraph("<b>SURFACE</b>", S["cardlab"]), Paragraph("<b>STATUS</b>", S["cardlab"]),
                  Paragraph("<b>METHOD</b>", S["cardlab"])]], colWidths=[52*mm, 52*mm, 82*mm])
    hdr.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), BG_LT),
                             ("LEFTPADDING", (0,0), (-1,-1), 5), ("RIGHTPADDING", (0,0), (-1,-1), 5),
                             ("TOPPADDING", (0,0), (-1,-1), 3), ("BOTTOMPADDING", (0,0), (-1,-1), 3)]))
    story.append(hdr)
    cov_col = {"MEASURED": TEAL, "NOT MEASURED": MUTED, "UNAVAILABLE": colors.HexColor("#B45309")}
    for surf, status, meth in L["coverage"]:
        col = cov_col.get(status.split(" — ")[0], MUTED)
        r = Table([[Paragraph(surf, S["body"]),
                    Paragraph(f"<b><font color='#{col.hexval()[2:]}'>{status}</font></b>", S["body"]),
                    Paragraph(meth, S["score_d"])]], colWidths=[52*mm, 52*mm, 82*mm])
        r.setStyle(TableStyle([("LINEBELOW", (0,0), (-1,-1), 0.5, BORDER),
                               ("LEFTPADDING", (0,0), (-1,-1), 5), ("RIGHTPADDING", (0,0), (-1,-1), 5),
                               ("TOPPADDING", (0,0), (-1,-1), 3.4), ("BOTTOMPADDING", (0,0), (-1,-1), 3.4),
                               ("VALIGN", (0,0), (-1,-1), "TOP")]))
        story.append(r)
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("Surfaces marked NOT MEASURED are outside the scope of a public crawl. They are listed so the reader can see exactly where this report's knowledge stops — no value has been estimated to fill them.", S["interp"]))
    story.append(CondPageBreak(60*mm))
    story.append(Spacer(1, 7*mm))

    # ================================================== findings (flows on from above)
    sev_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3, "NOTE": 4}
    findings = sorted(L["findings"], key=lambda f: sev_order.get(f["sev"], 9))
    story.append(Paragraph(f"03 {len(findings)} ISSUES, RANKED BY SEVERITY", S["eyebrow"]))
    story.append(Paragraph("Findings", S["h1"]))
    story.append(Spacer(1, 1.2*mm)); story.append(_rule(38*mm, AMBER, 1.1)); story.append(Spacer(1, 4*mm))

    for i, f in enumerate(findings, 1):
        chip_bg, chip_tx, bar = SEV.get(f["sev"], SEV["NOTE"])
        chip = Table([[Paragraph(f"<font color='#{chip_tx.hexval()[2:]}'>{f['sev']}</font>",
                                 ParagraphStyle("chip", fontName="Helvetica-Bold", fontSize=6.2,
                                                leading=8, textColor=chip_tx, charSpace=0.9))]],
                     colWidths=[20*mm])
        chip.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), chip_bg),
                                  ("LEFTPADDING", (0,0), (-1,-1), 4), ("RIGHTPADDING", (0,0), (-1,-1), 4),
                                  ("TOPPADDING", (0,0), (-1,-1), 2), ("BOTTOMPADDING", (0,0), (-1,-1), 2)]))
        head = Table([[chip, Paragraph(f"{i}. {f['title']}", S["finding_t"])]], colWidths=[22*mm, 151*mm])
        head.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                                  ("LEFTPADDING", (0,0), (-1,-1), 0)]))
        ev = Table([[Paragraph(f["evidence"].replace("\n", "<br/>"), S["evidence"])]], colWidths=[173*mm])
        ev.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), BG_LT),
                                ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
                                ("TOPPADDING", (0,0), (-1,-1), 3.4), ("BOTTOMPADDING", (0,0), (-1,-1), 3.4)]))
        inner = [[head], [Spacer(1, 1.2*mm)], [ev]]
        head_block = Table(inner, colWidths=[173*mm])
        head_block.setStyle(TableStyle([("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 0),
                                        ("LINEBEFORE", (0,0), (0,-1), 2.6, bar),
                                        ("LEFTPADDING", (0,0), (0,-1), 6)]))
        read_block = Table([[Paragraph(f["reading"], S["interp"])]], colWidths=[173*mm])
        read_block.setStyle(TableStyle([("LEFTPADDING", (0,0), (0,-1), 6),
                                        ("LINEBEFORE", (0,0), (0,-1), 2.6, bar),
                                        ("TOPPADDING", (0,0), (-1,-1), 0)]))
        story.append(KeepTogether([head_block, Spacer(1, 1.2*mm), read_block, Spacer(1, 1.7*mm)]))

    # ================================================== register (flows)
    story.append(CondPageBreak(58*mm))
    story.append(Spacer(1, 7*mm))
    story.append(Paragraph("03 FINDINGS · EVIDENCE REGISTER", S["eyebrow"]))
    story.append(Paragraph("Where every number in this report came from", S["h1"]))
    story.append(Spacer(1, 1.2*mm)); story.append(_rule(38*mm, AMBER, 1.1)); story.append(Spacer(1, 4*mm))
    rhdr = Table([[Paragraph("<b>MEASUREMENT</b>", S["cardlab"]), Paragraph("<b>SOURCE</b>", S["cardlab"]),
                   Paragraph("<b>VALUE OBSERVED</b>", S["cardlab"]), Paragraph("<b>DATE</b>", S["cardlab"])]],
                 colWidths=[38*mm, 48*mm, 84*mm, 16*mm])
    rhdr.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), BG_LT),
                              ("LEFTPADDING", (0,0), (-1,-1), 4), ("RIGHTPADDING", (0,0), (-1,-1), 4),
                              ("TOPPADDING", (0,0), (-1,-1), 3), ("BOTTOMPADDING", (0,0), (-1,-1), 3)]))
    story.append(rhdr)
    for item, src, val, dt in L["register"]:
        r = Table([[Paragraph(item, S["body"]), Paragraph(src, S["score_d"]),
                    Paragraph(val, S["kv"]), Paragraph(dt, S["score_d"])]],
                  colWidths=[38*mm, 48*mm, 84*mm, 16*mm])
        r.setStyle(TableStyle([("LINEBELOW", (0,0), (-1,-1), 0.5, BORDER),
                               ("LEFTPADDING", (0,0), (-1,-1), 4), ("RIGHTPADDING", (0,0), (-1,-1), 4),
                               ("TOPPADDING", (0,0), (-1,-1), 2.9), ("BOTTOMPADDING", (0,0), (-1,-1), 2.9),
                               ("VALIGN", (0,0), (-1,-1), "TOP")]))
        story.append(r)
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("Every row above is a readable public surface. Where a row reads unavailable or not measured, that is exactly what was found — the report does not substitute an estimate.", S["interp"]))

    # ================================================== score + qualification (flows)
    story.append(CondPageBreak(64*mm))
    story.append(Spacer(1, 7*mm))
    story.append(Paragraph("04 SCORED FROM MEASURED VALUES ONLY", S["eyebrow"]))
    story.append(Paragraph("Opportunity score", S["h1"]))
    story.append(Spacer(1, 1.2*mm)); story.append(_rule(38*mm, AMBER, 1.1)); story.append(Spacer(1, 4*mm))
    for label, sub, val in L["score_dims"]:
        dots = Table([["", "", "", ""]], colWidths=[7*mm]*4, rowHeights=[3.6*mm])
        st = [("BACKGROUND", (i,0), (i,0), TEAL if i < val else BORDER) for i in range(4)]
        st += [("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 1.6),
               ("TOPPADDING", (0,0), (-1,-1), 0), ("BOTTOMPADDING", (0,0), (-1,-1), 0)]
        dots.setStyle(TableStyle(st))
        r = Table([[Paragraph(label, S["score_t"]), dots,
                    Paragraph(f"<b>{val} / 4</b>", S["score_t"])],
                   [Paragraph(sub, S["score_d"]), "", ""]],
                  colWidths=[62*mm, 34*mm, 20*mm])
        r.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                               ("LEFTPADDING", (0,0), (-1,-1), 0),
                               ("TOPPADDING", (0,0), (-1,0), 2), ("BOTTOMPADDING", (0,1), (-1,1), 4)]))
        story.append(r)
    story.append(Spacer(1, 5*mm))
    total = sum(v for _, _, v in L["score_dims"])
    box = Table([[
        Table([[Paragraph(f"OVERALL", S["ct_h"])],
               [Paragraph(f"{total} / 20", S["overall"])],
               [Paragraph(f"{len(L['score_dims'])} of 5 dimensions scored", S["overall_sub"])]],
              colWidths=[55*mm],
              style=TableStyle([("LEFTPADDING", (0,0), (-1,-1), 8), ("TOPPADDING", (0,0), (-1,-1), 2),
                                ("BOTTOMPADDING", (0,0), (-1,-1), 2)])),
        Table([[Paragraph(f"<font color='#FFFFFF'><b>{L['grade']}</b></font> — {L['grade_note']}", S["ct_b"])]],
              colWidths=[125*mm],
              style=TableStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                                ("LEFTPADDING", (0,0), (-1,-1), 6)]))]],
        colWidths=[60*mm, 126*mm])
    box.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), NAVY),
                             ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8),
                             ("VALIGN", (0,0), (-1,-1), "MIDDLE")]))
    story.append(box)

    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("QUALIFICATION", S["eyebrow"]))
    story.append(Paragraph("Read this before acting on it", S["h1"]))
    story.append(Spacer(1, 1.2*mm)); story.append(_rule(38*mm, AMBER, 1.1)); story.append(Spacer(1, 3.5*mm))
    qbox = Table([[Paragraph(L["qualification"], S["qual_b"])]], colWidths=[186*mm])
    qbox.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#FFFBEB")),
                              ("LINEBEFORE", (0,0), (0,-1), 2.6, AMBER),
                              ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
                              ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7)]))
    story.append(qbox)
    story.append(CondPageBreak(48*mm))
    story.append(Spacer(1, 6*mm))

    # ================================================== next steps + CTA (flows)
    story.append(Paragraph("05 ORDERED BY EFFORT AGAINST IMPACT", S["eyebrow"]))
    story.append(Paragraph("Suggested next steps", S["h1"]))
    story.append(Spacer(1, 1.2*mm)); story.append(_rule(38*mm, AMBER, 1.1)); story.append(Spacer(1, 4*mm))
    for i, (ey, t, d) in enumerate(L["next_steps"], 1):
        num = Table([[Paragraph(f"<font color='#FFFFFF'><b>{i}</b></font>",
                                ParagraphStyle("n", fontName="Helvetica-Bold", fontSize=10,
                                               leading=12, textColor=WHITE, alignment=TA_CENTER))]],
                    colWidths=[9*mm], rowHeights=[9*mm])
        num.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), TEAL),
                                 ("VALIGN", (0,0), (-1,-1), "MIDDLE")]))
        txt = Table([[Paragraph(ey, S["step_ey"])], [Paragraph(t, S["step_t"])],
                     [Spacer(1, 0.6*mm)], [Paragraph(d, S["step_d"])]], colWidths=[170*mm])
        txt.setStyle(TableStyle([("LEFTPADDING", (0,0), (-1,-1), 0),
                                 ("TOPPADDING", (0,0), (-1,0), 0), ("BOTTOMPADDING", (0,0), (-1,-1), 0)]))
        r = Table([[num, txt]], colWidths=[12*mm, 174*mm])
        r.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "TOP"), ("LEFTPADDING", (0,0), (-1,-1), 0)]))
        story.append(r); story.append(Spacer(1, 2.2*mm))

    story.append(Spacer(1, 1.5*mm))
    cta = Table([[
        Table([[Paragraph("NEXT STEP", S["ct_h"])],
               [Paragraph("Happy to walk through any of this on a short call.", S["cta_t"])],
               [Paragraph("Nothing here requires new tooling. The first items are configuration, not rebuilds.", S["cta_b"])],
               [Spacer(1, 2*mm)],
               [Paragraph("GET IN TOUCH", S["ct_h"])],
               [Paragraph(f"Smart Pursuit &nbsp; · &nbsp; {EMAIL}", S["ct_b"])]],
              colWidths=[148*mm],
              style=TableStyle([("LEFTPADDING", (0,0), (-1,-1), 0), ("TOPPADDING", (0,0), (-1,-1), 1),
                                ("BOTTOMPADDING", (0,0), (-1,-1), 1)])),
        Table([[Paragraph(f"<font color='#FFFFFF'><b>{PHONE}</b></font>",
                          ParagraphStyle("ph", fontName="Helvetica-Bold", fontSize=9, leading=11,
                                         textColor=WHITE, alignment=TA_CENTER))]],
              colWidths=[34*mm], rowHeights=[10*mm],
              style=TableStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE")])),
    ]], colWidths=[152*mm, 34*mm])
    cta.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), NAVY),
                             ("LEFTPADDING", (0,0), (0,-1), 8), ("RIGHTPADDING", (0,0), (0,-1), 6),
                             ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
                             ("VALIGN", (0,0), (-1,-1), "TOP")]))
    _cta_and_closing = [cta]

    # ---- closing panel: fills the final page with useful, non-invented content
    story.append(Spacer(1, 5*mm))
    closing = Table([[
        Table([[Paragraph("<b>ABOUT THIS REPORT</b>", S["cardlab"])],
               [Paragraph(
                   f"Prepared by Smart Pursuit for {L['brand']}. Every figure was read from a public "
                   f"surface on {L['generated_on']} — the Google Ads Transparency Center, the Meta Ad Library, "
                   f"and the brand's own website and published pages.", S["body"])],
               [Spacer(1, 1.5*mm)],
               [Paragraph("<b>HOW TO CHECK IT</b>", S["cardlab"])],
               [Paragraph(
                   "Each finding quotes the raw measurement above it. Ad counts can be re-checked by domain in the "
                   "Google Ads Transparency Center (region: India), and tag IDs by opening the site and searching "
                   "the page source. Spend, ROAS and CPA are private to the advertiser, so they are marked "
                   "unavailable rather than estimated.", S["body"])],
               ],
              colWidths=[148*mm],
              style=TableStyle([("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 0),
                                ("TOPPADDING", (0,0), (-1,-1), 1), ("BOTTOMPADDING", (0,0), (-1,-1), 1)])),
        Table([[Paragraph("<font color='#FFFFFF'><b>SP</b></font>",
                          ParagraphStyle("csp", fontName="Helvetica-Bold", fontSize=12, leading=13,
                                         textColor=WHITE, alignment=TA_CENTER))],
               [Paragraph("<font color='#93A6BA'>SMART<br/>PURSUIT</font>",
                          ParagraphStyle("cwm", fontName="Helvetica-Bold", fontSize=5.6, leading=7,
                                         textColor=MUTED_2, alignment=TA_CENTER))]],
              colWidths=[26*mm], rowHeights=[16*mm, 8*mm],
              style=TableStyle([("BACKGROUND", (0,0), (-1,0), NAVY),
                                ("BACKGROUND", (0,1), (-1,1), BG_LT),
                                ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                                ("LINEAFTER", (0,0), (-1,-1), 0, BG_LT)]))
    ]], colWidths=[156*mm, 30*mm])
    closing.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), BG_LT),
                                 ("LINEBEFORE", (0,0), (0,-1), 2.6, AMBER),
                                 ("LEFTPADDING", (0,0), (0,-1), 7), ("RIGHTPADDING", (0,0), (0,-1), 5),
                                 ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
                                 ("VALIGN", (0,0), (-1,-1), "TOP")]))
    _cta_and_closing.append(Spacer(1, 6*mm))
    _cta_and_closing.append(closing)
    story.append(KeepTogether(_cta_and_closing))

    # ================================================== doc
    def on_page(canv, doc):
        canv.saveState()
        canv.setFont("Helvetica", 7)
        canv.setFillColor(MUTED_2)
        canv.drawString(12*mm, 8*mm, f"Smart Pursuit  ·  {EMAIL}  ·  {PHONE}")
        canv.drawRightString(A4[0] - 12*mm, 8*mm, f"Page {doc.page} of {TOTAL[0]}")
        if doc.page > 1:
            box_x, box_y, box_w, box_h = 12*mm, A4[1] - 12.2*mm, 6.0*mm, 6.0*mm
            _lp = logo_asset()
            if _lp:
                w, h, wide = _logo_box(_lp, 6.0*mm, 46*mm)
                canv.drawImage(str(_lp), box_x, box_y + (box_h - h)/2.0,
                               width=w, height=h, mask="auto")
                if not wide:
                    canv.setFillColor(NAVY)
                    canv.setFont("Helvetica-Bold", 7.4)
                    canv.drawString(box_x + w + 2.2*mm, box_y + 1.9*mm, "SMART PURSUIT")
            else:
                # drawn fallback: navy rounded square with gold underline, then the wordmark
                canv.setFillColor(NAVY)
                canv.roundRect(box_x, box_y, box_w, box_h, 1.2*mm, stroke=0, fill=1)
                canv.setFillColor(AMBER)
                canv.rect(box_x + 1.1*mm, box_y + 0.9*mm, box_w - 2.2*mm, 0.5*mm, stroke=0, fill=1)
                canv.setFillColor(WHITE)
                canv.setFont("Helvetica-Bold", 6.6)
                canv.drawCentredString(box_x + box_w/2, box_y + 2.0*mm, "SP")
                canv.setFillColor(NAVY)
                canv.setFont("Helvetica-Bold", 7.4)
                canv.drawString(box_x + box_w + 2.2*mm, box_y + 1.9*mm, "SMART PURSUIT")
            canv.setFont("Helvetica-Bold", 6.6)
            canv.setFillColor(MUTED)
            canv.drawRightString(A4[0] - 12*mm, box_y + 1.9*mm, L["brand"].upper())
            canv.setStrokeColor(BORDER); canv.setLineWidth(0.5)
            canv.line(12*mm, A4[1] - 13.4*mm, A4[0] - 12*mm, A4[1] - 13.4*mm)
        canv.restoreState()

    doc = BaseDocTemplate(str(out_pdf), pagesize=A4,
                          leftMargin=12*mm, rightMargin=12*mm, topMargin=14*mm, bottomMargin=13*mm,
                          title=f"Paid Media & Measurement Audit - {L['brand']}",
                          author=AGENCY)
    def cover_frame(canv, doc):
        canv.saveState()
        canv.setFillColor(NAVY)
        canv.rect(0, 0, A4[0], A4[1], stroke=0, fill=1)
        canv.setFillColor(colors.HexColor("#10293F"))
        canv.circle(A4[0] - 34*mm, A4[1] - 22*mm, 30*mm, stroke=0, fill=1)
        canv.setFillColor(colors.HexColor("#0E2436"))
        canv.circle(A4[0] - 14*mm, A4[1] - 132*mm, 26*mm, stroke=0, fill=1)
        canv.setFillColor(colors.HexColor("#0D2136"))
        canv.circle(-6*mm, 26*mm, 34*mm, stroke=0, fill=1)
        canv.restoreState()
        on_page(canv, doc)
    frame1 = Frame(12*mm, 13*mm, 186*mm, A4[1] - 27*mm, id="c1",
                   leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    frameN = Frame(12*mm, 13*mm, 186*mm, A4[1] - 27*mm, id="cN",
                   leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="cover", frames=[frame1], onPage=cover_frame),
                          PageTemplate(id="body", frames=[frameN], onPage=on_page)])
    doc.build(story)
    return doc
