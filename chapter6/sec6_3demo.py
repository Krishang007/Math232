"""
Converted from `chapter6/sec6.3demo.ipynb`.

Section 6.3 demo: a simple Markov chain example and steady-state computation.
"""

from __future__ import annotations

import numpy as np

from rref import rref


def main() -> None:
    P = np.array(
        [
            [0.5, 0.4, 0.6],
            [0.2, 0.2, 0.3],
            [0.3, 0.4, 0.1],
        ],
        dtype=float,
    )
    print("P =\n", P)

    x = np.array([0.0, 1.0, 0.0])  # initial state (lion starts in reserve 2)
    print(f"\nx0 = {x}")

    for i in range(1, 16):
        x = P @ x
        print(f"x{i} = {x}")

    print("\nRREF(P - I):")
    rref_matrix, pivots = rref(P - np.eye(3))
    print(rref_matrix)
    print("pivot columns:", pivots)

    # Read off a steady-state eigenvector for eigenvalue 1 from the RREF above.
    v = np.array([1.875, 0.84375, 1.0], dtype=float)
    q = v / float(np.sum(v))
    print("\nSteady-state distribution q =")
    print(q)


if __name__ == "__main__":
    main()

