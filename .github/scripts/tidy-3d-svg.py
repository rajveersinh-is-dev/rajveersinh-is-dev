#!/usr/bin/env python3
"""Post-process github-profile-3d-contrib SVGs.

Two clean-ups, applied in place:

1. Transparent background - the generator paints a full-canvas rectangle
   behind everything. It is removed, and the background colour classes are
   forced to `transparent` so the image blends with the page (and with both
   GitHub light and dark themes).
2. Drop empty days - the calendar always spans a whole year, so a new
   account renders a large flat grey ramp for the months with no activity.
   Every level-0 tile face (the "no contributions" level) is made
   transparent, leaving only the coloured bars.

Usage: tidy-3d-svg.py FILE [FILE ...]
"""
import re
import sys


def tidy(svg: str) -> str:
    # 1. remove the full-canvas background rectangle
    svg = re.sub(
        r'<rect x="0" y="0" width="\d+" height="\d+" class="fill-bg"></rect>',
        "",
        svg,
    )

    # 2. force the background colour classes transparent
    svg = re.sub(r"(\.fill-bg\s*\{ fill: )[^;]*;", r"\1transparent;", svg)
    svg = re.sub(r"(\.stroke-bg\s*\{ stroke: )[^;]*;", r"\1transparent;", svg)

    # 3. hide empty days: level 0 of every tile face, across all periods
    svg = re.sub(
        r"(\.cont-(?:top|left|right)-p\d+-0\s*\{ fill: )[^;]*;",
        r"\1transparent;",
        svg,
    )
    return svg


def main(paths):
    for path in paths:
        with open(path, encoding="utf-8") as handle:
            before = handle.read()
        after = tidy(before)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(after)
        print(f"tidied {path} ({len(before)} -> {len(after)} bytes)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: tidy-3d-svg.py FILE [FILE ...]")
    main(sys.argv[1:])
