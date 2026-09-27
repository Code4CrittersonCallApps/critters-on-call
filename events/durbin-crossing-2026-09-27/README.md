# Critters on Call × Durbin Crossing — prize wheel

**Event date:** Sunday, September 27, 2026 · 10 AM – 1 PM  
**Location:** Durbin Crossing · 145 South Durbin Parkway, St Johns, FL 32259  
**Event ID:** `durbin-crossing-2026-09-27`  
**Expires:** **2026-09-29 00:00:00 America/New_York** (end of Mon Sep 28 night) — page stays live; wheel non-functional with “Event ended”  
**Brand:** Forest `#4C6458`, deep `#3A4F45`, sage `#5A7366`, gold `#c9a227`. Hub = Critters on Call text. See `BRANDING.md`.  
**Farm claim address:** 44065 Cushman Road, Callahan, FL 32011

## Live URL (MUST stay exact)

https://onchainoffgrid-hub.github.io/critters-on-call/events/durbin-crossing-2026-09-27/

Goat variants: `?goat=01` … `?goat=12` — see `QR-STICKERS.md`.

## Local

```bash
cd /workspace/critters-on-call && python3 -m http.server 8766
```

http://localhost:8766/events/durbin-crossing-2026-09-27/

## Flow (psychology)

1. **Spin without email/phone** — no gate before the wheel.
2. Prize result shows **immediately** when the wheel stops.
3. Tap **“Claim your prize”** → on-screen claim paths (any one works):
   - Text **PRIZE** to **914-263-1311**
   - DM on Facebook (**Sheehan Homestead** — `https://www.facebook.com/profile.php?id=61556795506312`)
   - Email **sheehanhomestead@gmail.com** (mailto prefilled with prize + Durbin Crossing)
   - Website booking help: **https://www.sheehanhomestead.com/booking-help**
   Honest fallback — page does **not** capture claims server-side.
4. Claim panel also shows **farm address** + optional Google review. No tour push.
5. Max **3 spins** per device (localStorage spin counter only). **Free spin does not count** against the 3.

## Tester reset

Open this URL to clear the spin counters for this event and reload the wheel:

https://onchainoffgrid-hub.github.io/critters-on-call/events/durbin-crossing-2026-09-27/?reset=1

The reset clears only these event-scoped localStorage keys:

- `coc_dc_device_v2_durbin-crossing-2026-09-27`
- `coc_dc_identity_spins_v1_durbin-crossing-2026-09-27`

It does not clear leads, claims, or any production rules. The `reset=1` parameter is removed before the reload.

## Rules (client-side)

- Max **3 spins** · free-spin wedge does **not** decrement
- **Gold Card — TOP PRIZE** = $100 bundle: $50 Gold Card + $25 farm ticket + $25 gift; landing this wedge closes further spins
- **Free spin** does not decrement the 3-spin limit
- Claims: text PRIZE / Facebook DM / email / booking-help (not browser-only). Review link after claim reveal: `https://g.page/r/CS74JMTm3xrWEAE/review`
- Staff `admin.html` (PIN `0927`) is legacy tooling only

## Wheel (8 segments · equal 45° wedges) · weights sum 100%

Geometry: conic from `0deg`, labels at midpoints `i*45+22.5`, shared label radius. Opposite wedges differ by 180°.

| # | Prize | Weight | Notes |
|---|--------|--------|------|
| 0 | **GOLD CARD — TOP PRIZE** | **5%** | $100 bundle: $50 Gold Card + $25 farm ticket + $25 gift; locks further spins · `DCGOLD-*` |
| 1 | $10 thrift / toy gift | **18%** | Teaser: toy, comic book, basketball cards, tumbler · `DC10T-*` |
| 2 | $10 farm gift | **15%** | Teaser: elephant ear, sweet potato slip, fertilizer, eggs · `DC10F-*` |
| 3 | $25 thrift / toy gift | **10%** | `DC25T-*` |
| 4 | $25 farm gift | **10%** | `DC25F-*` |
| 5 | Free spin | **22%** | Does **not** count against 3-spin limit |
| 6 | $25 farm ticket | **10%** | Separate ticket wedge · `DC25TIX-*` |
| 7 | $25 farm ticket | **10%** | Separate duplicate ticket wedge · `DC25TIX-*` |

Gold Card is the clearly marked best prize. Its result copy spells out the $50 card + $25 ticket + $25 gift bundle, and the wheel disables all further spins after it lands.

Footer chrome (Staff tools / CRM / Goat QR / Branding / palette) is not on the guest wheel page.

## Files

- `index.html` — wheel + claim-after-spin + farm address + expiry  
- `assets/qr-wheel.png` — QR to live wheel URL  
- `admin.html` — CSV export / mailto stub  
- `hen-mark-gold.png` — hen mark (header/favicon only)  
- `qr/` — print QRs  
- `OUTLINE.md` — CRM warming  
- `QR-STICKERS.md` — 12 goat URLs  
- `BRANDING.md` — greens + logo flag  

## Deploy

```bash
cd /workspace/critters-on-call
git add events/durbin-crossing-2026-09-27
git commit -m "Durbin Crossing wheel: mid-wedge labels, grand=Gold Membership uncapped"
git push origin main
```

Live path must remain `/events/durbin-crossing-2026-09-27/` so goat stickers keep working.
