"""
Reusable Smart Pursuit branded performance-audit PDF generator.

Usage as a module:
    from audit_pdf import generate_audit_pdf
    generate_audit_pdf(lead_data, out_pdf_path)

Usage from CLI:
    python audit_pdf.py --brand "Brand Name" --website example.com --niche D2C \\
        --ads 120 --spend "Rs.5-10 Cr/mo" --score 7 --revenue "Rs.1000 Cr FY25" \\
        --out audits/brand-audit.pdf \\
        --findings-file findings.md --wins-file wins.md etc.

Generates a 2-page branded PDF per the Smart Pursuit template used for Physics Wallah.
Outreach templates are written separately to outreach/<brand-slug>-Outreach-Templates.md.
"""
from __future__ import annotations
import argparse, re, json
from pathlib import Path
from datetime import date

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether,
)

# ---- Brand palette ----
PURPLE_DARK   = HexColor("#1F0F4F")
PURPLE        = HexColor("#4C27E0")
PURPLE_LIGHT  = HexColor("#EDE8FF")
GREEN         = HexColor("#10B981")
GREEN_LIGHT   = HexColor("#E6FBF3")
RED           = HexColor("#EF4444")
ORANGE        = HexColor("#F59E0B")
ORANGE_LIGHT  = HexColor("#FEF6E1")
DARK          = HexColor("#0F172A")
GRAY          = HexColor("#64748B")
GRAY_LIGHT    = HexColor("#F1F5F9")
BORDER        = HexColor("#E2E8F0")
WHITE         = HexColor("#FFFFFF")
# Map the canonical 'white' used throughout to WHITE
white = WHITE

ROOT = Path(__file__).resolve().parent.parent
AUDITS_DIR = ROOT / "audits"
OUTREACH_DIR = ROOT / "outreach"
AUDITS_DIR.mkdir(parents=True, exist_ok=True)
OUTREACH_DIR.mkdir(parents=True, exist_ok=True)


def _styles():
    ss = getSampleStyleSheet()
    def mk(name, **kw):
        return ParagraphStyle(name, parent=ss["Normal"], **kw)
    return {
        "H1":      mk("H1", fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=white),
        "SUB":     mk("SUB", fontName="Helvetica", fontSize=9, leading=12, textColor=HexColor("#CFC2FF")),
        "H2":      mk("H2", fontName="Helvetica-Bold", fontSize=12, leading=15, textColor=PURPLE_DARK, spaceAfter=1, spaceBefore=3),
        "H3":      mk("H3", fontName="Helvetica-Bold", fontSize=10, leading=13, textColor=DARK, spaceAfter=0, spaceBefore=1),
        "BODY":    mk("BODY", fontName="Helvetica", fontSize=8, leading=10.5, textColor=DARK, alignment=TA_JUSTIFY),
        "SB":      mk("SB", fontName="Helvetica-Bold", fontSize=26, leading=28, textColor=white, alignment=TA_CENTER),
        "SL":      mk("SL", fontName="Helvetica", fontSize=8, leading=10, textColor=HexColor("#CFC2FF"), alignment=TA_CENTER),
        "WT":      mk("WT", fontName="Helvetica-Bold", fontSize=9.5, leading=11, textColor=GREEN, spaceAfter=2),
        "WB":      mk("WB", fontName="Helvetica", fontSize=7.5, leading=10, textColor=DARK),
        "CTA_BIG": mk("CB", fontName="Helvetica-Bold", fontSize=13, leading=17, textColor=white, alignment=TA_CENTER),
        "CTA_SM":  mk("CS", fontName="Helvetica", fontSize=9, leading=13, textColor=white, alignment=TA_CENTER),
        "QSV":     mk("QSV", fontName="Helvetica-Bold", fontSize=13, leading=16, textColor=PURPLE_DARK, alignment=TA_CENTER),
        "QSL":     mk("QSL", fontName="Helvetica", fontSize=7, leading=9, textColor=GRAY, alignment=TA_CENTER),
        "ESUBJ":   mk("ES", fontName="Helvetica-Bold", fontSize=8.5, leading=11, textColor=PURPLE),
        "EBOD":    mk("EB", fontName="Helvetica", fontSize=8, leading=11, textColor=DARK),
    }


def _box(content, bg, border=None, pad=7):
    t = Table([[content]], colWidths=[180*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), bg),
        ("BOX",(0,0),(-1,-1), 0.5, border or bg),
        ("LEFTPADDING",(0,0),(-1,-1),pad),("RIGHTPADDING",(0,0),(-1,-1),pad),
        ("TOPPADDING",(0,0),(-1,-1),pad),("BOTTOMPADDING",(0,0),(-1,-1),pad),
    ]))
    return t


