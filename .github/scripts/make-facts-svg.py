#!/usr/bin/env python3
"""Build the facts strip and stamp the footer.

Run by .github/workflows/profile-facts.yml once a day. It reads the public
repositories of the account with the workflow token and writes:

  assets/facts-light.svg   assets/facts-dark.svg    the numbers in the header
  assets/footer-light.svg  assets/footer-dark.svg   the same files with the
                                                     refresh date in the footer
                                                     brought up to date

Commit counts come from GitHub's own contribution calendar, the same number the
profile sidebar prints, so the strip and the sidebar can never disagree. The
repository list and the manuscript count come from the REST API. Only the
standard library is used, so the workflow needs no extra setup. Running it by
hand works too: the token falls back to the local gh CLI when GITHUB_TOKEN is
not set.
"""
import datetime
import importlib.util
import json
import os
import pathlib
import re
import subprocess
import sys
import urllib.error
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ASSETS = ROOT / "assets"
API = "https://api.github.com"

# The palette and the SVG helpers live with the rest of the artwork, so the
# strip can never drift away from the banner.
_spec = importlib.util.spec_from_file_location("mpa", HERE / "make-profile-assets.py")
mpa = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mpa)


def owner_from_remote():
    """The account that owns this checkout."""
    r = subprocess.run(["git", "config", "--get", "remote.origin.url"], cwd=ROOT,
                       capture_output=True, text=True)
    m = re.search(r"github\.com[:/]([^/]+)/", r.stdout.strip())
    return m.group(1) if m else ""


# Deliberately not USERNAME: on Windows that environment variable holds the
# Windows account name, which once made this script read a different GitHub
# account entirely.
USER = (os.environ.get("PROFILE_OWNER") or owner_from_remote()
        or "rajveersinh-is-dev")


def token():
    t = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if t:
        return t.strip()
    r = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
    return r.stdout.strip()


AUTH = ""


def api(path):
    """Return (body, headers) for a REST call, or (None, None) on failure."""
    req = urllib.request.Request(API + path, headers={
        "Authorization": f"Bearer {AUTH}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "profile-facts",
    })
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            return json.loads(r.read().decode("utf-8")), dict(r.headers)
    except (urllib.error.HTTPError, urllib.error.URLError, ValueError, TimeoutError):
        return None, None


def public_repos():
    repos, page = [], 1
    while True:
        body, _ = api(f"/users/{USER}/repos?per_page=100&type=owner&page={page}")
        if not isinstance(body, list) or not body:
            break
        repos.extend(body)
        if len(body) < 100:
            break
        page += 1
    return [r for r in repos if not r.get("private")]


def commit_count(repo):
    """Commits on the default branch, read off the pagination header.

    Kept for reference. The strip shows GitHub's own contribution count, which
    covers every branch as well as pull requests and issues, because that is
    the number the profile sidebar prints.
    """
    body, headers = api(f"/repos/{USER}/{repo}/commits?per_page=1")
    if not isinstance(body, list):
        return 0
    if not body:
        return 0
    link = ""
    for k, v in (headers or {}).items():
        if k.lower() == "link":
            link = v
    m = re.search(r"[?&]page=(\d+)>;\s*rel=\"last\"", link)
    return int(m.group(1)) if m else len(body)


def graphql(query):
    """A GraphQL call. Returns the data object, or None."""
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query}).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {AUTH}",
            "Content-Type": "application/json",
            "Accept": "application/vnd.github+json",
            "User-Agent": "profile-facts",
        })
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            body = json.loads(r.read().decode("utf-8"))
    except (urllib.error.HTTPError, urllib.error.URLError, ValueError, TimeoutError):
        return None
    if body.get("errors"):
        return None
    return body.get("data")


def contributions():
    """GitHub's own contribution count for the last twelve months.

    This is the number GitHub prints in the profile sidebar, "N contributions in
    the last year", and it counts commits on every branch plus pull requests
    and issues. Counting the default branch alone gave a smaller and
    different number, which read as a contradiction with the sidebar.
    """
    data = graphql('{ user(login: "%s") { contributionsCollection '
                   '{ contributionCalendar { totalContributions } } } }' % USER)
    if not data:
        return None
    cal = (((data.get("user") or {}).get("contributionsCollection") or {})
           .get("contributionCalendar") or {})
    return cal.get("totalContributions")


