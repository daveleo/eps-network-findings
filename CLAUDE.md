# EPS network findings (public site) — Claude instructions

Workspace rules in `D:\Work\CLAUDE.md` apply. Keep `PROJECT.md` and `CHANGELOG.md` current.

## What this is

The public GitHub Pages site for the EPS network-dropout investigation, for Expromo IT and the original EPS developer. It is the published face of [[projects/EPS/PROJECT|EPS firmware]]: the report page is generated from `EPS/docs/report.md` via `EPS/tools/report_to_html.py`, so **the source of truth lives in the EPS repo, not here**. See `PROJECT.md`.

## How to run / build

- `python build.py` wraps the fragments in `src/` into standalone pages and rewrites internal links. GitHub Pages serves the repo root of `main`.
- To update the report page, regenerate it in the [[projects/EPS/PROJECT|EPS repo]] first, then rebuild here.

## Rules specific to this project

- This is a public site: pushing to `main` publishes within a minute or two. Ask before pushing, and keep it free of anything not meant to be public (customer names, access details).
- Don't hand-edit generated pages where a source exists; edit `src/` (or the EPS report) and re-run `build.py`.
- Keep the English and Danish pages (`*-da.html`, `hvorfor-v3-3.html`) cross-linked both ways when you add or rename one.
