import os

file_path = r"d:\internship work\LEO CONV CENTRE\riverwalk.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Hero
content = content.replace(
    "https://placehold.co/1920x1080/1a1a1a/c5a880?text=Riverwalk+Hero+Placeholder",
    "assets/river_walk_events-leo_group-pages-1_p1.webp"
)

# Feature 1
content = content.replace(
    "https://placehold.co/1920x1080/1a1a1a/c5a880?text=Estuary+Ballroom",
    "assets/river_walk_events-leo_group-pages-2_p1.webp"
)

# Marquee 1
content = content.replace(
    '<div class="marquee-img-wrap"><img src="https://placehold.co/600x400/1a1a1a/c5a880?text=Placeholder" alt="Space"></div>',
    '<div class="marquee-img-wrap"><img src="assets/river_walk_events-leo_group-pages-3_p1.webp" alt="Space"></div>'
)
# Marquee 2
content = content.replace(
    '<div class="marquee-img-wrap" style="border-radius: 0;"><img src="https://placehold.co/600x400/1a1a1a/c5a880?text=Placeholder" alt="Detail"></div>',
    '<div class="marquee-img-wrap" style="border-radius: 0;"><img src="assets/river_walk_events-leo_group-pages-4_p1.webp" alt="Detail"></div>'
)
# Marquee 3
content = content.replace(
    '<div class="marquee-img-wrap"><img src="https://placehold.co/600x400/1a1a1a/c5a880?text=Placeholder" alt="Ballroom"></div>',
    '<div class="marquee-img-wrap"><img src="assets/river_walk_events-leo_group-pages-5_p1.webp" alt="Ballroom"></div>'
)

# Feature 2
content = content.replace(
    "https://placehold.co/1920x1080/1a1a1a/c5a880?text=Architectural+Detail",
    "assets/river_walk_events-leo_group-pages-6_p1.webp"
)

# GSAP Cinematic
content = content.replace(
    "https://placehold.co/1920x1080/1a1a1a/c5a880?text=Cinematic+Sequence",
    "assets/river_walk_events-leo_group-pages-7_p1.webp"
)

# Booking
content = content.replace(
    "https://placehold.co/1920x1080/1a1a1a/c5a880?text=Reserve+Your+Date",
    "assets/river_walk_events-leo_group-pages-8_p1.webp"
)

# Masonry Gallery Images
content = content.replace(
    "https://placehold.co/800x800/1a1a1a/c5a880?text=Grand+Exterior",
    "assets/river_walk_events-leo_group-pages-1_p1.webp"
)
content = content.replace(
    "https://placehold.co/800x400/1a1a1a/c5a880?text=The+Ballroom",
    "assets/river_walk_events-leo_group-pages-2_p1.webp"
)
content = content.replace(
    "https://placehold.co/800x800/1a1a1a/c5a880?text=Crystal+Hall",
    "assets/river_walk_events-leo_group-pages-3_p1.webp"
)
content = content.replace(
    "https://placehold.co/400x400/1a1a1a/c5a880?text=Banquet+Lounge",
    "assets/river_walk_events-leo_group-pages-4_p1.webp"
)
content = content.replace(
    "https://placehold.co/400x400/1a1a1a/c5a880?text=Architectural+Detail",
    "assets/river_walk_events-leo_group-pages-6_p1.webp" # reused 6
)
content = content.replace(
    "https://placehold.co/800x400/1a1a1a/c5a880?text=Garden+Terrace",
    "assets/river_walk_events-leo_group-pages-7_p1.webp"
)
content = content.replace(
    "https://placehold.co/800x400/1a1a1a/c5a880?text=Evening+Setup",
    "assets/river_walk_events-leo_group-pages-8_p1.webp"
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Placeholders replaced in riverwalk.html")
