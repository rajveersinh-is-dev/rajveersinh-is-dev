<!--
  Profile README for Rajveersinh Pardeshi (@rajveersinh-is-dev)

  To publish: the repository must be PUBLIC and its name must exactly match the
  username, otherwise GitHub renders nothing here.

  Notes for future edits:
  - Every image is committed under assets/ rather than fetched from a hosted
    service. The stats cards, streak, summary cards, activity graph, trophy
    case, contribution snake and skill icons that were tried earlier all
    failed; see SETUP.md for what each one did when it broke.
  - Each image has a light and a dark twin, and the README picks the right one
    with the #gh-light-mode-only / #gh-dark-mode-only URL fragments. Those
    fragments only work when the two files share a base name.
  - The artwork is generated, not hand drawn. Run
    python .github/scripts/make-profile-assets.py to rebuild it,
    python .github/scripts/make-facts-svg.py to refresh the numbers and the
    date in the footer, and
    python .github/scripts/make-map.py to regenerate the research map.
  - Motion is SMIL animation inside the SVG files. GitHub strips CSS and style
    attributes out of README markdown, so an animated image is the only way to
    have any movement. Every animation is written so that a browser without
    SMIL still shows the finished artwork.
  - Projects are bullet lists, not tables. GitHub gives no control over table
    column widths, so on a phone the repo names broke across three lines.
  - No GitHub alert callouts: GitHub indents a blockquote, and a list inside
    one gets indented twice, which pushed the text into a narrow column.
  - The file is pure ASCII, so it survives being edited by tools that mangle
    UTF-8. Separators are written as / and the Greek letters are spelled out.
-->

<p align="center">
  <img alt="Rajveersinh Pardeshi" src="./assets/banner-light.svg#gh-light-mode-only" width="100%">
  <img alt="Rajveersinh Pardeshi" src="./assets/banner-dark.svg#gh-dark-mode-only" width="100%">
</p>

<p align="center">
  <img alt="Computational mathematics, scientific simulation, verifiable systems" src="./assets/tagline-light.svg#gh-light-mode-only" width="500">
  <img alt="Computational mathematics, scientific simulation, verifiable systems" src="./assets/tagline-dark.svg#gh-dark-mode-only" width="500">
</p>

<p align="center">
  <a href="mailto:daveaddams91@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-daveaddams91@gmail.com-7c3aed?style=flat-square&logo=gmail&logoColor=white"></a>
  <a href="https://github.com/rajveersinh-is-dev"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-rajveersinh--is--dev-7c3aed?style=flat-square&logo=github&logoColor=white"></a>
  <img alt="Location" src="https://img.shields.io/badge/Location-India-6e7681?style=flat-square">
  <img alt="Open to collaboration" src="https://img.shields.io/badge/Open%20to%20collaboration-7c3aed?style=flat-square">
</p>

<p align="center">
  <img alt="Repositories, commits, manuscripts and languages" src="./assets/facts-light.svg#gh-light-mode-only" width="100%">
  <img alt="Repositories, commits, manuscripts and languages" src="./assets/facts-dark.svg#gh-dark-mode-only" width="100%">
</p>

<p align="center">
  <a href="#about">About</a> / <a href="#results">Results</a> / <a href="#papers">Papers</a> / <a href="#research-map">Research map</a> / <a href="#projects">Projects</a> / <a href="#toolbox">Toolbox</a> / <a href="#contribution-activity">Activity</a> / <a href="#reach-me">Reach me</a>
</p>

<p align="center">
  <a href="#extremal-combinatorics">Combinatorics</a> / <a href="#graph-counting-and-spectra">Counting and spectra</a> / <a href="#conjectures-under-investigation">Conjectures</a> / <a href="#statistics-and-complex-systems">Statistics</a> / <a href="#simulation-and-formal-methods">Simulation</a> / <a href="#trust-and-autonomous-agents">Trust and agents</a>
</p>

---

## <img alt="" src="./assets/icons/about.svg" width="22" align="absmiddle">About

