# Investor Jax geo · Sheehan Homestead

**as_of:** 2026-09-26 7:00 PM ET  
**Seat:** Michael Sheehan / Sheehan Homestead · Jacksonville investor landing layer

## Investor proof (prefer these)

| Artifact | Path |
|---|---|
| **Excel (primary)** | `/workspace/critters-on-call/exec/data/INVESTOR_JAX_GEO.xlsx` |
| Excel copy | `/workspace/assets/INVESTOR_JAX_GEO.xlsx` |
| Excel copy | `/workspace/revops/INVESTOR_JAX_GEO.xlsx` |
| CSV | `/workspace/critters-on-call/exec/data/investor_jax_geo.csv` |
| JSON | `/workspace/critters-on-call/exec/data/investor_jax_geo.json` |
| Map HTML | `/workspace/critters-on-call/exec/investor-jax-geo.html` |

### Excel sheets
- `00_README` — rules, KPIs, sources
- `01_PINS` — full TAM geo + tags (1,522)
- `02_COUNTIES` — Duval / St. Johns / Clay / Nassau / Camden / Putnam / Baker / Bradford / Flagler
- `03_MANAGERS` — Vesta · GMS · MAY · First Coast · national (FSR/Greystar/…)
- `04_CUSTOMERS` — customer + lapsed only
- `05_FOCUS` — investor-focus subset (~523: managed · customer · S/A · Regional Enterprise / CDD-ish)

## What this is
Map-first **Jacksonville metro** investor view: start from geography → click a place/account → see CDD group, manager family (national vs regional vs local), wallet tier from honest `s_tier` / `market_tier` (no invented AA/AAA) → deep-link dunk / TAM / account pages in ~2 clicks.

## Data honesty
- **Sources:** `MASTER_GTM_TAM_Accounts.xlsx` (`02_ACCOUNTS`, `06_VESTA_CLUSTER`, `01_SEGMENT_TAM`) + `bookings_pipeline.json` + `bdr_tam_dialer.json` (customer enrich only).
- **Zero fabricated emails/names.** Mailto only when email already in TAM.
- **Geo:** city/county centroids → badge **Estimated** (no paid Mapbox).
- **Wallet labels:** `s_tier` S/A/B/C/D → "Wallet S/A/B/C/D". `market_tier` shown separately. **Do not invent AAA.**
- **Customer vs prospect:** primary = `penetration` (customer|lapsed|prospect); Vesta overlay from `06_VESTA_CLUSTER`; dialer `is_customer` enrich. Pipeline flag = strong bookings title match (not a customer invent).

## Pin / rollup counts (as shipped)
- Pins total: **1522**
- Investor focus default: **~523**
- Managed (has `management_company`): **126**
- Customers (after enrich): see Excel `00_README` / `04_CUSTOMERS`
- Counties: Duval 877 · St. Johns 285 · Clay 171 · Nassau 115 · Camden 58 · + thin Putnam/Baker/Bradford/Flagler

## Manager scale (tagged, not invented)
- **National:** FirstService Residential, Greystar, AIR Communities, Invited, Troon, Concert Golf, Gables Residential
- **Regional (FL amenity/CMS):** Vesta, GMS, MAY Management, First Coast CMS
- **Local:** CMC Jacksonville, Lifestyles Property Services, Brahm, …

## Deep links (HTML; Excel is the rigor proof)
- Dunk: `principal-dunk.html`
- TAM: `bdr-tam.html`
- Account pages when matched: `account-vesta.html`, `account-may.html`, `account-first-coast.html`, `account-trees.html`
- Expansion twin: `expansion-tampa.html` / `market-tampa.html`

## Sample click paths (HTML)
1. Open map → click **St. Johns** bubble → pin **Durbin Crossing CDD (Vesta)** → tags Manager:Vesta · Regional · Wallet S · customer → related Vesta CDDs → **Dunk** / **account-vesta.html**
2. Filter **MAY Management** → pin any MAY CDD → related under MAY → `account-may.html` + TAM
3. Filter **Customers** → pick a Duval customer → mailto if public email → dunk board

## IA
Ops homepage primary · dunk high flyer from Growth · Trophy case · Jax geo = Jacksonville investor entry · Tampa expansion already shipped.

## No GitHub push
Local suite + `/workspace/assets/` + `/workspace/critters-on-call/exec/` copies only.
