#program to compute and visualize matrix transformations
import numpy as np
import matplotlib.pyplot as plt
import sympy as smp
from matplotlib.patches import FancyArrowPatch
pi = np.pi

# ============================================================
# TRANSFORMATION MATRICES (refer to formulas in transformations.md)
# ============================================================

# --- Rotation ---
def rotation(theta):
    """Rotation matrix (counterclockwise by theta degrees)."""
    theta_rad = np.radians(theta)
    R = np.array([[np.cos(theta_rad), -np.sin(theta_rad)],
                  [np.sin(theta_rad),  np.cos(theta_rad)]])
    return R

# --- Scaling ---
def scaling(kx, ky):
    """Scaling matrix: scales x by kx, y by ky."""
    S = np.array([[kx, 0],
                  [0, ky]])
    return S

# --- Shear ---
def horizontal_shear(k):
    """Horizontal shear matrix (factor k).
    Effect: (x, y) -> (x + ky, y)"""
    H = np.array([[1, k],
                  [0, 1]])
    return H

def vertical_shear(k):
    """Vertical shear matrix (factor k).
    Effect: (x, y) -> (x, kx + y)"""
    V = np.array([[1, 0],
                  [k, 1]])
    return V

# --- Reflection ---
def reflection_x():
    """Reflection across the x-axis. (x, y) -> (x, -y)"""
    return np.array([[1,  0],
                     [0, -1]])

def reflection_y():
    """Reflection across the y-axis. (x, y) -> (-x, y)"""
    return np.array([[-1, 0],
                     [ 0, 1]])

def reflection_yx():
    """Reflection across the line y = x. (x, y) -> (y, x)"""
    return np.array([[0, 1],
                     [1, 0]])

def reflection_ynx():
    """Reflection across the line y = -x. (x, y) -> (-y, -x)"""
    return np.array([[ 0, -1],
                     [-1,  0]])

def reflection_line(theta):
    """General reflection across a line at angle theta (degrees) to x-axis."""
    theta_rad = np.radians(theta)
    R = np.array([[np.cos(2*theta_rad),  np.sin(2*theta_rad)],
                  [np.sin(2*theta_rad), -np.cos(2*theta_rad)]])
    return R

# ============================================================
# HELPER: check if a matrix is orthogonal
# ============================================================
def is_orthogonal(P, tol=1e-10):
    """Check if P is an orthogonal matrix (P^T P = I)."""
    I = np.eye(P.shape[0])
    return np.allclose(P.T @ P, I, atol=tol)

# ============================================================
# VISUALIZATION
# ============================================================

def _make_unit_square():
    """Return vertices of the unit square as a 2×5 array (closed path)."""
    return np.array([[0, 1, 1, 0, 0],
                     [0, 0, 1, 1, 0]])

def _make_shape(kind="square"):
    """Return vertices of a simple shape for visualizing transformations."""
    if kind == "square":
        return _make_unit_square()
    elif kind == "triangle":
        return np.array([[0, 1, 0.5, 0],
                         [0, 0, 1,   0]])
    elif kind == "house":
        return np.array([[0, 1, 1, 0.5, 0, 0],
                         [0, 0, 1, 1.5, 1, 0]])
    elif kind == "arrow":
        return np.array([[0, 0.6, 0.6, 1, 0.5, 0, 0.4, 0.4, 0],
                         [0.4, 0.4, 0.7, 0.5, 0, 0.5, 0.7, 0.4, 0.4]])
    else:
        return _make_unit_square()

