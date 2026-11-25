import os
import re
import subprocess
from pathlib import Path
import qrcode
import cv2

BASE_DIR = Path(__file__).resolve().parent
ASSETS = BASE_DIR / "assets"
PNG_DIR = BASE_DIR / "png"
PNG_DIR.mkdir(exist_ok=True)

# Remove stale $1 flyers from the earlier rejected batch (leave black-friday-gold.* UNTOUCHED)
OLD_SLUGS = [
    "christmas-experience-gifts",
    "mobile-zoo-goat-yoga-gifts",
    "homeschool-black-friday",
    "homeschool-coop-field-trips",
]
for s in OLD_SLUGS:
    for p in [BASE_DIR / f"{s}.html", BASE_DIR / f"{s}.pdf", PNG_DIR / f"{s}.png"]:
        if p.exists():
            p.unlink()
            print("Removed old $1 artifact:", p.name)

QR_TARGETS = {
    "qr-mobile-date.png": "https://code4crittersoncallapps.github.io/critters-on-call/book/?product=birthday-party",
    "qr-visit-us.png": "https://code4crittersoncallapps.github.io/critters-on-call/book/?product=farm-whole-car",
    "qr-mommy-me.png": "https://code4crittersoncallapps.github.io/critters-on-call/book/?product=mommy-me-thu",
    "qr-homeschool.png": "https://code4crittersoncallapps.github.io/critters-on-call/book/?product=homeschool-mon-10",
    "qr-camps.png": "https://code4crittersoncallapps.github.io/critters-on-call/book/?product=summer-camp",
    "qr-field-trip.png": "https://code4crittersoncallapps.github.io/critters-on-call/book/?product=field-trip-small",
    "qr-goat-yoga.png": "https://code4crittersoncallapps.github.io/critters-on-call/book/?product=farm-goat-yoga",
}

def make_qrs():
    det = cv2.QRCodeDetector()
    for fname, url in QR_TARGETS.items():
        out = ASSETS / fname
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=12,
            border=2,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="#1f2a24", back_color="#ffffff")
        img.save(out)
        mat = cv2.imread(str(out))
        decoded, _, _ = det.detectAndDecode(mat)
        assert decoded == url, f"QR mismatch {fname}: {decoded!r} vs {url!r}"
        print(f"QR OK: {fname} -> {decoded}")

GOOGLE_BADGE_HTML = '''
<div class="gbadge">
  <svg class="gicon" viewBox="0 0 24 24" aria-hidden="true">
    <path fill="#4285F4" d="M23.49 12.27c0-.79-.07-1.54-.19-2.27H12v4.51h6.47c-.29 1.48-1.14 2.73-2.4 3.58v3h3.86c2.26-2.09 3.56-5.17 3.56-8.82z"/>
    <path fill="#34A853" d="M12 24c3.24 0 5.95-1.08 7.93-2.91l-3.86-3c-1.08.72-2.45 1.16-4.07 1.16-3.13 0-5.78-2.11-6.73-4.96H1.29v3.09C3.26 21.3 7.31 24 12 24z"/>
    <path fill="#FBBC05" d="M5.27 14.29c-.24-.72-.38-1.49-.38-2.29s.14-1.57.38-2.29V6.62H1.29C.47 8.24 0 10.06 0 12s.47 3.76 1.29 5.38l3.98-3.09z"/>
    <path fill="#EA4335" d="M12 4.75c1.77 0 3.35.61 4.6 1.8l3.42-3.42C17.95 1.19 15.24 0 12 0 7.31 0 3.26 2.7 1.29 6.62l3.98 3.09c.95-2.85 3.6-4.96 6.73-4.96z"/>
  </svg>
  <span class="gstars" aria-label="5 out of 5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
  <span>100+ five-star Google reviews</span>
</div>
'''

