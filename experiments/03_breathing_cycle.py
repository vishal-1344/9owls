from __future__ import annotations

import os
import sys

import matplotlib.pyplot as plt
import numpy as np

# Ensure the package is importable when running as a script
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.append(ROOT)

from nineowls.clio import ClioEngine  # type: ignore[import]


def main() -> None:
    engine = ClioEngine()
    result = engine.run_breathing_cycle(t_end=60.0, dt=0.05, seed=42)

    t = result.t
    r = result.r_hist

    plt.figure(figsize=(8, 4))
    plt.plot(t, r, label="Order parameter r(t)")
    plt.xlabel("time")
    plt.ylabel("phase coherence r")
    plt.title("9 Owls Kuramoto Breathing Cycle (Diastole → Systole → Diastole)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