Most of my work is in extremal graph theory and combinatorial geometry, where the aim is to settle small cases exactly rather than bound them loosely. A good share of it starts from somebody else's conjecture and ends in a negative result, which I publish rather than quietly drop. Alongside that: missing data that is not missing at random, plasma confinement, and agents that write and verify their own successors.

<p align="center">
  <img alt="Reproducible by default: every published result reruns from a single command" src="./assets/seal-light.svg#gh-light-mode-only" width="430">
  <img alt="Reproducible by default: every published result reruns from a single command" src="./assets/seal-dark.svg#gh-dark-mode-only" width="430">
</p>

<details>
<summary><b>What I work on, and what I am doing now</b></summary>

**What I work on**

- Extremal graph theory and combinatorial geometry. Small cases settled by enumeration, then a proof of why the enumeration stopped where it did.
- Missing data under MNAR. Honest imputation is a hard problem when the mechanism is unobserved.
- Formal safety layers. Reachability analysis wrapped around a control loop, so compliance holds in the worst case and not only on average.
- Confidential verification. Credentials, mixnets and proof systems for agent identity and retrieval provenance.
- GPU first simulation. Compute shaders and JIT compiled kernels, because the physics deserves better than a slow interpreted loop.

**Currently**

- Plasma confinement stability, drift orbits and energetic particle losses.
- Whether critical transitions can be signaled early in complex systems, rather than explained after the fact.
- Automation that improves itself: agents generating, verifying and publishing successors.
- Making heavy mathematics legible and reproducible in public.

</details>

I like results I can reproduce from scratch, and proofs that survive someone trying to break them. Most repositories ship a script that reruns the whole thing.

---

## <img alt="" src="./assets/icons/results.svg" width="22" align="absmiddle">Results

Three results I would defend in a hostile review. Each card opens the repository it came from.

<p align="center">
  <a href="https://github.com/rajveersinh-is-dev/convex-thrackle-census#gh-light-mode-only"><img alt="Convex thrackles: a maximal convex thrackle on n vertices has exactly 2^(n-1) - n edges" src="./assets/card-thrackle-light.svg#gh-light-mode-only" width="100%"></a>
  <a href="https://github.com/rajveersinh-is-dev/convex-thrackle-census#gh-dark-mode-only"><img alt="Convex thrackles: a maximal convex thrackle on n vertices has exactly 2^(n-1) - n edges" src="./assets/card-thrackle-dark.svg#gh-dark-mode-only" width="100%"></a>
</p>
<p align="center">
  <a href="https://github.com/rajveersinh-is-dev/k-regular-partition-log-concavity#gh-light-mode-only"><img alt="k-regular partitions: the log-concavity threshold of p_k(n) stabilises at 26 for every k >= 30" src="./assets/card-logconcavity-light.svg#gh-light-mode-only" width="100%"></a>
  <a href="https://github.com/rajveersinh-is-dev/k-regular-partition-log-concavity#gh-dark-mode-only"><img alt="k-regular partitions: the log-concavity threshold of p_k(n) stabilises at 26 for every k >= 30" src="./assets/card-logconcavity-dark.svg#gh-dark-mode-only" width="100%"></a>
</p>
<p align="center">
  <a href="https://github.com/rajveersinh-is-dev/polygon-triangulation-packing#gh-light-mode-only"><img alt="Polygon triangulations: exact packing and covering numbers" src="./assets/card-packing-light.svg#gh-light-mode-only" width="100%"></a>
  <a href="https://github.com/rajveersinh-is-dev/polygon-triangulation-packing#gh-dark-mode-only"><img alt="Polygon triangulations: exact packing and covering numbers" src="./assets/card-packing-dark.svg#gh-dark-mode-only" width="100%"></a>
</p>

---

## <img alt="" src="./assets/icons/papers.svg" width="22" align="absmiddle">Papers

Manuscripts with a published PDF. The title opens the PDF, the name opens the repository with the proofs, the code and the tests.

