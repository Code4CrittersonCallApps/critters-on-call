import os
import subprocess
import qrcode
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE_DIR, "assets")
PNG_DIR = os.path.join(BASE_DIR, "png")
os.makedirs(PNG_DIR, exist_ok=True)

QR_TARGETS = {
    "qr-gold.png": "https://code4crittersoncallapps.github.io/gold/",
    "qr-gift-card.png": "https://code4crittersoncallapps.github.io/critters-on-call/book/?product=gift-card-deal",
    "qr-birthday.png": "https://code4crittersoncallapps.github.io/critters-on-call/book/?product=birthday-party",
    "qr-homeschool.png": "https://code4crittersoncallapps.github.io/critters-on-call/book/?product=homeschool-mon-10",
    "qr-field-trip.png": "https://code4crittersoncallapps.github.io/critters-on-call/book/?product=field-trip-small",
}

def make_qrs():
    detector = cv2.QRCodeDetector()
    for fname, url in QR_TARGETS.items():
        out = os.path.join(ASSETS, fname)
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=12,
            border=2,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="#1a241c", back_color="#ffffff")
        img.save(out)
        mat = cv2.imread(out)
        decoded, _, _ = detector.detectAndDecode(mat)
        assert decoded == url, f"QR mismatch for {fname}: got {decoded!r}, expected {url!r}"
        print(f"QR OK: {fname} -> {decoded}")

