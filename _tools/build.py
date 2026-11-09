import json, re, sys, html
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import SERVICES, AREAS, ML_AREAS, TOP, INTROS, INTROS2
from articles2 import ARTICLES2
from articles_daily import ARTICLES_DAILY

REPO = sys.argv[1]
BASE = "https://fixmatekerala.com"
TEL = "+917736516727"
TEL_SHOW = "+91 77365 16727"

src = open(f"{REPO}/electrician-north-paravur.html", encoding="utf-8").read()
STYLE = re.search(r"<style>.*?</style>", src, re.S).group(0)
CALL_SVG = re.search(r'(<svg viewBox="0 0 24 24" fill="none".*?</svg>)', src, re.S).group(1)
WA_SVG = re.search(r'(<svg viewBox="0 0 24 24" fill="currentColor">.*?</svg>)', src, re.S).group(1)
FOOTER = re.search(r"<footer>.*?</footer>", src, re.S).group(0)

EXTRA_CSS = """<style>
.svc{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:12px}
.svc a{display:block;text-decoration:none;border:1px solid var(--line);border-radius:14px;padding:14px 16px}
.svc a:hover{border-color:var(--accent)}
.svc b{display:block;color:var(--dark);font-size:15px}.svc span{font-size:13.5px;color:var(--muted)}
.areas a{text-decoration:none}
.ml{background:var(--soft);border-radius:14px;padding:18px 20px;font-size:15.5px;line-height:1.8}
article.post{max-width:760px;margin:0 auto;padding:10px 0 30px}
article.post h1{font-size:34px;margin:10px 0 8px}
article.post h2{font-size:22px;margin:28px 0 8px}
article.post p,article.post li{font-size:16px;color:#33354a}
article.post .meta{color:#8a8ca0;font-size:13px}
.tip{border-left:3px solid var(--accent);background:#fff8f4;padding:12px 16px;border-radius:0 10px 10px 0;margin:18px 0}
.posts a{display:block;text-decoration:none;border:1px solid var(--line);border-radius:14px;padding:18px;margin-bottom:12px}
.posts a:hover{border-color:var(--accent)}.posts b{font-size:18px;color:var(--dark)}.posts p{margin:6px 0 0;color:var(--muted);font-size:14.5px}
</style>"""


def wa_link(msg):
    from urllib.parse import quote
    return f"https://wa.me/917736516727?text={quote(msg)}"


def head(title, desc, path, image, schema):
    url = BASE + path
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#ff6a1a">
<meta property="og:type" content="website">
<meta property="og:site_name" content="FixMate Kerala">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}{image}">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
{STYLE}
{EXTRA_CSS}
</head>
<body>"""


def header(wa):
    return f"""<header>
  <a class="brand" href="/"><div class="brand-mark">F</div>FixMate <span>Kerala</span></a>
  <div class="head-actions">
    <a class="cbtn call" href="tel:{TEL}" aria-label="Call FixMate Kerala">{CALL_SVG}<span class="lbl">Call</span></a>
    <a class="cbtn wa" href="{wa}" target="_blank" rel="noopener" aria-label="WhatsApp FixMate Kerala">{WA_SVG}<span class="lbl">WhatsApp</span></a>
  </div>
</header>"""


def tail(wa):
    foot = FOOTER.replace('<span>Home repairs in North Paravur, Kerala</span>',
                          '<span><a href="/areas">Areas we serve</a><a href="/blog/">Home tips</a>Home repairs in North Paravur, Kerala</span>')
    return f"""{foot}