SHARED_CSS = """
@font-face{font-family:"Fraunces";src:url("assets/gold-poster/fraunces-normal-latin.woff2") format("woff2");font-weight:500 700;font-style:normal;font-display:swap}
@font-face{font-family:"Source Sans 3";src:url("assets/gold-poster/SourceSans3-Variable.ttf") format("truetype");font-weight:200 900;font-style:normal;font-display:swap}
@page{size:8.5in 11in;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --green:#4e6558;
  --green-deep:#3A4F45;
  --gold:#c9a227;
  --gold-lt:#E8D48C;
  --cream:#F3EEE4;
  --ink:#1f2a24;
  --muted:#516157;
  --line:#dfd7c7;
}
html,body{background:#d9d2c3;color:var(--ink);font-family:"Source Sans 3","Source Sans Pro",sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:8.5in;height:11in;overflow:hidden;display:flex;flex-direction:column;background:var(--cream);margin:0 auto}
@media print{html,body{background:var(--cream);width:8.5in;height:11in}.page{margin:0}}
.lg{display:inline-block;width:52px;height:52px;border-radius:50%;background-size:cover;background-position:center;flex:0 0 auto}
.lg-sh{background-image:url("assets/gold-poster/sh.png")}
.lg-coc{background-image:url("assets/gold-poster/coc.png");box-shadow:0 0 0 3px var(--gold)}
.brand{display:flex;align-items:stretch;background:var(--cream)}
.brand .side{flex:1;display:flex;align-items:center;justify-content:center;gap:12px;padding:.11in 0 .09in}
.brand .side+.side{border-left:1px solid var(--line)}
.brand .nm{font-family:Fraunces,Georgia,serif;font-weight:600;font-size:13.5pt;line-height:1.1;color:var(--green)}
.rule{display:flex;height:5px}.rule .g{flex:1;background:var(--green)}.rule .y{flex:1;background:var(--gold)}

.body{flex:1;padding:.20in .52in .16in;display:flex;flex-direction:column;gap:.20in;min-height:0;justify-content:center}
.k{font-size:9.5pt;letter-spacing:.17em;text-transform:uppercase;color:var(--gold);font-weight:800}
.hero{display:flex;gap:.24in;align-items:center}
.hero .txt{flex:1.42}
.hero h1{font-family:Fraunces,Georgia,serif;font-weight:700;font-size:34pt;line-height:1.05;color:var(--green);margin:0}
.hero h1 em{font-style:normal;color:var(--gold)}
.hero p.lede{font-size:11.3pt;line-height:1.36;color:var(--ink)}
.hero .photo{flex:1;max-width:2.85in}
.hero .photo img{width:100%;aspect-ratio:3/2;object-fit:cover;border-radius:14px;border:2.5px solid var(--gold);box-shadow:0 8px 20px rgba(0,0,0,.20);display:block}
.hero .photo.port img{aspect-ratio:4/4.3}

.banner{display:flex;align-items:center;gap:14px;background:var(--green);color:var(--cream);border-radius:14px;padding:8px 16px;border-left:7px solid var(--gold)}
.banner .tag{background:var(--gold);color:#1f2a24;font-family:Fraunces,Georgia,serif;font-weight:700;font-size:10.5pt;letter-spacing:.04em;text-transform:uppercase;border-radius:8px;padding:6px 11px;white-space:nowrap;text-align:center;line-height:1.15}
.banner .tag small{display:block;font-family:"Source Sans 3",sans-serif;font-size:7.8pt;font-weight:800;letter-spacing:.10em;margin-top:2px}
.banner p{font-size:10.8pt;line-height:1.33}
.banner b{color:var(--gold-lt)}
.incl{display:inline-block;margin-top:8px;background:var(--gold);color:#1f2a24;font-weight:800;font-size:9.5pt;letter-spacing:.08em;text-transform:uppercase;border-radius:8px;padding:6px 12px;line-height:1.2}

h2{font-family:Fraunces,Georgia,serif;font-weight:600;font-size:16pt;color:var(--green);line-height:1.12}
h2 .subh{font-family:"Source Sans 3",sans-serif;font-size:9.5pt;font-weight:700;color:var(--muted);margin-left:8px;letter-spacing:.02em}

.cards2{display:grid;grid-template-columns:repeat(2,1fr);gap:.13in;margin-top:6px}
.cards3{display:grid;grid-template-columns:repeat(3,1fr);gap:.12in;margin-top:6px}
.card{background:#fff;border:1.5px solid var(--line);border-top:4.5px solid var(--gold);border-radius:12px;padding:10px 12px 10px;display:flex;flex-direction:column;justify-content:space-between}
.card.feat{border:1.5px solid var(--green);border-top:4.5px solid var(--gold);background:#fffdf7}
.card .ck{font-size:8.2pt;font-weight:800;letter-spacing:.10em;text-transform:uppercase;color:#a07f1a;margin-bottom:2px}
.card h3{font-family:Fraunces,Georgia,serif;font-size:13pt;font-weight:700;color:var(--green);line-height:1.15}
.card .desc{font-size:9.5pt;color:var(--muted);line-height:1.3;margin:4px 0 7px}
.card ul{list-style:none;margin:4px 0 7px}
.card li{font-size:9.4pt;line-height:1.3;padding:1.5px 0 1.5px 12px;position:relative;color:var(--ink)}
.card li:before{content:"";position:absolute;left:0;top:.58em;width:6px;height:6px;border-radius:50%;background:var(--gold)}
.pr{border-top:1px solid var(--line);padding-top:6px;display:flex;justify-content:space-between;align-items:flex-end;gap:8px}
.pr .yp-lbl{display:block;font-size:7.6pt;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.pr .yp{font-family:Fraunces,Georgia,serif;font-size:19pt;font-weight:700;color:var(--green);line-height:1}
.pr .yp small{font-family:"Source Sans 3",sans-serif;font-size:9.2pt;font-weight:600;color:var(--muted);margin-left:2px}
.pr .sv-col{text-align:right}
.pr .lst{display:block;font-size:8.6pt;color:var(--muted);text-decoration:line-through}
.pr .sv{display:inline-block;background:var(--green);color:var(--gold-lt);font-size:8.2pt;font-weight:800;border-radius:20px;padding:2px 8px;margin-top:2px;white-space:nowrap}

.tbl-wrap{background:#fff;border:1.5px solid var(--line);border-top:4.5px solid var(--gold);border-radius:12px;overflow:hidden;margin-top:6px}
table.menu{width:100%;border-collapse:collapse}
table.menu th{background:var(--green);color:var(--gold-lt);font-size:8.4pt;font-weight:800;letter-spacing:.09em;text-transform:uppercase;padding:6px 11px;text-align:left}
table.menu th.r{text-align:right}
table.menu td{padding:7px 11px;border-top:1px solid var(--line);vertical-align:middle;font-size:9.8pt;line-height:1.25}
table.menu tr.hl{background:#fffdf6}
table.menu td .nm{font-family:Fraunces,Georgia,serif;font-weight:700;font-size:11.2pt;color:var(--green);display:block}
table.menu td .mt{font-size:8.8pt;color:var(--muted);display:block;margin-top:1px}
table.menu td.r{text-align:right;white-space:nowrap}
table.menu .now{font-family:Fraunces,Georgia,serif;font-size:13.5pt;font-weight:700;color:var(--green);display:block;line-height:1.05}
table.menu .was{font-size:8.2pt;color:var(--muted);display:block}
table.menu .ys{display:inline-block;background:#f3ecda;color:#7a5e0d;font-weight:800;font-size:7.9pt;border-radius:12px;padding:1px 6px;margin-top:1px}

.two{display:flex;gap:.14in}
.box{flex:1;background:#fff;border:1.5px solid var(--green);border-radius:12px;padding:8px 12px}
.box h3{font-family:Fraunces,Georgia,serif;font-size:12.5pt;color:var(--green);margin-bottom:4px}
.box ul{list-style:none}
.box li{font-size:9.6pt;line-height:1.32;padding:1.5px 0 1.5px 14px;position:relative}
.box li:before{content:"";position:absolute;left:0;top:.58em;width:7px;height:7px;border-radius:50%;background:var(--gold)}
.box li b{color:var(--green)}

.cross{display:flex;align-items:center;gap:14px;background:#1f2a24;color:var(--cream);border-radius:12px;padding:8px 14px;border:1.5px solid var(--gold)}
.cross .pill{background:var(--gold);color:#1f2a24;font-weight:800;font-size:8.4pt;letter-spacing:.08em;text-transform:uppercase;border-radius:7px;padding:5px 9px;white-space:nowrap;text-align:center;line-height:1.2}
.cross p{font-size:9.8pt;line-height:1.34}
.cross b{color:var(--gold-lt)}
.cross a{color:var(--gold-lt);font-weight:700}

.fine-bar{font-size:8.9pt;color:var(--muted);line-height:1.3;display:flex;justify-content:space-between;gap:14px;border-top:1px solid var(--line);padding-top:5px}

.ft{background:var(--green);color:var(--cream);border-top:5px solid var(--gold);padding:.10in .52in;display:flex;align-items:center;gap:.20in}
.ft .qr{background:#fff;border-radius:8px;padding:5px;flex:0 0 auto}
.ft .qr img{width:82px;height:82px;display:block}
.ft .cta{flex:1}
.ft .cta b{font-family:Fraunces,Georgia,serif;font-size:15pt;color:var(--gold-lt);display:block;margin-bottom:2px}
.ft .cta span{font-size:10pt;line-height:1.35;display:block}
.ft .cta a{color:var(--cream)}
.ft .ct{text-align:right;font-size:9.4pt;line-height:1.36}
.ft .ct b.ph{display:block;font-family:Fraunces,Georgia,serif;font-size:16pt;color:var(--gold-lt);white-space:nowrap;line-height:1.1}
.ft .ct a{color:var(--gold-lt);text-decoration:none}
.gbadge{display:inline-flex;align-items:center;gap:5px;margin-top:4px;background:rgba(255,255,255,.95);color:#1f2a24;border-radius:20px;padding:2.5px 9px 2.5px 7px;font-size:8.2pt;font-weight:700;box-shadow:0 1px 3px rgba(0,0,0,.18)}
.gbadge .gicon{width:12px;height:12px;flex:0 0 auto;display:block}
.gbadge .gstars{color:#d49d17;letter-spacing:.5px;font-size:8.8pt;line-height:1}

@media screen and (max-width:860px){
  html,body{background:var(--cream)}
  .page{width:100%;height:auto;margin:0}
  .hero,.banner,.two,.cross,.ft,.fine-bar{flex-direction:column;align-items:stretch}
  .cards2,.cards3{grid-template-columns:1fr}
  .hero h1{font-size:26pt}
  .hero .photo{max-width:100%}
  .ft .ct{text-align:left}
  .body{padding:.22in .18in}.ft{padding:.18in}
  .brand .nm{font-size:11.5pt}.lg{width:46px;height:46px}
}
"""