SHARED_CSS = """
@font-face {
  font-family: "Playfair Display";
  src: url("assets/PlayfairDisplay-Variable.ttf") format("truetype");
  font-weight: 400 900; font-style: normal;
}
@font-face {
  font-family: "Playfair Display";
  src: url("assets/PlayfairDisplay-Italic-Variable.ttf") format("truetype");
  font-weight: 400 900; font-style: italic;
}
@font-face {
  font-family: "Source Sans 3";
  src: url("assets/SourceSans3-Variable.ttf") format("truetype");
  font-weight: 200 900; font-style: normal;
}
@font-face {
  font-family: "Cinzel";
  src: url("assets/Cinzel-Variable.ttf") format("truetype");
  font-weight: 400 900; font-style: normal;
}

:root {
  --forest: #4C6458;
  --forest-deep: #3A4F45;
  --sage: #5A7366;
  --gold: #c9a227;
  --gold-deep: #B8923A;
  --gold-light: #E8D48C;
  --cream: #F3EEE4;
  --white: #FFFDF8;
  --ink: #1a241c;
  --muted: #516157;
  --line: rgba(58, 79, 69, 0.18);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html, body {
  background: #ded7c7;
  color: var(--ink);
  font-family: "Source Sans 3", "Liberation Sans", sans-serif;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

@page { size: Letter; margin: 0; }

.page {
  width: 8.5in;
  height: 11in;
  margin: 0 auto;
  background: var(--cream);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  position: relative;
  border: 0.105in solid var(--forest-deep);
  outline: 0.055in solid var(--gold);
  outline-offset: -0.175in;
}

@media print {
  html, body { background: var(--cream); width: 8.5in; height: 11in; }
  .page { margin: 0; }
}

.why {
  flex: 0 0 auto;
  background: linear-gradient(180deg, #E8D48C 0%, #c9a227 52%, #B8923A 100%);
  color: var(--forest-deep);
  text-align: center;
  padding: 0.075in 0.22in 0.065in;
  border-bottom: 0.045in solid var(--forest-deep);
}
.why .kicker {
  font-family: "Cinzel", serif;
  font-weight: 800;
  font-size: 9pt;
  letter-spacing: 0.19em;
  text-transform: uppercase;
  color: var(--forest-deep);
  margin-bottom: 0.015in;
}
.why .headline {
  font-family: "Playfair Display", serif;
  font-weight: 900;
  font-size: 31pt;
  line-height: 0.96;
  letter-spacing: -0.02em;
  color: var(--forest-deep);
  text-shadow: 0 1px 0 rgba(255,253,248,0.55);
}
.why .headline.xl { font-size: 34pt; }

.event {
  flex: 0 0 auto;
  background: var(--forest-deep);
  color: var(--cream);
  text-align: center;
  padding: 0.05in 0.14in;
  font-family: "Cinzel", serif;
  font-size: 8.9pt;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  border-bottom: 0.038in solid var(--gold);
  white-space: nowrap;
}
.event .gold { color: var(--gold-light); }

.main {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 0.10in 0.24in 0.085in;
  gap: 0.07in;
  min-height: 0;
  background:
    radial-gradient(ellipse at 50% 18%, rgba(201,162,39,0.16) 0%, transparent 62%),
    var(--cream);
}

.hero-strip {
  display: grid;
  grid-template-columns: 1.32fr 1fr;
  gap: 0.12in;
  align-items: stretch;
  flex: 0 0 auto;
}

.hero-box {
  background: var(--forest-deep);
  color: var(--cream);
  border-radius: 7px;
  padding: 0.095in 0.13in;
  border: 2px solid var(--gold);
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.hero-box .tag {
  display: inline-block;
  align-self: flex-start;
  background: var(--gold);
  color: var(--forest-deep);
  font-family: "Cinzel", serif;
  font-weight: 800;
  font-size: 7.4pt;
  letter-spacing: 0.11em;
  text-transform: uppercase;
  padding: 2px 7px;
  border-radius: 4px;
  margin-bottom: 0.04in;
}
.hero-box h2 {
  font-family: "Playfair Display", serif;
  font-weight: 800;
  font-size: 16.5pt;
  line-height: 1.06;
  color: #fff;
  margin-bottom: 0.04in;
}
.hero-box h2 em { font-style: normal; color: var(--gold-light); }
.hero-box p {
  font-size: 9.2pt;
  line-height: 1.28;
  color: rgba(243, 238, 228, 0.94);
}
.hero-price-line {
  display: flex;
  align-items: baseline;
  gap: 0.08in;
  margin-top: 0.05in;
  padding-top: 0.045in;
  border-top: 1px solid rgba(232,212,140,0.35);
  flex-wrap: wrap;
}
.hero-price-line .yp-lab {
  font-size: 8pt;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--gold-light);
  font-weight: 700;
}
.hero-price-line .yp-val {
  font-family: "Playfair Display", serif;
  font-size: 20pt;
  font-weight: 900;
  color: #fff;
  line-height: 1;
}
.hero-price-line .yp-was {
  font-size: 9pt;
  color: rgba(243,238,228,0.78);
}
.hero-price-line .yp-save {
  background: var(--gold);
  color: var(--forest-deep);
  font-weight: 800;
  font-size: 8.4pt;
  padding: 1.5px 7px;
  border-radius: 999px;
}

.photo-card {
  border: 0.028in solid var(--forest-deep);
  box-shadow: 0 0 0 0.022in var(--gold), 0 3px 10px rgba(26,36,28,0.20);
  border-radius: 6px;
  overflow: hidden;
  background: #1a241c;
  position: relative;
  min-height: 1.45in;
}
.photo-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.photo-card .cap {
  position: absolute;
  left: 0; right: 0; bottom: 0;
  background: rgba(26, 36, 28, 0.86);
  color: var(--gold-light);
  font-size: 7.5pt;
  font-weight: 700;
  letter-spacing: 0.03em;
  padding: 3px 6px;
  text-align: center;
}

.photos-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.11in;
  height: 1.42in;
  flex: 0 0 auto;
}
.photos-2 .photo-card { min-height: 0; height: 100%; }

.sec-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  border-bottom: 1.5px solid rgba(58,79,69,0.25);
  padding-bottom: 0.02in;
  margin-bottom: 0.04in;
}
.sec-head h3 {
  font-family: "Playfair Display", serif;
  font-size: 13pt;
  font-weight: 800;
  color: var(--forest-deep);
}
.sec-head span {
  font-size: 8pt;
  font-weight: 700;
  color: var(--sage);
  text-transform: uppercase;
  letter-spacing: 0.07em;
}

.deals-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.075in;
  flex: 0 0 auto;
}
.deal {
  background: var(--white);
  border: 1px solid rgba(58,79,69,0.22);
  border-top: 0.04in solid var(--gold);
  border-radius: 6px;
  padding: 0.065in 0.09in 0.065in;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 0.03in;
}
.deal.featured {
  border: 1.5px solid var(--gold-deep);
  border-top: 0.048in solid var(--forest-deep);
  background: #FFFBF0;
}
.deal .dk {
  font-size: 7pt;
  font-weight: 800;
  letter-spacing: 0.09em;
  text-transform: uppercase;
  color: var(--sage);
}
.deal h4 {
  font-family: "Playfair Display", serif;
  font-size: 11.2pt;
  font-weight: 800;
  color: var(--forest-deep);
  line-height: 1.1;
  margin-top: 1px;
}
.deal p.desc {
  font-size: 8.4pt;
  line-height: 1.22;
  color: var(--ink);
}
.deal .pbox {
  margin-top: 0.02in;
  padding-top: 0.035in;
  border-top: 1px dashed rgba(58,79,69,0.22);
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 5px;
  flex-wrap: wrap;
}
.deal .yp {
  font-size: 7.9pt;
  font-weight: 700;
  color: var(--forest-deep);
}
.deal .yp strong {
  font-family: "Playfair Display", serif;
  font-size: 13pt;
  font-weight: 900;
  color: var(--forest-deep);
  margin-left: 2px;
}
.deal .ys {
  font-size: 7.6pt;
  font-weight: 800;
  color: var(--forest-deep);
  background: rgba(201,162,39,0.26);
  border: 1px solid rgba(184,146,58,0.55);
  border-radius: 999px;
  padding: 1px 6px;
  white-space: nowrap;
}
.deal .lst {
  font-size: 7.6pt;
  color: var(--muted);
  width: 100%;
  line-height: 1.15;
}

.perks-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0.075in;
  flex: 0 0 auto;
}
.perk {
  background: var(--white);
  border: 1px solid rgba(58,79,69,0.22);
  border-top: 0.035in solid var(--forest-deep);
  border-radius: 6px;
  padding: 0.055in 0.065in;
  text-align: center;
}
.perk .pv {
  font-family: "Playfair Display", serif;
  font-weight: 900;
  font-size: 11.5pt;
  color: var(--gold-deep);
  line-height: 1.05;
}
.perk h4 {
  font-size: 9pt;
  font-weight: 800;
  color: var(--forest-deep);
  margin: 1px 0;
  line-height: 1.12;
}
.perk p {
  font-size: 7.8pt;
  line-height: 1.2;
  color: var(--muted);
}

.proof-bar {
  display: flex;
  flex-wrap: nowrap;
  gap: 0.06in;
  align-items: center;
  justify-content: center;
  flex: 0 0 auto;
}
.chip {
  background: var(--forest-deep);
  color: var(--cream);
  font-family: "Cinzel", serif;
  font-size: 7.2pt;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  padding: 0.028in 0.075in;
  border: 1px solid var(--gold);
  border-radius: 3px;
  white-space: nowrap;
}
.chip.light {
  background: #FFFBF0;
  color: var(--forest-deep);
  border: 1px solid var(--gold-deep);
}

.bookrow {
  display: grid;
  grid-template-columns: 1.56in 1fr;
  gap: 0.12in;
  align-items: center;
  background: var(--white);
  border: 1.5px solid var(--forest-deep);
  border-radius: 7px;
  padding: 0.07in 0.11in;
  flex: 0 0 auto;
}
.qr-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.scan-shout {
  font-family: "Cinzel", serif;
  font-size: 7.8pt;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--gold-light);
  background: var(--forest-deep);
  padding: 2.5px 6px;
  border: 1px solid var(--gold);
  margin-bottom: 3px;
  width: 100%;
  text-align: center;
}
.qr-frame {
  display: block;
  width: 1.18in;
  height: 1.18in;
  background: #fff;
  border: 2.5px solid var(--forest-deep);
  box-shadow: 0 0 0 1.5px var(--gold);
  padding: 2px;
}
.qr-frame img { width: 100%; height: 100%; display: block; }
.qr-cap {
  margin-top: 2px;
  font-size: 6.8pt;
  font-weight: 700;
  color: var(--forest-deep);
  text-align: center;
  line-height: 1.15;
}

.cta-copy h3 {
  font-family: "Playfair Display", serif;
  font-weight: 800;
  font-size: 13.5pt;
  color: var(--forest-deep);
  line-height: 1.1;
  margin-bottom: 3px;
}
.cta-copy p {
  font-size: 8.8pt;
  line-height: 1.24;
  color: var(--ink);
  margin-bottom: 5px;
}
.btn-row {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  margin-top: 2px;
}
.btn {
  display: inline-block;
  text-decoration: none;
  font-weight: 800;
  font-size: 8.5pt;
  padding: 4.5px 10px;
  border-radius: 5px;
  letter-spacing: 0.02em;
}
.btn-primary {
  background: var(--forest-deep);
  color: var(--gold-light);
  border: 1.5px solid var(--gold);
}
.btn-gold {
  background: var(--gold);
  color: var(--forest-deep);
  border: 1.5px solid var(--forest-deep);
}
.fine-note {
  font-size: 7.2pt;
  line-height: 1.2;
  color: var(--muted);
  margin-top: 4px;
}

.foot {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  gap: 0.10in;
  padding: 0.065in 0.22in 0.07in;
  background: var(--forest-deep);
  color: var(--cream);
  border-top: 0.032in solid var(--gold);
}
.foot img.sophie {
  width: 0.56in;
  height: 0.56in;
  border-radius: 50%;
  border: 0.02in solid var(--gold);
  object-fit: cover;
  background: #fff;
  flex-shrink: 0;
}
.foot .brand { flex: 1; min-width: 0; }
.foot .brand .name {
  font-family: "Cinzel", serif;
  font-weight: 800;
  font-size: 9.8pt;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--gold-light);
  line-height: 1.15;
}
.foot .brand .sub {
  font-size: 8.2pt;
  font-weight: 600;
  color: var(--cream);
  line-height: 1.22;
  margin-top: 1px;
}
.foot .phone {
  text-align: right;
  font-weight: 800;
  font-size: 11.5pt;
  color: var(--gold-light);
  line-height: 1.12;
  flex-shrink: 0;
}
.foot .phone a { color: var(--gold-light); text-decoration: none; }
.foot .phone small {
  display: block;
  font-size: 7.2pt;
  font-weight: 600;
  letter-spacing: 0.04em;
  color: var(--cream);
  text-transform: uppercase;
}

@media screen and (max-width: 860px) {
  html, body { background: var(--cream); }
  .page {
    width: 100%;
    height: auto;
    min-height: 100vh;
    border-width: 6px;
    outline-width: 2px;
    outline-offset: -10px;
  }
  .event { white-space: normal; }
  .proof-bar { flex-wrap: wrap; }
  .why .headline, .why .headline.xl { font-size: 24pt; }
  .main { padding: 14px; gap: 12px; }
  .hero-strip, .photos-2, .deals-grid, .perks-4, .bookrow {
    grid-template-columns: 1fr;
    height: auto;
  }
  .photo-card { min-height: 190px; }
  .photos-2 .photo-card { height: 190px; }
  .qr-frame { width: 148px; height: 148px; }
  .foot { flex-direction: column; text-align: center; padding: 12px; }
  .foot .phone { text-align: center; }
}
"""