def visualize(matrix, shape="square", title=None):
    """
    Visualize the effect of a 2x2 transformation matrix on a shape.
    
    Parameters
    ----------
    matrix : 2x2 numpy array
        The transformation matrix.
    shape  : str
        One of 'square', 'triangle', 'house', 'arrow'.
    title  : str or None
        Plot title (auto-generated if None).
    """
    original = _make_shape(shape)
    transformed = matrix @ original

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Determine plot limits
    all_pts = np.hstack([original, transformed])
    margin = 0.5
    lo = all_pts.min() - margin
    hi = all_pts.max() + margin

    for ax, pts, label, color in zip(
        axes,
        [original, transformed],
        ["Original", "Transformed"],
        ["#2196F3", "#F44336"]
    ):
        ax.fill(pts[0], pts[1], alpha=0.25, color=color)
        ax.plot(pts[0], pts[1], 'o-', color=color, linewidth=2, markersize=5)
        ax.set_xlim(lo, hi)
        ax.set_ylim(lo, hi)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.axhline(0, color='k', linewidth=0.5)
        ax.axvline(0, color='k', linewidth=0.5)
        ax.set_title(label, fontsize=13, fontweight='bold')

    if title is None:
        title = f"Transformation Matrix\n{np.array2string(matrix, precision=3)}"
    fig.suptitle(title, fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

def visualize_overlay(matrix, shape="square", title=None):
    """
    Overlay original and transformed shapes on a single plot
    with basis vector arrows showing where e1 and e2 map to.
    """
    original = _make_shape(shape)
    transformed = matrix @ original

    fig, ax = plt.subplots(figsize=(7, 7))

    # Draw shapes
    ax.fill(original[0], original[1], alpha=0.2, color='#2196F3', label='Original')
    ax.plot(original[0], original[1], 'o-', color='#2196F3', lw=2, ms=5)

    ax.fill(transformed[0], transformed[1], alpha=0.2, color='#F44336', label='Transformed')
    ax.plot(transformed[0], transformed[1], 'o-', color='#F44336', lw=2, ms=5)

    # Draw basis vectors and their images
    origin = [0, 0]
    e1 = matrix[:, 0]  # image of e1
    e2 = matrix[:, 1]  # image of e2

    ax.annotate('', xy=[1, 0], xytext=origin,
                arrowprops=dict(arrowstyle='->', color='#1565C0', lw=2))
    ax.annotate('', xy=[0, 1], xytext=origin,
                arrowprops=dict(arrowstyle='->', color='#1565C0', lw=2))
    ax.annotate('', xy=e1, xytext=origin,
                arrowprops=dict(arrowstyle='->', color='#C62828', lw=2))
    ax.annotate('', xy=e2, xytext=origin,
                arrowprops=dict(arrowstyle='->', color='#C62828', lw=2))

    ax.text(1.05, -0.15, 'e₁', color='#1565C0', fontsize=11, fontweight='bold')
    ax.text(-0.2,  1.05, 'e₂', color='#1565C0', fontsize=11, fontweight='bold')
    ax.text(e1[0]+0.05, e1[1]-0.15, f'T(e₁)={e1.round(2)}', color='#C62828', fontsize=9)
    ax.text(e2[0]+0.05, e2[1]+0.05, f'T(e₂)={e2.round(2)}', color='#C62828', fontsize=9)

    # Limits
    all_pts = np.hstack([original, transformed, e1.reshape(2,1), e2.reshape(2,1)])
    margin = 0.8
    lo = all_pts.min() - margin
    hi = all_pts.max() + margin
    ax.set_xlim(lo, hi)
    ax.set_ylim(lo, hi)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color='k', lw=0.5)
    ax.axvline(0, color='k', lw=0.5)
    ax.legend(loc='upper left', fontsize=10)

    if title is None:
        title = f"Transformation Matrix\n{np.array2string(matrix, precision=3)}"
    ax.set_title(title, fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.show()

# ============================================================
# ANGLE INPUT HELPER — supports radians like "3*pi/2" or degrees
# ============================================================
def parse_angle(prompt):
    """Ask user for an angle, accepting degrees or radian expressions like 3*pi/4."""
    unit = input("  Angle units — (d)egrees or (r)adians? [d]: ").strip().lower()
    raw = input(f"  {prompt}: ").strip()
    # Evaluate expression (supports pi, e.g. "3*pi/2", "-pi/4", "5*pi/6")
    val = eval(raw, {"pi": np.pi, "np": np, "__builtins__": {}})
    if unit == "r":
        return np.degrees(val)   # convert to degrees for rotation()
    return float(val)

# ============================================================
# BUILD A SINGLE TRANSFORMATION FROM USER INPUT
# ============================================================
TRANSFORM_MENU = """  Transformations:
    rot      – Rotation (counterclockwise)
    scale    – Scaling
    hshear   – Horizontal Shear
    vshear   – Vertical Shear
    refx     – Reflection (x-axis)
    refy     – Reflection (y-axis)
    refyx    – Reflection (y = x)
    refynx   – Reflection (y = -x)
    refline  – General Reflection (line at angle θ)
    custom   – Custom 2×2 Matrix"""

def build_transform(prefix=""):
    """Interactively build one transformation matrix. Returns (matrix, label)."""
    t = input(f"{prefix}Type (rot/scale/hshear/vshear/refx/refy/refyx/refynx/refline/custom): ").strip().lower()
    if t == "rot":
        deg = parse_angle("Enter angle θ")
        return rotation(deg), f"Rotation({deg:.2f}°)"
    elif t == "scale":
        kx = float(input(f"{prefix}  kx (x-scale): "))
        ky = float(input(f"{prefix}  ky (y-scale): "))
        return scaling(kx, ky), f"Scale({kx},{ky})"
    elif t == "hshear":
        k = float(input(f"{prefix}  Shear factor k: "))
        return horizontal_shear(k), f"HShear({k})"
    elif t == "vshear":
        k = float(input(f"{prefix}  Shear factor k: "))
        return vertical_shear(k), f"VShear({k})"
    elif t == "refx":
        return reflection_x(), "Ref(x-axis)"
    elif t == "refy":
        return reflection_y(), "Ref(y-axis)"
    elif t == "refyx":
        return reflection_yx(), "Ref(y=x)"
    elif t == "refynx":
        return reflection_ynx(), "Ref(y=-x)"
    elif t == "refline":
        deg = parse_angle("Line angle θ")
        return reflection_line(deg), f"Ref(line@{deg:.2f}°)"
    elif t == "custom":
        print(f"{prefix}  Enter 2×2 matrix entries:")
        a = float(input(f"{prefix}    a (row1 col1): "))
        b = float(input(f"{prefix}    b (row1 col2): "))
        c = float(input(f"{prefix}    c (row2 col1): "))
        d = float(input(f"{prefix}    d (row2 col2): "))
        return np.array([[a, b], [c, d]]), "Custom"
    else:
        print("  Unknown type — using identity.")
        return np.eye(2), "Identity"

# ============================================================
# INTERACTIVE LOOP
# ============================================================
if __name__ == "__main__":
    np.set_printoptions(precision=4, suppress=True)

    print("="*58)
    print("   MATRIX TRANSFORMATIONS SOLVER & VISUALIZER  (Math 232)")
    print("="*58)

    while True:
        print()
        print("What would you like to do?")
        print("  1. Single transformation")
        print("  2. Compose multiple transformations")
        print("  3. Apply transformation to a specific vector")
        print("  4. Check if a matrix is orthogonal")
        print("  q. Quit")
        print()
        choice = input("Choice: ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break

        # ---- Single transformation ----
        if choice == "1":
            print()
            print(TRANSFORM_MENU)
            M, label = build_transform()

        # ---- Compose multiple transformations ----
        elif choice == "2":
            print()
            print(TRANSFORM_MENU)
            n = int(input("\n  How many transformations to compose? "))
            matrices = []
            labels = []
            for i in range(n):
                print(f"\n  --- Transformation {i+1} (applied {'first' if i == 0 else 'after #' + str(i)}) ---")
                Mi, li = build_transform(prefix="  ")
                matrices.append(Mi)
                labels.append(li)
                print(f"  [{li}] =\n{Mi}")
            # Compose: T_n ... T_2 T_1  (last entered is outermost)
            M = matrices[-1]
            for i in range(len(matrices)-2, -1, -1):
                M = M @ matrices[i]
            label = " ∘ ".join(reversed(labels))

        # ---- Apply to a vector ----
        elif choice == "3":
            print()
            print(TRANSFORM_MENU)
            M, label = build_transform()
            print(f"\n  [{label}] =\n{M}")
            x1 = float(input("\n  Enter vector x-component: "))
            x2 = float(input("  Enter vector y-component: "))
            v = np.array([x1, x2])
            result = M @ v
            print(f"\n  T({v}) = {result}")
            print(f"\n  Original length:    ||v|| = {np.linalg.norm(v):.4f}")
            print(f"  Transformed length: ||Tv|| = {np.linalg.norm(result):.4f}")
            # Skip visualization prompt for vector-only mode
            input("\nPress Enter to continue...")
            continue

        # ---- Orthogonality check ----
        elif choice == "4":
            print("\n  Enter 2×2 matrix entries:")
            a = float(input("    a (row1 col1): "))
            b = float(input("    b (row1 col2): "))
            c = float(input("    c (row2 col1): "))
            d = float(input("    d (row2 col2): "))
            P = np.array([[a, b], [c, d]])
            print(f"\n  Matrix:\n{P}")
            print(f"  P^T P =\n{P.T @ P}")
            print(f"  Determinant: {np.linalg.det(P):.4f}")
            print(f"  Orthogonal: {is_orthogonal(P)}")
            if is_orthogonal(P):
                det = np.linalg.det(P)
                if np.isclose(det, 1):
                    print("  → This is a ROTATION (det = +1)")
                elif np.isclose(det, -1):
                    print("  → This is a REFLECTION (det = -1)")
            input("\nPress Enter to continue...")
            continue
        else:
            print("Invalid choice, try again.")
            continue

        # ---- Display matrix info ----
        print(f"\n{'='*45}")
        print(f"Transformation: {label}")
        print(f"{'='*45}")
        print(f"Matrix:\n{M}")
        print(f"Determinant:  {np.linalg.det(M):.4f}")
        print(f"Orthogonal:   {is_orthogonal(M)}")
        if is_orthogonal(M):
            det = np.linalg.det(M)
            if np.isclose(det, 1):
                print("  → This is a ROTATION (det = +1)")
            elif np.isclose(det, -1):
                print("  → This is a REFLECTION (det = -1)")

        # ---- Optional: apply to a vector ----
        do_vec = input("\nApply to a specific vector? (y/n) [n]: ").strip().lower()
        if do_vec == "y":
            x1 = float(input("  x-component: "))
            x2 = float(input("  y-component: "))
            v = np.array([x1, x2])
            result = M @ v
            print(f"  T({v}) = {result}")

        # ---- Optional: visualize ----
        do_viz = input("Visualize? (y/n) [y]: ").strip().lower()
        if do_viz != "n":
            shape = input("  Shape (square/triangle/house/arrow) [square]: ").strip()
            if shape not in ("square", "triangle", "house", "arrow"):
                shape = "square"
            view = input("  View mode (side/overlay) [overlay]: ").strip()
            if view == "side":
                visualize(M, shape=shape, title=label)
            else:
                visualize_overlay(M, shape=shape, title=label)
