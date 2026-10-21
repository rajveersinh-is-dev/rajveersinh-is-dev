#!/usr/bin/env python3
"""Generate the profile README artwork.

Everything under assets/ except the 3D contribution images is produced here, so
the whole look of the page can be changed in one place and rebuilt with:

    python .github/scripts/make-profile-assets.py

Output is deterministic and pure ASCII. Every file is written in a light and a
dark variant, because GitHub switches between them with the #gh-light-mode-only
and #gh-dark-mode-only URL fragments, and those only work when the two files
share a base name.

Motion lives inside the SVG files as SMIL animation. GitHub strips CSS and
style attributes out of README markdown, so an animated image is the only way
to have any movement on the page. Every animation is written so that a reader
whose browser does not support SMIL still sees the finished artwork, never a
blank space.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets"
ICONS = ASSETS / "icons"

SANS = "Ubuntu, Helvetica, Arial, sans-serif"
MONO = "JetBrains Mono, Ubuntu Mono, SFMono-Regular, Menlo, Consolas, monospace"

LIGHT = {
    "name": "light",
    "bg": ("#ffffff", "#f3f0ff", "#ddd6fe"),
    "title": "#2e1065",
    "text": "#3b2a63",
    "muted": "#6e7681",
    "accent": "#7c3aed",
    "accent2": "#c026d3",
    "soft": "#8b5cf6",
    "card": "#ffffff",
    "card_edge": "#e3dcfb",
    "panel": "#faf8ff",
    "pill": "#f3f0ff",
    "pill_edge": "#ddd6fe",
}

DARK = {
    "name": "dark",
    "bg": ("#140d2b", "#2a1057", "#4c1d95"),
    "title": "#f5f3ff",
    "text": "#e9e4ff",
    "muted": "#a9a3c4",
    "accent": "#a78bfa",
    "accent2": "#e879f9",
    "soft": "#c4b5fd",
    "card": "#1b1231",
    "card_edge": "#3d2c68",
    "panel": "#170f2c",
    "pill": "#241645",
    "pill_edge": "#3d2c68",
}

# The thrackle that decorates the banner and the footer.
THRACKLE = [
    (1279.5, 227.3), (1218.1, 282.6), (1024.3, 326.4), (742.5, 348.5),
    (437.2, 343.9), (178.3, 313.7), (25.2, 264.8), (13.0, 208.4),
    (144.4, 157.3), (389.3, 123.4), (691.7, 114.4), (982.2, 132.3),
    (1194.3, 173.0),
]
# The footer is the same wave, flipped and shifted so it reads as a closing
# band rather than a repeat of the header.
FOOTER_THRACKLE = [
    (1279.5, 142.7), (1194.3, 197.0), (982.2, 237.7), (691.7, 255.6),
    (389.3, 246.6), (144.4, 212.7), (13.0, 161.6), (25.2, 105.2),
    (178.3, 56.3), (437.2, 26.1), (742.5, 21.5), (1024.3, 43.6),
    (1218.1, 87.4),
]
# Spokes are drawn from the first vertex to every other one except the two
# that the closing edge already covers.
SPOKE_SKIP = {1, 12}
STAMP_TOKEN = "__LAST_UPDATED__"
# The section icons are used in headings, where a light and dark pair would
# need both copies, so they use one mid tone that reads on either background.
ICON_ACCENT = "#8b5cf6"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, size=13, fill="#000", weight="400", anchor="start",
        family=SANS, spacing=None, extra=""):
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    f = f' font-family="{family}"' if family != SANS else ""
    w = f' font-weight="{weight}"' if weight != "400" else ""
    l = f' letter-spacing="{spacing}"' if spacing else ""
    return (f'<text x="{x}" y="{y}"{f}{w}{a} font-size="{size}"{l} '
            f'fill="{fill}"{extra}>{esc(s)}</text>')


def head(w, h, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-label="{esc(title)}">')


def write(name, body):
    ASSETS.mkdir(parents=True, exist_ok=True)
    (ASSETS / name).write_text(body, encoding="utf-8", newline="\n")
    return name


def write_icon(name, body):
    ICONS.mkdir(parents=True, exist_ok=True)
    (ICONS / name).write_text(body, encoding="utf-8", newline="\n")


# ---------------------------------------------------------------- banner ----
def wave(points, t, opacity=0.45):
    """The thrackle outline, its spokes and its vertices."""
    pts = " ".join(f"{x},{y}" for x, y in points)
    spokes = []
    for i, (x, y) in enumerate(points):
        if i in SPOKE_SKIP:
            continue
        spokes.append(f'<line x1="{points[0][0]}" y1="{points[0][1]}" '
                      f'x2="{x}" y2="{y}"/>')
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="4"/>' for x, y in points)
    return (f'<g fill="none"><polygon points="{pts}" stroke="{t["accent"]}" '
            f'stroke-width="1.6" opacity="{opacity}"/>'
            f'<g stroke="{t["accent"]}" stroke-width="1" opacity="0.22">'
            f'{"".join(spokes)}</g>'
            f'<g fill="{t["soft"]}" opacity="0.65">{dots}</g></g>')


def banner(t):
    """Banner with the thrackle drawing itself once, then the rule breathing.

    The base attribute values are the finished state, so a browser without SMIL
    shows the complete artwork instead of a blank band.
    """
    pts = " ".join(f"{x},{y}" for x, y in THRACKLE)
    spokes = []
    for i, (x, y) in enumerate(THRACKLE):
        if i in SPOKE_SKIP:
            continue
        spokes.append(f'<line x1="{THRACKLE[0][0]}" y1="{THRACKLE[0][1]}" '
                      f'x2="{x}" y2="{y}"/>')
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="4"/>' for x, y in THRACKLE)
    return f"""{head(1280, 220, "Rajveersinh Pardeshi")}
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t['bg'][0]}"/><stop offset="0.55" stop-color="{t['bg'][1]}"/><stop offset="1" stop-color="{t['bg'][2]}"/></linearGradient>
<linearGradient id="rule" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{t['accent']}"/><stop offset="1" stop-color="{t['accent2']}"/></linearGradient>
</defs>
<rect width="1280" height="220" fill="url(#bg)"/>
<g fill="none">
<polygon points="{pts}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="0" stroke="{t['accent']}" stroke-width="1.6" opacity="0.45"><animate attributeName="stroke-dashoffset" from="1" to="0" dur="2.6s" begin="0s" fill="freeze"/></polygon>
<g stroke="{t['accent']}" stroke-width="1" opacity="0.22">{"".join(spokes)}<animate attributeName="opacity" from="0" to="0.22" dur="1.2s" begin="1.4s" fill="freeze"/></g>
<g fill="{t['soft']}" opacity="0.65">{dots}<animate attributeName="opacity" from="0" to="0.65" dur="1s" begin="2s" fill="freeze"/></g>
</g>
{txt(640, 104, "Rajveersinh Pardeshi", 58, t["title"], "700", "middle", SANS, 1.5)}
<rect x="470" y="128" width="340" height="4" rx="2" fill="url(#rule)" opacity="0.9"><animate attributeName="opacity" values="0.9;0.42;0.9" dur="7s" repeatCount="indefinite"/></rect>
</svg>
"""


def footer(t):
    """Closing band. The date is a token that the daily workflow replaces."""
    return f"""{head(1280, 128, "Rajveersinh Pardeshi, profile footer")}
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t['bg'][0]}"/><stop offset="0.55" stop-color="{t['bg'][1]}"/><stop offset="1" stop-color="{t['bg'][2]}"/></linearGradient>
<linearGradient id="rule" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{t['accent']}"/><stop offset="1" stop-color="{t['accent2']}"/></linearGradient>
</defs>
<rect width="1280" height="128" fill="url(#bg)"/>
{wave(FOOTER_THRACKLE, t)}
<rect x="470" y="58" width="340" height="4" rx="2" fill="url(#rule)" opacity="0.9"/>
{txt(470, 104, f"PROFILE REFRESHED {STAMP_TOKEN}", 11.5, t["muted"], "500", "start", SANS, 1.5)}
</svg>
"""


# --------------------------------------------------------------- tagline ----
def tagline(t):
    """Self-hosted replacement for the external typing SVG.

    Three lines cross-fade on a nine second loop. The first line carries the
    finished opacity so that a browser without SMIL still shows a tagline.
    """
    lines = ["Computational mathematics",
             "Scientific simulation",
             "Verifiable systems"]
    body = []
    for i, line in enumerate(lines):
        base = "1" if i == 0 else "0"
        body.append(
            f'<text x="320" y="31" text-anchor="middle" font-family="{SANS}" '
            f'font-size="22" font-weight="500" letter-spacing="0.3" '
            f'fill="{t["text"]}" opacity="{base}">{esc(line)}'
            f'<animate attributeName="opacity" values="0;1;1;0;0" '
            f'keyTimes="0;0.04;0.30;0.36;1" dur="9s" begin="{i * 3}s" '
            f'repeatCount="indefinite"/></text>')
    return f"""{head(640, 44, "Computational mathematics, scientific simulation, verifiable systems")}
