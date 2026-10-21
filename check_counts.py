"""Compare the commit counts: ours, and GitHub's own contribution totals."""
import json
import subprocess

U = "rajveersinh-is-dev"

QUERY = """
{
  user(login: "%s") {
    contributionsCollection {
      contributionCalendar { totalContributions }
      totalCommitContributions
      totalIssueContributions
      totalPullRequestContributions
      totalPullRequestReviewContributions
      restrictedContributionsCount
    }
    repositoriesContributedTo(first: 1) { totalCount }
  }
}
""" % U


def api(path):
    r = subprocess.run(["gh", "api", path], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if r.returncode:
        return None
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return None


def graphql(query):
    r = subprocess.run(["gh", "api", "graphql", "-f", f"query={query}"],
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace")
    if r.returncode:
        return {"_err": r.stderr[:300]}
    return json.loads(r.stdout)


g = graphql(QUERY)
print("=== GitHub's own contribution totals (last 12 months) ===")
print(json.dumps(g.get("data", g), indent=1))

print("\n=== ours, counted per repository ===")


def commits_of(repo, branch):
    body, headers = api(f"repos/{U}/{repo}/commits?per_page=1")
    if not isinstance(body, list):
        return 0
    import re
    link = ""
    for k, v in (headers or {}).items():
        if k.lower() == "link":
            link = v
    m = re.search(r"[?&]page=(\d+)>;\s*rel=\"last\"", link)
    return int(m.group(1)) if m else len(body)


repos = api(f"users/{U}/repos?per_page=100&type=owner") or []
total_default = 0
per_repo = []
for r in repos:
    if r["private"]:
        continue
    n = commits_of(r["name"], r["default_branch"])
    total_default += n
    per_repo.append((n, r["name"]))
per_repo.sort(reverse=True)
print(f"  public repos, default branch only: {total_default}")
for n, name in per_repo[:8]:
    print(f"    {n:>4}  {name}")

# commits on every branch, which is closer to what a contribution graph counts
import re
all_branch = 0
for r in repos:
    if r["private"]:
        continue
    body, headers = api(f"repos/{U}/{r['name']}/commits?per_page=1")
    if not isinstance(body, list):
        continue
    link = ""
    for k, v in (headers or {}).items():
        if k.lower() == "link":
            link = v
    m = re.search(r"[?&]page=(\d+)>;\s*rel=\"last\"", link)
    all_branch += int(m.group(1)) if m else len(body)
print(f"\n  (the endpoint only walks the default branch, so this is the same number)")
print(f"  private repos are excluded from both: "
      f"{sum(1 for r in repos if r['private'])} private")
