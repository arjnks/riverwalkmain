# -*- coding: utf-8 -*-
import io, os
HERE = os.path.dirname(os.path.abspath(__file__))
exec(io.open(os.path.join(HERE, "core.py"), encoding="utf-8").read())

about = u"""
<section id="about">
  <div class="wrap about">
    <div class="about-copy reveal">
      <div class="section-head" style="margin-bottom:30px;">
        <div class="eyebrow">About the venue</div>
        <h2 class="serif">Contemporary in structure, <em>Kerala</em> at heart.</h2>
      </div>
      <p>Most days blur into the next. Then once in a while, something matters enough to bring everyone into one place &mdash; a wedding, a fiftieth anniversary, a launch a whole company has worked toward for a year. Those are the days people remember. River Walk exists for those days.</p>
      <p>A small river runs along the front of the property. Mango groves and coconut palms dot the landscape. Paddy fields surround you on every side. The air smells like rain and earth.</p>
      <p>It&rsquo;s far enough out for the quiet. And close enough to reach.</p>
      <div class="hero-ctas" style="margin-top:8px;">
        <a href="visit.html" class="btn btn-dark">Getting here</a>
      </div>
    </div>
    <div class="about-media reveal">
      <img src="img/about.webp" alt="Covered driveway and porte-coch&egrave;re at River Walk Convention Centre">
      <div class="about-tag">
        <div class="stat-num">21,000<span style="font-size:1rem;">&nbsp;sqft</span></div>
        <div class="stat-label">Built + landscaped footprint, Kuttanellur</div>
      </div>
    </div>
  </div>
</section>
"""

doors = u"""
<section id="doors">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="eyebrow">Two kinds of gathering</div>
      <h2 class="serif">Space for every kind of gathering.</h2>
      <p>Five spaces, one river, two very different ways to use them.</p>
    </div>
    <div class="doors reveal">
      <a class="door" href="celebrations.html">
        <img src="img/hall-thamara.webp" alt="Thamara hall dressed for a wedding reception">
        <div class="door-scrim"></div>
        <div class="door-inner">
          <div class="eyebrow">Celebrations</div>
          <h3>Celebrate a life milestone.</h3>
          <p>Weddings, receptions, anniversaries, engagements, christenings&hellip;</p>
          <span class="door-cta">&rarr;</span>
        </div>
      </a>
      <a class="door" href="corporate.html">
        <img src="img/hall-ambal.webp" alt="Ambal hall set up in theatre configuration for a conference">
        <div class="door-scrim"></div>
        <div class="door-inner">
          <div class="eyebrow">Corporate events</div>
          <h3>Host a corporate milestone.</h3>
          <p>Conferences, exhibitions, launches, AGMs, offsites&hellip;</p>
          <span class="door-cta">&rarr;</span>
        </div>
      </a>
    </div>
  </div>
</section>
"""

grounds = u"""
<section id="grounds">
  <div class="garden-feature">
    <div class="top">
      <div class="copy-col">
        <div class="copy-col-inner reveal">
          <div class="eyebrow" style="color:var(--terracotta); margin-bottom:16px;">The grounds</div>
          <h2 class="serif" style="font-size:clamp(1.8rem,3vw,2.5rem); line-height:1.15; margin-bottom:20px;">Green, layered, <em style="color:var(--moss);">unhurried</em>.</h2>
          <p style="color:rgba(28,42,32,0.75); margin-bottom:16px;">Mango and coconut for canopy, flowering planting at eye level, paddy stretching out past the boundary on every side, and the river along the front. The grounds are laid out as a series of rooms without walls &mdash; a court for cocktails, a lawn for the ceremony, a shaded terrace at the pond for guests who want to step away, a rustic table by the mango grove for the intimate family dinner that runs late.</p>
          <p style="color:rgba(28,42,32,0.75);">Outdoor space built to be used, not just photographed.</p>
        </div>
      </div>
      <img src="img/grounds-path.webp" alt="Lantern-lit path through the grounds at River Walk">
    </div>
  </div>
  <div class="garden-strip">
    <figure><img src="img/grounds-facade.webp" alt="Hall facade opening onto the lawn at dusk"><figcaption>The halls open onto Haritham</figcaption></figure>
    <figure><img src="img/hall-kulir.webp" alt="Shaded terrace beside the fish pond"><figcaption>Poyka, the terrace at the fish pond</figcaption></figure>
  </div>
</section>
"""

