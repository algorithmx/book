More complex surfaces can be obtained, if the variation of the generator is set to depend on the second parameter of the surface and the variation of the guide curve is set to depend on the first parameter of the surface during the motion.

2.4. Surfaces Constructed on a Set of Curves

Consider the construction of surfaces on a set of curves \( c_i(u) \) that do not intersect with each other, \( i=0,1,...,n \). By changing the parameterization (1.15.4) we bring all the curves to the one parametric length so that the parametric domain of each curve is in the range of \( u_{\text{min}} \) to \( u_{\text{max}} \). The set of non-intersecting curves having the same parametric length is called a set of curves. Let the first parameter of the surface \( r(u,v) \) coincide with the common parameter of the curves. Choose the ascending sequence of values \( v_i \) for the second parameter of the surface and assign it to the set of curves \( c_i(u) \), \( i=0,1,...,n \). If all curves of the set are cyclic closed, then the surface under construction is cyclic closed with respect to the first parameter.

A ruled surface is constructed on a set of two curves and it is the locus of line segments joining the corresponding points of curves of the set. Suppose we are given two curves \( c_0(u) \) and \( c_1(u) \). Describe the ruled surface by the vector function

$$
r(u,v) = (1-v) c_0(u) + v c_1(u).
$$  

(2.4.1)

Fig. 2.4.1 shows the ruled surface.

![Diagram](image)

Fig. 2.4.1.

A sector surface is a special case of the ruled surface. It can be obtained from the ruled surface (2.4.1) by replacing one of the curves—for example, \( c_1(u) \)—by the point \( p \). The radius vector of the sector surface is described by the formula

$$
r(u,v) = (1-v) c_0(u) + v p, \quad v \leq 1.
$$
If the curve $c_0(u)$ is cyclic closed, then the sector surface is also cyclic closed with respect to the first parameter. When $v=1$, the points of the surface are singular points, because the partial derivatives with respect to the first parameter of the radius vector of the surface at these points are equal to zero.

Construct a surface on the set of curves $c_i(t), i=0,1,...,n$ in a way similar to the construction of a Lagrange curve (1.3.2) on a set of points. Choose the ascending sequence of the second parameter values $v_i$ in which the surface $r(u,v)$ must coincide with curves $c_i(u)$. Note that the shape of the surface depends on the values $v_i, i=0,1,...,n$. Let us represent the Lagrange surface constructed on the set of curves $c_i(u), i=0,1,2,...,n$ by the vector function

$$r(u,v) = \sum_{i=0}^{n} L_i^n(v)c_i(u),$$

(2.4.2)

where $L_i^n(v)$ are the Lagrange coefficients (1.3.3). Each $v$-line $r(\text{const},v)$ of such a surface is a Lagrange curve.

Suppose that besides curves $c_i(u)$, we also know the partial derivatives of the surface with respect to the second parameter $r_v(u,v_i)=\frac{\partial r(u,v)}{\partial v}\bigg|_{v=v_i}$ on the coordinate lines along the selected values of the second parameter $v=v_i, i=0,1,2,...,n$. Represent the lofted surface constructed on the set of curves by the vector function

$$r(u,v) = (1 - 3w^2 + 2w^3)c_i(u) + (3w^2 - 2w^3)c_{i+1}(u) +$$
$$+ (w - 2w^2 + w^3)(v_{i+1} - v_i)r_v(u,v_i) + (-w^2 + w^3)(v_{i+1} - v_i)r_v(u,v_{i+1}) =$$

$$=[\alpha_0(w) \quad \alpha_1(w) \quad \beta_0(w) \quad \beta_1(w)] \cdot \begin{bmatrix}
c_i(u) \\
c_{i+1}(u) \\
r_v(u,v_i)(v_{i+1} - v_i) \\
r_v(u,v_{i+1})(v_{i+1} - v_i)
\end{bmatrix},$$

(2.4.3)

where $w = w(v) = \frac{v - v_i}{v_{i+1} - v_i}$ is a local surface parameter, and the index $i$ is found from the condition $v_i \leq v \leq v_{i+1}$. The lofted surface is constructed in a way similar to the construction of the composite Hermite spline (1.3.10), and is cubic in the $v$ direction. As the parameter $w$ varies from 0 to 1, the surface parameter varies from $v_i$ to $v_{i+1}$.

If the derivatives $r_v(u,v_i)$ of the set are unknown, they can be found from the adjacent curves analogous to calculating the derivatives at the control points of a composite Hermite spline; for example,

$$r_v(u,v_i) = c_{i-1}(u)\frac{v_i - v_{i+1}}{(v_{i-1} - v_i)(v_{i-1} - v_{i+1})} + c_i(u)\frac{2v_i - v_{i-1} - v_{i+1}}{(v_i - v_{i-1})(v_i - v_{i+1})} + c_{i+1}(u)\frac{v_i - v_{i-1}}{(v_{i+1} - v_{i-1})(v_{i+1} - v_i)}$$

for the inner curves ($i=1,2,...,n-1$), and
$$ r_v(u, v_0) = \frac{3}{2} \frac{c_1(u) - c_0(u)}{v_1 - v_0} - \frac{1}{2} r_v(u, v_1), $$
$$ r_v(u, v_n) = \frac{3}{2} \frac{c_n(u) - c_{n-1}(u)}{v_n - v_{n-1}} - \frac{1}{2} r_v(u, v_{n-1}) $$

for the outer curves \( i=0, i=n \). The calculation formulas \( r_v(u, v_0) \) and \( r_v(u, v_n) \) yield zero second derivatives on the outer curves of the surface in the directions perpendicular to the edge of the surface. If all the curves of the set are cyclic closed then the surface (2.4.2) is cyclic closed with respect to the first parameter. The surface can also be cyclic closed with respect to the second parameter. The lofted surface constructed on the set of curves is shown in Fig. 2.4.2.

![Fig. 2.4.2.](image)

In special cases, a surface (2.4.3) can serve as a transition bridge from one surface to another. The conjugate surfaces must have rectangular parametric domains. Suppose, for example, it is required to smoothly conjugate the edge of the surface \( a(u, v_{\text{max}}) \) with the edge of the surface \( b(u, v_{\text{min}}) \). Let us represent the bridge surface by the vector function

$$ r(u, w) = a(u, v_{\text{max}}) (1 - 3w^2 + 2w^3) + $$
$$ + b(u, v_{\text{min}}) (3w^2 - 2w^3) + $$
$$ + a_v(u, v_{\text{max}}) (w - 2w^2 + w^3) k_a + $$
$$ + b_v(u, v_{\text{min}}) (-w^2 + w^3) k_b, \quad (2.4.4) $$
$$ u_{\text{min}} \leq t \leq u_{\text{max}}, \quad 0 \leq w \leq 1, $$

where \( a_v(u, v_{\text{max}}) = \left. \frac{\partial a(u, v)}{\partial v} \right|_{v=v_{\text{max}}} \) is the partial derivative with respect to the fixed parameter of the radius vector of the first conjunct surface,

$$ b_v(u, v_{\text{min}}) = \left. \frac{\partial b(u, v)}{\partial v} \right|_{v=v_{\text{min}}} $$ 

is the partial derivative with respect to the fixed parameter of the radius vector of the second conjunct surface, are \( k_a \) and \( k_b \) are coefficients normalizing derivatives \( a_v(u, v_{\text{max}}) \) and \( b_v(u, v_{\text{min}}) \) respectively. Coefficients \( k_a \) and \( k_b \) are obtained by dividing the average distance between the edges of the conjunct surfaces
by the average length of the partial derivatives \(a_v(u,v_{\text{max}})\) and \(b_v(u,v_{\text{min}})\). The bridge surface is shown in Fig. 2.4.3.

![Fig. 2.4.3.](image)

Construct a surface on the set of curves similarly to how you construct Bezier curves on a set of points. To do this, substitute the curves of the set in (1.6.2) for the control points. A **Bezier surface constructed on the set of curves** \(c_i(u), i=0,1,...,n\) is described by the vector function

$$
r(u,v) = \frac{\sum_{i=0}^{n} B^n_i(v) w_i(u) c_i(u)}{\sum_{i=0}^{n} B^n_i(v) w_i(u)},
$$

(2.4.5)

where \(B^n_i(v)\) are Bernstein functions (1.4.2). In general, each curve \(c_i(u)\) of the set has its own weight \(w_i(u)\), which is a scalar function of the parameter of the corresponding curve. Each line of the surface at \(u=\text{const}\) is a rational Bezier curve. In the particular case where all curves of the set have similar weights not depending on the parameter, the radius vector of the Bezier surface on the set of curves is calculated by the formula

$$
r(u,v) = \sum_{i=0}^{n} B^n_i(v) c_i(u).
$$

(2.4.6)

Unlike other surfaces constructed on the set of curves, the surface (2.4.5) does not pass through the curves of the set.

Let us construct a surface on the set of curves in a way similar to the way in which we construct a B-spline curve on a set of points. To do this, substitute the curves of the set for the control points in (1.9.1). A **B-spline surface constructed on a set of curves** \(c_i(u), i=0,1,...,n\), is described by the vector function

$$
r(u,v) = \frac{\sum_{j=0}^{n} N_j^m(v) w_j(u) c_j(u)}{\sum_{j=0}^{n} N_j^m(v) w_j(u)},
$$

(2.4.7)
where $N_j^m(v)$ are B-splines (1.8.1) of the $m$-th order, and $w_i(u)$ is the weight function of the set curve $c_i(u)$. Each B-spline $N_j^m(v)$ is constructed on a non-decreasing sequence of $m+2$ knots $v_j, v_{j+1}, \ldots, v_{j+m+1}$.

