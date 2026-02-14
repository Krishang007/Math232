## 3.3 GEOMETRIC TRANSFORMATIONS

### Rotation Matrix (Counterclockwise by angle θ)

**Formula:**

`R_θ = [cos θ  -sin θ]
      [sin θ   cos θ]`

**Derivation:** Images of standard basis vectors

`e₁ = (1, 0) rotates to (cos θ, sin θ)      (first column)
e₂ = (0, 1) rotates to (-sin θ, cos θ)     (second column)`

**Properties:**

`Preserves length: ||R_θ x|| = ||x||
Preserves angles: (R_θ u)·(R_θ v) = u·v`

---

### Scaling Matrix

**Formula:**

`S = [k_x  0  ]
    [0   k_y]`

**Effect:** Scales x-component by k_x, y-component by k_y

**Special cases:**

`k_x = k_y: Uniform scaling (similar triangles)
k_x ≠ k_y: Differential scaling
k = 1/2: Compression
k = 2: Expansion`

---

### Shear Matrices

**Horizontal shear (factor k):**

`H = [1  k]
    [0  1]

Effect: (x, y) ↦ (x + ky, y)
(y-component fixed, x-component changes with y)`

**Vertical shear (factor k):**

`V = [1  0]
    [k  1]

Effect: (x, y) ↦ (x, kx + y)
(x-component fixed, y-component changes with x)`

---

### Reflection Matrices

**Across x-axis:**

`[1   0]     Effect: (x, y) ↦ (x, -y)
[0  -1]`

**Across y-axis:**

`[-1  0]     Effect: (x, y) ↦ (-x, y)
[0   1]`

**Across line y = x:**

`[0  1]     Effect: (x, y) ↦ (y, x)  (swap coordinates)
[1  0]`

**Across line y = -x:**

`[0  -1]     Effect: (x, y) ↦ (-y, -x)
[-1  0]`

**General reflection across line at angle θ to x-axis:**

`[cos 2θ   sin 2θ]
[sin 2θ  -cos 2θ]`

---

### Orthogonal Matrices

**Definition:** Square matrix P is **orthogonal** if:

`P^T P = I

Equivalently: P^(-1) = P^T`

## TRANSFORMATION MATRICES ⭐ MUST MEMORIZE

### Rotation (counterclockwise by θ)

`R_θ = [cos θ  -sin θ]
      [sin θ   cos θ]

Example R_π/4 = [√2/2  -√2/2]
                [√2/2   √2/2]`

**Derivation:** Images of standard basis vectors

`e₁ = (1, 0) rotates to (cos θ, sin θ)      (first column)
e₂ = (0, 1) rotates to (-sin θ, cos θ)     (second column)`

**Properties:**

`Preserves length: ||R_θ x|| = ||x||
Preserves angles: (R_θ u)·(R_θ v) = u·v`

### Scaling

`S = [k_x  0  ]   (multiply x by k_x, y by k_y)
    [0   k_y]

Example: S = [2  0]  (double x, keep y)
             [0  1]`

**Effect:** Scales x-component by k_x, y-component by k_y

**Special cases:**

`k_x = k_y: Uniform scaling (similar triangles)
k_x ≠ k_y: Differential scaling
k = 1/2: Compression
k = 2: Expansion`

### Shear (Horizontal)

### Shear Matrices

**Horizontal shear (factor k):**

`H = [1  k]
    [0  1]

Effect: (x, y) ↦ (x + ky, y)
(y-component fixed, x-component changes with y)`

`H = [1  k]   (x-component shifts by k·y)
    [0  1]

Example: H = [1  2]
             [0  1]`

### Shear (Vertical)

**Vertical shear (factor k):**

`V = [1  0]
    [k  1]

Effect: (x, y) ↦ (x, kx + y)
(x-component fixed, y-component changes with x)`

`V = [1  0]   (y-component shifts by k·x)
    [k  1]

Example: V = [1  0]
             [3  1]`

Reflection Matrices

### Reflection (x-axis)

`[1   0]
[0  -1]`

### Reflection (y-axis)

`[-1  0]
[0   1]`

### Reflection (y = x)

`[0  1]   (swap x and y)
[1  0]`

### Reflection (y = -x)

`[0  -1]
[-1  0]`

**General reflection across line at angle θ to x-axis:**

`[cos 2θ   sin 2θ]
[sin 2θ  -cos 2θ]`

## Orthogonal Matrices

`P is orthogonal  ⟺  P^T P = I
                 ⟺  P^(-1) = P^T

Properties: Preserves length and angles
            det(P) = ±1
            All rotation and reflection matrices are orthogonal`