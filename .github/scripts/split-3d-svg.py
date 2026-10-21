#!/usr/bin/env python3
"""Split one github-profile-3d-contrib SVG into three standalone images.

The generator draws the 3D contribution calendar, the contribution radar and
the language donut on a single 1280x850 canvas. This script separates them so
the README can show the calendar big and centred, with the radar and donut
side by side underneath.

For each input it writes, next to it:

    profile-3d-calendar-<theme>.svg   calendar bars, cropped tight, plus the
                                      "N contributions / stars / forks" caption
    profile-3d-radar-<theme>.svg      contribution radar
    profile-3d-pie-<theme>.svg        language donut + legend

It also applies the three clean-ups the profile needs: a transparent background,
no empty-day tiles, and a palette that matches the page.

The generator paints the contribution tiles with two heat ramps, one for all
time and one for the current year, and paints the radar in the same green. The
page is violet, so the ramps are rotated onto violet and magenta and the
radar takes the accent. Lightness is preserved, so a busier day still reads
as a busier day. The language colours in the donut are pulled part of the way
towards the accent, which keeps each language recognisable while the block
reads as one palette.

Usage: split-3d-svg.py INPUT.svg THEME      (THEME is e.g. light or dark)
"""
import math
import os
import re
import sys
import xml.etree.ElementTree as ET

SVGNS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVGNS)

# ---- layout constants (fixed by the generator's 1280x850 canvas) ----------
CANVAS_W, CANVAS_H = 1280, 850

# radar and language donut never move; only their contents vary inside these
RADAR_BOX = (771, 95, 1191, 445)
PIE_BOX = (53, 533, 445, 767)
SIDE_PAD = 20              # breathing room before the aspect is normalised
SIDE_ASPECT = 1.3          # both side-by-side panels share this aspect ratio

# the stats caption is laid out from fixed fractions of the canvas width, so
# its position is constant even though the numbers change
COUNTS_CENTER_X = 551.5
COUNTS_BOTTOM_Y = 832.0
CAPTION_GAP = 34           # px between the calendar bars and the caption

CAL_PAD = 16               # breathing room around the cropped calendar

EMPTY_TILE = re.compile(r"^cont-(top|left|right)-p\d+-0$")
DATE_RANGE = re.compile(r"\d{4}-\d{2}-\d{2}")

# ---- palette ----------------------------------------------------------------
# The accent of the page, and the hue the two heat ramps are rotated onto.
ACCENT = (124, 58, 237)          # 7c3aed
NEUTRAL = {"dark": (169, 163, 196), "light": (110, 118, 129)}
LANGUAGE_MIX = 0.40              # how far the language colours move to the accent

# The generator paints the tiles with four series: the all-time heat ramp, the
# current-year ramp, a neutral and a pale one. Each series is repainted from
# a ramp of its own, so the level of a tile is still readable: on the dark
# background a busier day is brighter, and on the light one it is deeper, which
# is the convention GitHub's own contribution graph uses.
RAMPS = {
    "dark": {
        "total":  ["#5b21b6", "#7c3aed", "#a78bfa", "#ddd6fe"],
        "season": ["#86198f", "#c026d3", "#f0abfc", "#fbcfe8"],
        "grey":   ["#3b4252", "#57606a", "#8b949e", "#c9d1d9"],
        "other":  ["#f5f3ff", "#eae4ff", "#dcd6fb", "#bfa9f5"],
    },
    "light": {
        "total":  ["#ddd6fe", "#c4b5fd", "#a78bfa", "#6d28d9"],
        "season": ["#fce7f3", "#f5d0fe", "#e879f9", "#a21caf"],
        "grey":   ["#3b4252", "#57606a", "#8b949e", "#c9d1d9"],
        "other":  ["#f5f3ff", "#eae4ff", "#dcd6fb", "#bfa9f5"],
    },
}
FACE_SHADE = {"top": 1.0, "left": 0.84, "right": 0.70}

# ---- the wave ---------------------------------------------------------------
# The tiles are emitted week by week, seven days to a week, so wrapping them
# in groups of seven gives one group per week. Each group bobs and brightens
# in turn, and the delay between the groups sends a ripple along the time
# axis.
DAYS_PER_WEEK = 7
WAVE_CYCLE = 3.5          # seconds for one bob and one shimmer
WAVE_STEP = 0.06          # seconds between the start of one week and the next
WAVE_RISE = 3.0           # pixels a week rises by
WAVE_GLOW = 1.3           # how bright a week gets at the top of the wave