To construct the set of $n+1$ B-splines of the $m$-th order open with respect to the second parameter of the B-spline curve, $n+m+2$ knots $v_j$, $i=0,1,\ldots,n+m+1$ are required. To construct the set of $n+1$ B-splines of the $m$-th order cyclic closed with respect to the second parameter of the B-spline curve, $n+2m+2$ knots $v_j$, $i=0,1,\ldots,n+2m+1$ are required. A sequence of knots of the second parameter of the surface is constructed similarly to the sequence of knots of a B-spline curve (1.9.1). The second parameter of the B-spline surface ranges from the knot value $v_{\text{min}} = v_m$ to the knot value $v_{\text{max}} = v_{n+m+1}$.

Each line $u=\text{const}$ on the surface (2.4.7) is a B-spline curve (1.9.1). Fig. 2.4.4 shows the B-spline surface and the set of the curves used to construct the surface.

In the particular case when all curves of the set have equal weights independent of the parameter, the radius vector of the B-spline surface on the set of curves is calculated by the formula

$$r(u,v) = \sum_{j=0}^{n} N_j^m(v)c_j(u). \quad (2.4.8)$$

The B-spline surface constructed on a set of curves does not pass through the set of curves.

Suppose we are given a set of curves $c_i(u), i=0,1,\ldots,n$, a guide curve $g(v)$, and an ascending sequence of parametric values of the guide curve $v_i$ conformal to the set of curves. Construct the surface $r(u,v)$ passing through the set of curves, taking into account the behavior of the guide curve. Let the second parameter range between $v_i$ and $v_{i+1}$ and let the surface be the weighted sum of the swept surfaces constructed on the guide curve $g(v)$ with generators $c_i(u)$ and $c_{i+1}(u)$. In accordance with (2.3.7), the radius vector of the swept surface constructed on the generator $c_i(u)$ is calculated by the formula

$$r_i(u,v) = g(v) + M_i(v) \cdot (c_i(u) - g(v)).$$

In accordance with (2.3.8), let us calculate the rotation matrix $M_i(v)$ of the current moving basis relative to its initial position using the formula
$$ M_i(v) = A(v) \cdot A^{-1}(v_i). $$

A lofted surface constructed on the set of curves \( c_i(u), \ i=0,1,...,n \) with the guide curve \( g(v) \) is described by the vector function

$$
r(u,v) = r_i(u,v) (1-3w^2+2w^3) + r_{i+1}(u,v) (3w^2-2w^3),
$$

where the index \( i \) is determined by the condition \( v_i \leq v \leq v_{i+1} \), and \( w = \frac{v - v_i}{v_{i+1} - v_i} \) is a local parameter. Fig. 2.4.5 shows a surface on a set of three curves and a guide curve.

![Fig. 2.4.5.](image)

### 2.5. Surfaces Constructed on a Mesh of Curves

Suppose there are two families of curves: the set of curves \( c_i(u), \ i=0,1,2,...,n, \ u_{\text{min}} \leq u \leq u_{\text{max}}, \) and the set of curves \( b_j(v), \ j=0,1,2,...,m, \ v_{\text{min}} \leq v \leq v_{\text{max}}; \) see Fig. 2.5.1. Let each curve \( c_i(u) \) of the first set intersect at \( u=u_j, \ j=0,1,2,...,m \) with each curve \( b_j(v) \) of the second set at \( v=v_i, \ i=0,1,2,...,n. \) Let the parameters of the intersection points of the curves form ascending sequences: \( u_j < u_{j+1} \) and \( v_i < v_{i+1}. \) We call the two families of curves satisfying the above requirements a mesh of the curves.

![Fig. 2.5.1.](image)
The simplest mesh of the curves is two pairs of segments constructed on four common points \( p_{00}, p_{10}, p_{01}, p_{11} \). Let the first set form the segments \( c_0(u) = p_{00}(1-u) + p_{10}u \) and \( c_1(u) = p_{01}(1-u) + p_{11}u \), and let the second set form the segments \( b_0(v) = p_{00}(1-v) + p_{01}v \) and \( b_1(v) = p_{10}(1-v) + p_{11}v \). A bilinear surface constructed on this mesh of the curves is determined by the vector function

$$
r(u,v) = (1-u)(1-v) p_{00} + u(1-v) p_{10} + (1-u)v p_{01} + uv p_{11}.
$$  

(2.5.1)

The bilinear surface is shown in Fig. 2.5.2.

Surface (2.5.1) is a special case of the ruled surface (2.4.1) constructed on the two segments \( c_0(u) \) and \( c_1(u) \). A bilinear surface is a ruled surface with respect to two parameters.

To construct a bilinear surface it is sufficient to know the radius vectors of the points \( p_{00}, p_{10}, p_{01}, \) and \( p_{11} \). If the points \( p_{00} \) and \( p_{01} \) or \( p_{10} \) and \( p_{11} \) coincide, then we obtain a triangular surface with a singular point.

Construct a ruled surface (2.4.1) with reduction of the curves \( c_0(u) \) and \( c_1(u) \) to the parametric length \( 0 \leq u \leq 1 \). Let us add and subtract the vector function of the bilinear surface (2.5.1) from the vector function of this ruled surface. \( p_{00} \) and \( p_{10} \) are the initial and end points of the curve \( c_0(u) \), and \( p_{01} \) and \( p_{11} \) – the initial and the end points of the curve \( c_1(u) \) of the ruled surface. After these manipulations the vector function does not change but takes the form

$$
r(u,v) = (1-v) c_0(u) + v c_1(u) +
+ (1-u) (p_{00}(1-v) + p_{01}v) + u (p_{10}(1-v) + p_{11}v) -
- (1-u)(1-v) p_{00} - u(1-v) p_{10} - (1-u)v p_{01} - uv p_{11}.
$$  

(2.5.2)

In (2.5.2) we introduced notation for the segments joining the ends of the curves \( c_0(u) \) and \( c_1(u) \): \( b_0(v) = p_{00}(1-v) + p_{01}v \) and \( b_1(v) = p_{10}(1-v) + p_{11}v \). If we use arbitrary curves starting and ending at the same points as \( b_0(v) \) and \( b_1(v) \), then we obtain the Coons surface. The radius vector of the Coons surface constructed on four curves, \( c_0(u) \), \( c_1(u) \), \( b_0(v) \), and \( b_1(v) \), is described by the function
$$ r(u,v) = (1-v)c_0(u) + v c_1(u) + (1-u)b_0(v) + u b_1(v) - $$
$$ -(1-u)(1-v)p_{00} - u(1-v)p_{10} - (1-u)v p_{01} - uv p_{11}. $$ (2.5.3)

A Coons surface is shown in Fig. 2.5.3.

Let us construct a Coons surface on four arcs of one ellipse as an example:

$$ r(u,v) = p + $$
$$ + a\left(1-u-v-(1-v)\cos\frac{\pi u}{2} + v\sin\frac{\pi u}{2} - (1-u)\cos\frac{\pi v}{2} + u\sin\frac{\pi v}{2}\right)i_1 + $$
$$ + b\left(u-v-(1-v)\sin\frac{\pi u}{2} + v\cos\frac{\pi u}{2} + (1-u)\sin\frac{\pi v}{2} - u\cos\frac{\pi v}{2}\right)i_2, $$

where \( p \) – radius vector of the center, \( a \) and \( b \) – semi-axes of the ellipse, and \( i_1, i_2 \) – basis vectors lying in the plane of the ellipse; see Fig. 2.5.4.

The partial derivatives of the radius vector of the surface with respect to parameters \( u \) and \( v \) are parallel at the junction points of the ellipse arcs.

We introduce the notation:

$$ s(u,0) = c_0(u), \quad s(u,1) = c_1(u), \quad s(0,v) = b_0(v), \quad s(1,v) = b_1(v), $$
$$ s(0,0) = p_{00}, \quad s(1,0) = p_{10}, \quad s(0,1) = p_{01}, \quad s(1,1) = p_{11}, $$
$$ \mu_0(w) = 1-w, \quad \mu_1(i) = w, $$

As a result the vector function (2.5.3) takes the form

$$
r(u,v) = \begin{bmatrix} \mu_0(u) & \mu_1(u) \end{bmatrix} \cdot \begin{bmatrix} s(0,v) \\ s(1,v) \end{bmatrix} + \begin{bmatrix} \mu_0(v) & \mu_1(v) \end{bmatrix} \cdot \begin{bmatrix} s(u,0) \\ s(u,1) \end{bmatrix} - \\
- \begin{bmatrix} \mu_0(u) & \mu_1(u) \end{bmatrix} \cdot \begin{bmatrix} s(0,0) & s(0,1) \\ s(1,0) & s(1,1) \end{bmatrix} \cdot \begin{bmatrix} \mu_0(v) \\ \mu_1(v) \end{bmatrix}.
$$  

(2.5.4)

Surface (2.5.4) is constructed on four curves whose coefficients are linear functions. Such a linear unification of four curves is called a **linear Coons surface**. The functions \( \mu_0(w) \) and \( \mu_1(w) \) are called **displacement functions**. In general, Coons surface curves may not intersect and points \( p_{00}, p_{10}, p_{01}, p_{11} \) might be arbitrary points.

A composite surface can be constructed from surfaces (2.5.4) by a boundary curve junction; i.e., making the boundary curves common to both surfaces. To ensure that the derivative perpendicular to the boundary does not lose continuity at the surface junction, we add the derivatives perpendicular to the boundary direction to the description of the surface. This means we add the partial derivatives of the surface along the boundary curves \( s_u(i,v), s_v(u,j) \) and the partial derivatives at the surface corners \( s_u(i,j), s_v(i,j), s_{uv}(i,j) \), where \( i=0,1 \) and \( j=0,1 \), to the description of the surface. Substitute the linear displacement functions by the cubic displacement functions

