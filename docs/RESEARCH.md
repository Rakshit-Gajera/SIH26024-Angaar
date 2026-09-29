# Angaar: research notes

The facts, numbers and findings behind the Angaar deck (SIH26024). Every number here was checked against the source linked next to it. Anything that is our own calculation is marked **(our calculation)**.

---

## 1. What SIH26024 asks for, and where Angaar answers it

| The problem statement asks for | Angaar |
|---|---|
| Digital tracking of statutory compliance (safety, environment, production, labour) | Obligations library turned into each mine's calendar; Star Rating, EC and return items tracked as declared vs verified |
| Real-time monitoring of inspections, observations, violations and corrective actions | Field app entries become actions with an owner, SLA and escalation; closure needs photo proof at the QR plate and a second person |
| AI/analytics for high-risk areas, recurring failures and anomalies | Cross-check engine, NDVI on Sentinel-2, Isolation Forest on attendance and readings, LightGBM with SHAP to order inspections |
| Geo-tagged, time-stamped field reporting on mobile | Installable web app that works offline; QR location plates underground where GPS does not work |
| Dashboards for mine officials, corporate management and regulators | Mine, Area, Subsidiary, CIL, CCO and DGMS views of the same record |
| Automated alerts, reminders, reports and escalation | SLA timers, escalation to Area GM, drafts of Star Rating evidence, PARIVESH six-monthly report and monthly returns |
| Less paperwork, more transparency and accountability | Data entered once; SHA-256 hash-chained audit log; every step signed |
| Scalable across mines and subsidiaries | Rollout from 5 pilot mines to all 380 Star Rating mines |
| Optional: GIS, OCR, blockchain audit trails, multilingual interfaces | Sentinel-2 maps, Tesseract OCR for letters, hash-chained log, Hindi voice through Bhashini |

## 2. The condition behind the problem

**Most compliance data is self-declared.**

