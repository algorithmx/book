COORDINATE SYSTEMS

Geometric models are usually constructed in Cartesian coordinate systems. In certain cases it is convenient to prefer curvilinear coordinate systems, such as cylindrical or spherical. Curvilinear coordinate systems are used to set up numerical experiments in continuum mechanics. We consider coordinate transformations and position changes of vectors and points underlying objects of geometric model in Cartesian coordinate systems, as well as description of vectors and points in curvilinear coordinate systems.

A.1. Affine Coordinates

A point in space is described by coordinates in some coordinate system. In an affine coordinate system, a point can be described by a radius vector.

A radius vector defines the translation transformation that translates the origin of a coordinate system to a given point in space. Unlike a vector, the radius vector is associated with the origin. This difference affects the formulas in the transition from one coordinate system to another, and the formulas for the change of position in space. Let us consider the differences between the transformation of coordinates of a point and transformations of vector components in the transition from one affine coordinate system to another.

Suppose we have chosen a point in three-dimensional Euclidean space and three non-collinear vectors. Let us construct an affine coordinate system on the chosen point and vectors, which we call the global system. Suppose that a local affine coordinate system with fixed basis vectors is built in the chosen global coordinate system:

$$ \mathbf{i}_1 = \begin{bmatrix} i_{11} \\ i_{12} \\ i_{13} \end{bmatrix}, \quad \mathbf{i}_2 = \begin{bmatrix} i_{21} \\ i_{22} \\ i_{23} \end{bmatrix}, \quad \mathbf{i}_3 = \begin{bmatrix} i_{31} \\ i_{32} \\ i_{33} \end{bmatrix}, $$

with its origin at the origin of the global system. Vectors $\mathbf{i}_1, \mathbf{i}_2,$ and $\mathbf{i}_3$ are linearly independent. Let us assume that vectors $\mathbf{i}_1, \mathbf{i}_2,$ and $\mathbf{i}_3$ may not be orthogonal to each other, and are of arbitrary length. Let the position of some point $q$ in the global system be described by coordinates $q_1, q_2,$ and $q_3,$ and the position of this point in the local system be described by coordinates $y_1, y_2,$ and $y_3.$ Then the equality

$$ q = y_1 \mathbf{i}_1 + y_2 \mathbf{i}_2 + y_3 \mathbf{i}_3 $$
implies that the relation between the global $q_1, q_2, q_3$ and local $y_1, y_2, y_3$ coordinates of the considered point is:

$$\begin{bmatrix} q_1 \\ q_2 \\ q_3 \end{bmatrix} = \begin{bmatrix} i_1 & i_2 & i_3 \end{bmatrix} \cdot \begin{bmatrix} y_1 \\ y_2 \\ y_3 \end{bmatrix} = A \cdot \begin{bmatrix} y_1 \\ y_2 \\ y_3 \end{bmatrix},$$

(A.1.1)

where the columns of transformation matrix $A$ are composed of the components of the basis vectors $i_1, i_2,$ and $i_3$ of the local coordinate system

$$A = \begin{bmatrix} i_1 & i_2 & i_3 \end{bmatrix} = \begin{bmatrix} i_{11} & i_{21} & i_{31} \\ i_{12} & i_{22} & i_{32} \\ i_{13} & i_{23} & i_{33} \end{bmatrix}.$$

The inverse transformation is given by

$$\begin{bmatrix} y_1 \\ y_2 \\ y_3 \end{bmatrix} = A^{-1} \cdot \begin{bmatrix} q_1 \\ q_2 \\ q_3 \end{bmatrix}.$$

(A.1.2)

If the basis of the global coordinate system and the basis $i_1, i_2,$ and $i_3$ are orthonormal, the determinant of matrix $A$ is unity, and the inverse matrix is the transposed matrix:

$$A^{-1} = A^{-T} = \begin{bmatrix} i_{11} & i_{21} & i_{31} \\ i_{12} & i_{22} & i_{32} \\ i_{13} & i_{23} & i_{33} \end{bmatrix}.$$

Let us shift the origin of the local coordinate system to the point $r$. Let the position of some point $p$ in the global system be described by coordinates $p_1, p_2,$ and $p_3$, and the position of the same point in the local system be described by $x_1, x_2,$ and $x_3$ (see Fig. A.1.1).

![Diagram](image-url)  

Fig. A.1.1.
Then from the equality

$$ p = r + x_1 i_1 + x_2 i_2 + x_3 i_3 , $$

we obtain the relation for the global—$p_1, p_2,$ and $p_3$—and local—$x_1, x_2,$ and $x_3$—coordinates of the considered point:

$$
\begin{bmatrix}
p_1 \\
p_2 \\
p_3
\end{bmatrix} = A \cdot \begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix} + \begin{bmatrix}
r_1 \\
r_2 \\
r_3
\end{bmatrix}.
$$

(A.1.3)

The inverse transformation is given by

$$
\begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix} = A^{-1} \cdot \begin{bmatrix}
p_1 \\
p_2 \\
p_3
\end{bmatrix} - A^{-1} \cdot \begin{bmatrix}
r_1 \\
r_2 \\
r_3
\end{bmatrix}.
$$

(A.1.4)

If the basis of the global coordinate system and the basis $i_1, i_2, i_3$ are both orthonormal, the inverse matrix is the transposed matrix, and the transformation (A.1.4) takes the form

$$
\begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix} = \begin{bmatrix}
i_{11} & i_{12} & i_{13} \\
i_{21} & i_{22} & i_{23} \\
i_{31} & i_{32} & i_{33}
\end{bmatrix} \cdot \begin{bmatrix}
p_1 \\
p_2 \\
p_3
\end{bmatrix} + \begin{bmatrix}
o_1 \\
o_2 \\
o_3
\end{bmatrix},
$$

where the components $o_1, o_2,$ and $o_3,$ and $r_1, r_2,$ and $r_3,$ are related by:

$$
\begin{bmatrix}
o_1 \\
o_2 \\
o_3
\end{bmatrix} = -\begin{bmatrix}
i_{11} & i_{12} & i_{13} \\
i_{21} & i_{22} & i_{23} \\
i_{31} & i_{32} & i_{33}
\end{bmatrix} \cdot \begin{bmatrix}
r_1 \\
r_2 \\
r_3
\end{bmatrix}.
$$

A vector in an affine coordinate system determines the displacement from one point in the space to another point, and is thus not associated with the origin. The vector's components, $y_1, y_2,$ and $y_3,$ in the local coordinate system, and $q_1, q_2,$ and $q_3$ in the global coordinate system, are related by (A.1.1) and (A.1.2). The radius vector defines the translation of the origin of the coordinate system to the given point in the space; therefore, the coordinates of the origin of the local system are present in the formulas of coordinate transformation of the radius vector. Coordinates of a point—$x_1, x_2, x_3$ in the local coordinate system and $p_1, p_2, p_3$ in the global coordinate system—are related by (A.1.3) and (A.1.4).
A.2. Modification of Vectors and Points

The simplest modification of a point is displacement in the space by the displacement vector $\mathbf{w}$. We describe the position of the point before the modification by the radius vector $\mathbf{r}_0$, and the position of the point after the modification by the radius vector $\mathbf{r}$. The point's position after the displacement by the vector $\mathbf{w}$ is described by the radius vector equal to the sum of the radius vector of its initial position $\mathbf{r}_0$ and the displacement vector $\mathbf{w}$:

$$
\mathbf{r} = \mathbf{r}_0 + \mathbf{w}.
$$

The coordinates of radius vector $\mathbf{r}$ are equal to the sum of the corresponding coordinates of radius vector $\mathbf{r}_0$ and components of vector $\mathbf{w}$.

Unlike a point, a vector does not change when displaced in space, since the vector defines the relative position of two points that is not changed when they are displaced simultaneously.

Consider rotation of a point about an axis. Let the initial position of the considered point be described by the radius vector $\mathbf{r}_0$, and the rotation axis be determined by the point $\mathbf{q}$ and the unit vector $\mathbf{v}$. Now let us rotate the considered point counterclockwise around the axis by the angle $\alpha$ if viewed toward the vector $\mathbf{v}$ (see Fig. A.2.1).

![Diagram](image)

Fig. A.2.1.

Let us construct the vector $\mathbf{p} = \mathbf{r}_0 - \mathbf{q}$. Expand the vector $\mathbf{p}$ into two components,

$$
\mathbf{p} = \mathbf{t} + \mathbf{n},
$$

(A.2.2)

where the vector $\mathbf{t} = (\mathbf{p} \cdot \mathbf{v}) \mathbf{v}$ is parallel to vector $\mathbf{v}$, and the vector $\mathbf{n} = \mathbf{p} - (\mathbf{p} \cdot \mathbf{v}) \mathbf{v}$ is orthogonal to vector $\mathbf{v}$. Vector $\mathbf{t}$ does not change as a result of the rotation, and vector $\mathbf{n}$ is rotated by the angle $\alpha$ toward the vector

$$
\mathbf{b} = \mathbf{v} \times \mathbf{n} = \mathbf{v} \times (\mathbf{p} - (\mathbf{p} \cdot \mathbf{v}) \mathbf{v}) = \mathbf{v} \times \mathbf{p}.
$$

(A.2.3)
Since vector $\mathbf{v}$ has unit length, vector $\mathbf{b}$ has a length equal to the length of vector $\mathbf{n}$. Moreover, it is orthogonal to vectors $\mathbf{v}$ and $\mathbf{n}$. After rotation by angle $\alpha$, vector $\mathbf{n}$ becomes equal to the vector $\mathbf{n} \cos \alpha + \mathbf{b} \sin \alpha$. Hence, after the rotation, the considered point is determined by the radius vector

$$
\mathbf{r} = \mathbf{q} + \mathbf{t} + \mathbf{n} \cos \alpha + \mathbf{b} \sin \alpha =
\mathbf{q} + (\mathbf{p} \cdot \mathbf{v}) \mathbf{v} + (\mathbf{p} - (\mathbf{p} \cdot \mathbf{v}) \mathbf{v}) \cos \alpha + \mathbf{v} \times \mathbf{p} \sin \alpha.
$$
(A.2.4)

Taking into account the equality $(\mathbf{p} \cdot \mathbf{v}) \mathbf{v} = (\mathbf{v} \cdot \mathbf{v}) \mathbf{p}$, expression (A.2.4) takes the form

$$
\mathbf{r} = \mathbf{q} + (\mathbf{v} \cdot \mathbf{v}) \cdot \mathbf{p} + \cos \alpha (\mathbf{E} - \mathbf{v} \cdot \mathbf{v}) \cdot \mathbf{p} + \sin \alpha \mathbf{v} \times \mathbf{p} = \mathbf{q} + \mathbf{A} \cdot (\mathbf{r}_0 - \mathbf{q}). $$
(A.2.5)

Rotation matrix $\mathbf{A}$ is defined by

$$
\mathbf{A} = (1 - \cos \alpha) \mathbf{v} \mathbf{v} + \cos \alpha \mathbf{E} + \sin \alpha \mathbf{v} \times,
$$

