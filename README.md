# 9 Owls: A Geometric Architecture for Multi-Agent Reasoning

**Status:** Research prototype / reference implementation  
**Spec:** “9 Owls System: A Geometric Architecture for Multi-Agent Reasoning” (2025)

---

## Overview

**9 Owls** is a spatially instantiated, dynamically coupled multi-agent architecture.

Unlike standard “chain-of-thought” or workflow-based agent systems, 9 Owls treats
intelligence as a **resonant state** emerging from the synchronization of nine
distinct autonomous entities (the “Owls”) that inhabit a shared geometric manifold.

The system rejects opaque, ad hoc orchestration in favor of explicit physical-style
law. The three pillars are:

1. **Topological Necessity**  
   Agent layout is determined by solutions to **Thomson** and **Tammes** problems
   on a sphere (energy-minimizing or separation-maximizing point sets).

2. **Dynamical Synchronization**  
   Reasoning is modeled as a **phase-locking process** governed by
   Kuramoto-style coupled oscillators.

3. **Thermodynamic Regulation**  
   Exploration vs. exploitation is governed by **Langevin dynamics**, with a
   “temperature” parameter that anneals the system from chaotic creativity to
   crystallized decision-making.

This repository is the reference implementation for:

- geometric layouts,
- dynamical control laws,
- and the 9 specialized agent roles.

---

## 1. Geometric Architectures

In 9 Owls, geometry is not decoration; it **determines** information flow.

Distances and angles encode:

- who can talk to whom at high bandwidth,
- how much influence one agent can exert on another,
- whether the system is in a stable or exploratory configuration.

We implement (or plan to implement) three main geometric modes.

### 1.1 Twisted Prism (Thomson N = 9)

Derived from the N = 9 solution of the **Thomson problem** (minimizing total
electrostatic potential).

- **Structure**

  Three equilateral triangles stacked along the vertical axis (Z), with the
  top and bottom rotated by 60 degrees relative to the equator:

  - North polar triad (strategy)
  - Equatorial triad (operations)
  - South polar triad (foundations)

- **Function**

  High stability and balanced influence. Used for:

  - crisis response,
  - safety-critical control,
  - situations where multiple value systems must be respected.

- **Triad hierarchy**

  - **North Pole – Strategy**  
    Planning, abstract reasoning, meta-cognition.

  - **Equator – Operations**  
    Perception, action, short-term memory. Acts as the high-speed bus.

  - **South Pole – Foundations**  
    Long-term memory, world model, ethics and safeguards.

### 1.2 Adversarial Sphere (Tammes N = 9)

Derived from the N = 9 solution of the **Tammes problem** (maximizing the
minimum distance between points on a sphere).

- **Structure**

  Agents are packed to **maximize minimum pairwise separation**. Each Owl is as
  far as possible from all others on the surface of the sphere.

- **Function**

  Maximum cognitive diversity. Used for:

  - scientific discovery,
  - hypothesis generation,
  - adversarial brainstorming.

- **Dynamics**

  A “Tammes force” penalizes belief convergence. Agents are encouraged to hold
  maximally orthogonal priors until a separate convergence phase is triggered.

### 1.3 Hyperbolic Parliament

Here, the agents are embedded in a hyperbolic disk (e.g., Poincaré disk model).

- **Structure**

  - One central **integrator** in the interior.
  - Eight peripheral **specialists** near the boundary.

- **Function**

  Hierarchical synthesis:

  - Specialists operate in deep, isolated conceptual regions.
  - All cross-domain communication must pass through the central Owl.
  - Encourages coherent, global narratives from highly diverse expertise.

Use case: **interdisciplinary synthesis** and long-horizon planning.

---

## 2. System Dynamics

The “9 Owls” do not just vote or pass messages. They **oscillate, couple, and
cool down** according to explicit dynamical rules. A typical cycle has a
“breathing” pattern:

- **Diastole**: Low coupling, high diversity.
- **Systole**: High coupling, consensus formation.

### 2.1 Kuramoto Synchronization

Each Owl i has a phase `theta_i(t)` representing its reasoning cycle.

A simplified Kuramoto-style update is:

```text
d theta_i / dt = omega_i
                 + (K(t) / N) * sum_j A_ij * sin(theta_j - theta_i)


Where:

omega_i is the natural frequency (fast perceptual agents vs slower ethics/meta),

K(t) is a time-varying coupling strength controlled by a meta-cognitive loop,

A_ij is the adjacency matrix derived from the chosen geometric layout.

Breathing loop:

Diastole (low K)
Desynchronization: agents explore independently, perform internal red-teaming,
and check each other’s assumptions.

Systole (high K)
Phase locking: threads of reasoning collapse into a shared conclusion or plan.
```

### 2.2 Riemannian Consensus

Belief states often live on curved manifolds (e.g., probability distributions,
rotations, hyperbolic embeddings), not plain Euclidean space.

Instead of naïve averaging, 9 Owls uses a Riemannian consensus procedure:

x_next = Exp_x( epsilon * sum_j w_ij * Log_x(x_j) )


Log_x(x_j) maps neighbor states into the tangent space at x.

Exp_x(.) maps the update back to the manifold.

w_ij can encode trust or confidence.

This keeps the consensus state valid on the underlying manifold and avoids
“tearing” the geometry.

### 2.3 Langevin Annealing (Temperature of Thought)

To escape local optima and avoid premature convergence, the state X_t of the
system can follow a Langevin-style stochastic differential equation:

```
dX_t = - grad(U(X_t)) * dt + sqrt(2 * T) * dW_t
```


U is an energy or objective function (e.g., disagreement, risk, or free energy).

T is a temperature parameter set by the meta agent.

W_t is Brownian noise.

Interpretation:

High T (hot cognition) → exploratory, creative, noisy.

Low T (cold cognition) → precise, convergent, risk-averse.

Annealing schedule → controlled transition from “imagine” to “decide,”
with the ability to re-heat if new evidence or ethical alarms appear.

## 3. Agent Roster: The Nine Owls

The 9 Owls are functionally heterogeneous and mapped to the geometric triads.

### 3.1 Operational Triad (Equator)

High-bandwidth interface to the environment.

Owl-Perception (Oper) – The Observer
Multimodal encoding into latent space.

Owl-Action (Oact) – The Executor
Tool use, API calls, external actuation.

Owl-Communication (Ocom) – The Narrator
Dialogue with users, explanation, external language interface.

### 3.2 Strategic Triad (North Pole)

Abstract reasoning and control.

Owl-Planning (Oplan) – The Architect
Goal decomposition, search over futures, plan refinement.

Owl-Reasoning (Orea) – The Critic
Logical checks, consistency analysis, counterexample search.

Owl-Meta (Ometa) – The Controller
Adjusts global parameters (K, T), monitors uncertainty and stopping conditions.

### 3.3 Foundational Triad (South Pole)

Identity, memory, and safety.

Owl-Memory (Omem) – The Archivist
Long-term memory, retrieval, episodic context.

Owl-WorldModel (Oworld) – The Simulator
Predictive modeling of environment dynamics.

Owl-Ethics (Oeth) – The Guardian
Values, constraints, and veto power over unsafe or misaligned plans.

### 3.4 Jester Mode

One Owl (often Orea, or a rotating seat) can be designated as the Jester:

rewarded for challenging consensus,

tasked with generating alternative explanations and failure modes,

ensures the swarm never becomes complacent.

## 4. Code Layout (Planned)

The Python package is organized as follows:

nineowls/geometry.py

Thomson / Tammes point generation on S²

Hyperbolic (disk) layouts

Construction of adjacency matrices from geometry

nineowls/dynamics.py

Kuramoto integration

Riemannian consensus operators (stubs or implementations)

Langevin / annealing schedules

nineowls/agents.py

Definitions of the 9 Owl roles

Typed interfaces for plugging in models (e.g., LLM, world model, retriever)

nineowls/clio.py

CLIO: “Cognitive Loop via In-Situ Optimization”

Runs full reasoning cycles: initialization → diastole → systole → report

experiments/

03_breathing_cycle.py – breathing Kuramoto cycle with simple plots

Dependencies (planned)

numpy

scipy

matplotlib

Additional dependencies such as networkx, torch or jax, or notebook may
be added as the simulator matures.

Install core dependencies via:

pip install -r requirements.txt

Status

This repository is in the theory → code translation phase.

The underlying geometry and dynamics are fully specified in the technical report.

The Python modules will be implemented incrementally, starting from:

- geometric layouts, and

- a simple Kuramoto “breathing” demo for the nine oscillators.

Citation

If you reference this architecture, please cite:

“9 Owls System: A Geometric Multi-Agent Cognitive Engine,” Technical Report, 2025.