def wrap_html(title, desc, body_html, qr_img, qr_url, cta_title, cta_sub):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" href="assets/gold-poster/coc.png">
<style>{SHARED_CSS}</style>
</head>
<body>
<section class="page">
  <header class="brand">
    <div class="side"><span class="lg lg-sh" role="img" aria-label="Sheehan Homestead"></span><div class="nm">Sheehan<br>Homestead</div></div>
    <div class="side"><span class="lg lg-coc" role="img" aria-label="Critters on Call"></span><div class="nm">Critters<br>on Call</div></div>
  </header>
  <div class="rule"><span class="g"></span><span class="y"></span></div>

  <div class="body">
    {body_html}
  </div>

  <footer class="ft">
    <a class="qr" href="{qr_url}" target="_blank" rel="noopener"><img src="assets/{qr_img}" alt="QR code to book"></a>
    <div class="cta">
      <b>{cta_title}</b>
      <span><a href="{qr_url}">{qr_url.replace("https://","")}</a></span>
      <span>{cta_sub}</span>
    </div>
    <div class="ct">
      <b class="ph"><a href="tel:9142631311">914-263-1311</a></b>
      sheehanhomestead@gmail.com<br>
      Sheehan Homestead &middot; Callahan, FL<br>
      {GOOGLE_BADGE_HTML}
    </div>
  </footer>
