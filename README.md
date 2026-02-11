# A Geometric Architecture for High-Level Multi-Agent Reasoning

**Project:** 9 Owls
**Status:** Research prototype / reference implementation

---

## Overview

**9 Owls** is a spatially instantiated, dynamically coupled multi-agent architecture.

Unlike standard “chain-of-thought” or workflow-based agent systems, 9 Owls treats intelligence as a **resonant state** emerging from the synchronization of nine distinct autonomous entities (the “Owls”) that inhabit a shared geometric manifold.

The system rejects opaque, ad hoc orchestration in favor of explicit, physics-style laws. The three pillars are:

1.  **Topological Necessity**
    Agent layout is determined by solutions to **Thomson** and **Tammes** problems on a sphere (energy-minimizing or separation-maximizing point sets).
2.  **Dynamical Synchronization**
    Reasoning is modeled as a **phase-locking process** governed by Kuramoto-style coupled oscillators.
3.  **Thermodynamic Regulation**
    Exploration vs. exploitation is governed by **Langevin dynamics**, with a “temperature” parameter that anneals the system from chaotic creativity to crystallized decision-making.

This repository is the reference implementation for geometric layouts, dynamical control laws, and the 9 specialized agent roles.

---

## 1. Geometric Architectures

In 9 Owls, geometry is not decoration; it **determines** information flow. Distances and angles encode:
* Who can talk to whom at high bandwidth.
* How much influence one agent can exert on another.
* Whether the system is in a stable or exploratory configuration.



We implement three main geometric modes:

### 1.1 Twisted Prism (Thomson N = 9)
Derived from the $N = 9$ solution of the **Thomson problem** (minimizing total electrostatic potential on the sphere).

* **Structure:** Three equilateral triangles stacked along the vertical axis ($Z$), with the top and bottom rotated by $60^{\circ}$ relative to the equator.
    * **North polar triad:** Strategy
    * **Equatorial triad:** Operations
    * **South polar triad:** Foundations
* **Function:** High stability and balanced influence. Used for crisis response, safety-critical control, and situations where multiple value systems must be respected.

**Triad Hierarchy:**
* **North Pole – Strategy:** Planning, abstract reasoning, meta-cognition.
* **Equator – Operations:** Perception, action, short-term memory. Acts as the high-speed bus.
* **South Pole – Foundations:** Long-term memory, world model, ethics and safeguards.

### 1.2 Adversarial Sphere (Tammes N = 9)
Derived from the $N = 9$ solution of the **Tammes problem** (maximizing the minimum distance between points on a sphere).

* **Structure:** Agents are packed to **maximize minimum pairwise separation**. Each Owl is as far as possible from all others on the surface of the sphere.
* **Function:** Maximum cognitive diversity. Used for scientific discovery, hypothesis generation, and adversarial brainstorming.
* **Dynamics:** A “Tammes force” penalizes belief convergence. Agents are encouraged to hold maximally orthogonal priors until a separate convergence phase is triggered.

### 1.3 Hyperbolic Parliament
Here, the agents are embedded in a hyperbolic disk (e.g., Poincaré disk).

* **Structure:** One central **integrator** in the interior, eight peripheral **specialists** near the boundary.
* **Function:** Hierarchical synthesis. Specialists operate in deep, isolated conceptual regions. All cross-domain communication must pass through the central Owl, encouraging coherent, global narratives from highly diverse expertise.
* **Use Case:** Interdisciplinary synthesis and long-horizon planning.

---

## 2. System Dynamics

The 9 Owls do not just vote or pass messages. They **oscillate, couple, and cool down** according to explicit dynamical rules.

A typical cycle has a “breathing” pattern:
* **Diastole:** Low coupling, high diversity.
* **Systole:** High coupling, consensus formation.



### 2.1 Kuramoto Synchronization
Each Owl $i$ has a phase $\theta_i(t)$ representing its reasoning cycle. A simplified Kuramoto-style update:

$$
\frac{d\theta_i}{dt} = \omega_i + \frac{K(t)}{N} \sum_j A_{ij} \sin(\theta_j - \theta_i)
$$

Where:
* $\omega_i$: Natural frequency (e.g., fast perceptual agents vs. slower ethics/meta).
* $K(t)$: Time-varying coupling strength controlled by a meta-cognitive loop.
* $A_{ij}$: Adjacency matrix derived from the chosen geometric layout.

**Breathing Loop:**
1.  **Diastole (low $K$):** Desynchronization. Agents explore independently, perform internal red-teaming, and check each other’s assumptions.
2.  **Systole (high $K$):** Phase locking. Threads of reasoning collapse into a shared conclusion or plan.

