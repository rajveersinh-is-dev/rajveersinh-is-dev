#!/usr/bin/env python3
"""Generate the research map on the profile README.

The map is a stack of three 3D slabs, one per strand of the work. Each slab
has a front face, a top face and a side face, so it reads as a solid object
floating over a soft shadow. Light sweeps across each slab, the slabs drift
up and down out of phase, and a pulse runs down the connectors between them.

Everything is SMIL animation inside the SVG, because GitHub strips CSS and
style attributes out of README markdown. Every animation is additive on top
of a finished drawing, so a renderer that ignores SMIL still shows the whole
map.

The canvas is 640 wide on purpose: the profile column is about 565px at its
narrowest, so the artwork is only ever scaled a little and the labels stay
readable.

Run:

    python .github/scripts/make-map.py

Outputs assets/map-light.svg and assets/map-dark.svg.
"""
import pathlib
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets"

SANS = "Ubuntu, Helvetica, Arial, sans-serif"

W = 640
H = 540
MARGIN_X = 46
CARD_W = 540
CARD_H = 116
DEPTH_X = 22
DEPTH_Y = 18
CARD_TOP = (54, 212, 370)

BADGE_X = 44
BADGE_Y = 44
BADGE_R = 20
TEXT_X = 104
PILL_GAP = 8
PILL_H = 22
PILL_FS = 11
TITLE_FS = 18
SUB_FS = 12.5
WATERMARK_FS = 30

LIGHT = {
    "name": "light",
    "bg": "#ffffff",
    "bg_edge": "#e6e0fb",
    "card_a": "#ffffff",
    "card_b": "#faf8ff",
    "top": "#f1edff",
    "side": "#e7e2fb",
    "edge": "#ddd6fe",
    "highlight": "#ffffff",
    "title": "#241456",
    "text": "#3b2a63",
    "muted": "#6e7681",
    "accent": "#7c3aed",
    "accent2": "#c026d3",
    "pill": "#f5f2ff",
    "pill_edge": "#ded6fb",
    "pill_text": "#3b2a63",
    "shadow": "#2e1065",
    "glow": "#7c3aed",
    "glow_lo": 0.0,
    "glow_hi": 0.07,
    "shine": 0.10,
}

DARK = {
    "name": "dark",
    "bg": "#120b26",
    "bg_edge": "#2f2154",
    "card_a": "#231746",
    "card_b": "#1a1130",
    "top": "#332157",
    "side": "#241645",
    "edge": "#3d2c68",
    "highlight": "#a78bfa",
    "title": "#f5f3ff",
    "text": "#ddd6fe",
    "muted": "#a9a3c4",
    "accent": "#a78bfa",
    "accent2": "#e879f9",
    "pill": "#2a1b4d",
    "pill_edge": "#43307a",
    "pill_text": "#ddd6fe",
    "shadow": "#000000",
    "glow": "#a78bfa",
    "glow_lo": 0.0,
    "glow_hi": 0.12,
    "shine": 0.16,
}

CLUSTERS = [
    {
        "id": "extremal",
        "num": "01",
        "mark": "I",
        "title": "Extremal combinatorics",
        "sub": "exact counts first, then a proof of the bound",
        "pills": ["Thrackle census", "Triangle packings", "2-adic valuations"],
    },
    {
        "id": "simulation",
        "num": "02",
        "mark": "II",
        "title": "Inference and simulation",
        "sub": "measurement, dynamics, and the models around them",
        "pills": ["MNAR diagnostics", "Early warning", "Plasma confinement"],
    },
    {
        "id": "verification",
        "num": "03",
        "mark": "III",
        "title": "Verification and agents",
        "sub": "checks the work, then writes its successor",
        "pills": ["Verifiable credentials", "Agent identity", "Formal safety"],
    },
]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text_width(s, size, weight="400"):
    """Rough advance width for Helvetica. Good enough to catch overflow."""
    narrow = "iljtfrI.,:;'|!()[] "
    wide = "mwMW@%"
    factor = 0.58 if weight in ("600", "700") else 0.55
    total = 0.0
    for ch in s:
        if ch in narrow:
            total += 0.31 * size
        elif ch in wide:
            total += 0.86 * size
        else:
            total += factor * size
    return total