def _kv(rows, styles, c1=42*mm, c2=138*mm):
    BODY = styles["BODY"]
    data = [[Paragraph(f"<b>{k}</b>", BODY), Paragraph(v, BODY)] for k,v in rows]
    t = Table(data, colWidths=[c1, c2])
    t.setStyle(TableStyle([
        ("BOX",(0,0),(-1,-1),0.5,BORDER),("INNERGRID",(0,0),(-1,-1),0.25,BORDER),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),
        ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
    ]))
    return t


def _bar(label, score, color, styles):
    BODY = styles["BODY"]
    bar_tbl = Table([[""]], colWidths=[(score/10.0)*120*mm], rowHeights=[3.5*mm])
    bar_tbl.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1), color)]))
    row = Table([[Paragraph(f"<b>{label}</b>", BODY), bar_tbl, Paragraph(f"{score}/10", BODY)]],
                colWidths=[38*mm, 122*mm, 20*mm])
    row.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),2),("BOTTOMPADDING",(0,0),(-1,-1),2),
    ]))
    return row


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def generate_audit_pdf(lead: dict, out_pdf: Path | None = None) -> tuple[Path, Path]:
    """
    Generate audit PDF + outreach MD for a lead.

    lead dict keys (all optional unless marked required):
      brand (required), website (required), niche, score (default 7),
      ads_active (int), spend, revenue, destination,
      ad_intro (str) - short exec summary,
      ad_intelligence - list of (label, value) tuples,
      scores - dict of label->(score 1-10, color RED/ORANGE/GREEN),
      findings - list of str (HTML-safe),
      competitors - list of (name, what_better, signal) tuples,
      wins - list of (title, body, color, bg_color) tuples,
      impact - list of (metric, current, after, impact) tuples,
      outreach - list of (subject, body) tuples,
      agency_name, agency_phone, agency_email (defaults to Smart Pursuit)
    """
    S = _styles()
    brand = lead["brand"]
    website = lead["website"]
    niche = lead.get("niche", "")
    score = int(lead.get("score", 7))
    slug = _slug(brand)
    agency_name = lead.get("agency_name", "Smart Pursuit")
    agency_phone = lead.get("agency_phone", "7095024220")
    agency_email = lead.get("agency_email", "smartpursuit3@gmail.com")

    if out_pdf is None:
        out_pdf = AUDITS_DIR / f"{slug}-audit-report.pdf"
    out_pdf = Path(out_pdf)
    out_md = OUTREACH_DIR / f"{slug}-outreach-templates.md"

    # ---- Footer callback ----
    def on_page(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 7)
        canvas.setFillColor(GRAY)
        canvas.drawCentredString(A4[0]/2, 8*mm,
            f"Prepared by {agency_name}  |  Ph: {agency_phone}  |  Email: {agency_email}  |  Confidential Audit for {brand}  |  Page %d" % doc.page)
        canvas.restoreState()

    doc = SimpleDocTemplate(str(out_pdf), pagesize=A4,
        leftMargin=12*mm, rightMargin=12*mm, topMargin=8*mm, bottomMargin=12*mm,
        title=f"{brand} - Performance Audit by {agency_name}")

    story = []

    # Header
    header_inner = [
        [Paragraph(f"FOR: <b>{brand.upper()}</b> &nbsp;|&nbsp; <font size=8>CONFIDENTIAL PERFORMANCE AUDIT</font>", S["SUB"])],
        [Spacer(1,1*mm)],
        [Paragraph("We Found 3 Leaks Costing You ~40% of Ad Spend", S["H1"])],
        [Spacer(1,1*mm)],
        [Paragraph(f"Prepared by {agency_name} - Performance Marketing for Scaling D2C &amp; Edtech Brands", S["SUB"])],
    ]
    ht = Table(header_inner, colWidths=[128*mm])
    ht.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), PURPLE_DARK),
        ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
        ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
    ]))
    badge = Table([
        [Paragraph("LEAD SCORE", S["SL"])],
        [Paragraph(str(score), S["SB"])],
        [Paragraph("/ 10 &nbsp;<font color='#FFD166'>HOT</font>" if score >= 6 else f"/ 10", S["SL"])],
    ], colWidths=[48*mm])
    badge.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), PURPLE),
        ("ALIGN",(0,0),(-1,-1),"CENTER"),
        ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
    ]))
    cover = Table([[ht, badge]], colWidths=[132*mm, 48*mm])
    cover.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP")]))
    story.append(cover)
    story.append(Spacer(1,1*mm))

    # Quick stats
    stats = [
        (f"{lead.get('ads_active','?')}+", "Active Meta ads"),
        (lead.get("spend","-"), "Est. monthly spend"),
        (niche or "-", "Niche"),
        (lead.get("revenue","-"), "Revenue"),
    ]
    cells = []
    for v,l in stats:
        c = Table([[Paragraph(str(v), S["QSV"])],[Paragraph(l, S["QSL"])]], colWidths=[44*mm])
        c.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),GRAY_LIGHT),("BOX",(0,0),(-1,-1),0.5,BORDER),
                               ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4)]))
        cells.append(c)
    sr = Table([cells], colWidths=[45*mm]*4)
    story.append(sr)
    story.append(Spacer(1,1*mm))

    # Exec summary
    exec_text = lead.get("ad_intro", f"{brand} ({website}) is running active Meta ads in India and shows clear performance-marketing leaks.")
    story.append(Paragraph("EXECUTIVE SUMMARY", S["H2"]))
    story.append(_box(Paragraph(exec_text, S["BODY"]), PURPLE_LIGHT, border=PURPLE))
    story.append(Spacer(1,1*mm))

    # Ad intelligence
    ad_intel = lead.get("ad_intelligence", [
        ("Active platforms", "Meta (Facebook + Instagram) primary; other platforms as observed."),
        ("Funnel type", lead.get("destination","Website traffic")),
    ])
    story.append(Paragraph("1. AD INTELLIGENCE", S["H2"]))
    story.append(_kv(ad_intel, S))
    story.append(Spacer(1,1*mm))

    # Scores
    default_scores = {
        "Creative Variety": (3,RED), "UGC & Social Proof": (2,RED),
        "Copy & Hook Strength": (5,ORANGE), "Landing Page CRO": (4,RED),
        "Tracking & CAPI": (4,RED), "Retargeting Depth": (3,RED),
    }
    scores = lead.get("scores", default_scores)
    story.append(Paragraph("2-5. CREATIVE / COPY / CRO / TRACKING SCORES", S["H2"]))
    score_rows = [[_bar(label, s, color, S)] for label,(s,color) in scores.items()]
    st_tbl = Table(score_rows, colWidths=[180*mm])
    st_tbl.setStyle(TableStyle([("BOX",(0,0),(-1,-1),0.5,BORDER),("INNERGRID",(0,0),(-1,-1),0.25,BORDER),
                               ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),
                               ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3)]))
    story.append(st_tbl)
    story.append(Spacer(1,1*mm))
    for f in lead.get("findings", []):
        story.append(Paragraph("- " + f, S["BODY"]))
    story.append(Spacer(1,1*mm))

    # Competitors
    story.append(Paragraph("6. COMPETITOR BENCHMARK", S["H2"]))
    comp = lead.get("competitors", [("Competitor","What they do better","Signal")])
    ct = Table([[Paragraph(f"<b>{c}</b>", S["BODY"]) for c in comp[0]]] +
               [[Paragraph(c, S["BODY"]) for c in row] for row in comp[1:]],
               colWidths=[42*mm, 78*mm, 60*mm])
    ct.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0), PURPLE_LIGHT),
        ("TEXTCOLOR",(0,0),(-1,0), PURPLE_DARK),
        ("BOX",(0,0),(-1,-1),0.5,BORDER),("INNERGRID",(0,0),(-1,-1),0.25,BORDER),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),
        ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
    ]))
    story.append(ct)
    story.append(Spacer(1,1*mm))

    # Quick wins
    story.append(Paragraph("7. 3 QUICK WINS (Implement in 7 Days)", S["H2"]))
    wins = lead.get("wins", [
        ("WIN 1 - Creative: Deploy 15 UGC Reels", "Shoot 15 fifteen-second UGC/customer testimonials; replace 30% of stale creatives.", GREEN, GREEN_LIGHT),
        ("WIN 2 - CRO: Build a dedicated landing page", "Route ad traffic to a campaign-specific page with sticky CTA, social proof, and clear offer.", ORANGE, ORANGE_LIGHT),
        ("WIN 3 - Tracking: Server-Side CAPI + Retargeting", "Fire events server-side; build 3 retargeting audiences; run dedicated creatives per audience.", PURPLE, PURPLE_LIGHT),
    ])
    for title, body, border, bg in wins:
        story.append(_box([Paragraph(title, S["WT"]), Paragraph(body, S["WB"])], bg, border=border))
        story.append(Spacer(1,1*mm))

    # Impact
    impact = lead.get("impact", [
        ("Metric", "Current (est.)", "After Wins", "Impact"),
        ("CTR (Meta)", "Baseline", "+25-50%", "+30-50%"),
        ("Landing Page CVR", "Baseline", "+30-50%", "+40-50%"),
        ("Cost Per Acquisition", "100", "65-75", "-25-35%"),
        ("Ad Spend Wastage", "~35-45%", "~15-20%", "Significant savings"),
    ])
    it = Table([[Paragraph(f"<b>{c}</b>", S["BODY"]) for c in impact[0]]] +
               [[Paragraph(c, S["BODY"]) for c in row] for row in impact[1:]],
               colWidths=[50*mm,40*mm,45*mm,45*mm])
    it.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),PURPLE_LIGHT),("TEXTCOLOR",(0,0),(-1,0),PURPLE_DARK),
        ("BOX",(0,0),(-1,-1),0.5,BORDER),("INNERGRID",(0,0),(-1,-1),0.25,BORDER),
        ("ALIGN",(1,1),(-1,-1),"CENTER"),("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),
        ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
        ("BACKGROUND",(3,1),(3,-1),GREEN_LIGHT),("TEXTCOLOR",(3,1),(3,-1),GREEN),
    ]))
    story.append(Spacer(1,1*mm))
    story.append(Paragraph("EXPECTED IMPACT", S["H3"]))
    story.append(it)
    story.append(Spacer(1,1*mm))

    # CTA
    cta = [
        [Paragraph("READY TO PLUG THESE LEAKS?", S["CTA_BIG"])],
        [Spacer(1,1*mm)],
        [Paragraph(f"{agency_name} will run a <b>14-day performance sprint</b> for {brand}: "
                   f"Creative refresh, CRO rebuild of top landing pages, CAPI + retargeting setup. "
                   f"We work on a <b>performance-fee model</b> tied to conversion-cost reduction.", S["CTA_SM"])],
        [Spacer(1,1*mm)],
        [Paragraph(f"Ph/WhatsApp: <b>{agency_phone}</b> &nbsp;|&nbsp; Email: <b>{agency_email}</b>", S["CTA_SM"])],
        [Spacer(1,1*mm)],
        [Paragraph(f"- {agency_name} Performance Team", S["CTA_SM"])],
    ]
    ctat = Table(cta, colWidths=[180*mm])
    ctat.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),PURPLE_DARK),
        ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
        ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
    ]))
    story.append(KeepTogether(ctat))

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)

    # Write outreach MD (separate file)
    emails = lead.get("outreach", [
        (f"Subject A (Roast-Audit): I audited {brand}'s ads - 3 leaks costing you money",
         f"Hi {brand} team,\n\nI spent 30 minutes on {website} and your Meta Ad Library. I spotted 3 leaks costing roughly 25-40% of ad spend. Can I send over a 2-page confidential audit? 15-minute call if any of it lands.\n\n- {agency_name} | Ph: {agency_phone}"),
        (f"Subject B (Loom - 30 sec):",
         f"\"Hey - I recorded a 3-minute screen recording of your funnel showing 3 specific leaks. Happy to send - where should I ping it (WhatsApp / email)?\""),
        (f"Subject C (FOMO): Your competitors are winning with UGC Reels",
         f"Hi,\n\nWhile auditing your category I noticed competitors are running UGC Reels + retargeting at far lower CPA. Your creative is still founder-talking-head heavy and retargeting looks one-size-fits-all. 3-win, 7-day playbook attached. 15 minutes to walk through?\n\n- {agency_name}"),
    ])
    md = [
        f"# {brand} - Outreach Templates ({agency_name} BD team)",
        "",
        f"> Companion to `audits/{slug}-audit-report.pdf` (Lead score {score}/10). Do NOT attach to the audit PDF - internal BD templates only.",
        "", "---", "",
    ]
    for subj, body in emails:
        md.append(f"### {subj}"); md.append(""); md.append(body); md.append(""); md.append("---"); md.append("")
    out_md.write_text("\n".join(md))

    return out_pdf, out_md


# ---- CLI ----
if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Generate Smart Pursuit branded audit PDF + outreach MD")
    ap.add_argument("--brand", required=True)
    ap.add_argument("--website", required=True)
    ap.add_argument("--niche", default="")
    ap.add_argument("--score", type=int, default=7)
    ap.add_argument("--out", default=None)
    ap.add_argument("--data", default=None, help="Path to JSON file with full lead data (overrides other flags)")
    args = ap.parse_args()

    if args.data:
        lead = json.loads(Path(args.data).read_text())
    else:
        lead = {"brand": args.brand, "website": args.website, "niche": args.niche, "score": args.score}

    pdf, md = generate_audit_pdf(lead, Path(args.out) if args.out else None)
    print(f"PDF:  {pdf}")
    print(f"MD:   {md}")
