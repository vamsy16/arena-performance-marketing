#!/usr/bin/env python3
"""Build Food/Bangalore lead JSONs and generate branded audit PDFs + outreach templates."""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from leads_data_a import LEADS_A
from leads_data_b import LEADS_B
from leads_data_c import LEADS_C
from audit_pdf_food import generate_audit_pdf, _slug

LEADS = LEADS_A + LEADS_B + LEADS_C

def main():
    (ROOT / "leads").mkdir(exist_ok=True)
    ok = []
    for lead in LEADS:
        slug = _slug(lead["brand"])
        (ROOT / "leads" / f"{slug}.json").write_text(
            json.dumps(lead, ensure_ascii=False, indent=2), encoding="utf-8")
        pdf, md = generate_audit_pdf(lead)
        ok.append((lead["brand"], slug, pdf.name, md.name))
    print(f"\nGenerated {len(ok)} leads:\n")
    for brand, slug, pdf, md in ok:
        print(f"  {brand:22s} -> audits/{pdf}  +  outreach/{md}")

if __name__ == "__main__":
    main()