<a class="wa-float" href="{wa}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{WA_SVG}</a>
</body>
</html>
"""


BUSINESS_REF = {"@type": "HomeAndConstructionBusiness", "@id": BASE + "/#business", "name": "FixMate Kerala"}
SVC = {s[0]: s for s in SERVICES}


def crumbs_schema(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + p} for i, (n, p) in enumerate(items)]}


def area_links(current=None):
    out = ['<li><a href="/">North Paravur</a></li>']
    for slug, en, ml in AREAS:
        if slug == current:
            out.append(f"<li>{en}</li>")
        else:
            out.append(f'<li><a href="/home-services-{slug}">{en}</a></li>')
    return '<ul class="areas">' + "".join(out) + "</ul>"


# ---------------- Area pages ----------------
def area_page(i, slug, en, ml):
    path = f"/home-services-{slug}"
    title = f"Electrician, Plumber and Home Repairs in {en} | FixMate Kerala"
    desc = f"Book electricians, plumbers, AC repair, carpenters, cleaning and pest control in {en}. Clear prices from ₹49. Call or WhatsApp FixMate Kerala."
    wa = wa_link(f"Hi FixMate Kerala, I need a home service in {en}.")
    order = TOP[i % len(TOP):] + TOP[:i % len(TOP)]
    rest = [s[0] for s in SERVICES if s[0] not in order]
    cards = "".join(
        f'<a href="/{k}-north-paravur"><b>{SVC[k][1]} in {en}</b><span>{SVC[k][4]}. From ₹49.</span></a>'
        for k in order + rest)
    others = [a for a in AREAS if a[0] != slug]
    near = ", ".join(a[1] for a in others[:4])
    faqs = [
        (f"Do you provide home services in {en}?",
         f"Yes. {en} is part of our regular service area along with North Paravur, {near} and nearby places."),
        (f"How do I book an electrician or plumber in {en}?",
         f"Book online, call {TEL_SHOW} or send us a WhatsApp message with your address in {en}, the job you need and a photo of the issue. We confirm the visit time with you."),
        ("Are spare parts included in the price?",
         "Our prices cover labour. Materials and spare parts are extra at shop price, and we tell you before buying anything."),
        (f"{en} ൽ സേവനം ലഭിക്കുമോ?",
         f"ലഭിക്കും. {ml} ഉൾപ്പെടെ നോർത്ത് പറവൂരിനടുത്തുള്ള സ്ഥലങ്ങളിൽ ഞങ്ങൾ സേവനം നൽകുന്നു. വിളിക്കുക അല്ലെങ്കിൽ WhatsApp ചെയ്യുക: {TEL_SHOW}."),
    ]
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "name": title, "url": BASE + path, "about": BUSINESS_REF,
         "areaServed": {"@type": "Place", "name": f"{en}, Ernakulam, Kerala"}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
        crumbs_schema([("Home", "/"), ("Areas we serve", "/areas"), (f"Home services in {en}", path)])]}
    intro = INTROS[i % 3].format(a=en)
    intro2 = INTROS2[i % 3].format(a=en)
    faq_html = "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in faqs)
    body = f"""{header(wa)}
<main class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> &rsaquo; <a href="/areas">Areas we serve</a> &rsaquo; {en}</nav>
  <div class="hero">
    <div>
      <div class="eyebrow">{en}, Ernakulam</div>
      <h1>Home repairs and services in {en}</h1>
      <p>{intro}</p><p>{intro2}</p>
      <div class="from">Prices from <b>₹49</b></div>
      <div class="ctas">
        <a class="cbtn book" href="/">Book online</a>
        <a class="cbtn call" href="tel:{TEL}">{CALL_SVG}Call {TEL_SHOW}</a>
        <a class="cbtn wa" href="{wa}" target="_blank" rel="noopener">{WA_SVG}WhatsApp</a>
      </div>
    </div>
    <div class="hero-img"><img src="/images/handyman-north-paravur.jpg" alt="Home repair service in {en}" width="640" height="480"></div>
  </div>

  <section>
    <h2>Services available in {en}</h2>
    <p class="sub">Tap a service to see the jobs and prices.</p>
    <div class="svc">{cards}</div>
    <p class="note">Minimum order ₹199 per visit. Materials and spare parts are extra at shop price.</p>
  </section>

  <section>
    <h2>How booking works</h2>
    <div class="steps">
      <div class="step"><b>Choose the job</b><p>Pick what you need and see the price upfront.</p></div>
      <div class="step"><b>Share your address</b><p>Tell us where in {en} you are and when suits you.</p></div>
      <div class="step"><b>We come and fix it</b><p>A checked professional visits and gets it done.</p></div>
    </div>
  </section>

  <section>
    <h2>മലയാളത്തിൽ</h2>
    <div class="ml">{ml} ഭാഗത്ത് ഇലക്ട്രീഷ്യൻ, പ്ലംബർ, എസി റിപ്പയർ, ക്ലീനിംഗ് തുടങ്ങിയ വീട്ടുസേവനങ്ങൾ ആവശ്യമുണ്ടോ? FixMate Kerala പരിശീലനം ലഭിച്ച ജോലിക്കാരെ നിങ്ങളുടെ വീട്ടിലേക്ക് അയയ്ക്കുന്നു. ജോലി തുടങ്ങുന്നതിന് മുമ്പ് നിരക്ക് അറിയിക്കും. ₹49 മുതൽ നിരക്കുകൾ. വിളിക്കുക അല്ലെങ്കിൽ WhatsApp ചെയ്യുക: {TEL_SHOW}.</div>
  </section>

  <section>
    <h2>Other areas we serve</h2>
    {area_links(slug)}
  </section>

  <section>
    <h2>Questions people ask</h2>
    {faq_html}
  </section>

  <div class="band">
    <div><h2>Need help at home in {en}?</h2><p>Call or WhatsApp us, or book online in two minutes.</p></div>
    <div class="ctas" style="margin:0"><a class="cbtn book" href="/">Book online</a><a class="cbtn wa" href="{wa}" target="_blank" rel="noopener">{WA_SVG}WhatsApp</a></div>
  </div>
