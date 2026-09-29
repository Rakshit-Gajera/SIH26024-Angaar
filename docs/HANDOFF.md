# Angaar: project handoff

Current state of the Angaar project (SIH26024, team Computer Smashers, Team ID 178955) and what comes next. Read the [README](../README.md) first for the idea itself.

## 1. Status

| Item | State | Where |
|---|---|---|
| Idea deck (6 slides, NMIET template) | Done | `presentation/Angaar_SIH26024_Computer_Smashers.pptx` |
| Deck as PDF for the SIH portal | Done | `presentation/Angaar_SIH26024_Computer_Smashers.pdf` |
| App screens (mine view, satellite check, two phone screens) | Done | `screens/html`, `screens/png` |
| Satellite reclamation check on real Sentinel-2 data | Done and reproducible | `satellite-check/satellite_check.py` |
| Research, numbers and sources | Done | `docs/RESEARCH.md` |

**Deadline:** SIH 2026 idea submission closes on 30 September 2026. Upload the **PDF**, not the PPTX. Check your college SPOC's internal deadline, which may be earlier.

## 2. What is in the deck

| Slide | Content |
|---|---|
| 1. Title | SIH26024, the PS title, Smart Automation, Software, Team ID 178955, Computer Smashers |
| 2. Proposed solution | Why it is needed (Star Rating: 380 mines self-rated, top 10% visited), the idea, how it addresses the problem, what is new; mine view and phone screens |
| 3. Technical approach | Stack table (who built each part), 5-step flow: Capture, Collect, Cross-check, Act, Report; human control line |
| 4. Feasibility and viability | Satellite check screen, feasibility (technical, economic, operational), three risks with strategies, rollout |
| 5. Impact and benefits | Estimate: 38 site visits vs 4,560 mine-checks a year, with the working; impact by user; social, economic and environmental benefits; scale; beyond India |
| 6. Research and references | 11 verified links, data links note, our Star Rating study: 9 of 50 items checkable |

Deck style rules used:
- Titles in Times New Roman (template), body in Arial, all text 14 pt or larger.
- Two colours: navy `#1F497D` and amber `#C55A11`.
- No em dashes and no filler words.
- The template's section headings are kept word for word.

## 3. Key decisions

- **Name:** Angaar (अंगार), a glowing coal ember.
- **One web app for office and phone.** It installs on Android and works offline, so there is no separate app-store release.
- **Human control.** Rules and our models flag mismatches; Llama only drafts report text; an officer closes every case. A mismatch opens a review, never a penalty.
- **Honest data.** Screens use demo data for a fictional mine (JH-OC-07) and say so. The satellite values are real.
- **References** cite official sources only.

## 4. Build plan (next steps)

1. **Obligations library:** Star Rating items, EC and CTO conditions, CMR 2017 and OSH Code 2020 duties as data, with a calendar per mine.
2. **Field app (PWA):** offline queue (IndexedDB), QR plate scan, in-app camera, Hindi voice note (Bhashini), pre-shift district clearance.
3. **Cross-check engine:** start with the four checks that use public data (Sentinel-2 reclamation, CPCB air quality, DGMS records, PARIVESH filing dates), then CLIP wages and despatch once data sharing with CIL is approved.
4. **Actions and escalation:** owner, SLA, escalation to Area GM, closure with photo proof (perceptual-hash reuse check) and second-person verification.
5. **Dashboards:** mine, area, subsidiary, CCO and DGMS views of declared vs verified.
6. **Drafts:** Star Rating evidence pack, PARIVESH six-monthly report, monthly returns.
7. **Pilot:** 5 mines in one BCCL area for 3 months, then one subsidiary at month 6.

## 5. Running what exists

```bash
# satellite check (real Sentinel-2 data)
cd satellite-check
pip install -r requirements.txt
python satellite_check.py
```

To view the screens, open any file in `screens/html` in a browser.
