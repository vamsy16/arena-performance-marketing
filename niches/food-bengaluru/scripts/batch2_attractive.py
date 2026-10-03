# -*- coding: utf-8 -*-
"""
ATTRACTIVE-style blocks for the ten batch-2 leads, derived from their own lead
records so the workbook's roadmap/competitor sheets stay in sync with the audits.

No projections: the `roi` block is intentionally omitted for every batch-2 lead —
the audits contain measured values only, and the workbook says so explicitly.
"""
import re

from batch2_leads import LEADS2


def _plain(html):
    t = re.sub(r"</?b>", "", html)
    t = t.replace("<br/>", " ").replace("&amp;", "&")
    return re.sub(r"\s+", " ", t).strip()


def _split_finding(html):
    t = _plain(html)
    if ":" in t[:120]:
        head, rest = t.split(":", 1)
        return head.strip(), rest.strip()
    return t[:70], t


ATTRACTIVE2 = {}
for _slug, _l in LEADS2.items():
    ATTRACTIVE2[_slug] = dict(
        roadmap_days=14,
        vs_who=", ".join(c[0] for c in _l["competitors"][:2]),
        you=[f"{v} {label}" for v, label in _l["stats"]] + [_l["headline"]],
        competitor=[f"{c[0]}: {c[1]}" for c in _l["competitors"]],
        leaks=[_split_finding(f) for f in _l["findings"]],
        roadmap=[(w[0].replace("WIN ", "DAY "), w[0], w[1]) for w in _l["wins"]],
    )
