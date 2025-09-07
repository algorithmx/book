SURFACES

Surfaces are the main descriptive elements of a modeled object's shape. In general, a surface has a complex boundary, described by two-dimensional curves in the parametric space of the surface. This boundary can be constructed for any surface having a domain of a simple form—for example, rectangular. This chapter deals with methods of surface construction. Surfaces can be constructed on a set of points, or they can be based on curves and on other surfaces.

2.1. Surfaces

Let a Cartesian rectangular coordinate system with a fixed orthonormal basis be chosen in a three-dimensional Euclidean space.

A surface is a vector function

$$ r(u,v) = \begin{bmatrix} r_1(u,v) \\ r_2(u,v) \\ r_3(u,v) \end{bmatrix} $$

(2.1.1)

of two scalar parameters, $u$ and $v$, taking their values in a two-dimensional connected domain $\Omega$. We will assume that the coordinates $r_1(u,v), r_2(u,v), r_3(u,v)$ of a point on the surface $r(u,v)$ are single-valued continuous functions of parameters $u$ and $v$. This is a parametric description of the surface. A description of a surface by an equation satisfied by the points of the surface is not invariant under coordinate transformations; that is, transition to a different coordinate system changes the surface equation.

The surface is a continuous mapping of a two-dimensional connected domain $\Omega$ into three-dimensional space. The area $\Omega$ will be described in a two-dimensional Cartesian coordinate system. In the special case, the area $\Omega$ is a rectangle and the parameters of the surface take their values in the range $v_{\min} \leq v \leq v_{\max}, \ v_{\min} \leq v \leq v_{\max}$. In general, the area $\Omega$ is described by two-dimensional curves.

The surface is called periodic with respect to the first parameter if there is a $p_u > 0$, such that $r(u+kp_u,v)=r(u,v)$, where $k$ is integer. The surface is called periodic with respect to the second parameter, if there is a $p_v > 0$, such that $r(u,v+kp_v)=r(u,v)$, where $k$ is integer. To avoid ambiguity, the domain of a periodic surface must lie within one period for each parameter. A periodic surface with a rectangular parameter domain $\Omega$ is called cyclic closed with respect to the first parameter, if $p_u = u_{\max} - u_{\min}$; and cyclic closed with respect to the second parameter, if $p_v = v_{\max} - v_{\min}$.
We introduce the following notation for the partial derivatives with respect to the parameters of the surface.

$$ r_1 = \frac{\partial r}{\partial u}, \quad r_2 = \frac{\partial r}{\partial v}, \quad r_{11} = \frac{\partial^2 r}{\partial u^2}, \quad r_{22} = \frac{\partial^2 r}{\partial v^2}, \quad r_{12} = \frac{\partial^2 r}{\partial u \partial v} = r_{21} = \frac{\partial^2 r}{\partial v \partial u}. $$

The subscript index in the notation corresponds to the number of the parameter with respect to which the differentiation is performed. Next, we assume that the coordinate functions $r_1(u,v), r_2(u,v), r_3(u,v)$ have continuous derivatives in each parameter of any order we need.

The point of the surface is called regular if at this point the lengths of the partial derivatives with respect to both parameters of the surface are non-zero, and partial derivatives of the surface are not parallel. Otherwise the point of the surface is called singular.

It is possible to construct a surface at a regular point on the vectors $r_1$ and $r_2$. A plane passing through the point of the surface parallel to the vectors $r_1$ and $r_2$ at this point is called a tangent plane to the surface.

If we fix one of the parameters, and change the other one within some limits, we get a curve that lies on the surface. Such curves are called coordinate curves of the surface. The curves along which only the $u$ parameter changes are called $u$-lines, and the curves along which only the $v$ parameter changes are called $v$-lines. Derivatives $r_1$ and $r_2$ of the surface are the vectors tangent to the corresponding coordinate curves.

In order to construct an arbitrary curve on the surface one can introduce the dependence of the surface parameters $u$ and $v$ on some common parameter—for example, $u = u(t)$ and $v = v(t)$. Surface parameters $u$ and $v$ are the coordinates of the point on the surface in some chosen Cartesian coordinate system. We use lowercase letters in bold italics to denote the column coordinates of the points and column components of the vectors in two-dimensional space; for example,

$$ p = \begin{bmatrix} u \\ v \end{bmatrix}. $$

The term two-dimensional curve denotes the vector function

$$ r(t) = \begin{bmatrix} u(t) \\ v(t) \end{bmatrix} $$
(2.1.2)

of scalar parameter $t$ that takes values in the range of $t_{\text{min}} \leq t \leq t_{\text{max}}$. Let coordinates $u(t), v(t)$ of a point on a plane curve be single-valued continuous functions of parameter $t$. Similar to three-dimensional curves, plane curves can be cyclic and cyclic closed curves.

Two-dimensional curves can be constructed on a set of points, on the basis of other plane curves, or using analytic functions. We will use the methods of three-dimensional curve construction to construct two-dimensional curves—with the only
difference being that instead of using three-dimensional objects we will use two-
dimensional points, vectors, and base curves.

A **surface curve** is described by the relation

$$\mathbf{r}(t) = \begin{bmatrix} r_1(u(t), v(t)) \\ r_2(u(t), v(t)) \\ r_3(u(t), v(t)) \end{bmatrix}. \quad (2.1.3)$$

The derivative of the surface curve

$$\frac{d\mathbf{r}}{dt} = r_1 \frac{du}{dt} + r_2 \frac{dv}{dt}$$

lies in a tangent plane constructed at the given point.

The **metric properties** of the surface are expressed by the metric properties of the curves on it. Let us investigate the metric properties of a surface in the neighborhood of a point specified by parameters $u$ and $v$. Let us move from the given point along some surface curve to an infinitely close point specified by the parameters $u+du$, $v+dv$, and calculate the arc length. Up to the term linearly dependent on infinitesimals, the arc length is

