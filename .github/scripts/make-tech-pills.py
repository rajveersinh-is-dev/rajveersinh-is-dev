#!/usr/bin/env python3
"""Generate self-hosted tech stack pills for the Toolbox section.

Replaces shields.io badges with SVG pills drawn in the page's violet and
neutral palette. Each group is one row of rounded rectangles with the
technology name inside, in both light and dark theme twins.

Run:

    python .github/scripts/make-tech-pills.py

Outputs tech-languages-light.svg, tech-languages-dark.svg,
tech-tools-light.svg, tech-tools-dark.svg.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets"

SANS = "Ubuntu, Helvetica, Arial, sans-serif"

LIGHT = {
    "name": "light",
    "bg": "#ffffff",
    "pill": "#f3f0ff",
    "pill_edge": "#ddd6fe",
    "pill_text": "#3b2a63",
}
DARK = {
    "name": "dark",
    "bg": "#140d2b",
    "pill": "#241645",
    "pill_edge": "#3d2c68",
    "pill_text": "#e9e4ff",
}

# Groups of technologies, each rendered as one SVG row of pills.
GROUPS = [
    {
        "slug": "tech-languages",
        "title": "Languages",
        "items": ["Python", "TypeScript", "JavaScript", "Rust", "LaTeX", "Lean 4", "WGSL"],
    },
    {
        "slug": "tech-tools",
        "title": "Tools and frameworks",
        "items": ["Three.js", "Node.js", "Docker", "GitHub Actions", "Git",
                  "Tectonic", "CP-SAT", "PyQt6"],
    },
]

PILL_H = 24
PILL_RX = 12
PILL_GAP = 10
PILL_FS = 11
PAD_X = 12
PAD_Y = 14


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, size, fill, weight="500", anchor="middle", family=SANS):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" text-anchor="{anchor}" fill="{fill}">{esc(s)}</text>')


def head(w, h, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-label="{esc(title)}">')


def pills_svg(t, items):
    # Measure each pill width so they fit tightly.
    widths = [max(48, 0.66 * PILL_FS * len(item) + 20) for item in items]
    total = sum(widths) + PILL_GAP * (len(widths) - 1)
    w = total + 2 * PAD_X
    h = PILL_H + 2 * PAD_Y
    body = []
    x = PAD_X
    for item, pw in zip(items, widths):
        cx = x + pw / 2
        body.append(
            f'<rect x="{x:.0f}" y="{PAD_Y}" width="{pw:.0f}" height="{PILL_H}" '
            f'rx="{PILL_RX}" fill="{t["pill"]}" stroke="{t["pill_edge"]}" '
            f'stroke-width="1"/>'
        )
        body.append(txt(cx, PAD_Y + PILL_H / 2 + 4, item, PILL_FS, t["pill_text"]))
        x += pw + PILL_GAP
    return (f'{head(w, h, f"Tech stack: {", ".join(items)}")}'
            f'<rect width="{w}" height="{h}" fill="{t["bg"]}"/>'
            f'{"".join(body)}</svg>\n')


def main():
    made = []
    for g in GROUPS:
        for t in (LIGHT, DARK):
            name = f"{g['slug']}-{t['name']}.svg"
            body = pills_svg(t, g["items"])
            ASSETS.mkdir(parents=True, exist_ok=True)
            (ASSETS / name).write_text(body, encoding="ascii", newline="\n")
            made.append(name)
    for p in sorted(ASSETS.rglob("*.svg")):
        if "profile-3d" in str(p):
            continue
        data = p.read_bytes()
        try:
            data.decode("ascii")
        except UnicodeDecodeError:
            raise SystemExit(f"non ASCII byte in {p}")
    print(f"wrote {len(made)} tech pill files")
    for m in made:
        print("  ", m)


if __name__ == "__main__":
    main()