def wrap_page(title, desc, body_html):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" href="assets/sophie-logo.png">
<style>
{SHARED_CSS}
</style>
</head>
<body>
<div class="page">
{body_html}
</div>
</body>
</html>
"""

FOOTER_HTML = """
  <div class="foot">
    <img class="sophie" src="assets/sophie-logo.png" alt="Sophie the Great Pyrenees and the Critters on Call animal family">
    <div class="brand">
      <div class="name">Critters on Call · Sheehan Homestead</div>
      <div class="sub">44065 Cushman Road, Callahan, FL 32011 · sheehanhomestead.com · sheehanhomestead@gmail.com</div>
    </div>
    <div class="phone"><a href="tel:9142631311">914-263-1311</a><small>Call or text GOAT</small></div>
  </div>
"""

# ---------------------------------------------------------------------------
# 1. BLACK FRIDAY GOLD MEMBER HERO FLYER
# ---------------------------------------------------------------------------
flyer_gold_body = f"""
  <div class="why">
    <div class="kicker">Black Friday – Cyber Monday · Nov 27 – Dec 1, 2026</div>
    <div class="headline xl">Critter Gold for $1</div>
  </div>
  <div class="event">
    Black Friday Hero Deal <span class="gold">·</span> Gold Membership $1 + $50 Gift Card at 50% Off <span class="gold">·</span> Christmas Gift Ready
  </div>
  <div class="main">
    <div class="hero-strip">
      <div class="hero-box">
        <span class="tag">Black Friday Hero Bundle</span>
        <h2>Unlock Gold for <em>$1</em> + Half-Off Gift Card</h2>
        <p>Skip the plastic clutter this Christmas — give a full year of farm mornings, animals, and big savings. Get Critter Gold (normally $49.99) for <strong>$1</strong>, and pair it with a <strong>$50 Homestead Gift Card at 50% off ($25)</strong>.</p>
        <div class="hero-price-line">
          <span class="yp-lab">Your price</span>
          <span class="yp-val">$26</span>
          <span class="yp-was"><s>$99.99</s> ($1 Gold + $25 Card)</span>
          <span class="yp-save">You save $73.99</span>
        </div>
      </div>
      <div class="photo-card">
        <img src="assets/gold-card.jpg" alt="Critters on Call Gold Member Card — In Critters We Trust, 914-263-1311" style="object-fit:contain;background:#1a241c;padding:4px 6px 20px;">
        <div class="cap">Critter Gold Member · Or get Gold alone for $1 (save $48.99)</div>
      </div>
    </div>

    <div>
      <div class="sec-head">
        <h3>What Your $1 Gold Membership Includes</h3>
        <span>Normally $49.99/yr · You save $48.99</span>
      </div>
      <div class="perks-4" >
        <div class="perk">
          <div class="pv">FREE</div>
          <h4>2-Person Farm Tour</h4>
          <p>$25 value. Meet at least 8 animals on our Callahan homestead.</p>
        </div>
        <div class="perk">
          <div class="pv">FREE</div>
          <h4>Farm Gift or Thrifty Toy</h4>
          <p>Up to $25 value — farm eggs, plants, or a classic toy treasure in person.</p>
        </div>
        <div class="perk">
          <div class="pv">FREE</div>
          <h4>Prototype App Access</h4>
          <p>Play farm games, explore animal lessons &amp; spin Stead Spin online.</p>
        </div>
        <div class="perk">
          <div class="pv">40% OFF</div>
          <h4>Big-Ticket Items</h4>
          <p>40% off camps, mobile petting zoos &amp; field trips all year.</p>
        </div>
      </div>
    </div>

    <div>
      <div class="sec-head">
        <h3>Real Example Savings · Your Price vs. List</h3>
        <span>Nov 27 – Dec 1, 2026</span>
      </div>
      <div class="deals-grid" >
        <div class="deal featured">
          <div>
            <div class="dk">Option A · Gold Only</div>
            <h4>Critter Gold Membership</h4>
            <p class="desc">Free 2-person farm tour, free farm gift or thrifty toy, prototype app access, and 40% off camps, mobile zoos &amp; field trips.</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$1</strong></span>
            <span class="ys">You save $48.99</span>
            <div class="lst">Regularly $49.99/year</div>
          </div>
        </div>
        <div class="deal featured">
          <div>
            <div class="dk">Option B · Hero Bundle</div>
            <h4>$1 Gold + $50 Gift Card (50% Off)</h4>
            <p class="desc">Everything in Gold plus $50 credit toward farm visits, Mommy &amp; Me, homeschool mornings, or a 2027 party.</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$26</strong></span>
            <span class="ys">You save $73.99</span>
            <div class="lst">Combined list value $99.99</div>
          </div>
        </div>
        <div class="deal">
          <div>
            <div class="dk">Big-Ticket Savings Example</div>
            <h4>Standard Weekend Mobile Zoo</h4>
            <p class="desc">90-minute backyard party with at least 9 animals. Gold cuts 40% off big-ticket service rates.</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$329.40</strong></span>
            <span class="ys">You save $219.60</span>
            <div class="lst">List price $549 (+ travel from Callahan)</div>
          </div>
        </div>
        <div class="deal">
          <div>
            <div class="dk">Christmas Stocking Stuffer</div>
            <h4>$50 Gift Card Alone (50% Off)</h4>
            <p class="desc">Use for a Whole-Car Farm Visit ($50 list, up to 5 guests) or two $25 Mommy &amp; Me mornings.</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$25</strong></span>
            <span class="ys">You save $25</span>
            <div class="lst">Face value $50 · Never expires</div>
          </div>
        </div>
      </div>
    </div>

    <div class="proof-bar">
      <span class="chip">100+ Google reviews</span>
      <span class="chip">Almost 10,000 Facebook followers</span>
      <span class="chip">At least 8 farm animals</span>
      <span class="chip light">Claim gifts in person · Callahan, FL</span>
    </div>

    <div class="bookrow">
      <div class="qr-wrap">
        <div class="scan-shout">Scan for Gold</div>
        <a class="qr-frame" href="https://code4crittersoncallapps.github.io/gold/" target="_blank" rel="noopener">
          <img src="assets/qr-gold.png" alt="QR code to Critter Gold web app">
        </a>
        <div class="qr-cap">code4crittersoncallapps.github.io<br>/gold/</div>
      </div>
      <div class="cta-copy">
        <h3>Lock your $1 Gold &amp; Black Friday Gift Card (Nov 27 – Dec 1)</h3>
        <p>Open the Gold prototype app right now, or reserve the Black Friday $50 Gift Card at 50% off online. Prefer a real human? Call or text <strong>GOAT</strong> to <strong>914-263-1311</strong> and we will set up your gift card or membership today.</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="https://code4crittersoncallapps.github.io/gold/" target="_blank" rel="noopener">Open Gold App →</a>
          <a class="btn btn-gold" href="https://code4crittersoncallapps.github.io/critters-on-call/book/?product=gift-card-deal" target="_blank" rel="noopener">Claim $25 Gift Card ($50 Value) →</a>
        </div>
        <div class="fine-note">Gifts and farm tours are redeemed in person by appointment in Callahan, FL (not mailed). Offer valid Nov 27 – Dec 1, 2026. Travel on mobile visits is quoted from Callahan before booking.</div>
      </div>
    </div>
  </div>
  {FOOTER_HTML}
