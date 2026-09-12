"""Run audit_pdf.generate_audit_pdf for every lead JSON that doesn't have a PDF yet."""
import os, sys, json, traceback
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from audit_pdf import generate_audit_pdf, _slug, ROOT

LEADS = ROOT / "leads"
AUDITS = ROOT / "audits"
failed = []
succeeded = []
for jf in sorted(LEADS.glob("*.json")):
    lead = json.loads(jf.read_text())
    slug = _slug(lead["brand"])
    pdf = AUDITS / f"{slug}-audit-report.pdf"
    if pdf.exists() and pdf.stat().st_size > 5000:
        # Already has a non-tiny PDF; skip (covers #1-#6).
        continue
    try:
        out_pdf, out_md = generate_audit_pdf(lead)
        succeeded.append(lead["brand"])
    except Exception as e:
        failed.append((lead["brand"], str(e)))
        traceback.print_exc()

print(f"\nSucceeded: {len(succeeded)}")
for b in succeeded: print(f"  OK  {b}")
print(f"\nFailed: {len(failed)}")
for b,e in failed: print(f"  FAIL {b}: {e}")