$$ \alpha_0(w) = 1-3w^2+2w^3, \quad \alpha_1(w) = 3w^2-2w^3, \quad \beta_0(w) = w-2w^2+w^3, \quad \beta_1(w) = -w^2+w^3. $$

The radius vector of the surface constructed this way is described by the vector functions

$$
r(u,v) =
\begin{bmatrix} \alpha_0(u) & \alpha_1(u) & \beta_0(u) & \beta_1(u) \end{bmatrix} \cdot \begin{bmatrix} s(0,v) \\ s(1,v) \\ s_u(0,v) \\ s_u(1,v) \end{bmatrix} + \begin{bmatrix} \alpha_0(v) & \alpha_1(v) & \beta_0(v) & \beta_1(v) \end{bmatrix} \cdot \begin{bmatrix} s(u,0) \\ s(u,1) \\ s_v(u,0) \\ s_v(u,1) \end{bmatrix} - \\
- \begin{bmatrix} \alpha_0(u) & \alpha_1(u) & \beta_0(u) & \beta_1(u) \end{bmatrix} \cdot \begin{bmatrix} s(0,0) & s(0,1) & s_u(0,0) & s_u(0,1) \\ s(1,0) & s(1,1) & s_u(1,0) & s_u(1,1) \\ s_{uv}(0,0) & s_{uv}(0,1) & s_{uv}(1,0) & s_{uv}(1,1) \end{bmatrix} \cdot \begin{bmatrix} \alpha_0(v) \\ \alpha_1(v) \\ \beta_0(v) \\ \beta_1(v) \end{bmatrix}.
$$  

(2.5.5)

The surface (2.5.5) is called a **cubic Coons surface**.

A.R. Forrest has suggested generalizing surfaces (2.5.4) and (2.5.5) and using **generalized displacement functions** \( \alpha_i^k(u) \) instead of linear or cubic displacement...
functions. Index $k$ indicates that the generalized displacement function is multiplied by the vector function, which is a derivative of $k$-th order of the boundary curve. The order-zero derivative of the function is referred to as the function itself. In terms of the generalized displacement function, $\alpha_i(u) = \alpha^0_i(u)$, $\beta_j(u) = \alpha^1_j(u)$, and $i=0,1$. The generalized displacement functions must satisfy the equalities

$$\frac{d^n \alpha_i^k}{du^n} \bigg|_{u=j} = \delta_i^j \delta_n^k = \begin{cases} 1, & \text{if } i = j \text{ and } k = n \\ 0, & \text{if } i \neq j \text{ or } k \neq n \end{cases}.$$  

A **generalized Coons surface** is described by the vector function

$$r(u,v) = \sum_{i=0}^{n} \sum_{k=0}^{m} \alpha_i^k(u)s_u^{(k)}(i,v) + \sum_{j=0}^{m} \sum_{l=0}^{n} \alpha_j^l(v)s_v^{(l)}(u,j) - \sum_{i=0}^{n} \sum_{k=0}^{m} \sum_{l=0}^{n} \alpha_i^k(u)\alpha_j^l(v)s_{uv}^{(kl)}(i,j),$$

where $u \in [0,1]$, $v \in [0,1]$, and the given values for the derivatives at the edges of the surfaces

$$s_u^{(k)}(i,v) = \left. \frac{\partial^k r(u,v)}{\partial u^k} \right|_{u=i}, \quad i = 0,1,$$

$$s_v^{(l)}(u,j) = \left. \frac{\partial^l r(u,v)}{\partial v^l} \right|_{v=j}, \quad j = 0,1,$$

and the given values of the derivatives at the corners of the parametric area of the surface are used

$$s_{uv}^{(kl)}(i,j) = \left. \frac{\partial^{kl} r(u,v)}{\partial u^k \partial v^l} \right|_{u=i, v=j}, \quad i,j = 0,1.$$

We can use polynomials as the generalized displacement functions.

A **Gordon surface** constructed on the mesh of curves formed by the set $c_i(u)$, $i=0,1,2,...,n$, $u_0 \leq u \leq u_m$ and by the set $b_j(v)$, $j=0,1,2,...,m$, $v_0 \leq v \leq v_m$, is described by the vector function

$$r(u,v) = \sum_{i=0}^{n} L_i^n(v)c_i(u) + \sum_{j=0}^{m} L_j^m(u)b_j(v) - \sum_{j=0}^{m} \sum_{i=0}^{n} L_j^m(u)L_i^n(v)p_{ji}, \quad (2.5.6)$$

where $L_i^n(v)$ and $L_j^m(u)$ are Lagrange coefficients (1.3.3), and $p_{ji}$ are the intersection points of the curves: $p_{ji} = c_i(u_j) = b_j(v_i)$. A Gordon surface is shown in Fig. 2.5.5.
If all the curves of the set are cyclic closed, the surface (2.5.6) will be cyclic closed in the corresponding direction.

Other splines can be used instead of functions $L_i^n(v)$ and $L_j^m(u)$. Let us describe the surface of type (2.5.6) using the lofted surface (2.4.3) construction principle as an example. Find the index $j$ from the condition $u_{j+1} \leq u \leq u_j$ and index $i$ from the condition $v_{i+1} \leq v \leq v_i$ for the parameters $u$ and $v$ of the surface. The Coons patch surface located between the curves $c_i(u), c_{i+1}(u), b_j(v), b_{j+1}(v)$ is described by the vector function

$$ r(u, v) = F_i^T \begin{bmatrix} c_i(u) \\ c_{i+1}(u) \\ s_v(u, v_i) \\ s_v(u, v_{i+1}) \end{bmatrix} + F_j^T \begin{bmatrix} b_j(v) \\ b_{j+1}(v) \\ s_u(u_j, v) \\ s_u(u_{j+1}, v) \end{bmatrix} - F_j^T \begin{bmatrix} p_{ji} & p_{ji+1} & s_v(u_j, v_i) & s_v(u_j, v_{i+1}) \\ p_{j+1i} & p_{j+1i+1} & s_v(u_{j+1}, v_i) & s_v(u_{j+1}, v_{i+1}) \\ s_u(u_j, v_i) & s_u(u_j, v_{i+1}) & s_{uv}(u_j, v_i) & s_{uv}(u_j, v_{i+1}) \\ s_u(u_{j+1}, v_i) & s_u(u_{j+1}, v_{i+1}) & s_{uv}(u_{j+1}, v_i) & s_{uv}(u_{j+1}, v_{i+1}) \end{bmatrix} F_i, $$

where

$$ F_i = \begin{bmatrix} \alpha_0(w) \\ \alpha_1(w) \\ (v_{i+1} - v_i)\beta_0(w) \\ (v_{i+1} - v_i)\beta_1(w) \end{bmatrix}, \quad F_j = \begin{bmatrix} \alpha_0(t) \\ \alpha_1(t) \\ (u_{j+1} - u_j)\beta_0(t) \\ (u_{j+1} - u_j)\beta_1(t) \end{bmatrix} $$

are column-matrices,

$$ t = \frac{u - u_j}{u_{j-1} - u_j}, \quad w = \frac{v - v_i}{v_{i-1} - v_i} $$

local parameters of the surface varying from 0 to 1,

$p_{ji} = c_i(u_j) = b_j(v_i)$ – points of curves intersection, $s_u(u, v)$ – partial derivative of the radius vector of the surface with respect to the first parameter, $s_v(u, v)$ – partial derivative of
the radius vector of the surface with respect to the second parameter, \( s_{uv}(u,v) \) – mixed derivative of the radius vector of the surface with respect to the first and second parameters. Let us calculate the derivatives of the surface \( s_u(u,v) \), \( s_v(u,v) \) and \( s_{uv}(u,v) \) on the mesh curves from adjacent curves the same way the derivatives of the composite Hermite spline (1.3.10) at reference points are calculated using adjacent points

$$
s_u(u_j, v) = b_{j-1}(v) \frac{u_j - u_{j+1}}{(u_{j-1} - u_j)(u_{j-1} - u_{j+1})} + b_j(v) \frac{2u_j - u_{j-1} - u_{j+1}}{(u_{j-1} - u_j)(u_j - u_{j+1})} + b_{j+1}(v) \frac{u_j - u_{j-1}}{(u_{j+1} - u_j)(u_{j+1} - u_j)},
$$

$$
s_v(u, v_i) = c_{i-1}(u) \frac{v_i - v_{i+1}}{(v_{i-1} - v_i)(v_{i-1} - v_{i+1})} + c_i(u) \frac{2v_i - v_{i-1} - v_{i+1}}{(v_{i-1} - v_i)(v_i - v_{i+1})} + c_{i+1}(u) \frac{v_i - v_{i-1}}{(v_{i+1} - v_i)(v_{i+1} - v_i)}
$$

for the inner curves \((j=1,2,...,m-1, i=1,2,...,n-1)\) and

$$
s_u(u_0, v) = \frac{3}{2} \frac{b_1(v) - b_0(v)}{u_1 - u_0} - \frac{1}{2} s_u(u_1, v),
$$

$$
s_u(u_m, v) = \frac{3}{2} \frac{b_m(v) - b_{m-1}(v)}{u_m - u_{m-1}} - \frac{1}{2} s_u(u_{m-1}, v),
$$

$$
s_v(u, v_0) = \frac{3}{2} \frac{c_1(u) - c_0(u)}{v_1 - v_0} - \frac{1}{2} s_v(u, v_1),
$$

$$
s_v(u, v_n) = \frac{3}{2} \frac{c_n(u) - c_{n-1}(u)}{v_n - v_{n-1}} - \frac{1}{2} s_v(u, v_{n-1})
$$

for the outer curves. The mixed derivatives are computed using the partial derivatives \( s_v(u,v) \) and \( s_u(u,v) \)

