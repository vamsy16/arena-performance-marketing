#!/usr/bin/env python3
"""Regenerate all Food/Bengaluru audits in the house ATTRACTIVE format.
Old text-format PDFs are preserved under audits/_previous-text-format/."""
import json, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from audit_attractive import build_pdf
from leads_attractive_block import ATTRACTIVE
from audit_pdf_food import _slug

def main():
    leads_dir = ROOT / "leads"
    audits = ROOT / "audits"
    old = audits / "_previous-text-format"
    old.mkdir(exist_ok=True)
    ok, missing = [], []
    for f in sorted(leads_dir.glob("*.json")):
        lead = json.loads(f.read_text(encoding="utf-8"))
        slug = _slug(lead["brand"])
        block = ATTRACTIVE.get(slug)
        if not block:
            missing.append(slug); continue
        # move old version aside once
        target = audits / f"{slug}-audit-report.pdf"
        if target.exists() and not (old / target.name).exists():
            shutil.move(str(target), str(old / target.name))
        lead.update(block)
        build_pdf(lead, target)
        ok.append((lead["brand"], target.name))
    print(f"Attractive-format audits generated: {len(ok)}")
    for b, n in ok: print(f"  {b:22s} -> audits/{n}")
    if missing: print("MISSING BLOCKS:", missing)

if __name__ == "__main__":
    main()
