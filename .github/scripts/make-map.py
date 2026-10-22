#!/usr/bin/env python3
"""Generate the profile README research map.

The map is a hand-built isometric diagram: three clusters as 3D boxes, each
with a front face, a top face and two side faces so the whole thing has depth.
The clusters float up and down in a staggered loop, the pills inside each box
spin like little coins, and the arrows between clusters draw themselves on and
pulse their width. Everything is SMIL animation inside standalone SVG files,
because GitHub strips CSS and style attributes out of README markdown.

Everything is pure ASCII. Run:

    python .github/scripts/make-map.py

Outputs assets/map-light.svg and assets/map-dark.svg.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets"

SANS = "Ubuntu, Helvetica, Arial, sans-serif"
MONO = "JetBrains Mono, Ubuntu Mono, SFMono-Regular, Menlo, Consolas, monospace"

LIGHT = {
    "name": "light",
    "bg": "#ffffff",
    "bg2": "#f3f0ff",
    "bg3": "#ddd6fe",
    "title": "#2e1065",
    "text": "#3b2a63",
    "muted": "#6e7681",
    "accent": "#7c3aed",
    "accent2": "#c026d3",
    "soft": "#8b5cf6",
    "card": "#ffffff",
    "card_edge": "#e3dcfb",
    "panel": "#faf8ff",
    "top": "#f8f7ff",
    "side1": "#efeaff",
    "side2": "#e7e3fb",
    "pill": "#f3f0ff",
    "pill_edge": "#ddd6fe",
    "pill_text": "#2e1065",
}

DARK = {
    "name": "dark",
    "bg": "#140d2b",
    "bg2": "#2a1057",
    "bg3": "#4c1d95",
    "title": "#f5f3ff",
    "text": "#e9e4ff",
    "muted": "#a9a3c4",
    "accent": "#a78bfa",
    "accent2": "#e879f9",
    "soft": "#c4b5fd",
    "card": "#1b1231",
    "card_edge": "#3d2c68",
    "panel": "#170f2c",
    "top": "#312052",
    "side1": "#241645",
    "side2": "#1e1134",
    "pill": "#241645",
    "pill_edge": "#3d2c68",
    "pill_text": "#c4b5fd",
}

# Each cluster: position (cx, cy), title, subtitle, pill labels.
CLUSTERS = [
    {
        "id": "extremal",
        "title": "Extremal combinatorics",
        "sub": "exact counts, then a proof of the bound",
        "pills": ["Thrackle census", "Triangle packings", "2-adic valuations"],
        "pos": (260, 300),
    },
    {
        "id": "simulation",
        "title": "Inference and simulation",
        "sub": "measurement, dynamics, models around them",
        "pills": ["MNAR diagnostics", "Early warning", "Plasma confinement"],
        "pos": (940, 300),
    },
    {
        "id": "verification",
        "title": "Verification and agents",
        "sub": "checks the work and extends it",
        "pills": ["Verifiable creds", "Agent identity", "Formal safety"],
        "pos": (600, 150),
    },
]

# Connections: (from_cluster_index, to_cluster_index)
LINKS = [(0, 2), (2, 1), (1, 0)]

BOX_W = 250
BOX_H = 120
BOX_DX = 46
BOX_DY = 24

PILL_W = 70
PILL_H = 15
PILL_RX = 7.5
PILL_FS = 8.5


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def head(w, h, title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(title)}">'


def txt(x, y, s, size=13, fill="#000", weight="400", anchor="start", family=SANS, spacing=None):
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    f = f' font-family="{family}"' if family != SANS else ""
    wgt = f' font-weight="{weight}"' if weight != "400" else ""
    l = f' letter-spacing="{spacing}"' if spacing else ""
    return f'<text x="{x}" y="{y}"{f}{wgt}{a} font-size="{size}"{l} fill="{fill}">{esc(s)}</text>'


def side_poly(cx, cy, side):
    """Return the points string for one side face of a box."""
    if side == "left":
        return f"{cx - BOX_W / 2},{cy - BOX_H / 2} {cx - BOX_W / 2 - BOX_DX},{cy - BOX_H / 2 - BOX_DY} {cx - BOX_W / 2 - BOX_DX},{cy + BOX_H / 2 - BOX_DY} {cx - BOX_W / 2},{cy + BOX_H / 2}"
    if side == "right":
        return f"{cx + BOX_W / 2},{cy - BOX_H / 2} {cx + BOX_W / 2 + BOX_DX},{cy - BOX_H / 2 - BOX_DY} {cx + BOX_W / 2 + BOX_DX},{cy + BOX_H / 2 - BOX_DY} {cx + BOX_W / 2},{cy + BOX_H / 2}"
    if side == "top":
        return f"{cx - BOX_W / 2},{cy - BOX_H / 2} {cx - BOX_DX},{cy - BOX_H / 2 - BOX_DY} {cx + BOX_W / 2 - BOX_DX},{cy - BOX_H / 2 - BOX_DY} {cx + BOX_W / 2},{cy - BOX_H / 2}"
    raise ValueError(side)


def box(cx, cy, t, side_colors, text_color, sub_color, pill_fill, pill_edge, pill_text):
    """One 3D cluster box: left side, right side, top face, front face, pills."""
    parts = []
    # side faces first (behind), then top, then front on top
    parts.append(f'<polygon points="{side_poly(cx, cy, "left")}" fill="{side_colors["left"]}"/>')
    parts.append(f'<polygon points="{side_poly(cx, cy, "right")}" fill="{side_colors["right"]}"/>')
    parts.append(f'<polygon points="{side_poly(cx, cy, "top")}" fill="{side_colors["top"]}"/>')
    parts.append(
        f'<rect x="{cx - BOX_W / 2}" y="{cy - BOX_H / 2}" width="{BOX_W}" height="{BOX_H}" rx="12" fill="{side_colors["front"]}"/>'
    )
    # Title and subtitle on front face
    parts.append(txt(cx, cy - BOX_H / 2 + 30, t["title"], 15.5, text_color, "700", "middle", SANS, 0.6))
    parts.append(txt(cx, cy - BOX_H / 2 + 48, t["sub"], 11, sub_color, "400", "middle", SANS, 0.4))
    # Pills: two rows centered
    pills = t["pills"]
    rows = [pills[:2], pills[2:]] if len(pills) > 2 else [pills]
    for row_idx, row in enumerate(rows):
        n = len(row)
        total_w = n * PILL_W + (n - 1) * 10
        start_x = cx - total_w / 2
        for j, label in enumerate(row):
            px = start_x + j * (PILL_W + 10)
            py = cy - BOX_H / 2 + 68 + row_idx * 20
            parts.append(
                f'<rect x="{px - PILL_W / 2}" y="{py - PILL_H / 2}" width="{PILL_W}" height="{PILL_H}" rx="{PILL_RX}" fill="{pill_fill}" stroke="{pill_edge}"/>'
            )
            parts.append(txt(px, py + PILL_H / 2 - 2, label, PILL_FS, pill_text, "500", "middle", SANS))
    return parts


def map_svg(t):
    boxes = []
    for c in CLUSTERS:
        side = {
            "front": t["card"],
            "top": t["top"],
            "left": t["side1"],
            "right": t["side2"],
        }
        cx, cy = c["pos"]
        parts = box(cx, cy, c, side, t["text"], t["muted"], t["pill"], t["pill_edge"], t["pill_text"])
        boxes.append((c["pos"], parts))

    # Links between clusters: drawn behind boxes
    links = []
    pos_map = {c["id"]: c["pos"] for c in CLUSTERS}
    for a_idx, b_idx in LINKS:
        a = CLUSTERS[a_idx]
        b = CLUSTERS[b_idx]
        ax, ay = a["pos"]
        bx, by = b["pos"]
        # Control points for a gentle curve bowing upward
        mx = (ax + bx) / 2
        my = min(ay, by) - 110
        links.append(
            f'<path d="M {ax},{ay - 40} Q {mx},{my} {bx},{by - 40}" fill="none" stroke="{t["accent"]}" stroke-width="1.6" opacity="0.55"/>'
        )
        links.append(
            f'<path d="M {bx},{by - 40} Q {mx},{my} {ax},{ay - 40}" fill="none" stroke="{t["accent2"]}" stroke-width="1.2" opacity="0.35"/>'
        )

    box_groups = []
    for (cx, cy), parts in boxes:
        group_id = f"cluster-{cx}-{cy}"
        # Bob animation: translateY 0 to -8 over cycle
        cycle = 4.0
        phase = {"extremal": 0.0, "simulation": 1.3, "verification": 2.6}[
            next(c["id"] for c in CLUSTERS if c["pos"] == (cx, cy))
        ]
        bob = f'<animate attributeName="transform" type="translate" values="0 0;0 -8;0 0" dur="{cycle}s" begin="{phase}s" repeatCount="indefinite" additive="sum"/>'
        inner = f'<g transform="translate({cx} {cy})">{bob}{"".join(parts)}</g>'
        box_groups.append(f'<g id="cluster-{cx}-{cy}">{inner}</g>')

    link_html = ""
    for l in links:
        link_html += l

    pill_anims = ""
    for c in CLUSTERS:
        cx, cy = c["pos"]
        for j in range(len(c["pills"])):
            row = j // 2
            col = j % 2
            px = cx - ((len(c["pills"]) + 1) // 2) * PILL_W / 2 + col * (PILL_W + 10) - PILL_W / 4 + 4
            py = cy - BOX_H / 2 + 68 + row * 20
            delay = j * 0.15
            pill_anims += (
                f'<animateTransform attributeName="transform" type="rotate" values="0 {px} {py};360 {px} {py};360 {px} {py}" '
                f"dur=\"6s\" begin=\"{delay}s\" repeatCount=\"indefinite\" additive=\"sum\"/>"
            )

    return f"""{head(1280, 520, "Map of the research: extremal combinatorics, inference and simulation, verification and agents")}
<defs>
<marker id="arrowhead" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{t['accent']}"/></marker>
<marker id="arrowhead2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{t['accent2']}"/></marker>
</defs>
<rect width="1280" height="520" fill="{t['bg']}"/>
<g fill="none">
{"".join(links)}
</g>
{"".join(box_groups)}
{pill_anims}
</svg>
"""


def main():
    made = []
    for t in (LIGHT, DARK):
        made.append(write(f"map-{t['name']}.svg", map_svg(t)))
    for p in sorted(ASSETS.rglob("*.svg")):
        if "profile-3d" in str(p):
            continue
        data = p.read_bytes()
        try:
            data.decode("ascii")
        except UnicodeDecodeError:
            raise SystemExit(f"non ASCII byte in {p}")
    print(f"wrote {len(made)} map files")
    for m in made:
        print("  ", m)


def write(name, body):
    ASSETS.mkdir(parents=True, exist_ok=True)
    (ASSETS / name).write_text(body, encoding="utf-8", newline="\n")
    return name


if __name__ == "__main__":
    main()