</main>"""
    return path, head(title, desc, path, "/images/handyman-north-paravur.jpg", schema) + body + tail(wa)


def areas_index():
    path = "/areas"
    title = "Areas We Serve near North Paravur | FixMate Kerala"
    desc = "FixMate Kerala provides home repairs and services in North Paravur, Varapuzha, Kottuvally, Aluva and nearby places in Ernakulam."
    wa = wa_link("Hi FixMate Kerala, I need a home service.")
    cards = "".join(f'<a href="/home-services-{s}"><b>{en}</b><span>{ml}</span></a>' for s, en, ml in AREAS)
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "name": title, "url": BASE + path, "about": BUSINESS_REF},
        crumbs_schema([("Home", "/"), ("Areas we serve", path)])]}
    body = f"""{header(wa)}
<main class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> &rsaquo; Areas we serve</nav>
  <section style="border-top:none">
    <h1 style="font-size:34px;margin-bottom:10px">Areas we serve</h1>
    <p class="sub">FixMate Kerala is based in North Paravur and serves these nearby places. For other places, call us to check availability.</p>
    <div class="svc"><a href="/"><b>North Paravur</b><span>നോർത്ത് പറവൂർ</span></a>{cards}</div>
  </section>
</main>"""
    return path, head(title, desc, path, "/images/fixmate-kerala-og.jpg", schema) + body + tail(wa)


# ---------------- Articles ----------------
ARTICLES = [
    ("ceiling-fan-making-noise", "Ceiling Fan Making Noise or Running Slow? Causes and Fixes",
     "Why ceiling fans wobble, hum, click or run slowly, what you can safely check yourself, and when to call an electrician.",
     "electrician", "/images/electrician-north-paravur.jpg", """
<p>A ceiling fan runs for hours every day in a Kerala home, so small problems show up quickly. Most fan noises have a simple cause. Here is how to narrow it down before you call anyone.</p>
<div class="tip"><b>Safety first:</b> switch off the fan at the switch and the MCB before you touch it, and use a steady ladder. Never open the regulator or switch board yourself.</div>
<h2>1. Wobbling or shaking</h2>
<p>Usually caused by a loose canopy screw, a loose blade screw, or blades that are slightly bent or carry different amounts of dust. Clean all blades, then tighten every screw you can see. If it still wobbles, the blades may need balancing or the hanging rod may be loose.</p>
<h2>2. Clicking or ticking</h2>
<p>Often a loose blade screw or a loose canopy cover rubbing against the rod. Tighten and listen again. A clicking sound that follows the speed of the fan can also come from a worn bearing.</p>
<h2>3. Humming or buzzing</h2>
<p>A hum is commonly caused by the regulator, especially older step regulators, or by a loose wire connection. Try the fan at full speed. If the hum disappears at full speed, the regulator is the likely cause. This needs an electrician.</p>
<h2>4. Running slower than before</h2>
<p>The most common cause is a weak capacitor. It is a small, cheap part and replacing it is a short job. Low voltage in the evening can also make fans slow, so check whether other fans in the house are slow too.</p>
<h2>5. Grinding noise</h2>
<p>A grinding or rough sound usually means the bearings are worn or dry. Bearings can be replaced, but for an old fan a new fan can be the better value. Ask for a quote first.</p>
<h2>When to call an electrician</h2>
<ul><li>The fan hums, sparks, smells of burning or gets very hot</li><li>The fan is slow even at full speed</li><li>The fan still wobbles after cleaning and tightening</li><li>The switch or regulator feels warm</li></ul>
<p>FixMate Kerala handles fan repair, capacitor change and new fan installation in North Paravur and nearby places, with the price agreed before work starts.</p>
"""),
    ("water-tank-cleaning-kerala", "How Often Should You Clean Your Water Tank in Kerala?",
     "A simple guide to water tank and well cleaning in Kerala homes: how often, warning signs, and what a proper cleaning includes.",
     "water-tank-cleaning", "/images/water-tank-cleaning-north-paravur.jpg", """