### Extremal combinatorics

- **[Convex thrackles: a residue bound, a wedge lemma, and the census 2^(n-1) - n](https://github.com/rajveersinh-is-dev/convex-thrackle-census/blob/HEAD/paper/main.pdf)** in [convex-thrackle-census](https://github.com/rajveersinh-is-dev/convex-thrackle-census) ![PDF](./assets/badge-pdf-light.svg#gh-light-mode-only) ![PDF](./assets/badge-pdf-dark.svg#gh-dark-mode-only) ![code](./assets/badge-code-light.svg#gh-light-mode-only) ![code](./assets/badge-code-dark.svg#gh-dark-mode-only)
- **[The extremal number of maximal convex-position subsets of a planar point set](https://github.com/rajveersinh-is-dev/maximal-convex-position-subsets/blob/HEAD/paper/main.pdf)** in [maximal-convex-position-subsets](https://github.com/rajveersinh-is-dev/maximal-convex-position-subsets) ![PDF](./assets/badge-pdf-light.svg#gh-light-mode-only) ![PDF](./assets/badge-pdf-dark.svg#gh-dark-mode-only) ![code](./assets/badge-code-light.svg#gh-light-mode-only) ![code](./assets/badge-code-dark.svg#gh-dark-mode-only)
- **[Edge-disjoint non-crossing triangle packings of planar point sets](https://github.com/rajveersinh-is-dev/edge-disjoint-triangle-packings/blob/HEAD/paper/main.pdf)** in [edge-disjoint-triangle-packings](https://github.com/rajveersinh-is-dev/edge-disjoint-triangle-packings) ![PDF](./assets/badge-pdf-light.svg#gh-light-mode-only) ![PDF](./assets/badge-pdf-dark.svg#gh-dark-mode-only) ![code](./assets/badge-code-light.svg#gh-light-mode-only) ![code](./assets/badge-code-dark.svg#gh-dark-mode-only)
- **[Edge-disjoint triangulations of convex polygons: packing numbers and resolutions](https://github.com/rajveersinh-is-dev/edge-disjoint-triangulations/blob/HEAD/paper/main.pdf)** in [edge-disjoint-triangulations](https://github.com/rajveersinh-is-dev/edge-disjoint-triangulations) ![PDF](./assets/badge-pdf-light.svg#gh-light-mode-only) ![PDF](./assets/badge-pdf-dark.svg#gh-dark-mode-only) ![code](./assets/badge-code-light.svg#gh-light-mode-only) ![code](./assets/badge-code-dark.svg#gh-dark-mode-only)
- **[Exact packing and covering numbers for polygon triangulations](https://github.com/rajveersinh-is-dev/polygon-triangulation-packing/blob/HEAD/paper/main.pdf)** in [polygon-triangulation-packing](https://github.com/rajveersinh-is-dev/polygon-triangulation-packing) ![PDF](./assets/badge-pdf-light.svg#gh-light-mode-only) ![PDF](./assets/badge-pdf-dark.svg#gh-dark-mode-only) ![code](./assets/badge-code-light.svg#gh-light-mode-only) ![code](./assets/badge-code-dark.svg#gh-dark-mode-only)
- **[The triple-covering number of a convex polygon: a gap-weight certificate](https://github.com/rajveersinh-is-dev/triple-cover-convex-polygon/blob/HEAD/paper/main.pdf)** in [triple-cover-convex-polygon](https://github.com/rajveersinh-is-dev/triple-cover-convex-polygon) ![PDF](./assets/badge-pdf-light.svg#gh-light-mode-only) ![PDF](./assets/badge-pdf-dark.svg#gh-dark-mode-only) ![code](./assets/badge-code-light.svg#gh-light-mode-only) ![code](./assets/badge-code-dark.svg#gh-dark-mode-only)
- **[Tolerance-based distance orderings of point sets: exact chamber counts](https://github.com/rajveersinh-is-dev/threshold-preference-arrangements/blob/HEAD/paper/main.pdf)** in [threshold-preference-arrangements](https://github.com/rajveersinh-is-dev/threshold-preference-arrangements) ![PDF](./assets/badge-pdf-light.svg#gh-light-mode-only) ![PDF](./assets/badge-pdf-dark.svg#gh-dark-mode-only) ![code](./assets/badge-code-light.svg#gh-light-mode-only) ![code](./assets/badge-code-dark.svg#gh-dark-mode-only)
- **[Unit distances among the vertices of a convex polygon](https://github.com/rajveersinh-is-dev/unit-distances-in-convex-position/blob/HEAD/paper/main.pdf)** in [unit-distances-in-convex-position](https://github.com/rajveersinh-is-dev/unit-distances-in-convex-position) ![PDF](./assets/badge-pdf-light.svg#gh-light-mode-only) ![PDF](./assets/badge-pdf-dark.svg#gh-dark-mode-only) ![code](./assets/badge-code-light.svg#gh-light-mode-only) ![code](./assets/badge-code-dark.svg#gh-dark-mode-only)

### Graph counting and spectra

- **[Cycle counts of k-connected graphs: a sharp minimum and a decidability theorem](https://github.com/rajveersinh-is-dev/cycle-spectra-connectivity/blob/HEAD/paper/main.pdf)** in [cycle-spectra-connectivity](https://github.com/rajveersinh-is-dev/cycle-spectra-connectivity) ![PDF](./assets/badge-pdf-light.svg#gh-light-mode-only) ![PDF](./assets/badge-pdf-dark.svg#gh-dark-mode-only) ![code](./assets/badge-code-light.svg#gh-light-mode-only) ![code](./assets/badge-code-dark.svg#gh-dark-mode-only)
- **[The 2-adic valuation of connected labeled graphs and digraphs](https://github.com/rajveersinh-is-dev/connected-labeled-parity/blob/HEAD/paper/main.pdf)** in [connected-labeled-parity](https://github.com/rajveersinh-is-dev/connected-labeled-parity) ![PDF](./assets/badge-pdf-light.svg#gh-light-mode-only) ![PDF](./assets/badge-pdf-dark.svg#gh-dark-mode-only) ![code](./assets/badge-code-light.svg#gh-light-mode-only) ![code](./assets/badge-code-dark.svg#gh-dark-mode-only)
- **[Maximizing the number of distinct 2-adic valuations of subset sums](https://github.com/rajveersinh-is-dev/adic-diversity/blob/HEAD/paper/main.pdf)** in [adic-diversity](https://github.com/rajveersinh-is-dev/adic-diversity) ![PDF](./assets/badge-pdf-light.svg#gh-light-mode-only) ![PDF](./assets/badge-pdf-dark.svg#gh-dark-mode-only) ![code](./assets/badge-code-light.svg#gh-light-mode-only) ![code](./assets/badge-code-dark.svg#gh-dark-mode-only)
- **[Inertia exponents of graphs: Boolean admissibility and the q/s ceiling](https://github.com/rajveersinh-is-dev/inertia-admissible-polynomials/blob/HEAD/paper/main.pdf)** in [inertia-admissible-polynomials](https://github.com/rajveersinh-is-dev/inertia-admissible-polynomials) ![PDF](./assets/badge-pdf-light.svg#gh-light-mode-only) ![PDF](./assets/badge-pdf-dark.svg#gh-dark-mode-only) ![code](./assets/badge-code-light.svg#gh-light-mode-only) ![code](./assets/badge-code-dark.svg#gh-dark-mode-only)
- **[The total domination number of 4 x n grid graphs](https://github.com/rajveersinh-is-dev/total-domination-4xn-grids/blob/HEAD/paper/main.pdf)** in [total-domination-4xn-grids](https://github.com/rajveersinh-is-dev/total-domination-4xn-grids) ![PDF](./assets/badge-pdf-light.svg#gh-light-mode-only) ![PDF](./assets/badge-pdf-dark.svg#gh-dark-mode-only) ![code](./assets/badge-code-light.svg#gh-light-mode-only) ![code](./assets/badge-code-dark.svg#gh-dark-mode-only)

### Probability, statistics and computation

- **[Exact expected subgraph counts in the random k-out graph](https://github.com/rajveersinh-is-dev/kout-local-structure/blob/HEAD/paper/main.pdf)** in [kout-local-structure](https://github.com/rajveersinh-is-dev/kout-local-structure) ![PDF](./assets/badge-pdf-light.svg#gh-light-mode-only) ![PDF](./assets/badge-pdf-dark.svg#gh-dark-mode-only) ![code](./assets/badge-code-light.svg#gh-light-mode-only) ![code](./assets/badge-code-dark.svg#gh-dark-mode-only)
- **[The sharp two-sided Cheeger-Buser bound for finite weighted graphs](https://github.com/rajveersinh-is-dev/sharp-cheeger-buser-certification/blob/HEAD/paper/main.pdf)** in [sharp-cheeger-buser-certification](https://github.com/rajveersinh-is-dev/sharp-cheeger-buser-certification) ![PDF](./assets/badge-pdf-light.svg#gh-light-mode-only) ![PDF](./assets/badge-pdf-dark.svg#gh-dark-mode-only) ![code](./assets/badge-code-light.svg#gh-light-mode-only) ![code](./assets/badge-code-dark.svg#gh-dark-mode-only)
- **[Exact rational perturbation theory for Kemeny's constant](https://github.com/rajveersinh-is-dev/kemeny-perturbation-theory/blob/HEAD/paper/main.pdf)** in [kemeny-perturbation-theory](https://github.com/rajveersinh-is-dev/kemeny-perturbation-theory) ![PDF](./assets/badge-pdf-light.svg#gh-light-mode-only) ![PDF](./assets/badge-pdf-dark.svg#gh-dark-mode-only) ![code](./assets/badge-code-light.svg#gh-light-mode-only) ![code](./assets/badge-code-dark.svg#gh-dark-mode-only)
- **[A fourth-order iterative method for scalar nonlinear equations](https://github.com/rajveersinh-is-dev/verified-iterative-root-finding/blob/HEAD/paper/main.pdf)** in [verified-iterative-root-finding](https://github.com/rajveersinh-is-dev/verified-iterative-root-finding) ![PDF](./assets/badge-pdf-light.svg#gh-light-mode-only) ![PDF](./assets/badge-pdf-dark.svg#gh-dark-mode-only) ![code](./assets/badge-code-light.svg#gh-light-mode-only) ![code](./assets/badge-code-dark.svg#gh-dark-mode-only)

### Formal methods, systems and languages

- **[Adaptive dual hull pruning: an exact algorithm for the weight-constrained shortest path problem](https://github.com/rajveersinh-is-dev/adhp-cspp/blob/HEAD/paper/main.pdf)** in [adhp-cspp](https://github.com/rajveersinh-is-dev/adhp-cspp) ![PDF](./assets/badge-pdf-light.svg#gh-light-mode-only) ![PDF](./assets/badge-pdf-dark.svg#gh-dark-mode-only) ![code](./assets/badge-code-light.svg#gh-light-mode-only) ![code](./assets/badge-code-dark.svg#gh-dark-mode-only)
- **[Certified-Dose: a formally verified reachability wrapper for process control dosing](https://github.com/rajveersinh-is-dev/certified-dose/blob/HEAD/paper/certified_dose_paper.pdf)** in [certified-dose](https://github.com/rajveersinh-is-dev/certified-dose) ![PDF](./assets/badge-pdf-light.svg#gh-light-mode-only) ![PDF](./assets/badge-pdf-dark.svg#gh-dark-mode-only) ![code](./assets/badge-code-light.svg#gh-light-mode-only) ![code](./assets/badge-code-dark.svg#gh-dark-mode-only)
- **[NumLang: a formally verified, self-applicable supercompiler for systems languages](https://github.com/rajveersinh-is-dev/numlang/blob/HEAD/paper/book/main_book.pdf)** in [numlang](https://github.com/rajveersinh-is-dev/numlang) ![PDF](./assets/badge-pdf-light.svg#gh-light-mode-only) ![PDF](./assets/badge-pdf-dark.svg#gh-dark-mode-only) ![code](./assets/badge-code-light.svg#gh-light-mode-only) ![code](./assets/badge-code-dark.svg#gh-dark-mode-only)
- **[Dual-Pruned Decoding: certified resource-aware search for autoregressive generation](https://github.com/rajveersinh-is-dev/dual-pruned-decoding/blob/HEAD/paper/main.pdf)** in [dual-pruned-decoding](https://github.com/rajveersinh-is-dev/dual-pruned-decoding) ![PDF](./assets/badge-pdf-light.svg#gh-light-mode-only) ![PDF](./assets/badge-pdf-dark.svg#gh-dark-mode-only) ![code](./assets/badge-code-light.svg#gh-light-mode-only) ![code](./assets/badge-code-dark.svg#gh-dark-mode-only)

---

## <img alt="" src="./assets/icons/map.svg" width="22" align="absmiddle">Research map

The three strands of the work, and how they feed each other. Enumeration produces a number, a proof turns the number into a theorem, and the verification layer checks the theorem and then writes its successor. The slabs drift out of phase, light sweeps across each face, and a pulse runs down each connector.

<p align="center">
  <img alt="Research map: extremal combinatorics, inference and simulation, verification and agents" src="./assets/map-light.svg#gh-light-mode-only" width="100%">
  <img alt="Research map: extremal combinatorics, inference and simulation, verification and agents" src="./assets/map-dark.svg#gh-dark-mode-only" width="100%">
</p>

---

## <img alt="" src="./assets/icons/projects.svg" width="22" align="absmiddle">Projects

The repositories behind the papers, the investigations that have not concluded, and the software.

### Combinatorics and geometry

- **[bishops-graph-metric-dimension](https://github.com/rajveersinh-is-dev/bishops-graph-metric-dimension)**: Exact metric dimension of bishop colour components, via a diamond rook-board reformulation, integer programming, and closed form conjectures ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)
- **[k-regular-partition-log-concavity](https://github.com/rajveersinh-is-dev/k-regular-partition-log-concavity)**: Resolves the Heim-Neuhauser conjecture on the log-concavity threshold of k-regular partitions, with a Lean 4 formalization ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)

### Conjectures under investigation

Full writeups, including the ones that do not work out.

- **[anti-ramsey-disjoint-copies-investigation](https://github.com/rajveersinh-is-dev/anti-ramsey-disjoint-copies-investigation)**: Autonomous investigation of the Gorgol-Gorlich conjecture on anti-Ramsey numbers, with exact CP-SAT experiments and a hostile audit of each claim ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)
- **[binomial-coprime-105](https://github.com/rajveersinh-is-dev/binomial-coprime-105)**: Erdos problem 376: binomial coefficients coprime to 105 ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)
- **[bollobas-leader-subsequence-sums](https://github.com/rajveersinh-is-dev/bollobas-leader-subsequence-sums)**: Proves the t = 0 case of Bollobas-Leader on few subsequence sums in Z_n x Z_n ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)
- **[degree-sensitivity-boolean](https://github.com/rajveersinh-is-dev/degree-sensitivity-boolean)**: Exact reductions, Farkas certificates, a machine verified refutation of the (10,4) case, and an obstruction analysis at (14,5) ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)
- **[erdos-powerful-triples](https://github.com/rajveersinh-is-dev/erdos-powerful-triples)**: Erdos-Mollin-Walsh on three consecutive powerful numbers, closed with an honest negative report ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)
- **[erdos-problem-536-lcm-sets](https://github.com/rajveersinh-is-dev/erdos-problem-536-lcm-sets)**: Problem #536: sets with no three distinct elements sharing a pairwise LCM ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)
- **[erdos-straus-conjecture-investigation](https://github.com/rajveersinh-is-dev/erdos-straus-conjecture-investigation)**: Exact criterion, a hard-core reduction, a Type I and Type II dichotomy, plus new parametric families ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)
- **[graham-distinct-partial-sums](https://github.com/rajveersinh-is-dev/graham-distinct-partial-sums)**: A width sufficient condition for Graham's distinct partial sums conjecture, with exact arithmetic verification ![updated today](./assets/badge-fresh-today-light.svg#gh-light-mode-only) ![updated today](./assets/badge-fresh-today-dark.svg#gh-dark-mode-only)
- **[ramanujan-signing-cut-vertex-obstruction](https://github.com/rajveersinh-is-dev/ramanujan-signing-cut-vertex-obstruction)**: A cut-vertex obstruction for cubic graphs in the Xu 2026 Ramanujan signing problem ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)
- **[union-closed-sets-conjecture](https://github.com/rajveersinh-is-dev/union-closed-sets-conjecture)**: Frankl's union-closed sets conjecture: structural bounds, proof attempts, and finite verification ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)

### Statistics and complex systems

- **[umbra](https://github.com/rajveersinh-is-dev/umbra)**: Python library for MNAR aware missing data diagnostics, identifiability bounds, and robust imputation when the data is not missing at random. ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)
- **[early-warning-complex-systems](https://github.com/rajveersinh-is-dev/early-warning-complex-systems)**: Framework for testing whether statistical, physical and information theoretic indicators can anticipate critical transitions and collapse. ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)
- **[bootstrap-percolation-Qd-r4](https://github.com/rajveersinh-is-dev/bootstrap-percolation-Qd-r4)**: Exact minimum percolating sets in the d-dimensional hypercube under 4-neighbour bootstrap percolation: lower bound, constructions, verified small cases ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)
- **[sharp-two-point-concentration-bound](https://github.com/rajveersinh-is-dev/sharp-two-point-concentration-bound)**: A sharp two-point moment-generating-function bound for sums of independent bounded random variables, an explicit improvement on Hoeffding ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)
- **[terrain-erosion-engine](https://github.com/rajveersinh-is-dev/terrain-erosion-engine)**: Procedural terrain generator running hydraulic and thermal erosion on the GPU, using WebGPU compute shaders and Three.js. ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)

### Simulation and formal methods

- **[Tokamak-Py](https://github.com/rajveersinh-is-dev/Tokamak-Py)**: Numba accelerated N body electromagnetic plasma confinement engine, using Boris integration for stable particle pushing, with a PyQt6 interface. ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)
- **[sare](https://github.com/rajveersinh-is-dev/sare)**: SARE: a verified adaptive elimination ordering for sparse fill-in reduction ![updated today](./assets/badge-fresh-today-light.svg#gh-light-mode-only) ![updated today](./assets/badge-fresh-today-dark.svg#gh-dark-mode-only)
- **[Lilium-Mathematical-Art](https://github.com/rajveersinh-is-dev/Lilium-Mathematical-Art)**: Mathematical reconstruction of a white lily bouquet built in the presentation style of Hamid Naderi Yeganeh. ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)
- **[ascii-motion](https://github.com/rajveersinh-is-dev/ascii-motion)**: ASCII animation experiments built as a self-contained HTML page. ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)
- **[dual-pruned-decoding](https://github.com/rajveersinh-is-dev/dual-pruned-decoding)**: Dual-Pruned Decoding: Lagrangian Hull Pruning for budget-constrained language model generation. ![updated today](./assets/badge-fresh-today-light.svg#gh-light-mode-only) ![updated today](./assets/badge-fresh-today-dark.svg#gh-dark-mode-only)

### Trust and autonomous agents

- **[docutrust](https://github.com/rajveersinh-is-dev/docutrust)**: Sovereign trust fabric covering verifiable credentials, agent identity federation, mixnets, retrieval provenance and zero knowledge state machines. ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)
- **[autod](https://github.com/rajveersinh-is-dev/autod)**: Repository synthesizer that uses frontier models to invent, develop, verify and publish a working open source project every 48 hours. ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)
- **[repo-improver-bot](https://github.com/rajveersinh-is-dev/repo-improver-bot)**: Engineering bot that sorts repositories by domain and upgrades them with tests, docs, benchmarks and CI through automated pull requests. ![updated this week](./assets/badge-fresh-week-light.svg#gh-light-mode-only) ![updated this week](./assets/badge-fresh-week-dark.svg#gh-dark-mode-only)

---

## <img alt="" src="./assets/icons/toolbox.svg" width="22" align="absmiddle">Toolbox

**Languages**

<p align="center">
  <img alt="Languages" src="./assets/tech-languages-light.svg#gh-light-mode-only">
  <img alt="Languages" src="./assets/tech-languages-dark.svg#gh-dark-mode-only">
</p>

**Tools and frameworks**

<p align="center">
  <img alt="Tools and frameworks" src="./assets/tech-tools-light.svg#gh-light-mode-only">
  <img alt="Tools and frameworks" src="./assets/tech-tools-dark.svg#gh-dark-mode-only">
</p>

**Also working with**

Numba / NumPy / SciPy / Jupyter / WebGPU / PyQt6 / LLM agents / zero knowledge proofs / verifiable credentials

---

## <img alt="" src="./assets/icons/activity.svg" width="22" align="absmiddle">Contribution activity

<p align="center">
  <img alt="3D contribution graph" src="./profile-3d-contrib/profile-3d-calendar-light.svg#gh-light-mode-only" width="80%">
  <img alt="3D contribution graph" src="./profile-3d-contrib/profile-3d-calendar-dark.svg#gh-dark-mode-only" width="80%">
</p>

<p align="center">
  <img alt="Contribution breakdown" src="./profile-3d-contrib/profile-3d-radar-light.svg#gh-light-mode-only" width="40%">
  <img alt="Languages" src="./profile-3d-contrib/profile-3d-pie-light.svg#gh-light-mode-only" width="40%">
  <img alt="Contribution breakdown" src="./profile-3d-contrib/profile-3d-radar-dark.svg#gh-dark-mode-only" width="40%">
  <img alt="Languages" src="./profile-3d-contrib/profile-3d-pie-dark.svg#gh-dark-mode-only" width="40%">
</p>

---

<details>
<summary><b>How this page is built</b></summary>

Every image on this page is self-hosted and regenerated by a script:

- `make-profile-assets.py` - banner, tagline, facts strip, research map, seal, result cards, tech pills, paper badges, section icons
- `make-map.py` - animated 3D research map with drifting slabs and pulsing connectors
- `make-facts-svg.py` - contribution count, repo and manuscript numbers, footer refresh date (runs every hour)
- `make-freshness.py` - repo freshness badges for the Projects section (runs every hour)
- `split-3d-svg.py` - repaints the 3D contribution graph from the page palette (runs every hour)
- `make-tech-pills.py` - self-hosted tech stack pills replacing external badges

The `profile-facts` and `profile-3d` workflows run on a schedule and on every push to main, so the numbers and the graph stay current. Nothing is fetched from a hosted service at render time; every image is committed under `assets/` or `profile-3d-contrib/`.

</details>

---

## <img alt="" src="./assets/icons/reach.svg" width="22" align="absmiddle">Reach me

- Email: [daveaddams91@gmail.com](mailto:daveaddams91@gmail.com)
- GitHub: [@rajveersinh-is-dev](https://github.com/rajveersinh-is-dev)
- Issues and pull requests are open on all the repositories above.

Open to research collaboration, reproducibility bugs, and pull requests. Based in India, happy to work across time zones.

<p align="center">
  <img alt="gradient footer" src="./assets/footer-light.svg#gh-light-mode-only" width="100%">
  <img alt="gradient footer" src="./assets/footer-dark.svg#gh-dark-mode-only" width="100%">
</p>