$$
s_{uv}(u_j, v_i) = \frac{1}{2} \left( \frac{\partial s_u(u_j, v)}{\partial v} \right)_{v=v_i} + \frac{\partial s_v(u, v_i)}{\partial u} \right)_{u=u_j}.
$$

Suppose that in (2.5.7) the curves \( c_i(u) \) and \( b_j(v) \) of the mesh are the cubic Hermite splines (1.3.10) constructed on the set of points \( p_{ji} \) and are determined by the relations:

$$
c_i(u) = F_j^T \begin{bmatrix} p_{ji} \\ p_{ji+1} \\ s_u(u_j, v_i) \\ s_u(u_{j+1}, v_i) \end{bmatrix},
$$

$$
b_j(v) = F_i^T \begin{bmatrix} p_{ji} \\ p_{ji+1} \\ s_v(u_j, v_i) \\ s_v(u_{j+1}, v_i) \end{bmatrix}.
$$
Substituting these relations into (2.5.7), we obtain three identical matrix terms, two positive and one negative. As a result the formula (2.5.7) takes the form

$$ r(u,v) = F_j^T \begin{bmatrix} p_{ji} & p_{j+1i} & s_u(u_j, v_i) & s_v(u_j, v_i) \\ p_{j-1i} & p_{j+1i+1} & s_u(u_{j+1}, v_i) & s_v(u_{j+1}, v_i+1) \\ s_u(u_j, v_i) & s_u(u_j, v_i+1) & s_u(u_j, v_i) & s_u(u_j, v_i+1) \\ s_u(u_{j+1}, v_i) & s_u(u_{j+1}, v_i+1) & s_u(u_{j+1}, v_i) & s_u(u_{j+1}, v_i+1) \end{bmatrix} F_j, \tag{2.5.8} $$

where we use the notation:

$$ s_u(u_j, v_i) = \frac{u_j - u_{j-1}}{(u_{j-1} - u_j)(u_{j-1} - u_{j+1})} + \frac{2u_j - u_{j-1} - u_{j+1}}{(u_j - u_{j-1})(u_j - u_{j+1})} + \frac{u_j - u_{j+1}}{(u_{j+1} - u_j)(u_{j+1} - u_{j+2})}, $$

$$ s_v(u_j, v_i) = \frac{v_i - v_{i-1}}{(v_{i-1} - v_i)(v_{i-1} - v_{i+1})} + \frac{2v_i - v_{i-1} - v_{i+1}}{(v_i - v_{i-1})(v_i - v_{i+1})} + \frac{v_i - v_{i+1}}{(v_{i+1} - v_i)(v_{i+1} - v_{i+2})}, $$

$$ s_{uv}(u_j, v_i) = \begin{bmatrix} u_j - u_{j+1} \\ (u_{j-1} - u_j)(u_{j-1} - u_{j+1}) \\ 2u_j - u_{j-1} - u_{j+1} \\ (u_j - u_{j-1})(u_j - u_{j+1}) \\ u_j - u_{j+1} \\ (u_{j+1} - u_j)(u_{j+1} - u_{j+2}) \end{bmatrix}^T \begin{bmatrix} p_{j-1i-1} & p_{j-1i} & p_{j-1i+1} \\ p_{j-1i} & p_{ji} & p_{j+1i} \\ p_{j+1i-1} & p_{j+1i} & p_{j+1i+1} \end{bmatrix} \begin{bmatrix} v_i - v_{i+1} \\ (v_{i-1} - v_i)(v_{i-1} - v_{i+1}) \\ 2v_i - v_{i-1} - v_{i+1} \\ (v_i - v_{i-1})(v_i - v_{i+1}) \\ v_i - v_{i+1} \\ (v_{i+1} - v_i)(v_{i+1} - v_i) \end{bmatrix}. $$

The surface (2.5.8) is completely determined by the points \( p_{ji} \).

### 2.6. Surfaces Constructed on a Set of Points

Construct a bicubic surface by changing the bilinear surface (2.5.1) constructed on four points \( p_{00}, p_{10}, p_{01}, \) and \( p_{11} \). Let the surface be the cubic function of both the first and the second parameter. Let the parameter domains of the surface vary in the ranges \( 0 \leq u \leq 1 \) and \( 0 \leq v \leq 1 \). We require that the radius vector of the surface coincide with points \( p_{00}, p_{10}, p_{01}, \) and \( p_{11} \) at the corners, that the partial derivatives of the radius vector with respect to parameter \( u \) will be equal to \( u_{00}, u_{10}, u_{01}, \) and \( u_{11} \) at the corners, that the partial derivatives of the radius vector with respect to parameter \( v \) will be equal
to \( v_{00}, v_{10}, v_{01}, \) and \( v_{11} \) at the corners, and that the second mixed derivatives of the radius vector with respect to parameters \( u \) and \( v \) will be equal to \( t_{00}, t_{10}, t_{01}, \) and \( t_{11} \) at the corners. Thus, the following conditions must be satisfied for a bicubic surface \( r(u,v): \)

$$
\begin{align*}
r(0,0) &= p_{00}, & r(1,0) &= p_{10}, & r(0,1) &= p_{01}, & r(1,1) &= p_{11}, \\
r_u(0,0) &= u_{00}, & r_u(1,0) &= u_{10}, & r_u(0,1) &= u_{01}, & r_u(1,1) &= u_{11}, \\
r_v(0,0) &= v_{00}, & r_v(1,0) &= v_{10}, & r_v(0,1) &= v_{01}, & r_v(1,1) &= v_{11}, \\
r_{uv}(0,0) &= t_{00}, & r_{uv}(1,0) &= t_{10}, & r_{uv}(0,1) &= t_{01}, & r_{uv}(1,1) &= t_{11}.
\end{align*}
$$

A surface that meets the specified conditions is

$$
r(u,v) = \begin{bmatrix}
p_{00} & p_{01} & v_{00} & v_{01} \\
p_{10} & p_{11} & v_{10} & v_{11} \\
u_{00} & u_{01} & t_{00} & t_{01} \\
u_{10} & u_{11} & t_{10} & t_{11}
\end{bmatrix} \begin{bmatrix}
\alpha_0(v) \\
\alpha_1(v) \\
\beta_0(v) \\
\beta_1(v)
\end{bmatrix},
$$

where \( \alpha_0(w) = 1 - 3w^2 + 2w^3, \alpha_1(w) = 3w^2 - 2w^3, \beta_0(w) = w - 2w^2 + w^3, \) and \( \beta_1(w) = -w^2 + w^3. \)

Construct a bicubic surface consisting of multiple surfaces (2.6.1) joined at the boundaries and the corners. Suppose there is the set of control points \( p_{ij}, i=0,1,...,n, j=0,1,...,m, \) arranged in \( n+1 \) rows and \( m+1 \) columns, with \( n+1 \) points in each column and with \( m+1 \) points in each row. The indexes of the point indicate that the point \( p_{ij} \) is located in \( i \)-th row at the \( j \)-th position in a row. Rows will be enumerated from 0 to \( n \) and their points will be enumerated from 0 to \( m \). According to the location of row of the control points, construct the set of knots \( v_i, i=0,1,...,n \) so that the change of knot values is proportional to the distance between adjacent rows of control points:

$$
\frac{v_{i+1} - v_i}{v_i - v_{i-1}} \approx \frac{\sum_{j=0}^{m-1} |p_{i+1,j} - p_{ij}|}{\sum_{j=1}^{m} |p_{ij} - p_{i,j-1}|}.
$$

Construct the set of knots \( u_j, j=0,1,...,m \) according to the location of columns of control points so that the change in knot values is proportional to the distance between adjacent columns of control points:

$$
\frac{u_{j+1} - u_j}{u_j - u_{j-1}} \approx \frac{\sum_{i=0}^{n-1} |p_{i,j+1} - p_{ij}|}{\sum_{i=1}^{n} |p_{ij} - p_{i,j-1}|}.
$$
We require that for the parametric values \( u = u_j \) and \( v = v_i \), the surface \( r(u,v) \) passes through the points \( p_{ij} \); i.e., \( r(u_j, v_i) = p_{ij} \). Construction of a bicubic surface requires the determination of its partial derivatives at control points \( u_{ij}, v_{ij}, \) and \( t_{ij} \).

The partial derivatives \( u_{ij} \) and \( v_{ij} \) of the surface radius vector at control points are calculated by analogy to the calculation of the derivatives at the control points of a Hermite spline. For this we construct a vector Lagrange polynomial (1.3.4) of the second order, which passes through three adjacent points \( p_{i-1,j}, p_{ij}, \) and \( p_{i+1,j} \) at parameter values \( v_{i-1}, v_i, \) and \( v_{i+1} \), compute the derivative of this polynomial at \( v_i \) and take its partial derivative with respect to the second parameter of the surface radius vector at the point \( v_i, i = 1,2,...,n-1 \):

$$
v_{ij} = \frac{\partial r(u_j, v_i)}{\partial v} = p_{i-1,j} \frac{v_i - v_{i+1}}{(v_{i-1} - v_i)(v_{i-1} - v_{i+1})} + p_{ij} \frac{2v_i - v_{i-1} - v_{i+1}}{(v_i - v_{i-1})(v_i - v_{i+1})} + p_{i+1,j} \frac{v_i - v_{i-1}}{(v_{i+1} - v_i)(v_{i+1} - v_i)}
$$

Similarly, we calculate the partial derivatives with respect to the first parameter of the surface radius vector at the points \( u_j, j = 1,2,...,m-1 \)

