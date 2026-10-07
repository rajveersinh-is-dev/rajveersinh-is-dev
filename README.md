<!--
  Profile README for Rajveersinh Pardeshi (@rajveersinh-is-dev)

  To publish: create a PUBLIC repo named exactly  rajveersinh-is-dev  and put this
  file at its root. A private repo will not show up on your profile.

  Notes for future edits:
  - The top wave is decoration only. capsule-render draws its own text with a
    CSS fade-in that many renderers never play, which leaves the words invisible.
    So there is no text in it, and the name below is a normal Markdown heading.
  - Every badge is plain shields.io. Dynamic GitHub badges (repo count) and
    multi-icon sets like skillicons have both proven unreliable here.
-->

<p align="center">
  <img alt="gradient banner" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=4c1d95,7c3aed,c026d3,2563eb&height=120&section=header&animation=fadeIn">
</p>

<h1 align="center">Rajveersinh Pardeshi</h1>

<p align="center">
  Computational mathematics / Scientific simulation / Verifiable systems
</p>

<p align="center">
  <a href="mailto:daveaddams91@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-daveaddams91@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white"></a>
  <a href="https://github.com/rajveersinh-is-dev"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-rajveersinh--is--dev-181717?style=for-the-badge&logo=github&logoColor=white"></a>
  <img alt="Location" src="https://img.shields.io/badge/Location-India-7c3aed?style=for-the-badge">
  <img alt="Open to collaboration" src="https://img.shields.io/badge/Open%20to%20collaboration-f97316?style=for-the-badge">
</p>

---

## About

Most of my work is in extremal graph theory and combinatorial geometry, where the aim is to settle small cases exactly rather than bound them loosely. Alongside that: missing data that is not missing at random, plasma confinement, and agents that write and verify their own successors.

I like results I can reproduce from scratch, and proofs that survive someone trying to break them. Most repositories ship a script that reruns the whole thing.

<table>
<tr>
<td width="50%" valign="top">

**What I work on**

- Extremal graph theory and combinatorial geometry. Small cases settled by enumeration, then a proof of why the enumeration stopped where it did.
- Missing data under MNAR. Honest imputation is a hard problem when the mechanism is unobserved.
- Formal safety layers. Reachability analysis wrapped around a control loop, so compliance holds in the worst case and not only on average.
- Confidential verification. Credentials, mixnets and proof systems for agent identity and retrieval provenance.
- GPU first simulation. Compute shaders and JIT compiled kernels, because the physics deserves better than a slow interpreted loop.

</td>
<td width="50%" valign="top">

**Currently**

- Plasma confinement stability, drift orbits and energetic particle losses.
- Whether critical transitions can be signaled early in complex systems, rather than explained after the fact.
- Automation that improves itself: agents generating, verifying and publishing successors.
- Making heavy mathematics legible and reproducible in public.

**Contact**

Open to research collaboration, reproducibility bugs, and PRs. Based in India, happy to work across time zones.

</td>
</tr>
</table>

---

## Projects

### Combinatorics and geometry