$$ds = |r_1 du + r_2 dv|.$$

The squared length of an infinitesimal arc is

$$ds^2 = r_1^2 du^2 + 2r_1 r_2 dudv + r_2^2 dv^2.$$

We introduce the notation

$$g_{11} = r_1 \cdot r_1, \quad g_{12} = g_{21} = r_1 \cdot r_2 = r_2 \cdot r_1, \quad g_{22} = r_2 \cdot r_2. \quad (2.1.4)$$

Then the length of an infinitesimal arc of the surface curve will be given by the formula

$$ds^2 = g_{11} du^2 + 2g_{12} dudv + g_{22} dv^2.$$

The expression on the right-hand side is a quadratic form of differentials $du$ and $dv$, and is called the **first quadratic form** of the surface. The quantities $g_{11}(u,v)$, $g_{12}(u,v)$, $g_{21}(u,v)$, and $g_{22}(u,v)$ determine the metric properties of the surface and are called the coefficients of the first quadratic form of the surface.

Using the first quadratic form we can calculate the **arc length** of the surface curve. Suppose we are given with a segment of a surface curve $u=u(t)$, $v=v(t)$, $t_1 \leq t \leq t_2$. In the limit, the sum of infinitesimal arc lengths $ds$ gives the length of the corresponding segment of the curve.
The first quadratic form of the surface allows calculation of angles between the surface curves. Suppose there are two surface curves passing through a common point defined by parameters $u$ and $v$. Denote by $du$ and $dv$ the differentials of the surface parameters corresponding to the infinitesimal shift along the first surface curve, and by $\delta u$ and $\delta v$ the differentials of the surface parameters corresponding to an infinitesimal shift along the second surface curve. These infinitesimal shifts are determined by the vectors

$$
dr = r_1 du + r_2 dv, \quad \delta r = r_1 \delta u + r_2 \delta v.
$$

Let us find the cosine of the angle $\varphi$ between the surface curves as a dot product of vectors tangent to the curves, divided by the product of the lengths of these vectors.

$$
\cos \varphi = \frac{dr \cdot \delta r}{|dr||\delta r|} = \frac{g_{11} du \delta u + g_{12} du \delta v + g_{21} dv \delta u + g_{22} dv \delta v}{\sqrt{(g_{11} du \delta u + 2g_{12} du \delta v + g_{22} dv \delta v)(g_{11} \delta u \delta u + 2g_{12} \delta u \delta v + g_{22} \delta v \delta v)}}.
$$

This expression allows us to find the angle between the coordinate $u$-curve and $v$-curve at the given point of the surface, if we assume that $du \neq 0, \; dv = 0, \; \delta u = 0, \; \delta v \neq 0$ at this point; then

$$
\cos \varphi = \frac{g_{12}}{\sqrt{g_{11} g_{22}}}.
$$

If $g_{12} = 0$, then the coordinate curves at the given point are orthogonal.

The first quadratic form is also used for calculation of a surface area. Consider an infinitesimal curvilinear parallelogram with sides $du$ and $dv$ at the point specified by parameters $u$ and $v$ on the surface. The parallelogram area in the first approximation equals

$$
dS = |r_1 du \times r_2 dv| = |r_1 \times r_2| dudv.
$$

Represent the square of the vector length $r_1 \times r_2$ in the following way:

$$
|r_1 \times r_2|^2 = |r_1|^2 |r_2|^2 \sin^2 \varphi = |r_1|^2 |r_2|^2 (1 - \cos^2 \varphi) = g_{11} g_{22} \left( 1 - \frac{g_{12}^2}{g_{11} g_{22}} \right) = g_{11} g_{22} - g_{12}^2.
$$

Thus, the area of the infinitesimal curvilinear parallelogram in the first approximation is given by the formula
$$ dS = \sqrt{g_{11}g_{22} - g_{12}^2} \, du \, dv. $$

Then the area of the surface with the parameters taking values in a two-dimensional connected region $\Omega$ is calculated using the integral

$$ S = \iint_{\Omega} \sqrt{g_{11}g_{22} - g_{12}^2} \, du \, dv. $$

The geometrical properties of the surface, which can be determined by the first quadratic form, are called the internal geometry of the surface.

At a regular point, the normal to the surface is determined by the cross product $r_1 \times r_2$. Since vectors $r_1$ and $r_2$ lie on the tangent to the surface plane, their cross product is orthogonal to the tangent plane. Dividing the vector $r_1 \times r_2$ by its length, we obtain the formula for the unit normal to the surface at the given point:

$$ m = \frac{r_1 \times r_2}{\sqrt{g_{11}g_{22} - g_{12}^2}}. $$

Consider some surface curve defined by the functions $u = u(t), v = v(t)$. Calculate the increment that the radius vector of the surface curve gets with an infinitesimal increment of its parameter $dt$ by a precision of up to the second order of $dt$:

$$ \Delta r = \frac{dr}{dt} \, dt + \frac{1}{2} \frac{d^2r}{dt^2} \, dt^2. $$

Find the projection of $\Delta r$ on the normal to the surface at the given point. The first derivative of the curve is orthogonal to the normal to the surface, so the second derivative of the curve plays a major part in the projection $\Delta r$ on the normal:

$$ \frac{d^2r}{dt^2} = r_{11} \left( \frac{du}{dt} \right)^2 + 2r_{12} \frac{du}{dt} \frac{dv}{dt} + r_{22} \left( \frac{dv}{dt} \right)^2 + r_1 \frac{d^2u}{dt^2} + r_2 \frac{d^2v}{dt^2}. $$

