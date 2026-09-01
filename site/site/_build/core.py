# -*- coding: utf-8 -*-
import io, os

B = "/home/claude/build"

SPACES = [
    ("THAMARA",  "The Grand Hall",   "The lotus.",        "750+",
     "The largest of the three halls, and the room a wedding is built around. Ceremony, reception, or both."),
    ("AMBAL",    "The Lily Hall",    "The water lily.",   "500+",
     "A mid-scale hall with its own entrance and pre-function foyer, so it can run entirely independently of the others."),
    ("MANJADI",  "The Private Hall",  "The red seed children collect.", "250+",
     "The most intimate of the halls \u2014 for engagements, smaller receptions, board meetings and the functions that want a quieter room."),
]
OUTDOOR = [
    ("HARITHAM", "The Lawn",         "Greenery.",         "600+",
     "Open lawn under the sky \u2014 for the ceremony, the cocktail hour, or a reception that wants no ceiling at all.", "Open air"),
    ("POYKA",    "The Garden Lounge","The pond.",         "50+",
     "A shaded terrace set beside the fish pond, back from the main halls \u2014 for guests who want to step away, or a small gathering before the main event.", "Open air, by the fish pond"),
]

NAV = [("celebrations.html", "Celebrations"), ("corporate.html", "Corporate"),
       ("partners.html", "Partners"), ("spaces.html", "Spaces"),
       ("gallery.html", "Gallery"), ("visit.html", "Visit")]


def head(title, desc):
    return u"""<!DOCTYPE html>
<html lang="en">
<script>document.documentElement.classList.add('js');</script>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<meta name="description" content="%s">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400;500;600&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
""" % (title, desc)


def header(here=""):
    def cls(h):
        return u' class="active"' if h == here else u''
    links = u"\n".join([u'      <a href="%s"%s>%s</a>' % (h, cls(h), t) for h, t in NAV])
    dlinks = u"\n".join([u'  <a href="%s"%s>%s</a>' % (h, cls(h), t) for h, t in NAV])
    return u"""
<header id="siteHeader">
  <div class="wrap">
    <a href="index.html" class="brand">river walk <small>convention centre</small></a>
    <nav class="links">
%s
      <a href="#enquire" class="nav-cta">Enquire</a>
    </nav>
    <button class="menu-btn" id="menuBtn" aria-label="Open menu">&#9776;</button>
  </div>
</header>

<div class="drawer" id="drawer">
  <button class="close" id="closeDrawer" aria-label="Close menu">&times;</button>
%s
  <a href="#enquire">Enquire</a>
</div>

<div id="top"></div>
""" % (links, dlinks)


def hero(img, alt, eyebrow, h1, lede, cta1, cta1_href, cta2, cta2_href):
    return u"""
<section class="hero" style="padding:0;">
  <img src="%s" alt="%s">
  <div class="scrim"></div>
  <div class="hero-content wrap">
    <div class="eyebrow">%s</div>
    <h1>%s</h1>
    <p class="lede">%s</p>
    <div class="hero-ctas">
      <a href="%s" class="btn btn-primary">%s</a>
      <a href="%s" class="btn btn-ghost">%s</a>
    </div>
  </div>
  <div class="scroll-cue">SCROLL</div>
</section>
""" % (img, alt, eyebrow, h1, lede, cta1_href, cta1, cta2_href, cta2)


def divider():
    return u"""
<svg class="river-divider" viewBox="0 0 1240 56" preserveAspectRatio="none" aria-hidden="true">
  <path d="M0,28 C120,4 220,52 340,30 C460,8 540,50 660,28 C780,6 860,50 980,28 C1080,10 1160,40 1240,26"/>
</svg>
"""


def stats(items):
    cells = u"".join([u"""    <div>
      <div class="stat-num">%s</div>
      <div class="stat-label">%s</div>
    </div>
""" % (n, l) for n, l in items])
    return u'\n<section class="stats">\n  <div class="wrap">\n%s  </div>\n</section>\n' % cells


MONO = ("font-style:normal; font-family:'JetBrains Mono',monospace; font-size:0.62rem; "
        "letter-spacing:.1em; text-transform:uppercase; color:rgba(246,241,230,0.5); vertical-align:middle;")
WAVE = ('<svg class="hall-svg" width="90" height="20" viewBox="0 0 90 20"><path d="M0,10 C15,0 25,20 40,10 '
        'C55,0 65,20 80,10 L90,10" fill="none" stroke="#d9b169" stroke-width="1.4"/></svg>')