where \( \mathbf{v} \mathbf{v} = \begin{bmatrix} v_1 v_1 & v_1 v_2 & v_1 v_3 \\ v_2 v_1 & v_2 v_2 & v_2 v_3 \\ v_3 v_1 & v_3 v_2 & v_3 v_3 \end{bmatrix}, \quad \mathbf{E} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}, \quad \mathbf{v} \times = \begin{bmatrix} 0 & -v_3 & v_2 \\ v_3 & 0 & -v_1 \\ -v_2 & v_1 & 0 \end{bmatrix}, \text{ and } v_1, v_2, v_3 \text{ are components of unit vector } \mathbf{v}.
$$

Matrix $\mathbf{A}$ is orthogonal. When transposing it, only the sign of its last term is changed; this corresponds to rotation of the point by the angle $\alpha$.

The formula for rotation of a free vector in the space is obtained from formula (A.2.5), assuming that $\mathbf{q} = 0$.

Let us determine the coordinates of the point $\mathbf{r}$, symmetric to point $\mathbf{r}_0$ relative to the plane. Let the plane of symmetry be defined by point $\mathbf{q}$ and by unit vector $\mathbf{n}$ (see Fig A.2.2).

Construct the vector $\mathbf{p} = \mathbf{r}_0 - \mathbf{q}$ and represent it as a sum of two vectors—the projection on the unit vector $\mathbf{n}$ and the component $\mathbf{u}$ perpendicular to the unit vector $\mathbf{n}$:

$$
\mathbf{p} = (\mathbf{p} \cdot \mathbf{n}) \mathbf{n} + \mathbf{u},
$$
where $u = p - (p \cdot n)n$. After mirroring the vector $p$, its normal to the plane component changes its sign. The position of the symmetrical point is described by the radius vector

$$
r = q - (p \cdot n)n + (p - (p \cdot n)n) = q + (E - 2nn^T)p = q + A(r_0 - q),
$$

(A.2.6)

where $A = \begin{bmatrix} 1 - 2n_1n_1 & -2n_1n_2 & -2n_1n_3 \\ -2n_2n_1 & 1 - 2n_2n_2 & -2n_2n_3 \\ -2n_3n_1 & -2n_3n_2 & 1 - 2n_3n_3 \end{bmatrix}$ is the symmetry matrix, and $n_1, n_2, n_3$ are the components of unit vector $n$.

The formula for the symmetry transformations of a free vector in the space is obtained from formula (A.2.6), assuming that $q = 0$.

Let us now consider scaling the radius vector of a point. Suppose we are given three mutually orthogonal vectors $i_1, i_2,$ and $i_3$, and it is required to increase the size of the scaled object by $m_1$ times in the direction of vector $i_1$, by $m_2$ times in the direction of vector $i_2$, and by $m_3$ times in the direction of vector $i_3$. Consider the change of position of point $r_0$ of the scaled object for which the point $q$ does change its position. The position of the considered point after scaling is described by the radius vector

$$
r = q + A(r_0 - q),
$$

(A.2.7)

where $A = \begin{bmatrix} m_1i_1 & m_2i_2 & m_3i_3 \\ m_1i_2 & m_2i_2 & m_3i_3 \\ m_1i_3 & m_2i_3 & m_3i_3 \end{bmatrix}$ is the scaling matrix.

The formula for scaling of a free vector in space is obtained from formula (A.2.7), assuming that $q = 0$.

### A.3. Homogeneous Coordinates

Formulas for converting the coordinates of the radius vector of a point under its rotation around an axis (A.2.5) of symmetry relative to a plane (A.2.6), and scaling (A.2.7), have a similar form

$$
r = q + A(r_0 - q) = A \cdot r_0 + (q - A \cdot q) = A \cdot r_0 + w,
$$

where $w$ is a displacement vector. The displacement of point $r_0$ is formally described as $r = A \cdot r_0 + w$, with unit matrix $A$. Coordinate transformation formula (A.1.3) has a similar form. All of these transformations can be written in a common form as $P = A \cdot X$, using homogeneous coordinates and extended matrices.

Homogeneous coordinates and extended matrices are based on regular coordinates and matrices. To obtain homogeneous coordinates, a fourth coordinate equal to one is added to the three coordinates of the point, and a fourth component equal to zero is added to the three components of the vector. To obtain the extended
matrix, the dimension of the regular matrix is increased by unity. In terms of homogeneous coordinates, equality (A.1.3) has the form

$$
\begin{bmatrix}
p_1 \\
p_2 \\
p_3 \\
1
\end{bmatrix} =
\begin{bmatrix}
i_{11} & i_{12} & i_{13} & r_1 \\
i_{21} & i_{22} & i_{23} & r_2 \\
i_{31} & i_{32} & i_{33} & r_3 \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2 \\
x_3 \\
1
\end{bmatrix}.
$$

The inverse transformation (A.1.4) has the form

$$
\begin{bmatrix}
x_1 \\
x_2 \\
x_3 \\
1
\end{bmatrix} =
\begin{bmatrix}
a_{11} & a_{12} & a_{13} & o_1 \\
a_{21} & a_{22} & a_{23} & o_2 \\
a_{31} & a_{32} & a_{33} & o_3 \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
p_1 \\
p_2 \\
p_3 \\
1
\end{bmatrix},
$$

where $$
\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{bmatrix} = A^{-1}, \quad
\begin{bmatrix}
o_1 \\
o_2 \\
o_3
\end{bmatrix} = -A^{-1} \cdot
\begin{bmatrix}
r_1 \\
r_2 \\
r_3
\end{bmatrix}.
$$

If the basis $i_1, i_2, i_3$ is orthonormal, the inverse transformation (A.1.4) has the form

$$
\begin{bmatrix}
x_1 \\
x_2 \\
x_3 \\
1
\end{bmatrix} =
\begin{bmatrix}
i_{11} & i_{12} & i_{13} & o_1 \\
i_{21} & i_{22} & i_{23} & o_2 \\
i_{31} & i_{32} & i_{33} & o_3 \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
p_1 \\
p_2 \\
p_3 \\
1
\end{bmatrix}.
$$

To construct rational curves and surfaces, an additional parameter is required—the so-called weight of the point—along with the coordinates of the points. Here is an example calculating the radius vector of a point of a rational curve:

$$
p(t) = \frac{\sum_{j=0}^{n} f_j(t) w_j p_j}{\sum_{j=0}^{n} f_j(t) w_j} = \frac{wp}{w},
$$

where $w_i$ is the weight of the control point $p_i$, and $f_i(t)$ is some function of the parameter of curve $t$ calculated for every control point $p_i$. In the above example the same manipulations are performed with the weight of the point, and with the coordinates multiplied by the weights. Therefore, homogeneous coordinates are also used to work with rational curves and surfaces, in which the weight acts as an
additional coordinate. When a point has weight $w$, the expression of its radius vector in homogeneous coordinates has the form

$$\mathbf{P} = \begin{bmatrix} wp_1 \\ wp_2 \\ wp_3 \\ w \end{bmatrix}.$$

When using homogeneous coordinates, computations are performed for the homogeneous component without isolation of the spatial coordinates. The spatial coordinates of the point are calculated in the final stage of the calculation, dividing the first three components by the weight $w$.

### A.4. Curvilinear Coordinates

Generally, basis vectors of systems in the curvilinear coordinate system have different lengths and directions at various points of the space. This complicates the description of geometric objects. But curvilinear coordinates are sometimes convenient.

Suppose we choose a point and three non-collinear vectors in three-dimensional space. Let us construct an affine coordinate system in the space on the chosen point and vectors. The coordinates of the points in this system are denoted by $x^1$, $x^2$, and $x^3$. The coordinates' indices are denoted as superscripts, which allows simplifying the cumbersome summation of similar terms by introducing agreement on summation over repeated indices. Suppose that there exist continuous and differentiable single-valued functions

$$u^1 = u^1(x^1, x^2, x^3),$$
$$u^2 = u^2(x^1, x^2, x^3),$$
$$u^3 = u^3(x^1, x^2, x^3),$$

such that their reverse functions

$$x^1 = x^1(u^1, u^2, u^3),$$
$$x^2 = x^2(u^1, u^2, u^3),$$
$$x^3 = x^3(u^1, u^2, u^3),$$
(A.4.1)

are also continuously differentiable and single-valued functions.

If one of the parameters in (A.4.1) is fixed—for example, $u^i=\text{const}$—then we obtain some surface in space, which we call the surface of the $i$-th coordinate. Function (A.4.1) must be such that the surfaces of each $i$-th coordinate do not intersect with each other. In this case, parameters $u^1$, $u^2$, and $u^3$ can serve as the coordinates of points in this space. To describe a point in the space with coordinates $u^1$, $u^2$, and $u^3$ we use the notation
similar to the notation of points in an affine coordinate system. Let us require that the determinant of the Jacobian matrix of the system (A.4.1) is non-zero:

$$\begin{vmatrix}
\frac{\partial x^1}{\partial u^1} & \frac{\partial x^1}{\partial u^2} & \frac{\partial x^1}{\partial u^3} \\
\frac{\partial x^2}{\partial u^1} & \frac{\partial x^2}{\partial u^2} & \frac{\partial x^2}{\partial u^3} \\
\frac{\partial x^3}{\partial u^1} & \frac{\partial x^3}{\partial u^2} & \frac{\partial x^3}{\partial u^3}
\end{vmatrix} \neq 0.$$
(A.4.2)

We describe a curve in a curvilinear coordinate system by a set of functions $u^1 = u^1(t)$, $u^2 = u^2(t)$, and $u^3 = u^3(t)$, of a common parameter $t$, in the form of the vector function.

$$r(t) = \begin{bmatrix} u^1(t) \\ u^2(t) \\ u^3(t) \end{bmatrix}. \hspace{1cm} (A.4.3)$$

The term coordinate lines designates curves in which only one of the coordinates changes and other coordinates do not. The curve $r(u^k)$, in which only the $k$-th coordinate is changed ($t = u^k$), and the remaining coordinates are constants, is referred to as the $k$-th coordinate line. In general, coordinate lines are not straight lines; this is why the coordinate system obtained by the process described above is called a curvilinear coordinate system.

Each point in the space with coordinates $u^1$, $u^2$, $u^3$ can be the origin for a local coordinate system with basic functions $r_1$, $r_2$, $r_3$, which are derivatives of the coordinate lines at the considered point:

$$r_1 = \frac{dr(u^1)}{du^1}, \quad r_2 = \frac{dr(u^2)}{du^2}, \quad r_3 = \frac{dr(u^3)}{du^3}. \hspace{1cm} (A.4.4)$$

By virtue of (A.4.2), vectors $r_1$, $r_2$, and $r_3$ are not coplanar, and can be used as the basis to expand any other vector at a given point of the space. The set of vectors $r_1$, $r_2$, and $r_3$ is called a tangent basis. In general, basis vectors $r_1$, $r_2$, and $r_3$ are different at each point, so they can be used to expand just those vectors that are computed at the same point in the space. Basis vector $r_k$ is directed along the tangent to the $k$-th coordinate line at this point; its length is generally different from unity.
The square of the length of an infinitesimal interval given by infinitesimal increments of the coordinates $du^1$, $du^2$, and $du^3$ is equal to