The projection of the second derivative of the curve on the normal to the surface characterizes the curvature of the surface—only the surface, not the curve. Indeed, if the curve is constructed on the surface, then no matter how it is curved, the projection of the vector $\Delta r$ on the normal to the plane will be equal to zero. The dot product of $\Delta r$ and the surface normal yields

$$ \Delta r \cdot m = \frac{1}{2} \frac{d^2r}{dt^2} \cdot m \, dt^2 = \frac{1}{2} \left( r_{11} \cdot m \left( \frac{du}{dt} \right)^2 + 2r_{12} \cdot m \frac{du}{dt} \frac{dv}{dt} + r_{22} \cdot m \left( \frac{dv}{dt} \right)^2 \right) dt^2. $$
We introduce the notation

$$ b_{11} = r_{11} \cdot m, \quad b_{12} = b_{21} = r_{12} \cdot m = r_{21} \cdot m, \quad b_{22} = r_{22} \cdot m. $$
(2.1.5)

From this we have the expression for the major part of the deviation of the surface curve from the tangent plane:

$$ \Delta r \cdot m = \frac{1}{2} \left( b_{11} du^2 + 2b_{12} du dv + b_{22} dv^2 \right). $$

The expression in parentheses on the right side of this equation is a quadratic form of the differentials $du$ and $dv$. It is called the second quadratic form of the surface. The terms $b_{11}(u,v), b_{12}(u,v), b_{21}(u,v)$, and $b_{22}(u,v)$ determine the curvature of the surface; they are called the coefficients of the second quadratic form of the surface.

The coefficients of the second quadratic form can be expressed in a different way. We can use the fact that the normal vector $m$ is always orthogonal to the vectors $r_1$ and $r_2$. Let us differentiate the relations $m \cdot r_1 = 0$ and $m \cdot r_2 = 0$ with respect to $u$ and $v$, yielding

$$ b_{11} = -m_1 \cdot r_1, \quad b_{12} = -m_2 \cdot r_1, \quad b_{21} = -m_1 \cdot r_2, \quad b_{22} = -m_2 \cdot r_2, $$

where $m_1 = \frac{\partial m}{\partial u}$ and $m_2 = \frac{\partial m}{\partial v}$ are partial derivatives of the normal to the surface with respect to the parameters of the surface. The dot product of the differentials $dr = r_1 du + r_2 dv, dm = m_1 du + m_2 dv$ results in the equation

$$ -dr \cdot dm = b_{11} du^2 + 2b_{12} du dv + b_{22} dv^2. $$
(2.1.6)

Vector $m$ has unit length. We can differentiate the relation $m \cdot m = 1$ with respect to the parameters of the surface, and get as a result

$$ m_1 \cdot m = 0, \quad m_2 \cdot m = 0. $$

From these equations it follows that the derivatives of the normal to the surface with respect to the parameters lie in the tangent plane of the surface; i.e., $m_1$ and $m_2$ can be represented as expansions in vectors $r_1$ and $r_2$. The Weingarten derivative formulas

$$ m_1 = -\frac{b_{11} g_{22} - b_{12} g_{12}}{g} r_1 - \frac{b_{12} g_{11} - b_{11} g_{21}}{g} r_2, $$
$$ m_2 = -\frac{b_{21} g_{22} - b_{22} g_{12}}{g} r_1 - \frac{b_{22} g_{11} - b_{21} g_{21}}{g} r_2, $$

express the partial derivatives of the normal to the surface in terms of the derivatives of the surface and the coefficients of the first and the second quadratic forms. The coefficients of the Weingarten derivative formulas can be determined from the system of equations obtained by the dot product of the equations $m_1 = a_{11} r_1 + a_{12} r_2$ and $m_2 = a_{21} r_1 + a_{22} r_2$ by $r_1$ and $r_2$.
Let us establish the relation between the curvature of the surface curve and the orientation of its tangent vector in the osculating plane. Consider the equation

$$ m \cdot \frac{d^2 r}{dt^2} = b_{11} \left( \frac{du}{dt} \right)^2 + 2b_{12} \frac{du}{dt} \frac{dv}{dt} + b_{22} \left( \frac{dv}{dt} \right)^2. $$

The second derivative of the surface curve is

$$ \frac{d^2 r}{dt^2} = \frac{d^2 s}{dt^2} t + \left( \frac{ds}{dt} \right)^2 kn, $$

where $t$ — tangent vector of the surface curve, $n$ — principal normal of the surface curve, $k$ — curvature of the surface curve, $s$ — arc length of the surface curve. The tangent vector $t$ of the curve lies on the tangent to the surface plane and is orthogonal to the normal to the surface $m$; therefore the following equation holds:

$$ ds^2 kn \cdot m = b_{11} du^2 + 2b_{12} du dv + b_{22} dv^2. $$

Substituting the squared differential of the arc length of the curve expressed in the first quadratic form, we obtain

$$ kn \cdot m = \frac{b_{11} du^2 + 2b_{12} du dv + b_{22} dv^2}{g_{11} du^2 + 2g_{12} du dv + g_{22} dv^2}. $$
(2.1.7)

The geometric meaning of the last relation can be clearer if we consider the normal section of the surface—the intersection curve of the surface and the plane passing through the normal to the surface, and also through the tangent to the surface curve.

Fig. 2.1.1 shows a surface curve and corresponding normal section of a surface; the normal section passes through the given point on the curve. The first part of the equation (2.1.7) depends only on the location of the given point and the direction of the surface curve determined by the ratio of $du$ to $dv$. Therefore, any surface curve passing through the given point and having a tangent in common with the given normal section will have the same value $kn \cdot m$, despite the fact that it has a different curvature. The normal section lies on the surface as well as on the section plane, so its principal
normal lies on the section plane as well, and hence $|n \cdot m|=1$ for the normal section. Thus the normal section has the minimum curvature among all surface curves passing through the given point and having a tangent in common with it. This curvature is equal to

