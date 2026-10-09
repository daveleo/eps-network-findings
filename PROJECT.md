---
name: EPS network findings (public site)
status: active
priority:
version: 2026-10-09
deadline:
next: Share the link with IT and the original EPS developer; update the pages after the load test and pilot
updated: 2026-10-09
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
- `index.html`, `executive-summary.html`, `findings.html`, `report.html`: the built site
- `.nojekyll`: serve files as they are

## Current state

First version published 2026-10-09: executive summary, findings at a glance, full report (status 2026-10-09 evening).

## Milestones

- [x] 2026-10-09 — Site published with the three documents