### 2.2 Riemannian Consensus
Belief states often live on curved manifolds (e.g., probability distributions, rotations, hyperbolic embeddings), not plain Euclidean space. Instead of naïve averaging, 9 Owls uses a Riemannian consensus procedure:

$$
x_{\text{next}} = \text{Exp}_x \left( \epsilon \sum_j w_{ij} \text{Log}_x(x_j) \right)
$$

Where:
* $\text{Log}_x(x_j)$: Maps neighbor states into the tangent space at $x$.
* $\text{Exp}_x(\cdot)$: Maps the updated direction back onto the manifold.
* $w_{ij}$: Encodes trust, confidence, or structural importance.

This keeps the consensus state valid on the underlying manifold and avoids “tearing” the geometry.

### 2.3 Langevin Annealing (Temperature of Thought)
To escape local optima and avoid premature convergence, the global state $X_t$ can follow a Langevin-style stochastic differential equation:

$$
dX_t = -\nabla U(X_t) dt + \sqrt{2T} dW_t
$$

Where:
* $U$: Energy or objective function (e.g., disagreement, risk, or free energy).
* $T$: Temperature parameter set by a meta agent.
* $W_t$: Brownian noise.

**Interpretation:**
* **High $T$ (“hot cognition”):** Exploratory, creative, noisy.
* **Low $T$ (“cold cognition”):** Precise, convergent, risk-averse.
* **Annealing:** A schedule gives a controlled transition from “imagine” to “decide,” with the ability to re-heat if new evidence or ethical alarms appear.

---

## 3. Agent Roster: The Nine Owls

The 9 Owls are functionally heterogeneous and mapped to the geometric triads.

### 3.1 Operational Triad (Equator)
*High-bandwidth interface to the environment.*

* **Owl-Perception (Oper) – The Observer:** Multimodal encoding into latent space.
* **Owl-Action (Oact) – The Executor:** Tool use, API calls, external actuation.
* **Owl-Communication (Ocom) – The Narrator:** Dialogue with users, explanation, external language interface.

### 3.2 Strategic Triad (North Pole)
*Abstract reasoning and global control.*

* **Owl-Planning (Oplan) – The Architect:** Goal decomposition, search over futures, plan refinement.
* **Owl-Reasoning (Orea) – The Critic:** Logical checks, consistency analysis, counterexample search.
* **Owl-Meta (Ometa) – The Controller:** Adjusts global parameters ($K, T$), monitors uncertainty and stopping conditions.

### 3.3 Foundational Triad (South Pole)
*Identity, memory, and safety.*

* **Owl-Memory (Omem) – The Archivist:** Long-term memory, retrieval, episodic context.
* **Owl-WorldModel (Oworld) – The Simulator:** Predictive modeling of environment dynamics.
* **Owl-Ethics (Oeth) – The Guardian:** Values, constraints, and veto power over unsafe or misaligned plans.

### 3.4 Jester Mode
One Owl (often **Orea**, or a rotating seat) can be designated as the **Jester**:
* Rewarded for challenging consensus.
* Tasked with generating alternative explanations and failure modes.
* Ensures the swarm never becomes complacent.

---

## 4. Code Layout (Planned)

The Python package is organized as follows:

```text
nineowls/
  geometry.py     # Thomson/Tammes point generation on S², hyperbolic layouts,
                  # construction of adjacency matrices from geometry
  dynamics.py     # Kuramoto integration, Riemannian consensus, Langevin/annealing
  agents.py       # Definitions of the 9 Owl roles
                  # Typed interfaces for plugging in models (LLM, world model, retriever)
  clio.py         # CLIO: “Cognitive Loop via In-Situ Optimization”
                  # Runs full reasoning cycles: init -> diastole -> systole -> report

experiments/
  03_breathing_cycle.py  # Breathing Kuramoto cycle with simple plots

requirements.txt
README.md
LICENSE
````

-----

## 5\. Dependencies (Planned)

Core numerical and plotting stack:

  * `numpy`
  * `scipy`
  * `matplotlib`

Additional dependencies (e.g., `networkx`, `torch`, `jax`, `notebooks`) may be added as the simulator matures.

Install core dependencies via:

```bash
pip install -r requirements.txt
```

-----

## 6\. Status

This repository is currently in the **theory $\to$ code translation** phase.

The underlying geometry and dynamics are specified in the technical report. Python modules will be implemented incrementally, starting from geometric layouts and a simple Kuramoto “breathing” demo for the nine oscillators.

-----

## 7\. Citation

If you reference this architecture, please cite:

> **“9 Owls System: A Geometric Multi-Agent Cognitive Engine,” Technical Report, 2025.**