$$ds^2 = \sum_{i=1}^{3} \sum_{j=1}^{3} r_i \cdot r_j \, du^i \, du^j.$$

The coefficients

$$g_{ij} = g_{ij}(u^1, u^2, u^3) = r_i \cdot r_j, \quad i, j = 1, 2, 3$$

(A.4.5)

are called covariant components of the metric tensor at the point in space with coordinates $u^1$, $u^2$, and $u^3$. The matrix composed of the covariant components of the metric tensor is denoted by $G$.

Agreement on summation over repeated indices gives a compact form to many formulas. For this, the superscript index is assigned to the coordinates, and the subscript indices are assigned to the vectors of the tangent basis, and to the covariant components.

Agreement on summation over repeated indices reads: Summation in expressions is performed over indices that are repeated once as subscript and once as superscript indices, while the indices span the range from one to the dimension of the space. Agreement allows dropping the summation signs and giving compact forms to expressions, such as,

$$a_i b_k^i \equiv \sum_{i=1}^{3} a_i b_k^i, \quad a_i b^{ijk} c_k \equiv \sum_{i=1}^{3} \sum_{k=1}^{3} a_i b^{ijk} c_k.$$

Applying agreement on summation over repeated indices, the expression for the square of the length of an infinitesimal interval takes the form

$$ds^2 = r_i \cdot r_j \, du^i \, du^j = g_{ij} \, du^i \, du^j.$$

Indices on which the summation is performed are called dummy indices, and other indices are called free indices. The dummy indices are absent on one of the sides of the equation. The free indices take the value of the numbers of one of the dimensions of the space. To avoid confusion among the indices when there is a large number of them, remember three rules:

1. Free indices on both sides of the equal sign hold the same position.
2. Dummy indices over which summation is performed are met once as subscript and once as superscript, and only on one side of the equation.
3. An index of a parameter with respect to which differentiation is performed is a subscript index.

When translating to a new curvilinear coordinate system $u'^1$, $u'^2$, and $u'^3$, the covariant components of the metric tensor $g_{kn}$ in the new coordinate system are related to components $g_{ij}$ by

$$g_{kn}' = A_{k}^{i} \cdot A_{n}^{j} \cdot g_{ij}.$$
where $A^i_k = \frac{\partial u^i}{\partial u^k}$. The basis vectors of curvilinear systems are related by analogous relations

$$
r_k = A^i_k \cdot r_i.
$$

(A.4.6)

For a tangent basis $r_1, r_2,$ and $r_3$, a reciprocal basis $r^1, r^2,$ and $r^3$ can be constructed at each point by the rule

$$
r_i \cdot r^k = \delta^k_i,
$$

(A.4.7)

where $\delta^k_i$ are Kronecker symbols, taking values $\delta^k_i = 1$ at $i = k$ and $\delta^k_i = 0$ at $i \neq k$. To find the vectors of the reciprocal basis, we represent them in the form of expansion in a tangent basis with unknown coefficients. From the above conditions, we get a system of linear algebraic equations for the unknown coefficients. After solving it we obtain the coefficients of the reciprocal basis vectors expansion in the vectors of the tangent basis

$$
r^k = g^{ki} r_i,
$$

(A.4.8)

where $g^{ki}$ — coefficients of matrix $G^{-1}$. The coefficients $g^{ki} = r^k \cdot r^i$ are called contravariant components of the metric tensor, given in the coordinate system $u^1, u^2, u^3$. When translating to another curvilinear coordinate system $u'^1, u'^2, u'^3$, the contravariant components of metric tensor $g'^{ij}$ in the new coordinate system are related to components $g^{ij}$ by

$$
g'^{ij} = A^n_k A^l_i g^{kl},
$$

where $A^j_i = \frac{\partial u^j}{\partial u^i}$. The vectors of the reciprocal basis of curvilinear coordinate systems are related by analogous relations

$$
r^i = A^i_k r^k.
$$

(A.4.9)

Since $G^{-1}$ is the inverse matrix of the matrix $G$, their product is the identity matrix, which implies that the mixed components of the metric tensor are equal to $\delta^k_i$

$$
g_{ik} g^{jk} = g^{jk} = \delta^k_i.
$$

The vectors of the reciprocal basis and of the tangent basis are related by

$$
r^1 = \frac{r_2 \times r_3}{\sqrt{g}}, \quad r^2 = \frac{r_3 \times r_1}{\sqrt{g}}, \quad r^3 = \frac{r_1 \times r_2}{\sqrt{g}},
$$

$$
r_1 = r^2 \times r^3 \sqrt{g}, \quad r_2 = r^3 \times r^1 \sqrt{g}, \quad r_3 = r^1 \times r^2 \sqrt{g},
$$

(A.4.10)
where $g$ is the determinant of matrix $G$. The latter relations can be written as

$$
r^k = e^{ijk} \frac{r_i \times r_j}{\sqrt{g}}, \quad r_k = e_{ijk} r^i \times r^j \sqrt{g},
$$

or as

$$
r_i \times r_j = e_{ijk} r^k \sqrt{g}, \quad r^i \times r^j = e^{ijk} \frac{r_k}{\sqrt{g}},
$$

where we use Levi-Civita symbols $e^{ijk}$ and $e_{ijk}$. The values $e^{ijk}$ and $e_{ijk}$ are equal to 0 if among the indices there are found two that are the same; equal to 1 for a sequence of indices 1, 2, 3 and for sequences 2,3,1 and 3,1,2 (obtained from 1,2,3 by circular permutation); and equal to -1 when this order is violated (i.e., for the sequences 3,2,1, 2,1,3, and 1,3,2).

An arbitrary vector $a$ in curvilinear coordinates can be expanded in the tangent basis or the reciprocal basis, and can be represented as

$$
a = a^i r_i = a_i x^i.
$$

The result of the scalar product of vectors $a$ and $b$ is a number that, depending on the vector representation, is equal to

$$
a \cdot b = a^i b^j g_{ij} = a_i b_j g^{ij} = a^i b_i = a_i b^i. \tag{A.4.11}
$$

The vector product of vectors $a$ and $b$ can be represented as

$$
a \times b = a^i b^j e_{ijk} \sqrt{g} r^k = a_i b_j e^{ijk} \frac{r_k}{\sqrt{g}}, \tag{A.4.12}
$$

where the following equalities are used:

$$
e^{ijk} \frac{1}{\sqrt{g}} = (r^i \times r^j) \cdot r^k, \quad e_{ijk} \sqrt{g} = (r_i \times r_j) \cdot r_k.
$$

The terms

$$
\varepsilon^{ijk} = e^{ijk} \frac{1}{\sqrt{g}} = (r^i \times r^j) \cdot r^k, \quad \varepsilon_{ijk} = e_{ijk} \sqrt{g} = (r_i \times r_j) \cdot r_k
$$

are contravariant and covariant components of the Levi-Civita tensor, respectively.

### A.5. Differentiation in Curvilinear Coordinates

In an affine coordinate system, basis vectors have equal values and direction at every point in the space; so when differentiating, they act as constants. In a curvilinear coordinate system, basis vectors are different at every point in the space, so when
differentiating, one should take into account the change of basis vectors when moving from one point to another.

Let us find the change in vectors of the tangent basis when moving from a point in space with coordinates $u^1, u^2,$ and $u^3$, to an infinitely close point with coordinates $u^1 + \delta u^1, u^2 + \delta u^2,$ and $u^3 + \delta u^3$. Up to linear terms relative to $\delta u^i, i=1,2,3$, the change of basis vectors can be represented as

$$
\delta r_i = \frac{\partial r_i}{\partial u^j} \delta u^j = r_j \delta u^j = \Gamma_{ij}^k r_k \delta u^j,
$$

where $\Gamma_{ij}^k$ are as-yet unknown coefficients of derivatives $r_j$ of the tangent basis expansion in the basis $r_1, r_2, r_3$. In all the expressions, we invoke agreement on summation over repeated indices. The scalar product of the equality

$$
r_j = \Gamma_{ij}^k r_k
$$

by $r_1, r_2,$ and $r_3$ yields the system of equations for $\Gamma_{ij}^k$

$$
\begin{align*}
\Gamma_{ij}^1 g_{11} + \Gamma_{ij}^2 g_{12} + \Gamma_{ij}^3 g_{13} &= \Gamma_{ij}^1 = r_j \cdot r_1, \\
\Gamma_{ij}^1 g_{21} + \Gamma_{ij}^2 g_{22} + \Gamma_{ij}^3 g_{23} &= \Gamma_{ij}^2 = r_j \cdot r_2, \\
\Gamma_{ij}^1 g_{31} + \Gamma_{ij}^2 g_{32} + \Gamma_{ij}^3 g_{33} &= \Gamma_{ij}^3 = r_j \cdot r_3.
\end{align*}
$$

We now introduce the notation $\Gamma_{ijk} = r_j \cdot r_k$. Coefficients $\Gamma_{ijk}$ can be expressed in terms of derivatives of the covariant components of the metric tensor. For this let us write out the known equalities

$$
r_j \cdot r_k = g_{jk}, \quad r_k \cdot r_i = g_{ki}, \quad r_i \cdot r_j = g_{ij},
$$

in which indices $i, j,$ and $k$ are cyclically permuted, spanning the values from one to the dimension of the space. Let us differentiate the first equality with respect to $u^i$, the second, with respect to $u^j$, and the third with respect to $u^k$. We obtain:

$$
\begin{align*}
r_{ji} \cdot r_k + r_j \cdot r_{ki} &= \frac{\partial g_{jk}}{\partial u^i}, \\
r_{kj} \cdot r_i + r_k \cdot r_{ij} &= \frac{\partial g_{ki}}{\partial u^j}, \\
r_{ik} \cdot r_j + r_i \cdot r_{jk} &= \frac{\partial g_{ij}}{\partial u^k}.
\end{align*}
$$

If we add the first two equations and subtract the third one from them, we obtain a formula for the coefficients $\Gamma_{ijk}$

$$
\Gamma_{ijk} = \frac{1}{2} \left( \frac{\partial g_{kj}}{\partial u^i} + \frac{\partial g_{ik}}{\partial u^j} - \frac{\partial g_{ij}}{\partial u^k} \right).
$$
We now solve system of equations (A.5.3) for $\Gamma_{ij}^k$ to obtain the equality

$$\Gamma_{ij}^n = g^{nk}\Gamma_{ij,k}. \quad (A.5.5)$$

Rewrite system (A.5.3) in the form

$$\Gamma_{ij,n} = g_{nk}\Gamma_{ij}^k.$$

We substitute equality (A.5.4) in (A.5.5), and obtain the final expression for the coefficients in expansion (A.5.1):

$$\Gamma_{ij}^n = \frac{1}{2}g^{nk}\left(\frac{\partial g_{kj}}{\partial u^i} + \frac{\partial g_{ik}}{\partial u^j} - \frac{\partial g_{ij}}{\partial u^k}\right).$$