$$
\mu = \frac{b_{11}du^2 + 2b_{12}dudv + b_{22}dv^2}{g_{11}du^2 + 2g_{12}dudv + g_{22}dv^2}.
$$

(2.1.8)

The curvature of a normal section is called normal curvature of the surface at the given point and for the given direction.

The angle between the normal to the surface and the principal normal of the surface curve is equal to the angle between the normal section plane and the tangent plane of the curve. If the curvature of the normal section is known, then one can determine the curvature of the surface curve tangent to the normal section, provided that the angle between the normal to the surface and the principal normal of the curve is known.

This fact is stated in the Meusnier theorem formulated as: The curvature radius $p=1/k$ at a given point on the surface is equal to the product of the curvature radius $p_m=1/\mu$ of the corresponding normal section at this point by the cosine of the angle between the normal to the surface and the principal normal of the curve:

$$
\frac{1}{k} = \frac{1}{\mu} n \cdot m.
$$

If the normal section is tangent to the coordinate $u$-curve, then $dv=0$ and

$$
\mu_u = \frac{b_{11}}{g_{11}},
$$

where $\mu_u$ denotes the normal curvature of the surface in the $u$-direction. Similarly, the normal curvature of the surface $\mu_v$ in the $v$-direction is

$$
\mu_v = \frac{b_{22}}{g_{22}}.
$$

It is possible to construct many normal sections at a given point of a surface. These sections will differ in directions determined by the ratio of $du$ to $dv$. The direction of a normal section with zero curvature is called the asymptotic direction at the given point. There are no more than two asymptotic directions at each point on the surface, except for those cases when all of the coefficients of the second quadratic form at the given point vanish.

We have considered the projection of the curvature vector $kn$ of the surface curve onto the normal to the surface $m$. We will now consider the remaining part of the curvature vector—its projection on the tangent plane. It is equal to
$$ h = kn - m (kn \cdot m). $$

The length of the vector $h$ is called the **geodesic curvature** of the surface curve. The geodesic curvature of the normal section is equal to zero. If we construct the projection orthogonal to the tangent plane of the surface curve, then the curvature of this projection at the given point will be equal to the length of the vector $h$. The normal curvature is characteristic of the surface and the geodesic curvature is characteristic of the curve on it.

The **principal curvatures** of the surface determine the direction characterized by the relation between the vectors $dr$ and $dm$. From equations (2.1.6) and (2.1.8) it follows that the following equality holds for the vectors $dr$ and $dm$:

$$
\mu (dr \cdot dr) = -(dr \cdot dm),
$$
(2.1.9)

The curvature of the normal section at a given point depends on the relative directions of the vectors $dr$ and $dm$. Let us find such direction of movement along the surface on which the vectors $dr$ and $dm$ are collinear—i.e., where the equality $dm = \lambda dr$ holds. From equations (2.1.8) and (2.1.9) it follows that the following equality must hold for collinear vectors $dr$ and $dm$:

$$
\begin{bmatrix}
g_{11} & g_{12} \\
g_{21} & g_{22}
\end{bmatrix}
\begin{bmatrix}
du \\
dv
\end{bmatrix}
= \frac{1}{\lambda}
\begin{bmatrix}
b_{11} & b_{12} \\
b_{21} & b_{22}
\end{bmatrix}
\begin{bmatrix}
du \\
dv
\end{bmatrix}.
$$
(2.1.10)

Thus, the desired direction can be determined with the help of a system of linear algebraic equations for $du$ and $dv$

$$
\begin{bmatrix}
g_{11} & g_{12} \\
g_{21} & g_{22}
\end{bmatrix}
- \frac{1}{\lambda}
\begin{bmatrix}
b_{11} & b_{12} \\
b_{21} & b_{22}
\end{bmatrix}
\begin{bmatrix}
du \\
dv
\end{bmatrix} = 0.
$$

This system is homogeneous and has a nontrivial solution if the determinant of its matrix is zero:

$$
(g_{11}g_{22} - g_{12}^2)\lambda^2 - (b_{11}g_{22} + b_{22}g_{11} - 2b_{12}g_{12})\lambda + (b_{11}b_{22} - b_{12}^2) = 0.
$$
(2.1.11)

Expanding the determinant, we arrive at a quadratic equation with respect to $\lambda$, which in general provides us with two roots: $\lambda_1$ and $\lambda_2$. Substituting each root into any equation of (2.1.10) we obtain two directions on the surface, determined by the ratios $du_1/dv_1$ and $du_2/dv_2$.

The directions of motion on the surface for which vectors $dr$ and $dm$ are collinear are called the **principal directions** of the surface. The normal sections at a given point of the surface with their tangents directed along the principal directions are called the **principal sections**, and their curvatures are called the **principal curvatures** at the given point of the surface. It is simple to get the sum and the product of the principal curvatures from (2.1.11):
$$
\lambda_1 + \lambda_2 = \frac{b_{11}g_{22} + b_{22}g_{11} - 2b_{12}g_{12}}{g}, \quad \lambda_1 \lambda_2 = \frac{b_{11}b_{22} - b_{12}b_{21}}{g}.
$$
(2.1.12)

The half-sum of the principal curvatures is called the **mean curvature** of the surface at the given point, and the product of the principal curvatures is called the **Gauss curvature** of the surface at the given point.

Denote the tangent vectors of the normal sections along the principal directions by $t_1$ and $t_2$. Let us show that the principal directions of the surface are mutually orthogonal. Express the main directions in terms of the derivatives of the radius vector

$$
t_1 = r_1 du_1 + r_2 dv_1, \\
t_2 = r_1 du_2 + r_2 dv_2.
$$