WAVE_CSS = """
.week {
  animation: week-bob %(cycle)ss ease-in-out infinite,
             week-glow %(cycle)ss ease-in-out infinite;
}
@keyframes week-bob {
  0%%, 100%% { translate: 0 0; }
  50%% { translate: 0 -%(rise)spx; }
}
@keyframes week-glow {
  0%%, 100%% { filter: brightness(1); }
  50%% { filter: brightness(%(glow)s); }
}
"""


def _parse_colour(spec):
    """'rgb(1, 2, 3)' or '#7c3aed' to an (r, g, b) tuple."""
    spec = spec.strip().rstrip(";").strip()
    if spec.startswith("#"):
        h = spec[1:]
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    nums = re.findall(r"[\d.]+", spec)
    return tuple(int(float(n)) for n in nums[:3])


def _fmt_colour(rgb):
    return "rgb(%d, %d, %d)" % tuple(max(0, min(255, int(round(c)))) for c in rgb)


def _rgb_to_hsl(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    hi, lo = max(r, g, b), min(r, g, b)
    light = (hi + lo) / 2
    if hi == lo:
        return 0.0, 0.0, light
    d = hi - lo
    sat = d / (2 - hi - lo) if light > 0.5 else d / (hi + lo)
    if hi == r:
        hue = ((g - b) / d) % 6
    elif hi == g:
        hue = (b - r) / d + 2
    else:
        hue = (r - g) / d + 4
    return hue * 60.0, sat, light


def classify(spec):
    """Which of the four series a tile belongs to, read from its original hue."""
    rgb = _parse_colour(spec)
    if len(rgb) < 3:
        return "grey"
    hue, sat, _ = _rgb_to_hsl(*rgb)
    if sat < 0.06:
        return "grey"
    if hue < 62:
        return "total"        # the all time ramp, yellow in the original
    if hue <= 165:
        return "season"       # the current year ramp, green in the original
    return "other"            # the pale series


def tile_colour(spec, level, face, theme):
    """The repainted colour for one tile face."""
    family = classify(spec)
    ramp = RAMPS.get(theme, RAMPS["dark"])[family]
    base = _parse_colour(ramp[max(0, min(3, level - 1))])
    shade = FACE_SHADE.get(face, 1.0)
    return _fmt_colour(tuple(c * shade for c in base))


def blend_to_accent(spec):
    r, g, b = _parse_colour(spec)
    return _fmt_colour(tuple(c + (a - c) * LANGUAGE_MIX
                             for c, a in zip((r, g, b), ACCENT)))


# ---- tiny affine matrix helpers -------------------------------------------
def _mul(A, B):
    a1, b1, c1, d1, e1, f1 = A
    a2, b2, c2, d2, e2, f2 = B
    return (a1 * a2 + c1 * b2, b1 * a2 + d1 * b2,
            a1 * c2 + c1 * d2, b1 * c2 + d1 * d2,
            a1 * e2 + c1 * f2 + e1, b1 * e2 + d1 * f2 + f1)


def _apply(M, x, y):
    a, b, c, d, e, f = M
    return (a * x + c * y + e, b * x + d * y + f)


def parse_transform(text):
    M = (1, 0, 0, 1, 0, 0)
    for name, raw in re.findall(r"(\w+)\s*\(([^)]*)\)", text):
        v = [float(x) for x in re.split(r"[\s,]+", raw.strip()) if x]
        if name == "translate":
            m = (1, 0, 0, 1, v[0], v[1] if len(v) > 1 else 0)
        elif name == "scale":
            sx = v[0]
            sy = v[1] if len(v) > 1 else v[0]
            m = (sx, 0, 0, sy, 0, 0)
        elif name == "skewX":
            m = (1, 0, math.tan(math.radians(v[0])), 1, 0, 0)
        elif name == "skewY":
            m = (1, math.tan(math.radians(v[0])), 0, 1, 0, 0)
        elif name == "rotate":
            a = math.radians(v[0])
            c, s = math.cos(a), math.sin(a)
            m = (c, s, -s, c, 0, 0)
        elif name == "matrix":
            m = tuple(v[:6])
        else:
            continue
        M = _mul(M, m)
    return M


# ---- geometry --------------------------------------------------------------
def visible_tile_bbox(group):
    """Union bbox of every tile face that is not an empty day (level 0)."""
    box = [float("inf"), float("inf"), float("-inf"), float("-inf")]
    found = 0

    def walk(el, M):
        nonlocal found
        t = el.get("transform")
        if t:
            M = _mul(M, parse_transform(t))
        if el.tag.split("}")[-1] == "rect":
            cls = el.get("class") or ""
            if cls.startswith("cont-") and not EMPTY_TILE.match(cls):
                x = float(el.get("x", 0))
                y = float(el.get("y", 0))
                w = float(el.get("width", 0))
                h = float(el.get("height", 0))
                for px, py in ((x, y), (x + w, y), (x, y + h), (x + w, y + h)):
                    tx, ty = _apply(M, px, py)
                    box[0] = min(box[0], tx)
                    box[1] = min(box[1], ty)
                    box[2] = max(box[2], tx)
                    box[3] = max(box[3], ty)
                found += 1
        for child in el:
            walk(child, M)

    walk(group, (1, 0, 0, 1, 0, 0))
    return (tuple(box) if found else None), found


def pad_box(box, pad):
    return (box[0] - pad, box[1] - pad, box[2] + pad, box[3] + pad)


def centre_to_aspect(box, aspect):
    """Grow a box about its centre until it has the requested aspect ratio."""
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    if w / h < aspect:
        want = h * aspect
        x0 -= (want - w) / 2
        x1 += (want - w) / 2
    else:
        want = w / aspect
        y0 -= (want - h) / 2
        y1 += (want - h) / 2
    return (x0, y0, x1, y1)


# ---- document assembly -----------------------------------------------------
def tidy_style(style_el, theme):
    """Force the background colour classes transparent and restyle the palette."""
    css = style_el.text or ""
    css = re.sub(r"(\.fill-bg\s*\{ fill: )[^;]*;", r"\1transparent;", css)
    css = re.sub(r"(\.stroke-bg\s*\{ stroke: )[^;]*;", r"\1transparent;", css)
    css = re.sub(
        r"(\.cont-(?:top|left|right)-p\d+-0\s*\{ fill: )[^;]*;",
        r"\1transparent;",
        css,
    )

    # repaint the four tile series from the page palette
    def repaint(m):
        face, row, level, colour = m.group(1), m.group(2), int(m.group(3)), m.group(4)
        if level == 0:
            return m.group(0)          # an empty day, already transparent
        return (f".cont-{face}-p{row}-{level} {{ fill: "
                f"{tile_colour(colour, level, face, theme)};")

    css = re.sub(
        r"\.cont-(top|left|right)-p(\d+)-(\d+)\s*\{\s*fill:\s*([^;]*);",
        repaint,
        css,
    )

    # the radar takes the accent, the weak lines the neutral of this theme
    neutral = NEUTRAL.get(theme, NEUTRAL["dark"])
    css = re.sub(r"(\.radar\s*\{[^}]*?stroke:\s*)[^;]*(;)",
                 lambda m: m.group(1) + _fmt_colour(ACCENT) + m.group(2), css)
    css = re.sub(r"(\.radar\s*\{[^}]*?fill:\s*)[^;]*(;)",
                 lambda m: m.group(1) + _fmt_colour(ACCENT) + m.group(2), css)
    for sel in (".fill-weak", ".stroke-weak"):
        css = re.sub(rf"({re.escape(sel)}\s*{{\s*(?:fill|stroke):\s*)[^;]*(;)",
                     lambda m: m.group(1) + _fmt_colour(neutral) + m.group(2), css)

    style_el.text = css
    return style_el


def group_into_weeks(calendar):
    """Wrap the tiles in one group per week and give each a delay.

    The generator emits the tiles week by week, seven days to a week, so the
    groups line up with the time axis. The groups carry an animation delay
    rather than an animation of their own, which is what turns 53 separate
    loops into a single wave travelling through the graph.
    """
    tiles = [c for c in list(calendar) if c.tag.split("}")[-1] == "g"]
    for child in list(calendar):
        calendar.remove(child)
    weeks = 0
    for start in range(0, len(tiles), DAYS_PER_WEEK):
        week = ET.SubElement(calendar, "g", {
            "class": "week",
            "style": "animation-delay: %.2fs" % (weeks * WAVE_STEP),
        })
        for tile in tiles[start:start + DAYS_PER_WEEK]:
            calendar.append(tile)
        weeks += 1
    return weeks


def blend_inline_fills(el):
    """Pull the language colours in the donut part of the way to the accent."""
    for node in el.iter():
        fill = node.get("fill")
        if fill and fill.startswith("#") and len(fill) == 7:
            node.set("fill", blend_to_accent(fill))
    return el


def build_document(style_el, box, *groups):
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    svg = ET.Element(f"{{{SVGNS}}}svg", {
        "width": str(round(w)),
        "height": str(round(h)),
        "viewBox": f"{x0:.2f} {y0:.2f} {w:.2f} {h:.2f}",
    })
    svg.append(style_el)
    for g in groups:
        if g is not None:
            svg.append(g)
    return ET.tostring(svg, encoding="unicode")


def pick_groups(root):
    """Find the calendar, radar, pie and totals groups by their content."""
    groups = [c for c in list(root) if c.tag.split("}")[-1] == "g"]

    def rects(el):
        return sum(1 for d in el.iter() if d.tag.split("}")[-1] == "rect")

    def has_class(el, name):
        return any((d.get("class") or "") == name for d in el.iter())

    def has_date_text(el):
        return any(
            d.tag.split("}")[-1] == "text" and DATE_RANGE.search(d.text or "")
            for d in el.iter()
        )

    calendar = max(groups, key=rects)
    totals = next((g for g in groups if has_date_text(g)), None)
    radar = next((g for g in groups if has_class(g, "radar")), None)
    pie = next((g for g in groups
                if g is not calendar and g is not radar and g is not totals), None)
    if None in (radar, pie):
        raise SystemExit("could not locate radar/pie groups in the SVG")
    return calendar, radar, pie, totals


def strip_caption_period(totals):
    """Drop the ISO date-range text so only the contribution stats remain."""
    for child in list(totals):
        if child.tag.split("}")[-1] == "text" and DATE_RANGE.search(child.text or ""):
            totals.remove(child)
    return totals


def split(path, theme):
    with open(path, encoding="utf-8") as fh:
        root = ET.fromstring(fh.read())

    style = next(c for c in list(root) if c.tag.split("}")[-1] == "style")
    tidy_style(style, theme)

    calendar, radar, pie, totals = pick_groups(root)
    blend_inline_fills(pie)
    weeks = group_into_weeks(calendar)
    style.text = (style.text or "") + (WAVE_CSS % {
        "cycle": WAVE_CYCLE, "rise": WAVE_RISE, "glow": WAVE_GLOW})
    outdir = os.path.dirname(os.path.abspath(path))

    # --- calendar: crop tight around the bars, then re-centre the caption ---
    cal_box, faces = visible_tile_bbox(calendar)
    if cal_box is None:
        raise SystemExit("no contribution tiles found; nothing to crop")

    if totals is not None:
        totals = strip_caption_period(totals)
        dx = (cal_box[0] + cal_box[2]) / 2 - COUNTS_CENTER_X
        dy = (cal_box[3] + CAPTION_GAP) - COUNTS_BOTTOM_Y
        totals.set("transform", f"translate({dx:.2f} {dy:.2f})")
        cap_box = (313 + dx, 802 + dy, 790 + dx, 832 + dy)
        union = (min(cal_box[0], cap_box[0]), min(cal_box[1], cap_box[1]),
                 max(cal_box[2], cap_box[2]), max(cal_box[3], cap_box[3]))
    else:
        union = cal_box

    cal_crop = (union[0] - CAL_PAD, union[1] - CAL_PAD,
                union[2] + CAL_PAD, union[3] + CAL_PAD)

    # --- radar and donut: fixed boxes, normalised to a shared aspect ratio ---
    radar_crop = centre_to_aspect(pad_box(RADAR_BOX, SIDE_PAD), SIDE_ASPECT)
    pie_crop = centre_to_aspect(pad_box(PIE_BOX, SIDE_PAD), SIDE_ASPECT)

    outputs = {
        f"profile-3d-calendar-{theme}.svg":
            build_document(style, cal_crop, calendar, totals),
        f"profile-3d-radar-{theme}.svg":
            build_document(style, radar_crop, radar),
        f"profile-3d-pie-{theme}.svg":
            build_document(style, pie_crop, pie),
    }
    for name, doc in outputs.items():
        with open(os.path.join(outdir, name), "w", encoding="utf-8") as fh:
            fh.write(doc)
        print(f"wrote {name}  ({len(doc)} bytes)")

    print(f"  calendar: {faces} tile faces, crop "
          f"({cal_crop[0]:.0f},{cal_crop[1]:.0f})-({cal_crop[2]:.0f},{cal_crop[3]:.0f}), "
          f"{weeks} weeks in the wave")


def main(argv):
    if len(argv) != 3:
        sys.exit("usage: split-3d-svg.py INPUT.svg THEME")
    split(argv[1], argv[2])


if __name__ == "__main__":
    main(sys.argv)