- **Star Rating of Coal Mines** (Ministry of Coal, run by the Coal Controller's Organisation): mines self-evaluate on seven modules; the top 10% by self-assessed score get a physical inspection, the other 90% are reviewed online.
  Sources: [starrating.coal.gov.in](https://starrating.coal.gov.in/faq.php), [The Reporters' Collective, 27 Nov 2024](https://www.reporters-collective.in/trc/blinded-by-the-stars-a-govts-rating-scheme-is-helping-coal-miners-pat-their-own-back)
- **2022-23 cycle:** 380 mines took part and 43 got 5 stars. The Reporters' Collective found that 19 of those 43 had only partial or no compliance with some legally required environmental safeguards.
- **DGMS** has assigned coal mine inspections by risk through the Shram Suvidha portal since 2016 ([DGMS at a Glance 2023](https://www.dgms.net/DGMS%20AT%20A%20GLANCE%202023.pdf)). Better evidence makes that risk rating better.

## 3. Our study of the Star Rating opencast template

Source: [Template_OC.pdf](https://starrating.coal.gov.in/policy/Template_OC.pdf) (draft evaluation template for opencast mines).

- **50 numbered items** across 7 modules worth 100 points: mining operations (17), environment (26), technology (10), economic performance (15), rehabilitation and resettlement (8), worker compliance (8), safety and security (16).
- Star bands: 91-100% five stars, 81-90% four, 71-80% three, 61-70% two, 41-60% one.
- For every item, the mine fills in the "actual value" itself.

**9 of the 50 items have an independent record we can check every month (our calculation):**

| Item | What it is | Independent record |
|---|---|---|
| 9 | Ambient air quality: monitoring and limits | CPCB CAAQMS station data |
| 13 | EMP compliance report submitted on time | PARIVESH submission date |
| 18 | Biological reclamation of mined land | Sentinel-2 NDVI |
| 27 | Despatch target achieved | Railway rake loading and road weighbridge |
| 29 | Grade slippage (realisation) | Third-party sampling results on UTTAM |
| 40 | Orders under Section 22 | DGMS records |
| 43 | Disasters | DGMS records |
| 44 | Fatal accidents | DGMS records |
| 45 | Serious bodily injuries | DGMS records |

Items such as back-filling (measured in volume), haul road width and dump height need a drone or ground survey, so we did not count them.

## 4. The satellite check

- Data: Sentinel-2 L2A, bands B4 (red) and B8 (near infrared), 10 m pixels, from the Earth Search STAC catalogue ([earth-search.aws.element84.com](https://earth-search.aws.element84.com/v1)).
- Scenes: `S2B_45QVG_20250302_0_L2A` (2 Mar 2025) and `S2C_45QVG_20260302_0_L2A` (2 Mar 2026, cloud 0.0007%).
- Area: an overburden dump in Jharia coalfield, centre 23.758 N, 86.417 E, polygon area 39.3 ha.
- Rule: a pixel is green when NDVI ≥ 0.30. 0.30 is the median NDVI of natural vegetation 3 km west in the same image, so the rule adapts to the season.
- Result: 0.2 ha green in March 2025, 0.3 ha in March 2026. A declared reclamation of 12.0 ha (demo figure) would be flagged as a mismatch of 11.7 ha.
- Reproduce: `satellite-check/satellite_check.py`.

## 5. The impact estimate (our calculation)

- 380 mines rated in 2022-23; the top 10% (about 38) got a site visit.
- 9 of 50 opencast items have an outside record (section 3).
- Angaar checks all 380 mines every month on those 9 items: 380 × 12 = **4,560 mine-checks a year**, against about 38 site visits.
- This compares coverage, not depth: a site visit still checks all 50 items. Angaar tells the visit where to go first.

## 6. Scale and safety numbers

| Fact | Value | Source |
|---|---|---|
| India's coal output, FY 2024-25 | 1,047.5 Mt | [MoC Year End Review 2025, PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2213723) |
| Coal India mines, 1 April 2023 | 322 (138 underground, 171 opencast, 13 mixed) | [MoC Annual Report 2023-24, ch. 8](https://coal.gov.in/sites/default/files/2024-02/chap8AnnualReport2024en.pdf) |
| Fatal accidents in coal mines, 2013-22 | 528 accidents, 604 deaths; 2,614 serious accidents | [DGMS SANKET](https://dgms.net/Sanket%200404_2024.pdf) |
| Fatal accidents per year | 2013: 77, 2016: 67, 2020: 48, 2021: 43, 2022: 24, 2023: 38, 2024: 38, 2025: 41 | DGMS SANKET; DGMS; Lok Sabha reply, Aug 2026 |
| OSH Code 2020 | In force from 21 Nov 2025 | [PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2192802) |

## 7. Data sources and access

| Source | What Angaar uses it for | Access |
|---|---|---|
| Sentinel-2 (ESA Copernicus) | Reclamation, green belt, dump spread | Public, free |
| CPCB CAAQMS | Air quality against EC limits | Public |
| DGMS SANKET and records | Accidents, Section 22 orders, risk model training | Public reports; inspection records through DGMS |
| Coal Directory of India 2024-25 | Master list of mines | Public ([coalcontroller.gov.in](https://coalcontroller.gov.in/coal-directory-india)) |
| UTTAM | Third-party coal quality | Public ([uttam.coalindia.in](https://uttam.coalindia.in/sampling_process.html)) |
| PARIVESH | EC compliance filing dates | Public ([parivesh.nic.in](https://parivesh.nic.in)) |
| CLIP (CIL) | Contract wages by worker (WIN) | Through approved data sharing with CIL ([clip.cmpdi.co.in](https://clip.cmpdi.co.in/home)) |
| Attendance and despatch (CIL) | Wage and despatch cross-checks | Through approved data sharing with CIL |
| Bhashini | Hindi and regional speech-to-text | Public API ([bhashini.gov.in](https://bhashini.gov.in)) |