"""

# ---------------------------------------------------------------------------
# 2. B2C MULTI-OPTION #1: CHRISTMAS EXPERIENCE GIFTS
# ---------------------------------------------------------------------------
flyer_xmas_body = f"""
  <div class="why">
    <div class="kicker">Christmas Experience Gifts · Nov 27 – Dec 1, 2026</div>
    <div class="headline">Give Farm Memories, Not Clutter</div>
  </div>
  <div class="event">
    Black Friday &amp; Cyber Week <span class="gold">·</span> Gold $1 <span class="gold">·</span> 50% Off Gift Cards <span class="gold">·</span> Farm Visits &amp; Mommy &amp; Me
  </div>
  <div class="main">
    <div class="photos-2">
      <div class="photo-card">
        <img src="assets/kids-wagon.jpg" alt="Mommy and little girl meeting a silkie chicken and bunny in a red wagon" style="object-position:center 22%;">
        <div class="cap">Gentle farm mornings · Mommy &amp; Me &amp; Whole-Car Visits</div>
      </div>
      <div class="photo-card">
        <img src="assets/kids-pen.jpg" alt="Smiling kids petting bunnies and chicks at Critters on Call" style="object-position:center 35%;">
        <div class="cap">At least 8 friendly animals to meet, feed &amp; learn about</div>
      </div>
    </div>

    <div>
      <div class="sec-head">
        <h3>Pick Your Christmas Gift · Black Friday Pricing</h3>
        <span>Valid Nov 27 – Dec 1, 2026</span>
      </div>
      <div class="deals-grid" >
        <div class="deal featured">
          <div>
            <div class="dk">Best Stocking Stuffer</div>
            <h4>Critter Gold Membership</h4>
            <p class="desc">Free 2-person farm tour ($25 value), free farm gift or thrifty toy, prototype app access, and 40% off camps, mobile zoos &amp; field trips all year.</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$1</strong></span>
            <span class="ys">You save $48.99</span>
            <div class="lst">List price $49.99/yr</div>
          </div>
        </div>
        <div class="deal featured">
          <div>
            <div class="dk">Half-Off Gift Certificate</div>
            <h4>$50 Homestead Gift Card</h4>
            <p class="desc">Put $50 in family farm fun under the tree for half price. Good toward farm visits, Mommy &amp; Me, homeschool mornings, or parties.</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$25</strong></span>
            <span class="ys">You save $25</span>
            <div class="lst">$50 face value · 50% off</div>
          </div>
        </div>
        <div class="deal">
          <div>
            <div class="dk">Family Outing · Callahan, FL</div>
            <h4>Whole-Car Farm Visit (Up to 5)</h4>
            <p class="desc">60-minute guided visit for the whole family carload. Meet goats, bunnies, chickens &amp; friends. Pair with a half-off $50 gift card!</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$25</strong></span>
            <span class="ys">You save $25</span>
            <div class="lst">$50 list · Funded with $25 gift card</div>
          </div>
        </div>
        <div class="deal">
          <div>
            <div class="dk">Toddlers &amp; Littles (Ages 0–5)</div>
            <h4>Two Mommy &amp; Me Mornings</h4>
            <p class="desc">Calm 1-hour farm mornings (Thu &amp; select Sat, 10 AM) for 1 adult + under-5s. Use one half-off $50 gift card to cover two $25 mornings!</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$25</strong></span>
            <span class="ys">You save $25</span>
            <div class="lst">$50 list ($25/session × 2)</div>
          </div>
        </div>
        <div class="deal">
          <div>
            <div class="dk">Hero Bundle · Most Popular Gift</div>
            <h4>Gold ($1) + $50 Gift Card ($25)</h4>
            <p class="desc">Give them Gold perks + a free tour + a free gift + $50 to spend on any 2027 farm day or backyard party.</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$26</strong></span>
            <span class="ys">You save $73.99</span>
            <div class="lst">Combined list value $99.99</div>
          </div>
        </div>
        <div class="deal">
          <div>
            <div class="dk">2027 Birthday Lock-In</div>
            <h4>Standard Backyard Mobile Zoo</h4>
            <p class="desc">90-minute weekend party with at least 9 animals brought to your yard. Gold ($1) unlocks 40% off big-ticket bookings.</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$329.40</strong></span>
            <span class="ys">You save $219.60</span>
            <div class="lst">$549 weekend list (+ travel from Callahan)</div>
          </div>
        </div>
      </div>
    </div>

    <div class="proof-bar">
      <span class="chip">100+ Google reviews</span>
      <span class="chip">Almost 10,000 Facebook followers</span>
      <span class="chip">Family-run in Callahan, FL</span>
    </div>

    <div class="bookrow">
      <div class="qr-wrap">
        <div class="scan-shout">Scan to Claim</div>
        <a class="qr-frame" href="https://code4crittersoncallapps.github.io/critters-on-call/book/?product=gift-card-deal" target="_blank" rel="noopener">
          <img src="assets/qr-gift-card.png" alt="QR code to claim Black Friday $50 Gift Card for $25">
        </a>
        <div class="qr-cap">code4crittersoncallapps.github.io<br>/critters-on-call/book/</div>
      </div>
      <div class="cta-copy">
        <h3>Wrap up a Christmas gift they will talk about all year</h3>
        <p>Grab the 50%-off $50 gift card, unlock Gold for $1, or pick a farm date now. Text <strong>GOAT</strong> to <strong>914-263-1311</strong> and Michael or Ann-Marie will send your digital certificate right away.</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="https://code4crittersoncallapps.github.io/critters-on-call/book/?product=gift-card-deal" target="_blank" rel="noopener">Claim $25 Gift Card ($50 Value) →</a>
          <a class="btn btn-gold" href="https://code4crittersoncallapps.github.io/gold/" target="_blank" rel="noopener">Get $1 Gold App →</a>
        </div>
        <div class="fine-note">Farm tours &amp; Gold physical gifts are claimed in person by appointment in Callahan, FL. Offer window: Nov 27 – Dec 1, 2026.</div>
      </div>
    </div>
  </div>
  {FOOTER_HTML}