Coefficients $\Gamma_{ij,k}$ are called Christoffel symbols of the first kind, and the coefficients $\Gamma_{ij}^k$ are called Christoffel symbols of the second kind. They are expressed in terms of the components of the metric tensor and their derivatives with respect to the curvilinear coordinates. The Christoffel symbols possess the symmetry $\Gamma_{misk} = \Gamma_{mis}k$, $\Gamma_{m}^k = \Gamma_{mr}^k$. They are not the components of a tensor.

Let us compute the derivative of the vector function in curvilinear coordinates $u^1$, $u^2$, and $u^3$. Let the coordinates of the vector function $a(t)$ be continuous functions $u^1 = u^1(t)$, $u^2 = u^2(t)$, and $u^3 = u^3(t)$ of a common parameter $t$. Let the increment of the coordinates $\delta u^1$, $\delta u^2$, and $\delta u^3$ correspond to the change of the parameter $\delta t$ of the vector function. We require that maximum increment of coordinates $\delta u^i$ tends to zero as $\delta t$ tends to zero. The increment of vector function $a(t)$ in the local basis at the point with coordinates $u^1(t)$, $u^2(t)$, and $u^3(t)$ is

$$\delta a = a(t+\delta t) - a(t) = a'(t+\delta t)(r_i + \delta r_i) - a'(t)r_i = a'(t+\delta t)(r_i + \Gamma_{ij}^k r_k \delta u^j) - a'(t)r_i.$$

Dividing the last equality by $\delta t$ and making $\delta t$ tend to zero, we obtain the formula for the derivative of the vector function

$$\frac{da}{dt} = \frac{da'}{dt} r_i + a' \Gamma_{ij}^k r_k \frac{du^j}{dt} = \frac{da'}{dt} r_i + a^n \Gamma_{nj}^i r_i \frac{du^j}{dt} = \left(\frac{da'}{dt} + a^n \Gamma_{nj}^i \frac{du^j}{dt}\right) r_i. \quad (A.5.6)$$

The expression

$$\frac{Da^i}{dt} = \frac{da^i}{dt} + a^n \Gamma_{nj}^i \frac{du^j}{dt}$$

is called the absolute or covariant derivative of the contravariant components of the vector function in the direction of the curve $u^1(t)$, $u^2(t)$, $u^3(t)$.
The tangent basis and the reciprocal basis are equivalent at some point in the space, and therefore the vector $\mathbf{a}(t)$ of the curve can also be expanded in the reciprocal basis at the point of the curve

$$
\mathbf{a}(t) = a_i r^i,
$$

(A.5.7)

where $a_i$ are covariant components of the vector $\mathbf{a}$. To derive the derivative $\mathbf{a}(t)$ in the given representation, we need to know how to change the vectors of the reciprocal basis when translating from the point with coordinates $u^1(t), u^2(t),$ and $u^3(t)$ to an infinitely close point with coordinates $u^1(t)+\delta u^1, u^2(t)+\delta u^2,$ and $u^3(t)+\delta u^3$.

Differentiating equation (A.4.7), we obtain

$$
r_j \cdot \frac{\partial r^k}{\partial u^j} = -\frac{\partial r_j}{\partial u^j} \cdot r^k = -\Gamma_{ij}^k r^i \cdot r^k = -\Gamma_{ij}^k,
$$

(A.5.8)

which implies that $-\Gamma_{ij}^k$ are coefficients of expansion of the derivatives $\frac{\partial r^k}{\partial u^j}$ in the reciprocal basis

$$
r_j^k = \frac{\partial r^k}{\partial u^j} = -\Gamma_{ij}^k r^i.
$$

(A.5.9)

Indeed, if we compute the inner product of equation (A.5.9) with $r_i$, we obtain the equality (A.5.8). Thus, up to terms linear relative to $\delta u^j$, the change of vectors of the reciprocal basis is

$$
\delta r^k = \frac{\partial r^k}{\partial u^j} \delta u^j = -\Gamma_{ij}^k r^i \delta u^j.
$$

Using representation (A.5.7), we obtain the formula for the derivative of the vector function of the curve

$$
\frac{da}{dt} = \frac{da_i}{dt} r^i - a_i \Gamma_{ij}^k r^j \frac{du^j}{dt} = \frac{da_i}{dt} r^i - a_i \Gamma_{ij}^k r^j \frac{du^j}{dt} = \left( \frac{da_i}{dt} - a_i \Gamma_{ij}^k \frac{du^j}{dt} \right) r^i.
$$

(A.5.10)

The expression

$$
\frac{Da_i}{dt} = \frac{da_i}{dt} - a_i \Gamma_{ij}^k \frac{du^j}{dt}
$$

is called the absolute or covariant derivative of the covariant components of the vector function in the direction of the curve $u^1(t), u^2(t), u^3(t)$.

As can be seen, the derivative of a vector function is also a vector function. Differentiating the representations

$$
\frac{da}{dt} = \frac{Da_i}{dt} r^i, \quad \frac{da}{dt} = \frac{Da^i}{dt} r_i
$$
and using formulas (A.5.6) and (A.5.10), we can obtain higher-order derivatives for the vector function $\mathbf{a}(t)$.

### A.6. Tensors in Curvilinear Coordinates

**Tensors** are objects described by several components. Operations on tensors do not depend on the chosen coordinate system. In different coordinate systems, the same tensor has different components. In the same coordinate system, a tensor can be represented by either its covariant or its contravariant components, or it can be represented by a mixture of components. The covariant components have subscript indices, the contravariant components have superscript indices, and mixed components have both subscript and superscript indices. There is a tensor called the **metric tensor**. The inertia tensor of a solid, the tensor of space curvature, a strain tensor, and the stress tensor of a continuous medium are examples of tensors. Tensors defined for each point of some region of the space form a **tensor field**.

A vector function is a tensor of rank one. Let us imagine that at each point in a space a vector function is given, whose components depend on the point's position in the space; i.e., the components are functions of the point's coordinates, $u^1, u^2,$ and $u^3$. This type of vector function defines a **vector field** in the space.

Let us find the change of the vector field $\mathbf{a}(u^1, u^2, u^3)$ when translating from a point with coordinates $u^1, u^2,$ and $u^3$ to an infinitely close point along one of the coordinate lines. Let this translation correspond to a change in the coordinate $u^i$ of an infinitesimal amount $\delta u^i$. The increment of the vector field represented by the contravariant components $\mathbf{a}(u^1, u^2, u^3) = a^i r_i$ up to the linear with respect to $\delta u^i$ terms is

$$
\delta \mathbf{a} = \frac{\partial a^i}{\partial u^j} \delta u^j r_i + a^i \frac{\partial r_i}{\partial u^j} \delta u^j.
$$

Recall that in these expressions we invoke the agreement on summation over repeated indices. Dividing both sides of this equality by $\delta u^i$, and letting $\delta u^i$ tend to zero, we obtain the formula for the derivative of the vector field represented in terms of the contravariant components

$$
\frac{\partial \mathbf{a}}{\partial u^j} = \frac{\partial a^i}{\partial u^j} r_i + a^i \Gamma^k_{ij} r_k = \left( \frac{\partial a^i}{\partial u^j} + a^n \Gamma^i_{nj} \right) r_i.
$$

The expression

$$
\nabla_j a^i = \frac{\partial a^i}{\partial u^j} + a^n \Gamma^i_{nj}
$$

(A.6.1)
is called the covariant derivative of the contravariant components of the vector field. The symbol $\nabla_j$ is referred to as the sign of the covariant derivative with respect to coordinate $u^j$.

The increment of the vector field as represented in terms of the covariant components $a(u^1, u^2, u^3) = a_i r^i$ up to the linear with respect to $\delta u^j$ terms is

$$\delta a = \frac{\partial a_i}{\partial u^j} \delta u^j r^i + a_i \frac{\partial r^i}{\partial u^j} \delta u^j.$$

From this expression we obtain the formula for the derivative of the vector field in the representation using covariant components

$$\frac{\partial a}{\partial u^j} = \frac{\partial a_i}{\partial u^j} r^i - a_i \Gamma_{ij}^k r^k = \left( \frac{\partial a_i}{\partial u^j} - a_n \Gamma_{ij}^n \right) r^i.$$

The expression

$$\nabla_j a_i = \frac{\partial a_i}{\partial u^j} - a_n \Gamma_{ij}^n$$

(A.6.2)

is called the covariant derivative of the covariant components of the vector field.

The metric tensor is a second-rank tensor, and forms a tensor field in space. By analogy, representing the vector in the form $a = a_i r^i = a^i r_i$, we can represent a second-rank tensor—for example, the metric tensor—using dyads of the basis vectors in the form $M = g_{ik} r^i r^k = g^{ik} r_i r_k$. Differentiating the tensor in this representation using the rule of differentiation of sums and products of functions, we obtain the expression for the covariant derivatives of the components of the second-rank tensor

$$\frac{\partial (g_{ik} r^i r^k)}{\partial u^j} = \frac{\partial g_{ik}}{\partial u^j} r^i r^k + g_{ik} \frac{\partial r^i}{\partial u^j} r^k + g_{ik} r^i \frac{\partial r^k}{\partial u^j} =$$

$$= \frac{\partial g_{ik}}{\partial u^j} r^i r^k - g_{ik} \Gamma_{nj}^n r^i r^k - g_{ik} r^i \Gamma_{kj}^n r^k =$$

$$= \left( \frac{\partial g_{ik}}{\partial u^j} - g_{nk} \Gamma_{ij}^n - g_{in} \Gamma_{kj}^n \right) r^i r^k = \nabla_j g_{ik} r^i r^k.$$

$$\frac{\partial (g^{ik} r_i r_k)}{\partial u^j} = \frac{\partial g^{ik}}{\partial u^j} r_i r_k + g^{ik} \frac{\partial r_i}{\partial u^j} r_k + g^{ik} r_i \frac{\partial r_k}{\partial u^j} =$$

$$= \frac{\partial g^{ik}}{\partial u^j} r_i r_k + g^{ik} \Gamma_{nj}^n r_i r_k + g^{ik} r_i \Gamma_{kj}^n r_k =$$

$$= \left( \frac{\partial g^{ik}}{\partial u^j} + g^{nk} \Gamma_{nj}^i + g^{in} \Gamma_{kj}^k \right) r_i r_k = \nabla_j g^{ik} r_i r_k,$$

where
$$ \nabla_j g_{ki} = \frac{\partial g_{ki}}{\partial u^j} - g_{ni} \Gamma_{kj}^n - g_{kn} \Gamma_{ij}^n. $$
(A.6.3)

$$ \nabla_j g^{ki} = \frac{\partial g^{ki}}{\partial u^j} + g^{ni} \Gamma_{nj}^k + g^{ki} \Gamma_{nj}^i $$
(A.6.4)

are covariant derivatives of the components of the metric tensor. Since no properties of the metric tensor components were used for the derivation of equations (A.6.3) and (A.6.4), any other components of a second-rank tensor can be substituted for the metric tensor components. Equalities (A.6.3) and (A.6.4) are definitions of covariant derivatives of covariant and contravariant components of second-rank tensors.