def text(x, y, s, size, fill, weight="400", anchor="start", spacing=None, opacity=None):
    attrs = [
        f'x="{x:.1f}"',
        f'y="{y:.1f}"',
        f'font-family="{SANS}"',
        f'font-size="{size}"',
        f'fill="{fill}"',
    ]
    if weight != "400":
        attrs.append(f'font-weight="{weight}"')
    if anchor != "start":
        attrs.append(f'text-anchor="{anchor}"')
    if spacing is not None:
        attrs.append(f'letter-spacing="{spacing}"')
    if opacity is not None:
        attrs.append(f'opacity="{opacity}"')
    return f'<text {" ".join(attrs)}>{esc(s)}</text>'


def pill_width(label):
    return text_width(label, PILL_FS, "500") + 20


def defs(t):
    n = t["name"]
    return f"""<defs>
<linearGradient id="card-{n}" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="{t['card_a']}"/>
<stop offset="1" stop-color="{t['card_b']}"/>
</linearGradient>
<linearGradient id="shine-{n}" x1="0" y1="0" x2="1" y2="0">
<stop offset="0" stop-color="{t['accent']}" stop-opacity="0"/>
<stop offset="0.5" stop-color="{t['accent']}" stop-opacity="{t['shine']}"/>
<stop offset="1" stop-color="{t['accent']}" stop-opacity="0"/>
</linearGradient>
<radialGradient id="glow-{n}" cx="0.5" cy="0.5" r="0.5">
<stop offset="0" stop-color="{t['glow']}" stop-opacity="{t['glow_hi']}"/>
<stop offset="1" stop-color="{t['glow']}" stop-opacity="{t['glow_lo']}"/>
</radialGradient>
<radialGradient id="shadow-{n}" cx="0.5" cy="0.5" r="0.5">
<stop offset="0" stop-color="{t['shadow']}" stop-opacity="0.34"/>
<stop offset="0.55" stop-color="{t['shadow']}" stop-opacity="0.14"/>
<stop offset="1" stop-color="{t['shadow']}" stop-opacity="0"/>
</radialGradient>
<marker id="tip-{n}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto">
<path d="M 0 1 L 9 5 L 0 9 z" fill="{t['accent']}"/>
</marker>
</defs>"""