"""

# ---------------------------------------------------------------------------
# 3. B2C MULTI-OPTION #2: PARTIES, MOBILE ZOO & GOAT YOGA
# ---------------------------------------------------------------------------
flyer_parties_body = f"""
  <div class="why">
    <div class="kicker">Black Friday – Cyber Monday · Nov 27 – Dec 1, 2026</div>
    <div class="headline">Backyard Zoos &amp; Goat Yoga</div>
  </div>
  <div class="event">
    Unlock 40% Off Big-Ticket Mobile Zoos With $1 Gold <span class="gold">·</span> Plus Half-Off $50 Gift Cards
  </div>
  <div class="main">
    <div class="photos-2">
      <div class="photo-card">
        <img src="assets/community-event.jpg" alt="Critters on Call mobile petting zoo tent with bunnies and goats" style="object-position:center 35%;">
        <div class="cap">We bring the fence, tent, helpers &amp; at least 6 to 9 animals</div>
      </div>
      <div class="photo-card">
        <img src="assets/goat-yoga.jpg" alt="Outdoor goat yoga class with baby goats" style="object-position:center 40%;">
        <div class="cap">Private Group Goat Yoga &amp; Goats &amp; Mimosas</div>
      </div>
    </div>

    <div>
      <div class="sec-head">
        <h3>2027 Birthday Parties, Bunny Visits &amp; Goat Yoga</h3>
        <span>With $1 Gold (40% off) · Nov 27 – Dec 1</span>
      </div>
      <div class="deals-grid" >
        <div class="deal">
          <div>
            <div class="dk">Quiet &amp; Gentle · 60 Minutes</div>
            <h4>Bunny Haven Mobile Visit</h4>
            <p class="desc">Bunnies &amp; gentle friends brought to your home. Great for toddlers, sensory-friendly birthdays &amp; smaller yards.</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$90</strong> wkdy / <strong>$141</strong> wknd</span>
            <span class="ys">Save $60–$94</span>
            <div class="lst">List: $150 weekday / $235 weekend (40% off w/ Gold)</div>
          </div>
        </div>
        <div class="deal">
          <div>
            <div class="dk">Popular Backyard Choice · 75 Min</div>
            <h4>Mini Petting Zoo (At Least 6 Animals)</h4>
            <p class="desc">Goats, bunnies &amp; fowl in a neat backyard setup with our team guiding every interaction.</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$179.40</strong> wkdy / <strong>$215.40</strong> wknd</span>
            <span class="ys">Save $119.60–$143.60</span>
            <div class="lst">List: $299 weekday / $359 weekend (40% off w/ Gold)</div>
          </div>
        </div>
        <div class="deal featured">
          <div>
            <div class="dk">Signature Birthday · 90 Minutes</div>
            <h4>Standard Petting Zoo (At Least 9 Animals)</h4>
            <p class="desc">Full backyard petting zoo with goats, bunnies, chickens &amp; friends. Setup, supervision &amp; cleanup handled.</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$215.40</strong> wkdy / <strong>$329.40</strong> wknd</span>
            <span class="ys">Save $143.60–$219.60</span>
            <div class="lst">List: $359 weekday / $549 weekend (40% off w/ Gold)</div>
          </div>
        </div>
        <div class="deal">
          <div>
            <div class="dk">Grown-Up Gift · Group Event (Up to 20)</div>
            <h4>Private Goat Yoga / Goats &amp; Mimosas</h4>
            <p class="desc">60-minute flow with a certified instructor &amp; playful goats at your lawn or clubhouse. Goats &amp; Mimosas includes our mobile bartender.</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$599.25</strong> / <strong>$974.25</strong></span>
            <span class="ys">Save $199.75–$324.75</span>
            <div class="lst">25% off list ($799 Goat Yoga / $1,299 Goats &amp; Mimosas)</div>
          </div>
        </div>
        <div class="deal featured">
          <div>
            <div class="dk">Gift Now, Pick Date Later</div>
            <h4>$1 Gold + $50 Gift Card ($25)</h4>
            <p class="desc">Not sure of the 2027 party date yet? Lock Gold for $1 (40% off mobile) plus a $50 gift card for $25 to put under the tree.</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$26</strong></span>
            <span class="ys">You save $73.99</span>
            <div class="lst">List $99.99 · Includes free farm tour + gift</div>
          </div>
        </div>
        <div class="deal">
          <div>
            <div class="dk">On the Farm · Christmas Morning</div>
            <h4>Whole-Car Farm Visit (Up to 5)</h4>
            <p class="desc">Prefer to come to us in Callahan? Grab a half-off $50 gift card ($25) for a private 60-min family farm visit.</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$25</strong></span>
            <span class="ys">You save $25</span>
            <div class="lst">$50 list · Meet at least 8 animals</div>
          </div>
        </div>
      </div>
    </div>

    <div class="proof-bar">
      <span class="chip">100+ Google reviews</span>
      <span class="chip">Almost 10,000 Facebook followers</span>
      <span class="chip light">Step Up LIVE eligible families welcome</span>
    </div>

    <div class="bookrow">
      <div class="qr-wrap">
        <div class="scan-shout">Scan to Reserve</div>
        <a class="qr-frame" href="https://code4crittersoncallapps.github.io/critters-on-call/book/?product=birthday-party" target="_blank" rel="noopener">
          <img src="assets/qr-birthday.png" alt="QR code to reserve a birthday petting zoo or gift card">
        </a>
        <div class="qr-cap">code4crittersoncallapps.github.io<br>/critters-on-call/book/</div>
      </div>
      <div class="cta-copy">
        <h3>Gift a 2027 party or Goat Yoga session before peak dates fill</h3>
        <p>Join Gold for <strong>$1</strong> (Nov 27 – Dec 1) to lock 40% off big-ticket mobile zoos, or reserve a date hold right now. Call or text <strong>GOAT</strong> to <strong>914-263-1311</strong> for a travel quote from Callahan.</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="https://code4crittersoncallapps.github.io/critters-on-call/book/?product=birthday-party" target="_blank" rel="noopener">Book Party / Hold Date →</a>
          <a class="btn btn-gold" href="https://code4crittersoncallapps.github.io/gold/" target="_blank" rel="noopener">Unlock $1 Gold First →</a>
        </div>
        <div class="fine-note">Travel from Callahan, FL is quoted separately before you book (50% off travel with standard Gold). Free weather reschedules with 48 hrs' notice.</div>
      </div>
    </div>
  </div>
  {FOOTER_HTML}