Their dot product is

$$
t_1 \cdot t_2 = [du_1 \ dv_1] \cdot G \cdot [du_2 \ dv_2]^T,
$$
(2.1.13)

where $G = \begin{bmatrix} g_{11} & g_{12} \\ g_{21} & g_{22} \end{bmatrix}$.

We can show that it is generally zero. For this we write down the system of two equations (2.1.10) for the first principal direction, then multiply the first equation by $du_2$ and the second equation by $dv_2$. Next we add the first and the second equations and get the following result:

$$
[du_2 \ dv_2] \cdot (B - \lambda_1 G) \cdot [du_1 \ dv_1]^T = 0,
$$

where $B = \begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix}$.

Similarly, we obtain the second equation by interchanging the principal directions,

$$
[du_1 \ dv_1] \cdot (B - \lambda_2 G) \cdot [du_2 \ dv_2]^T = 0.
$$

Subtract one of the last two equations from the other and will yield the equation:

$$
[du_1 \ dv_1] \cdot ((\lambda_2 - \lambda_1) G) \cdot [du_2 \ dv_2]^T = 0,
$$

which implies that the principal directions are orthogonal at $\lambda_1 \neq \lambda_2$. If the principal curvatures of the surface are identical then any two orthogonal directions can be selected as the principals (this situation occurs on the sphere and on the plane). The point where $\lambda_2 = \lambda_1$ is called the umbilical point.

Since the principal directions are orthogonal in general, then the derivatives of the radius vector of the surface and its normals in any direction can be expanded into unit vectors $t_1$ and $t_2$ of the principal directions.
$$
\frac{dr}{ds} = t_1 \cos \varphi + t_2 \sin \varphi, \quad \frac{dm}{ds} = -\lambda_1 t_1 \cos \varphi - \lambda_2 t_2 \sin \varphi,
$$

where the angle $\varphi$ is measured from the first to the second principal direction in the tangent plane. Taking into account the last equations, the curvature of the normal section in an arbitrary direction is determined by the relation

$$
\mu = -\frac{dr}{ds} \cdot \frac{dm}{ds} = \lambda_1 \cos^2 \varphi + \lambda_2 \sin^2 \varphi. \tag{2.1.14}
$$

Formula (2.1.14) is called the Euler formula. It expresses the curvature of an arbitrary normal section at the point in terms of the principal curvatures and the angle between the normal section and the first principal direction. From this equation, it can be seen that the principal curvatures of the surface, $\lambda_1$ and $\lambda_2$, are the maximum and minimum curvatures, respectively.

The Gauss curvature of the surface (2.1.12) can be used to determine the surface behavior at an arbitrary point. Since the denominator in (2.1.12) is greater than zero, the sign of the Gauss curvature depends on the sign of the numerator—i.e., on the sign of the determinant of the matrix $B$. If $|B| > 0$, then the point is called elliptical. The behavior of the surface at the elliptical point is shown in Fig. 2.1.2. If $|B| < 0$, the point is called hyperbolic. The behavior of the surface at the hyperbolic point is shown in Fig. 2.1.3.

When we move from the considered point in any direction, the surface bends either in the direction of the normal or in the opposite direction, depending on the signs of $\lambda_1$ and $\lambda_2$. According to (2.1.14), there exist normal sections for which the following equation holds

$$
\mu_1 \cos^2 \varphi + \mu_2 \sin^2 \varphi = 0.
$$

Tangents to the normal sections at angles

$$
\varphi = \pm \arctg \left( \sqrt{\frac{\mu_1}{\mu_2}} \right)
$$

lie in the tangent plane symmetrically with respect to the principal directions, and determine asymptotic direction at the given point. If at the given point $|B| = 0$, then this
point is called parabolic. The behavior of the surface at the parabolic point is shown in Fig. 2.1.4.

Fig. 2.1.4.

When $\lambda_1 = \lambda_2 = 0$, each direction is asymptotic. Otherwise, the principal direction is the asymptotic direction with zero curvature. The corresponding normal section at such point has a rectifying point.

If for each point of the surface curve the tangent is parallel to one of the principal directions at this point of the surface, the surface curve is called the **curvature line**. The coordinate curves are often the curvature lines. Let $u$-lines and $v$-lines be curvature lines. In this case the following equalities hold at each point of the surface:

$$g_{12} = g_{21} = b_{12} = b_{21} = 0,$$

(2.1.15)

due to the orthogonality of the principal directions. The opposite proposition is also true: If at every point of the surface the equations (2.1.15) hold, then the coordinate curves are the curvature lines.

### 2.2. Analytic Surfaces

The surface is called an **analytic surface** if its coordinates in the local coordinate system can be described by analytic functions without using points, vectors, curves, or other surfaces.

Local coordinate systems are used for analytic surfaces in which the surfaces are expressed in canonical form. Construct a local Cartesian coordinate system with the origin at $p$ and basis vectors $i_x, i_y, i_z$. A surface with coordinates $x(u,v), y(u,v), z(u,v)$ in the local coordinate system is described by the vector function

$$r(u,v) = p + x(u,v) i_x + y(u,v) i_y + z(u,v) i_z.$$

(2.2.1)

Let $p_i$ be the coordinate of the origin $p$ of the local coordinate system, $x_i$ be the components of the basis vector $i_x$, $y_i$ be the components of the basis vector $i_y$, and $z_i$ be the components of the basis vector $i_z$, $i=1,2,3$. Then the analytic surface is the function