<p>Overhead tanks and wells collect silt, algae and dirt over time, especially after the monsoon. Clean storage matters for drinking, cooking and bathing water.</p>
<h2>How often to clean</h2>
<ul><li><b>Overhead and sump tanks:</b> at least once every 6 months</li><li><b>After heavy monsoon rain or flooding:</b> clean and disinfect as soon as the water settles</li><li><b>Wells:</b> once a year, ideally before the monsoon, and again if the water changes colour or smell</li></ul>
<h2>Warning signs your tank needs cleaning now</h2>
<ul><li>Water looks cloudy, yellow or has particles</li><li>A musty or rotten smell</li><li>Green or slimy layer on the tank walls</li><li>Small insects or larvae in the water</li><li>Taps and shower heads clogging often</li></ul>
<h2>What a proper cleaning includes</h2>
<ol><li>Draining the tank and removing settled sludge</li><li>Scrubbing walls, floor and lid</li><li>Rinsing out the dirty water</li><li>Disinfecting the tank</li><li>Final rinse and refilling</li></ol>
<div class="tip"><b>Tip:</b> keep the tank lid closed and in good condition. A broken lid lets in dust, leaves, insects and birds, and makes the tank dirty much faster.</div>
<h2>Can I do it myself?</h2>
<p>Small tanks can be cleaned at home, but working inside a tank or a well is risky, especially on a roof or in a deep well. For wells in particular, use trained people.</p>
<p>FixMate Kerala offers water tank and well cleaning in North Paravur and nearby places, with the price agreed before work starts.</p>
"""),
    ("monsoon-home-checklist-kerala", "Monsoon Home Checklist for Kerala Houses",
     "A practical checklist to get your Kerala home ready for the monsoon: roof, gutters, wiring, plumbing, damp and pests.",
     "handyman", "/images/handyman-north-paravur.jpg", """
<p>A few small checks before the rain starts can save a lot of trouble and money during the monsoon. Use this list in May, and again before the northeast monsoon in October.</p>
<h2>Roof and drainage</h2>
<ul><li>Clear leaves from the terrace, gutters and drain pipes</li><li>Check roof tiles or sheets for cracks and gaps</li><li>Look for old water stains on ceilings, which show where leaks start</li><li>Make sure water drains away from the house walls and foundation</li></ul>
<h2>Electrical safety</h2>
<ul><li>Check outdoor sockets, lights and the motor switch for water entry</li><li>Fix loose wires and damaged switch boards before the rain</li><li>Test that the MCB and ELCB trip correctly</li><li>Keep the inverter and battery in a dry place</li></ul>
<div class="tip"><b>Safety:</b> if the MCB keeps tripping after rain, do not keep switching it back on. Moisture in the wiring needs an electrician.</div>
<h2>Plumbing and water</h2>
<ul><li>Clean the water tank and check the lid</li><li>Clear bathroom and kitchen drains</li><li>Check the pump and foot valve</li><li>If you use a well, check the well wall and cover</li></ul>
<h2>Walls, doors and windows</h2>
<ul><li>Seal cracks in outer walls and around windows</li><li>Treat damp patches early, before paint peels</li><li>Oil hinges and locks, since wooden doors swell in the rain</li><li>Fix mosquito nets on windows and doors</li></ul>
<h2>Pests</h2>
<ul><li>Remove standing water in pots, tyres and the terrace to stop mosquitoes breeding</li><li>Check wooden furniture and door frames for termites</li></ul>
<p>FixMate Kerala can handle most of this in one visit in North Paravur and nearby places: electrician, plumber, carpenter, tank cleaning, mosquito nets and pest control.</p>
"""),
]


ARTICLES = ARTICLES + ARTICLES2 + ARTICLES_DAILY


def article_page(slug, title, desc, svc, image, content, date="2026-11-10"):
    path = f"/blog/{slug}"
    wa = wa_link("Hi FixMate Kerala, I read your home tips and need help.")
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": title, "description": desc, "image": BASE + image,
         "datePublished": date, "dateModified": date,
         "author": {"@type": "Organization", "name": "FixMate Kerala", "url": BASE + "/"},
         "publisher": BUSINESS_REF, "mainEntityOfPage": BASE + path},
        crumbs_schema([("Home", "/"), ("Home tips", "/blog/"), (title, path)])]}
    s = SVC[svc]
    body = f"""{header(wa)}
