# Branding — Durbin Crossing wheel

## Hex greens used (wife chicken-in-circle logo)

| Token | Hex | Source |
|-------|-----|--------|
| Forest (primary) | `#4C6458` | Dominant fill sampled from Drive **Homestead Logo Circle.png** (wife chicken logo). Local copy: `/workspace/assets/durbin-qr/homestead-logo-circle.png` (Drive id `1iGq6b_C34hT68kWpEDf19zV8_DIALBVx`). Also reads `#4E6558` as mean. |
| Forest deep | `#3A4F45` | Darker companion for alternating wheel segments / hub gradient |
| Sage | `#5A7366` | Lighter companion accent / buttons |
| Card gold | `#c9a227` | Critters / membership gold |
| Gold deep | `#B8923A` | gold-card deep gold |
| Cream | `#F3EEE4` | cream text |

**Not used:** gold-card brochure `#2F4F3E` / `#4F6559`, website leaf `#3d6b4f`.

## Wheel center (hub)

**Critters on Call Gold Membership medallion** — metallic gold gradient hub (`.gold-card-hub`) with embossed card feel, generic chip accent, and `.wheel-hub-brand` text: “Critters on Call” / “GOLD” / “Member”. Evokes premium gold membership card marketing; not a bank trademark 1:1.

**Betty & Gus** (farm guardians from Homestead Defender / Pyrenees Guard):

| Character | Role | Asset |
|-----------|------|-------|
| Betty | Barn Queen · cream Great Pyrenees | `assets/betty.png` (from `/workspace/critters-play/assets/betty.png`) |
| Gus | Night Scout · black-and-tan Pyrenees mix | `assets/gus.png` (from `/workspace/critters-play/assets/gus.png`) |

Placed as fixed chrome flanking the wheel (`.wheel-mascot--betty` / `--gus`) so they do **not** spin with the wheel.

- Sheehan Homestead / chicken-in-circle logo is **not** placed in the hub (source file used only to sample green).
- Header favicon + small brand chip may still use `hen-mark-gold.png` (monochrome/gold Critters mark).

## Event details (on-page)

Visible in `.event-details` on `index.html`: Sunday Sep 27 2026 · 10 AM–1 PM · Durbin Crossing · 145 South Durbin Parkway, St Johns FL 32259 · Animal pickup 8:45 AM · Kate Smith / Vesta CDD line.

## Wheel labels (v3 voice)

Scoped under `.dc-wheel`: font ~0.48rem, `span` `top: 0.32rem` (toward rim), width ~2.85rem, two-line shorts (`$10<br>THRIFT`, etc.) so each label stays inside its 45° wedge.