By analogy, representing the vectors in the form $a_i r^i = a r_i$, we can represent a tensor of any rank using its components and groups of corresponding basis vectors in the form $T = t^{kim} r_k r_l r_m = t_{kim} r^k r^l r^m = t_{lm} r^k r^l r^m = t_{lm} r^k r^l r^m$. Each superscript index of a tensor component corresponds to the vector of the tangent basis $r_i$, and each subscript index corresponds to the vector of the reciprocal basis $r^i$. By analogy with vectors, we obtain the formula for the covariant derivatives of the components of a tensor of arbitrary rank. For example, differentiating the right-hand side of expression $T = t^{ki} r_k r_l r^m$ according to the rules of differentiating sums and products of functions,

$$
\frac{\partial (t^{ki} r_k r_l r^m)}{\partial u^j} =
$$

$$
= \frac{\partial t^{ki}}{\partial u^j} r_k r_l r^m + t^{ki} \frac{\partial r_k}{\partial u^j} r_l r^m + t^{ki} r_k \frac{\partial r_l}{\partial u^j} r^m + t^{ki} r_k r_l \frac{\partial r^m}{\partial u^j} =
$$

$$
= \frac{\partial t^{ki}}{\partial u^j} r_k r_l r^m + t^{ki} \Gamma_{lj}^n r_n r_l r^m + t^{ki} \Gamma_{lj}^n r_n r_l r^m - t^{ki} \Gamma_{lj}^n r_n r_l r^m =
$$

$$
= \frac{\partial t^{ki}}{\partial u^j} r_k r_l r^m + t^{mi} \Gamma_{lj}^k r_k r_l r^m + t^{mi} \Gamma_{lj}^k r_k r_l r^m - t^{ki} \Gamma_{lj}^n r_n r_l r^m =
$$

$$
= \left( \frac{\partial t^{ki}}{\partial u^j} + t^{mi} \Gamma_{lj}^k + t^{mi} \Gamma_{lj}^k - t^{ki} \Gamma_{lj}^n \right) r_k r_l r^m =
$$

$$
= \nabla_j t^{ki} r_k r_l r^m
$$

and taking the components of the same triad of basis vectors of the resultant, we obtain expressions for covariant derivatives of the mixed components of a third-rank tensor

$$ \nabla_j t^{ki} = \frac{\partial t^{ki}}{\partial u^j} + t^{mi} \Gamma_{lj}^k + t^{mi} \Gamma_{lj}^k - t^{ki} \Gamma_{lj}^n. $$

From this result, we can formulate a general rule for calculating the covariant derivative of components of a tensor of arbitrary rank. Besides the partial derivative of a given tensor component $\partial t^{***}/\partial u$ (indices are replaced with dots), a few sums are
added into the covariant derivative, each corresponding to one of the indices. Since each subscript index corresponds to a sum of the form $-t_{n}^{***}\Gamma_{*j}^{n}$, and each superscript index corresponds to a sum of the form $+t_{n}^{***}\Gamma_{nj}^{*}$, where the value of the corresponding index (designated by a point) passes from the components to their Christoffel symbols, and summation is performed over the index $n$. In symbolic notation, it looks like this:

$$\nabla_{j}t_{n}^{***} = \frac{\partial t_{n}^{***}}{\partial u^{j}} + ... + t_{n}^{***}\Gamma_{nj}^{*} + ... - ... - t_{n}^{***}\Gamma_{*j}^{n} - ...$$

Let us show that the components of the metric tensor can be taken out of the symbol of the covariant derivative $\nabla_{j}$. Differentiating equalities $g_{ki}=r_{i}r_{k}$ and $g^{ki}=r^{k}r^{i}$, and using (A.5.2) and (A.5.9), we obtain expressions for the derivatives of the metric tensor components:

$$\frac{\partial g_{ki}}{\partial u^{j}} = g_{kn}\Gamma_{ij}^{n} + g_{ni}\Gamma_{kj}^{n}, \quad (A.6.5)$$

$$\frac{\partial g^{ki}}{\partial u^{j}} = -g^{kn}\Gamma_{nj}^{i} - g^{ni}\Gamma_{kj}^{k}. \quad (A.6.6)$$

Substituting relations $a^{i}=g^{ik}a_{k}$ and (A.6.6) into equation (A.6.1), we obtain

$$\nabla_{j}a^{i} = \nabla_{j}(g^{ik}a_{k}) = g^{ik}\frac{\partial a_{k}}{\partial u^{j}} + a_{k}\frac{\partial g^{ik}}{\partial u^{j}} + a_{k}g^{nk}\Gamma_{nj}^{i} =$$

$$= g^{ik}\frac{\partial a_{k}}{\partial u^{j}} - a_{k}g^{nk}\Gamma_{nj}^{k} = g^{ik}\left(\frac{\partial a_{k}}{\partial u^{j}} - a_{n}\Gamma_{kj}^{n}\right) = g^{ik}\nabla_{j}a_{k}. \quad (A.6.7)$$

In the transformation, we changed the notation of the dummy indices. Similarly, substituting relations $a_{i}=g_{ik}a^{k}$ and (A.6.5) into equation (A.6.2), we obtain

$$\nabla_{j}a_{i} = \nabla_{j}(g_{ik}a^{k}) = g_{ik}\frac{\partial a^{k}}{\partial u^{j}} + a^{k}\frac{\partial g_{ik}}{\partial u^{j}} - a^{k}g_{kn}\Gamma_{nj}^{n} =$$

$$= g_{ik}\frac{\partial a^{k}}{\partial u^{j}} + a^{k}g_{nk}\Gamma_{nj}^{k} = g_{ik}\left(\frac{\partial a^{k}}{\partial u^{j}} + a^{n}\Gamma_{nj}^{k}\right) = g_{ik}\nabla_{j}a^{k}. \quad (A.6.8)$$

From equations (A.6.7) and (A.6.8) we conclude that the components of the metric tensor can be taken out of the symbol of the covariant derivative. As might be expected, from relations (A.6.5) and (A.6.6) it follows that the covariant derivatives of the components of the metric tensor, (A.6.3) and (A.6.4), are equal to zero.

Nabla-operator or Hamiltonian operator are alternative names for the same operator that is denoted by symbol $\nabla$, whose formal definition is
$$ \nabla = \frac{\partial}{\partial u^j} r^j = \frac{\partial}{\partial u^1} r^1 + \frac{\partial}{\partial u^2} r^2 + \frac{\partial}{\partial u^3} r^3. $$

The Hamiltonian operator is considered to have the attributes of a vector. By applying the Hamiltonian operator to a tensor, a new tensor can be constructed. For example, as a result of applying the Hamiltonian operator to a tensor of rank zero (scalar), $f$, we obtain a first-rank tensor (vector), which is called the gradient of a scalar:

$$ \nabla f = r^j \frac{\partial f}{\partial u^j} = r^1 \frac{\partial f}{\partial u^1} + r^2 \frac{\partial f}{\partial u^2} + r^3 \frac{\partial f}{\partial u^3} = \text{grad } f. $$

The Hamilton operator can act on tensors as a tensor (the result is a tensor which rank is higher than the original tensor rank by one), a scalar (the rank of the result is lower than the rank of the original tensor by one), or a vector (the rank of the result is equal to the rank of the original tensor):

$$ \nabla a = r^j \frac{\partial a}{\partial u^j} = r^j r^i \left( \frac{\partial a_i}{\partial u^j} - a_n \Gamma^n_{ij} \right) = \nabla_j a_i r^j r^i = \text{grad } a, $$

$$ \nabla \cdot a = r^j \cdot \frac{\partial a}{\partial u^j} = r^j \cdot r^i \left( \frac{\partial a_i}{\partial u^j} - a_n \Gamma^n_{ij} \right) = \nabla_j a^j = \text{div } a, $$

$$ \nabla \times a = r^j \times \frac{\partial a}{\partial u^j} = r^j \times r^i \left( \frac{\partial a_i}{\partial u^j} - a_n \Gamma^n_{ij} \right) = \frac{1}{\sqrt{g}} e^{ijk} r_k \nabla_j a_i = \text{rot } a. $$

The result of applying the Hamiltonian operator to the tensor $T = t^k_{im} r_k r_l r^m$ has the form

$$ \nabla T = r^j \frac{\partial T}{\partial u^j} = \nabla_j t^k_{im} r_k r_l r^m = \text{grad } T, $$

$$ \nabla \cdot T = r^j \cdot \frac{\partial T}{\partial u^j} = \nabla_j t^j_{im} r_l r^m = \text{div } T, $$

$$ \nabla \times T = r^j \times \frac{\partial T}{\partial u^j} = \frac{e^{jqn}}{\sqrt{g}} g_{kj} \nabla_j t^k_{im} r_l r^m = \frac{e^{jqn}}{\sqrt{g}} \nabla_j t^j_{kn} r_l r^m = \text{rot } T. $$

The Hamilton operator may act several times on the same object. For example, the scalar product of Hamiltonian operators is called the Laplace operator:

$$ \nabla^2 = \nabla \cdot \nabla = g^{ij} \frac{\partial^2}{\partial u^i \partial u^j} - g^{ik} \Gamma^k_{ij} \frac{\partial}{\partial u^j}. $$

The action of the Laplace operator on a scalar can be written as

$$ \nabla \cdot \nabla f = \nabla^2 f = \text{div grad } f. $$
In a Cartesian coordinate system, the Laplace operator has the form

$$\nabla^2 = \frac{\partial^2}{(\partial x_1)^2} + \frac{\partial^2}{(\partial x_2)^2} + \frac{\partial^2}{(\partial x_3)^2}.$$

The Hamiltonian operator is used to describe tensor (or scalar or vector) fields. The above formulas allow us to write out equations for tensors that are invariant with respect to their coordinate systems. For example, using the Hamiltonian operator, the differential $da$ of vector field $\mathbf{a}(u^1, u^2, u^3)$ can be expressed as:

$$da = \frac{\partial \mathbf{a}}{\partial u^i} du^i = du^n r_n \cdot \frac{\partial \mathbf{a}}{\partial u^i} = dr \cdot \nabla \mathbf{a} = (\nabla \mathbf{a})^T \cdot dr,$$

where we use the notation $dr = du^n r_n$.

### A.7. Examples of Tensors

The **strain tensor** is used in continuum mechanics to determine changes in distances and angles between points of the medium. The strain tensor is a symmetric second-rank tensor. Consider two infinitely close points of the medium, $P$ and $Q$. Let point $P$ have coordinates $u^1, u^2,$ and $u^3$, and point $Q$ have coordinates $u^1+du^1, u^2+du^2,$ and $u^3+du^3$ before the deformation. An infinitesimal fiber connecting these points can be described by the vector $dr = du^i r_i$. Recall that we use the agreement on summation over repeated indices in these expressions. The square of the length of the fiber connecting points $P$ and $Q$ of the medium before the deformation is expressed through components of the metric tensor:

$$ds^2 = dr \cdot dr = du^i r_i \cdot r_j du^j = du^i g_{ij} du^j = [du^1 du^2 du^3] \cdot G \cdot [du^1 du^2 du^3]^T,$$

where $G = \begin{bmatrix} g_{11} & g_{12} & g_{13} \\ g_{21} & g_{22} & g_{23} \\ g_{31} & g_{32} & g_{33} \end{bmatrix}$ is the matrix of the metric tensor. Let the vector field