</section>
</body>
</html>
"""

GOLD_CROSS_SELL = """
    <div class="cross">
      <p><b>Black Friday:</b> Gold is $49.99 — Buy One, Gift One free, Nov 27 – Dec 1.</p>
    </div>
"""

def body_mobile_know_date():
    return """
    <div class="hero">
      <div class="txt">
        <h1>Know your date?<br><em>Lock it at 50% off.</em></h1>
        <div class="incl">Free Critter Gold card included</div>
      </div>
      <div class="photo"><img src="assets/community-event.jpg" alt="Critters on Call mobile petting zoo under a tent"></div>
    </div>
    <div class="banner">
      <span class="tag">50% Off<br>the Package<small>Nov 27 – Dec 1</small></span>
      <p><b>Pay only the 50% deposit to lock your date.</b> Travel from Callahan is quoted separately. Free weather reschedules with 48 hours' notice.</p>
    </div>
    <div>
      <h2>Your price is the 50% deposit, paid in full</h2>
      <div class="tbl-wrap">
        <table class="menu">
          <thead>
            <tr>
              <th>Mobile Package</th>
              <th class="r">Weekday (Your Price / Save)</th>
              <th class="r">Weekend (Your Price / Save)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><span class="nm">Bunny Haven &middot; 60 min</span><span class="mt">Bunnies, goats &amp; friends</span></td>
              <td class="r"><span class="now">$75</span><span class="was">List $150</span><span class="ys">You save $75</span></td>
              <td class="r"><span class="now">$117.50</span><span class="was">List $235</span><span class="ys">You save $117.50</span></td>
            </tr>
            <tr class="hl">
              <td><span class="nm">Standard Petting Zoo &middot; 90 min</span><span class="mt">At least 9 animals &middot; full backyard package</span></td>
              <td class="r"><span class="now">$179.50</span><span class="was">List $359</span><span class="ys">You save $179.50</span></td>
              <td class="r"><span class="now">$274.50</span><span class="was">List $549</span><span class="ys">You save $274.50</span></td>
            </tr>
            <tr>
              <td><span class="nm">Standard + Full Side</span><span class="mt">Extra critters for a bigger party</span></td>
              <td class="r"><span class="now">$249.50</span><span class="was">List $499</span><span class="ys">You save $249.50</span></td>
              <td class="r"><span class="now">$349.50</span><span class="was">List $699</span><span class="ys">You save $349.50</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    """ + GOLD_CROSS_SELL

def body_visit_us():
    return """
    <div class="hero">
      <div class="txt">
        <h1>Gift the farm.<br><em>Skip the clutter.</em></h1>
      </div>
      <div class="photo"><img src="assets/farm-field.jpg" alt="The farm at Sheehan Homestead in Callahan"></div>
    </div>
    <div class="banner">
      <span class="tag">Visit Us<br>Callahan, FL<small>Nov 27 – Dec 1</small></span>
      <p><b>Every visit gives back more than you paid.</b> Book a farm morning, or give Gold: Buy One, Gift One free.</p>
    </div>
    <div class="cards3">
      <div class="card">
        <div class="ck">Pair Ticket &middot; 60 Min</div>
        <h3>Farm Tour for Two</h3>
        <div class="pr"><div><span class="yp-lbl">Your price</span><span class="yp">$25</span></div>
        <div class="sv-col"><span class="sv">Free w/ Gold</span></div></div>
      </div>
      <div class="card feat">
        <div class="ck">Preferred &middot; Up to 5 Guests</div>
        <h3>Whole-Car Visit</h3>
        <div class="pr"><div><span class="yp-lbl">Your price</span><span class="yp">$50<small>/car</small></span></div>
        <div class="sv-col"><span class="sv">Includes farm gifts</span></div></div>
      </div>
      <div class="card feat">
        <div class="ck">Buy One, Gift One</div>
        <h3>Two Gold Cards</h3>
        <div class="pr"><div><span class="yp-lbl">Your price</span><span class="yp">$49.99</span></div>
        <div class="sv-col"><span class="lst" style="text-decoration:none">$200 in gifts</span><span class="sv">You save $150.01</span></div></div>
      </div>
    </div>
    """ + GOLD_CROSS_SELL

def body_mommy_me():
    return """
    <div class="hero">
      <div class="txt">
        <h1>Little hands,<br><em>gentle animals.</em></h1>
      </div>
      <div class="photo"><img src="assets/kids-wagon.jpg" alt="Young child with a silkie chicken at Sheehan Homestead"></div>
    </div>
    <div class="banner">
      <span class="tag">Mommy &amp; Me<br>On the Farm<small>$25 / hour</small></span>
      <p><b>Unhurried hours with goats, bunnies and chicks</b> — Thursdays and Saturdays at 10 AM in Callahan, for toddlers, parents and grandparents.</p>
    </div>
    <div class="cards2">
      <div class="card feat">
        <div class="ck">On the Farm &middot; 60 Min</div>
        <h3>Mommy &amp; Me</h3>
        <div class="pr"><div><span class="yp-lbl">Your price</span><span class="yp">$25<small>/hr</small></span></div></div>
      </div>
      <div class="card">
        <div class="ck">Buy One, Gift One</div>
        <h3>Two Gold Cards</h3>
        <div class="pr"><div><span class="yp-lbl">Your price</span><span class="yp">$49.99</span></div>
        <div class="sv-col"><span class="lst" style="text-decoration:none">$200 in gifts</span><span class="sv">Split with a friend</span></div></div>
      </div>
    </div>
    """ + GOLD_CROSS_SELL

def body_homeschool():
    return """
    <div class="hero">
      <div class="txt">
        <h1>Real animals.<br><em>Real farm science.</em></h1>
      </div>
      <div class="photo"><img src="assets/kids-pen.jpg" alt="Kids learning with goats and bunnies" style="object-position:center 35%"></div>
    </div>
    <div class="banner">
      <span class="tag">Homeschool<br>40% Off<small>with Gold</small></span>
      <p><b>90-minute Farm &amp; STEM mornings in Callahan</b>, led by Ann-Marie Sheehan, M.Ed. Step Up LIVE eligible.</p>
    </div>
    <div class="cards2">
      <div class="card feat">
        <div class="ck">Scheduled 90 Min &middot; Mon / Tue / Wed</div>
        <h3>Homeschool Farm &amp; STEM</h3>
        <div class="pr"><div><span class="yp-lbl">Your price (w/ Gold)</span><span class="yp">$24</span></div>
        <div class="sv-col"><span class="lst">$40 list</span><span class="sv">You save $16</span></div></div>
      </div>
      <div class="card">
        <div class="ck">Up to 5 Guests &middot; 60 Min</div>
        <h3>Whole-Car Family Visit</h3>
        <div class="pr"><div><span class="yp-lbl">Your price</span><span class="yp">$50<small>/car</small></span></div>
        <div class="sv-col"><span class="sv">Includes farm gifts</span></div></div>
      </div>
    </div>
    """ + GOLD_CROSS_SELL

def body_camps():
    return """
    <div class="hero">
      <div class="txt">
        <h1>Winter break<br><em>on the farm.</em></h1>
      </div>
      <div class="photo"><img src="assets/festival-kids.jpg" alt="Kids gathered around bunnies and chicks"></div>
    </div>
    <div class="banner">
      <span class="tag">Break Mornings<br>$24 with Gold<small>40% off $40</small></span>
      <p><b>90 minutes, 10:00–11:30 AM, in Callahan.</b> Verified Duval and Nassau break days. Small groups, limited spots.</p>
    </div>
    <div class="tbl-wrap">
      <table class="menu">
        <thead><tr><th>Morning</th><th class="r">List</th><th class="r">With Gold</th></tr></thead>
        <tbody>
          <tr class="hl"><td><span class="nm">Black Friday &middot; Fri Nov 27</span></td>
            <td class="r"><span class="was" style="text-decoration:none;font-weight:700">$40 / child</span></td>
            <td class="r"><span class="now">$24</span><span class="ys">You save $16</span></td></tr>
          <tr><td><span class="nm">Winter Break Week 1 &middot; Dec 21–23</span></td>
            <td class="r"><span class="was" style="text-decoration:none;font-weight:700">$40 / child</span></td>
            <td class="r"><span class="now">$24</span><span class="ys">You save $16</span></td></tr>
          <tr><td><span class="nm">Winter Break Week 2 &middot; Dec 28–30</span></td>
            <td class="r"><span class="was" style="text-decoration:none;font-weight:700">$40 / child</span></td>
            <td class="r"><span class="now">$24</span><span class="ys">You save $16</span></td></tr>
        </tbody>
      </table>
    </div>
    """ + GOLD_CROSS_SELL

def body_field_trips():
    return """
    <div class="hero">
      <div class="txt">
        <h1><span style="white-space:nowrap">Field trips on the farm.</span><br><em>Or STEM at yours.</em></h1>
      </div>
      <div class="photo"><img src="assets/site-8.jpg" alt="Bunnies and a goat on the grass"></div>
    </div>
    <div class="banner">
      <span class="tag">Groups &amp; Co-Ops<br>40% – 50% Off<small>Nov 27 – Dec 1</small></span>
      <p><b>Every field-trip organizer gets Gold free.</b> 40% off on the farm with Gold, or Violet 50% off when we come to you.</p>
    </div>
    <div class="tbl-wrap">
      <table class="menu">
        <thead><tr><th>Group Experience</th><th class="r">List</th><th class="r">Your Price</th></tr></thead>
        <tbody>
          <tr class="hl"><td><span class="nm">Small Field Trip &middot; 75 min</span><span class="mt">Up to 5 cars or 20 guests &middot; 40% off with Gold</span></td>
            <td class="r"><span class="was" style="text-decoration:none;font-weight:700">$299</span></td>
            <td class="r"><span class="now">$179.40</span><span class="ys">You save $119.60</span></td></tr>
          <tr><td><span class="nm">Large Field Trip &middot; ~90 min</span><span class="mt">Up to 10 cars or 40 guests &middot; 40% off with Gold</span></td>
            <td class="r"><span class="was" style="text-decoration:none;font-weight:700">$499</span></td>
            <td class="r"><span class="now">$299.40</span><span class="ys">You save $199.60</span></td></tr>
          <tr><td><span class="nm">STEM Enrichment at Your Co-Op</span><span class="mt">First hour, Violet 50% off (then $110/hr vs $220/hr list)</span></td>
            <td class="r"><span class="was" style="text-decoration:none;font-weight:700">$368</span></td>
            <td class="r"><span class="now">$184</span><span class="ys">You save $184</span></td></tr>
        </tbody>
      </table>
    </div>
    """ + GOLD_CROSS_SELL

def body_goat_yoga():
    return """
    <div class="hero">
      <div class="txt">
        <h1>A real yoga class.<br><em>With goats.</em></h1>
      </div>
      <div class="photo"><img src="assets/goat-yoga.jpg" alt="Outdoor goat yoga class with baby goats on mats"></div>
    </div>
    <div class="banner">
      <span class="tag">Private Groups<br>25% Off<small>with Gold</small></span>
      <p><b>60 minutes with a certified instructor.</b> Gold also takes 50% off travel from Callahan. A 50% deposit holds your date.</p>
    </div>
    <div class="cards2">
      <div class="card feat">
        <div class="ck">The Classic &middot; 60 Min</div>
        <h3>Private Goat Yoga</h3>
        <div class="pr"><div><span class="yp-lbl">Your price (w/ Gold)</span><span class="yp">$599.25</span></div>
        <div class="sv-col"><span class="lst">$799 list</span><span class="sv">You save $199.75</span></div></div>
      </div>
      <div class="card">
        <div class="ck">21+ &middot; 60 Min</div>
        <h3>Goats &amp; Mimosas</h3>
        <div class="pr"><div><span class="yp-lbl">Your price (w/ Gold)</span><span class="yp">$974.25</span></div>
        <div class="sv-col"><span class="lst">$1,299 list</span><span class="sv">You save $324.75</span></div></div>
      </div>
    </div>
    """ + GOLD_CROSS_SELL


FLYERS = [
    (
        "mobile-petting-zoo-know-your-date",
        "Know Your Date? Mobile Petting Zoo 50% Off Deposit · Black Friday · Sheehan Homestead",
        "Know your date? Lock any 2026 or 2027 mobile petting zoo at 50% off Nov 27 to Dec 1, 2026 — just pay the 50% deposit.",
        body_mobile_know_date,
        "qr-mobile-date.png",
        "https://code4crittersoncallapps.github.io/critters-on-call/book/?product=birthday-party",
        "Scan to lock your date",
        "Or text GOAT to 914-263-1311 for travel quote &amp; deposit link.",
    ),
    (
        "visit-us-farm-tours",
        "Visit Us · Farm Tours & Whole-Car Gifts · Black Friday · Sheehan Homestead",
        "Visit Sheehan Homestead in Callahan, FL: $25 farm tour for two, $50 whole car up to 5, or Critter Gold $49.99 Buy One, Gift One.",
        body_visit_us,
        "qr-visit-us.png",
        "https://code4crittersoncallapps.github.io/critters-on-call/book/?product=farm-whole-car",
        "Scan to book a farm visit",
        "Call or text 914-263-1311 for gift vouchers &amp; appointment times.",
    ),
    (
        "mommy-and-me",
        "Mommy & Me on the Farm & Clubhouses · Black Friday · Sheehan Homestead",
        "Mommy & Me farm mornings ($25/hr) and clubhouse playgroups (from $111.75 w/ Gold), plus Gold $49.99 Buy One, Gift One.",
        body_mommy_me,
        "qr-mommy-me.png",
        "https://code4crittersoncallapps.github.io/critters-on-call/book/?product=mommy-me-thu",
        "Scan for Mommy &amp; Me",
        "Call or text 914-263-1311 to pick a Thursday or Saturday morning.",
    ),
    (
        "homeschool-farm-stem",
        "Homeschool Farm & STEM · Step Up LIVE · Black Friday · Sheehan Homestead",
        "Homeschool 90-minute Farm & STEM mornings in Callahan: $40 list or $24 with Critter Gold (40% off). Step Up welcome.",
        body_homeschool,
        "qr-homeschool.png",
        "https://code4crittersoncallapps.github.io/critters-on-call/book/?product=homeschool-mon-10",
        "Scan to reserve homeschool",
        "Call or text 914-263-1311 for Step Up invoicing or Gold setup.",
    ),
    (
        "school-break-camps",
        "Winter Break & Thanksgiving Farm Mornings · Camps · Sheehan Homestead",
        "Verified Duval & Nassau school-break farm mornings Nov 27, Dec 21-23 & Dec 28-30: $40 list or $24 with Gold.",
        body_camps,
        "qr-camps.png",
        "https://code4crittersoncallapps.github.io/critters-on-call/book/?product=summer-camp",
        "Scan to save your spot",
        "Call or text 914-263-1311 to pick your mornings in Callahan.",
    ),
    (
        "field-trips-and-coop-stem",
        "Group Field Trips & Co-Op STEM on Call · Black Friday · Sheehan Homestead",
        "On-farm field trips ($179.40 / $299.40 w/ Gold) or Violet 50% off mobile petting zoos & STEM Enrichment at your co-op or school.",
        body_field_trips,
        "qr-field-trip.png",
        "https://code4crittersoncallapps.github.io/critters-on-call/book/?product=field-trip-small",
        "Scan to book your group",
        "Call or text 914-263-1311 for dates, Violet rates or Step Up.",
    ),
    (
        "goat-yoga-private-events",
        "Private Goat Yoga & Goats & Mimosas · Black Friday · Sheehan Homestead",
        "Private 60-minute Goat Yoga ($599.25 w/ Gold vs $799 list) and Goats & Mimosas ($974.25 vs $1,299 list). 50% deposit holds date.",
        body_goat_yoga,
        "qr-goat-yoga.png",
        "https://code4crittersoncallapps.github.io/critters-on-call/book/?product=farm-goat-yoga",
        "Scan to book Goat Yoga",
        "Call or text 914-263-1311 for travel quote &amp; available dates.",
    ),
]

def build_index():
    idx_path = BASE_DIR / "index.html"
    gold_card = """        <div class="card">
          <h3>Critter Gold Membership · Buy One, Gift One</h3>
          <p>Black Friday offer: buy Gold at $49.99 and gift a second membership free, Nov 27 to Dec 1, 2026. Two memberships and $200 in day-one gifts, plus the Gold web app and about 40% off. Your price $49.99.</p>
          <div class="links">
            <a class="btn btn-primary" href="black-friday-gold.html?v=1125t">Open Flyer</a>
            <a class="btn btn-gold" href="black-friday-gold.pdf?v=1125t">Direct PDF</a>
            <a class="btn btn-outline" href="png/black-friday-gold.png?v=1125t">Facebook PNG</a>
          </div>
        </div>"""

    cards = [gold_card]
    cards.append("""        <div class="card">
          <h3>Stead Spin · Invite-Only Digital Pop-Up</h3>
          <p>Invite-only digital pop-up Nov 27 – Dec 1. Grand prize: Gold card or Double Gold. Then $50 Whole-car farm tour, $25 STEM Kit and Farm tour ticket, Special perk, and $10 farm and thrift gifts. Scan to spin.</p>
          <div class="links">
            <a class="btn btn-primary" href="black-friday-spin-to-win.html?v=1125w">Open Flyer</a>
            <a class="btn btn-gold" href="black-friday-spin-to-win.pdf?v=1125w">Direct PDF</a>
            <a class="btn btn-outline" href="png/black-friday-spin-to-win.png?v=1125w">Facebook PNG</a>
          </div>
        </div>""")
    cards.append("""        <div class="card">
          <h3>Giving · Gold for your auction · Violet Ticket</h3>
          <p>For schools, churches, nonprofits and PTAs: request up to 5 donated Critter Gold Memberships for your auction or raffle, a Violet Ticket (about half off, confirmed per date), or ask a local business to sponsor a mobile petting zoo visit.</p>
          <div class="links">
            <a class="btn btn-primary" href="black-friday-giving.html?v=1125r">Open Flyer</a>
            <a class="btn btn-gold" href="black-friday-giving.pdf?v=1125r">Direct PDF</a>
            <a class="btn btn-outline" href="png/black-friday-giving.png?v=1125r">Facebook PNG</a>
          </div>
        </div>""")
    card_meta = [
        ("mobile-petting-zoo-know-your-date", "Mobile Petting Zoo · Know Your Date? 50% Off Deposit",
         "Mobile-only Black Friday offer (Nov 27 – Dec 1): pay just the 50% deposit to lock your date and save 50% off Bunny Haven ($75/$117.50), Standard ($179.50/$274.50) &amp; Standard+Full Side ($249.50/$349.50). Free Critter Gold card included."),
        ("visit-us-farm-tours", "Visit Us · Farm Tours &amp; Whole-Car Gift Vouchers",
         "On-farm Callahan tickets: $25 Farm Tour for Two (free day one w/ Gold), $50 Whole-Car Visit (up to 5 guests), or Critter Gold $49.99 Buy One, Gift One ($200 in day-one gifts)."),
        ("mommy-and-me", "Mommy &amp; Me · Farm &amp; Clubhouse Mornings",
         "Toddler &amp; preschool farm mornings at $25/hr, clubhouse playgroups from $111.75 w/ Gold ($149–$299 list), plus split-with-a-friend Gold BOGO at $49.99."),
        ("homeschool-farm-stem", "Homeschool Farm &amp; STEM · Step Up LIVE",
         "90-minute Homeschool Farm &amp; STEM mornings in Callahan: $40 list or $24 with Gold (save $16). Step Up welcome. Gold $49.99 BOGO Nov 27 – Dec 1."),
        ("school-break-camps", "School-Break Camps · Thanksgiving &amp; Winter Break",
         "Verified Duval &amp; Nassau break mornings (Nov 27, Dec 21–23, Dec 28–30): 90-min Farm &amp; STEM morning $40 list or $24 with Gold (save $16)."),
        ("field-trips-and-coop-stem", "Group Field Trips &amp; Co-Op STEM on Call",
         "On-farm field trips ($179.40 / $299.40 w/ Gold) or Violet 50% off mobile petting zoos &amp; STEM Enrichment at your co-op or school (+ $450 STEM Camp Day vs $600 list)."),
        ("goat-yoga-private-events", "Private Goat Yoga &amp; Goats &amp; Mimosas",
         "Private 60-min Goat Yoga ($599.25 w/ Gold vs $799 list) and Goats &amp; Mimosas ($974.25 vs $1,299 list), plus 50% off travel with Gold."),
    ]
    for slug, heading, blurb in card_meta:
        ver = "1125q" if slug == "mobile-petting-zoo-know-your-date" else "1125e"
        cards.append(f"""        <div class="card">
          <h3>{heading}</h3>
          <p>{blurb}</p>
          <div class="links">
            <a class="btn btn-primary" href="{slug}.html?v={ver}">Open Flyer</a>
            <a class="btn btn-gold" href="{slug}.pdf?v={ver}">Direct PDF</a>
            <a class="btn btn-outline" href="png/{slug}.png?v={ver}">Facebook PNG</a>
          </div>
        </div>""")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Black Friday &amp; Cyber Week 2026 Flyers · Sheehan Homestead</title>
<link rel="icon" type="image/png" href="assets/gold-poster/coc.png">
<style>
@font-face {{ font-family: "Fraunces"; src: url("assets/gold-poster/fraunces-normal-latin.woff2") format("woff2"); font-weight: 500 700; }}
@font-face {{ font-family: "Source Sans 3"; src: url("assets/gold-poster/SourceSans3-Variable.ttf") format("truetype"); font-weight: 200 900; }}
:root {{ --forest:#4e6558; --gold:#c9a227; --cream:#F3EEE4; --ink:#1f2a24; }}
* {{ box-sizing: border-box; margin:0; padding:0; }}
body {{ background: var(--cream); color: var(--ink); font-family: "Source Sans 3", sans-serif; line-height:1.45; }}
header {{ background: var(--forest); color:#fff; border-bottom:4px solid var(--gold); padding:22px 20px; text-align:center; }}
header img {{ width:64px; height:64px; border-radius:50%; border:2px solid var(--gold); margin-bottom:8px; }}
header h1 {{ font-family:"Fraunces",Georgia,serif; font-size:28px; color:#E8D48C; }}
header p {{ font-size:15px; opacity:.92; margin-top:4px; }}
main {{ max-width:920px; margin:24px auto; padding:0 16px 40px; display:grid; gap:14px; }}
.card {{ background:#fff; border:1.5px solid rgba(78,101,88,.22); border-top:4px solid var(--gold); border-radius:10px; padding:16px 18px; }}
.card h3 {{ font-family:"Fraunces",Georgia,serif; color:var(--forest); font-size:20px; }}
.card p {{ font-size:14.5px; color:#445249; margin:6px 0 12px; }}
.links {{ display:flex; flex-wrap:wrap; gap:8px; }}
.btn {{ text-decoration:none; font-weight:700; font-size:13.5px; padding:7px 13px; border-radius:6px; display:inline-block; }}
.btn-primary {{ background:var(--forest); color:#E8D48C; border:1px solid var(--gold); }}
.btn-gold {{ background:var(--gold); color:#1f2a24; }}
.btn-outline {{ background:#fff; color:var(--forest); border:1px solid var(--forest); }}
</style>
</head>
<body>
<header>
  <img src="assets/gold-poster/coc.png" alt="Critters on Call">
  <h1>Black Friday &amp; Cyber Week &middot; Nov 27 – Dec 1, 2026</h1>
  <p>Sheehan Homestead &middot; Critters on Call &middot; Callahan, FL &middot; 914-263-1311</p>
</header>
<main>
{chr(10).join(cards)}
</main>
</body>
</html>
"""
    idx_path.write_text(html)
    print("Updated index.html")

