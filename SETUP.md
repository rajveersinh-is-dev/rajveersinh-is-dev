# Publishing this README to your GitHub profile

GitHub renders the `README.md` from a repository whose name **exactly matches your
username**, and only if that repository is **public**. Nothing else about it is special.

---

## 1. The repo

It already exists and is live:

```
rajveersinh-is-dev/rajveersinh-is-dev     public, branch main
```

The name must track the username. When the login changes, rename the repository
too, or the README stops rendering. GitHub does not do this for you.

## 2. Publishing a change

```powershell
git clone https://github.com/rajveersinh-is-dev/rajveersinh-is-dev.git
cd rajveersinh-is-dev
# edit, then
git add -A
git commit -m "docs: ..."
git push
```

Commit as `rajveersinh-is-dev <daveaddams91@gmail.com>`. That email is the one
verified on the account, which is what makes GitHub attribute the commit to you.

## 3. Your profile fields

These are already set:

| Field | Value |
|:--|:--|
| Display name | Rajveersinh Pardeshi |
| Bio | Researcher in computational geometry, plasma physics and formal methods. Building verifiable systems, GPU simulations and autonomous agents. |
| Location | India |
| Public email | daveaddams91@gmail.com |

The bio is capped at 160 characters. To change any of them:

```powershell
gh api --method PATCH user `
  -f name="Rajveersinh Pardeshi" `
  -f bio="..." `
  -f location="India"
```

The public email is only editable in the browser at
<https://github.com/settings/emails>.

---

## The layout

```
README.md                        the profile README
SETUP.md                         this file, never shown on your profile
assets/                          every image the README uses
  banner-light.svg  banner-dark.svg
  tagline-light.svg tagline-dark.svg
  facts-light.svg   facts-dark.svg
  map-light.svg     map-dark.svg
  seal-light.svg    seal-dark.svg
  card-*-light.svg  card-*-dark.svg
  badge-pdf-light.svg  badge-pdf-dark.svg
  badge-code-light.svg  badge-code-dark.svg
  badge-fresh-*-light.svg  badge-fresh-*-dark.svg
  tech-languages-light.svg  tech-languages-dark.svg
  tech-tools-light.svg  tech-tools-dark.svg
  footer-light.svg  footer-dark.svg
  freshness.json                    repo freshness categories
  icons/                          one line icon per section heading
profile-3d-contrib/              the 3D contribution images, generated hourly
.github/scripts/
  make-profile-assets.py         rebuilds everything in assets/
  make-facts-svg.py              rebuilds the numbers and stamps the footer
  make-tech-pills.py             generates self-hosted tech stack pills
  make-freshness.py              generates repo freshness badges
  make-map.py                    regenerates the research map
  split-3d-svg.py                splits the 3D graph into separate images
.github/workflows/
  profile-3d.yml                 rebuilds the 3D contribution images (hourly + push)
  profile-facts.yml              rebuilds the facts strip and the footer stamp (hourly + push)