$$
u_{ij} = \frac{\partial r(u_j, v_i)}{\partial u} = p_{ij-1} \frac{u_j - u_{j+1}}{(u_{j-1} - u_j)(u_{j-1} - u_{j+1})} + p_{ij} \frac{2u_j - u_{j-1} - u_{j+1}}{(u_j - u_{j-1})(u_j - u_{j+1})} + p_{ij+1} \frac{u_j - u_{j-1}}{(u_{j+1} - u_j)(u_{j+1} - u_j)}
$$

The derivatives at the boundary control points of the surface are obtained from the condition that the second derivative of the radius vector with respect to the parameter \( v \)

$$
\frac{\partial^2 r(u_j, v_0)}{\partial v^2} = \frac{3}{2} \frac{p_{1j} - p_{0j}}{v_1 - v_0} - \frac{1}{2} \frac{\partial r(u_j, v_1)}{\partial v}
$$

$$
\frac{\partial^2 r(u_j, v_n)}{\partial v^2} = \frac{3}{2} \frac{p_{nj} - p_{n-1,j}}{v_n - v_{n-1}} - \frac{1}{2} \frac{\partial r(u_j, v_{n-1})}{\partial v}
$$

and with respect to the parameter \( u \)

$$
\frac{\partial^2 r(u_0, v_i)}{\partial u^2} = \frac{3}{2} \frac{p_{1i} - p_{0i}}{u_1 - u_0} - \frac{1}{2} \frac{\partial r(u_1, v_i)}{\partial u}
$$

$$
\frac{\partial^2 r(u_m, v_i)}{\partial u^2} = \frac{3}{2} \frac{p_{mi} - p_{m-1,i}}{u_m - u_{m-1}} - \frac{1}{2} \frac{\partial r(u_{m-1}, v_i)}{\partial u}
$$

vanishes at the boundary control points.

The partial derivatives \( t_{ij} \) of the surface radius vector at the control points are calculated by finite-difference formulas

$$
t_{ij} = \frac{\partial^2 r(u_j, v_i)}{\partial u \partial v} = \frac{p_{i+1,j+1} - p_{i-1,j+1} - p_{i+1,j-1} + p_{i-1,j-1}}{(u_{i+1} - u_{i-1})(v_{i+1} - v_{i-1})}
$$
If during the calculation of the derivatives $t_j$ the index $i-1$ or $j-1$ becomes less than zero, then it is set equal to zero; if the index $i+1$ is greater than $n+1$ then it is set equal to $n+1$; if the index $j+1$ is greater than $m+1$, then it is set equal to $m+1$.

To calculate the radius vector of a surface constructed on a mesh of points, follow these additional steps. Find indexes $I$ and $j$ of the corner control point $p_{ij}$ of the considered part of the surface from the condition $u_j \leq u \leq u_{j+1}$ and $v_i \leq v \leq v_{i+1}$; using the given parameters $u$ and $v$, calculate the surface radius vector

$$r(u,v) = \begin{bmatrix} p_{ij} & p_{i+1,j} & v_j & v_{i+1,j} \\ p_{i,j+1} & p_{i+1,j+1} & v_{i,j+1} & v_{i+1,j+1} \\ u_{ij} & u_{i+1,j} & t_j & t_{i+1,j} \\ u_{i,j+1} & u_{i+1,j+1} & t_{i,j+1} & t_{i+1,j+1} \end{bmatrix} \begin{bmatrix} \alpha_0(y) \\ \alpha_1(y) \\ \beta_0(y) \\ \beta_1(y) \end{bmatrix},$$

(2.6.2)

where $x = \frac{u - u_j}{u_{j-1} - u_j}$, $y = \frac{v - v_i}{v_{i-1} - v_i}$.

It should be noted that the surface (2.6.2) may have self-intersections and folds in the places where the distance between adjacent control points is not proportional to the difference between the values of the relevant parameters and where the partial derivatives $t_j$ take large values.

### 2.7. Bezier Surfaces

Let there be the set of points $p_{ij}$, $i=0,1,...,n$, $j=0,1,...,m$, be conventionally arranged at the nodes of the rectangular mesh; i.e., let them be conventionally disposed in $n+1$ rows, with $m+1$ points in each row. Point indexation means that the location of point $p_{ij}$ is at the $j$-th position in the $i$-th row. The rows are numbered from 0 to $n$ and the points in the rows are numbered from 0 to $m$. A Bezier surface constructed on the set of points $p_{ij}$ is described by the vector function

$$r(u,v) = \sum_{i=0}^{n} \sum_{j=0}^{m} B^n_i(v)B^m_j(u)p_{ij},$$

(2.7.1)

where $B^n_i(v) = \frac{n!}{(n-i)!i!} v^i(1-v)^{n-i}$ and $B^m_j(u) = \frac{m!}{(m-j)!j!} u^j(1-u)^{m-j}$ are functions of the Bernstein basis. In accordance with (1.4.3), we have

$$\sum_{i=0}^{n} \sum_{j=0}^{m} B^n_i(v)B^m_j(u) = 1.$$  

(2.7.2)
Points $p_{ij}$ are called control points. The sections of the surface (2.7.1) along the lines $u=\text{const}$ or $v=\text{const}$ are Bezier curves of the $m$-th and $n$-th order, respectively. We say that the surface (2.7.1) has order $m$ with respect to the first parameter and has order $n$ with respect to the second parameter. The parameter domain of the surface is a square with side equal to unity.

Fig. 2.7.1.

If we imagine that the bilinear surface is constructed on each four adjacent points $p_{ij}$, $p_{i+1,j}$, $p_{i,j+1}$, and $p_{i+1,j+1}$, we obtain a polyhedron which we call the control polyhedron. The control polyhedron provides a general view of the Bezier surface. The Bezier surface together with its control polyhedron is shown in Fig. 2.7.1. Since only zero and the last Bernstein coefficient take the maximum possible value, and the rest are equal to zero, the Bezier surface passes only through the corner control points of the mesh: $p_{00}$, $p_{0m}$, $p_{n0}$, and $p_{nm}$.

We assign the weight $w_{ij}$ to each control point $p_{ij}$ respectively. The rational Bezier surface constructed on the set of points $p_{ij}$ is described by the vector function

$$r(u,v) = \frac{\sum_{i=0}^{n} \sum_{j=0}^{m} B^n_i(v) B^m_j(u) w_{ij} p_{ij}}{\sum_{i=0}^{n} \sum_{j=0}^{m} B^n_i(v) B^m_j(u) w_{ij}}. \quad (2.7.3)$$

In terms of homogeneous coordinates the radius vector of a rational Bezier surface is described by the equation of the same form as (2.7.1)

$$R(u,v) = \sum_{i=0}^{n} \sum_{j=0}^{m} B^n_i(v) B^m_j(u) P_{ij},$$

where $P_{ij} = [w_{ij} p_{ij} w_{ij}]^T$ are extended vectors (1.6.3) of the surface control points. Not the absolute values of the weights of the points, but rather their relative values, play a role in the rational surfaces. The greater the weight of the control point relative to weights
of other control points, the closer the surface passes to this point. If the weight of all the control points is equal then the rational Bezier surface takes the form of (2.7.1).

The radius vector of a rational surface is calculated as a quotient of two functions of the parameters \( u \) and \( v \); so when computing the derivatives of a rational surface the right side of (2.7.3) should be considered as a composite function. If we conventionally denote the radius vector of a rational surface as \( r = \frac{wr}{w} \), then the partial derivatives of the radius vector of a rational surface are determined by formulas

$$
\frac{\partial r}{\partial u} = \frac{1}{w} \frac{\partial (wr)}{\partial u} - \frac{wr}{w^2} \frac{\partial w}{\partial u}, \quad \frac{\partial r}{\partial v} = \frac{1}{w} \frac{\partial (wr)}{\partial v} - \frac{wr}{w^2} \frac{\partial w}{\partial v}.
$$

The higher-order derivatives are calculated similarly.

A rational Bezier surface can describe a part of a second-order surface as well as a part of a torus surface. For this purpose it is easy to use a rational Bezier surface of the second order constructed on nine control points:

$$
r(u, v) = \begin{bmatrix}
(1-v)^2 & 2v(1-v) & v^2 \\
w_u p_{00} & w_u p_{01} & p_{02} \\
w_v p_{10} & w_v p_{11} & w_v p_{12} \\
p_{20} & w_u p_{21} & p_{22}
\end{bmatrix} \cdot \begin{bmatrix}
(1-u)^2 \\
2u(1-u) \\
u^2
\end{bmatrix},
$$

$$
(1-u)^2 + 2u(1-u)w_u + u^2 \cdot (1-v)^2 + 2v(1-v)w_v + v^2 \right) \tag{2.7.4}
$$

The weights of the corner points are equal to unity; and for the remaining points, we introduce the weights \( w_u \) and \( w_v \), which have indexes of the parametric directions of the surface. The type of the surface obtained by formula (2.7.4) depends on the position of the control points and weights \( w_u \) and \( w_v \). If the sections of the surface (2.7.4) along the lines \( u=\text{const} \) or \( v=\text{const} \) are circular arcs with open angles \( \alpha_u \) and \( \alpha_v \), respectively, then \( w_u = \cos(\alpha_u/2) \) and \( w_v = \cos(\alpha_v/2) \).

A composite Bezier surface allows overcoming the rigid link between the smoothness of the surface and the number of control points it is constructed on. We obtain a composite Bezier surface as a result of joining individual Bezier surfaces having common control points along the junction borders and identical degrees. In order to smoothly join the individual Bezier surfaces to each other, it is necessary that the segments of the control polyhedrons adjacent to the common points of the joining surfaces lie in the same plane.

### 2.8. B-Spline Surfaces

