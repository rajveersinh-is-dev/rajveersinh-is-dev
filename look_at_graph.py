"""Look at the structure of the published 3D calendar."""
import base64
import json
import re
import subprocess

U = "rajveersinh-is-dev"
R = "rajveersinh-is-dev"


def get(path):
    r = subprocess.run(["gh", "api", f"repos/{U}/{R}/contents/{path}"],
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace")
    return base64.b64decode(json.loads(r.stdout)["content"]).decode("utf-8")


body = get("profile-3d-contrib/profile-3d-calendar-dark.svg")
i = body.find("</style>")
rest = body[i + 8:]

print("groups <g>:", len(re.findall(r"<g[ >]", rest)))
print("rects    :", len(re.findall(r"<rect", rest)))
print("paths    :", len(re.findall(r"<path", rest)))
print()
print("--- the first 1600 characters of the drawing ---")
print(rest[:1600].replace("><", ">\n<"))
print()
print("--- the distinct class names, sorted ---")
cls = sorted(set(re.findall(r'class="([^"]+)"', rest)))
print(len(cls), "classes, e.g.:", cls[:6], "...", cls[-4:])
print()
print("--- how many times does one class repeat? ---")
from collections import Counter
c = Counter(re.findall(r'class="([^"]+)"', rest))
print(c.most_common(4))
print()
print("--- the class names that identify a single row ---")
rows = sorted({int(m) for m in re.findall(r"-p(\d+)-\d+", " ".join(cls))})
print("p values:", rows)
