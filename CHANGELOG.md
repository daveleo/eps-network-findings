# Changelog

## 2026-10-11 — New page: "Why v3.2 should be official"
- Added a fourth document, `why-v3-2.html`: a decision brief making the scientifically grounded, unbiased case for adopting v3.2. Verdict/recommendation first, then the v2.2 → v3.0 → v3.1 → v3.2 change lineage (each step tied to the finding that drove it), a tested v2.2-vs-v3.2 comparison table, a simplified view of the 14-fault matrix, cost/compatibility, honest limits, and the case for adoption.
- Every claim links to the section of the other pages that justifies it (findings `#h-ab`, `#h-mech`, `#h-dhcp`, `#h-faults`, `#h-std`, `#h-corr`; executive summary `#h-standards`, `#h-limits`, `#h-rollout`; full report).
- `build.py` now builds four pages and the nav carries "Why v3.2"; landing page leads with the new brief (status 2026-10-11).

## 2026-10-11 (round 2) — v3.2 fault-matrix results; v3.2 recommended
- All three pages updated with the measured v3.2 results. Findings: the single-register fault table gains a v3.2 column — v3.2 recovers from all 14 faults, including the four v3.1 died on (ping block, retry count 0, forced 10-half and the field-matching PHY power-down, back in 11–12 s with no reset); no dead outcome anywhere, outputs never moved, no false re-init in steady state.
- The two tail-only FAILs noted honestly as the stray-ping check (it also fired on faults that cannot affect ping), not service loss.
- Candidate box and executive-summary note rewritten from "under test" to tested; all three pages now recommend v3.2 as the field candidate in place of v3.1 (+118 B flash). Report page regenerated with the measured v3.2 paragraph and chronology.

## 2026-10-11 — Single-register fault matrix, reset start-up, v3.2 candidate
- All three pages updated. Findings: new section on the single-register chip-fault test (14 faults × 3, v3.1 vs v2.2) — v3.1 repairs the 5 registers it checks and survives socket faults; v2.2 dead or stuck on 12 of 14. Four faults (ping block, retry count 0, forced 10-half, PHY power-down) fall outside v3.1's check; PHY power-down reproduces the field symptom exactly.
- Reset start-up: 200 USB resets each, v3.1 and v2.2 both 200/200, no deaf event (the deaf start-up has only ever appeared on unit 2).
- Candidate v3.2 noted on all three pages: widens the 5 s health check to the mode, retry and PHY registers; built and under test, v3.1 stays final until it proves out.
- Report page regenerated from the full report (new §5.24).

## 2026-10-10 — v3.1 as the final firmware
- All three pages updated: v3.1 presented as the current final firmware; final-build re-run of every short test; pre-registered standards suite (56 requirements, 10 standards): v3.1 46 pass, v2.2 26 pass, with causes and what is fixable.
- Corrected: v2.2 does not use one MAC for every unit; its MAC is set per unit before flashing (passes IEEE 802 MAC addressing).
- Findings page: new chart of requirements per standard (with table view). Landing page and README updated.

## 2026-10-09 — First version
- Executive summary of EPS firmware 3.0, findings at a glance, full investigation report; landing page; `build.py`.
