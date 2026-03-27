## Math 232 — Computing Assignment 3 (CA3): Concepts to Study

This is a “two main ideas” assignment:
1) **Change of basis / coordinate vectors / matrix representations of linear maps** (Problem 1)  
2) **Power Method for dominant eigenpairs** (Problem 2)

---

## Notation & Big Picture

- A **basis** \(\mathfrak{B}=\{v_1,\dots,v_4\}\) for \(\mathbb{R}^4\) lets you write any vector \(x\) as
  \[
  x=c_1v_1+\cdots+c_4v_4.
  \]
  The coordinate vector is \([x]_{\mathfrak{B}}=\begin{bmatrix}c_1\\c_2\\c_3\\c_4\end{bmatrix}\).
- The **standard basis** \(S=\{e_1,e_2,e_3,e_4\}\) corresponds to the usual “entries of the vector”.
  So \([x]_S\) is just the usual vector \(x\) written as a column.

---

## Problem 1: Change of Basis + Linear Transformations

### 1a) Change-of-coordinates matrices

Key objects:

- \(P_{S\leftarrow \mathfrak{B}}\): converts **\(\mathfrak{B}\)-coordinates → standard coordinates**.
  - Construction: put the basis vectors as columns (in standard coordinates):
    \[
    P_{S\leftarrow \mathfrak{B}}=\big[\,v_1\ v_2\ v_3\ v_4\,\big].
    \]
  - Meaning:
    \[
    [x]_S = P_{S\leftarrow \mathfrak{B}}[x]_{\mathfrak{B}}.
    \]

- \(P_{\mathfrak{B}\leftarrow S}\): converts **standard coordinates → \(\mathfrak{B}\)-coordinates**.
  - Relationship:
    \[
    P_{\mathfrak{B}\leftarrow S} = \left(P_{S\leftarrow \mathfrak{B}}\right)^{-1}.
    \]
  - Meaning:
    \[
    [x]_{\mathfrak{B}} = P_{\mathfrak{B}\leftarrow S}[x]_S.
    \]

Common pitfall: mixing up the arrow direction.  
Memory trick: the arrow “points to” the coordinate system you end up in.

### 1b) Coordinate vector in \(\mathfrak{B}\)

You are given \(x\) in standard coordinates, and you want \([x]_{\mathfrak{B}}\):
\[
[x]_{\mathfrak{B}} = P_{\mathfrak{B}\leftarrow S}\,x.
\]

Interpretation: you’re solving for the coefficients \(c_1,\dots,c_4\) in \(x=\sum c_iv_i\).

### 1c) Matrix of a linear map in a nonstandard basis

You are given \(L:\mathbb{R}^4\to\mathbb{R}^4\) by a formula:
\[
L(x_1,x_2,x_3,x_4)=(x_2+5x_4,\ x_1-x_3,\ x_1+x_2+x_3+x_4,\ 0).
\]

Step 1: Build the standard matrix \([L]_S\).  
Because the output components are linear combinations of \(x_1,\dots,x_4\), you can read off rows:

- First component \(x_2+5x_4\) → row \([0,1,0,5]\)
- Second component \(x_1-x_3\) → row \([1,0,-1,0]\)
- Third component \(x_1+x_2+x_3+x_4\) → row \([1,1,1,1]\)
- Fourth component \(0\) → row \([0,0,0,0]\)

Step 2: Convert to the \(\mathfrak{B}\) basis:
\[
[L]_{\mathfrak{B}} = P_{\mathfrak{B}\leftarrow S}\,[L]_S\,P_{S\leftarrow \mathfrak{B}}
= P_{\mathfrak{B}\leftarrow S}\,[L]_S\,(P_{\mathfrak{B}\leftarrow S})^{-1}.
\]

Concept to know: this is a **similarity transform**; it’s how the *same* linear map looks under a different coordinate system.

### 1d) Apply \(L\) in \(\mathfrak{B}\)-coordinates

Once you have \([L]_{\mathfrak{B}}\) and \([x]_{\mathfrak{B}}\):
\[
[L(x)]_{\mathfrak{B}} = [L]_{\mathfrak{B}}\,[x]_{\mathfrak{B}}.
\]

---

## Problem 2: Power Method (Dominant Eigenvalue/Eigenvector)

### What the algorithm is doing

Given a matrix \(A\), the Power Method iterates:
\[
y_{k+1}=Ax_k,\qquad x_{k+1}=\frac{y_{k+1}}{\|y_{k+1}\|}.
\]

If \(A\) has a unique **dominant eigenvalue** \(\lambda_1\) (largest magnitude) and your start vector \(x_0\) has some component in the dominant eigenvector direction, then:
- \(x_k\) tends to the **dominant eigenvector direction**
- a scalar estimate tends to the **dominant eigenvalue**

### Eigenvalue approximation used in the notebook

The notebook uses the **Rayleigh quotient** for a unit vector \(x_k\):
\[
\lambda^{(k)} = x_k^T A x_k.
\]

Why it makes sense to study: if \(x_k\) is close to an eigenvector \(v\), then \(x_k^TAx_k\) is close to its eigenvalue.

### Convergence criterion in CA3

The assignment defines convergence as:
- the last two vectors agree to **4 decimal places in each component**.

Then you:
- record the converged eigenvector as `x_d` (truncate to 4 decimals, **do not round**)
- record the eigenvalue as `lambda_d` (truncate to 2 decimals)

Truncation vs rounding:
- truncating to 4 decimals means keep digits through the 4th decimal place and drop the rest (no “carry”).

---

## Python / NumPy skills you’ll use repeatedly

- Matrix-vector multiplication: `A @ x`
- Vector “length”: \(\|x\|=\sqrt{x\cdot x}\) (dot product)
- `np.dot(u, v)` and `u @ v` (for 1D arrays) are common
- Slicing/indexing:
  - `A[i, j]` uses **0-based** indexing
  - `A[:, j]` is column `j`, `A[i, :]` is row `i`
- Shape checking:
  - vectors often have shape `(4,)` (1D arrays) in this notebook

---

## Quick self-check questions (good study targets)

- Can you explain the difference between \(P_{S\leftarrow \mathfrak{B}}\) and \(P_{\mathfrak{B}\leftarrow S}\)?
- Can you derive \([L]_S\) from the formula for \(L(x_1,x_2,x_3,x_4)\)?
- Why does \([L]_{\mathfrak{B}} = P_{\mathfrak{B}\leftarrow S}[L]_SP_{S\leftarrow \mathfrak{B}}\) make sense conceptually?
- What conditions make the Power Method converge?
- Why normalize at every step?
- What is the Rayleigh quotient and why is it a good eigenvalue estimate?

