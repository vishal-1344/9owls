from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np

from .agents import OwlSpec, default_owl_specs
from .dynamics import (
    KuramotoConfig,
    simulate_kuramoto,
    order_parameter,
)
from .geometry import GeometryConfig, get_geometry


@dataclass
class ClioResult:
    """
    Result of a single CLIO breathing-cycle simulation.
    """
    t: np.ndarray
    theta_hist: np.ndarray
    r_hist: np.ndarray


@dataclass
class ClioEngine:
    """
    CLIO: Cognitive Loop via In-Situ Optimization.

    This minimal version runs a Kuramoto-based breathing cycle over N = 9
    oscillators using a chosen geometric layout and role specification.
    """
    geometry_config: GeometryConfig = GeometryConfig()
    owl_specs: Optional[list[OwlSpec]] = None

    def __post_init__(self) -> None:
        if self.owl_specs is None:
            self.owl_specs = default_owl_specs()

    def run_breathing_cycle(
        self,
        t_end: float = 60.0,
        dt: float = 0.05,
        seed: int = 0,
    ) -> ClioResult:
        """
        Run a single breathing cycle simulation with:
          - low coupling (diastole) at start/end,
          - high coupling (systole) in the middle.
        """
        rng = np.random.default_rng(seed)

        # Geometry and adjacency
        positions, adjacency = get_geometry(self.geometry_config)
        N = positions.shape[0]

        t = np.arange(0.0, t_end + dt, dt)

        # Assign natural frequencies: faster at equator, slower at poles (just as a demo)
        base_omega = 1.0
        omega = base_omega * np.ones(N, dtype=float)
        # small random variation
        omega += 0.1 * rng.standard_normal(N)

        cfg = KuramotoConfig(
            omega=omega,
            K_low=0.5,
            K_high=4.0,
            t_switch_on=10.0,
            t_switch_off=40.0,
        )

        def K_of_t(t_val: float) -> float:
            return cfg.coupling(t_val)

        # Random initial phases
        theta0 = rng.uniform(low=0.0, high=2.0 * np.pi, size=N)

        theta_hist = simulate_kuramoto(
            t_span=t,
            theta0=theta0,
            omega=omega,
            adjacency=adjacency,
            coupling_schedule=K_of_t,
        )

        r_hist = np.zeros_like(t, dtype=float)
        for k in range(t.size):
            r, _ = order_parameter(theta_hist[k])
            r_hist[k] = r

        return ClioResult(t=t, theta_hist=theta_hist, r_hist=r_hist)
