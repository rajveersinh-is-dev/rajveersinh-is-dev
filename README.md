<!--
  Profile README for Rajveersinh Pardeshi (@rajveersinh-is-dev)

  To publish: create a PUBLIC repo named exactly  rajveersinh-is-dev  and put this
  file at its root. A private repo will not show up on your profile.

  Notes for future edits:
  - The banner and footer are hand-built SVGs in assets/, not a hosted service,
    so nothing can silently fail to render. Each has a light and a dark twin,
    and the README picks the right one with the #gh-light-mode-only /
    #gh-dark-mode-only URL fragments. The name is drawn inside the banner, so
    there is no Markdown heading for it.
  - The tagline under the banner is an animated typing SVG from
    readme-typing-svg (DenverCoder1). If it ever stops loading, swap that <img>
    for a plain centred line of text.
  - Every badge is flat-square and shares one accent (violet 7c3aed) plus a
    neutral grey (6e7681), so the palette matches the banner.
  - Projects are bullet lists, not tables. GitHub gives no control over table
    column widths, so on a phone the repo names broke across three lines and
    the descriptions were squeezed into a narrow strip.
  - No GitHub alert callouts: GitHub indents a blockquote, and a list inside one
    gets indented twice, which pushed the text into a narrow column.
  - Major sections are separated by --- rules. GitHub also draws a border under
    every h2, so each heading sits between two lines; that is deliberate.
  - The 3D contribution graph is generated once a day by
    .github/workflows/profile-3d.yml into profile-3d-contrib/. The action
    renders one combined canvas per theme; split-3d-svg.py then cuts it into
    three images (calendar, radar, language donut), strips the white background
    and drops the empty-day tiles. Do not hand-edit the SVGs; change
    .github/profile-3d-settings.json instead.
-->

<p align="center">
  <img alt="Rajveersinh Pardeshi" src="./assets/banner-light.svg#gh-light-mode-only" width="100%">
  <img alt="Rajveersinh Pardeshi" src="./assets/banner-dark.svg#gh-dark-mode-only" width="100%">
</p>

<p align="center">
  <img alt="Computational mathematics, scientific simulation, verifiable systems" src="https://readme-typing-svg.demolab.com?font=Ubuntu&weight=500&size=22&duration=3200&pause=900&color=7C3AED&center=true&vCenter=true&width=440&height=44&lines=Computational+mathematics;Scientific+simulation;Verifiable+systems">
</p>

<p align="center">
  <a href="mailto:daveaddams91@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-daveaddams91@gmail.com-7c3aed?style=flat-square&logo=gmail&logoColor=white"></a>
  <a href="https://github.com/rajveersinh-is-dev"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-rajveersinh--is--dev-7c3aed?style=flat-square&logo=github&logoColor=white"></a>
  <img alt="Location" src="https://img.shields.io/badge/Location-India-6e7681?style=flat-square">
  <img alt="Open to collaboration" src="https://img.shields.io/badge/Open%20to%20collaboration-7c3aed?style=flat-square">
</p>

<p align="center">
  <a href="#about">About</a> · <a href="#projects">Projects</a> · <a href="#toolbox">Toolbox</a> · <a href="#contribution-activity">Contribution activity</a> · <a href="#reach-me">Reach me</a>
</p>

---

## About

Most of my work is in extremal graph theory and combinatorial geometry, where the aim is to settle small cases exactly rather than bound them loosely. A good share of it starts from somebody else's conjecture and ends in a negative result, which I publish rather than quietly drop. Alongside that: missing data that is not missing at random, plasma confinement, and agents that write and verify their own successors.

I like results I can reproduce from scratch, and proofs that survive someone trying to break them. Most repositories ship a script that reruns the whole thing.

### What I work on

- Extremal graph theory and combinatorial geometry. Small cases settled by enumeration, then a proof of why the enumeration stopped where it did.
- Missing data under MNAR. Honest imputation is a hard problem when the mechanism is unobserved.
- Formal safety layers. Reachability analysis wrapped around a control loop, so compliance holds in the worst case and not only on average.
- Confidential verification. Credentials, mixnets and proof systems for agent identity and retrieval provenance.
- GPU first simulation. Compute shaders and JIT compiled kernels, because the physics deserves better than a slow interpreted loop.

### Currently

- Plasma confinement stability, drift orbits and energetic particle losses.
- Whether critical transitions can be signaled early in complex systems, rather than explained after the fact.
- Automation that improves itself: agents generating, verifying and publishing successors.
- Making heavy mathematics legible and reproducible in public.

### Contact

Open to research collaboration, reproducibility bugs, and PRs. Based in India, happy to work across time zones.

