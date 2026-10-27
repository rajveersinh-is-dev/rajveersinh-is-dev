#!/usr/bin/env python3
"""Generate repo freshness badges for the Projects section.

Fetches the last push date of every public repository and emits one small
badge SVG per freshness category, in light and dark theme twins:

  updated today / this week / this month / this year / stale

A project is "today" if pushed within the last 24 hours, "this week" within
7 days, "this month" within 30 days, "this year" within 365 days, otherwise
"stale". The category is recomputed whenever the facts workflow runs, so the
badges never show a date that has aged past its bucket.

Run:

    python .github/scripts/make-freshness.py

Outputs assets/badge-fresh-*-light.svg and assets/badge-fresh-*-dark.svg.
"""
import datetime
import importlib.util
import json
import os
import pathlib
import subprocess
import urllib.error
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ASSETS = ROOT / "assets"
API = "https://api.github.com"

_spec = importlib.util.spec_from_file_location("mpa", HERE / "make-profile-assets.py")
mpa = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mpa)

USER = (os.environ.get("PROFILE_OWNER") or
        subprocess.run(["git", "config", "--get", "remote.origin.url"], cwd=ROOT,
                       capture_output=True, text=True).stdout.strip()
        or "rajveersinh-is-dev")
import re
_m = re.search(r"github\.com[:/]([^/]+)/", subprocess.run(
    ["git", "config", "--get", "remote.origin.url"], cwd=ROOT,
    capture_output=True, text=True).stdout.strip())
if _m:
    USER = _m.group(1)


def token():
    t = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if t:
        return t.strip()
    r = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
    return r.stdout.strip()


AUTH = ""


def api(path):
    req = urllib.request.Request(API + path, headers={
        "Authorization": f"Bearer {AUTH}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "profile-freshness",
    })
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            return json.loads(r.read().decode("utf-8"))
    except (urllib.error.HTTPError, urllib.error.URLError,
            ValueError, TimeoutError):
        return None


def public_repos():
    repos, page = [], 1
    while True:
        body = api(f"/users/{USER}/repos?per_page=100&type=owner&page={page}")
        if not isinstance(body, list) or not body:
            break
        repos.extend(body)
        if len(body) < 100:
            break
        page += 1
    return [r for r in repos if not r.get("private")]


def freshness_category(pushed_at):
    """Return one of today, week, month, year, stale."""
    pushed = datetime.datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
    age = (datetime.datetime.now(datetime.timezone.utc) - pushed).total_seconds()
    if age < 86400:
        return "today"
    if age < 604800:
        return "week"
    if age < 2592000:
        return "month"
    if age < 31536000:
        return "year"
    return "stale"


FRESH_LABEL = {
    "today": "updated today",
    "week": "updated this week",
    "month": "updated this month",
    "year": "updated this year",
    "stale": "not updated recently",
}


def badge_svg(t, category):
    label = FRESH_LABEL[category]
    # Measure the label width.
    w = max(70, 0.66 * 10 * len(label) + 22)
    h = 20
    return (f'{mpa.head(w, h, f"Repo freshness: {label}")}'
            f'<rect width="{w}" height="{h}" fill="{t["pill"]}" '
            f'stroke="{t["pill_edge"]}" stroke-width="1" rx="10"/>'
            f'<text x="{w / 2}" y="14" font-family="{mpa.SANS}" '
            f'font-size="10" font-weight="500" text-anchor="middle" '
            f'fill="{t["pill_text"]}">{label}</text>'
            f'</svg>\n')


def main():
    global AUTH
    AUTH = token()
    if not AUTH:
        print("no token available, set GITHUB_TOKEN or run gh auth login")
        return 1
    repos = public_repos()
    cats = {}
    for r in repos:
        pushed = r.get("pushed_at")
        if not pushed:
            continue
        cats[r["name"]] = freshness_category(pushed)
    made = []
    for cat in ("today", "week", "month", "year", "stale"):
        for t in (mpa.LIGHT, mpa.DARK):
            name = f"badge-fresh-{cat}-{t['name']}.svg"
            body = badge_svg(t, cat)
            ASSETS.mkdir(parents=True, exist_ok=True)
            (ASSETS / name).write_text(body, encoding="ascii", newline="\n")
            made.append(name)
    # Also write a small JSON map so the README generator (or a later step)
    # can look up which badge each repo gets.
    (ASSETS / "freshness.json").write_text(
        json.dumps(cats, indent=2), encoding="utf-8", newline="\n")
    print(f"wrote {len(made)} freshness badge files plus freshness.json")
    for m in made:
        print("  ", m)
    for cat, n in sorted({c: list(cats.values()).count(c) for c in cats.values()}.items()):
        print(f"  {cat}: {n} repos")


if __name__ == "__main__":
    import sys
    sys.exit(main())
