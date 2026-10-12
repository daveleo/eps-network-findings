# EPS network findings

Public documents on why Expromo EPS power sequencers (Keyestudio KS0304: ATmega328P + WIZnet W5500) drop off the network on firmware v2.2, a code analysis of the firmware, and the firmware line that fixes it: v3.0–v3.2 and **v3.3, the recommended official firmware**, with every version compared on the same bench.

**Read online:** https://daveleo.github.io/eps-network-findings/

| Document | For |
|---|---|
| [Why v3.3 should be official](https://daveleo.github.io/eps-network-findings/why-v3-3.html) | the decision brief: what the code analysis found, what v3.3 changes, the evidence, limits |
| [All versions compared](https://daveleo.github.io/eps-network-findings/comparison.html) | v2.2, v3.1, v3.2, v3.3 side by side: features, 17-fault matrix, recovery, standards, regression |
| [Executive summary](https://daveleo.github.io/eps-network-findings/executive-summary.html) | decision makers and IT: what changed from v2.2 to v3.3, comparison with v2.2 on the bench and against network standards, fit with enterprise network practice, limits, rollout |
| [Findings at a glance](https://daveleo.github.io/eps-network-findings/findings.html) | engineers: status of each finding, charts and statistics |
| [Full investigation report](https://daveleo.github.io/eps-network-findings/report.html) | the record: setup, methods, every test and result, limits |
| [Hvorfor v3.3](https://daveleo.github.io/eps-network-findings/hvorfor-v3-3.html) (dansk) | kort orientering: hvad er ændret fra v2.2 til v3.3, og hvorfor vi bør bruge v3.3 |
| [Alle versioner sammenlignet](https://daveleo.github.io/eps-network-findings/comparison-da.html) (dansk) | the comparison page in Danish |

Status 2026-10-12 (v3.3 recommended as official). The earlier brief [Why v3.2](https://daveleo.github.io/eps-network-findings/why-v3-2.html) stays online. The firmware itself and the raw bench data are kept in Expromo's private repository.

## Updating

The pages in `src/` are the same HTML fragments published internally. After changing one, run `python build.py`; it writes the standalone pages and `index.html` next to it, and replaces internal links with links between these pages. Danish pages are listed in `PAGES_DA` (they get `lang="da"` and a Danish nav); the Danish comparison's fault-matrix rows are translated from the English page, so update both when the data changes.