"""

# ---------------------------------------------------------------------------
# 4. HOMESCHOOL-ONLY #1: HOMESCHOOL FARM & STEM + WINTER BREAK
# ---------------------------------------------------------------------------
flyer_hs_body = f"""
  <div class="why">
    <div class="kicker">Homeschool Black Friday – Cyber Monday · Nov 27 – Dec 1, 2026</div>
    <div class="headline">Homeschool Farm &amp; STEM</div>
  </div>
  <div class="event">
    Hands-On Science on the Farm <span class="gold">·</span> Led by Ann-Marie Sheehan, M.Ed. <span class="gold">·</span> Step Up Welcome
  </div>
  <div class="main">
    <div class="hero-strip">
      <div class="hero-box">
        <span class="tag">Christmas Gift for Homeschoolers</span>
        <h2>Real Animals, Real Science &amp; <em>$1 Gold</em></h2>
        <p>Give your homeschooler mornings outdoors with <strong>at least 8 farm animals</strong> and hands-on STEM led by a former teacher (M.Ed. in STEM Education Leadership). Unlock <strong>Critter Gold for $1</strong> (Nov 27 – Dec 1) to get a free farm tour, free farm gift, prototype app lessons, and <strong>40% off camps &amp; field trips</strong>.</p>
        <div class="hero-price-line">
          <span class="yp-lab">Gold price</span>
          <span class="yp-val">$1</span>
          <span class="yp-was"><s>$49.99</s></span>
          <span class="yp-save">You save $48.99</span>
        </div>
      </div>
      <div class="photo-card">
        <img src="assets/farm-field.jpg" alt="Oak-shaded pasture at Sheehan Homestead in Callahan, FL" style="object-position:center 55%;">
        <div class="cap">Sheehan Homestead · 44065 Cushman Rd, Callahan, FL</div>
      </div>
    </div>

    <div>
      <div class="sec-head">
        <h3>Homeschool Gift Options · Your Price / You Save</h3>
        <span>Black Friday – Cyber Monday (Nov 27 – Dec 1)</span>
      </div>
      <div class="deals-grid" >
        <div class="deal featured">
          <div>
            <div class="dk">Winter Break &amp; Black Friday Mornings</div>
            <h4>Farm &amp; STEM Camp Morning (90 Min)</h4>
            <p class="desc">10:00–11:30 AM. Guided animal encounters + harvest/winter STEM activity. Black Friday (Nov 27) &amp; Winter Break (Dec 21–23, Dec 28–30 proposed).</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$24</strong>/child</span>
            <span class="ys">You save $16 (40% off w/ Gold)</span>
            <div class="lst">List price $40/child · Small groups, limited spots</div>
          </div>
        </div>
        <div class="deal featured">
          <div>
            <div class="dk">Weekly Homeschool Days · Callahan</div>
            <h4>$50 Gift Card at 50% Off ($25)</h4>
            <p class="desc">Apply toward scheduled 90-min Homeschool Farm &amp; STEM mornings ($40/ticket, Mon/Tue/Wed) — covers a full morning plus $10 credit left over!</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$25</strong></span>
            <span class="ys">You save $25</span>
            <div class="lst">$50 gift card face value · Use any 2026–27 morning</div>
          </div>
        </div>
        <div class="deal">
          <div>
            <div class="dk">First Family Visit · Up to 5 Guests</div>
            <h4>Whole-Car Farm Visit (60 Min)</h4>
            <p class="desc">Bring the whole homeschool family to meet goats, bunnies &amp; chickens. Pair with a half-off $50 gift card for 50% off.</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$25</strong></span>
            <span class="ys">You save $25</span>
            <div class="lst">$50 list · Funded with $25 gift card</div>
          </div>
        </div>
        <div class="deal">
          <div>
            <div class="dk">Free With $1 Gold Membership</div>
            <h4>2-Person Farm Tour + Farm Gift + App</h4>
            <p class="desc">Walk the farm ($25 value), take home a free farm gift or thrifty toy (up to $25 value), and play farm lessons &amp; games in the Gold web app.</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$1</strong></span>
            <span class="ys">You save $48.99</span>
            <div class="lst">$49.99 Gold list · Normally $50+ in day-one gifts</div>
          </div>
        </div>
      </div>
    </div>

    <div class="proof-bar">
      <span class="chip">Step Up for Students welcome</span>
      <span class="chip">100+ Google reviews</span>
      <span class="chip">Almost 10,000 Facebook followers</span>
      <span class="chip light">At least 8 animals on farm</span>
    </div>

    <div class="bookrow">
      <div class="qr-wrap">
        <div class="scan-shout">Scan to Book</div>
        <a class="qr-frame" href="https://code4crittersoncallapps.github.io/critters-on-call/book/?product=homeschool-mon-10" target="_blank" rel="noopener">
          <img src="assets/qr-homeschool.png" alt="QR code to book Homeschool Farm and STEM">
        </a>
        <div class="qr-cap">code4crittersoncallapps.github.io<br>/critters-on-call/book/</div>
      </div>
      <div class="cta-copy">
        <h3>Plan your winter &amp; spring homeschool mornings now</h3>
        <p>Parents stay with kids on the farm. Ask us about Step Up reimbursement paths, co-op group dates, or gift cards. Text <strong>GOAT</strong> to <strong>914-263-1311</strong>.</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="https://code4crittersoncallapps.github.io/critters-on-call/book/?product=homeschool-mon-10" target="_blank" rel="noopener">Book Homeschool Morning →</a>
          <a class="btn btn-gold" href="https://code4crittersoncallapps.github.io/gold/" target="_blank" rel="noopener">Claim $1 Gold Membership →</a>
        </div>
        <div class="fine-note">Scheduled homeschool mornings are $40 list (90 min). Winter break Dec 21–23 &amp; Dec 28–30 morning dates are proposed; confirm times when booking. Offer valid Nov 27 – Dec 1, 2026.</div>
      </div>
    </div>
  </div>
  {FOOTER_HTML}