def manuscript_pdf(repo, branch):
    """The built PDF of a manuscript, if the repository has one under paper/."""
    body, _ = api(f"/repos/{USER}/{repo}/git/trees/{branch}?recursive=1")
    if not isinstance(body, dict):
        return ""
    for entry in body.get("tree", []):
        p = entry.get("path", "")
        if (entry.get("type") == "blob" and p.startswith("paper/")
                and p.lower().endswith(".pdf")):
            return p
    return ""


def gather():
    repos = public_repos()
    manuscripts = 0
    languages = {}
    for r in repos:
        if manuscript_pdf(r["name"], r["default_branch"]):
            manuscripts += 1
        lang = r.get("language")
        if lang:
            languages[lang] = languages.get(lang, 0) + 1
    top = sorted(languages.items(), key=lambda kv: (-kv[1], kv[0]))[:3]
    return {
        "repos": len(repos),
        "contributions": contributions(),
        "manuscripts": manuscripts,
        "languages": len(languages),
        "top": ", ".join(name for name, _ in top),
    }


def facts_svg(t, f):
    if f.get("contributions"):
        activity = (f"{f['contributions']:,}", "CONTRIBUTIONS", "in the last year")
    else:
        # The contribution calendar was unreachable. Say so rather than show a
        # number from a different measure.
        activity = ("-", "CONTRIBUTIONS", "count unavailable")
    cells = [
        (str(f["repos"]), "PUBLIC REPOS", "on GitHub"),
        activity,
        (str(f["manuscripts"]), "MANUSCRIPTS", "with a public PDF"),
        (str(f["languages"]), "LANGUAGES", f["top"] or "in use"),
    ]
    w, h, cw = 1280, 116, 320
    body = []
    for i, (value, label, sub) in enumerate(cells):
        cx = i * cw + cw // 2
        body.append(mpa.txt(cx, 56, value, 38, t["accent"], "700", "middle", mpa.MONO))
        body.append(mpa.txt(cx, 79, label, 11.5, t["text"], "700", "middle", mpa.SANS, 1.6))
        body.append(mpa.txt(cx, 99, sub, 11.5, t["muted"], "400", "middle"))
        if i:
            body.append(f'<line x1="{i * cw}" y1="26" x2="{i * cw}" y2="90" '
                        f'stroke="{t["card_edge"]}" stroke-width="1"/>')
    return (f'{mpa.head(w, h, "Profile facts: repositories, commits, manuscripts and languages")}'
            f'<rect x="0.75" y="0.75" width="{w - 1.5}" height="{h - 1.5}" rx="14" '
            f'fill="{t["panel"]}" stroke="{t["card_edge"]}"/>'
            f'{"".join(body)}</svg>\n')


def stamp_footer():
    today = datetime.datetime.now(datetime.timezone.utc).strftime("%d %b %Y").upper()
    for name in ("footer-light.svg", "footer-dark.svg"):
        p = ASSETS / name
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        text = re.sub(r"PROFILE REFRESHED [^<]*", "PROFILE REFRESHED " + today, text)
        p.write_text(text, encoding="utf-8", newline="\n")


def main():
    global AUTH
    AUTH = token()
    if not AUTH:
        print("no token available, set GITHUB_TOKEN or run gh auth login")
        return 1
    who, _ = api("/user")
    login = (who or {}).get("login", "?")
    print(f"owner={USER}  token belongs to {login}")
    if login != USER:
        print(f"WARNING: the token is for {login}, not {USER}. "
              f"The numbers would describe the wrong account.")
    f = gather()
    print(f"repos={f['repos']} contributions={f['contributions']} "
          f"manuscripts={f['manuscripts']} languages={f['languages']} "
          f"top={f['top']}")
    for t in (mpa.LIGHT, mpa.DARK):
        (ASSETS / f"facts-{t['name']}.svg").write_text(
            facts_svg(t, f), encoding="utf-8", newline="\n")
    stamp_footer()
    print("wrote assets/facts-light.svg, assets/facts-dark.svg, stamped the footers")
    return 0


if __name__ == "__main__":
    sys.exit(main())
