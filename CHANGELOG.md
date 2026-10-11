# Changelog

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