$$\begin{bmatrix}
r_1(u,v) \\
r_2(u,v) \\
r_3(u,v)
\end{bmatrix} = \begin{bmatrix}
p_1 \\
p_2 \\
p_3
\end{bmatrix} + \begin{bmatrix}
x_1 & y_1 & z_1 \\
x_2 & y_2 & z_2 \\
x_3 & y_3 & z_3
\end{bmatrix} \cdot \begin{bmatrix}
x(u,v) \\
y(u,v) \\
z(u,v)
\end{bmatrix}.$$
The coordinates of a point on the surface (2.2.1) equal

$$ r_i(u,v) = p_i + x(u,v) \cdot x_i + y(u,v) \cdot y_i + z(u,v) \cdot z_i. $$

Upon changing the position or orientation of an analytic surface described in this way, the coordinates of the origin of the local coordinate system and its basis vectors change, but the analytical functions of the surface remain unchanged, preserving the canonical form. Let us consider examples of analytic surfaces.

A conical surface is described by the vector function

$$ r(u,v) = p + (r + hv \tan \gamma)(\cos u \cdot i_x + \sin u \cdot i_y) + hv \cdot i_z, $$
$$ u \in [0, 2\pi], \quad v \in [v_{\min}, v_{\max}], $$

where $r$ — one of the base radii of the cone, $h$ — the cone length, $\gamma$ — the angle between the generator and the axis of the cone. We place the origin of the local coordinate system at the center of one of the cone bases and direct the basis vector $i_z$ along the axis of the surface. The cone surface is cyclic with respect to the first parameter and truncated with respect to the second parameter. A circular cone is shown in Fig. 2.2.1.

If the angle $\gamma$ is set equal to zero, we obtain a cylindrical surface.

![Fig. 2.2.1.](image)

We describe the surface of a torus by the vector function

$$ r(u,v) = p + (R + r \cos v) \cos u \cdot i_x + (R + r \cos v) \sin u \cdot i_y + r \sin v \cdot i_z, $$
$$ u \in [0, 2\pi], \quad v \in [v_{\min}, v_{\max}], $$

where $r$ is the radius of the torus tube, and $R$ is the radius of the tube axis. The origin of the local coordinate system is placed at the torus center, while the basis vector $i_z$ is directed along the torus axis; see Fig. 2.2.2. Scalar functions $x(u,v) = (R + r \cos v) \cos u,$
$$ y(u,v) = (R + r \cos v) \sin u, $$
$$ z(u,v) = r \sin v $$ are related by the equation

$$ \left( \sqrt{x^2 + y^2} - R \right)^2 + z^2 = r^2. $$

When $r \leq R$, the torus surface is cyclic closed with respect to both parameters and has the shape of a donut, then $v_{\min} = -\pi$ and $v_{\max} = \pi$. If $r > R$, then to prevent surface self-intersections we restrict the domain of the second parameter. We set $v_{\min} = -\pi + v_0,$
$$ v_{\text{max}} = \pi - v_0, \text{ where } v_0 = \arccos(R/r), \text{ if } -|r| < R < r. \text{ When } 0 < R < r, \text{ the torus surface has the shape of an apple; see Fig. 2.2.3.} $$

If $R = 0$ the torus surface becomes a sphere of radius $r$. If $-|r| < R < 0$ the torus surface has the shape of a lemon. If the tube axis radius does not exceed the tube radius, then the torus surface has singular points at $v = \pm (\pi - \arccos(R/r))$ because the derivative of the surface with respect to the first parameter vanishes at these points.

An ellipsoid is described by the vector function

$$
\mathbf{r}(u,v) = p + a \cos v \cos u \mathbf{i}_x + b \cos v \sin u \mathbf{i}_y + c \sin v \mathbf{i}_z,
$$

where $u \in [0, 2\pi]$, $v \in [-\pi/2, \pi/2]$,

where $a, b,$ and $c$ are semi-axes of the ellipsoid. Similar to the sphere, the ellipsoid is a cyclic surface with respect to the first parameter. The scalar functions $x(u,v) = a \cos v \cos u$, $y(u,v) = b \cos v \sin u$, and $z(u,v) = c \sin v$ of the ellipsoid are related by the equation

$$
\left( \frac{x}{a} \right)^2 + \left( \frac{y}{b} \right)^2 + \left( \frac{z}{c} \right)^2 = 1.
$$

A one-sheet hyperboloid is described by the vector function

$$
\mathbf{r}(u,v) = p + a \cosh v \cos u \mathbf{i}_x + b \cosh v \sin u \mathbf{i}_y + c \sinh v \mathbf{i}_z,
$$

where $u \in [0, 2\pi]$, $v \in [v_{\text{min}}, v_{\text{max}}]$,

where $a$ and $b$ are real semi-axes of the hyperboloid, and $c$ is its imaginary semi-axis. The real semi-axes are equal to the distances from the point $p$ to the points of intersection of the surface with the axes $i_x$ and $i_y$ of the local coordinate system. The one-sheet hyperboloid is a cyclic surface with respect to the first parameter. The scalar functions $x(u,v) = a \cosh v \cos u$, $y(u,v) = b \cosh v \sin u$, and $z(u,v) = c \sinh v$ of the hyperboloid are related by the equation

$$
\left( \frac{x}{a} \right)^2 + \left( \frac{y}{b} \right)^2 - \left( \frac{z}{c} \right)^2 = 1.
$$
We describe a **two-sheet hyperboloid** by the vector function

$$ r(u,v) = p + a \sinh u \cos v i_x + b \sinh u \sin v i_y + c \cosh v i_z, $$

where $u \in [0, 2\pi]$, $v \in [0, v_{\text{max}}]$,

where $a$ and $b$ are the imaginary semi-axes of the hyperboloid, and $c$ is its real semi-axis. The real semi-axis is equal to the distance from the point $p$ to the points of intersection of the surface with the axis $i_z$ of the local coordinate system. The two-sheet hyperboloid is a cyclic surface with respect to the first parameter. The scalar functions $x(u,v) = a \sinh u \cos v$, $y(u,v) = b \sinh u \sin v$, and $z(u,v) = c \cosh v$ of the hyperboloid are related by the equation

