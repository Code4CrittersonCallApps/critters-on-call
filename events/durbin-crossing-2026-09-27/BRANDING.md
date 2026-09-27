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

**Critters on Call Gold Membership card art** — real shipped card (Sophie the Great Pyrenees + goat-with-phone + pig + duck + ducklings), circular crop covering the hub disk.

| Asset | Source |
|-------|--------|
| `assets/gold-card-hub.jpg` | Crop of `exec/collateral/gold-card.jpg` (same art as flyers / gold-card brochure / membership one-pagers). Centered on the animal medallion + “CRITTERS ON CALL” card framing. |

- No CSS fake metallic medallion.
- No Betty / Gus flanking chrome on this event page.
- Sheehan Homestead / chicken-in-circle logo is **not** placed in the hub (source file used only to sample green).
- Header favicon + small brand chip may still use `hen-mark-gold.png` (monochrome/gold Critters mark).

## Event details (on-page)

Visible in `.event-details` on `index.html`: Sunday Sep 27 2026 · 10 AM–1 PM · Durbin Crossing · 145 South Durbin Parkway, St Johns FL 32259.

## Wheel labels

Scoped under `.dc-wheel`: font ~0.48rem, mid-wedge placement via JS (`i*45°+22.5°` with conic from `0deg`), short labels so each label stays inside its 45° wedge.