<g>{"".join(body)}</g>
</svg>
"""


# ------------------------------------------------------------- research map -
MAP_BOXES = [
    (30, 30, "Extremal combinatorics",
     "exact counts, then a proof of the bound",
     ["Thrackle census", "Triangle packings", "Cycle spectra",
      "2-adic valuations", "Erdos problems", "Convex subsets"]),
    (890, 30, "Inference and simulation",
     "measurement, dynamics, and the models around them",
     ["MNAR diagnostics", "Early warning", "Plasma confinement",
      "Terrain erosion", "Perturbation theory", "Root finding"]),
    (460, 268, "Verification and agents",
     "the machinery that checks the work and extends it",
     ["Verifiable credentials", "Agent identity", "Formal safety",
      "Supercompiler", "Repo automation", "Certified dosing"]),
]


def map_svg(t):
    boxes = []
    for x, y, title, sub, pills in MAP_BOXES:
        w, h = 360, 190
        p = []
        for i, label in enumerate(pills):
            col, row = i % 2, i // 2
            px = x + 16 + col * 168
            py = y + 62 + row * 36
            p.append(f'<rect x="{px}" y="{py}" width="160" height="28" rx="8" '
                     f'fill="{t["pill"]}" stroke="{t["pill_edge"]}"/>')
            p.append(txt(px + 80, py + 18, label, 11.5, t["text"], "500", "middle"))
        boxes.append(f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" '
                     f'fill="{t["panel"]}" stroke="{t["card_edge"]}"/>'
                     f'{txt(x + 18, y + 30, title, 15.5, t["title"], "700")}'
                     f'{txt(x + 18, y + 48, sub, 11, t["muted"])}'
                     f'{"".join(p)}</g>')

    def arrow(d, label=None, lx=0, ly=0):
        a = ""
        if label:
            a = txt(lx, ly, label, 10.5, t["muted"], "500", "middle")
        return (f'<path d="{d}" fill="none" stroke="{t["accent"]}" stroke-width="1.4" '
                f'marker-end="url(#head)"/>{a}')

    return f"""{head(1280, 486, "Map of the research: extremal combinatorics, inference and simulation, verification and agents")}