<main class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> &rsaquo; <a href="/blog/">Home tips</a> &rsaquo; {html.escape(title)}</nav>
  <article class="post">
    <h1>{html.escape(title)}</h1>
    <div class="meta">FixMate Kerala · {pretty(date)}</div>
    {content}
    <div class="band">
      <div><h2>Need a hand with this?</h2><p>See {s[1]} jobs and prices for North Paravur and nearby places.</p></div>
      <div class="ctas" style="margin:0"><a class="cbtn book" href="/{svc}-north-paravur">See prices</a><a class="cbtn wa" href="{wa}" target="_blank" rel="noopener">{WA_SVG}WhatsApp</a></div>
    </div>
  </article>
</main>"""
    return path, head(f"{title} | FixMate Kerala", desc, path, image, schema) + body + tail(wa)


def pretty(d):
    import datetime
    return datetime.date.fromisoformat(d).strftime("%d %B %Y").lstrip("0")


def blog_index():
    path = "/blog/"
    title = "Home Tips for Kerala Homes | FixMate Kerala"
    desc = "Practical home repair and maintenance tips for Kerala homes from FixMate Kerala, North Paravur."
    wa = wa_link("Hi FixMate Kerala, I need help at home.")
    cards = "".join(f'<a href="/blog/{a[0]}"><b>{html.escape(a[1])}</b><p>{html.escape(a[2])}</p></a>' for a in reversed(ARTICLES))
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "Blog", "name": "FixMate Kerala Home Tips", "url": BASE + path, "publisher": BUSINESS_REF},
        crumbs_schema([("Home", "/"), ("Home tips", path)])]}
    body = f"""{header(wa)}
<main class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> &rsaquo; Home tips</nav>
  <article class="post">
    <h1>Home tips</h1>
    <p>Simple, practical advice for looking after a Kerala home.</p>
    <div class="posts">{cards}</div>
  </article>