$$ \left( \frac{x}{a} \right)^2 + \left( \frac{y}{b} \right)^2 - \left( \frac{z}{c} \right)^2 = -1. $$

We describe an **elliptical paraboloid** by the vector function

$$ r(u,v) = p + a v \cos u i_x + b v \sin u i_y + v^2 i_z, $$

where $u \in [0, 2\pi]$, $v \in [0, v_{\text{max}}]$,

where $a$ and $b$ are the semi-axes of the paraboloid. An elliptical paraboloid is a cyclic surface with respect to the first parameter. The scalar functions $x(u,v) = a v \cos u$, $y(u,v) = b v \sin u$, and $z(u,v) = v^2$ of the paraboloid are related by the equation

$$ \left( \frac{x}{a} \right)^2 + \left( \frac{y}{b} \right)^2 = z. $$

We describe a **hyperbolic paraboloid** by the vector function

$$ r(u,v) = p + a u i_x + b v i_y + (u^2 - v^2) i_z, $$

where $u \in [u_{\text{min}}, u_{\text{max}}]$, $v \in [v_{\text{min}}, v_{\text{max}}]$,

where $a$ and $b$ are the semi-axes of the paraboloid. The scalar functions $x(u,v) = a u$, $y(u,v) = b v$, and $z(u,v) = u^2 - v^2$ of the hyperbolic paraboloid are related by the equation

$$ \left( \frac{x}{a} \right)^2 - \left( \frac{y}{b} \right)^2 = z. $$

The hyperbolic paraboloid is not a cyclic surface.
2.3. Surfaces Constructed by Curve Translation

A surface can be obtained by translating a curve along a given path. An arbitrary curve can serve as a path. The curve that is translated to generate the surface is called the generator curve, and the curve serving as a translation path is called the guide curve. Let a generator be described by the curve $c(u)$, $u_{\text{min}} \leq u \leq u_{\text{max}}$, and a guide curve be $g(v)$, $v_{\text{min}} \leq v \leq v_{\text{max}}$. Let the first parameter of the surface coincide with the parameter of the generator curve $c(u)$, and its second parameter with the parameter of the guide curve $g(v)$. The domain of the swept surface parameters is a rectangle. If the generator $c(u)$ is cyclic closed, then the swept surface is also cyclic closed with respect to the first parameter.

During the translation of the generator along the guide curve, the orientation of the generator in space may remain the same, or the same with respect to the guide curve. In the first case, the generator performs a plane-parallel translation; this surface is called an evolution surface. In the second case let us select the two simplest guide curves among all possible—a line segment and a circular arc. If the guide curve is a line segment then the surface is called an extrusion surface. If the guide curve is a circular arc or circle then the surface is called a revolution surface. In other cases the sliding surface is called a swept surface.

If the dot product of the tangent vectors at any two points of a curve is always greater than zero, the curve is called monotonic. A monotonic curve cannot be closed. Examples of monotonic curves are a segment, a helix, and some other curves.

An evolution surface obtained by translation of the curve $c(u)$, $u_{\text{min}} \leq u \leq u_{\text{max}}$, along the monotonic guide curve $g(v)$, is described by the vector function

$$
r(u,v) = g(v) + c(u) - g(v_{\text{min}}).
$$

(2.3.1)

The radius vector of the evolution surface is constructed as a sum of two vectors: the vector of a point on the guide curve $g(v)$ and the vector of the generator point location relative to the starting point of the guide curve $c(u) - g(v_{\text{min}})$. An evolution surface is shown in Fig. 2.3.1.

Fig. 2.3.1.
The **extrusion surface** obtained by translation of the curve $c(u)$, $u_{\text{min}} \leq u \leq u_{\text{max}}$, along the vector $d$, is described by the vector function

$$r(u,v) = c(u) + v d.$$

(2.3.2)

An extrusion surface is shown in Fig. 2.3.2.

![Fig. 2.3.2.](image)

Let us construct a **revolution surface** using the local rectangular Cartesian coordinate system associated with the rotation axis. Locate the origin $p$ on the rotation axis and direct the third basis vector $i_3$ of the local coordinate system along the rotation axis. Direct the first basis vector $i_1$ of the local coordinate system toward the generator. To do this, we construct the vector $d = c(u_1) - p$ and subtract its component parallel to the rotation axis from $d$: $d_1 = d - (i_3 \cdot d)i_3$. The point $c(u_1)$ might be any point of the guide curve that doesn’t lie on the rotation axis. We direct the basis vector $i_1$ along $d_1$

$$i_1 = \frac{d_1}{|d_1|}.$$

Direct the basis vector $i_2$ of the local coordinate system parallel to the vector $i_2 = i_3 \times i_1$. To calculate the radius vector of the point of the revolution surface let us construct the matrix

$$A = [i_1 \ i_2 \ i_3],$$

whose columns contain the components of the basis vectors of the local coordinate system. The matrix $A$ is the coordinate transformation matrix of the radius vector of the point from the local coordinate system to the global coordinate system.

The surface obtained by rotating the curve $c(u)$, $u_{\text{min}} \leq u \leq u_{\text{max}}$, by angle $\alpha$ about the axis defined by the vector $i_3$ and the point $p$, is described by the vector function

$$r(u,v) = p + M(v) \cdot (c(u) - p),$$

(2.3.3)