$$\mathbf{a}(u^1, u^2, u^3) = \begin{bmatrix} a^1(u^1, u^2, u^3) \\ a^2(u^1, u^2, u^3) \\ a^3(u^1, u^2, u^3) \end{bmatrix}$$

describe the displacement of the material point with coordinates $u^1, u^2,$ and $u^3$. As a result of the deformation of the continuous medium, the considered points are displaced and take new positions. After the deformation, point $P$ is described by the coordinates $u^1+a^1, u^2+a^2,$ and $u^3+a^3$, and point $Q$ is described by coordinates $u^1+du^1+a^1+da^1, u^2+du^2+a^2+da^2,$ and $u^3+du^3+a^3+da^3$. The differential of the displacement vector field $da(u^1, u^2, u^3)$ describes the change in the distance between
infinitely close points of a continuous medium. After the deformation, the considered infinitesimal fiber is described by the vector

$$ dr' = dr + da = dr + (\nabla a)^T \cdot dr = du^i r_i + \nabla_i a^n du^i r_n. $$

The square of the length of the fiber connecting points $P$ and $Q$ of the medium after the deformation is expressed as follows:

$$
(ds')^2 = dr' \cdot dr' = (dr + (\nabla a)^T \cdot dr) \cdot (dr + (\nabla a)^T \cdot dr) =
$$
$$
= (du^i r_i + \nabla_i a^n du^i r_n) \cdot (du^j r_j + \nabla_j a^k du^j r_k) =
$$
$$
= du^i \left( g_{ij} + \nabla_i a_j + \nabla_j a_i + \nabla_i a^n \nabla_j a_n \right) du^j =
$$
$$
= [du^1 du^2 du^3] \cdot G' \cdot [du^1 du^2 du^3]^T,
$$

where $G'$ is a matrix with components $g_{ij}' = g_{ij} + \nabla_i a_j + \nabla_j a_i + \nabla_i a^n \nabla_j a_n$. The strain tensor is defined by the equation

$$
\varepsilon = \frac{1}{2} (G' - G),
$$

where $\varepsilon = \begin{bmatrix} \varepsilon_{11} & \varepsilon_{12} & \varepsilon_{13} \\ \varepsilon_{21} & \varepsilon_{22} & \varepsilon_{23} \\ \varepsilon_{31} & \varepsilon_{32} & \varepsilon_{33} \end{bmatrix}$ is the matrix of the strain tensor in the covariant representation. The covariant components of the strain tensor are defined by the formula

$$
\varepsilon_{ij} = \frac{1}{2} (\nabla_i a_j + \nabla_j a_i + \nabla_i a^n \nabla_j a_n). \tag{A.7.1}
$$

Formula (A.7.1) is obtained under the assumption that the coordinate system $u^1, u^2, u^3$ remains unchanged during the deformation. In continuum mechanics, the consideration of a process in a fixed coordinate system is called a spatial representation, and the system itself is called an Euler system. There is another approach, in which a coordinate system $u^1, u^2, u^3$ is assumed to be connected with the material points, and is deformed together with the medium. For this approach, coordinates of material points remain constant under deformation, but components of the metric tensor are changed. The infinitesimal fiber connecting the considered points after the deformation is described by the vector $dr' = du^i r_i$, where the basis vectors $r_i$ differ from the basis vectors $r_n$ of the original state. This type of description of a process is called a material representation, and the system used is called a Lagrangian system. The covariant components of the strain tensor in the material representation are determined by the formula
The strain tensor can be defined in the coordinate system with the basis vectors $r_n$ (in the initial configuration in the spatial representation), or can be specified in the coordinate system with basis vectors $r_n'$ (in the final configuration in the material representation). In the first case, the strain tensor is called the Cauchy-Green strain tensor; in the second case it is called the Almansi-Hamel strain tensor. In general, the strain tensor can be described in an arbitrary coordinate system.

As an example, let us obtain the strain tensor in a coordinate system approximately describing a deformed state of a continuous medium. Application of formula (A.7.1) for large displacements is complicated by the terms $\nabla_i a^n \nabla_j a_n$ that are non-linear with respect to the components of the displacement vector, which cannot always be neglected. To use formula (A.7.2), we need to know the metric tensor for the initial state and the final state—which is unknown and must be determined. Suppose that we are to apply the material representation, and in the process of solving the problem we know the deformed state of the medium approximately (for example, from the previous iteration). Since we know the deformed condition only approximately, the coordinates of the material points in our approach do not remain constant, but the change is small. Major changes occur in the basis vectors of the coordinate system, moving from $r_n$ in the not-deformed state to $r_n'$, approximately describing the deformed state of the medium. In this approach, after deformation the infinitesimal fiber connecting the considered points $P$ and $Q$, is described by the vector

$$
dr' = dr + dv = dr + (\nabla v)^T \cdot dr = du^i r_i' + \nabla_i v^j du^j r_n',
$$

where the vector field $v(u^1, u^2, u^3) = \begin{bmatrix} v^1(u^1, u^2, u^3) \\ v^2(u^1, u^2, u^3) \\ v^3(u^1, u^2, u^3) \end{bmatrix}$ describes the displacement of the point of the medium with coordinates $u^1, u^2, u^3$ to the final state. If we know the deformed state of the medium precisely, then the equality $r_n' = r_n$ is satisfied and the vector field $v(u^1, u^2, u^3)$ is zero. The vector $v(u^1, u^2, u^3)$ describes the magnitude of the error in our knowledge of the deformed state. In this case, after the deformation, the square of the length of the fiber between points $P$ and $Q$ of the medium is expressed as:

$$
(ds')^2 = (du^i r_i' + \nabla_i v^j du^j r_n') \cdot (du^i r_i' + \nabla_i v^j du^j r_n') = du^i \left( g_{ij}' - g_{ij} + \nabla_i v_j + \nabla_j v_i + \nabla_i v^m \nabla_j v_m \right) du^j,
$$

The strain-tensor components in this approach are defined by the equality

$$
\varepsilon_{ij} = \frac{1}{2} \left( g_{ij}' - g_{ij} + \nabla_i v_j + \nabla_j v_i + \nabla_i v^m \nabla_j v_m \right).
$$
Since $r_{n}$ are close to $r_{n}$, the vector components $v(u^{1}, u^{2}, u^{3})$ are small and formula (A.7.3) can be linearized and represented in the form

$$
\varepsilon_{ij} = \frac{1}{2} \left( g_{ij} - g_{ij} + \nabla_{i} v_{j} + \nabla_{j} v_{i} \right).
$$

(A.7.4)

Formula (A.7.4) can be used for large displacements. Its advantage is that it contains only linear terms for the components of the vector $v(u^{1}, u^{2}, u^{3})$. Determination of the deformed state must be made by iterative methods. We approximately know the deformed condition of the medium and the associated coordinate system $u^{1}, u^{2}, u^{3}$ at each iteration. The basis vectors $r_{n}$ and the components of the metric tensor $g_{ij}$ must be calculated for this state. Next, using (A.7.4), we find the correction $v(u^{1}, u^{2}, u^{3})$ to the vector field of displacements. The vector field $v(u^{1}, u^{2}, u^{3})$ is zero at the point of solution.

A curvature tensor is used to determine the properties of a space. In general, the order of differentiation with respect to the coordinates is important in curved spaces. When changing the order of differentiation, additional terms appear. Let some vector function $a = a(u^{1}, u^{2}, u^{3}) r^{i}$ be given. Consider some surface $u^{i} = u^{i}(t, w), i = 1, 2, 3$, in the space. We can always choose a surface that passes through any given point or line. Let us calculate the absolute differential $D_{t}a$ of the vector function for infinitesimal displacement from the point with coordinates $u^{1}, u^{2}, u^{3}$ to the point with coordinates $u^{1} + \frac{\partial u^{1}}{\partial t} dt, u^{2} + \frac{\partial u^{2}}{\partial t} dt, u^{3} + \frac{\partial u^{3}}{\partial t} dt$ along the surface in the direction of its first parameter

$$
D_{t}a = \left( \frac{\partial a_{i}}{\partial u^{j}} - a_{n} \Gamma_{ij}^{n} \right) r^{i} \frac{\partial u^{j}}{\partial t} dt = \left( \frac{\partial a_{i}}{\partial t} - a_{n} \Gamma_{ij}^{n} \frac{\partial u^{j}}{\partial t} \right) r^{i} dt \equiv (D_{t}a)_{i} r^{i} dt.
$$

Similarly, let us calculate the absolute differential $D_{w}a$ of the vector function for infinitesimal displacement from the same point to the point with coordinates $u^{1} + \frac{\partial u^{1}}{\partial w} dw, u^{2} + \frac{\partial u^{2}}{\partial w} dw, u^{3} + \frac{\partial u^{3}}{\partial w} dw$ along the surface in the direction of its second parameter

$$
D_{w}a = \left( \frac{\partial a_{i}}{\partial u^{j}} - a_{n} \Gamma_{ij}^{n} \right) r^{i} \frac{\partial u^{j}}{\partial w} dw = \left( \frac{\partial a_{i}}{\partial w} - a_{n} \Gamma_{ij}^{n} \frac{\partial u^{j}}{\partial w} \right) r^{i} dw \equiv (D_{w}a)_{i} r^{i} dw.
$$

The obtained differentials can also be considered vector functions of the same parameters at the same point. Let us calculate the differential of the vector function $D_{t}a$ along the surface in the direction of its second parameter, and the differential of the vector function $D_{w}a$ along the surface in the direction of its first parameter:
$$ D_wD_t a = \left( \frac{\partial (D_t a)_i}{\partial w} - (D_t a)_n \Gamma^n_j \frac{\partial u^j}{\partial w} \right) r^i dw = $$
$$ = \left( \frac{\partial^2 a_i}{\partial t \partial w} - \frac{\partial a_n}{\partial w} \Gamma^n_j \frac{\partial u^j}{\partial t} - a_n \frac{\partial \Gamma^n_j}{\partial w} \frac{\partial u^j}{\partial t} - a_n \Gamma^n_j \frac{\partial^2 u^j}{\partial t \partial w} - \frac{\partial a_n}{\partial t} \Gamma^n_r \frac{\partial u^r}{\partial w} + a_m \Gamma^m_j \frac{\partial u^j}{\partial t} \Gamma^n_r \frac{\partial u^r}{\partial w} \right) r^i dt dw. $$

$$ D_tD_w a = \left( \frac{\partial (D_w a)_i}{\partial t} - (D_w a)_n \Gamma^n_j \frac{\partial u^j}{\partial t} \right) r^i dt = $$
$$ = \left( \frac{\partial^2 a_i}{\partial w \partial t} - \frac{\partial a_n}{\partial t} \Gamma^n_j \frac{\partial u^j}{\partial w} - a_n \frac{\partial \Gamma^n_j}{\partial t} \frac{\partial u^j}{\partial w} - a_n \Gamma^n_j \frac{\partial^2 u^j}{\partial w \partial t} - \frac{\partial a_n}{\partial w} \Gamma^n_r \frac{\partial u^r}{\partial t} + a_m \Gamma^m_j \frac{\partial u^j}{\partial w} \Gamma^n_r \frac{\partial u^r}{\partial t} \right) r^i dw dt. $$

The obtained expressions differ in that the derivatives with respect to $t$ and with respect to $w$ are swapped. The first and fourth terms of the two expressions are identical. The second term of the first expression is equal to the fifth term of the second expression (if dummy index $r$ is denoted by $j$). Subtracting the second expression from the first expression, and changing the notations of the dummy indices, we obtain:

$$ D_wD_t a - D_tD_w a = $$
$$ = \left( -a_n \frac{\partial \Gamma^n_j}{\partial w} \frac{\partial u^j}{\partial t} + a_m \Gamma^m_j \frac{\partial u^j}{\partial t} \Gamma^n_r \frac{\partial u^r}{\partial w} + a_n \frac{\partial \Gamma^n_j}{\partial t} \frac{\partial u^j}{\partial w} - a_m \Gamma^m_j \frac{\partial u^j}{\partial t} \Gamma^n_r \frac{\partial u^r}{\partial t} \right) r^i dw dt = $$
$$ = \left( -\frac{\partial \Gamma^n_j}{\partial u^r} + \Gamma^k_j \Gamma^n_r \frac{\partial u^j}{\partial u^r} + \Gamma^k_j \Gamma^n_r \frac{\partial u^j}{\partial u^r} - \Gamma^k_j \Gamma^n_r \frac{\partial u^j}{\partial u^r} \right) \frac{\partial u^j}{\partial w} a_n r^i dw dt = $$
$$ = R_{rij} \frac{\partial u^j}{\partial t} \frac{\partial u^r}{\partial w} a_n dw dt r^i, \quad (A.7.5) $$

where we introduce the notation

$$ R_{rij} = \frac{\partial \Gamma^n_j}{\partial u^r} - \frac{\partial \Gamma^n_j}{\partial u^r} + \Gamma^k_j \Gamma^n_r \frac{\partial u^j}{\partial u^r} - \Gamma^k_j \Gamma^n_r \frac{\partial u^j}{\partial u^r}. \quad (A.7.6) $$
The coefficients $R_{rji}^n$ are the components of the space curvature tensor. The curvature tensor is also called the Riemann-Christoffel tensor. It depends only on the point in the space where it is calculated.

If one of the coordinate surfaces $u^1 = u^1(u^2, u^3)$, $u^2 = u^2(u^3, u^1)$, or $u^3 = u^3(u^1, u^2)$, passing through the considered point, is chosen as the surface $u^i = u^i(t, w)$, then expression (A.7.5) takes the form

$$D_r D_j a - D_j D_r a = R_{rji}^n a_n r^j du' du', \quad (A.7.7)$$

since $dw = du'$ and $dt = du'$. The left-hand side of (A.7.7) is called the second alternative differential of the vector function. If the vector function is chosen as an expansion in the tangent basis $a = a^i(u^1, u^2, u^3)r_i$, then performing a similar derivation we obtain the following expression for the second alternative differential of the vector function

$$D_r D_j a - D_j D_r a = -R_{rji}^n a^i r_n du' du'. \quad (A.7.7)$$

It can be seen from formula (A.7.7) that the curvature tensor is skew-symmetric with respect to the first two indices:

$$R_{rji}^n = -R_{jri}^n.$$

The components of the curvature tensor (A.7.6) are three times covariant and one time contravariant. Using the components of the metric tensor, we can obtain fully covariant components of the curvature tensor:

$$R_{rjk} = g_{nk} R_{jrk}^n.$$

The covariant components of the curvature tensor satisfy the symmetry conditions

$$R_{rjk} = -R_{jrk} = -R_{rjk} = R_{jkr}.$$

If the operation of convolution over indices $n$ and $r$ is applied to the curvature tensor, we obtain the Ricci tensor, whose covariant components are

$$R_{ji} = R_{nji}^n = \frac{\partial \Gamma_{in}^n}{\partial u^j} - \Gamma_{kn}^n \Gamma_{ij}^k - \frac{\partial \Gamma_{ij}^n}{\partial u^n} + \Gamma_{kj}^n \Gamma_{in}^k.$$

Convolving the Ricci tensor, we obtain the curvature invariant

$$R = g^{nr} R_{ji}.$$

The curvature tensor describes the curvature of a space. In a Euclidean space, all the components of the curvature tensor are zero. In the general case, a two-dimensional space on some surface is not Euclidean, and has a non-zero curvature tensor. A flat surface is an example of a two-dimensional Euclidean space. Although coordinate lines on a plane can be curves, all the components of the curvature tensor of flat space are
equal to zero. Spaces for which all the components of the curvature tensor are zero, by analogy with surfaces, are called flat.

In a space of any dimension, the curvature tensor is expressed in terms of the metric tensor components and its first and second order derivatives. This property was used by A. Einstein to obtain the equations for a gravitational field in general relativity. He was looking for an equation similar to the Poisson equation, in which the energy-momentum tensor would be proportional to the differential expression of the second order, formed by the components of the metric tensor of four-dimensional space-time. Such an equation, in the general case, has the form

$$ R_{ik} + c R g_{ik} + \lambda g_{ik} + \mu T_{ik} = 0, $$

where $R_{ik}$ are the covariant components of the Ricci tensor, $R$ is the curvature invariant, $g_{ik}$ are the covariant components of the metric tensor, $T_{ik}$ are the covariant components of the energy-momentum tensor, and $c, \lambda,$ and $\mu$ are constants. Based on the principles of general relativity, we obtain the Einstein equation

$$ R_{ik} - \frac{1}{2} R g_{ik} + \lambda g_{ik} = -\mu T_{ik}. $$

Spaces of dimensions with non-zero curvature tensors are the subject of Riemannian geometry.

### A.8. Orthogonal Curvilinear Coordinates

Description of the geometry of objects in curvilinear coordinates is complicated. In practice, orthogonal curvilinear coordinates are used, in most cases. In an orthogonal coordinate system, coordinate lines of different families are mutually orthogonal. Vectors $r_1, r_2,$ and $r_3$ of the tangent basis are also mutually orthogonal, since they are tangential to the corresponding coordinate lines. In an orthogonal curvilinear coordinate system, vectors $r^1, r^2,$ and $r^3$ of the tangent basis and the corresponding vectors $r^1, r^2,$ and $r^3$ of the reciprocal basis, have the same direction, but their length is generally different; the off-diagonal components of the metric tensor are zero; i.e., $g_{ij} = 0$ and $g^{ij} = 0$ when $i \neq j,$ and $g^{ii} = \frac{1}{g_{ii}}.$ Some of the Christoffel symbols in an orthogonal curvilinear coordinate system are zeros, and, consequently, many formulas are simplified.

A **cylindrical coordinate system** is an orthogonal coordinate system. The parameters of a cylindrical coordinate system are the polar radius ($u^1 = r$), the polar angle ($u^2 = \varphi$), and the vertical axis ($u^3 = z$). Cylindrical coordinates $r, \varphi,$ and $z$ are related to Cartesian coordinates $x^1, x^2,$ and $x^3$ by the equalities
$$ r = \sqrt{x^1 x^1 + x^2 x^2}, \quad \varphi = \arctg \left( \frac{x^2}{x^1} \right), \quad z = x^3. $$

The reverse dependencies have the form

$$ x^1 = r \cos \varphi, \quad x^2 = r \sin \varphi, \quad x^3 = z. $$

We assume that the parameters of the cylindrical coordinate system vary in the following range: $0 \leq r, 0 \leq \varphi < 2\pi.$

The Jacobi matrix of transition from a Cartesian coordinate system to a cylindrical coordinate system is:

$$
\begin{bmatrix}
\frac{\partial x^1}{\partial u^1} & \frac{\partial x^1}{\partial u^2} & \frac{\partial x^1}{\partial u^3} \\
\frac{\partial x^2}{\partial u^1} & \frac{\partial x^2}{\partial u^2} & \frac{\partial x^2}{\partial u^3} \\
\frac{\partial x^3}{\partial u^1} & \frac{\partial x^3}{\partial u^2} & \frac{\partial x^3}{\partial u^3}
\end{bmatrix} =
\begin{bmatrix}
\cos \varphi & -r \sin \varphi & 0 \\
\sin \varphi & r \cos \varphi & 0 \\
0 & 0 & 1
\end{bmatrix}.
$$

The components of the metric tensor in the new coordinate system are defined by the formula

$$ g_{kn} = \frac{\partial x^i}{\partial u^k} \frac{\partial x^j}{\partial u^n} \delta_j^i, $$

where $\delta_j^i$ are Kronecker symbols (A.4.7). The components of the metric tensor and non-zero Christoffel symbols in it are

$$
G = \begin{bmatrix}
g_{11} & g_{13} & g_{13} \\
g_{21} & g_{22} & g_{23} \\
g_{31} & g_{32} & g_{33}
\end{bmatrix} =
\begin{bmatrix}
1 & 0 & 0 \\
0 & r^2 & 0 \\
0 & 0 & 1
\end{bmatrix},
\quad G^{-1} = \begin{bmatrix}
g^{11} & g^{12} & g^{13} \\
g^{21} & g^{22} & g^{23} \\
g^{31} & g^{32} & g^{33}
\end{bmatrix} =
\begin{bmatrix}
1 & 0 & 0 \\
0 & \frac{1}{r^2} & 0 \\
0 & 0 & 1
\end{bmatrix},
$$

$$ \Gamma_{12,2} = \Gamma_{21,2} = r; \quad \Gamma_{22,1} = -r, $$
$$ \Gamma_{12}^2 = \Gamma_{21}^2 = \frac{1}{r}; \quad \Gamma_{22}^1 = -r. $$

As we see, in cylindrical coordinates the lengths of the first and third vectors of the tangent basis are equal to unity, and the length of the second vector corresponding to the polar angle is equal to $r.$

Vector functions in a cylindrical coordinate system are expressed through the vectors of the tangent and reciprocal bases as follows:
$$ \mathbf{a} = a^r e_r + a^\varphi e_\varphi + a^z e_z = a^r e^r + a^\varphi e^\varphi + a^z e^z. $$

Partial derivatives of the vectors of the tangent basis (A.5.2) in cylindrical coordinates are

$$
\begin{align*}
\frac{\partial e_r}{\partial r} &= 0, & \frac{\partial e_r}{\partial \varphi} &= \frac{1}{r} e_\varphi, & \frac{\partial e_r}{\partial z} &= 0, \\
\frac{\partial e_\varphi}{\partial r} &= \frac{1}{r} e_r, & \frac{\partial e_\varphi}{\partial \varphi} &= -r e_r, & \frac{\partial e_\varphi}{\partial z} &= 0, \\
\frac{\partial e_z}{\partial r} &= 0, & \frac{\partial e_z}{\partial \varphi} &= 0, & \frac{\partial e_z}{\partial z} &= 0.
\end{align*}
$$

Partial derivatives of the vectors of the reciprocal basis (A.5.9) in cylindrical coordinates are

$$
\begin{align*}
\frac{\partial e^r}{\partial r} &= 0, & \frac{\partial e^r}{\partial \varphi} &= r e_\varphi, & \frac{\partial e^r}{\partial z} &= 0, \\
\frac{\partial e^\varphi}{\partial r} &= -\frac{1}{r} e_r, & \frac{\partial e^\varphi}{\partial \varphi} &= -\frac{1}{r} e_r, & \frac{\partial e^\varphi}{\partial z} &= 0, \\
\frac{\partial e^z}{\partial r} &= 0, & \frac{\partial e^z}{\partial \varphi} &= 0, & \frac{\partial e^z}{\partial z} &= 0.
\end{align*}
$$

We can see that some vectors of the tangent and reciprocal bases of the cylindrical coordinate system change when moving from one point in the space to another. All of this generally complicates the description of geometric objects, but in some special cases usage of the curvilinear systems is justified. Formula (A.5.6) for the derivative of a vector function in a cylindrical coordinate system has the form

$$
\frac{d\mathbf{a}}{dt} = \left( \frac{da^r}{dt} - ra^\varphi \frac{d\varphi}{dt} \right) e_r + \left( \frac{da^\varphi}{dt} + \frac{a^r}{r} \frac{dr}{dt} + \frac{a^\varphi}{r} \frac{d\varphi}{dt} \right) e_\varphi + \frac{da^z}{dt} e_z.
$$

A spherical coordinate system is an orthogonal coordinate system. The parameters of a spherical coordinate system are the radius ($u^1 = r$), the longitude ($u^2 = \varphi$), and the latitude ($u^3 = \theta$). The spherical coordinates $r$, $\varphi$, and $\theta$ are related to the Cartesian coordinates $x^1$, $x^2$, and $x^3$ by the equalities

$$
r = \sqrt{x^1 x^1 + x^2 x^2 + x^3 x^3}, \quad \varphi = \arctg \left( \frac{x^2}{x^1} \right), \quad \theta = \arctg \left( \frac{\sqrt{x^1 x^1 + x^2 x^2}}{x^3} \right).
$$

The reverse dependencies have the form
$$ x^1 = r \cos \varphi \sin \theta, \quad x^2 = r \sin \varphi \sin \theta, \quad x^3 = r \cos \theta. $$

We assume that the parameters of the spherical coordinate system vary within the following limits: $0 \leq r, 0 \leq \varphi < 2\pi,$ and $0 \leq \theta \leq \pi.$

The Jacobi matrix of transition from the Cartesian coordinate system to the spherical coordinate system is:

$$
\begin{bmatrix}
\frac{\partial x^1}{\partial u^1} & \frac{\partial x^1}{\partial u^2} & \frac{\partial x^1}{\partial u^3} \\
\frac{\partial x^2}{\partial u^1} & \frac{\partial x^2}{\partial u^2} & \frac{\partial x^2}{\partial u^3} \\
\frac{\partial x^3}{\partial u^1} & \frac{\partial x^3}{\partial u^2} & \frac{\partial x^3}{\partial u^3}
\end{bmatrix} =
\begin{bmatrix}
\cos \varphi \sin \theta & -r \sin \varphi \sin \theta & r \cos \varphi \cos \theta \\
\sin \varphi \sin \theta & r \cos \varphi \sin \theta & r \sin \varphi \cos \theta \\
\cos \theta & 0 & -r \sin \theta
\end{bmatrix}.
$$

The components of the metric tensor in the spherical coordinate system are

$$
G = \begin{bmatrix}
g_{11} & g_{12} & g_{13} \\
g_{21} & g_{22} & g_{23} \\
g_{31} & g_{32} & g_{33}
\end{bmatrix} =
\begin{bmatrix}
1 & 0 & 0 \\
0 & r^2 \sin^2 \theta & 0 \\
0 & 0 & r^2
\end{bmatrix},
\quad G^{-1} = \begin{bmatrix}
g^{11} & g^{12} & g^{13} \\
g^{21} & g^{22} & g^{23} \\
g^{31} & g^{32} & g^{33}
\end{bmatrix} =
\begin{bmatrix}
1 & 0 & 0 \\
0 & \frac{1}{r^2 \sin^2 \theta} & 0 \\
0 & 0 & \frac{1}{r^2}
\end{bmatrix}.
$$

Only the following derivatives of the components of the metric tensor are non-zero:

$$
\frac{\partial g_{22}}{\partial u^1} = 2r \sin^2 \theta, \quad \frac{\partial g_{22}}{\partial u^3} = 2r^2 \sin \theta \cos \theta, \quad \frac{\partial g_{33}}{\partial u^1} = 2r.
$$

In accordance with (A.5.4), non-zero Christoffel symbols in the spherical coordinate system are

$$
\Gamma_{12,2} = \Gamma_{21,2} = r \sin^2 \theta, \quad \Gamma_{22,1} = -r \sin^2 \theta,
$$
$$
\Gamma_{23,2} = \Gamma_{32,2} = r^2 \sin \theta \cos \theta, \quad \Gamma_{22,3} = -r^2 \sin \theta \cos \theta,
$$
$$
\Gamma_{13,3} = \Gamma_{31,3} = r, \quad \Gamma_{33,1} = -r,
$$
$$
\Gamma_{12}^2 = \Gamma_{21}^2 = \frac{1}{r}, \quad \Gamma_{22}^1 = -r \sin^2 \theta,
$$
$$
\Gamma_{23}^2 = \Gamma_{32}^2 = \tan \theta, \quad \Gamma_{22}^3 = -\sin \theta \cos \theta,
$$
$$
\Gamma_{13}^3 = \Gamma_{31}^3 = \frac{1}{r}, \quad \Gamma_{33}^1 = -r.
$$

Vector functions in spherical coordinates are expressed through vectors of the tangent and reciprocal bases, as follows:

$$
a = a^r e_r + a^\theta e_\theta + a^\varphi e_\varphi = a_r e_r + a_\theta e_\theta + a_\varphi e_\varphi.
$$
Partial derivatives of the vectors of the tangent basis (A.5.2) with respect to spherical coordinates are

$$
\frac{\partial e_r}{\partial r} = 0, \quad \frac{\partial e_r}{\partial \varphi} = \frac{1}{r} e_\theta, \quad \frac{\partial e_r}{\partial \theta} = \frac{1}{r} e_\varphi,
$$
$$
\frac{\partial e_\varphi}{\partial r} = \frac{1}{r} e_\varphi, \quad \frac{\partial e_\varphi}{\partial \varphi} = -r \sin^2 \theta e_r, \quad \frac{\partial e_\varphi}{\partial \theta} = \tan \theta e_\varphi,
$$
$$
\frac{\partial e_\theta}{\partial r} = \frac{1}{r} e_\theta, \quad \frac{\partial e_\theta}{\partial \varphi} = \tan \theta e_\varphi, \quad \frac{\partial e_\theta}{\partial \theta} = -r e_r.
$$

Partial derivatives of the vectors of the reciprocal basis (A.5.9) with respect to spherical coordinates are

$$
\frac{\partial e^r}{\partial r} = 0, \quad \frac{\partial e^r}{\partial \varphi} = r \sin^2 \theta e_\varphi, \quad \frac{\partial e^r}{\partial \theta} = r e_\theta,
$$
$$
\frac{\partial e^\varphi}{\partial r} = -\frac{1}{r} e_\varphi, \quad \frac{\partial e^\varphi}{\partial \varphi} = -\frac{1}{r} e_r, \quad \frac{\partial e^\varphi}{\partial \theta} = -\tan \theta e_\varphi,
$$
$$
\frac{\partial e^\theta}{\partial r} = -\frac{1}{r} e_\theta, \quad \frac{\partial e^\theta}{\partial \varphi} = \sin \theta \cos \theta e_r, \quad \frac{\partial e^\theta}{\partial \theta} = -\frac{1}{r} e_r.
$$

Formula (A.5.6) for the derivative of the vector function in the spherical coordinate system has the form

$$
\frac{da}{dt} = \left( \frac{da^r}{dt} - a^\varphi r \sin^2 \theta \frac{d\varphi}{dt} - a^\theta r \frac{d\theta}{dt} \right) e_r + \\
+ \left( \frac{da^\varphi}{dt} + \frac{a^\varphi}{r} \frac{dr}{dt} + \frac{a^r}{r} \frac{d\varphi}{dt} + a^\varphi \tan \theta \frac{d\theta}{dt} + a^\theta \tan \theta \frac{d\varphi}{dt} \right) e_\varphi + \\
+ \left( \frac{da^\theta}{dt} + \frac{a^\theta}{r} \frac{dr}{dt} + \frac{a^r}{r} \frac{d\theta}{dt} - a^\varphi \sin \theta \cos \theta \frac{d\varphi}{dt} \right) e_\theta.
$$

Geometric modeling is usually performed in Cartesian coordinate systems, but the input and output information about a modeled object can be represented in curvilinear coordinates. Cylindrical and spherical coordinate systems are more frequently used than other curvilinear systems. The information given in this Appendix allows building any curvilinear coordinate system and establishing its relationship with the Cartesian coordinate system.
REFERENCES

1. Bartels R.H., Beatty J.C., Barsky B.A. An Introduction to Splines for use in Computer Graphics and Geometric Modeling. – Morgan Kaufmann Publishers Inc., San Mateo, California, 1987.

2. Bohm W. A Survey of Curve and Surface Methods in CAGD. – Computer Aided Geometric Design. – North-Holland Amsterdam, v.1, n.1, July 1984.

3. Cardon D.L. T-Spline Simplification. – Brigham Young University, 2007.

4. Christoph M. Hoffman. Geometric and Solid Modeling. – Morgan Kaufmann Publishers Inc., San Mateo, California, 1989.

5. De Boor C. A Practical Guide to Splines. – Springer, Berlin, 1879.

6. Golovanov N.N., Ilyutko D.P., Nosovskiy G.V., Fomenko A.T. Computer Geometry. – Akademiya, Moscow, 2006 (in Russian).

7. Golovanov N.N. Geometric Modeling. – Fizmat, Moscow, 2002 (in Russian).

8. Faux I.E., Pratt M.J. Computational Geometry for Design and Manufacture. – Ellis Horwood, Chichester, 1979.

9. Hilbert D., Cohn-Vossen S. Anschauliche Geometrie, – Berlin, 1932.

10. James D. Foley, Andries Van Dam. Fundamentals Interactive Computer Graphics. – Addison-Wesley Publishing Company Reading, Massachusetts, Menlo Park, California, London, Amsterdam, Don Mills, Ontario, Sydney, 1982.

11. Kramer C.A. Solving Geometric Constraint System: A Case Study in Kinematics. – The MIT Press, Cambridge, Massachusetts, London, 1992.

12. Les Piegl, Wayne Tiller. The NURBS Book. – Springer, 1997.

13. Neamtu M. Homogeneous Simplex Splines. – Vanderbilt University, Nashville.

14. Preparata F.P., Shamos M. Computational Geometry: An Introduction. – Springer-Verlag. New York Berlin Tokyo, 1985.

15. Sokolnikoff I.S. Tensor Analysis. Theory And Applications To Geometry And Mechanics Of Continua.

16. Versprille K.J. Computer-aided design applications of the rational B-spline approximation form. – Diss. Syracuse University, 1975.