---
name: pdf-report-generator
description: "When user wants to generate beautiful attractive PDF audit report to send to leads. Use when user says 'generate PDF', 'create audit PDF', 'beautiful report for client', 'PDF to send to lead', 'outreach PDF'. This skill converts performance-lead-audit or ig-whatsapp-audit into a branded, visual PDF with charts, scores, and quick wins. Uses open-design (385 templates) and reportlab. For audit itself, see performance-lead-audit. For outreach DM, see outreach-personalizer."
metadata:
  version: 1.0.0
---

# PDF Report Generator - Beautiful Audit PDFs for Outreach

You generate beautiful, attractive PDF audit reports that agency can send to leads to get them to understand leaks and book a call.

## When to Use

- User says "Generate PDF for this lead", "Create beautiful report", "PDF to send to client"
- After running performance-lead-audit or ig-whatsapp-audit
- User wants to send audit as PDF, not just text DM

## What Makes PDF Attractive (Design Principles)

Use `open-design` skill (385 templates) for inspiration + reportlab for generation.

**Structure of PDF (1-2 pages, not 10):**

1. **Cover Header:**
   - Kicker: "PERFORMANCE AUDIT REPORT" (purple)
   - Brand Name: "Magicbricks.com - Real Estate Marketplace" (large)
   - Lead Score Badge: "10/10 🔥 HOT LEAD"
   - Date + Prepared by

2. **Executive Summary Box:**
   - Purple light background, rounded corners
   - 2-3 lines: Spend, traffic, biggest leak

3. **Ad Intelligence Table:**
   - Platform | Active | Spend Signal | Gap
   - Dark header, light rows

4. **Creative Audit - Mistakes:**
   - ❌ Icons + bold title + description
   - 3 mistakes max

5. **CRO Audit Table:**
   - Area | Finding
   - Yellow light background for urgency

6. **3 Quick Wins:**
   - Green boxes with WIN 1, WIN 2, WIN 3
   - Each: Title + Description + Expected lift

7. **How We Can Help:**
   - 2-3 lines pitch, not salesy
   - Calendly link

8. **Footer:**
   - Prepared by, skills used, contact

**Design:**
- Colors: Purple #7C3AED for kicker, dark #111827 for titles, gray #6B7280 for subtitles
- Fonts: Helvetica-Bold for headings, Helvetica for body
- Spacing: Plenty of white space, not cluttered
- Tables: Rounded, light backgrounds
- No more than 2 pages - leads won't read 10 pages

## How to Generate (Technical)

### Option 1: Python reportlab (Works now - we generated sample)

```python
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
# See generate_audit_pdf.py for full code
```

We already generated sample: `templates/sample-lead-audit-report.pdf` - beautiful 1-page audit for Magicbricks.

### Option 2: HTML + open-design + PDF export

Use `open-design` skill (385 templates):
- Pick landing page template
- Fill with audit data
- Export as HTML -> PDF via wkhtmltopdf or browser print

### Option 3: Canva via API (Future)

Use Canva API to fill template with brand data.

## Input Required

- Brand Name + Website
- Audit report (from performance-lead-audit or ig-whatsapp-audit)
- 3 Quick Wins
- Your agency name + Calendly link
- Lead Score

## Output

- PDF file: `[brand]-audit-report.pdf` (e.g., `magicbricks-audit-report.pdf`)
- Location: `templates/` or `reports/`
- Ready to send to lead via Email/WhatsApp

## Example Trigger

- "Generate beautiful PDF for Magicbricks audit"
- "Create PDF report for Zouk to send to client"
- "Make audit PDF for Instagram lead @xyz"

## Workflow

1. Run performance-lead-audit for brand (gets 9-point report)
2. Run pdf-report-generator to convert report to beautiful PDF
3. Run outreach-personalizer to write DM/email that says "I made a quick audit PDF for you..."

**Full outreach flow:**
```
Find lead (lead-prospecting) -> Audit (performance-lead-audit) -> PDF (pdf-report-generator) -> DM (outreach-personalizer) -> Send PDF via Email/WhatsApp
```

This gets 3x more replies than plain text DM.

## Sample PDF

We generated sample: `templates/sample-lead-audit-report.pdf` for Magicbricks.com

Check it - it's 1 page, purple header, tables, green win boxes, professional.

## Related Skills

- `performance-lead-audit`: Get audit data first
- `ig-whatsapp-audit`: For IG/WhatsApp leads
- `open-design`: 385 design templates for inspiration
- `outreach-personalizer`: Write DM to send PDF