def card(t, c, index, top):
    """One 3D slab in local coordinates, plus its grounded shadow."""
    n = t["name"]
    x0 = 0.0
    y0 = 0.0
    x1 = CARD_W
    y1 = CARD_H

    front = (
        f'<rect x="{x0}" y="{y0}" width="{CARD_W}" height="{CARD_H}" rx="14" '
        f'fill="url(#card-{n})" stroke="{t["edge"]}" stroke-width="1"/>'
    )
    top_face = (
        f'<polygon points="{x0},{y0} {x0 + DEPTH_X},{y0 - DEPTH_Y} '
        f'{x1 + DEPTH_X},{y0 - DEPTH_Y} {x1},{y0}" '
        f'fill="{t["top"]}" stroke="{t["edge"]}" stroke-width="1"/>'
    )
    side_face = (
        f'<polygon points="{x1},{y0} {x1 + DEPTH_X},{y0 - DEPTH_Y} '
        f'{x1 + DEPTH_X},{y1 - DEPTH_Y} {x1},{y1}" '
        f'fill="{t["side"]}" stroke="{t["edge"]}" stroke-width="1"/>'
    )
    lip = (
        f'<line x1="14" y1="{y0}" x2="{x1 - 14}" y2="{y0}" '
        f'stroke="{t["highlight"]}" stroke-width="1" opacity="0.45"/>'
    )

    parts = [top_face, side_face, front, lip]

    # badge with a roman numeral
    parts.append(
        f'<circle cx="{BADGE_X}" cy="{BADGE_Y}" r="{BADGE_R}" '
        f'fill="{t["accent"]}" fill-opacity="0.10" '
        f'stroke="{t["accent"]}" stroke-opacity="0.55" stroke-width="1.2"/>'
    )
    parts.append(
        text(BADGE_X, BADGE_Y + 5, c["mark"], 13, t["accent"], "700", "middle", "0.5")
    )

    # watermark number, top right
    parts.append(
        text(
            x1 - 16,
            50,
            c["num"],
            WATERMARK_FS,
            t["accent"],
            "700",
            "end",
            "1",
            0.10,
        )
    )

    parts.append(text(TEXT_X, 36, c["title"], TITLE_FS, t["title"], "700", "start", "0.2"))
    parts.append(text(TEXT_X, 58, c["sub"], SUB_FS, t["muted"], "400", "start", "0.1"))

    # pills, one row
    widths = [pill_width(p) for p in c["pills"]]
    total = sum(widths) + PILL_GAP * (len(widths) - 1)
    available = CARD_W - TEXT_X - 20
    if total > available:
        raise SystemExit(
            f"pills for {c['id']} need {total:.0f}px, only {available}px available"
        )
    px = TEXT_X
    for label, pw in zip(c["pills"], widths):
        parts.append(
            f'<rect x="{px:.1f}" y="{77}" width="{pw:.1f}" height="{PILL_H}" rx="11" '
            f'fill="{t["pill"]}" stroke="{t["pill_edge"]}" stroke-width="1"/>'
        )
        parts.append(
            text(
                px + pw / 2,
                77 + PILL_H / 2 + 3.7,
                label,
                PILL_FS,
                t["pill_text"],
                "500",
                "middle",
                "0.1",
            )
        )
        px += pw + PILL_GAP

    # light sweep clipped to the front face
    clip_id = f"clip-{n}-{index}"
    parts.append(
        f'<clipPath id="{clip_id}"><rect x="0" y="0" width="{CARD_W}" '
        f'height="{CARD_H}" rx="14"/></clipPath>'
    )
    parts.append(
        f'<g clip-path="url(#{clip_id})">'
        f'<g transform="skewX(-14)">'
        f'<rect x="0" y="0" width="120" height="{CARD_H}" fill="url(#shine-{n})">'
        f'<animateTransform attributeName="transform" type="translate" '
        f'values="-260 0;760 0" dur="7.5s" begin="{index * 1.7:.1f}s" '
        f'repeatCount="indefinite"/></rect></g></g>'
    )

    body = (
        f'<g transform="translate({MARGIN_X} {top})">'
        f'<g>'
        f'<animateTransform attributeName="transform" type="translate" '
        f'values="0 2;0 -4.5;0 2" dur="5.5s" begin="{index * 0.9:.1f}s" '
        f'repeatCount="indefinite"/>'
        f'{"".join(parts)}</g></g>'
    )
    return body


def shadow(t, index, top):
    """Soft contact shadow under one slab, drawn behind connectors and cards."""
    cx = MARGIN_X + CARD_W / 2
    cy = top + CARD_H + 10
    begin = index * 0.9
    return (
        f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="230" ry="16" '
        f'fill="url(#shadow-{t["name"]})">'
        f'<animate attributeName="ry" values="16;13;16" dur="5.5s" '
        f'begin="{begin:.1f}s" repeatCount="indefinite"/>'
        f'<animate attributeName="opacity" values="0.85;0.6;0.85" dur="5.5s" '
        f'begin="{begin:.1f}s" repeatCount="indefinite"/></ellipse>'
    )


