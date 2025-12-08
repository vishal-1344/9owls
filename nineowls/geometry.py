from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Tuple

import math
import numpy as np

Array = np.ndarray


@dataclass
class GeometryConfig:
    """
    Configuration for 9 Owls geometric layouts.

    mode:
        - "twisted_prism": Thomson-like N=9 twisted prism configuration.
        - "tammes_like":   Separation-maximizing Fibonacci sphere layout.
    """
    mode: Literal["twisted_prism", "tammes_like"] = "twisted_prism"
    adjacency_angle_deg: float = 80.0  # max geodesic distance for edges


def spherical_to_cart(lat_rad: float, lon_rad: float) -> Array:
    """
    Convert spherical coordinates (latitude, longitude) to Cartesian coordinates
    on the unit sphere S^2.

    lat_rad: latitude in radians (-pi/2 .. pi/2)
    lon_rad: longitude in radians (-pi .. pi)
    """
    x = math.cos(lat_rad) * math.cos(lon_rad)
    y = math.cos(lat_rad) * math.sin(lon_rad)
    z = math.sin(lat_rad)
    return np.array([x, y, z], dtype=float)


def twisted_prism_positions() -> Array:
    """
    Construct a Thomson-like twisted prism configuration for N=9 points on S^2.

    We use three equilateral triangles:
      - north triad at +45 degrees latitude (strategy),
      - equatorial triad at 0 degrees (operations),
      - south triad at -45 degrees (foundations),

    with the north/south triads rotated by +60 degrees relative to the equator.
    """
    lat_deg = np.array([45.0, 0.0, -45.0], dtype=float)
    lat_rad = np.deg2rad(lat_deg)

    long_equator = np.deg2rad(np.array([0.0, 120.0, 240.0], dtype=float))
    long_shifted = long_equator + np.deg2rad(60.0)

    pts = []

    # North polar triad (strategy) – shifted
    for lam in long_shifted:
        pts.append(spherical_to_cart(lat_rad[0], lam))

    # Equatorial triad (operations)
    for lam in long_equator:
        pts.append(spherical_to_cart(lat_rad[1], lam))

    # South polar triad (foundations) – shifted
    for lam in long_shifted:
        pts.append(spherical_to_cart(lat_rad[2], lam))

    return np.vstack(pts)  # shape (9, 3)


def fibonacci_sphere_positions(n: int) -> Array:
    """
    Generate n approximately uniformly spaced points on the unit sphere S^2
    using the Fibonacci spiral construction (good Tammes-like approximation).
    """
    indices = np.arange(0, n, dtype=float) + 0.5
    phi = math.pi * (3.0 - math.sqrt(5.0))  # golden angle

    y = 1.0 - (2.0 * indices / n)
    radius = np.sqrt(1.0 - y * y)
    theta = phi * indices

    x = radius * np.cos(theta)
    z = radius * np.sin(theta)

    pts = np.stack([x, y, z], axis=1)
    # Normalize just to be safe
    pts /= np.linalg.norm(pts, axis=1, keepdims=True) + 1e-12
    return pts


def adjacency_from_threshold(positions: Array, max_geodesic_distance: float) -> Array:
    """
    Build a symmetric adjacency matrix A_ij using a geodesic distance threshold.

    positions: array of shape (N, 3) on the unit sphere.
    max_geodesic_distance: threshold in radians.
    """
    N = positions.shape[0]
    A = np.zeros((N, N), dtype=float)

    for i in range(N):
        for j in range(i + 1, N):
            dot = float(np.clip(np.dot(positions[i], positions[j]), -1.0, 1.0))
            angle = math.acos(dot)
            if angle <= max_geodesic_distance:
                A[i, j] = 1.0
                A[j, i] = 1.0

    return A


def get_geometry(config: GeometryConfig) -> Tuple[Array, Array]:
    """
    Construct positions (N,3) and adjacency matrix (N,N) for the specified mode.
    """
    if config.mode == "twisted_prism":
        positions = twisted_prism_positions()
    elif config.mode == "tammes_like":
        positions = fibonacci_sphere_positions(9)
    else:
        raise ValueError(f"Unsupported geometry mode: {config.mode}")

    max_angle = math.radians(config.adjacency_angle_deg)
    adjacency = adjacency_from_threshold(positions, max_angle)
    return positions, adjacency