<defs>
<marker id="head" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{t['accent']}"/></marker>
</defs>
<rect width="1280" height="486" fill="none"/>
{"".join(boxes)}
{arrow("M 390 96 C 430 96 430 300 458 300", "verification", 404, 60)}
{arrow("M 890 96 C 850 96 850 300 822 300", "verification", 876, 60)}
{arrow("M 560 268 C 500 236 300 236 226 220", "new problems", 400, 232)}
</svg>
"""


# ------------------------------------------------------------------- seal ---
def seal(t):
    return f"""{head(460, 132, "Reproducible by default: every result reruns from one command")}
<rect x="1" y="1" width="458" height="130" rx="16" fill="{t['panel']}" stroke="{t['card_edge']}"/>
<circle cx="66" cy="66" r="44" fill="none" stroke="{t['accent']}" stroke-width="1.6"/>
<circle cx="66" cy="66" r="36" fill="none" stroke="{t['accent']}" stroke-width="0.8" opacity="0.5"/>
<path d="M 46 66 L 60 80 L 87 50" fill="none" stroke="{t['accent']}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
{txt(130, 58, "REPRODUCIBLE BY DEFAULT", 15, t["title"], "700", "start", SANS, 0.8)}
{txt(130, 80, "every published result reruns", 12, t["text"])}
{txt(130, 97, "from a single command", 12, t["text"])}
</svg>
"""


# ------------------------------------------------------------------ cards ---
CARDS = [
    {
        "slug": "card-thrackle",
        "title": "Convex thrackles",
        "formula": "2^(n-1) - n",
        "claim": "A maximal convex thrackle on n vertices has",
        "claim2": "exactly 2^(n-1) - n edges",
        "repo": "convex-thrackle-census",
        "diagram": "thrackle",
    },
    {
        "slug": "card-logconcavity",
        "title": "k-regular partitions",
        "formula": "N_k = 26   for k >= 30",
        "claim": "The log-concavity threshold of p_k(n) stabilises at 26",
        "claim2": "for every k >= 30, sharp and formalised in Lean 4",
        "repo": "k-regular-partition-log-concavity",
        "diagram": "bars",
    },
    {
        "slug": "card-packing",
        "title": "Polygon triangulations",
        "formula": "tau(n),  kappa(n)",
        "claim": "Exact packing and covering numbers for polygon",
        "claim2": "triangulations, with constructive proofs",
        "repo": "polygon-triangulation-packing",
        "diagram": "polygon",
    },
]


def diagram(kind, t):
    """A small figure for each card, drawn in the same visual language."""
    if kind == "thrackle":
        pts = [(30, 86), (60, 26), (104, 44), (116, 96), (72, 112)]
        poly = " ".join(f"{x},{y}" for x, y in pts + [pts[0]])
        edges = ""
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                edges += f'<line x1="{pts[i][0]}" y1="{pts[i][1]}" x2="{pts[j][0]}" y2="{pts[j][1]}"/>'
        return (f'<g fill="none" stroke="{t["accent"]}" stroke-width="1.2" opacity="0.85">'
                f'<polygon points="{poly}" stroke-width="1.8"/>{edges}</g>')
    if kind == "bars":
        heights = [30, 46, 62, 78, 90, 96, 92, 84]
        b = ""
        for i, h in enumerate(heights):
            x = 26 + i * 14
            fill = t["accent"] if i < 5 else t["soft"]
            b += (f'<rect x="{x}" y="{104 - h}" width="9" height="{h}" rx="2" '
                  f'fill="{fill}" opacity="{1 if i < 5 else 0.55}"/>')
        return (f'<g>{b}</g><line x1="20" y1="105" x2="146" y2="105" '
                f'stroke="{t["muted"]}" stroke-width="1"/>')
    if kind == "polygon":
        pts = [(72, 20), (120, 48), (104, 100), (40, 100), (24, 48)]
        poly = " ".join(f"{x},{y}" for x, y in pts + [pts[0]])
        diags = ""
        for a, b in ((0, 2), (0, 3), (1, 3), (1, 4), (2, 4)):
            diags += (f'<line x1="{pts[a][0]}" y1="{pts[a][1]}" '
                      f'x2="{pts[b][0]}" y2="{pts[b][1]}"/>')
        return (f'<g fill="none" stroke="{t["accent"]}" stroke-width="1.2" opacity="0.85">'
                f'<polygon points="{poly}" stroke-width="1.8"/>{diags}</g>')
    return ""


def card(c, t):
    """One result as a full width row.

    The cards used to sit three across at 31 percent of the content column,
    which left about 230 pixels for a 380 pixel wide image. The claim text
    rendered at roughly seven points and was unreadable.

    The row is 600 units wide on purpose. The profile column runs from about
    565 pixels on a narrow window to the full content width on a wide one, so
    artwork of that size is never scaled down. The type is therefore drawn at
    the size it is read, and the claim is split over two lines so that it fits
    without shrinking.
    """
    w, h = 600, 180
    return f"""{head(w, h, c['title'])}