```

---

## Editing the README

### The artwork is generated, not hand drawn

Everything under `assets/` is produced by one script:

```powershell
python .github/scripts/make-profile-assets.py
```

Change the palette, the thrackle geometry, a card, a pill in the research map
or an icon in that file, then rerun it and commit the result. Do not hand edit
the SVGs, they will be overwritten.

The research map is its own script:

```powershell
python .github/scripts/make-map.py
```

It draws the three strands as three 3D slabs that drift out of phase, with a
light sweep across each face and a pulse running down the connectors between
them. The canvas is 640 wide on purpose: the profile column is about 565px at
its narrowest, so the labels stay legible instead of shrinking to nothing.

The tech stack pills are their own script:

```powershell
python .github/scripts/make-tech-pills.py
```

It generates self-hosted SVG pills for the languages and tools rows in the
Toolbox section, replacing external shields.io badges so the page has no
external image dependency.

The repo freshness badges are generated alongside the facts strip:

```powershell
python .github/scripts/make-freshness.py
```

It fetches the last push date of every public repository and categorizes each
as today, this week, this month, this year, or stale. The categories are
written to `assets/freshness.json` and rendered as small badge SVGs referenced
from the Projects section.

The numbers in the facts strip and the date in the footer come from a second
script that talks to the GitHub API:

```powershell
python .github/scripts/make-facts-svg.py
```

It uses `GITHUB_TOKEN` if it is set, otherwise it falls back to the token from
the local `gh` CLI. The `profile-facts` workflow runs it every hour and on
every push to main, so the numbers stay current.

One trap worth knowing: the script reads the account from `PROFILE_OWNER`, or
else from the checkout's own remote. It deliberately does not read `USERNAME`,
because on Windows that environment variable holds the Windows account name, and
the script once read a completely different GitHub account because of it.

### Sections

| Section | Where the content comes from |
|:--|:--|
| About | Two paragraphs, then a collapsed block with the longer lists |
| Results | Three full width rows, each linking to the repository it came from, each with a small sparkline trend |
| Papers | Every manuscript with a public PDF, grouped by theme, each with PDF and code badges |
| Research map | The three strands of the work, drawn in `make-map.py` |
| Projects | Everything that is not a published paper, each with a freshness badge |
| Toolbox | Self-hosted tech stack pills replacing external badges |
| How this page is built | Collapsed block listing the generator scripts and their cadence |
| Contribution activity | The 3D graph, generated by `profile-3d.yml` |
| Reach me | Contact details |

### Adding a paper

The Papers section links to `paper/main.pdf` on the default branch, using `HEAD`
so it works whichever branch the manuscript lives on:

```
https://github.com/rajveersinh-is-dev/REPO/blob/HEAD/paper/main.pdf
```

A repository only belongs in that section once its PDF is actually built and
committed. Until then it belongs under Projects, and a manuscript with no PDF
is better listed by its subject than by a link that 404s.

### Adding a project

Projects are bullet lists, not tables. GitHub gives no control over table
column widths, so on a phone the repository names broke across three lines and
the descriptions were squeezed into a narrow strip.

**Keeping it uncluttered.** The lists are written as results, one short line
each. If a cluster passes about a dozen entries, give it its own subsection
rather than widening the page.

### Changing colours

Everything uses one accent, violet `7c3aed`, plus a neutral grey `6e7681`.
They are defined once, in the `LIGHT` and `DARK` dictionaries at the top of
`.github/scripts/make-profile-assets.py`, and every badge colour in the README
matches them.

| Where | Current value |
|:--|:--|
| Accent | `7c3aed` |
| Accent, second stop | `c026d3` |
| Neutral | `6e7681` |
| Motif | `8b5cf6` |

Individual badge colours are the hex at the end of each shields.io URL.

### Sizing the artwork

The profile column runs from about 565 pixels on a narrow window to the full
content width on a wide one. An image is scaled to the column, so an image
wider than the narrowest column is scaled down and its type gets smaller with
it.

The result rows are therefore 600 units wide, which is never scaled down, and
their type is drawn at the size it is read. The claim is split over two lines
so that it fits at 14 points without shrinking. If you change a claim, keep
each line under about 55 characters, or it will run into the edge of the panel.

### The 3D contribution graph

The graph comes from `yoshi389111/github-profile-3d-contrib`, which paints
the contribution tiles with its own heat ramps: yellow and orange for all
time, green for the current year, and the raw GitHub language colours in the
donut. None of that matches the page.

`.github/scripts/split-3d-svg.py` repaints it on the way through. Each tile
is classified by the hue of the colour the generator gave it, so the four
series stay apart, and then repainted from a ramp of its own:

| Series | Meaning | Dark theme | Light theme |
|:--|:--|:--|:--|
| all time | every contribution | violet | violet |
| this year | the current season | magenta | magenta |
| neutral | unused days | grey | grey |
| other | a secondary series | pale violet | pale violet |

Lightness is kept per level, so a busier day still reads as a busier day, and
on the dark background a busier day is brighter, which is the convention
GitHub's own contribution graph uses. The radar takes the accent, the weak
lines take the neutral of the theme, and the language colours are pulled 40
percent towards the accent, which keeps each language recognisable while the
block reads as one palette.

To change the ramps, edit `RAMPS` in that script and re-run the
`GitHub-Profile-3D-Contrib` workflow (runs every hour and on push).

### The wave

The graph is not a still picture. The tiles are emitted week by week, seven
days to a week, so the split script wraps them in one group per week and
starts the wave off in each group.

| Effect | How | Why |
|:--|:--|:--|
| the bars rise and settle in turn | an SMIL transform on the week group | SMIL is certain to run inside a README image, since GitHub renders one in a sandbox with no scripting, and it is what made the previous typing banner move |
| the week brightens as it goes | a CSS filter on the same group | the two effects use different properties, so they cannot fight |

Each week group carries its own delay, 0.06 seconds after the one before it,
so the 53 groups read as one wave travelling through the year rather than 53
loops. The movement is 3 pixels over a 3.5 second cycle, which is slow enough
to be felt rather than watched.

**Hover is not possible.** GitHub renders a README image in a sandbox where
the SVG receives no pointer events, so a hover rule inside it can never fire.
The image is a single element to the page. Continuous animation is the only
kind that works there.

The generator's own one-shot growth animation is left in place, so the graph
builds itself when the page opens and the wave then runs through it.

### The numbers in the facts strip

The strip shows the same number GitHub prints in the profile sidebar, taken
from the contribution calendar:

```
{ user(login: "...") { contributionsCollection
    { contributionCalendar { totalContributions } } } }
