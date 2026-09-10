---
name: pdf-report-generator
description: "When user wants to generate beautiful attractive PDF audit report to send to leads. Use when user says 'generate PDF', 'create audit PDF', 'beautiful report for client', 'PDF to send to lead', 'outreach PDF'. This skill converts performance-lead-audit or ig-whatsapp-audit into a branded, visual PDF with charts, scores, and quick wins, with Smart Pursuit branding. Uses open-design (385 templates) and reportlab. For audit itself, see performance-lead-audit. For outreach DM, see outreach-personalizer."
metadata:
  version: 1.2.0
---

# PDF Report Generator - Beautiful Audit PDFs for Outreach (Smart Pursuit Branded)

You generate beautiful, attractive PDF audit reports that agency can send to leads to get them to understand leaks and book a call.

**Agency Branding (ALWAYS include in NEW PDFs generated after audit):**
- Agency Name: Smart Pursuit
- Contact: 7095024220
- Email: smartpursuit3@gmail.com
- Do NOT update existing PDFs (sample-lead-audit-report.pdf, sample-conversion-pdf.pdf) - keep them as is. Only NEW lead PDFs after audit should have Smart Pursuit branding.

## When to Use
- User says "Generate PDF for this lead", "Create beautiful report", "PDF to send to client"
- After running performance-lead-audit or ig-whatsapp-audit

## Structure (1-2 pages, conversion-focused)

1. **Cover Header:**
   - FOR: [BRAND NAME] | CONFIDENTIAL AUDIT | Prepared by Smart Pursuit
   - Title: "We Found 3 Leaks Costing You ~40% of Ad Spend"
   - Lead Score Badge

2. **Executive Summary Box (Purple)**

3. **Ad Intelligence Table**

4. **Creative Audit - Mistakes**

5. **CRO Audit Table**

6. **3 Quick Wins with ROI (Green boxes)**

7. **Case Study**

8. **How We Work + Guarantee**

9. **CTA Box (Dark) with Smart Pursuit Contact:**
   ```
   📞 Call/WhatsApp: 7095024220
   📧 Email: smartpursuit3@gmail.com
   — Smart Pursuit Team
   ```

10. **Footer:** Prepared by Smart Pursuit • 📞 7095024220 • 📧 smartpursuit3@gmail.com

## Templates

- Existing PDFs (DO NOT UPDATE): sample-lead-audit-report.pdf, sample-conversion-pdf.pdf (keep old branding)
- NEW template for future leads: smart-pursuit-performance-TEMPLATE.pdf (has [BRAND NAME] placeholder + Smart Pursuit contact) - USE THIS as base for all NEW lead PDFs after audit

## How to Generate

Use reportlab. See generate_branded_pdfs.py for template code. Always include Smart Pursuit contact in CTA and footer for NEW PDFs.

## Workflow

1. Run performance-lead-audit for brand
2. Run pdf-report-generator → generates [brand]-audit-report.pdf with Smart Pursuit branding (using smart-pursuit-performance-TEMPLATE.pdf as base)
3. Run outreach-personalizer → DM says "I made quick audit PDF for you..."

## Related Skills

- `performance-lead-audit`, `ig-whatsapp-audit`, `outreach-personalizer`