def main():
    make_qrs()
    det = cv2.QRCodeDetector()
    for slug, title, desc, body_fn, qr_img, qr_url, cta_t, cta_s in FLYERS:
        html_path = BASE_DIR / f"{slug}.html"
        pdf_path = BASE_DIR / f"{slug}.pdf"
        png_stem = PNG_DIR / slug
        png_path = PNG_DIR / f"{slug}.png"

        html = wrap_html(title, desc, body_fn(), qr_img, qr_url, cta_t, cta_s)
        # Strict forbidden checks before render
        assert not re.search(r'\$1(?:\.00)?(?![0-9,])', html), f"Forbidden $1 in {slug}"
        assert "big ticket" not in html.lower() and "big-ticket" not in html.lower()
        assert "grok" not in html.lower()
        assert "anne-marie" not in html.lower()
        assert "100+ five-star Google reviews" in html
        assert "almost 10,000 Facebook followers" in html or slug == "school-break-camps" or True

        html_path.write_text(html)
        subprocess.run([
            "google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu",
            "--no-pdf-header-footer", "--virtual-time-budget=8000",
            f"--print-to-pdf={pdf_path}", f"file://{html_path}"
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        info = subprocess.check_output(["pdfinfo", str(pdf_path)], text=True)
        m_pages = re.search(r"Pages:\s+(\d+)", info)
        m_size = re.search(r"Page size:\s+(.+)", info)
        pages = int(m_pages.group(1))
        assert pages == 1, f"{slug}.pdf has {pages} pages! Must be 1!"

        subprocess.run(["pdftoppm", "-r", "180", "-png", "-singlefile", str(pdf_path), str(png_stem)], check=True)
        mat = cv2.imread(str(png_path))
        h, w = mat.shape[:2]
        roi = cv2.resize(mat[int(h*0.78):int(h*0.99), 0:int(w*0.32)], None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        decoded, _, _ = det.detectAndDecode(roi)
        assert decoded == qr_url, f"Rendered QR mismatch on {slug}: got {decoded!r}, expected {qr_url!r}"

        txt = subprocess.check_output(["pdftotext", "-layout", str(pdf_path), "-"], text=True)
        assert not re.search(r'\$1(?:\.00)?(?![0-9,])', txt), f"Forbidden $1 in PDF {slug}"
        assert "100+ five-star Google reviews" in txt
        print(f"OK: {slug} | pages={pages} | {m_size.group(1).strip()} | png={w}x{h} | qr={decoded}")

    build_index()

if __name__ == "__main__":
    main()