Construct a non-uniform rational surface based on B-splines in the same way we constructed the Bezier surface based on the Bernstein functions. Let there be a set of points \( p_{ij}, i=0,1,...,n, j=0,1,...,m \), conventionally placed at the nodes of a rectangular mesh in the form of \( n+1 \) rows, with \( m+1 \) points in each row. A non-uniform rational
surface based on B-splines of order \( k \) with respect to the first parameter and of order \( l \) with respect to the second parameter is described by the vector function

$$
r(u,v) = \frac{\sum_{i=0}^{n} \sum_{j=0}^{m} N_i^l(v) N_j^k(u) w_{ij} p_{ij}}{\sum_{i=0}^{n} \sum_{j=0}^{m} N_i^l(v) N_j^k(u) w_{ij}},
$$

(2.8.1)

where \( N_i^l(v) \) and \( N_j^k(u) \) are B-splines (1.8.1). Surface (2.8.1) is called a **NURBS surface** (Non-Uniform Rational B-Spline surface) or **B-spline surface**.

Each of the order-\( k \) B-spline \( N_j^k(u) \) is constructed on a non-decreasing sequence of \( k+2 \) knots \( u_j, u_{j+1}, \ldots, u_{j+k-1} \). Construction of the set of \( m+1 \) order-\( k \) B-splines requires \( m+k+2 \) knots \( u_j \) in total, in the case of an open surface, and \( m+2k+2 \) knots in total, in the case of a cyclic closed surface. Each of the order-\( l \) B-spline \( N_i^l(v) \) is constructed on a non-decreasing sequence of \( l+2 \) knots, \( v_i, v_{i+1}, \ldots, v_{i+l-1} \). Construction of the set of \( n+1 \) \( l \)-order B-splines requires \( n+l+2 \) knots \( v_i \) in total, for an open surface, and \( n+2l+2 \) knots in total for a cyclic closed surface. As follows from (2.8.1), the B-spline surface has two non-decreasing sequences of knots, one for the first parameter, and the other for the second parameter.

Sections of the surface (2.8.1) along the lines \( u=\text{const} \) or \( v=\text{const} \) are the B-spline curves of the \( k \)-th and \( l \)-th order respectively. We say that the surface (2.8.1) has degree \( k \) with respect to the first parameter, and has degree \( l \) with respect to the second parameter. Parametric domain of the B-spline surface is a rectangle: \( u_k \leq u \leq u_{m+k+1} \), \( v_l \leq v \leq v_{n+l+1} \). Thus, \( u_{\min}=u_k, u_{\max}=u_{m+k+1}, v_{\min}=v_l, v_{\max}=v_{n+l+1} \).

Let knot numbering start from zero. For the B-spline surface closed with respect to the first parameter one usually uses the B-splines \( N_j^k(u) \) constructed on non-decreasing sequence of knots, in which the first and the last \( k+1 \) knots coincide: \( u_0=u_1=\ldots=u_k \) and \( u_{m-1}=u_{m-2}=\ldots=u_{m+k+1} \). For the B-spline surface open with respect to the second parameter one usually uses the B-splines \( N_i^l(v) \) constructed on non-decreasing sequence of knots, in which the first and the last \( l+1 \) knots coincide: \( v_0=v_1=\ldots=v_l \) and \( v_{n-1}=v_{n-2}=\ldots=v_{n+l-1} \). For the B-spline surface cyclic closed with respect to the first (second) parameter the corresponding sequence of knots should reflect the closeness: the first \( 2k \) (\( 2l \)) knots must be separated by intervals the same as the intervals the last \( 2k \) (\( 2l \)) knots are separated by.

When all control points of the B-spline surface have equal weights, then with (1.8.11) the formula (2.8.1) for calculation of the radius vector of the surface based on B-splines becomes

$$
r(u,v) = \sum_{i=0}^{n} \sum_{j=0}^{m} N_i^l(v) N_j^k(u) p_{ij}.
$$

(2.8.2)

In terms of homogeneous coordinates (1.6.3), the formula (2.8.1) has the form

$$
R(u,v) = \sum_{i=0}^{n} \sum_{j=0}^{m} N_i^l(v) N_j^k(u) P_{ij},
$$
similar to the form (2.8.2).

If the bilinear surfaces are constructed on every four adjacent control points, then we obtain some control polyhedron of the surface. If we construct the B-spline surface based on the B-splines of the first order, then it will coincide with its control polyhedron.

To compute the radius vector of the B-spline surface, the formulas (1.9.3) and (1.9.4) are used. Using the parameter value \( u \) from the condition \( u_j \leq u < u_{j+1} \) let us define the number \( j \) of non-vanishing not-normalized order-zero B-splines

$$
M_j^0(u) = \frac{1}{u_{j+1} - u_j}.
$$

Then, using the Cox–De Boor recursion relation,

$$
M_r^k(u) = \frac{u_{r+k+1} - u}{u_{r+k+1} - u_r} M_{r+1}^{k-1}(u) + \frac{u - u_r}{u_{r+k+1} - u_r} M_r^{k-1}(u),
$$

we calculate all non-vanishing B-splines up to the \( k \)-th order at the given parameter \( u \): \( M_{j-k}^k(u), M_{j-k+1}^k(u), \ldots, M_j^k(u) \). Then, we normalize the B-splines of the \( k \)-th order as

$$
N_r^k(u) = (u_{r+k+1} - u_r) M_r^k(u), \quad r = j-k, j-k+1, \ldots, j.
$$

Similarly, using the value of the parameter \( v \) from the condition \( v_i \leq v < v_{i+1} \), let us define the number \( i \) of non-vanishing not-normalized order-zero B-splines

$$
M_i^0(v) = \frac{1}{v_{i+1} - v_i}.
$$

Then, using the Cox–De Boor recursion relation,

$$
M_q^l(v) = \frac{v_{q+l+1} - v}{v_{q+l+1} - v_q} M_{q+1}^{l-1}(v) + \frac{v - v_q}{v_{q+l+1} - v_q} M_q^{l-1}(v),
$$

we calculate all non-vanishing B-splines up to the \( l \)-th order at the given parameter \( v \): \( M_{i-l}^l(v), M_{i-l+1}^l(v), \ldots, M_i^l(v) \)—and normalize them:

$$
N_q^l(v) = (v_{q+l+1} - v_q) M_q^l(v), \quad q = i-l, i-l+1, \ldots, i.
$$

Since in general only a part of the B-splines is non-vanishing, the radius vector of the point of the B-spline surface (2.8.1) for the parameters \( u_j \leq u < u_{j+1} \) and \( v_i \leq v < v_{i+1} \) is calculated by formula
$$ r(u,v) = \frac{\sum_{q=i-l}^{i} \sum_{r=j-k}^{j} N_q^l(v) N_r^k(u) w_{qr} p_{qr}}{\sum_{q=i-l}^{i} \sum_{r=j-k}^{j} N_q^l(v) N_r^k(u) w_{qr}}. $$

When calculating B-splines, you can at the same time calculate their derivatives using relations (1.8.15).

Compute the partial derivatives of the surface by differentiating the numerator and denominator on the right-hand side of (2.8.1), taking into account (1.8.15) and (1.8.5):

$$
\begin{align*}
\frac{\partial r}{\partial u} &= \frac{\partial}{\partial u} \left( \frac{wr}{w} \right) = \frac{1}{w} \frac{\partial (wr)}{\partial u} - \frac{wr}{w^2} \frac{\partial w}{\partial u}, \\
\frac{\partial r}{\partial v} &= \frac{\partial}{\partial v} \left( \frac{wr}{w} \right) = \frac{1}{w} \frac{\partial (wr)}{\partial v} - \frac{wr}{w^2} \frac{\partial w}{\partial v},
\end{align*}
$$

where

$$ wr = \sum_{i=0}^{n} \sum_{j=0}^{m} N_i^l(v) N_j^k(u) w_{ij} p_{ij} $$ – the numerator of the right-hand side of (2.8.1),

$$ w = \sum_{i=0}^{n} \sum_{j=0}^{m} N_i^l(v) N_j^k(u) w_{ij} $$ – the denominator of the right-hand side of (2.8.1),

$$
\frac{\partial (wr)}{\partial u} = k \sum_{i=0}^{n} \sum_{j=1}^{m} N_i^l(v) N_j^{k-1}(u) \frac{w_{ij} p_{ij} - w_{ij-1} p_{ij-1}}{u_{j+k} - u_j} $$ – derivative of the numerator with respect to \( u \),

$$
\frac{\partial w}{\partial u} = k \sum_{i=0}^{n} \sum_{j=1}^{m} N_i^l(v) N_j^{k-1}(u) \frac{w_{ij} - w_{ij-1}}{u_{j+k} - u_j} $$ – derivative of the denominator with respect to \( u \),

$$
\frac{\partial (wr)}{\partial v} = l \sum_{i=1}^{n} \sum_{j=0}^{m} N_i^{l-1}(v) N_j^k(u) \frac{w_{ij} p_{ij} - w_{i-1,j} p_{i-1,j}}{v_{i+l} - v_i} $$ – derivative of the numerator with respect to \( v \), and

$$
\frac{\partial w}{\partial v} = l \sum_{i=1}^{n} \sum_{j=0}^{m} N_i^{l-1}(v) N_j^k(u) \frac{w_{ij} - w_{i-1,j}}{v_{i+l} - v_i} $$ – derivative of the denominator with respect to \( v \).

Let there be found numbers \( j \) and \( i \) of the knots \( u_j \) and \( v_i \) for parameter values \( u \) and \( v \) from the conditions \( u_j \leq u < u_{j+1} \) and \( v_i \leq v < v_{i+1} \). The following B-splines are non-vanishing at the given values of the parameters: \( N_{j-k}^k(u), \ldots, N_{j-1}^k(u), N_j^k(u) \) and \( N_i^{l-1}(v), \ldots, N_{i-1}^{l-1}(v), N_i^l(v) \), and also \( N_{j-k+1}^{k-1}(u), \ldots, N_{j-1}^{k-1}(u), N_j^{k-1}(u) \) and \( N_{i-1}^{l-1}(v), \ldots, N_i^{l-1}(v), N_{i+1}^{l-1}(v) \); therefore the summation in the above formulas is carried out on indexes corresponding to non-vanishing B-splines.

