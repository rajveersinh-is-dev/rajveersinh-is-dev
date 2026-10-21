"""Count commits across every branch, not only the default branch."""
import json
import re
import subprocess

U = "rajveersinh-is-dev"


def api(path):
    """Return (body, headers). Uses --include so the Link header is available."""
    r = subprocess.run(["gh", "api", "--include", path], capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    if r.returncode:
        return None, {}
    raw = r.stdout
    sep = "\r\n\r\n" if "\r\n\r\n" in raw else "\n\n"
    head, _, body = raw.partition(sep)
    headers = {}
    for line in head.splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            headers[k.strip().lower()] = v.strip()
    try:
        return json.loads(body), headers
    except json.JSONDecodeError:
        return None, headers


def last_page(path):
    body, headers = api(path)
    if not isinstance(body, list):
        return 0
    m = re.search(r"[?&]page=(\d+)>;\s*rel=\"last\"", headers.get("link", ""))
    return int(m.group(1)) if m else len(body)


repos = api(f"users/{U}/repos?per_page=100&type=owner")[0] or []
total_default = 0
total_all = 0
branches = 0
for r in repos:
    if r["private"]:
        continue
    total_default += last_page(f"repos/{U}/{r['name']}/commits?per_page=1")
    for b in api(f"repos/{U}/{r['name']}/branches?per_page=100")[0] or []:
        branches += 1
        total_all += last_page(f"repos/{U}/{r['name']}/commits?sha={b['name']}&per_page=1")

print(f"  public repositories         : {sum(1 for r in repos if not r['private'])}")
print(f"  branches walked             : {branches}")
print(f"  commits on default branches : {total_default}")
print(f"  commits on every branch     : {total_all}")