```

An earlier version counted the commits on the default branch of each public
repository instead. That was a true number, but it measured something
different, and the two numbers sat on the same page looking like a
contradiction. Counting commits on every branch is not a fix either, because
the same commit is then counted once per branch that contains it.

### Checking the artwork

`light-preview.html` renders every light asset in a browser, which is the
quickest way to see a change to the banner, the map, the cards or the seal
without pushing first:

```powershell
python -m http.server 8731
# then open http://127.0.0.1:8731/light-preview.html
```

### Light and dark

Every image has a twin, and the README picks the right one with the
`#gh-light-mode-only` and `#gh-dark-mode-only` URL fragments. Those fragments
only work when the two files share a base name, so if you add an image, add
both.

The section icons are the exception. They are used inside headings, where a
light and dark pair would need both copies, so they use a single mid violet
that reads on either background.

---

## Things that were tried and removed, and why

Recording these so nobody has to rediscover them.

| Removed | Reason |
|:--|:--|
| **Stats cards**, top languages, streak, profile summary cards | `github-readme-stats` is a shared public Vercel instance and gets rate limited, so the cards intermittently render as a red error box. A profile that breaks at random is worse than no stats. The numbers are now built by `make-facts-svg.py` and committed as an SVG, so they cannot break. |
| **External typing header** (`readme-typing-svg`) | Its endpoint is a third party service and has already broken once. The tagline is now an animated SVG in `assets/`, so the page has no external image dependency other than the badge service. |
| **Text inside the gradient banner** (`capsule-render`) | capsule-render gives every text element `animation: fadeIn` from `opacity: 0`. Many renderers never play that animation, so the words stay invisible while the gradient still draws. The banner is drawn by hand now. |
| **Contribution grid snake** | Needed an `output` branch generated by a scheduled workflow, so it showed a broken image until that workflow had run. Removed rather than ship a visible gap. |
| **Skill icons** (`skillicons.dev`) | Its multi icon SVG only rendered the first icon. Replaced with plain shields.io badges, which are single files and always draw. |
| **Trophy case** and **activity graph** | Both services return HTTP 402, the hosts are gone. |
| **Dynamic repo count badge** | `img.shields.io/github/repos/rajveersinh-is-dev` returns a "badge not found" image. |
| **Emoji section titles and em dashes** | Cosmetic. Kept the headers plain so the page reads like a person wrote it. |

If you want a hosted stats card back later, the reliable route is to self host
`github-readme-stats` and point the image URLs at your own deployment.

---

## House rules this file follows

- **Pure ASCII.** The file is written in ASCII so that tools which mangle UTF-8
  cannot corrupt it. Separators are written as `/`, and the Greek letters are
  spelled out as `tau` and `kappa`.
- **No CSS in the markdown.** GitHub strips `<style>` blocks and `style`
  attributes, so all movement is SMIL animation inside the SVG files.
- **Every animation degrades.** Each animation is written so that its base
  attribute values are the finished state. A browser without SMIL shows the
  complete artwork rather than a blank band.
