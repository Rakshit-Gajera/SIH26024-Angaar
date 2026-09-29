# Angaar: instructions for AI coding agents (same as CLAUDE.md)

Read [`README.md`](README.md) for the idea and [`docs/HANDOFF.md`](docs/HANDOFF.md) for the current state and next steps. Facts and numbers live in [`docs/RESEARCH.md`](docs/RESEARCH.md); reuse them rather than guessing.

## Project

- SIH 2026, problem statement **SIH26024** (Ministry of Coal, Software, Smart Automation), team **Computer Smashers** (Team ID 178955).
- Product: **Angaar (अंगार)**. It checks what a coal mine declares against records the mine does not write, and shows Declared vs Verified compliance per mine.

## Layout

- `presentation/`: the deck (PPTX and PDF) and the NMIET template.
- `screens/html`, `screens/png`: app screens.
- `satellite-check/`: the working Sentinel-2 reclamation check.
- `docs/`: problem statement, research, handoff.

## Rules

1. Only use numbers that are in `docs/RESEARCH.md` or checked against a linked source; mark your own calculations as estimates.
2. Screens use demo data for a fictional mine (JH-OC-07) and must say so; never present demo figures as real mine data.
3. Writing style for the deck and docs:
   - plain and concrete, with real numbers and place names;
   - no em dashes;
   - none of the words "seamless", "leverage", "robust", "empower", "cutting-edge", "revolutionize", "game-changer", "holistic" or "unlock".
4. Deck style:
   - Times New Roman titles, Arial body, text 14 pt or larger;
   - navy `#1F497D` and amber `#C55A11`;
   - keep the template's section headings word for word.
5. Never commit secrets or API keys.