---

## Projects

### Featured

**[k-regular-partition-log-concavity](https://github.com/rajveersinh-is-dev/k-regular-partition-log-concavity)** resolves the Heim-Neuhauser conjecture on the log-concavity threshold of `k`-regular partitions.

### Combinatorics and geometry

- **[convex-thrackle-census](https://github.com/rajveersinh-is-dev/convex-thrackle-census)** — Exact census of `2^(n-1) - n` maximal convex thrackles, with a residue bound and wedge lemma
- **[triple-cover-convex-polygon](https://github.com/rajveersinh-is-dev/triple-cover-convex-polygon)** — Gap weight certificate giving a lower bound for all `n`, certified exact values through `n = 14`
- **[polygon-triangulation-packing](https://github.com/rajveersinh-is-dev/polygon-triangulation-packing)** — Exact extremal theory for `tau(n)` and `kappa(n)`, with constructive proofs
- **[maximal-convex-position-subsets](https://github.com/rajveersinh-is-dev/maximal-convex-position-subsets)** — Exact `f(n)` through `n = 9`, plus a point line duality theorem
- **[edge-disjoint-triangle-packings](https://github.com/rajveersinh-is-dev/edge-disjoint-triangle-packings)** — Convex barrier, then a reduction to subcubic trees
- **[cycle-spectra-connectivity](https://github.com/rajveersinh-is-dev/cycle-spectra-connectivity)** — Sharp minimum cycle count for `k` connected graphs, exact 3 connected spectrum to order 9
- **[connected-labeled-parity](https://github.com/rajveersinh-is-dev/connected-labeled-parity)** — Exact 2-adic valuations of connected labeled graphs and digraphs
- **[adic-diversity](https://github.com/rajveersinh-is-dev/adic-diversity)** — Largest number of distinct 2-adic valuations across the subset sums of `k` integers
- **[edge-disjoint-triangulations](https://github.com/rajveersinh-is-dev/edge-disjoint-triangulations)** — Packing number `floor(n/2)` and a full classification of `P_2m`, which has `2^(m-2)` resolutions
- **[inertia-admissible-polynomials](https://github.com/rajveersinh-is-dev/inertia-admissible-polynomials)** — Exact linearisation for the `q/s` ceiling of graph positive inertia, the `s = 1` case, and a conjectured barrier at 3
- **[k-regular-partition-log-concavity](https://github.com/rajveersinh-is-dev/k-regular-partition-log-concavity)** — Resolves the Heim-Neuhauser conjecture on the log-concavity threshold of `k`-regular partitions
- **[threshold-preference-arrangements](https://github.com/rajveersinh-is-dev/threshold-preference-arrangements)** — Exact chamber counts for tolerance-based distance orderings of point sets

### Conjectures under investigation

Full writeups, including the ones that do not work out.

- **[erdos-straus-conjecture-investigation](https://github.com/rajveersinh-is-dev/erdos-straus-conjecture-investigation)** — Exact criterion, a hard-core reduction, a Type I and Type II dichotomy, plus new parametric families
- **[erdos-problem-536-lcm-sets](https://github.com/rajveersinh-is-dev/erdos-problem-536-lcm-sets)** — Problem #536: sets with no three distinct elements sharing a pairwise LCM
- **[unit-distances-in-convex-position](https://github.com/rajveersinh-is-dev/unit-distances-in-convex-position)** — Erdos-Moser structural investigation of unit distances among convex polygon vertices
- **[ramanujan-signing-cut-vertex-obstruction](https://github.com/rajveersinh-is-dev/ramanujan-signing-cut-vertex-obstruction)** — A cut-vertex obstruction for cubic graphs in the Xu 2026 Ramanujan signing problem
- **[erdos-powerful-triples](https://github.com/rajveersinh-is-dev/erdos-powerful-triples)** — Erdos-Mollin-Walsh on three consecutive powerful numbers, closed with an honest negative report
- **[bollobas-leader-subsequence-sums](https://github.com/rajveersinh-is-dev/bollobas-leader-subsequence-sums)** — Proves the `t = 0` case of Bollobas-Leader on few subsequence sums in `Z_n x Z_n`

### Statistics and complex systems

- **[umbra](https://github.com/rajveersinh-is-dev/umbra)** — Python library for MNAR aware missing data diagnostics, identifiability bounds, and robust imputation when the data is not missing at random.
- **[early-warning-complex-systems](https://github.com/rajveersinh-is-dev/early-warning-complex-systems)** — Framework for testing whether statistical, physical and information theoretic indicators can anticipate critical transitions and collapse.

### Simulation and formal methods

- **[Tokamak-Py](https://github.com/rajveersinh-is-dev/Tokamak-Py)** — Numba accelerated N body electromagnetic plasma confinement engine, using Boris integration for stable particle pushing, with a PyQt6 interface.
- **[terrain-erosion-engine](https://github.com/rajveersinh-is-dev/terrain-erosion-engine)** — Procedural terrain generator running hydraulic and thermal erosion on the GPU, using WebGPU compute shaders and Three.js.
- **[certified-dose](https://github.com/rajveersinh-is-dev/certified-dose)** — Package, CLI and dashboard that put automated process control dosing inside a formal reachability analysis safety layer.

### Trust and autonomous agents

- **[docutrust](https://github.com/rajveersinh-is-dev/docutrust)** — Sovereign trust fabric covering verifiable credentials, agent identity federation, mixnets, retrieval provenance and zero knowledge state machines.
- **[autod](https://github.com/rajveersinh-is-dev/autod)** — Repository synthesizer that uses frontier models to invent, develop, verify and publish a working open source project every 48 hours.
- **[repo-improver-bot](https://github.com/rajveersinh-is-dev/repo-improver-bot)** — Engineering bot that sorts repositories by domain and upgrades them with tests, docs, benchmarks and CI through automated pull requests.

### Tools, languages and experiments

- **[numlang](https://github.com/rajveersinh-is-dev/numlang)** — Research programming language with a higher-order supercompiler, a polyhedral recurrence solver, and Lean 4 mechanized correctness proofs.
- **[Lilium-Mathematical-Art](https://github.com/rajveersinh-is-dev/Lilium-Mathematical-Art)** — Mathematical reconstruction of a white lily bouquet built in the presentation style of Hamid Naderi Yeganeh.

---

## Toolbox

**Languages**

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-7c3aed?style=flat-square&logo=python&logoColor=white">
  <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-7c3aed?style=flat-square&logo=typescript&logoColor=white">
  <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-7c3aed?style=flat-square&logo=javascript&logoColor=white">
  <img alt="LaTeX" src="https://img.shields.io/badge/LaTeX-7c3aed?style=flat-square&logo=latex&logoColor=white">
  <img alt="WGSL" src="https://img.shields.io/badge/WGSL-7c3aed?style=flat-square&logo=google&logoColor=white">
</p>

**Tools and frameworks**

<p>
  <img alt="Three.js" src="https://img.shields.io/badge/Three.js-6e7681?style=flat-square&logo=threedotjs&logoColor=white">
  <img alt="Node.js" src="https://img.shields.io/badge/Node.js-6e7681?style=flat-square&logo=nodedotjs&logoColor=white">
  <img alt="Docker" src="https://img.shields.io/badge/Docker-6e7681?style=flat-square&logo=docker&logoColor=white">
  <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-6e7681?style=flat-square&logo=githubactions&logoColor=white">
  <img alt="Git" src="https://img.shields.io/badge/Git-6e7681?style=flat-square&logo=git&logoColor=white">
</p>

**Also working with**

Numba · NumPy · SciPy · Jupyter · WebGPU · PyQt6 · LLM agents · Zero knowledge proofs · Verifiable credentials

---

## Contribution activity

<p align="center">
  <img alt="3D contribution graph" src="./profile-3d-contrib/profile-3d-calendar-light.svg#gh-light-mode-only" width="100%">
  <img alt="3D contribution graph" src="./profile-3d-contrib/profile-3d-calendar-dark.svg#gh-dark-mode-only" width="100%">
</p>

<p align="center">
  <img alt="Contribution breakdown" src="./profile-3d-contrib/profile-3d-radar-light.svg#gh-light-mode-only" width="46%">
  <img alt="Languages" src="./profile-3d-contrib/profile-3d-pie-light.svg#gh-light-mode-only" width="46%">
  <img alt="Contribution breakdown" src="./profile-3d-contrib/profile-3d-radar-dark.svg#gh-dark-mode-only" width="46%">
  <img alt="Languages" src="./profile-3d-contrib/profile-3d-pie-dark.svg#gh-dark-mode-only" width="46%">
</p>

---

## Reach me

- Email: [daveaddams91@gmail.com](mailto:daveaddams91@gmail.com)
- GitHub: [@rajveersinh-is-dev](https://github.com/rajveersinh-is-dev)
- Issues and pull requests are open on all the repositories above.

<p align="center">
  <img alt="gradient footer" src="./assets/footer-light.svg#gh-light-mode-only" width="100%">
  <img alt="gradient footer" src="./assets/footer-dark.svg#gh-dark-mode-only" width="100%">
</p>