location = u"""
<section id="location" class="location">
  <div class="wrap loc-grid">
    <div class="reveal">
      <div class="eyebrow">Location &amp; access</div>
      <h2 class="serif">Twenty minutes out.<br>Not a minute further.</h2>
      <p>The whole point of River Walk is that it feels far from town without being far from town. It sits on the highway corridor linking Kochi and Palakkad, so guests come in from across central Kerala without a detour &mdash; and families flying in land at Nedumbassery and are here inside the hour.</p>
      <ul class="loc-list">
        <li><span class="dot"></span> 300 m off the Kochi&ndash;Palakkad highway (NH 544), Kuttanellur</li>
        <li><span class="dot"></span> Onsite parking for cars and coaches &mdash; no offsite shuttling</li>
        <li><span class="dot"></span> Covered drop-off and porte-coch&egrave;re at the main entrance</li>
        <li><span class="dot"></span> Easy reach from Thrissur town and the wider Kochi&ndash;Palakkad belt</li>
        <li><span class="dot"></span> Under an hour from Nedumbassery (Cochin International Airport)</li>
      </ul>
      <div class="hero-ctas" style="margin-top:34px;">
        <a href="https://www.google.com/maps/search/Kuttanellur,+Thrissur" target="_blank" rel="noopener" class="btn btn-ghost">Open in Google Maps</a>
      </div>
    </div>
    <div class="map-frame reveal">
      <iframe src="https://maps.google.com/maps?q=Kuttanellur%2C%20Thrissur%2C%20Kerala&t=&z=13&output=embed" loading="lazy" allowfullscreen title="Map showing Kuttanellur, Thrissur"></iframe>
    </div>
  </div>
</section>
"""

routes = u"""
<section id="routes">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="eyebrow">Getting here</div>
      <h2 class="serif">However your guests <em>arrive</em>.</h2>
      <p>Approximate journey times, to be confirmed against the final approach road.</p>
    </div>
    <div class="spots reveal">
      <div class="spot"><h4>From Thrissur town</h4><p>Straight out along the Kochi&ndash;Palakkad highway. No town traffic once you are past the Round.</p></div>
      <div class="spot"><h4>From Nedumbassery</h4><p>Under an hour, almost entirely on the highway. Land in the morning, be here for lunch.</p></div>
      <div class="spot"><h4>From Thrissur railway station</h4><p>A short run out of town for guests arriving by train from Chennai, Bengaluru or the north.</p></div>
      <div class="spot"><h4>Parking</h4><p>Cars and coaches on the property, with a covered drop-off at the door. Nobody parks on the highway.</p></div>
    </div>
  </div>
</section>
"""

tour = u"""
<section id="tour" class="location">
  <div class="wrap">
    <div class="section-head reveal" style="max-width:700px;">
      <div class="eyebrow" style="color:var(--brass-light);">Virtual tour</div>
      <h2 class="serif">Walk it from <em style="color:var(--brass-light);">wherever you are</em>.</h2>
      <p style="color:rgba(246,241,230,0.72);">A 360&deg; walkthrough of all five spaces and the grounds, in daylight and after dark. Coming as each space is completed.</p>
    </div>
    <div class="tour-frame reveal">
      <span>360&deg; tour &mdash; to be embedded</span>
    </div>
  </div>
</section>
"""

ENQ_SUB = (u"Tell us the date, the headcount and which space you have in mind, and we&rsquo;ll "
           u"come back with availability and a time to walk the property. Chai is on us.")
ENQ_H = u"Come and see it.<br>Bring the family."

# ---------------- index ----------------
index = (head(u"River Walk Convention Centre, Thrissur \u2014 Weddings &amp; Corporate Events, Kuttanellur",
              u"A riverside convention centre outside Thrissur \u2014 five spaces, mango groves and paddy fields, up to 1,500 guests. Kuttanellur, on the Kochi\u2013Palakkad highway (NH 544).")
         + header()
         + hero(u"img/hero.webp", u"River Walk Convention Centre entrance walkway at dusk, lit by garden lanterns",
                u"Kuttanellur, Thrissur &nbsp;\u00b7&nbsp; NH 544",
                u"Gather your people.",
                u"In the heart of nature. Minutes from town. Thrissur&rsquo;s largest riverside venue for celebrations and gatherings.",
                u"Enquire", u"#enquire", u"Celebrations or corporate?", u"#doors")
         + divider() + about + doors + divider()
         + closing(u"All five spaces", ENQ_H, ENQ_SUB)
         + footer())

