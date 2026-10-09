# EPS network findings

Public documents on why Expromo EPS power sequencers (Keyestudio KS0304: ATmega328P + WIZnet W5500) drop off the network on firmware v2.2, and what firmware 3.0 changes.

**Read online:** https://daveleo.github.io/eps-network-findings/

| Document | For |
|---|---|
| [Executive summary](https://daveleo.github.io/eps-network-findings/executive-summary.html) | decision makers and IT: what changed in v3.0, comparison with v2.2, fit with enterprise network practice, limits, rollout |
| [Findings at a glance](https://daveleo.github.io/eps-network-findings/findings.html) | engineers: status of each finding, charts and statistics |
| [Full investigation report](https://daveleo.github.io/eps-network-findings/report.html) | the record: setup, methods, every test and result, limits |

Status 2026-10-09. The firmware itself and the raw bench data are kept in Expromo's private repository.

## Updating

The pages in `src/` are the same HTML fragments published internally. After changing one, run `python build.py`; it writes the standalone pages and `index.html` next to it, and replaces internal links with links between these pages.