$$u \in [u_{\text{min}}, u_{\text{max}}], \quad v \in [0, \alpha].$$
where $M(v) = A \cdot \begin{bmatrix} \cos(v) & -\sin(v) & 0 \\ \sin(v) & \cos(v) & 0 \\ 0 & 0 & 1 \end{bmatrix} \cdot A^{-1}$ is the rotation matrix. The matrix $M(v)$ transforms the vector $c(u) - p$ to the local coordinate system, rotates it by angle $v$ about the rotation axis, and transforms the rotated vector back into the global coordinate system. If the rotation angle $\alpha = 2\pi$, then the surface (2.3.3) is cyclic closed with respect to the second parameter. The revolution surface is shown in Fig. 2.3.3.

Let us construct a swept surface using a moving rectangular Cartesian coordinate system associated with a guide curve $g(v)$. Place its origin $p_0$ at the current point of the guide curve. Direct the first basis vector $i_1 = g'/|g'|$ of the moving coordinate system along a tangent to the guide curve. Construct the second basis vector $i_2$ orthogonal to the first one and let the third basis vector $i_3 = i_1 \times i_2$ together with the first and second one form the right-handed triad. Direct the basis vector $i_2$ parallel to the vector

$$
d_2(v) = d - (i_1 \cdot d) i_1,
$$

(2.3.4)

where $d$ is some vector not parallel to the tangent to the guide curve $g(v)$ at any of its points. The vector $d_2(v)$ is the component of the vector $d$ perpendicular to the vector $i_1$. Since we assume that vector $d$ is never parallel to vector $i_1$, vector $d_2(v)$ is never equal to zero. We assume that for the guide curve there is a vector $d$ never parallel to the tangent to the curve. The moving coordinate system is a function of the parameter $v$ of the guide curve

$$
p_0(v) = g(v),
$$

$$
i_1(v) = \frac{g'}{|g'|}, \quad i_2(v) = \frac{d_2}{|d_2|}, \quad i_3(v) = i_1 \times i_2,
$$

(2.3.5)

where $d_2$ is determined by the equation (2.3.4), and $g' = \frac{dg}{dv}$.

To calculate a radius vector of a point on the swept surface construct the matrix
$$ A(v) = \begin{bmatrix} i_1(v) & i_2(v) & i_3(v) \end{bmatrix}, $$
(2.3.6)

whose columns contain the components of the moving coordinate system basis vectors. The matrix $A(v)$ is the coordinate transformation matrix of the radius vector for a point from the moving coordinate system to the global coordinate system, and it is a function of the parameter of the guide curve.

Let us remember the position of the generator $c(u)$ in the moving tangent basis at the beginning of the guide curve and keep it during the translation along the guide curve. The radius vector of a point of the generator in the moving coordinate system for $v = v_{\text{min}}$ is

$$ x(u, v_{\text{min}}) = A^{-1}(v_{\text{min}}) \cdot (c(u) - g(v_{\text{min}})), $$

where $A^{-1}(v_{\text{min}})$ is the coordinate transformation matrix of the radius vector of the point from the global coordinate system to the moving coordinate system, calculated at the start point of the guide curve. During the translation along the guide curve the moving tangent basis changes its location and orientation in the space and drags along the generator rigidly bound to it. The vector $x(u, v_{\text{min}})$ describes the location of the generator's point relative to the point on the guide curve in the moving tangent basis. The location remains the same for an arbitrary parameter $v$. During the transition from the moving coordinate system to the global coordinate system for the current parameter $v$, we obtain the radius vector of the point on the swept surface

$$ r(u, v) = g(v) + A(v) \cdot x(u, v_{\text{min}}), $$

Thus, the radius vector of the swept surface is described by the vector function

$$ r(u, v) = g(v) + M(v) \cdot (c(u) - g(v_{\text{min}})), $$
(2.3.7)

where $M(v)$ is the rotation matrix of the current moving basis with respect to its initial position. This matrix is calculated by the formula

$$ M(v) = A(v) \cdot A^{-1}(v_{\text{min}}). $$
(2.3.8)

The matrix $M(v_{\text{min}})$ is equal to the identity matrix at the beginning of the guide curve.

To calculate the derivatives of the radius vector of the swept surface we calculate the derivatives of the matrix $M(v)$, which in turn reduces to calculation of the derivatives of the basis vectors $i_1(v), i_2(v), i_3(v)$. For example,

$$ \frac{d}{dv} i_1 = \frac{g'}{|g'|} - \left( i_1 \cdot \frac{g''}{|g'|} \right) i_1, $$

$$ \frac{d^2}{dv^2} i_1 = \frac{g'''}{|g'|} - 2 \left( i_1 \cdot \frac{g''}{|g'|} \right) \frac{d}{dv} i_1 - \left( i_1 \cdot \frac{g'''}{|g'|} + \frac{d}{dv} \left( i_1 \cdot \frac{g''}{|g'|} \right) \right) i_1. $$
(2.3.9)
From (2.3.9) it follows that for calculation of the second-order partial derivatives of the radius vector of the swept surface, the third-order derivatives of the radius vector of the guide curve are required.

The closeness of the swept surface with respect to the parameter $u$ is the same as the closeness of the guide $c(u)$, and the closeness of the surface with respect to parameter $v$ is the same as the closeness of the guide curve $g(v)$. The swept surface is shown in Fig. 2.3.4.

An evolution surface and a swept surface may intersect themselves if there is an unfavorable combination of their generator and guide curves.

In the general case, most surfaces can be represented in the form of a swept surface if during the motion the generator and the guide curve are able to change. Fig. 2.3.5 shows an extrusion surface. The planar generator of this surface becomes three times as small along the smaller transverse dimension and rotates by forty-five degrees during the motion. The reduction of the smallest transverse dimension of the generator depends linearly on the increase of the second parameter of the surface. The rotation of the generator is sinusoidal function of the second parameter of the surface. Fig. 2.3.6 shows a revolution surface with the distance between a non-planar generator from the axis varying as a truncated epicycloid during the rotation.