| Project | Result |
|:--|:--|
| **[convex-thrackle-census](https://github.com/rajveersinh-is-dev/convex-thrackle-census)** | Exact census of `2^(n-1) - n` maximal convex thrackles, with a residue bound and wedge lemma |
| **[triple-cover-convex-polygon](https://github.com/rajveersinh-is-dev/triple-cover-convex-polygon)** | Gap weight certificate giving a lower bound for all `n`, certified exact values through `n = 14` |
| **[polygon-triangulation-packing](https://github.com/rajveersinh-is-dev/polygon-triangulation-packing)** | Exact extremal theory for `tau(n)` and `kappa(n)`, with constructive proofs |
| **[maximal-convex-position-subsets](https://github.com/rajveersinh-is-dev/maximal-convex-position-subsets)** | Exact `f(n)` through `n = 9`, plus a point line duality theorem |
| **[edge-disjoint-triangle-packings](https://github.com/rajveersinh-is-dev/edge-disjoint-triangle-packings)** | Convex barrier, then a reduction to subcubic trees |
| **[cycle-spectra-connectivity](https://github.com/rajveersinh-is-dev/cycle-spectra-connectivity)** | Sharp minimum cycle count for `k` connected graphs, exact 3 connected spectrum to order 9 |
| **[connected-labeled-parity](https://github.com/rajveersinh-is-dev/connected-labeled-parity)** | Exact 2-adic valuations of connected labeled graphs and digraphs |
| **[adic-diversity](https://github.com/rajveersinh-is-dev/adic-diversity)** | Largest number of distinct 2-adic valuations across the subset sums of `k` integers |

### Statistics and complex systems

| Project | Description |
|:--|:--|
| **[umbra](https://github.com/rajveersinh-is-dev/umbra)** | Python library for MNAR aware missing data diagnostics, identifiability bounds, and robust imputation when the data is not missing at random. |
| **[early-warning-complex-systems](https://github.com/rajveersinh-is-dev/early-warning-complex-systems)** | Framework for testing whether statistical, physical and information theoretic indicators can anticipate critical transitions and collapse. |

### Simulation and formal methods

| Project | Description |
|:--|:--|
| **[Tokamak-Py](https://github.com/rajveersinh-is-dev/Tokamak-Py)** | Numba accelerated N body electromagnetic plasma confinement engine, using Boris integration for stable particle pushing, with a PyQt6 interface. |
| **[terrain-erosion-engine](https://github.com/rajveersinh-is-dev/terrain-erosion-engine)** | Procedural terrain generator running hydraulic and thermal erosion on the GPU, using WebGPU compute shaders and Three.js. |
| **[certified-dose](https://github.com/rajveersinh-is-dev/certified-dose)** | Package, CLI and dashboard that put automated process control dosing inside a formal reachability analysis safety layer. |

### Trust and autonomous agents

| Project | Description |
|:--|:--|
| **[docutrust](https://github.com/rajveersinh-is-dev/docutrust)** | Sovereign trust fabric covering verifiable credentials, agent identity federation, mixnets, retrieval provenance and zero knowledge state machines. |
| **[autod](https://github.com/rajveersinh-is-dev/autod)** | Repository synthesizer that uses frontier models to invent, develop, verify and publish a working open source project every 48 hours. |
| **[repo-improver-bot](https://github.com/rajveersinh-is-dev/repo-improver-bot)** | Engineering bot that sorts repositories by domain and upgrades them with tests, docs, benchmarks and CI through automated pull requests. |

---

## Toolbox

**Languages**

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white">
  <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
  <img alt="LaTeX" src="https://img.shields.io/badge/LaTeX-008080?style=for-the-badge&logo=latex&logoColor=white">
  <img alt="WGSL" src="https://img.shields.io/badge/WGSL-1B6AC9?style=for-the-badge&logo=google&logoColor=white">
</p>

**Tools and frameworks**

<p>
  <img alt="Three.js" src="https://img.shields.io/badge/Three.js-000000?style=for-the-badge&logo=threedotjs&logoColor=white">
  <img alt="Node.js" src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white">
  <img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
  <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=black">
  <img alt="Git" src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white">
</p>

**Also working with**

`Numba` / `NumPy` / `SciPy` / `Jupyter` / `WebGPU` / `PyQt6` / `LLM agents` / `Zero knowledge proofs` / `Verifiable credentials`

---

## Reach me

- Email: [daveaddams91@gmail.com](mailto:daveaddams91@gmail.com)
- GitHub: [@rajveersinh-is-dev](https://github.com/rajveersinh-is-dev)
- Issues and pull requests are open on all the repositories above.

<p align="center">
  <img alt="gradient footer" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=c026d3,7c3aed,2563eb&height=80&section=footer&animation=fadeIn&reversal=true">
</p>
