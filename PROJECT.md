---
name: EPS network findings (public site)
status: active
priority:
version: 2026-10-12
deadline:
next: Share comparison.html and the Danish brief with the product manager; update the pages (English and Danish) after the hands-on checks, real loads and pilot
updated: 2026-10-12
repo: daveleo/eps-network-findings
url: https://daveleo.github.io/eps-network-findings/
---

# EPS network findings (public site)

Public GitHub Pages site with the three documents of the EPS network-dropout investigation, for Expromo IT and the original EPS developer.

## What it is for

Sharing the findings outside the private EPS repo: an executive summary of firmware 3.0, a findings page with charts, and the full investigation report.

## How to run

`python build.py` builds the standalone pages from `src/`. GitHub Pages serves the repo root of `main`.

## How to use

Edit or replace a page in `src/` (the report comes from `EPS/docs/report.md` via `EPS/tools/report_to_html.py`), run `python build.py`, commit and push. The site updates within a minute or two.

## What is what

- `src/`: page sources (HTML fragments, as published internally)
- `build.py`: wraps the sources into standalone pages, rewrites internal links
- `index.html`, `why-v3-3.html`, `comparison.html`, `why-v3-2.html`, `executive-summary.html`, `findings.html`, `report.html`: the built site
- `hvorfor-v3-3.html`, `comparison-da.html`: the Danish pages (short brief for the product manager; the comparison in Danish)
- `.nojekyll`: serve files as they are

## Current state

Updated 2026-10-12 (later): **Danish pages** `hvorfor-v3-3.html` (short brief for the product manager: v2.2 → v3.3 and why v3.3) and `comparison-da.html` (the comparison in Danish, linked both ways with the English one); the comparison's recovery and standards tables now wrap instead of scrolling. Earlier 2026-10-12: **v3.3 recommended as official.** New pages `why-v3-3.html` (decision brief: code analysis, what v3.3 changes, overnight evidence, limits) and `comparison.html` (v2.2/v3.1/v3.2/v3.3 side by side: features, 17-fault matrix generated from the trial data, recovery scenarios, standards 26/46/46/48, regression). Executive summary, findings, report (regenerated from `EPS/docs/report.md`) and landing page bumped to v3.3; `why-v3-2.html` kept at its URL with a superseded note. Before: Updated 2026-10-11 (round 2): all three pages carry the single-register fault matrix for all three firmwares, the 200× reset start-up result, and the **tested** v3.2 candidate. v3.2 widens v3.1's 5 s health check to the mode, retry and PHY registers; on the same 14-fault matrix it recovered from all 14 faults — including the PHY power-down that matches the field symptom (11–12 s, no reset) — with no dead outcome and the outputs never moving, for +118 bytes of flash. The pages now recommend v3.2 as the field candidate in place of v3.1. A fourth document, `why-v3-2.html`, is a cross-linked decision brief making the unbiased case for adopting v3.2 as official; the landing page leads with it. Earlier: 2026-10-10 the standards suite (v3.1 46 of 56, v2.2 26); first published 2026-10-09.

## Milestones

- [x] 2026-10-09 — Site published with the three documents
- [x] 2026-10-10 — Pages updated for v3.1 (final) and the standards comparison
- [x] 2026-10-11 — Pages updated (round 1): fault matrix, reset start-up, v3.2 candidate (built)
- [x] 2026-10-11 — Pages updated (round 2): v3.2 fault-matrix results, v3.2 recommended as the field candidate
- [x] 2026-10-11 — New page "Why v3.2 should be official" (decision brief, cross-linked); site now four documents, landing leads with it
- [x] 2026-10-12 — v3.3: new pages "Why v3.3 should be official" and "All versions compared"; all pages bumped to v3.3; v3.2 brief kept
- [x] 2026-10-12 — Danish pages: short brief for the product manager and the comparison in Danish; comparison tables wrap
