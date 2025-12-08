from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Tuple

import numpy as np

Array = np.ndarray


@dataclass
class KuramotoConfig:
    """
    Configuration for a Kuramoto-style synchronization model over N oscillators.

    Attributes
    ----------
    omega : Array
        Natural frequencies (shape (N,)).
    K_low : float
        Coupling strength during "diastole" (low synchronization).
    K_high : float
        Coupling strength during "systole" (high synchronization).
    t_switch_on : float
        Time at which to switch from low to high coupling.
    t_switch_off : float
        Time at which to return to low coupling.
    """
    omega: Array
    K_low: float = 0.5
    K_high: float = 4.0
    t_switch_on: float = 10.0
    t_switch_off: float = 40.0

    def coupling(self, t: float) -> float:
        """Time-varying coupling K(t) implementing a simple breathing schedule."""
        if t < self.t_switch_on:
            return self.K_low
        if t > self.t_switch_off:
            return self.K_low
        return self.K_high


def kuramoto_rhs(
    t: float,
    theta: Array,
    omega: Array,
    adjacency: Array,
    K: float,
) -> Array:
    """
    Right-hand side of the Kuramoto ODE:

        d theta_i / dt = omega_i + (K / N) * sum_j A_ij * sin(theta_j - theta_i)

    Parameters
    ----------
    t : float
        Time (unused, but included for API compatibility).
    theta : Array
        Phase vector of shape (N,).
    omega : Array
        Natural frequencies, shape (N,).
    adjacency : Array
        Symmetric adjacency matrix A, shape (N, N).
    K : float
        Coupling strength at time t.

    Returns
    -------
    dtheta_dt : Array
        Time derivative of theta, shape (N,).
    """
    del t  # unused
    N = theta.size

    # Compute pairwise phase differences: theta_j - theta_i
    theta_i = theta.reshape(N, 1)
    theta_j = theta.reshape(1, N)
    phase_diff = theta_j - theta_i  # shape (N, N)

    coupling_term = (adjacency * np.sin(phase_diff)).sum(axis=1) / max(N, 1)

    return omega + K * coupling_term


def simulate_kuramoto(
    t_span: Array,
    theta0: Array,
    omega: Array,
    adjacency: Array,
    coupling_schedule: Callable[[float], float],
) -> Array:
    """
    Simulate the Kuramoto system using simple explicit Euler integration.

    Parameters
    ----------
    t_span : Array
        1D array of time points (monotonically increasing).
    theta0 : Array
        Initial phases, shape (N,).
    omega : Array
        Natural frequencies, shape (N,).
    adjacency : Array
        Adjacency matrix, shape (N, N).
    coupling_schedule : Callable[[float], float]
        Function K(t) returning coupling strength at time t.

    Returns
    -------
    theta_hist : Array
        Phase history, shape (len(t_span), N).
    """
    theta = theta0.astype(float).copy()
    T = t_span.size
    N = theta.size

    theta_hist = np.zeros((T, N), dtype=float)
    theta_hist[0] = theta

    for k in range(1, T):
        t_prev = float(t_span[k - 1])
        t_curr = float(t_span[k])
        dt = t_curr - t_prev

        K = coupling_schedule(t_prev)
        dtheta = kuramoto_rhs(t_prev, theta, omega, adjacency, K)
        theta = theta + dt * dtheta
        theta_hist[k] = theta

    return theta_hist


def order_parameter(theta: Array) -> Tuple[float, float]:
    """
    Compute the Kuramoto order parameter (r, psi):

        r e^{i psi} = (1/N) sum_j e^{i theta_j}

    r in [0, 1] measures phase coherence; psi is the mean phase.
    """
    z = np.exp(1j * theta)
    mean_z = np.mean(z)
    r = float(np.abs(mean_z))
    psi = float(np.angle(mean_z))
    return r, psi