</main>"""
    return path, head(title, desc, path, "/images/fixmate-kerala-og.jpg", schema) + body + tail(wa)


# ---------------- Malayalam on service pages ----------------
ML_MARK = "<!-- ml-section -->"


def add_malayalam(slug):
    f = f"{REPO}/{slug}-north-paravur.html"
    s = open(f, encoding="utf-8").read()
    if ML_MARK in s:
        return False
    _, en, ml, _, _ = SVC[slug]
    para = (f"നോർത്ത് പറവൂരിലും അടുത്ത സ്ഥലങ്ങളിലും {ml} സേവനം ആവശ്യമുണ്ടോ? "
            "FixMate Kerala പരിശീലനം ലഭിച്ച ജോലിക്കാരെ നിങ്ങളുടെ വീട്ടിലേക്ക് അയയ്ക്കുന്നു. "
            "ജോലി തുടങ്ങുന്നതിന് മുമ്പ് തന്നെ നിരക്ക് അറിയിക്കും. ₹49 മുതൽ നിരക്കുകൾ. "
            f"വിളിക്കുക അല്ലെങ്കിൽ WhatsApp ചെയ്യുക: {TEL_SHOW}.")
    faqs = [
        ("ഏതൊക്കെ സ്ഥലങ്ങളിൽ സേവനം ലഭിക്കും?", f"{ML_AREAS} എന്നിവിടങ്ങളിൽ സേവനം ലഭിക്കും. മറ്റു സ്ഥലങ്ങൾക്ക് വിളിച്ച് ചോദിക്കുക."),
        ("എങ്ങനെ ബുക്ക് ചെയ്യാം?", f"വെബ്സൈറ്റിൽ ഓൺലൈനായി ബുക്ക് ചെയ്യാം, അല്ലെങ്കിൽ {TEL_SHOW} എന്ന നമ്പറിൽ വിളിക്കുകയോ WhatsApp ചെയ്യുകയോ ചെയ്യാം. പ്രശ്നത്തിന്റെ ഫോട്ടോ അയച്ചാൽ കൂടുതൽ എളുപ്പമാകും."),
        ("സാധനങ്ങളുടെ വില നിരക്കിൽ ഉൾപ്പെടുമോ?", "നിരക്ക് ജോലിക്കൂലിക്ക് മാത്രമാണ്. ആവശ്യമായ സാധനങ്ങളും സ്പെയർ പാർട്സും കടയിലെ വിലയ്ക്ക് അധികമായി വരും."),
    ]
    faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    section = f"""{ML_MARK}
  <section>
    <h2>മലയാളത്തിൽ</h2>
    <div class="ml" style="background:#f6f7fb;border-radius:14px;padding:18px 20px;font-size:15.5px;line-height:1.8">{para}</div>
    <div style="margin-top:14px">{faq_html}</div>
  </section>

  <section>
    <h2>Questions people ask</h2>"""
    s = s.replace("<section>\n    <h2>Questions people ask</h2>", section, 1)
    # Areas chips become links
    s = s.replace("<li>North Paravur</li>", '<li><a href="/" style="text-decoration:none">North Paravur</a></li>', 1)
    for a, en_a, _ in AREAS:
        s = s.replace(f"<li>{en_a}</li>", f'<li><a href="/home-services-{a}" style="text-decoration:none">{en_a}</a></li>', 1)
    # Malayalam FAQ into schema
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    data = json.loads(m.group(1))
    for node in data["@graph"]:
        if node.get("@type") == "FAQPage":
            node["mainEntity"] += [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]
    s = s.replace(m.group(1), json.dumps(data, ensure_ascii=False), 1)
    # Footer links
    s = s.replace('<span>Home repairs in North Paravur, Kerala</span>',
                  '<span><a href="/areas">Areas we serve</a><a href="/blog/">Home tips</a>Home repairs in North Paravur, Kerala</span>', 1)
    s = re.sub(r"<!-- FixMate Kerala service page rev (\d+):[^>]*-->",
               lambda mm: f"<!-- FixMate Kerala service page rev {int(mm.group(1))+1}: Malayalam section, area links (rev {mm.group(1)} favicon) -->", s, 1)
    open(f, "w", encoding="utf-8").write(s)
    return True


def write_sitemap(extra):
    import datetime
    today = datetime.date.today().isoformat()
    urls = [("/", "1.0")] + [(f"/{s[0]}-north-paravur", "0.8") for s in SERVICES] + [(p, "0.7") for p in extra]
    body = "".join(f"  <url><loc>{BASE}{p}</loc><lastmod>{today}</lastmod><priority>{pr}</priority></url>\n" for p, pr in urls)
    open(f"{REPO}/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + body + "</urlset>\n")


if __name__ == "__main__":
    import os
    pages = []
    for i, (slug, en, ml) in enumerate(AREAS):
        pages.append(area_page(i, slug, en, ml))
    pages.append(areas_index())
    for a in ARTICLES:
        pages.append(article_page(*a))
    pages.append(blog_index())
    os.makedirs(f"{REPO}/blog", exist_ok=True)
    for path, content in pages:
        fn = "blog/index.html" if path == "/blog/" else path.lstrip("/") + ".html"
        open(f"{REPO}/{fn}", "w", encoding="utf-8").write(content)
    n = sum(add_malayalam(s[0]) for s in SERVICES)
    write_sitemap([p for p, _ in pages])
    print(len(pages), "pages written;", n, "service pages updated")
    print("\n".join(p for p, _ in pages))