# ---------------- spaces ----------------
spaces = (head(u"The Five Spaces \u2014 River Walk Convention Centre, Thrissur",
               u"Thamara, Ambal, Manjadi, Haritham and Poyka \u2014 three halls, a lawn and a garden lounge at River Walk, Kuttanellur, Thrissur.")
          + header(u"spaces.html")
          + hero(u"img/hall-haritham.webp", u"Haritham lawn at River Walk, lit for an evening event",
                 u"The spaces", u"Three halls, a lawn,<br>trees, water, and sky.",
                 u"All three halls open onto the lawn, so indoors and outdoors can run as one.",
                 u"Enquire about a date", u"#enquire", u"See the grounds", u"#grounds")
          + spaces_section(u"Five spaces, <em>one</em> river.",
                           u"Capacities below are seated for dining. Theatre, classroom and exhibition-booth configurations are on the corporate page. Take a single space, or take all five.")
          + grounds + divider()
          + closing(u"All five spaces", ENQ_H, ENQ_SUB)
          + footer())

# ---------------- celebrations ----------------
flow = u"""
<section id="flow">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="eyebrow">How a wedding moves</div>
      <h2 class="serif">A wedding doesn&rsquo;t happen <em>in one room</em>.</h2>
      <p>An Indian wedding moves. Here is one way the property carries it &mdash; though families rearrange this constantly, and that is the point of booking all five.</p>
    </div>
    <div class="flow reveal">
      <div class="flow-row"><span class="flow-ev">Mehendi &amp; the manjal kuri</span><span class="flow-sp">Poyka, then Haritham as the light goes</span></div>
      <div class="flow-row"><span class="flow-ev">Sangeet &amp; dinner under the trees</span><span class="flow-sp">Manjadi, opening out to the mango grove</span></div>
      <div class="flow-row"><span class="flow-ev">The ceremony</span><span class="flow-sp">Thamara, or Haritham under open sky</span></div>
      <div class="flow-row"><span class="flow-ev">Sadya &amp; the family lunch</span><span class="flow-sp">Ambal, with its own entrance</span></div>
      <div class="flow-row"><span class="flow-ev">Reception</span><span class="flow-sp">Thamara, opening onto the lawn</span></div>
      <div class="flow-row"><span class="flow-ev">Portraits &amp; the send-off</span><span class="flow-sp">The river steps, the pond walkway, the mango grove</span></div>
    </div>
    <div class="hero-ctas" style="margin-top:40px;">
      <a href="spaces.html" class="btn btn-dark">See all five spaces</a>
    </div>
  </div>
</section>
"""

celebrations = (head(u"Weddings &amp; Celebrations \u2014 River Walk Convention Centre, Thrissur",
                     u"A riverside wedding venue outside Thrissur. Five spaces, and room for up to 1,500 guests.")
                + header(u"celebrations.html")
                + hero(u"img/hall-thamara.webp", u"Thamara hall dressed for a wedding reception, opening onto the lawn",
                       u"Celebrations at River Walk",
                       u"Everyone you love,<br>in one place.",
                       u"Weddings, receptions, anniversaries, engagements, christenings&hellip;",
                       u"Enquire about a date", u"#enquire", u"How a wedding moves here", u"#flow")
                + divider()
                + u"""
<section id="why">
  <div class="wrap">
    <div class="section-head reveal" style="max-width:720px;">
      <div class="eyebrow">Why here</div>
      <h2 class="serif">The days you <em>keep</em>.</h2>
      <p>We live fast and we live scattered. Then once in a while everyone comes home &mdash; there is a date on the calendar, a house full of noise, a morning nobody wants to end. Those are the days people remember for thirty years, and they deserve a place that rises to the occasion.</p>
    </div>
  </div>
</section>
"""
                + flow + divider()
                + closing(u"All five spaces", ENQ_H, ENQ_SUB)
                + footer())

