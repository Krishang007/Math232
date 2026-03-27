"""
Converted from `chapter6/sec6.1demo.ipynb`.

Section 6.1 demo: power method / eigenvector iteration with simple visualizations.
"""

from __future__ import annotations

import time

import matplotlib.pyplot as plt
import numpy as np


def _clear_output(wait: bool = True) -> None:
    try:
        from IPython.display import clear_output as ipy_clear_output  # type: ignore

        ipy_clear_output(wait=wait)
        return
    except Exception:
        pass

    # Basic terminal clear fallback (works outside Jupyter).
    print("\033[2J\033[H", end="")


def _unit(vector: np.ndarray) -> np.ndarray:
    vector = np.asarray(vector, dtype=float)
    norm = float(np.sqrt(np.dot(vector, vector)))
    if norm == 0:
        raise ValueError("Cannot normalize the zero vector.")
    return vector / norm


def _power_iteration(A: np.ndarray, x0: np.ndarray, steps: int = 15) -> tuple[list[np.ndarray], list[float]]:
    A = np.asarray(A, dtype=float)
    x = _unit(x0)

    vectors = [x]
    lambdas = [float(np.dot(A @ x, x))]

    for _ in range(steps):
        x = _unit(A @ x)
        vectors.append(x)
        lambdas.append(float(np.dot(A @ x, x)))

    return vectors, lambdas


def _animate_vectors(
    vectors: list[np.ndarray],
    eigenvector: np.ndarray,
    eigenspace_direction: np.ndarray,
    *,
    xlim: tuple[float, float],
    ylim: tuple[float, float],
    num_vectors: int = 6,
    pause_s: float = 0.5,
    v_text_xy: tuple[float, float],
    block_end: bool = False,
) -> None:
    plt.ion()
    unit_v = _unit(eigenvector)
    direction = _unit(eigenspace_direction)

    fig, ax = plt.subplots()
    for shown in range(num_vectors + 1):
        _clear_output(wait=True)
        ax.clear()
        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)

        ax.spines["left"].set_position("zero")
        ax.spines["bottom"].set_position("zero")
        ax.spines["right"].set_color("none")
        ax.spines["top"].set_color("none")

        if shown >= 1:
            ax.quiver(
                0,
                0,
                unit_v[0],
                unit_v[1],
                angles="xy",
                scale_units="xy",
                scale=1,
                color=(1, 0, 1),
                width=0.006,
                headwidth=3,
                headlength=4,
            )
            ax.text(v_text_xy[0], v_text_xy[1], "$v$", fontsize=12, ha="left", va="bottom", color=(1, 0, 1))

            t = np.linspace(-2, 2, 100)
            ax.plot(t * direction[0], t * direction[1], "--", color=(1, 0, 1), alpha=0.3, linewidth=2)

        for i in range(min(shown, num_vectors)):
            ax.quiver(
                0,
                0,
                vectors[i][0],
                vectors[i][1],
                angles="xy",
                scale_units="xy",
                scale=1,
                color=(0, 0.6, 1),
                width=0.006,
                headwidth=3,
                headlength=4,
            )
            ax.text(
                vectors[i][0],
                vectors[i][1],
                f"$x_{i}$",
                fontsize=12,
                ha="left",
                va="bottom",
                color=(0, 0.6, 1),
            )

        fig.canvas.draw_idle()
        plt.pause(pause_s)

    plt.ioff()
    if block_end:
        plt.show()


def demo_example_1() -> None:
    A = np.array([[2, -4], [-1, -1]], dtype=float)  # eigenvalues -2, 3
    eigenvector = np.array([4, -1], dtype=float)  # eigenvector for eigenvalue 3

    print("Example 1")
    print("A =\n", A)
    print("unit eigenvector v =", _unit(eigenvector))

    vectors, lambdas = _power_iteration(A, x0=np.array([1, 0], dtype=float), steps=15)
    print("\nFirst few Rayleigh quotient approximations:")
    for i in range(min(6, len(lambdas))):
        print(f"  λ^({i}) = {lambdas[i]}")

    _animate_vectors(
        vectors,
        eigenvector=eigenvector,
        eigenspace_direction=eigenvector,
        xlim=(-0.5, 1.5),
        ylim=(-1, 0.5),
        num_vectors=6,
        pause_s=0.5,
        v_text_xy=(1.0, -0.25),
        block_end=False,
    )


def demo_example_2() -> None:
    A = np.array([[3, 2], [2, 3]], dtype=float)
    eigenvector = np.array([1, 1], dtype=float)  # eigenvector for eigenvalue 5

    print("Example 2")
    print("A =\n", A)
    print("unit eigenvector v =", _unit(eigenvector))

    vectors, lambdas = _power_iteration(A, x0=np.array([1, 0], dtype=float), steps=15)
    for i in range(len(vectors)):
        print(f"x_{i:<2} = {vectors[i]}, and λ^({i:<2}) = {lambdas[i]}")

    _animate_vectors(
        vectors,
        eigenvector=eigenvector,
        eigenspace_direction=eigenvector,
        xlim=(-0.5, 1.5),
        ylim=(-0.5, 1.0),
        num_vectors=6,
        pause_s=0.5,
        v_text_xy=(0.7, 0.8),
        block_end=True,
    )


def main() -> None:
    start = time.time()
    demo_example_1()
    demo_example_2()
    print(f"\nDone in {time.time() - start:.2f}s")


if __name__ == "__main__":
    main()