Similarly, the derivatives of the radius vector of B-spline surfaces of a higher order are calculated as:
$$
\frac{\partial^{(r+q)} r}{\partial u^{(r)} \partial v^{(q)}} = \frac{\partial^{(r+q)} w}{\partial u^{(r)} \partial v^{(q)}} \left( \frac{w(u,v)}{w(u,v)} \right).
$$

If the numbering of knots \( u_j \) starts, not from zero, but from \(-k-1\) (to reduce by \( k+1 \) the values of indexes for all knots \( u_j \)), the numbering of the knots \( v_i \) also starts, not from zero, but from \(-l-1\) (to reduce by \( l+1 \) the values of all indexes for the knots \( v_i \)), and then surface (2.8.1) coincides with the surface

$$
r(u,v) = \frac{\sum_{i=0}^{n} \sum_{j=0}^{m} N'_i(v) N^k_j(u) w_y P_{ij}}{\sum_{i=0}^{n} \sum_{j=0}^{m} N'_i(v) N^k_j(u) w_y},
$$

where \( N'_i(v) \) and \( N^k_j(u) \) are B-splines by definition (1.13.1). The B-spline surface (2.8.3) uses the definition of the B-spline in which it has the index of the last knot of the sequence the B-spline was constructed on. Surface (2.8.3) is distinguished from surface (2.8.1) only by the recursion relations used to calculate the surface radius vector and its derivatives. Relations (1.13.3) – (1.13.8) are used instead of the above formulas.

In the special case when \( k=m \) and \( l=n \), B-splines \( N^k_j(u) \) are constructed on the sequence of knots \( u_{-1-k}=u_{-k}=...=u_{-1}=0 \), \( u_0=u_1=...=u_k=1 \), and B-splines \( N'_i(v) \) are constructed on the sequence of knots \( v_{-1-l}=v_{-l}=...=v_{-1}=0 \), \( v_0=v_1=...=v_l=1 \), surface (2.8.3) coincides with the rational Bezier surface (2.7.3).

As an example, we construct a B-spline surface with knots of integer values.

Let the first \( k+1 \) knots of the \( u \)-sequence of the open B-spline curve have values equal to zero: \( u_0=u_1=...=u_k=0 \); the next \( m-k \) knots of the sequence have integer values from 1 to \( m-k \): \( u_{k+1}=j \), \( j=1,2,...,m-k \); and the remaining \( k+1 \) knots have the value \( m-k+1 \): \( u_{m+1}=u_{m+2}=...=u_{m+k+1}=m-k+1 \). Let the first \( l+1 \) knots of the \( v \)-sequence have zero values: \( v_0=v_1=...=v_l=0 \); the next \( n-l \) knots have integer values from 1 to \( n-l \): \( v_{l+1}=i \), \( i=1,2,...,n-l \); and the remaining \( l+1 \) knots have the value \( n-l+1 \): \( v_{n+1}=v_{n+2}=...=v_{n+l+1}=n-l+1 \).

Fig. 2.8.1 shows a B-spline surface of the third order with respect to both parametric directions constructed on a mesh consisting of sixty-three control points. The weights of all control points are identical.

![Fig. 2.8.1](image-url)
The control polyhedron of the surface shown in Fig. 2.8.1 is shown in Fig. 2.8.2.

For a B-spline surface that is cyclic closed with respect to the first (second) parameter, a uniform sequence of knots with a unit step can be used; for example, \( u_j = j - k, \quad j = 0, 1, \ldots, m + 2k + 1 \) (\( v_i = i - l, \quad i = 0, 1, \ldots, n + 2l + 1 \)).

If \( n = l, \quad m = k \), the knots of the \( u \)-sequence have values \( u_0 = u_1 = \ldots = u_m = 0, \quad u_{m+1} = u_{m+2} = \ldots = u_{2m+1} = 1 \), and the knots of the \( v \)-sequence have values \( v_0 = v_1 = \ldots = v_n = 0, \quad v_{n+1} = v_{n+2} = \ldots = v_{2n+1} = 1 \), then the B-spline surface (2.8.1) coincides with the rational Bezier surface (2.7.3). This follows from the fact that Bernstein functions are special cases of B-splines. The parametric domain of the B-spline surface in this case is a rectangle with sides equal to unity.

Unlike the Bezier surface, the order of the B-spline surface is not rigidly linked to the number of control points; also, it provides an opportunity to construct low-order surfaces on a large number of control points, which gives the surface more flexibility.

### 2.9. T-Spline Surfaces

The B-spline surface is constructed on a set of control points \( p_{ij} \), usually located at the nodes of a rectangular mesh. If it is required to construct a surface having a local feature, you’ll need a concentration of control points in the corresponding location. This concentration will entail an increase in the number of control points in all rows and columns of the mesh intersecting the local feature. If a surface has several local features, then you need to construct an unreasonably complicated surface. Some modification of the B-spline surface allows us to avoid this complexity.
Consider a surface based on B-splines described by the vector function

$$\mathbf{r}(u,v) = \frac{\sum_{i=0}^{n} N_i^k(u)N_i^k(v)w_ip_i}{\sum_{i=0}^{n} N_i^k(u)N_i^k(v)w_i},$$  \hspace{1cm} (2.9.1)

where $N_i^k(u)$ and $N_i^k(v)$ are B-splines of $k$-th order; $p_i$, $i=0,1,...,n$, are control points; and $w_i$ are their weights. The surface (2.9.1) may have unique B-splines $N_i^k(u)$ and $N_i^k(v)$ for each control point, because they can be constructed on unique sequences of knots. This surface (2.9.1) is called a T-spline surface.

To describe the sequence of knots of the B-splines in the parametric domain of the surface (2.9.1), we construct a mesh consisting of edges and vertices. Figs. 2.9.1–2.9.3 show mesh fragments in the parametric domain of the T-spline surface. Each mesh cell must be rectangular. The sides of the cell can be composed of several edges but the lengths of the opposite sides of each cell must be identical. Thus for the lengths of the cell edges located in the center of Fig. 2.9.1, these equalities must be satisfied:

$$u_1 + u_2 = u_3 + u_4 + u_5, \quad v_1 = v_2 + v_3.$$  

![Fig. 2.9.1](image)

The control points of the surface are associated with the mesh vertices.

When the mesh of the T-spline surface is constructed, the sequence of knots for the B-splines $N_i^k(u)$ and $N_i^k(v)$ of the $i$-th control point can be determined in the following way. Draw two lines through the $i$-th mesh node along the parametric directions—horizontal and vertical. Take $k+2$ points of intersection of the horizontal line with the vertical edges of the mesh as the sequence of knots for the B-spline $N_i^k(u)$. Take $k+2$ points of intersection of the vertical line with the horizontal edges of the mesh as the sequence of knots for the B-spline $N_i^k(v)$. Let $k/2$ knots of the sequence be found before the $i$-th vertex of the mesh, and let the remaining $k+2-(k/2)$ knots of the sequence start from the $i$-th vertex of the mesh. The gray dashed lines in Fig. 2.9.2 show the areas of non-zero values of the B-splines of the fifth order $N_i^5(u)$ and $N_i^5(v)$ for the $i$-th control point of the T-spline surface.
If the $T$-spline surface is not cyclic closed and there are not enough intersections at some side of the $i$-th vertex the mesh, let us make the boundary knot multiple. For the control point on the edge of the mesh, the associated mesh vertex will be included in a sequence of knots several times. In the Fig. 2.9.3, the multiplicity of the $j$-th knot in the sequence of knots of the fifth-order $B$-spline $N_j^5(u)$ is equal to four and the multiplicity of the $k$-th knot in the sequence of knots of the fifth-order $B$-spline $N_j^5(v)$ is equal to three.

A non-cyclic closed $T$-spline surface does not pass through its boundary control points.

A mesh in the parametric domain can also be constructed for a $B$-spline surface. This mesh is a regular rectangular grid. Typically, a $T$-spline surface is constructed by modifying a $B$-spline surface. To perform the modification, one can either insert new control points into the $B$-spline surface, or simplify the $B$-spline surface by removing control points and changing the location of the remaining control points. Fig. 2.9.4 shows a third-order $B$-spline surface with respect to both coordinate directions and its control points.
The $B$-splines of the endpoints of the surface are constructed on sequences of five knots, among which the last three coincide; therefore the surface does not pass through the control endpoints. It is required to have a local concentration of control points in the middle part of the surface, which implies an increase in the number of control points in all middle rows and columns of the mesh. The mesh in the parametric domain of the $B$-spline surface is a regular rectangular grid with a control point corresponding to each vertex. The mesh of the $T$-spline surface is obtained from the mesh of the $B$-spline surface by removing some edges and vertices. Fig. 2.9.5 shows the $T$-spline surface obtained by simplifying the $B$-spline surface shown in Fig. 2.9.4.

The shape of the $B$-spline surface may change during the simplification. Different methods may be used to minimize this change. Suppose it is required to construct a $T$-spline surface approximating some surface with a known radius vector described by the vector function $\mathbf{b}(u,v)$. The location of the control points of the surface (2.9.1) and their weights can be found from the minimum of the function
$$ \Psi(p_0, \ldots, p_n, w_0, \ldots, w_n) = \frac{1}{2} \iint \left( \frac{\sum_{i=0}^{n} N_i^k(u)N_i^k(v)w_i p_i}{\sum_{i=0}^{n} N_i^k(u)N_i^k(v)w_i} - b(u,v) \right)^2 dudv. $$

It is possible to replace the integration by a summation of the values of the integrand at some selected values of the parameters \( u \) and \( v \). The condition of the minimum of the function gives the system of equations. The solution of this system provides coordinates of the control points of the \( T \)-spline surface and their weights.

### 2.10. Surfaces of Triangular Form

Consider surfaces that have a triangular form, and a triangular parametric domain. It is convenient to use barycentric coordinates for triangular regions in two-dimensional space.

Let a Cartesian rectangular coordinate system be chosen in two-dimensional space for the parameters \( u \) and \( v \). Suppose there are three given points in this system—\( p_a = [u_a, v_a]^T \), \( p_b = [u_b, v_b]^T \) and \( p_c = [u_c, v_c]^T \), and suppose these points do not lie on one line (see Fig. 2.10.1).

![Fig. 2.10.1](image)

The position of any other point \( p = [u, v]^T \) can be described using the points \( p_a \), \( p_b \), and \( p_c \) with the help of the equation

$$ p = a p_a + b p_b + c p_c, $$  

where coefficients \( a, b, c \) are defined up to the constant factor. We require for complete determination that their sum be equal to unity:

$$ a + b + c = 1. $$
We find the values of the coefficients \(a\), \(b\), and \(c\) corresponding to the Cartesian coordinates \(u\) and \(v\) from the system of equations

$$
\begin{align*}
a u_a + b u_b + c u_c &= u, \\
a v_a + b v_b + c v_c &= v, \\
a + b + c &= 1.
\end{align*}
$$

The coefficients \(a\), \(b\), and \(c\) are expressed as follows

$$
a = \frac{1}{\Delta_{abc}} \begin{vmatrix} u & u_b & u_c \\ v & v_b & v_c \\ 1 & 1 & 1 \end{vmatrix}, \quad b = \frac{1}{\Delta_{abc}} \begin{vmatrix} u_a & u & u_c \\ v_a & v & v_c \\ 1 & 1 & 1 \end{vmatrix}, \quad c = \frac{1}{\Delta_{abc}} \begin{vmatrix} u_a & u_b & u \\ v_a & v_b & v \\ 1 & 1 & 1 \end{vmatrix},
$$

where the determinant of the system of equations (2.10.3)

$$
\Delta_{abc} = \begin{vmatrix} u_a & u_b & u_c \\ v_a & v_b & v_c \\ 1 & 1 & 1 \end{vmatrix} = u_a v_b + u_b v_c + u_c v_a - v_a u_b - v_b u_c - v_c u_a
$$

is equal to double the area of the triangle \(p_a p_b p_c\): \(\Delta_{abc} = 2S_{abc}\).

In many cases it is convenient to use three barycentric coordinates—i.e., coefficients \(a\), \(b\), and \(c\), instead of coordinates \(u\) and \(v\), to describe the position of a point in two-dimensional space. The barycentric coordinates of an arbitrary point \(p=[u \ v]^T\) are equal to the ratio between the area of the triangle \(p_a p_b p_c\) with the corresponding vertex replaced by point \(p\), to area of the triangle \(p_a p_b p_c\). The barycentric coordinates \(a\), \(b\), and \(c\) are functions of \(p\).

Let us note some properties of barycentric coordinates. They are governed by equation (2.10.2). If point \(p\) lies inside triangle \(p_a p_b p_c\), then its barycentric coordinates are non-negative. If point \(p\) coincides with one of the vertexes of triangle \(p_a p_b p_c\), then the corresponding barycentric coordinate of point \(p\) is equal to unity, and the other two barycentric coordinates are equal to zero. If point \(p\) belongs to the side of triangle \(p_a p_b p_c\) or lies on a continuation of the side, then one barycentric coordinate of point \(p\) is equal to zero. If point \(p\) lies outside triangle \(ABC\), then at least one barycentric coordinate of point \(p\) is negative.

Any two-dimensional vector \(t=[u \ v]^T\) can be described using points \(p_a\), \(p_b\), and \(p_c\) by the equation

$$
t = \alpha p_a + \beta p_b + \gamma p_c,
$$

Coefficients \(\alpha\), \(\beta\), and \(\gamma\) are called the barycentric components of the vector. Two-dimensional vector \(t\) can be represented as the difference between the radius vectors of two points; for example, \(p_1=a_1p_a+b_1p_b+c_1p_c\) and \(p_0=a_0p_a+b_0p_b+c_0p_c\). Since \(a_1+b_1+c_1=1\) and \(a_0+b_0+c_0=1\), then the barycentric components \(\alpha\), \(\beta\), \(\gamma\) of the two-dimensional vector are related by the equation
$$
\alpha + \beta + \gamma = 0. \tag{2.10.7}
$$

The values of barycentric components \( \alpha, \beta, \) and \( \gamma \) corresponding to the Cartesian components \( u \) and \( v \) of the vector \( t \) can be found from the system of equations

$$
\begin{align*}
\alpha u_a + \beta u_b + \gamma u_c &= u, \\
\alpha v_a + \beta v_b + \gamma v_c &= v, \\
\alpha + \beta + \gamma &= 0. \tag{2.10.8}
\end{align*}
$$

The components \( \alpha, \beta, \) and \( \gamma \) are expressed as follows:

$$
\alpha = \frac{1}{\Delta_{abc}} \begin{vmatrix} u & u_b & u_c \\ v & v_b & v_c \\ 0 & 1 & 1 \end{vmatrix}, \quad \beta = \frac{1}{\Delta_{abc}} \begin{vmatrix} u_a & u & u_c \\ v_a & v & v_c \\ 1 & 0 & 1 \end{vmatrix}, \quad \gamma = \frac{1}{\Delta_{abc}} \begin{vmatrix} u_a & u_b & u \\ v_a & v_b & v \\ 1 & 1 & 0 \end{vmatrix}, \tag{2.10.9}
$$

where determinant \( \Delta_{abc} \) is calculated by formula (2.10.5).

A triangular surface is constructed on three points. Let the parametric domain of the surface be bounded by a triangle with vertices at points \( p_a, p_b, \) and \( p_c; \) see Fig. 2.10.1. We introduce barycentric coordinates \( a, b, \) and \( c \) (2.10.4). We describe the radius vector of the triangular surface constructed on points \( p_1, p_2, \) and \( p_3 \) by a vector function of three parameters \( a, b, \) and \( c \):

$$
r(a,b,c) = ap_1 + bp_2 + cp_3, \quad a + b + c = 1. \tag{2.10.10}
$$

Suppose we are given three curves, \( c_1(t_1), c_2(t_2), \) and \( c_3(t_3), \) mutually intersecting at endpoints \( p_1, p_2, \) and \( p_3, \) as shown in Fig. 2.10.2.

Let us construct the surface inside the triangle formed by these curves. Change the parameterization to transform the curves such that the parameters 0 and 1 correspond to points \( p_3 \) and \( p_2 \) on curve \( c_1(t_1), \) parameters 0 and 1 correspond to points \( p_1 \) and \( p_3 \) on curve \( c_2(t_2), \) and parameters 0 and 1 correspond to points \( p_2 \) and \( p_1 \) on curve \( c_3(t_3). \)
The surface on three curves constructed on the given three curves is described by the vector function of three barycentric coordinates \(a\), \(b\), and \(c\):

$$
r(a,b,c) = a \left( c_3(1-b) + c_2(c) - p_1 \right) + \\
+ b \left( c_1(1-c) + c_3(a) - p_2 \right) + \\
+ c \left( c_2(1-a) + c_1(b) - p_3 \right),
$$

$$
0 \leq a \leq 1, \quad 0 \leq b \leq 1, \quad 0 \leq c \leq 1, \quad a + b + c = 1.
$$  

(2.10.11)

The boundaries of the surface (2.10.11) coincide with the curves on which the surface was constructed. At \(c=0\), \(b=1-a\) and vector

$$
r(a,1-a,0) = a \left( c_3(a) + c_2(0) - p_1 \right) + (1-a) \left( c_1(1) + c_3(a) - p_2 \right) = c_3(a)
$$

describes curve \(c_3(t_3)\). At \(a=0\), \(c=1-b\) and vector

$$
r(0,b,1-b) = b \left( c_1(b) + c_3(0) - p_2 \right) + (1-b) \left( c_2(1) + c_1(b) - p_3 \right) = c_1(b)
$$

describes curve \(c_1(t_1)\). At \(b=0\), \(a=1-c\) and vector

$$
r(1-c,0,c) = c \left( c_2(c) + c_1(0) - p_3 \right) + (1-c) \left( c_3(1) + c_2(c) - p_1 \right) = c_2(c)
$$

describes curve \(c_2(t_2)\). The first part of (2.10.11) is symmetrical under cyclic permutation of the indexes. Surface (2.10.11) is a triangular analog of the Coons surface (2.5.3).

Fig. 2.10.3 shows a triangular surface constructed on three identical circular arcs. The planes of the arcs are orthogonal to each other. The arcs intersect at points \(p_1\), \(p_2\), and \(p_3\). Each arc contains a quarter of a circle.

![Diagram](image)

Fig. 2.10.3.

Actually, the radius vectors of surfaces (2.10.10) and (2.10.11) depend on two parameters, since three parameters, \(a\), \(b\), and \(c\), are related by equation (2.10.2). We can rewrite relations (2.10.10) and (2.10.11) as functions of two parameters \(u\) and \(v\); for example: \(a(u,v)=u\), \(b(u,v)=v\), and \(c(u,v)=1-u-v\), where \(u\) and \(v\) take values in the triangular domain. We can rewrite relations (2.10.10) and (2.10.11) as functions of the same two parameters \(u\) and \(v\), taking their values in the ordinary rectangular domain.