"""

# ---------------------------------------------------------------------------
# 5. HOMESCHOOL-ONLY #2: CO-OP FIELD TRIPS & STEM ON CALL
# ---------------------------------------------------------------------------
flyer_coop_body = f"""
  <div class="why">
    <div class="kicker">Homeschool Co-Ops &amp; Groups · Nov 27 – Dec 1, 2026</div>
    <div class="headline">Co-Op Field Trips &amp; STEM</div>
  </div>
  <div class="event">
    Come to Our Farm (40% Off w/ $1 Gold) <span class="gold">·</span> Or We Come to Your Co-Op (Violet 50% Off)
  </div>
  <div class="main">
    <div class="photos-2">
      <div class="photo-card">
        <img src="assets/goat-herd.jpg" alt="Goats grazing on green grass at Sheehan Homestead" style="object-position:center 45%;">
        <div class="cap">Private co-op field trips in Callahan · planned parking &amp; lesson</div>
      </div>
      <div class="photo-card">
        <img src="assets/site-8.jpg" alt="Friendly bunnies in tunnel on green grass" style="object-position:center 45%;">
        <div class="cap">Mobile STEM on Call &amp; petting zoos brought straight to your co-op</div>
      </div>
    </div>

    <div>
      <div class="sec-head">
        <h3>Co-Op &amp; Group Savings · Your Price / You Save</h3>
        <span>Black Friday – Cyber Monday Lock (Nov 27 – Dec 1)</span>
      </div>
      <div class="deals-grid" >
        <div class="deal featured">
          <div>
            <div class="dk">Come to the Farm · Small Group</div>
            <h4>Small Private Field Trip</h4>
            <p class="desc">75–90 min private visit &amp; STEM lesson for up to 5 cars or 20 guests. Meet at least 8 farm animals. Includes free Gold for organizer.</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$179.40</strong></span>
            <span class="ys">You save $119.60 (40% off w/ $1 Gold)</span>
            <div class="lst">List price $299</div>
          </div>
        </div>
        <div class="deal featured">
          <div>
            <div class="dk">Come to the Farm · Large Co-Op</div>
            <h4>Large Private Field Trip</h4>
            <p class="desc">~90 min private visit &amp; STEM lesson for up to 10 cars or 40 guests. Planned parking and custom age-fit science activity.</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$299.40</strong></span>
            <span class="ys">You save $199.60 (40% off w/ $1 Gold)</span>
            <div class="lst">List price $499</div>
          </div>
        </div>
        <div class="deal">
          <div>
            <div class="dk">We Come to Your Co-Op · Violet Rate</div>
            <h4>STEM on Call (1 Hour)</h4>
            <p class="desc">Hands-on farm science brought to your co-op, church, or learning pod (50% off services &amp; 75% off travel for qualifying groups).</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$184</strong></span>
            <span class="ys">You save $184</span>
            <div class="lst">$368 list (then $110/hr vs. $220/hr list)</div>
          </div>
        </div>
        <div class="deal">
          <div>
            <div class="dk">We Come to Your Co-Op · Violet Rate</div>
            <h4>Mobile Mini Petting Zoo (2 Hrs)</h4>
            <p class="desc">At least 6 animals (goats, bunnies &amp; fowl) brought to your co-op lawn, plus setup, fencing &amp; facilitator.</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$274.50</strong></span>
            <span class="ys">You save $274.50</span>
            <div class="lst">$549 list (50% off services · 75% off travel)</div>
          </div>
        </div>
        <div class="deal">
          <div>
            <div class="dk">We Come to Your Co-Op · Violet Rate</div>
            <h4>Mobile Standard Zoo (2 Hrs)</h4>
            <p class="desc">At least 9 animals + tent, fencing &amp; facilitator for bigger co-op field days and church homeschool groups.</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$374.50</strong></span>
            <span class="ys">You save $374.50</span>
            <div class="lst">$749 list (50% off services · 75% off travel)</div>
          </div>
        </div>
        <div class="deal">
          <div>
            <div class="dk">Christmas Gift for Co-Op Teachers</div>
            <h4>$1 Gold + $50 Gift Card ($25)</h4>
            <p class="desc">Thank a co-op leader or homeschool mom with a $1 Gold card (free farm tour + gift + app) and a $50 gift card for $25.</p>
          </div>
          <div class="pbox">
            <span class="yp">Your price:<strong>$26</strong></span>
            <span class="ys">You save $73.99</span>
            <div class="lst">Combined value $99.99</div>
          </div>
        </div>
      </div>
    </div>

    <div class="proof-bar">
      <span class="chip">Led by Ann-Marie Sheehan, M.Ed.</span>
      <span class="chip">100+ Google reviews</span>
      <span class="chip">Almost 10,000 Facebook followers</span>
    </div>

    <div class="bookrow">
      <div class="qr-wrap">
        <div class="scan-shout">Scan to Hold</div>
        <a class="qr-frame" href="https://code4crittersoncallapps.github.io/critters-on-call/book/?product=field-trip-small" target="_blank" rel="noopener">
          <img src="assets/qr-field-trip.png" alt="QR code to book a Homeschool Co-Op Field Trip">
        </a>
        <div class="qr-cap">code4crittersoncallapps.github.io<br>/critters-on-call/book/</div>
      </div>
      <div class="cta-copy">
        <h3>Lock your co-op's winter or spring 2027 date early</h3>
        <p>Join Gold for <strong>$1</strong> (Nov 27 – Dec 1) to lock 40% off farm field trips, or request our Violet co-op rate when we come to you. Text <strong>GOAT</strong> to <strong>914-263-1311</strong> with your group size.</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="https://code4crittersoncallapps.github.io/critters-on-call/book/?product=field-trip-small" target="_blank" rel="noopener">Book Co-Op Field Trip →</a>
          <a class="btn btn-gold" href="https://code4crittersoncallapps.github.io/gold/" target="_blank" rel="noopener">Get $1 Gold Membership →</a>
        </div>
        <div class="fine-note">Violet rate is our partial-donation rate for co-ops, schools &amp; nonprofits (doesn't stack with Gold; we apply the better discount). Travel quoted from Callahan.</div>
      </div>
    </div>
  </div>
  {FOOTER_HTML}
"""

PAGES = [
    ("black-friday-gold", "Critter Gold $1 + Black Friday Gift Card · Sheehan Homestead", "Black Friday Gold Membership ($1 vs $49.99) + $50 Gift Card at 50% Off ($25). Nov 27 - Dec 1, 2026.", flyer_gold_body),
    ("christmas-experience-gifts", "Christmas Experience Gifts · Black Friday & Cyber Week · Sheehan Homestead", "Give farm memories instead of clutter: $1 Gold, 50% off $50 gift cards, farm visits, Mommy & Me. Nov 27 - Dec 1, 2026.", flyer_xmas_body),
    ("mobile-zoo-goat-yoga-gifts", "Backyard Parties, Mobile Zoo & Goat Yoga Gifts · Black Friday · Sheehan Homestead", "Black Friday & Cyber Week savings on Bunny Haven, Mini & Standard Mobile Zoos, and Private Goat Yoga. Nov 27 - Dec 1, 2026.", flyer_parties_body),
    ("homeschool-black-friday", "Homeschool Farm & STEM · Black Friday & Winter Break · Sheehan Homestead", "Homeschool Black Friday & Cyber Week: $1 Gold, $24 Winter Break Farm & STEM mornings, half-off gift cards. Nov 27 - Dec 1, 2026.", flyer_hs_body),
    ("homeschool-coop-field-trips", "Homeschool Co-Op Field Trips & STEM on Call · Black Friday · Sheehan Homestead", "Co-op field trips on the farm (40% off w/ $1 Gold) or STEM & petting zoos at your co-op (Violet 50% off). Nov 27 - Dec 1, 2026.", flyer_coop_body),
]

def make_index():
    cards = []
    for slug, title, desc, _ in PAGES:
        cards.append(f"""
        <div class="card">
          <h3>{title.split('·')[0].strip()}</h3>
          <p>{desc}</p>
          <div class="links">
            <a class="btn btn-primary" href="{slug}.html?v=1124h">Open Flyer</a>
            <a class="btn btn-gold" href="{slug}.pdf?v=1124h">Direct PDF</a>
            <a class="btn btn-outline" href="png/{slug}.png?v=1124h">Facebook PNG</a>
          </div>
        </div>""")
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Black Friday &amp; Cyber Week 2026 Flyers · Sheehan Homestead</title>
<link rel="icon" type="image/png" href="assets/sophie-logo.png">
<style>
@font-face {{ font-family: "Playfair Display"; src: url("assets/PlayfairDisplay-Variable.ttf") format("truetype"); font-weight: 400 900; }}
@font-face {{ font-family: "Source Sans 3"; src: url("assets/SourceSans3-Variable.ttf") format("truetype"); font-weight: 200 900; }}
:root {{ --forest:#3A4F45; --gold:#c9a227; --cream:#F3EEE4; --ink:#1a241c; }}
* {{ box-sizing: border-box; margin:0; padding:0; }}
body {{ background: var(--cream); color: var(--ink); font-family: "Source Sans 3", sans-serif; line-height:1.45; }}
header {{ background: var(--forest); color:#fff; border-bottom:4px solid var(--gold); padding:22px 20px; text-align:center; }}
header img {{ width:64px; height:64px; border-radius:50%; border:2px solid var(--gold); margin-bottom:8px; }}
header h1 {{ font-family:"Playfair Display",serif; font-size:28px; color:#E8D48C; }}
header p {{ font-size:15px; opacity:.9; margin-top:4px; }}
main {{ max-width:900px; margin:24px auto; padding:0 16px 40px; display:grid; gap:14px; }}
.card {{ background:#fff; border:1.5px solid rgba(58,79,69,.2); border-top:4px solid var(--gold); border-radius:10px; padding:16px 18px; }}
.card h3 {{ font-family:"Playfair Display",serif; color:var(--forest); font-size:20px; }}
.card p {{ font-size:14.5px; color:#445249; margin:6px 0 12px; }}
.links {{ display:flex; flex-wrap:wrap; gap:8px; }}
.btn {{ text-decoration:none; font-weight:700; font-size:13.5px; padding:7px 13px; border-radius:6px; display:inline-block; }}
.btn-primary {{ background:var(--forest); color:#E8D48C; border:1px solid var(--gold); }}
.btn-gold {{ background:var(--gold); color:var(--forest); }}
.btn-outline {{ background:#fff; color:var(--forest); border:1px solid var(--forest); }}
</style>
</head>
<body>
<header>
  <img src="assets/sophie-logo.png" alt="Sophie logo">
  <h1>Black Friday &amp; Cyber Week · Nov 27 – Dec 1, 2026</h1>
  <p>Sheehan Homestead · Critters on Call · Callahan, FL · 914-263-1311</p>
</header>
<main>
{''.join(cards)}
</main>
</body>
</html>"""
    with open(os.path.join(BASE_DIR, "index.html"), "w") as f:
        f.write(html)

def build_all():
    make_qrs()
    make_index()
    detector = cv2.QRCodeDetector()
    for slug, title, desc, body in PAGES:
        html_path = os.path.join(BASE_DIR, f"{slug}.html")
        pdf_path = os.path.join(BASE_DIR, f"{slug}.pdf")
        png_prefix = os.path.join(PNG_DIR, slug)
        png_path = os.path.join(PNG_DIR, f"{slug}.png")

        with open(html_path, "w") as f:
            f.write(wrap_page(title, desc, body))

        subprocess.run([
            "google-chrome",
            "--headless=new",
            "--no-sandbox",
            "--disable-gpu",
            "--no-pdf-header-footer",
            "--virtual-time-budget=6000",
            f"--print-to-pdf={pdf_path}",
            "file://" + os.path.abspath(html_path),
        ], check=True, capture_output=True)

        info = subprocess.run(["pdfinfo", pdf_path], check=True, capture_output=True, text=True).stdout
        pages_line = [l for l in info.splitlines() if l.startswith("Pages:")]
        page_count = pages_line[0].split(":")[1].strip() if pages_line else "?"
        size_line = [l for l in info.splitlines() if l.startswith("Page size:")]
        print(f"PDF {slug}.pdf -> Pages: {page_count} | {size_line[0] if size_line else ''}")
        assert page_count == "1", f"{slug}.pdf spilled onto {page_count} pages!"

        subprocess.run([
            "pdftoppm", "-r", "180", "-png", "-singlefile", pdf_path, png_prefix
        ], check=True, capture_output=True)

        # Verify QR inside rendered PNG is decodable (crop bottom-left QR zone)
        mat = cv2.imread(png_path)
        h, w = mat.shape[:2]
        roi = mat[int(h*0.65):int(h*0.95), 0:int(w*0.40)]
        roi2 = cv2.resize(roi, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
        decoded, _, _ = detector.detectAndDecode(roi2)
        if not decoded:
            decoded, _, _ = detector.detectAndDecode(mat)
        print(f"PNG {slug}.png -> {w}x{h} | QR decoded in flyer: {decoded!r}")
        assert decoded, f"Could not decode QR inside rendered flyer {png_path}!"

if __name__ == "__main__":
    build_all()