def space_card(idx, total, name, gloss, meaning, cap, body, meta2, capunit="Seated Pax"):
    return u"""      <div class="hall-card">
        <span class="hall-index">%02d / %02d</span>
        <h3>%s <span style="%s">%s</span></h3>
        <p><em>%s</em> %s</p>
        %s
        <div class="hall-meta">
          <div><span class="n">%s</span><span class="l">%s</span></div>
          <div><span class="n">%s</span><span class="l">&nbsp;</span></div>
        </div>
      </div>
""" % (idx, total, name, MONO, gloss, meaning, body, WAVE, cap, capunit, meta2)


def spaces_section(intro_h2, intro_p):
    cards = u""
    n = 0
    for name, gloss, meaning, cap, body in SPACES:
        n += 1
        cards += space_card(n, 5, name, gloss, meaning, cap, body, "Ground level")
    for name, gloss, meaning, cap, body, meta2 in OUTDOOR:
        n += 1
        unit = "Seated Pax" if name == "POYKA" else "Standing"
        cards += space_card(n, 5, name, gloss, meaning, cap, body, meta2, unit)
    return u"""
<section id="spaces" class="halls-section">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">The Spaces</div>
      <h2 class="serif">%s</h2>
      <p>%s</p>
    </div>
  </div>
  <div class="wrap" style="padding:0 40px;">
    <div class="halls-grid reveal">
%s    </div>
  </div>
</section>
""" % (intro_h2, intro_p, cards)


SET_CELEBRATIONS = [
    (u"g-1", u"img/hall-thamara.webp", u"Thamara dressed for a reception \u2014 image to come"),
    (u"g-2", u"img/hall-haritham.webp", u"Haritham under evening light \u2014 image to come"),
    (u"",    u"img/hall-kulir.webp",    u"Poyka, the terrace at the fish pond \u2014 image to come"),
    (u"",    u"img/about.webp",         u"Arrival, on the day \u2014 image to come"),
]
SET_CONFERENCES = [
    (u"g-1", u"img/hall-ambal.webp",    u"Ambal in theatre configuration \u2014 image to come"),
    (u"g-2", u"img/hall-manjadi.webp",  u"Manjadi set for a board meeting \u2014 image to come"),
    (u"",    u"img/grounds-path.webp",  u"Coach and car parking \u2014 image to come"),
    (u"",    u"img/grounds-facade.webp", u"The separate conference entrance \u2014 image to come"),
]


def _gal_figs(items):
    out = u""
    for cls, src, cap in items:
        c = u' class="%s"' % cls if cls else u""
        out += (u'      <figure%s><img src="%s" alt="Architectural visualisation of River Walk '
                u'Convention Centre">\n        <figcaption>%s</figcaption></figure>\n') % (c, src, cap)
    return out


def gallery(note=True):
    n = (u'      <p>The centre is still being built. These are architectural visualisations '
         u'\u2014 photographs will replace them as each space is finished.</p>\n') if note else u""
    return u"""
<section id="gallery">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Gallery</div>
      <h2 class="serif">A closer <em>walk</em> through.</h2>
%s    </div>
    <div class="gal-toggle reveal" data-gallery>
      <button type="button" class="gal-tab is-on" data-tab="celebrations">Celebrations</button>
      <button type="button" class="gal-tab" data-tab="conferences">Conferences</button>
    </div>
    <p class="gal-note reveal">The same five spaces, set up two ways. Captions mark the shot each frame will hold &mdash; the images below are stand-ins from the arrival visualisations.</p>
    <div class="gallery-grid reveal" data-panel="celebrations">
%s    </div>
    <div class="gallery-grid reveal" data-panel="conferences" hidden>
%s    </div>
  </div>
</section>
""" % (n, _gal_figs(SET_CELEBRATIONS), _gal_figs(SET_CONFERENCES))