# ---------------- corporate ----------------
corporate = (head(u"Corporate Events, Conferences &amp; Exhibitions \u2014 River Walk, Thrissur",
                  u"21,000 sq ft of event space on NH 544 outside Thrissur. Dealer meets, product launches, trade exhibitions, AGMs and company offsites for up to 1,500 delegates.")
             + header(u"corporate.html")
             + hero(u"img/hall-ambal.webp", u"Ambal hall set up in theatre configuration for a conference",
                    u"Corporate events at River Walk",
                    u"Everything a convention<br>centre should have. And a river.",
                    u"Conferences, exhibitions, launches, AGMs, and offsites \u2014 21,000 sq ft on the Kochi\u2013Palakkad highway, under an hour from Nedumbassery.",
                    u"Request the fact sheet", u"#enquire", u"See the specifications", u"#specs")
             + stats([(u"21,000", u"Sq. ft. of covered<br>&amp; open event space"),
                      (u"1,500", u"Delegates across<br>the property"),
                      (u'300<span style="font-size:1.4rem;">&nbsp;m</span>', u"To NH 544 &mdash; loading<br>access for exhibition build"),
                      (u'50<span style="font-size:1.4rem;">&nbsp;min</span>', u"From Nedumbassery airport,<br>direct on the highway")])
             + divider()
             + u"""
<section id="specs" class="location">
  <div class="wrap">
    <div class="section-head reveal" style="max-width:760px;">
      <div class="eyebrow" style="color:var(--brass-light);">Specifications</div>
      <h2 class="serif">What planners actually <em style="color:var(--brass-light);">ask for</em>.</h2>
      <p style="color:rgba(246,241,230,0.72); max-width:620px;">The floor, the power, the access and the parking. If a number you need isn&rsquo;t here, ask and we&rsquo;ll send it that day.</p>
    </div>
    <div class="conf-grid">
      <div class="reveal">
        <ul class="loc-list" style="margin-top:0;">
          <li><span class="dot"></span> Three halls, combinable, up to 1,500 delegates across the property</li>
          <li><span class="dot"></span> Truck and loading access for exhibition build</li>
          <li><span class="dot"></span> Power backup on every circuit; dedicated exhibitor power drops</li>
          <li><span class="dot"></span> Breakout rooms and pre-function foyers on each hall</li>
          <li><span class="dot"></span> Separate entrance &mdash; a conference never shares a door with a wedding</li>
          <li><span class="dot"></span> Parking for cars and coaches, with no offsite shuttling</li>
          <li><span class="dot"></span> GST-compliant invoicing and a single point of contact</li>
        </ul>
      </div>
      <div class="reveal">
        <p style="color:rgba(246,241,230,0.78);">When the session breaks, people walk out under the mango trees instead of into a corridor. Attendance holds through the afternoon, the conversations run longer and deeper, the work gets done more effortlessly.</p>
        <div class="hero-ctas" style="margin-top:30px;">
          <a href="spaces.html" class="btn btn-primary">See the five spaces</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""
             + u"""
<section id="types">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="eyebrow">What we host</div>
      <h2 class="serif">Not only <em>conferences</em>.</h2>
    </div>
    <div class="spots reveal">
      <div class="spot"><h4>Dealer meets</h4><p>Highway access, coach parking and a hall that seats the whole network at once.</p></div>
      <div class="spot"><h4>Exhibitions</h4><p>Column-free floor, loading access to the hall door, and exhibitor power drops.</p></div>
      <div class="spot"><h4>Launches</h4><p>Blackout capability, stage and AV, and grounds that photograph well for press.</p></div>
      <div class="spot"><h4>Offsites &amp; AGMs</h4><p>Breakouts indoors, the lawn and the river for everything between sessions.</p></div>
    </div>
  </div>
</section>
"""
             + closing(u"Not sure yet", u"Tell us what you&rsquo;re<br>planning.",
                       u"Send the dates, the delegate count and the format, and we&rsquo;ll come back with availability, the fact sheet and a quote.")
             + footer())

# ---------------- gallery ----------------
gallery_page = (head(u"Gallery &amp; Virtual Tour \u2014 River Walk Convention Centre, Thrissur",
                     u"Photographs, architectural visualisations and a 360-degree virtual tour of River Walk Convention Centre, Kuttanellur, Thrissur.")
                + header(u"gallery.html")
                + hero(u"img/grounds-facade.webp", u"Hall facade opening onto the lawn at dusk",
                       u"Gallery", u"A closer walk<br>through.",
                       u"The centre is still being built. These are architectural visualisations &mdash; photographs will replace them as each space is finished.",
                       u"Enquire about a date", u"#enquire", u"Virtual tour", u"#tour")
                + gallery(note=False) + tour
                + closing(u"All five spaces", ENQ_H, ENQ_SUB)
                + footer())

# ---------------- visit ----------------
visit = (head(u"Visit Us \u2014 River Walk Convention Centre, Kuttanellur, Thrissur",
              u"River Walk Convention Centre, Kuttanellur, Thrissur \u2014 on NH 544, the Kochi\u2013Palakkad highway, under an hour from Nedumbassery airport.")
         + header(u"visit.html")
         + location + routes + divider()
         + closing(u"All five spaces", ENQ_H, ENQ_SUB)
         + footer())


# ---------------- partners ----------------
PARTNER_CATS = [
 (u"Wedding planners", u"Placeholder \u2014 the planners we work with regularly, and what each is known for."),
 (u"Caterers", u"Placeholder \u2014 empanelled kitchens, plus a note that families may bring their own."),
 (u"Decor &amp; floral", u"Placeholder \u2014 decorators who know the halls and the lawn already."),
 (u"Photography &amp; film", u"Placeholder \u2014 photographers who know the property and the evening light."),
 (u"Music &amp; entertainment", u"Placeholder \u2014 melam, bands, DJs and sound crews who have worked the property."),
 (u"Mehendi &amp; beauty", u"Placeholder \u2014 artists and stylists who can work from the green rooms."),
 (u"Lighting &amp; AV", u"Placeholder \u2014 technical partners for both celebrations and conferences."),
 (u"Stay &amp; transport", u"Placeholder \u2014 nearby hotels, and coach operators for airport and station runs."),
]

partner_cards = u"".join([u"""      <div class="spot">
        <h4>%s</h4>
        <p>%s</p>
      </div>
""" % p for p in PARTNER_CATS])

partners = (head(u"Partners \u2014 River Walk Convention Centre, Thrissur",
                 u"The planners, caterers, decorators, photographers and technical partners we work with at River Walk Convention Centre, Kuttanellur, Thrissur.")
            + header(u"partners.html")
            + hero(u"img/hall-manjadi.webp", u"Manjadi hall set for a family function",
                   u"Partners", u"Every event runs on the people behind it.",
                   u"The planners, caterers, decorators and crews who know this property already \u2014 and how to work with anyone you would rather bring yourself.",
                   u"Enquire about a date", u"#enquire", u"Partner with us", u"#join")
            + divider()
            + u"""
<section id="directory">
  <div class="wrap">
    <div class="section-head reveal" style="max-width:720px;">
      <div class="eyebrow">Who we work with</div>
      <h2 class="serif">People who already know <em>the property</em>.</h2>
      <p>None of these lists are exclusive &mdash; you are free to bring your own.</p>
    </div>
    <div class="spots reveal">
""" + partner_cards + u"""    </div>
  </div>
</section>
"""
            + divider()
            + u"""
<section id="join" class="location">
  <div class="wrap">
    <div class="section-head reveal" style="max-width:760px;">
      <div class="eyebrow" style="color:var(--brass-light);">Partner with us</div>
      <h2 class="serif">Work at <em style="color:var(--brass-light);">River Walk</em>.</h2>
      <p style="color:rgba(246,241,230,0.72); max-width:620px;">We are building a panel of planners, caterers, decorators, photographers and technical crews for the seasons ahead. Placeholder copy \u2014 replace with the actual terms, the application process and what empanelment involves.</p>
    </div>
    <div class="conf-grid">
      <div class="reveal">
        <ul class="loc-list" style="margin-top:0;">
          <li><span class="dot"></span> Placeholder \u2014 what we look for in a partner</li>
          <li><span class="dot"></span> Placeholder \u2014 how empanelment works and what it costs</li>
          <li><span class="dot"></span> Placeholder \u2014 site access, load-in windows and storage</li>
          <li><span class="dot"></span> Placeholder \u2014 insurance and documentation required</li>
        </ul>
      </div>
      <div class="reveal">
        <p style="color:rgba(246,241,230,0.78);">Placeholder \u2014 a short paragraph on why vendors like working here: access, parking, load-in, power, and a team that answers the phone.</p>
        <div class="hero-ctas" style="margin-top:30px;">
          <a href="#enquire" class="btn btn-primary">Apply to join the panel</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""
            + closing(u"Not sure yet", u"Come and see it.<br>Bring the family.", ENQ_SUB)
            + footer())


B = os.path.abspath(os.path.join(HERE, ".."))
for fn, doc in [("index.html", index), ("celebrations.html", celebrations), ("corporate.html", corporate),
                ("spaces.html", spaces), ("gallery.html", gallery_page), ("visit.html", visit), ("partners.html", partners)]:
    io.open(os.path.join(B, fn), "w", encoding="utf-8").write(doc)
    print("%-20s %6d bytes" % (fn, len(doc)))