def connector(t, index, y_from, y_to):
    """Straight pulse channel between two slabs, with a live travelling dot."""
    n = t["name"]
    cx = MARGIN_X + CARD_W / 2
    start = y_from + 3
    end = y_to - 9
    path = f"M {cx:.1f} {start:.1f} L {cx:.1f} {end:.1f}"
    begin = index * 0.8
    return (
        f'<path d="{path}" fill="none" stroke="{t["accent"]}" '
        f'stroke-width="3" stroke-linecap="round" opacity="0.10"/>'
        f'<path d="{path}" fill="none" stroke="{t["accent"]}" stroke-width="2" '
        f'stroke-linecap="round" stroke-dasharray="5 7" '
        f'marker-end="url(#tip-{n})">'
        f'<animate attributeName="stroke-dashoffset" values="0;-24" dur="1.4s" '
        f'begin="{begin:.1f}s" repeatCount="indefinite"/></path>'
        f'<g>'
        f'<animateMotion dur="2.4s" begin="{begin + 0.2:.1f}s" '
        f'repeatCount="indefinite" path="{path}"/>'
        f'<circle r="8" fill="{t["accent2"]}" opacity="0.18"/>'
        f'<circle r="2.6" fill="{t["accent2"]}"/></g>'
    )


def map_svg(t):
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" role="img" '
        f'aria-label="Research map: extremal combinatorics, inference and simulation, '
        f'verification and agents">',
        defs(t),
        f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="18" '
        f'fill="{t["bg"]}" stroke="{t["bg_edge"]}" stroke-width="1"/>',
        f'<ellipse cx="{W / 2}" cy="{H / 2}" rx="330" ry="280" fill="url(#glow-{t["name"]})"/>',
    ]

    # shadows first, so connectors and slabs sit on top of them
    for i, top in enumerate(CARD_TOP):
        out.append(shadow(t, i, top))

    # connectors are drawn under the slabs
    for i in range(len(CARD_TOP) - 1):
        out.append(
            connector(t, i, CARD_TOP[i] + CARD_H, CARD_TOP[i + 1])
        )

    for i, c in enumerate(CLUSTERS):
        out.append(card(t, c, i, CARD_TOP[i]))

    out.append("</svg>")
    return "\n".join(out) + "\n"


def check_svg(name, body):
    ET.fromstring(body)
    try:
        body.encode("ascii")
    except UnicodeEncodeError as exc:
        raise SystemExit(f"{name}: non ASCII byte at {exc.start}")
    root = ET.fromstring(body)
    known = set()

    def local(tag):
        return tag.split("}")[-1]

    for el in root.iter():
        if local(el.tag) == "marker":
            known.add(el.get("id"))
        if el.get("attributeName") == "transform" and local(el.tag) == "animate":
            raise SystemExit(f"{name}: transform animated with <animate> instead of <animateTransform>")
    for child in root:
        if local(child.tag) in ("animate", "animateTransform", "animateMotion"):
            raise SystemExit(f"{name}: animation directly on the root element")
    for el in root.iter():
        for attr in ("marker-start", "marker-end"):
            ref = el.get(attr)
            if ref and ref.startswith("url(#"):
                if ref[5:-1] not in known:
                    raise SystemExit(f"{name}: dangling {attr} {ref}")
    if not any(local(el.tag) == "animateTransform" for el in root.iter()):
        raise SystemExit(f"{name}: no animation found")
    if body.count("<svg") != 1 or not body.rstrip().endswith("</svg>"):
        raise SystemExit(f"{name}: malformed document")
    # every slab must carry a title, subtitle and three pills
    for c in CLUSTERS:
        for piece in (c["title"], c["sub"], *c["pills"]):
            if piece not in body:
                raise SystemExit(f"{name}: missing label {piece!r}")


def main():
    made = []
    for t in (LIGHT, DARK):
        name = f"map-{t['name']}.svg"
        body = map_svg(t)
        check_svg(name, body)
        ASSETS.mkdir(parents=True, exist_ok=True)
        (ASSETS / name).write_text(body, encoding="ascii", newline="\n")
        made.append(name)
    print(f"wrote {len(made)} map files")
    for m in made:
        print("  ", ASSETS / m)


if __name__ == "__main__":
    main()