def enquiry(preselect, heading, sub):
    opts = [u"All five spaces"]
    for name, gloss, _, _, _ in SPACES:
        opts.append(u"%s \u2014 %s" % (name.title(), gloss))
    for name, gloss, _, _, _, _ in OUTDOOR:
        opts.append(u"%s \u2014 %s" % (name.title(), gloss))
    opts.append(u"Not sure yet")
    o = u"\n".join([u'          <option%s>%s</option>' %
                    (u' selected' if x == preselect else u'', x) for x in opts])
    return u"""
<section id="enquire" class="enquiry">
  <div class="wrap enq-grid">
    <div class="enq-info reveal">
      <div class="eyebrow" style="color:var(--terracotta); margin-bottom:14px;">Enquire</div>
      <h2 class="serif">%s</h2>
      <p>%s</p>
      <div class="enq-contact">
        <div>
          <div class="l">Address</div>
          <div class="v">River Walk Convention Centre, Kuttanellur,<br>Thrissur, Kerala &mdash; on NH 544 (Kochi&ndash;Palakkad)</div>
        </div>
        <div>
          <div class="l">Phone</div>
          <div class="v">+91 XXXXX XXXXX</div>
        </div>
        <div>
          <div class="l">Email</div>
          <div class="v">events@riverwalkcentre.in</div>
        </div>
        <div>
          <div class="l">Hours</div>
          <div class="v">9:30 AM &ndash; 6:30 PM, all days</div>
        </div>
      </div>
    </div>
    <form class="reveal" onsubmit="event.preventDefault(); this.querySelector('.submit-btn').textContent='Thank you \u2014 we will be in touch';">
      <div class="form-row">
        <div class="field"><label for="name">Full name</label><input id="name" type="text" required placeholder="Your name"></div>
        <div class="field"><label for="phone">Phone</label><input id="phone" type="tel" required placeholder="+91"></div>
      </div>
      <div class="form-row">
        <div class="field"><label for="date">Event date</label><input id="date" type="date"></div>
        <div class="field"><label for="pax">Expected guests</label><input id="pax" type="number" placeholder="e.g. 500"></div>
      </div>
      <div class="field">
        <label for="hall">Interested in</label>
        <select id="hall">
%s
        </select>
      </div>
      <div class="field">
        <label for="msg">Tell us about the event</label>
        <textarea id="msg" placeholder="Wedding, reception, anniversary, conference, exhibition&hellip;"></textarea>
      </div>
      <button type="submit" class="submit-btn">Send enquiry</button>
    </form>
  </div>
</section>
""" % (heading, sub, o)


def footer():
    return u"""
<footer>
  <div class="wrap">
    <div class="foot-top">
      <div class="foot-brand">
        <a href="index.html" class="brand">river walk <small>convention centre</small></a>
        <p>A riverside convention centre at Kuttanellur, outside Thrissur &mdash; on the Kochi&ndash;Palakkad highway.</p>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="celebrations.html">Celebrations</a></li>
          <li><a href="corporate.html">Corporate events</a></li>
          <li><a href="partners.html">Partners</a></li>
          <li><a href="spaces.html">The five spaces</a></li>
          <li><a href="spaces.html#grounds">The grounds</a></li>
          <li><a href="gallery.html">Gallery</a></li>
        </ul>
      </div>
      <div>
        <h4>Visit</h4>
        <ul>
          <li><a href="visit.html">Location &amp; access</a></li>
          <li><a href="#enquire">Enquire</a></li>
          <li><a href="tel:+91XXXXXXXXXX">+91 XXXXX XXXXX</a></li>
        </ul>
      </div>
      <div>
        <h4>Follow</h4>
        <ul>
          <li><a href="#">Instagram</a></li>
          <li><a href="#">Facebook</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; River Walk Convention Centre, Kuttanellur. All rights reserved.</span>
      <span>3D visualisation &mdash; Unique Garden Decor</span>
    </div>
  </div>
</footer>

<a class="wa" href="https://wa.me/91XXXXXXXXXX" target="_blank" rel="noopener" aria-label="Message River Walk on WhatsApp">
  <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.61-.92-2.21-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.06 2.87 1.21 3.07.15.2 2.09 3.2 5.07 4.49.71.3 1.26.49 1.69.63.71.22 1.36.19 1.87.12.57-.09 1.76-.72 2.01-1.41.25-.7.25-1.29.17-1.42-.07-.13-.27-.2-.57-.35zM12.04 21.5h-.01a9.4 9.4 0 01-4.79-1.31l-.34-.2-3.56.93.95-3.47-.22-.36a9.37 9.37 0 01-1.44-5.01c0-5.18 4.23-9.4 9.42-9.4a9.36 9.36 0 016.65 2.76 9.32 9.32 0 012.75 6.65c0 5.18-4.23 9.41-9.41 9.41zm8-17.42A11.32 11.32 0 0012.04.75C5.8.75.73 5.82.73 12.05c0 1.99.52 3.94 1.51 5.65L.64 23.25l5.69-1.49a11.3 11.3 0 005.71 1.53h.01c6.23 0 11.3-5.07 11.31-11.3a11.25 11.25 0 00-3.31-8z"/></svg>
</a>

<script>
  const header = document.getElementById('siteHeader');
  window.addEventListener('scroll', () => { header.classList.toggle('solid', window.scrollY > 60); });
  const drawer = document.getElementById('drawer');
  document.getElementById('menuBtn').addEventListener('click', () => drawer.classList.add('open'));
  document.getElementById('closeDrawer').addEventListener('click', () => drawer.classList.remove('open'));
  drawer.querySelectorAll('a').forEach(a => a.addEventListener('click', () => drawer.classList.remove('open')));
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if(e.isIntersecting){
        e.target.classList.add(e.target.classList.contains('river-divider') ? 'drawn' : 'in');
        io.unobserve(e.target);
      }
    });
  }, {threshold:0.2});
  document.querySelectorAll('.reveal, .river-divider').forEach(el => io.observe(el));

  // testimonials carousel
  document.querySelectorAll('[data-testimonials]').forEach(car => {
    const track = car.querySelector('.tcar-track');
    const slides = car.querySelectorAll('.tslide');
    const idxOut = car.querySelector('[data-idx]');
    let i = 0;
    const go = n => {
      i = (n + slides.length) % slides.length;
      track.style.transform = 'translateX(' + (-i * 100) + '%)';
      slides.forEach((s, k) => s.setAttribute('aria-hidden', k === i ? 'false' : 'true'));
      if (idxOut) idxOut.textContent = i + 1;
    };
    car.querySelector('[data-prev]').addEventListener('click', () => go(i - 1));
    car.querySelector('[data-next]').addEventListener('click', () => go(i + 1));
    car.addEventListener('keydown', e => {
      if (e.key === 'ArrowLeft') go(i - 1);
      if (e.key === 'ArrowRight') go(i + 1);
    });
    go(0);
  });

  // gallery celebrations / conferences toggle
  document.querySelectorAll('[data-gallery]').forEach(tabs => {
    const scope = tabs.parentElement;
    tabs.querySelectorAll('.gal-tab').forEach(btn => {
      btn.addEventListener('click', () => {
        const want = btn.dataset.tab;
        tabs.querySelectorAll('.gal-tab').forEach(b => b.classList.toggle('is-on', b === btn));
        scope.querySelectorAll('[data-panel]').forEach(p => { p.hidden = p.dataset.panel !== want; });
      });
    });
  });
</script>

</body>
</html>
"""