<rect x="0.75" y="0.75" width="{w - 1.5}" height="{h - 1.5}" rx="14" fill="{t['card']}" stroke="{t['card_edge']}"/>
<rect x="0.75" y="0.75" width="5" height="{h - 1.5}" rx="2.5" fill="{t['accent']}"/>
<g transform="translate(10, 32)">{diagram(c['diagram'], t)}</g>
{txt(175, 48, c['title'], 19, t['title'], '700')}
{txt(175, 86, c['formula'], 22, t['accent'], '700', 'start', MONO)}
{txt(175, 118, c['claim'], 14, t['text'])}
{txt(175, 138, c['claim2'], 14, t['text'])}
{txt(175, 164, c['repo'], 12.5, t['muted'], '500', 'start', MONO)}
</svg>
"""


# ------------------------------------------------------------------ icons ---
ICONS_SPEC = {
    "about": ('<circle cx="10" cy="6.8" r="3.2"/>'
              '<path d="M 3.8 16.4 a 6.2 6.2 0 0 1 12.4 0"/>'),
    "results": ('<circle cx="10" cy="10" r="7"/><circle cx="10" cy="10" r="3.4"/>'
                '<circle cx="10" cy="10" r="1" fill="current" stroke="none"/>'),
    "papers": ('<path d="M 5 2.8 h 7 L 15 6 v 11.2 H 5 Z"/>'
               '<path d="M 7.4 9 h 5.2 M 7.4 12 h 5.2"/>'),
    "map": ('<circle cx="10" cy="4.2" r="2.1"/><circle cx="4.4" cy="15" r="2.1"/>'
            '<circle cx="15.6" cy="15" r="2.1"/>'
            '<path d="M 9.2 6 L 5.2 13 M 10.8 6 L 14.8 13 M 6.5 15 h 7"/>'),
    "projects": ('<circle cx="4.6" cy="10" r="2"/><circle cx="10" cy="5" r="2"/>'
                 '<circle cx="10" cy="15" r="2"/><circle cx="15.6" cy="10" r="2"/>'
                 '<path d="M 6.4 9 L 8.2 6.2 M 6.4 11 L 8.2 13.8 M 12 6.2 L 13.8 8.8'
                 ' M 12 13.8 L 13.8 11.2"/>'),
    "toolbox": ('<rect x="3.4" y="3.4" width="5.6" height="5.6" rx="1.4"/>'
                '<rect x="11" y="3.4" width="5.6" height="5.6" rx="1.4"/>'
                '<rect x="3.4" y="11" width="5.6" height="5.6" rx="1.4"/>'
                '<rect x="11" y="11" width="5.6" height="5.6" rx="1.4"/>'),
    "activity": ('<path d="M 4 16.6 V 11 M 10 16.6 V 5.6 M 16 16.6 V 8.8"/>'),
    "reach": ('<rect x="2.8" y="5" width="14.4" height="10" rx="2"/>'
              '<path d="M 3.4 6.2 L 10 11.4 L 16.6 6.2"/>'),
}


def icon(name):
    """One icon file, used in both themes.

    A light and dark pair would need both copies inside the heading, and if the
    theme switching ever failed to hide one of them the heading would show two
    icons. A mid violet reads on both backgrounds, so one file is enough.

    The viewBox is 24 wide for a 20 wide drawing. The spare 4 units are the
    gap between the icon and the heading text: the heading cannot contain a
    space, because GitHub turns a leading space into a leading hyphen in the
    heading slug, and the navigation links are written against that slug.
    """
    body = ICONS_SPEC[name].replace('fill="current" stroke="none"',
                                     f'fill="{ICON_ACCENT}" stroke="none"')
    return (f'{head(24, 20, name)}'
            f'<g fill="none" stroke="{ICON_ACCENT}" stroke-width="1.5" '
            f'stroke-linecap="round" stroke-linejoin="round">{body}</g></svg>\n')


# ------------------------------------------------------------------- main ---
def main():
    made = []
    for t in (LIGHT, DARK):
        made.append(write(f"banner-{t['name']}.svg", banner(t)))
        made.append(write(f"footer-{t['name']}.svg", footer(t)))
        made.append(write(f"tagline-{t['name']}.svg", tagline(t)))
        made.append(write(f"map-{t['name']}.svg", map_svg(t)))
        made.append(write(f"seal-{t['name']}.svg", seal(t)))
        for c in CARDS:
            made.append(write(f"{c['slug']}-{t['name']}.svg", card(c, t)))
    for name in ICONS_SPEC:
        write_icon(f"{name}.svg", icon(name))
    for p in sorted(ASSETS.rglob("*.svg")):
        if "profile-3d" in str(p):
            continue
        data = p.read_bytes()
        try:
            data.decode("ascii")
        except UnicodeDecodeError:
            raise SystemExit(f"non ASCII byte in {p}")
    print(f"wrote {len(made)} artwork files plus {len(ICONS_SPEC) * 2} icons")
    for m in made:
        print("  ", m)


if __name__ == "__main__":
    main()