def testimonials():
    return u"""
<section class="testimonials">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="eyebrow">Testimonials</div>
      <h2 class="serif">In their <em>own words</em>.</h2>
    </div>
    <div class="tcar reveal" data-testimonials tabindex="0" aria-roledescription="carousel" aria-label="Client testimonials">
      <div class="tcar-viewport">
        <div class="tcar-track">
        <blockquote class="tslide">
          <p>&ldquo;Placeholder &mdash; two or three sentences from the family, in their own words, about how the day ran and what the property felt like. Replace before launch.&rdquo;</p>
          <cite><span class="tname">Name to come</span><span class="tmeta">Wedding &middot; Thamara &amp; Haritham &middot; 2026</span></cite>
        </blockquote>
        <blockquote class="tslide">
          <p>&ldquo;Placeholder &mdash; a short quote from a corporate client about the venue, the access and how the breaks worked. Replace before launch.&rdquo;</p>
          <cite><span class="tname">Name to come</span><span class="tmeta">Dealer meet &middot; Ambal &middot; 2026</span></cite>
        </blockquote>
        <blockquote class="tslide">
          <p>&ldquo;Placeholder &mdash; a line from a wedding planner or caterer about working here. Vendor voices reassure families as much as client ones do. Replace before launch.&rdquo;</p>
          <cite><span class="tname">Name to come</span><span class="tmeta">Wedding planner &middot; Thrissur</span></cite>
        </blockquote>
        <blockquote class="tslide">
          <p>&ldquo;Placeholder &mdash; a quote from a family who travelled in from abroad, about arrival, logistics and the grounds. Replace before launch.&rdquo;</p>
          <cite><span class="tname">Name to come</span><span class="tmeta">Reception &middot; Haritham &middot; 2026</span></cite>
        </blockquote>
        </div>
      </div>
      <div class="tcar-nav">
        <button class="tcar-btn" data-prev type="button" aria-label="Previous testimonial">&larr;</button>
        <span class="tcar-count"><span data-idx>1</span>&thinsp;/&thinsp;4</span>
        <button class="tcar-btn" data-next type="button" aria-label="Next testimonial">&rarr;</button>
      </div>
    </div>
  </div>
</section>
"""


def closing(preselect, heading, sub):
    return testimonials() + enquiry(preselect, heading, sub)
