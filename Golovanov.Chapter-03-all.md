CONSTRUCTIONS ON CURVES AND SURFACES

Curves and surfaces provide us with geometric information, if we refer to them with some parameters. When constructing a geometric model, we need to solve the inverse problem—to obtain the parameters of a curve or a surface from formulated geometric conditions. Solution of such problems is required in computing projections, determining points of intersection, and constructing new curves and surfaces that are required in geometric modeling, on the basis of other curves and surfaces.

3.1. Projection of a Point on a Curve

Suppose it is required to find the projection of a point $p$ on the line

$$
c(t) = c_0 + t c',
$$

where $c_0$ is a point of the line and $c'$ is a direction vector of non-zero length. Fig. 3.1.1 shows vector $c'$, point $c_0$, and the projection of point $p$. Construct the vector from a point of the line $c_0$ to point $p$ and calculate the dot product of this vector and vector $c'$.

If we divide this dot product by the length of vector $c'$, we obtain the length of the projection of vector $p - c_0$ on the straight line. If we divide this dot product by the square of the length of the vector $c'$, we obtain the length of the projection of vector $p - c_0$ on a straight line in the units of the vector $c'$ length—that is, parameter $t$ for the projection of point $p$ on a straight line.

Let us recall that each Latin letter in bold implies the presence of three coordinates. When we add, subtract, or multiply the radius vectors, the corresponding
manipulations are performed for each coordinate. These manipulations are similar, which gives us the ability to write them out in vector form. We don’t show the global coordinate system and, radius vectors of the points in the figures, we show the relative location of the objects. Let us repeat the steps of calculating the projection of a point on a line in detail.

Construct the vector $p - c_0$ from the initial point $c_0$ of the line to projected point $p$. Calculate the dot product $(p - c_0) \cdot c'$ equal to the length of the derivative vector of line $c'$ multiplied by the length of vector $p - c_0$. Dividing the dot product by the length of vector $c'$, we obtain the number $\frac{(p - c_0) \cdot c'}{\sqrt{c' \cdot c'}}$, equal to the distance (signed) from the initial point of line $c_0$ to point $p$, which is the projection of point $p$ on the line. Dividing this number one more time by the length of vector $c'$, we obtain the number $\frac{(p - c_0) \cdot c'}{c' \cdot c'}$, which is equal to the length (signed) of vector $p - c_0$ expressed in terms of the unit length of the line derivative (3.1.1). The negative sign $\frac{(p - c_0) \cdot c'}{c' \cdot c'}$ tells us that point $p$ lies on the line on the side of negative values of parameter $t$. For the initial point $c_0$, the parameter $t$ of the line is zero. For point $p$, parameter $t_p$ of the line is equal to $\frac{(p - c_0) \cdot c'}{c' \cdot c'}$. Using the relations for the radius vector of the line (3.1.1) and parameter $t_p$ of the point $p$ projection, we find the radius vector of projection $p_p$. Thus, parameter $t_p$ of the point $p$ projection on the line and the radius vector of the projection $p_p$ are calculated by the following formulas:

$$
t_p = \frac{(p - c_0) \cdot c'}{c' \cdot c'}, \quad p_p = c(t_p) = c_0 + t_p c'.
$$

(3.1.2)

The distance from the point to its projection on the line is equal to the length of vector $p_p - p$. The distance from the point to its projection on the line can be determined without calculating the point projection using the formula

$$
l_p = \frac{|(p - c_0) \times c'|}{|c'|}.
$$

Similarly, we find the projection of point $p$ on the line segment:

$$
c(t) = (1 - t)p_0 + tp_1.
$$

Parameter $t_p$ of the point $p$ projection on the line segment is calculated by formula (3.1.2), with point $c_0$ replaced by point $p_0$, and vector $c'$ replaced by vector $p_1 - p_0$:

$$
t_p = \frac{(p - p_0) \cdot (p_1 - p_0)}{|p_1 - p_0|^2}.
$$
Suppose it is required to find all projections of point $p$ on line $c(t)$. Every required point of the curve $c(t)$ satisfies the equation

$$
(p - c(t)) \cdot \frac{dc}{dt} = 0. \tag{3.1.3}
$$

This equation contains one unknown—parameter $t$. We solve the problem of finding projections of the point on the curve in two steps. Step one—We define initial approximations for parameters of the point projections on the curve. In step two, we find the values of the curve parameters defining the projection of a given point $p$ on curve $c(t)$ with a given precision.

To find initial approximations at some points of the curve with parameters $t_i$, we calculate the left-hand side of equation (3.1.3). Algorithms for selection of the trial points’ parameters are considered at the end of the chapter. If the dot product mentioned above has different signs in two adjacent points of the curve with parameters $t_i$ and $t_{i+1}$, then the value of $0.5(t_i + t_{i+1})$ can serve as the initial estimate in searching for the root of equation (3.1.3). The roots of equation (3.1.3) can be found by one of the methods for solving nonlinear algebraic equations. For example, the $(r+1)$-th approximation of the parameter of the point projection on the curve is calculated using the Newton method by the formula

$$
t^{(r+1)} = t^{(r)} - \frac{(p - c) \cdot \frac{dc}{dt}}{(p - c) \cdot \frac{d^2c}{dt^2} - \frac{dc}{dt} \cdot \frac{dc}{dt}}. \tag{3.1.4}
$$

The process of parameter refinement is stopped when the quantity $|t^{(r+1)} - t^{(r)}|$ at the next step of iteration is less than a specified value.

The projection of a point on various analytical curves can be found without using numerical methods. For example, let us find the projection of point $p$ on a circle:

$$
r(t) = p_0 + r \cos t i_x + r \sin t i_y, \quad 0 \leq t \leq 2\pi,
$$

where $i_x$ and $i_y$ are two mutually orthogonal unit vectors defining the position of the circle plane. To project a point on the circle plane and find the parameter of a two-dimensional projection of the point, we need to translate the point being projected to the local coordinate system with the origin at point $p_0$ and basis vectors $i_x, i_y,$ and $i_z = i_x \times i_y$. These manipulations are described by the formula

$$
t_p = \arctan \left( \frac{w \cdot i_y}{w \cdot i_x} \right). \tag{3.1.4}
$$

where $w = (p - p_0) - i_z ((p - p_0) \cdot i_z)$ is a projection of vector $p - p_0$ on the plane orthogonal to vector $i_z$.
3.2. Projection of a Point on a Surface

Suppose we need to find the projection of a point $p$ on the plane

$$
s(u,v) = s_0 + u s_1 + v s_2,
$$

where $s_0$ is the point on the plane, and $s_1$ and $s_2$ are non-parallel vectors of non-zero length. Point $p$ has a unique projection on the plane $s(u,v)$. Construct a unit normal to the plane:

$$
m = \frac{s_1 \times s_2}{|s_1||s_2|}.
$$

Then construct vector $p-s_0$ from the initial point $s_0$ of the plane to the projected point $p$. Calculate the dot product $(p-s_0) \cdot m$, which is equal to the length of the projection of vector $p-s_0$ onto the normal $m$. Multiplying vector $m$ by $(p-s_0) \cdot m$, we obtain vector $m((p-s_0) \cdot m)$ parallel to the normal vector, but with its length equal to the distance from the point being projected to the plane (3.2.1) (see Fig. 3.2.1). The radius vector of projection $p_s$ of point $p$ on the plane is equal to the difference between the radius vector of the projected point and radius vector $m((p-s_0) \cdot m)$:

$$
p_s = p - m((p-s_0) \cdot m).
$$

![Diagram](image)

Fig. 3.2.1.

Knowing the radius vector $p_s$ of the projection of point $p$ on the plane (3.2.1), we find parameters $u_p$ and $v_p$ of the plane for point $p_s$. Parameters $u_p$ and $v_p$ are the coordinates of the point $p_s$ in the local coordinate system of the plane with the origin at point $s_0$ and basis vectors $s_1, s_2, m$. For generality, we consider the case of the affine coordinate system. Let vectors $s_1$ and $s_2$ be not orthogonal and have arbitrary non-zero length. To calculate parameters $u_p$ and $v_p$ of point $p_s$, we find the lengths of the projections of $p_s-s_0$ onto vectors $s_1$ and $s_2$, which we denote by $p_1$ and $p_2$.
$$ p_1 = \frac{(p_s - s_0) \cdot s_1}{|s_1|}, \quad p_2 = \frac{(p_s - s_0) \cdot s_2}{|s_2|}. $$

The Fig. 3.2.2 shows vectors $s_1$ and $s_2$, point $s_0$, and projection $p_s$ of the specified point on the plane.

![Diagram](image)

**Fig. 3.2.2.**

Parameters $u_p$ and $v_p$ and the lengths of projections $p_1$ and $p_2$ are related by the equations

$$
p_1 = u_p |s_1| + v_p |s_2| \cos \varphi; \\
p_2 = v_p |s_2| + u_p |s_1| \cos \varphi,
$$

where $\cos \varphi = \frac{s_1 \cdot s_2}{|s_1||s_2|}$ is the cosine of the angle between vectors $s_1$ and $s_2$. We find the parameters of the projection of the point on the plane from the system of equations:

$$
u_p = \frac{p_1 - p_2 \cos \varphi}{(1 - \cos^2 \varphi)|s_1|} = \frac{g_{22}s_1 \cdot (p_s - s_0) - g_{12}s_2 \cdot (p_s - s_0)}{g_{11}g_{22} - g_{12}^2}, \quad (3.2.3)
$$

$$
v_p = \frac{p_2 - p_1 \cos \varphi}{(1 - \cos^2 \varphi)|s_2|} = \frac{g_{11}s_2 \cdot (p_s - s_0) - g_{12}s_1 \cdot (p_s - s_0)}{g_{11}g_{22} - g_{12}^2}, \quad (3.2.4)
$$

where $g_{11} = s_1 \cdot s_1$, $g_{22} = s_2 \cdot s_2$, and $g_{12} = s_1 \cdot s_2$ are the coefficients of the first fundamental quadratic form of the plane. If vectors $s_1$ and $s_2$ are orthogonal, then $g_{12} = 0$ and formulas (3.2.3) and (3.2.4) take the form

$$
u_p = \frac{(p_s - s_0) \cdot s_1}{s_1 \cdot s_1}, \quad v_p = \frac{(p_s - s_0) \cdot s_2}{s_2 \cdot s_2}.
$$

In the general case, the distance between a point and its projection is calculated as the length of vector $p_s - p$. The distance between the point and its projection on the
plane can be determined by calculating the projection of vector $p - s_0$ on the normal to the plane—not by calculating of the projection of the point:

$$
l_s = (p - s_0) \cdot m.
$$

The transition from the spatial coordinates of the point to surface parameters and back is a frequently encountered manipulation. Let us find a transformation matrix from the local coordinate system of a plane to the global coordinate system. Since point $p$ has coordinates $u_p, v_p,$ and $l_s$ in the local coordinate system of the plane with origin at $s_0$ and basis vectors $s_1, s_2,$ and $m,$ the following equality holds:

$$
p = s_0 + u_p s_1 + v_p s_2 + l_s m.
$$

Writing out this equality in matrix form:

$$
\begin{bmatrix}
u_p \\
v_p \\
l_s
\end{bmatrix} = s_0 + A \cdot \begin{bmatrix}
u_p \\
v_p \\
l_s
\end{bmatrix},
$$

where the columns of matrix $A$ are made up of the components of basis vectors $s_1, s_2,$ and $m$ of the local coordinate system. Let vector $s_1$ be described by components $s_{11}, s_{12},$ and $s_{13},$ the vector $s_2$ be described by components $s_{21}, s_{22},$ and $s_{23},$ and the vector $m$ be described by components $m_1, m_2,$ and $m_3;$ then

$$
A = \begin{bmatrix}
s_{11} & s_{21} & m_1 \\
s_{12} & s_{22} & m_2 \\
s_{13} & s_{23} & m_3
\end{bmatrix}.
$$

Thus, the transition from spatial coordinates of the point to parameters of the plane can be performed using the equality

$$
\begin{bmatrix}
u_p \\
v_p \\
l_s
\end{bmatrix} = A^{-1} \cdot (p - s_0),
$$

where $A^{-1}$ is inverse of matrix $A.$

Determination of the parameters of the projection of a point on the plane is used in seeking the initial approximations of the projection of a point on a surface. The initial approximations are important in iterative methods for solving systems of equations. An initial approximation must be in the domain in which solutions converge to the desired point. An incorrect initial approximation may result in divergence of the solution of the system of equations from the desired point. Moreover, the search for
initial approximations requires up to an order of magnitude more time than the iteration process for solving the system of equations, when the initial approximation is known.

Suppose it is required to find all projections of a point $p$ on a surface $s(u,v)$. Each of the required points of the surface $s(u,v)$ satisfies a system of two equations

$$
(p - s(u,v)) \cdot \frac{\partial s}{\partial u} = 0, \quad (p - s(u,v)) \cdot \frac{\partial s}{\partial v} = 0. \tag{3.2.5}
$$

The system of equations (3.2.5) has two unknowns—parameters $u$ and $v$. We solve the problem of determining the projection of the point on the surface in two steps. First we define initial approximations for parameters of the projections of the point on the surface; second, we find the values of the surface parameters defining the projection of a given point $p$ on the surface $s(u,v)$ with a given precision.

To find initial approximations in the neighborhood of certain points on the surface we calculate the left-hand side of (3.2.5). Let the trial points on the surface have parameters $u_i$ and $v_j$, let their neighborhoods be determined by increments of parameters $\Delta u$ and $\Delta v$. Let us calculate the values

$$
a_{ij} = (p - s(u_i - \Delta u, v_j)) \cdot \frac{\partial s}{\partial u}, \quad b_{ij} = (p - s(u_i + \Delta u, v_j)) \cdot \frac{\partial s}{\partial u},
$$
$$
c_{ij} = (p - s(u_i, v_j - \Delta v)) \cdot \frac{\partial s}{\partial v}, \quad d_{ij} = (p - s(u_i, v_j + \Delta v)) \cdot \frac{\partial s}{\partial v}.
$$

If $a_{ij}b_{ij} \leq 0$ and $c_{ij}d_{ij} \leq 0$, then the solution of system (3.2.5) can exist in the neighborhood of the trial point, and parameters $u_i$ and $v_j$ can be taken as the initial approximation. Starting with an initial approximation of parameters $u^{(0)} = u_i$ and $v^{(0)} = v_j$, and using one of the methods for solving non-linear algebraic equations, we find a solution of the system of equations with the required precision. For example, at the $r$-th iteration of the Newton method, the increments of projection parameters $\Delta u^{(r)}$ and $\Delta v^{(r)}$ are found from the system of non-linear equations

$$
((p-s) \cdot s_{11} - s_1 \cdot s_1) \Delta u^{(r)} + ((p-s) \cdot s_{12} - s_2 \cdot s_1) \Delta v^{(r)} = (s-p) \cdot s_1,
$$
$$
((p-s) \cdot s_{21} - s_1 \cdot s_2) \Delta u^{(r)} + ((p-s) \cdot s_{22} - s_2 \cdot s_2) \Delta v^{(r)} = (s-p) \cdot s_2,
$$

where $s = s(u^{(r)}, v^{(r)})$, $s_1 = \frac{\partial s}{\partial u}$, $s_2 = \frac{\partial s}{\partial v}$, $s_{11} = \frac{\partial^2 s}{\partial u^2}$, $s_{12} = s_{21} = \frac{\partial^2 s}{\partial u \partial v}$, $s_{22} = \frac{\partial^2 s}{\partial v^2}$ are partial derivatives of the radius vector of the surface at $u = u^{(r)}$ and $v = v^{(r)}$. The next approximation of the parameters of the point projection is equal to $u^{(r+1)} = u^{(r)} + \Delta u^{(r)}$ and $v^{(r+1)} = v^{(r)} + \Delta v^{(r)}$. The parameter refinement process is stopped when $|\Delta u^{(r)}|$ and $|\Delta v^{(r)}|$ at the next iteration are less than a specified value.

The projection of a point on some analytical surfaces can be found without using numerical methods. For example, to find the projection of a point on the surface of a circular cylinder, cone, sphere, or torus, it is necessary to translate the point being projected into the local coordinate system of the surface where it is easy to find the projection parameters.
3.3. Intersection Points of Curves

Let us find the intersection point of planar straight lines

$$ I_1(w_1) = p_1 + w_1 c_1 $$
$$ I_2(w_2) = p_2 + w_2 c_2 $$

(3.3.1)
(3.3.2)

Straight lines have a single intersection point if they are not parallel. Denote the unit normals to the straight lines $I_1(w_1)$ and $I_2(w_2)$ by $n_1$ and $n_2$. Let us recall that each bold italic Latin letter denotes the presence of two coordinates in two-dimensional space. If a tangent vector $c = [x \ y]^T$ to the curve has coordinates $x$ and $y$, then vector $n$ orthogonal to it has coordinates $-ky$ and $kx$, where $k = \frac{1}{\sqrt{x^2 + y^2}}$. Fig. 3.3.1 shows straight lines $I_1(w_1)$ and $I_2(w_2)$, normals to them, and a point of intersection $p$. It can be seen from the figure that for the intersection point the parameter of the second straight line can be found as the ratio of the projection of the vector $p_1 - p_2$ on the normal of the first straight line to the projection of the vector $c_2$ on the same normal.

![Diagram](image)

Fig. 3.3.1.

Thus, the parameters of the intersection point for the straight lines are equal to

$$ w_1 = \frac{n_2 \cdot (p_2 - p_1)}{n_2 \cdot c_1} $$
$$ w_2 = \frac{n_1 \cdot (p_1 - p_2)}{n_1 \cdot c_2} $$

(3.3.3)
(3.3.4)

The radius vector of the intersection point is obtained by inserting parameter (3.3.3) or (3.3.4) into the formula for the corresponding straight line:

$$ p = p_1 + \frac{n_2 \cdot (p_2 - p_1)}{n_2 \cdot c_1} c_1 = p_2 + \frac{n_1 \cdot (p_1 - p_2)}{n_1 \cdot c_2} c_2 $$
Suppose we are given planar segments

$$ l_1(t_1) = (1-t_1)p_1 + t_1q_1, \quad l_2(t_2) = (1-t_2)p_2 + t_2q_2, $$

constructed on points $p_1=[x_1\ y_1]^T, \ p_2=[x_2\ y_2]^T, \ q_1=[a_1\ b_1]^T,$ and $q_2=[a_2\ b_2]^T.$ The parameters of the intersection point can be found from the vector equation

$$
(1-t_1)p_1 + t_1q_1 = (1-t_2)p_2 + t_2q_2, $$

which is a system of two scalar equations:

$$
(x_1-a_1)t_1 - (x_2-a_2)t_2 = x_1 - x_2, $$
$$
(y_1-b_1)t_1 - (y_2-b_2)t_2 = y_1 - y_2. $$

If $(x_2-a_2)(y_1-b_1)-(x_1-a_1)(y_2-b_2)\neq 0,$ then according to Cramer's rule, the parameters of the intersection point are

$$ t_1 = \frac{(x_2-a_2)(y_1-y_2)-(x_1-x_2)(y_2-b_2)}{(x_2-a_2)(y_1-b_1)-(x_1-a_1)(y_2-b_2)}, $$
$$ t_2 = \frac{(x_1-a_1)(y_2-y_1)-(x_2-x_1)(y_1-b_1)}{(x_1-a_1)(y_2-b_2)-(x_2-a_2)(y_1-b_1)}. $$

Segments of the straight lines intersect if $0\leq t_1 \leq 1$ and $0\leq t_2 \leq 1;$ otherwise, continuations of the segments intersect.

Suppose it is required to find all intersection points of the planar curves whose radius vectors are described by the functions $c_1(t_1)$ and $c_2(t_2).$ At every point of intersection the following vector equation is satisfied:

$$ c_1(t_1) - c_2(t_2) = 0. $$ \hspace{1cm} (3.3.5)

The unknowns are the parameters of curves $t_1$ and $t_2.$ In general the system of equations is non-linear, and can be solved by iterative methods.

To find an initial approximation, we choose a set of trial points for each curve. For every combination of trial points, we construct tangent lines (3.3.1) and (3.3.2), where $p_1=c_1(t_1)$ and $p_2=c_2(t_2)$ are the trial points of the curves, and $c_1'=dc_1/dt_1$ and $c_2'=dc_2/dt_2$ are the derivatives of the curves at the trial points. Then, using formulas (3.3.3) and (3.3.4), we define parameters $w_1$ and $w_2$ of the tangent lines at their intersection point. Near the intersection point, parameters $w_1$ and $w_2$ approximately correspond to the increments of the parameters of the curves. Increments $w_1$ and $w_2$ are considered small if in the vicinity of the trial point of the curve, the curve can be approximated by the tangent line. If the increments are small, then $t_1^{(0)}=t_1+w_1$ and $t_2^{(0)}=t_2+w_2$ can be taken as an initial approximation when solving the system of equations (3.3.5).

The intersection points of some analytical curves can be found without using numerical methods. For example, solving the quadratic equation, one can find points of intersection of the straight line with second order curves.
The osculating points of curves $c_1(t_1)$ and $c_2(t_2)$ can be found by solving the system of equations

$$\begin{align*}
(c_1(t_1) - c_2(t_2)) \cdot \frac{dc_1}{dt_1} &= 0, \\
(c_2(t_2) - c_1(t_1)) \cdot \frac{dc_2}{dt_2} &= 0.
\end{align*}$$

Besides the intersection and the osculating points, the points at which the tangent lines are parallel to each other and the segment connecting the osculating points orthogonal to the tangent lines also satisfy this system.

Let us find the closest points of three-dimensional lines

$$\begin{align*}
c_1(t_1) &= p_1 + t_1d_1, \\
c_2(t_2) &= p_2 + t_2d_2.
\end{align*}$$

Each line is defined by the point $p_i$ and by the vector $d_i$, $i=1,2$. Let the parameters of the straight lines $w_1$ and $w_2$ correspond to the closest points. A segment connecting the closest points is orthogonal to both straight lines. Thus, for the desired points the following equalities must hold:

$$\begin{align*}
(p_1 + w_1d_1 - p_2 - w_2d_2) \cdot d_1 &= 0, \\
(p_1 + w_1d_1 - p_2 - w_2d_2) \cdot d_2 &= 0.
\end{align*}$$

If the lines are not parallel then this system of equations has a unique solution:

$$\begin{align*}
w_1 &= \frac{(p_2 - p_1) \cdot d_1a_{22} - (p_2 - p_1) \cdot d_2a_{12}}{a_{11}a_{22} - a_{12}a_{12}}, \\
w_2 &= \frac{(p_1 - p_2) \cdot d_2a_{11} - (p_1 - p_2) \cdot d_1a_{12}}{a_{11}a_{22} - a_{12}a_{12}},
\end{align*}$$

where $a_{11}=d_1'd_1$, $a_{22}=d_2'd_2$, $a_{12}=d_1'd_2$. If the straight lines intersect, then $w_1$ and $w_2$ correspond to their point of intersection. If the straight lines do not intersect, then $w_1$ and $w_2$ correspond to the nearest points of the straight lines.

To determine parameters $t_1$ and $t_2$ of the intersection points of the three-dimensional curves $c_1(t_1)$ and $c_2(t_2)$ we use the projection of the vector equation

$$c_1(t_1) - c_2(t_2) = 0$$

on the plane that is determined by the vectors tangent to curves $c_1'=dc_1/dt_1$ and $c_2'=dc_2/dt_2$. To do this we construct the local coordinate system with the origin at the point $0.5(c_1(t_1)+c_2(t_2))$ and basis vectors $i_1=c_1'$, $i_2=c_2'$, and $i_3=i_1\times i_2$ and translate the vector equation into this system. We seek the solution to the system of equations composed by equating the first two local coordinates of the points of the curve. In solving the system of equations by iterative methods it is better to construct a new local
coordinate system for every iteration. If the tangents to curve vectors $c_1$ and $c_2$ are parallel, then we use system of equations (3.3.6), in which planar curves are replaced by three-dimensional curves.

When determining the parameters of intersection of three-dimensional curves, we also obtain the points at which the tangent lines are orthogonal to the segment connecting the determined points besides the intersection and osculating points. After finding a solution, you should check that all three coordinates are equal for the determined points of the curve.

### 3.4. Intersection Points of a Surface and a Curve

Suppose it is required to find the intersection of a straight line (3.1.1) with a plane (3.2.1). If $c' \cdot m \neq 0$, where $m$ is the normal (3.2.2) to the plane, then the straight line is not parallel to the plane and the intersection point exists and is unique. The parameter of the straight line corresponding to the point of intersection of this line with the plane is calculated by the formula

$$
t_p = \frac{m \cdot (s_0 - c_0)}{m \cdot c'}.
$$

(3.4.1)

![Diagram](image)

Fig. 3.4.1.

Fig. 3.4.1 shows the straight line and the plane when viewed parallel to the plane. The numerator of the right-hand side of (3.4.1) includes the distance from a point of straight line $c_0$ to the plane, and the denominator includes the component of the derivative of the straight line normal to the plane. The ratio of these values gives the parameter of the straight line intersection with the plane. Inserting the (3.4.1) into the (3.1.1) yields the radius vector $p_s$ of the point of intersection of the straight line with the plane

$$
p_s = c_0 + c \frac{m \cdot (s_0 - c_0)}{m \cdot c'}.
$$
Then using formulas (3.2.3) and (3.2.4), we calculate the parameters of the plane corresponding to the point of intersection.

Determination of the parameters of the intersection of a straight line with a plane is used to search for initial approximations for the points of intersection of a surface with a curve. Suppose it is required to find all points of intersection of a surface with the radius vector described by vector function $s(u,v)$ with a curve with the radius vector described by vector function $c(t)$. At each point of intersection, the following vector equation must be satisfied:

$$s(u,v) - c(t) = 0,$$

which is a system of three scalar equations. The unknowns are three parameters—$u$, $v$, and $t$. Solving this system of equations yields parameters $u$, $v$, and $t$, using which, if necessary, you can calculate the points on the surface and on the curve. In general, the system of equations is non-linear and can be solved by iterative methods. There can be several points of intersection.

To find initial trial solutions, we choose a set of trial points on the surface and the curve. For each combination of trial points we perform the following test. Let the values of the parameters be $u_i$ and $v_i$ at the trial point of the surface, and the values of the parameters be $t_j$ at the trial point of the curve. Construct a tangent plane (3.2.1) at the trial point of the surface and a tangent line (3.1.1) at the trial point of the curve, where $s_0 = s(u_i,v_i)$, $c_0 = c(t_j)$, $s_1 = \frac{\partial s}{\partial u}$, and $s_2 = \frac{\partial s}{\partial v}$ at the trial point of the surface, with $c' = \frac{dc}{dt}$ at the trial point of the curve. If the trial points of the curve and the surface are regular and if the tangent line is not parallel to the tangent plane, then using the formulas (3.4.1), (3.2.3), and (3.2.4), we find parameter $t_p$ of the tangent line and parameters $u_p$ and $v_p$ of the tangent plane determining the point of their intersection. If the trial points are in the vicinity of the point of intersection of the curve and the surface, then values $u_p$ and $v_p$ approximately correspond to the increments of the parameters of the surface, and value $t_p$ approximately corresponds to the increment of the parameter of the curve.

![Diagram](image)

Fig. 3.4.2.

The increments $u_p$ and $v_p$ are considered small if the surface can be approximated by a tangent plane in the neighborhood of the surface point with parameters $u_i$ and $v_i$. Increments $t_p$ are considered small if the curve can be approximated by a tangent line in
the neighborhood of the point of the curve with parameters $t_i$. If the increments are small, then parameters $u^{(0)} = u_i + u_p, v^{(0)} = v_i + v_p,$ and $t^{(0)} = t_i + t_p$ can be taken as initial approximations to the solution of the system of equations (3.4.2). Fig. 3.4.2 shows a surface, its tangent plane, a curve, and its tangent line.

Osculating points of the curve and the surface can be found by solving a system of three equations:

$$
(s(u,v) - c(t)) \cdot \frac{\partial s}{\partial u} = 0,
$$

$$
(s(u,v) - c(t)) \cdot \frac{\partial s}{\partial v} = 0,
$$

$$
(s(u,v) - c(t)) \cdot \frac{dc}{dt} = 0.
$$

This system is also satisfied by a point where a tangent line is parallel to the tangent plane, and a segment connecting points of osculation is orthogonal to the tangent line and the tangent plane, beside the points of intersection and osculation.

### 3.5. Intersection Points of Three Surfaces

Suppose we are given three planes

$$
r(u,v) = r_0 + ur_1 + vr_2,
$$

$$
s(a,b) = s_0 + as_1 + bs_2,
$$

$$
q(x,y) = q_0 + xq_1 + yq_2,
$$

with unit normals $m_r, m_s,$ and $m_q,$ respectively. The planes have a unique intersection point if the mixed product of the normals is non-zero: $(m_r \times m_s) \cdot m_q \neq 0.$ Let the required point of intersection have a radius vector $p.$ Then vector $p - r_0$ is parallel to plane $r(u,v),$ vector $p - s_0$ is parallel to plane $s(a,b),$ and vector $p - q_0$ is parallel to plane $q(x,y).$ The following equalities are then satisfied:

$$
(p - r_0) \cdot m_r = 0, \quad (p - s_0) \cdot m_s = 0, \quad (p - q_0) \cdot m_q = 0.
$$

Denote the coordinates of point $p$ by $p_1, p_2,$ and $p_3,$ the components of the normal vector $m_r$ by $m_{1r}, m_{2r},$ and $m_{3r},$ the components of the normal vector $m_s$ by $n_{1s}, n_{2s},$ and $n_{3s},$ and the components of the normal vector $m_q$ by $l_{1q}, l_{2q},$ and $l_{3q}.$ Then the system of equations (3.5.1) takes the form

$$
m_{1r}p_1 + m_{2r}p_2 + m_{3r}p_3 = r_0 \cdot m_r,
$$

$$
n_{1s}p_1 + n_{2s}p_2 + n_{3s}p_3 = s_0 \cdot m_s,
$$

$$
l_{1q}p_1 + l_{2q}p_2 + l_{3q}p_3 = q_0 \cdot m_q.
$$
Solving this system of algebraic linear equations for $p_1, p_2,$ and $p_3$, we find the common point of the three planes. The parameters of the planes' intersection can be found by projecting point $p$ onto these planes by the method described above.

In the general case of an intersection of three surfaces $r(u,v)$, $s(a,b)$, and $q(x,y)$, each intersection point must satisfy the system of vector equations

$$
r(u,v) - q(x,y) = 0,
$$
$$
s(a,b) - q(x,y) = 0.
$$

This system of vector equations contains six scalar algebraic equations for six parameters of the surfaces, $u, v, a, b, x,$ and $y$.

To find an initial approximation of the solution, we select a set of trial points of the surface. For each combination of three trial points, we construct three tangent planes (3.5.1), where: $r_0 = r(u_i, v_i)$, $r_1 = \partial r / \partial u$, and $r_2 = \partial r / \partial v$ are calculated at trial point $[u_i, v_i]^T$ of surface $r(u,v)$; $s_0 = s(a_j, b_j)$, $s_1 = \partial s / \partial a$, and $s_2 = \partial s / \partial b$ are calculated at trial point $[a_j, b_j]^T$ of surface $s(a,b)$; and $q_0 = q(x_k, y_k)$, $q_1 = \partial q / \partial x$, and $q_2 = \partial q / \partial y$ are calculated at trial point $[x_k, y_k]^T$ of surface $q(x,y)$. Let us find the point of intersection of the three tangent planes and estimate the proximity of this point to the trial points, and thus the possibility using them trial points as the initial approximation.

### 3.6. Curves on Surfaces

A plane curve can be constructed using a two-dimensional curve

$$
c(t) = \begin{bmatrix} u(t) \\ v(t) \end{bmatrix}, \quad t_{\text{min}} \leq t \leq t_{\text{max}}
$$

and a local coordinate system in three-dimensional space. Let the origin of the local Cartesian coordinate system be located at point $p$, and let vectors $s_1, s_2,$ and $s_3$ be its basis vectors. Then the radius vector of the curve constructed in the plane of the first two basis vectors is calculated by the formula

$$
r(t) = p + u(t) s_1 + v(t) s_2.
$$

The plane curve has the same domain as the two-dimensional curve. The derivatives of the radius vector of the plane curve are calculated as the derivatives of a composite function:

$$
\frac{dr}{dt} = s_1 \frac{du}{dt} + s_2 \frac{dv}{dt},
$$
$$
\frac{d^2r}{dt^2} = s_1 \frac{d^2u}{dt^2} + s_2 \frac{d^2v}{dt^2},
$$
$$
\frac{d^3r}{dt^3} = s_1 \frac{d^3u}{dt^3} + s_2 \frac{d^3v}{dt^3}.
$$

A two-dimensional curve $c(t) = [u(t) \ v(t)]^T$ forms a plane curve in the parametric space of the plane (3.2.1).
$$ r(t) = s_0 + u(t) s_1 + v(t) s_2 $$

in three-dimensional space.

A surface curve is described by vector function (2.1.3); it is a combination of surface $s(u,v)$ and two-dimensional curve $c(t)=[u(t) \ v(t)]^T, t_{\text{min}} \leq t \leq t_{\text{max}}$, in the parametric space of this surface. The two-dimensional curve maps some part of the numerical axis onto the parametric space of the surface, and the surface maps the corresponding points into three-dimensional space. A surface curve is a three-dimensional curve; its radius vector is calculated by the formula

$$ r(t) = s(u(t),v(t)). $$

(3.6.1)

The surface curve has the same domain as the two-dimensional curve. Derivatives of the radius vector of the surface curve are calculated as the derivatives of a composite function:

$$ \frac{dr}{dt} = s_1 \frac{du}{dt} + s_2 \frac{dv}{dt}, $$

(3.6.2)

$$ \frac{d^2r}{dt^2} = s_{11} \left( \frac{du}{dt} \right)^2 + 2s_{12} \frac{du}{dt} \frac{dv}{dt} + s_{22} \left( \frac{dv}{dt} \right)^2 + s_1 \frac{d^2u}{dt^2} + s_2 \frac{d^2v}{dt^2}, $$

(3.6.3)

$$ \frac{d^3r}{dt^3} = s_{111} \left( \frac{du}{dt} \right)^3 + 3s_{112} \left( \frac{du}{dt} \right)^2 \frac{dv}{dt} + 3s_{122} \frac{du}{dt} \left( \frac{dv}{dt} \right)^2 + s_{222} \left( \frac{dv}{dt} \right)^3 + $$
$$ + 3s_{11} \frac{d^2u}{dt^2} \frac{du}{dt} + 3s_{12} \left( \frac{d^2u}{dt^2} \frac{dv}{dt} + \frac{d^2v}{dt^2} \frac{du}{dt} \right) + 3s_{22} \frac{d^2v}{dt^2} \frac{dv}{dt} + s_1 \frac{d^3u}{dt^3} + s_2 \frac{d^3v}{dt^3}, $$

(3.6.4)

and so on, where $s_1 = \frac{\partial s}{\partial u}, \ s_2 = \frac{\partial s}{\partial v}, \ s_1 = \frac{\partial s}{\partial u}, \ s_{11} = \frac{\partial^2 s}{\partial u^2}, \ s_{12} = \frac{\partial^2 s}{\partial u \partial v}, \ s_{22} = \frac{\partial^2 s}{\partial v^2}, \ s_{111} = \frac{\partial^3 s}{\partial u^3}, \ s_{112} = \frac{\partial^3 s}{\partial u^2 \partial v}, \ s_{122} = \frac{\partial^3 s}{\partial u \partial v^2}, \ s_{222} = \frac{\partial^3 s}{\partial v^3}$ are partial derivatives of the surface radius vector at point $[u(t) \ v(t)]^T$.

The surface curve is cyclic, if the two-dimensional curve is cyclic, or if the surface is cyclic with respect to one of the parameters and the two-dimensional curve passes through the points separated by the period of the surface with respect to the periodic parameter when another parameter is unchanged.

When planar point $[u \ v]^T$ is beyond the parametric domain of the surface, the radius vector $r(u,v)$ is calculated in accordance with the rules of construction of the extended surface.

Let the surface boundary $s(u,v)$ be described by $n$ two-dimensional contours $c_i(t)=[u_i(t) \ v_i(t)]^T, t_{\text{min}} \leq t \leq t_{\text{max}}, i=1,2,...,n$. In three-dimensional space, the boundary of this surface can be described by a set of surface curves, which are two-dimensional contours, or by three-dimensional closed composite curves whose segments are surface curves $c_i(t)=s(u_i(t),v_i(t))$.

A projection curve is a projection of a three-dimensional curve onto a surface. Suppose we are given a three-dimensional curve $c(t), t_{\text{min}} \leq t \leq t_{\text{max}}$, and a surface $s(u,v)$.
The two-dimensional curve $p(t) = [u(t) \ v(t)]^T$, each point $[u(w) \ v(w)]^T$ of which coincides with the projection of point $c(w)$ on the surface $s(u,v)$, is called a two-dimensional projection curve (Fig. 3.6.1). Together with the given surface $s(u,v)$, the two-dimensional projection curve $p(t)$ forms a surface curve (3.6.1)—a three-dimensional projection curve $s(u(t),v(t))$.

![Fig. 3.6.1.](image)

In general, it is not always possible to construct a two-dimensional curve $p(t)$; however, we may approximate it by a spline. To construct the spline, we choose a non-decreasing sequence of parameters $t_i, i=0,1,\ldots,n$, where $t_i < t_{i+1}, \ t_0 = t_{\text{min}},$ and $t_n = t_{\text{max}}$. For each point of the curve $c(t_i), i=0,1,\ldots,n$, we find parameters $u_i$ and $v_i$ of its projection on surface $s(u,v)$ and construct a two-dimensional spline $r(t)$ passing through points $p=[u_i, v_i]^T$ at parametric values $t=t_i, i=0,1,\ldots,n$. Spline $r(t)$ has the same parametric length as curve $c(t)$, and coincides with the projection curve at certain points. When such a spline exists, the point of the projection curve for some given parameter $w$ is found by the following algorithm: Compute the spline point $r(w)$ for the same parameter and use it as an initial approximation in the search for the projection of point $c(w)$ on surface $s(u,v)$.

The projection curve is composed of three objects: three-dimensional curve $c(t)$, the surface $s(u,v)$, and two-dimensional curve of initial approximations $r(t), t_{\text{min}} \leq t \leq t_{\text{max}}$. These objects, together with the algorithm of the projection of the point on the surface, make it possible to determine the points of the projection curve with any required accuracy. If $s(u,v)$ is a plane, you can determine the derivatives of the radius vector of the projection curve with the required accuracy.

A silhouette curve is a variation of a surface curve. Let there be given a surface $s(u,v)$ and a viewpoint $w$. A line passing through a viewpoint and a surface point is called a line of sight. The points at which a normal to the surface is orthogonal to a line of sight are located on curves called silhouette curves. When passing through a silhouette curve, a surface normal changes direction relative to the line of sight. The silhouette curve separates the visible and invisible part of the surface as seen from the viewpoint.

Fig. 3.6.2 shows silhouette curves of the surface of revolution. The location of a silhouette curve on the surface depends on the relative locations of the surface and a viewpoint. In general, a surface may have several silhouette curves. Each silhouette curve either is closed or ends at the surface boundary.

By definition, the points of a silhouette curve satisfy the equation

$$
i(u,v) \cdot m(u,v) = 0,
$$

(3.6.5)
where $m(u,v)$ is the normal to the surface $s(u,v)$, and $i(u,v) = s(u,v) - w$ is the direction vector of the line of sight. Viewpoint $w$ and vector $i(u,v)$ determine the line of sight for the considered point of the surface. If a viewpoint is located infinitely far from the surface, then the vector $i(u,v)$ does not depend on the parameters of the surface and is common to all points of the surface.

![Fig. 3.6.2.](image)

Equation (3.6.5) has two required parameters, $u$ and $v$. If one of the parameters is known, the other can be found from equation (3.6.5); that is, one of the parameters is a function of the other. To make the parameters equivalent we represent them as functions $u = u(t)$ and $v = v(t)$ of some common parameter $t$. The result of the solution of (3.6.5) is the surface curve $c(t) = s(u(t), v(t))$, which is a silhouette curve. In general, it is not always possible to find functions $u(t)$ and $v(t)$, so we approximate them by two-dimensional splines $r(t)$, $t_{\text{min}} \leq t \leq t_{\text{max}}$. The points of spline $r(t)$ are initial approximations for the iterative solutions of equation (3.6.5).

A silhouette curve is composed of three objects: the viewpoint $w$ or the direction vector of the line of sight $i$ (at an infinitely far viewpoint location); surface $s(u,v)$; and the two-dimensional curve of initial approximations $r(t)$. These objects, together with algorithm for solving equation (3.6.5), allow us to determine the points of a silhouette curve with any required accuracy.

We split the algorithm for constructing a silhouette curve into two steps: In the first step, we find the set of individual points of the silhouette curve; then in the second step, we construct the silhouette curve. To find the individual points of a silhouette curve, calculate dot product $i \cdot m$ at some selected points of the surface. If for some pair of adjacent points $i \cdot m$ changes sign, it means the surface passes through the silhouette curve. Taking the average values of these adjacent points as an initial approximation we find parameters $u$ and $v$ of the point of the silhouette curve by a numerical method. In this way we obtain a set of the individual points of the silhouette curves. These points are not connected with each other and may belong to different silhouette curves. It is important that there is at least one point of each silhouette curve in the set.

Next, take any point of the available set, and by moving from it to one side and then to the other in some increments, find the desired set of points of the silhouette curve point by point. The direction of motion is given by the vector
$$ t = \pm \frac{m_1 \times m}{|s_1|} \pm \frac{m_2 \times m}{|s_2|}, $$

where $m_1$ and $m_2$ are partial derivatives of the normal $m(u,v)$, and $s_1$ and $s_2$ are partial derivatives of the surface radius vector $s(u,v)$ with respect to parameters $u$ and $v$. The sign at term $(m_j \times m)/|s_j|, j=1,2$ coincides with the sign of the dot product $i'm_j, j=1,2$. The increment is calculated in accordance with the curvature of the surfaces at the current point. If

$$
\frac{|t \cdot r_1|}{|r_1|} > \frac{|t \cdot r_2|}{|r_2|},
$$

then give the increment to parameter $u$ and find the corresponding parameter of surface $v$. Otherwise, give the increment to parameter $v$ and find the corresponding parameter of surface $u$. Movement along the silhouette curve is stopped when we reach the edge of the surface, or when the line closes.

During construction of the points of the silhouette curve, we check whether the points of the set obtained in the beginning lie nearby. If the distance to any point of the set is commensurate with the current motion step, then remove this point from the set as being unnecessary. This way we obtain a sequence of points $p_i=[u_i, v_i]^T, i=0,1,2,...,n$ of one silhouette curve. In this case, the set of points obtained in the beginning does not contain any point of this silhouette curve. If points still remain in the set, then this surface has at least one more silhouette curve. Its set of points can be found by taking any other point from the set and repeating the abovementioned procedure.

With the help of the sequence of points, construct spline $r(t)$ passing through points $p=[u_i, v_i]^T$ at parametric values $t=t_i, i=0,1,...,n$. Having information about surface $s(u,v)$, viewpoint $w$, or the direction vector of the line of sight $l$, you can always find any other points of the line by the individual points of the silhouette curve located in their order. For example, to find a point lying between two given adjacent points of a silhouette curve, draw the plane perpendicular to the segment connecting the adjacent points and find a common point of the surface and the plane by finding the joint solution to the system of equations determining the intersection and equation (3.6.5).

Silhouette curves are used for construction of projections of surface $s(u,v)$ on a plane. The projection of a silhouette curve may have breaks and cuspidal points, but the silhouette curve itself does not have singular points, if these points do not exist on the surface in the area around the silhouette curve. The break points of the projection appear at the locations where the tangent line to the silhouette curve is parallel to the line of sight.

Fig. 3.6.3. Fig. 3.6.4.
Fig. 3.6.3 shows a projection of a silhouette curve of a torus when the viewpoint is located far away from the surface. Fig. 3.6.4, by contrast, shows a projection of a torus silhouette curve when the viewpoint is located at a finite distance from the torus surface.

### 3.7. Curves of Intersection of Surfaces

In general, it is impossible to operate separately with curves of intersection of surfaces and with the surfaces generating it; thus an **intersection curve** is described by two curves (3.6.1) on the intersecting surfaces. The curve of intersection of surfaces $r(u,v)$ and $s(a,b)$ is constructed by two curves, $r(u(t),v(t))$ and $s(a(t),b(t))$, and is written in the form

$$
c(t) = \begin{cases} 
r(u(t),v(t)) & t_{\text{min}} \leq t \leq t_{\text{max}} \\
s(a(t),b(t)) & 
\end{cases}
$$

(3.7.1)

The radius vector $c(t)$ of the intersection curve is calculated as the arithmetic average of the radius vectors of the points of the curves on the intersecting surfaces.

Curves $r(u(t),v(t))$ and $s(a(t),b(t))$ are subject to the following two rules.

**Rule 1.** Curves $r(u(t),v(t))$ and $s(a(t),b(t))$ have identical domains $t_{\text{min}} \leq t \leq t_{\text{max}}$.

**Rule 2.** Curves $r(u(t),v(t))$ and $s(a(t),b(t))$ have the same radius vector and derivatives at the same parameters; i.e., $r(u(t),v(t)) = s(a(t),b(t))$. In certain cases, approximate satisfaction of this equality is acceptable.

In special cases it is possible to find analytical functions $u(t), v(t), a(t),$ and $b(t)$ which satisfy the equality $r(u(t),v(t)) = s(a(t),b(t))$. Such intersection curves are called **ordinary**. In general, functions $u(t), v(t), a(t),$ and $b(t)$ are approximated by some splines coinciding with these functions at certain points. Such intersection curves are called **singular**. For singular curves, Rule 2 is satisfied only approximately; nevertheless, we always calculate the exact value of the radius vector of the intersection curve by solving the equation

$$
r(u,v) - s(a,b) = 0.
$$

(3.7.2)

For singular curves, approximations of functions $u(t), v(t), a(t),$ and $b(t)$ serve as initial approximations for solution of equation (3.7.2). Hereinafter, for intersection curves, we denote the functions that satisfy equation (3.7.2) or their approximations by $u(t), v(t), a(t),$ and $b(t)$.

Functions $u(t)$ and $v(t)$ form two-dimensional curves $c_r(t) = [u(t) \ v(t)]^T$ in the parametric space of surface $r(u,v)$, and functions $a(t)$ and $b(t)$ form two-dimensional curves $c_s(t) = [a(t) \ b(t)]^T$ in the parametric space of surface $s(a,b)$. Curves $c_r(t)$ and $c_s(t)$ are not limited by the domains of the surfaces and can go beyond them. Outside of the parametric domain, the radius vector of the surface is calculated in accordance with the rules of construction of the extended surface (2.15.1)–(2.15.3).

Let us find the line of intersection of planes
Let $r_3$ and $s_3$ be unit normals to the planes. The direction of the intersection line of the planes is determined by vector $z = r_3 \times s_3$. If the length of vector $z$ is non-zero, then the planes intersect; otherwise, they are parallel or coincide. Let us find a point on the intersection line of the intersecting planes. Construct vector $w = r_0 - s_0$ and calculate its projection parallel to the plane $s(a,b)$: $w' = w - s_3 (w \cdot s_3)$. Then determine the intersection point of the line passing through point $s_0$ in the direction of vector $w'$ intersecting with plane $r(u,v)$:

$$
p = s_0 + w' \frac{r_3 \cdot (r_0 - s_0)}{r_3 \cdot w'}.
$$

The planes intersect along the line

$$
l(t) = p + t z.
$$

The parameters of the surfaces corresponding to point $p$ are determined by the formulas

$$
u_p = \frac{r_1 \cdot (p - r_0)}{r_1 \cdot r_1}, \quad v_p = \frac{r_2 \cdot (p - r_0)}{r_2 \cdot r_2},
$$
$$
a_p = \frac{s_1 \cdot (p - s_0)}{s_1 \cdot s_1}, \quad b_p = \frac{s_2 \cdot (p - s_0)}{s_2 \cdot s_2},
$$

in case of orthogonality of pairs of vectors $r_1, r_2$ and $s_1, s_2$, or by formulas (3.2.3) and (3.2.4) in the general case. Similarly, we find the parameters for another point of the intersection line—for example point $q = p + t_q z$. Let parameters $u_q$ and $v_q$ correspond to point $q$ on plane $r(u,v)$, and parameters $a_q$ and $b_q$ correspond to the same point on plane $s(a,b)$. Functions

$$
u(t) = u_p(1-t) + u_q t, \quad v(t) = v_p(1-t) + v_q t,
$$
$$
a(t) = a_p(1-t) + a_q t, \quad b(t) = b_p(1-t) + b_q t
$$

are the solution of equation (3.7.2) and allow construction of the ordinary intersection curve of the planes (3.7.1).

Let us consider the special case of the intersection of an extrusion surface and a plane. Let surface (2.3.2) be obtained by extruding the curve on the plane $c(t) = w(x(t), y(t))$ formed by two-dimensional curve $c_w(t) = [x(t) \ y(t)]^T$, $l_{\text{min}} \leq t \leq l_{\text{max}}$ and plane $w(x,y) = p_0 + x_i i_1 + y_i i_2$. The extrusion surface is described by radius vector

$$
r(u,v) = p_0 + x(u) i_1 + y(u) i_2 + v d,
$$
$$
t_{\text{min}} \leq u \leq t_{\text{max}}, \quad v_{\text{min}} \leq v \leq v_{\text{max}}.
$$

The intersection curve of the extrusion surface and the plane $s(a,b) = q_0 + a j_1 + b j_2$ parallel to plane $w(x,y)$ is constructed from a transformed replica of curve $c_w(t)$ on plane $s(a,b)$.
and segment $c_r(t) = [t \ v_s]^T$ on surface $r(u,v)$. The value of the second parameter $v_s$ of surface $r(u,v)$ corresponding to the location of segment $c_r(t)$ is equal to

$$
v_s = \frac{(q_0 - p_0) \cdot d}{|d|^2}.
$$

The transformed replica of curve $c_w(t)$ on plane $s(a,b)$ is denoted by $c_s(t) = [a(t) \ b(t)]^T$. The replica of curve $c_w(t)$ must be transformed in accordance with the relative position of its basis vectors and the initial points of planes $s(a,b)$ and $w(x,y)$. This transformation is described by the equality:

$$
\begin{bmatrix} a(t) \\ b(t) \end{bmatrix} = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix} \begin{bmatrix} x(t) \\ y(t) \end{bmatrix} + \begin{bmatrix} a_1 \\ a_2 \end{bmatrix},
$$

where $a_{11} = \frac{j_1 \cdot i_1}{j_1 \cdot j_1}, \quad a_{12} = \frac{j_1 \cdot i_2}{j_1 \cdot j_1}, \quad a_{21} = \frac{j_2 \cdot i_1}{j_2 \cdot j_2}, \quad a_{22} = \frac{j_2 \cdot i_2}{j_2 \cdot j_2}, \quad a_1 = \frac{j_1 \cdot (p_0 - q_0)}{j_1 \cdot j_1}, \quad a_2 = \frac{j_2 \cdot (p_0 - q_0)}{j_2 \cdot j_2}$.

Segment $c_r(t)$ and curve $c_s(t)$ are located on different surfaces; they have the same parametric length $t_{\text{min}} \leq t \leq t_{\text{max}}$ and represent an ordinary curve of intersection

$$
c(t) = \begin{cases} r(t, v_s) \\ s(a(t), b(t)) \end{cases}
$$

of surface $r(u,v)$ and plane $s(a,b)$.

Similarly, we can construct curves of intersection of some other surfaces in the special case of their relative position; for example, the curve of intersection of the surface obtained by revolution of a curve in a plane about an axis that belongs to that plane and a plane passing through the axis of revolution. Another example: The intersection curve of a surface of revolution and a plane orthogonal to its axis of rotation is constructed by a circle on the plane and a segment on the surface.

In the general case, an intersection curve of surfaces is represented as a sequence of individual points of a curve. In this case, the pair of parameters $u_i, v_i$ and $a_i, b_i$ that obey equality (3.7.2) are called individual points. Arrange the sequences of individual points in the form of two curves in the parametric spaces of surfaces $r(u,v)$ and $s(a,b)$; for example, in the form of two-dimensional Hermite splines (1.3.10) passing through points $[u_i \ v_i]^T$ and $[a_i \ b_i]^T$ respectively at the parameter value of the intersection curve $t_i$, $i=0,1,2,\ldots,n$. The values of parameters $t_i$ corresponding to points $[u_i \ v_i]^T$ and $[a_i \ b_i]^T$ should not decrease. The change in parameter from one point to another is assumed to be proportional to the length of the intersection curve segment between the adjacent points. This parametrization of the intersection curve is close to the natural parametrization when the parameter is the length of the curve.
If you have a sequence of individual points of an intersection curve, you can always find any other point of the curve. Indeed, suppose parameters $u_1, v_1, a_1,$ and $b_1,$ and parameters $u_2, v_2, a_2,$ and $b_2,$ of the surfaces correspond to adjacent points $p_1$ and $p_2$ of the sequence of points of an intersection curve of surfaces $r(u,v)$ and $s(a,b).$ Let the parameter of intersection curve $t_1$ correspond to the first point, and the parameter of the intersection curve $t_2$ correspond to the second point. It is required to find a point of the intersection curve with parameter $t,$ where $t_1 < t < t_2.$ Construct the plane

$$
q(x,y) = p + x q_1 + y q_2,
$$

where $p = \frac{t_2 - t}{t_2 - t_1} p_1 + \frac{t - t_1}{t_2 - t_1} p_2,$ and vectors $q_1, q_2$ are orthogonal to the segment constructed from point $p_1$ to point $p_2,$ and are non-parallel (see Fig. 3.7.1).

![Fig. 3.7.1.](image)

Using an iterative methods, find the parameters of a point of intersection of surfaces $r(u,v)$ and $s(a,b)$ and plane $q(x,y)$ from the system of six equations in vector form:

$$
r(u,v) - q(x,y) = 0,
$$
$$
s(a,b) - q(x,y) = 0.
$$

As initial approximations, take the parameters

$$
u^{(0)} = \frac{t_2 - t}{t_2 - t_1} u_1 + \frac{t - t_1}{t_2 - t_1} u_2,
$$
$$
v^{(0)} = \frac{t_2 - t}{t_2 - t_1} v_1 + \frac{t - t_1}{t_2 - t_1} v_2,
$$
$$
a^{(0)} = \frac{t_2 - t}{t_2 - t_1} a_1 + \frac{t - t_1}{t_2 - t_1} a_2,
$$
$$
b^{(0)} = \frac{t_2 - t}{t_2 - t_1} b_1 + \frac{t - t_1}{t_2 - t_1} b_2,
$$
$$
x^{(0)} = 0,
$$
$$
y^{(0)} = 0.
$$

The resultant parameters $u, v, a,$ and $b$ define the required point of intersection. Thus, the sequence of points $[u_i, v_i]^T$ and $[a_i, b_i]^T$ allows us to find any other point of the intersection curve of the surfaces $r(u,v)$ and $s(a,b).$
3.8. An Algorithm to Construct Intersection Curves

Two surfaces may intersect across multiple curves. Let our goal be to construct all the curves of intersection that are at least partially owned by the parametric domain of both surfaces. Fig. 3.8.1 illustrates an example of two surfaces intersecting along two curves.

![Fig. 3.8.1.](image)

Vector equation (3.7.2) contains three scalar equations for coordinates of the radius vectors of the surfaces and four required parameters: $u, v, a,$ and $b$. If one of the four parameters is determined, the other three can be found from system of equations (3.7.2). This is the basis for the algorithm for construction of the intersection curve of the surfaces. We split the algorithm into two steps.

In the first step, find the set of individual points of the intersection curves by moving along the surfaces and investigating their proximity (see Fig. 3.8.2). The points from the set obtained in the first step are not connected to each other and may belong to different curves of intersection. It is important that each of the intersection curves contributes at least one point to the set.

In the second step, we take any point of the available set and find point-by-point the required sequence of points of the intersection curve by moving from the selected point to one side and then to the other side with some step. The direction of motion is given by the cross product of the normals to the surfaces. The step of motion is calculated in accordance with the curvature of the surfaces at the current point. Movement along the intersection curve is stopped when we reach the edge of one of the surfaces or when the line closes; i.e., the new point is located at a distance equal to the current step from the initial point. During the motion, we check if there are any points from the set obtained in the first step near to the path of motion. For this purpose, we calculate the distance from the current point of the intersection curve to each point of the set obtained in the first step along the path. If the calculated distance to any point in the set is commensurate with the current motion step, then this point is removed from the set as unnecessary. We thus obtain the sequence of individual points $[u_i, v_i]^T$ and $[a_i, b_i]^T$, $i=0,1,2,...,n$ of one intersection curve (see Fig. 3.8.3).
Construct two two-dimensional splines passing through points $[u_i, v_i]^T$ and $[a_i, b_i]^T$ in the parametric space of surfaces $r(u,v)$ and $s(a,b)$ (see Fig. 3.8.4). Now the set of points obtained in the first step does not contain any points of the intersection curve. If the points still remain in the set, then these surfaces have at least one more curve of intersection. The sequence of its points can be found by taking any other point from the set and repeating the second-step procedure (see Fig. 3.8.5). The construction of the curves is finished when no points remain in the set.

The first step is the most difficult step. To determine the initial points of intersection you can use various strategies, whose basic idea is a representation of every surface by a set of simple objects. These objects are then used to make a decision about initiating the iterative process for solving system of equations (3.7.2) with one fixed parameter. The simple objects can be plane patches, line segments, circumscribing polyhedra of the surface patches, or other items. To speed up the process, the objects can be sorted one way or another. Thus, we obtain a set of points belonging in the general case to different intersection curves of the given surfaces. To construct each intersection curve, we need to choose one particular point from the set.

The second step—despite its cumbersome description—is faster than the first step. Let us select from the set obtained in the first step any point of intersection of the surfaces. Suppose parameters of this point are $u_k$ and $v_k$ on the first surface, and the parameters are $a_k$ and $b_k$ on the second surface. Construct normals to surfaces $m_r(u_k, v_k)$ and $m_s(a_k, b_k)$. The intersection curve at each point is orthogonal to the normals of both surfaces; thus, the intersection curve is parallel to vector $t = m_r(u_k, v_k) \times m_s(a_k, b_k)$. Choose
the positive direction of vector $t$ as the direction of movement to the next point on the intersection curve. Next we define a possible displacement step for each of the four parameters $\Delta u, \Delta v, \Delta a,$ and $\Delta b$ from the condition that normals to the surfaces deviate by an angle that does not exceed a specified value $\Delta \alpha$. A possible displacement step is calculated by the formulas

$$
\Delta u = \frac{\Delta \alpha | r_1 |}{m_r \cdot r_1}, \quad \Delta v = \frac{\Delta \alpha | r_2 |}{m_r \cdot r_2}, \quad \Delta a = \frac{\Delta \alpha | s_1 |}{m_s \cdot s_1}, \quad \Delta b = \frac{\Delta \alpha | s_2 |}{m_s \cdot s_2},
$$

where $r_1 = \frac{\partial r}{\partial u}, \quad r_2 = \frac{\partial r}{\partial v}, \quad r_{11} = \frac{\partial^2 r}{\partial u^2}, \quad r_{22} = \frac{\partial^2 r}{\partial v^2}, \quad s_1 = \frac{\partial s}{\partial a}, \quad s_2 = \frac{\partial s}{\partial b}, \quad s_{11} = \frac{\partial^2 s}{\partial a^2}, \quad s_{22} = \frac{\partial^2 s}{\partial b^2}$ are derivatives at the point with parameters $u_k, v_k$ and $a_k, b_k$. If we increase one of the parameters and fix it, then we can find other parameters from system of equations (3.7.2). It is important that the absolute value of the change of each parameter does not exceed the determined possible steps. As a fixed parameter that will be given an increment, choose the parameter along which the direction of motion is closer to the direction of the intersection curve—i.e., has a smaller angle with vector $t$.

Fig. 3.8.6 shows the starting point $p_k = r(u_k, v_k) = s(a_k, b_k)$, the vectors of the derivatives $r_1, r_2, s_1,$ and $s_2$, and the displacement sphere, inside of which the increments of all the parameters do not exceed $\Delta u, \Delta v, \Delta a,$ and $\Delta b$ respectively. The next point of the intersection curve should not go beyond the displacement sphere. Radius $r_0$ of the displacement sphere is equal to the projection of vectors $\Delta ur_1, \Delta vr_2, \Delta as_1,$ and $\Delta bs_2$ on vector $t$ that is smallest in absolute value:

$$
r_0 = \min(|\Delta ur_1 \cdot t|, |\Delta vr_2 \cdot t|, |\Delta as_1 \cdot t|, |\Delta bs_2 \cdot t|) \frac{1}{|t|}.
$$

The zero projections of the vectors $\Delta ur_1, \Delta vr_2, \Delta as_1,$ and $\Delta bs_2$ on vector $t$ are ignored. For the next point of the intersection curve, the following parameter values are taken as initial approximations:
$$ u_{k+1}^{(0)} = u_k + r_0 \frac{t \cdot r_1}{|t|(r_1 \cdot r_1)}, \quad v_{k+1}^{(0)} = v_k + r_0 \frac{t \cdot r_2}{|t|(r_2 \cdot r_2)}, $$
$$ a_{k+1}^{(0)} = a_k + r_0 \frac{t \cdot s_1}{|t|(s_1 \cdot s_1)}, \quad b_{k+1}^{(0)} = b_k + r_0 \frac{t \cdot s_2}{|t|(s_2 \cdot s_2)}. $$

We fix the parameter whose derivative has the angle smallest in absolute value to the direction of the intersection curve. Next, the solution of system of equations (3.7.2), with the fixed parameter considered to be known and unchanging, yields the remaining three parameters. Thus, we find parameters $u_{k+1}$ and $v_{k+1}$ of the first surface and parameters $a_{k+1}$ and $b_{k+1}$ of the second surface for the next point of the intersection curve. We continue this process until the edge of one of the surfaces is reached or we find ourselves near the starting point.

If during the movement we find ourselves near the starting point, the curve of intersection is cyclic closed. The proximity of the points is determined by steps $\Delta u, \Delta v, \Delta a,$ and $\Delta b$.

If during the motion we reach the edge of one of the surfaces, then after determining the end-point of the intersection curve we continue to move and search for the parameters of the intersection curve in the other direction from the starting point—that is, in the direction opposite to the direction of vector $t$. Such a curve cannot be cyclic closed, so we continue to move until the parameters of another endpoint of the surface intersection curve are found.

If the intersection curve passes through an osculating point of the surfaces, then the surfaces have collinear normals at this point. The matrix of linearized system of equations (3.7.2) has a non-zero determinant at this point, and it is impossible to find the parameters of the osculating point of the surfaces from this system of equations. The parameters of the osculating point of the surfaces can be found solving the system of equations

$$
(r(u,v) - s(a,b)) \cdot \frac{\partial r}{\partial u} = 0,
$$
$$
(r(u,v) - s(a,b)) \cdot \frac{\partial r}{\partial v} = 0,
$$
$$
(s(a,b) - r(u,v)) \cdot \frac{\partial s}{\partial a} = 0,
$$
$$
(s(a,b) - r(u,v)) \cdot \frac{\partial s}{\partial b} = 0.
$$

It is not only the osculating point that satisfies this system, but also other points at which the tangent planes to the surfaces are parallel to each other and orthogonal to the line connecting the osculating points. Therefore, after solving the system of equations, we should verify that the obtained points are the osculating points.
3.9. Fillet Surfaces

Joining surfaces blend the transition from one surface to another at the location of their intersection. These surfaces are also known as fillet and chamfer surfaces. Joining surfaces are swept surfaces of varying generators along the two guide curves.

Let there be two intersecting surfaces (including, possibly, extension surfaces). Near the intersection curve the space is divided by the surfaces into four sectors. Surface normals and perpendiculars constructed from a surface to the sector points may have coinciding or opposite directions. Suppose that in the first sector perpendiculars constructed from the surface to points of the sector coincide with normals to both surfaces. In the second sector, perpendiculars constructed from the first surface to points of the sector coincide with normals to the first surface, and perpendiculars constructed from the second surface to points of the sector are opposite to the direction of the normal to the second surface. In the third sector the perpendiculars constructed from the surfaces to points of the sector are opposite in direction to the normals to both surfaces. In the fourth sector the perpendicular constructed from the first surface to points of the sector has its direction opposite to the direction of the first surface normal and the perpendicular constructed from the second surface to points of the sector coincides with the second surface normal.

A fillet surface can be obtained by sweeping an osculating sphere along two surfaces being joined. The sphere is swept along an intersection curve of the surfaces in one of the four sectors mentioned above. The fillet surface is located between the osculating curve of the sphere and the planes.

Suppose it is required to construct a fillet surface between surfaces $r(u,v)$ and $s(a,b)$. We represent the fillet surface in the form of a rational surface (2.4.5) constructed on three curves. To do this construct the osculating curves of the sphere and surfaces $c_r(t)$ and $c_s(t)$. The points of the third curve $c(t)$ must be located on the intersection of three planes: two planes osculating to the joining surfaces at points $c_r(t)$ and $c_s(t)$, and the plane passing through the osculating points and the center of the sphere. Curves $c_r(t)$, $c_s(t)$, and $c(t)$ must have identical parametric length. The radius vectors of curves $c_r(t)$ and $c_s(t)$ must specify the osculating points of the sphere corresponding to each other.

Curves $c_r(t)$ and $c_s(t)$ are called reference curves, and the curve $c(t)$ is called an average curve. A fillet surface is described by the function

$$
q(t,z) = \frac{(1-z)^2 c_r(t) + 2(1-z)zw(t)c(t) + z^2 c_s(t)}{(1-z)^2 + 2(1-z)zw(t) + z^2},
$$

where $w(t) = \cos\left(\frac{\alpha}{2}\right)$ is the weight of the points of the average curve, and $\alpha$ is the angle between the normals and the surfaces being joined. In the general case, angle $\alpha$ is a function of the first parameter of the fillet surface. The first parameter of the fillet surface (3.9.1) coincides with the parameter of curves $c_r(t)$, $c_s(t)$, and $c(t)$. When the second parameter changes while the first parameter of the fillet surface is fixed, the
movement occurs along a circular arc. This circular arc is represented in the form of a rational curve (1.5.10).

The extensions of the normals to the surfaces at the osculating points intersect at the center of the sweeping sphere. The parameters of the osculating points of the sphere—and hence, the curves $c_r(t)$ and $c_s(t)$—are related by the equation

$$
r(u,v) + \rho_r m_r(u,v) = s(a,b) + \rho_s m_s(a,b),
$$

(3.9.2)

where $m_r(u,v)$ and $m_s(a,b)$ are normals to surfaces $r(u,v)$ and $s(a,b)$ at the osculating points, and $\rho_r$ and $\rho_s$ are the lengths of the projections of vectors constructed from the osculating points to the center of the sphere on each normal, respectively. Values $\rho_r$ and $\rho_s$ are equal in their absolute value to the radius of the sphere $\rho$, but have signs corresponding to one of the mentioned sectors. Fig. 3.9.1 shows a section of surfaces $r(u,v)$ and $s(a,b)$ and the sphere by the plane passing through the osculating points and the center of the sphere.

![Diagram](image)

Fig. 3.9.1.

Three scalar equations (3.9.2) written in coordinate form contain four unknown parameters, $u, v, a,$ and $b$. If one of the four parameters is determined, the other three can be found from system of equations (3.9.2). Construction of a fillet surface using equation (3.9.2) is similar to the problem of constructing an intersection curve of surfaces. In both cases, the resultant solution is expressed as functions $u(t), v(t), a(t),$ and $b(t)$, specifying two surface curves, $c_r(t) = r(u(t), v(t))$ and $c_s(t) = s(a(t), b(t))$. Functions $u(t)$ and $v(t)$ form two-dimensional curve $c_r(t) = [u(t) \ v(t)]^T$ in the parametric space of surface $r(u,v)$, and functions $a(t)$ and $b(t)$ form two-dimensional curve $c_s(t) = [a(t) \ b(t)]^T$ in the parametric space of surface $s(a,b)$. Curves $c_r(t)$ and $c_s(t)$ are not limited to the domain of the surfaces and can go beyond them. Outside the parametric domain, the radius vector of the surface is calculated in accordance with the rules of construction for the extended surface (2.15.1)–(2.15.3).

In special cases it is possible to find analytical functions $u(t), v(t), a(t),$ and $b(t)$, for which equation (3.9.2) holds. For example, when joining two planes, the angle $\alpha$ between the normal to the planes does not change, functions $u(t), v(t), a(t),$ and $b(t)$ are
linea, r and average curve $c(t)$ coincides with the intersection line of the surfaces being joined. Similarly, we can find analytical functions $u(t), v(t), a(t),$ and $b(t)$ when joining a cylindrical surface and a plane orthogonal or parallel to its axis, when joining cylindrical and conical surfaces, torus surfaces, and surfaces of revolution with the same axes. In special cases, you should use an analytical surface. Specifically, when joining two planes, surface (3.9.1) should be replaced by a cylindrical surface, and when joining two surfaces of revolution with the same axes, surface (3.9.1) should be replaced by the surface of a torus.

In general, when joining two arbitrary surfaces, two-dimensional curves $c_r(t)$ and $c_s(t)$ are represented in the form of splines passing through points $[u_i, v_i]^T$ and $[a_i, b_i]^T$ at parametric values $t_i, i=0,1,2,...,n$. Parameters $u_i, v_i, a_i, b_i, i=0,1,2,...,n$ approximate functions $u(t), v(t), a(t),$ and $b(t),$ and equation (3.9.2) is satisfied by them. The variation of parameter $t_{i+1}-t_i$ when moving from one point to the next is set to be proportional to the average length of the segment of three-dimensional curve $c_r(t)$ and $c_s(t)$ between adjacent points.

If during the construction of surface (3.9.1) we have a curve of intersection of surfaces $c_0(s),$ then equation (3.9.2) can be supplemented by the equation

$$
\left( c_0(s) - \frac{1}{2} (r(u,v) + \rho_r m_r(u,v) + s(a,b) + \rho_s m_s(a,b)) \right) \cdot \frac{dc_0}{ds} = 0,
$$

and the search for parameters $u_i, v_i, a_i,$ and $b_i$ is performed by solving the system of four equations for four unknowns, moving with a step along the intersection curve.

The average curve $c(t)$ and the weight function $w(t)$ are calculated using reference curves $c_r(t)$ and $c_s(t)$. The current value of the weight function is the cosine of half the angle between vectors $\rho_r m_r$ and $\rho_s m_s$. The cosine of the angle between these vectors is their dot product divided by the product of the lengths of the vectors:

$$
\cos \alpha = \frac{\rho_r m_r \cdot m_s \rho_s}{\rho^2}.
$$

Using the formula $2\cos^2(\alpha/2)=1+\cos \alpha$ we obtain the function of the weights of corresponding points of the average curve

$$
w(t) = \cos(\alpha/2) = \frac{1}{\sqrt{2}} \sqrt{1 + \frac{(\rho_r m_r \cdot m_s \rho_s)}{\rho^2}}.
$$

(3.9.3)

For known normals $m_r$ and $m_s$ at the points of reference curves and the function of weights, the radius vector of the average curve is computed by the formula

$$
c(t) = \frac{1}{2} (c_r(t) + \rho_r m_r + c_s(t) + \rho_s m_s) - \frac{1}{2} \frac{\rho_r m_r + \rho_s m_s}{\cos^2(\alpha/2)} =
$$

$$
= \frac{1}{2} \left( c_r(t) + c_s(t) - (1-w^2) \frac{\rho_r m_r + \rho_s m_s}{w^2} \right).
$$

(3.9.4)
If reference curves $c_r(t)$ and $c_s(t)$ are cyclic closed, fillet surface (3.9.1) is also cyclic closed with respect to the first parameter. Fig. 3.9.2 shows a fillet surface in the general case.

![Fig. 3.9.2.](image)

Suppose it is required to construct a **variable radius fillet surface**. This requires a surface-intersection curve. The values of fillet radii $\rho_r = \rho_r(s)$ and $\rho_s = \rho_s(s)$ are assumed to be functions of the arc length $s$ of intersection curve $c_0(s)$ of the joining surfaces. In this case, the sweeping sphere has a variable radius. Moreover, the position of the center of the sphere is related to a point on the curve of intersection. Let us locate the center of the sweeping sphere in the normal plane of the intersection curve of the joining surfaces. The normal plane is orthogonal to the tangent vector of the curve. The parameters of the osculating points of the sphere are related by a system of equations:

$$
r(u,v) + \rho_r(s)m_r(u,v) = s(a,b) + \rho_s(s)m_s(a,b),
$$

$$
\left( c_0(s) - \frac{1}{2} \left( r(u,v) + \rho_r(s)m_r(u,v) + s(a,b) + \rho_s(s)m_s(a,b) \right) \right) \cdot \frac{dc_0}{ds} = 0. \tag{3.9.5}
$$

These equations contain four scalar equations for the four required parameters $u, v, a,$ and $b$. The parameter $s$ of the intersection curve is known. Let us calculate radii $\rho_r(s)$ and $\rho_s(s)$, point $c_0(s)$, and the tangent vector of the curve at this point $c_0'(s)$ at the current parameter $s$. Solving system of equations (3.9.5) yields the osculating parameters $u_i, v_i, a_i,$ and $b_i$ of the sweeping sphere and the surface at the current position. Using the sequence of obtained points, let us construct the reference curves, average curve, the function of weights of corresponding points of the average curve, and the function of radii depending on the first parameter of the joining surface. Surface (3.9.1) constructed from these data has a variable fillet radius.

Fig. 3.9.3 shows an example of fillet surfaces of variable radius.

![Fig. 3.9.3.](image)
A keep edge fillet surface is constructed when it is required that the reference curves do not go beyond the joining surfaces. When one of the reference curves reaches the edge of a joining surface, it is required that from that point onwards the reference curve passes along the surface boundary. In these cases it is possible to construct the surface obtained by motion of the sphere osculating with one surface and abutting against the boundary edge of the other surface. A keep edge fillet surface is shown in Fig. 3.9.4.

For surface (3.9.1), let the boundary of surface $s(a,b)$ be closer to the intersection curve of the joining surfaces than reference curve $c_r(t)$. Let this part of the boundary be described by curve $h(s)$. To construct the reference curve $c_r(t)=r(u(t),v(t))$, we use the following system of equations instead of system of equations (3.9.2):

$$
| r(u,v) + p_r m_r(u,v) - h(s) | = | p_r |,
$$

$$
(r(u,v) + p_r m_r(u,v) - h(s)) \cdot \frac{dh}{ds} = 0.
$$

(3.9.6)

Parameters $u$ and $v$ are the unknowns. When moving along the section of the boundary $h(s)$, parameter $s$ is known. The result of solving system of equations (3.9.6) is the curve $[u(s) \ v(s)]^T$ on surface $r(u,v)$. It must be consistent with curve $h(s)$.

Using two reference curves, $c_r(s)=r(u(s),v(s))$ and $h(s)$, we construct the fillet surface

$$
q(s,z) = \frac{(1-z)^2 c_r(s) + 2(1-z)zw(s)c(s) + z^2 h(s)}{(1-z)^2 + 2(1-z)zw(s) + z^2},
$$

$s_{\text{min}} \leq s \leq s_{\text{max}}, \quad 0 \leq z \leq 1,$

passing through edge $h(s)$. The average curve $c(s)$ and the weight function of its points $w(s)$ are constructed using formulas (3.9.4) and (3.9.3), where vector $p_r m_r$ is replaced by the vector

$$
p_s m_s = -h(s) + r(u,v) + p_r m_r(u,v).
$$

A fillet surface by chord is a form of surface (3.9.1) in which the distance between reference curves $c_r(t)$ and $c_s(t)$ (a chord of the arc along parameter $v$) is equal
to a given value $h$. To construct the reference curves, we use the following system of equations instead of system of equations (3.9.5):

$$ r(u,v) + \rho_r m_r(u,v) = s(a,b) + \rho_s m_s(a,b), $$

$$ \left( c_0(s) - \frac{1}{2} (r(u,v) + \rho_r m_r(u,v) + s(a,b) + \rho_s m_s(a,b)) \right) \cdot \frac{dc_0}{ds} = 0, $$

$$ |r(u,v) - s(a,b)| = h. $$

This system contains five scalar equations for the five unknown parameters $u$, $v$, $a$, $b$, and $\rho = |\rho_r| = |\rho_s|$. Fig. 3.9.5 shows a fillet surface by chord, and Fig. 3.9.6 shows a fillet surface with constant radius for comparison.

Consider the section of fillet surface (3.9.1) for some fixed value $t$ of the first parameter. Let $p_0 = c_r(t)$, $p_1 = c(t)$, $p_2 = c_s(t)$. Then the section of surface (3.9.1) is described by the radius vector

$$ q(z) = \frac{(1-z)^2 p_0 + 2(1-z)zw p_1 + z^2 p_2}{(1-z)^2 + 2(1-z)zw + z^2}, $$

which coincides with (1.5.10). A section of a fillet surface with a fixed first parameter is shown in Fig. 3.9.7.
The parametrization of curve (1.5.10) is not uniform. Due to this, the ratio of the length of some part of an arc of the curve to the parametric length of the same part of an arc is not constant. Let us see how to obtain a uniform surface parameterization with respect to the second parameter.

Equate the right-hand sides of (1.5.6) and (1.5.9) for $z_1$:

$$z_1 = \frac{u_1}{1 - u_1}, \quad z_1 = \frac{1}{w} \frac{1 - v}{v}.$$

From the resulting equality, find the value $1 - u_1$:

$$1 - u_1 = \frac{vw}{1 - v + vw}.$$

The length of segment $|p_0p_1|$ is equal to

$$l = p \cdot \tan \frac{\alpha}{2} = p \frac{\sqrt{1-w^2}}{w},$$

where $p$ is the fillet radius, $\alpha$ is angle $p_0op_2$, and $w$ is the cosine of the half-angle $p_0op_2$. The length of segment $|p_0u_1|$ is proportional to $1 - u_1$ and is equal to

$$l_1 = l(1 - u_1) = p \frac{\sqrt{1-w^2}}{w} \frac{zw}{1 - z + zw}.$$

Dividing $l_1$ by $p$, we obtain the tangent of half-angle $p_0oq$:

$$\tan \frac{\beta}{2} = \frac{z\sqrt{1-w^2}}{1 - z + zw}.$$

We now introduce a new parameter $x$, $0 \leq x \leq 1$, equal to the ratio of the current angle $\beta$ to the full arc angle $\alpha$. Then the last equality takes the form

$$\tan \left( \frac{\alpha}{2} x \right) = \frac{z\sqrt{1-w^2}}{1 - z + zw}.$$

We solve the last equation with respect to the parameter of the surface $z$ and obtain the function
$$ z(x) = \frac{\tan\left(\frac{\alpha}{2} x\right)}{(1-w)\tan\left(\frac{\alpha}{2} x\right) + \sqrt{1-w^2}}. $$
(3.9.9)

We replace parameter $z$ in formula (3.9.8) by parameter $x$ using function $z(x)$ (3.9.9) and obtain the formula

$$ q(t,x) = \frac{(1-z(x))^2 c_r(t) + 2(1-z(x))z(x)w(t)c(t) + (z(x))^2 c_s(t)}{(1-z(x))^2 + 2(1-z(x))z(x)w(t) + (z(x))^2}, $$

for the radius vector of a fillet surface with uniform parameterization with respect to the second parameter.

There are many ways to blend two surfaces. If in equations (3.9.2) or (3.9.5) the parameters of the absolute values of radii $\rho_r$ and $\rho_s$ are not equal, then we obtain a surface that can be called an elliptic fillet surface (Fig. 3.9.8).

Indeed, if the joining surfaces intersect at a right angle, lines $q(\text{const},v)$ of the surface section (3.9.1) are arcs of ellipses. In general, you can always calculate the parameters of radii $\rho_r(t)$ and $\rho_s(t)$, so that the fillet surface at section $q(\text{const},v)$ is the arc of an ellipse.

When substituting the constant weight function $w(t)=1$ into surface (3.9.1) we obtain a parabolic fillet surface:

$$ q(t,z) = \frac{(1-z)^2 c_r(t) + 2(1-z)zc(t) + z^2 c_s(t)}{(1-z)^2 + 2(1-z)z + z^2}, $$

Using weight functions different from (3.9.3) for surface (3.9.1) you can also obtain various joining surfaces. When substituting the constant weight function $w(t)>1$ we obtain a hyperbolic fillet surface.
3.10. Chamfer Surfaces

Along with the blending of joining surfaces it is sometimes required to construct fillet surfaces in the form of chamfers. A chamfer surface is constructed similarly to a fillet surface.

Assume there are two intersecting surfaces described by radius vectors $r(u,v)$ and $s(a,b)$. In the general case, a chamfer surface is represented in the form of a ruled surface

$$
q(t,z) = (1-z) c_r(t) + z c_s(t),
$$

\( t_{\text{min}} \leq t \leq t_{\text{max}}, \quad 0 \leq z \leq 1, \tag{3.10.1} $$

constructed on reference curves $c_r(t) = r(u(t), v(t))$ and $c_s(t) = s(a(t), b(t))$. Functions $u(t), v(t), a(t),$ and $b(t)$ forming two-dimensional curve $c_r(t) = [u(t) \ v(t)]^T$ in the parametric space of surface $r(u,v)$ and two-dimensional curve $c_s(t) = [a(t) \ b(t)]^T$ in the parametric space of the surface $s(a,b)$ are found by solving the vector equation

$$
r(u,v) + d_r t_r(u,v) = s(a,b) + d_s t_s(a,b), \tag{3.10.2} $$

where $d_r$ and $d_s$ are the distances from the reference points of the curve to the points of intersection of the tangent planes, and

$$
t_r(u,v) = \pm \frac{m_r \times (m_r \times m_s)}{|m_r \times m_s|} \quad \text{and} \quad t_s(a,b) = \mp \frac{m_s \times (m_s \times m_r)}{|m_s \times m_r|}
$$

are vectors lying in the planes tangent to surfaces $r(u,v)$ and $s(a,b)$, orthogonal to reference curves $c_r(t)$ and $c_s(t)$. Fig. 3.10.1 shows a section of surfaces $r(u,v), s(a,b)$ by the plane orthogonal to the intersection line of the tangent planes to surfaces $r(u,v)$ and $s(a,b)$ at the considered points.

The signs of $d_r$ and $d_s$ specify the sector to which the chamfer surface belongs. If the surfaces are flat and orthogonal to each other in the domain of intersection, then the absolute values $d_r$ and $d_s$ are equal to catheti of the chamfer.
Three scalar equations (3.10.2) written in coordinate form contain four unknown parameters $u, v, a,$ and $b$. If one of the four parameters is determined, the other three can be found from system of equations (3.10.2). When intersection line $c_0(s)$ of surfaces $r(u,v)$ and $s(a,b)$ exists, equation (3.10.2) can be supplemented by the equation

$$
\left( c_0(s) - \frac{1}{2} (r(u,v) + d_r t_r(u,v) + s(a,b) + d_s t_s(a,b)) \right) \cdot \frac{dc_0}{ds} = 0 .
$$

The resulting system contains four equations for four parameters: $u, v, a,$ and $b$. In this system quantities $d_r$ and $d_s$ can be made variables by making them dependent on the arc length $s$ of the curve $c_0(s)$: $d_r = d_r(s), d_s = d_s(s)$; then (3.10.1) describes a chamfer surface with variable catheti.

Fig. 3.10.2 shows an example of a chamfer surface.

![Chamfer Surface](image)

**Fig. 3.10.2.**

### 3.11. Position of a Point Relative to a Surface

A point in space can be located relative to a given surface. It can be located above the surface, beneath the surface or on the surface. To determine the location of a point $p$ relative to a surface $s(u,v)$ we find the projection $s(u_p,v_p)$ of the point $p$ on the surface or its extension. Beyond the parametric domain the surface is continued under the rule of its construction or, if there is no such rule, in accordance with the rules of construction of extended surfaces (2.15.1)–(2.15.3). We then construct the vector $v = p - s(u_p,v_p)$ from the projection $s(u_p,v_p)$ to the point $p$, and calculate the normal $m(u_p,v_p)$ to the surface at the projection point. The position of the point relative to the surface is determined by the dot product of vector $v$ and the normal $m$. If the length of vector $v$ is zero, then $v \cdot m = 0$ and point $p$ is located on the surface; if $v \cdot m > 0$, then point $p$ is located above the surface; and if $v \cdot m < 0$, then point $p$ is located beneath the surface.

In certain cases it is required to determine whether a two-dimensional point $r = [u_p, v_p]^T$ describing the projection of point $p$ belongs to the parametric domain of surface $\Omega$ or is beyond domain $\Omega$. Let surface $s(u,v)$ have a complex border described by a two-dimensional external contour and by several internal two-dimensional contours located entirely within the outer contour. Boundary contours of the surface are oriented so that when moving along each contour the surface is always located on the same side. Let the outer contour be oriented in the counter-clockwise direction when the surface is viewed in the direction opposite to its normal, and let the inner contours be oriented in the clockwise direction.
To specify the position of a planar point $r$ relative to the parametric domain $\Omega$ of the surface, we find the point of the two-dimensional boundary of domain $\Omega$ closest to $r$. Let the closest point of the two-dimensional boundary to $r$ turn out to be the point $c(t_r)$ of boundary contour $c(t)=[u(t)\ v(t)]^T$. Let us construct two-dimensional vector $w=r-c(t_r)$ from the nearest boundary point $c(t_r)$ to $r$, and calculate the normal $n(t_r)$ of a two-dimensional contour at the nearest point. The nearest point of the boundary contour may be either the projection of point $r$ on one of the contour segments, or the junction point of two segments of the contour. At junction points of two segments of the contour, the normalized sum of the normals of joining segments—i.e., the average normal—as the normal is taken. Since the normal to the two-dimensional curve is directed to the left of the first derivative of the curve, then with the orientation of the boundary contours accepted above, normal $n$ will be directed from the border into the parametric domain of the surface. The position of the planar point $r$ relative to the domain of the surface $\Omega$ is the dot product of two-dimensional vectors $w$ and $n$. If the length of vector $w$ is zero, then $w\cdot n=0$ and $r$ is located on the boundary of domain $\Omega$; if $w\cdot n>0$, then point $r$ is located inside domain $\Omega$; and if $w\cdot n<0$, then point $r$ is located outside domain $\Omega$.

### 3.12. Searching for Initial Approximations

To determine initial approximations, we choose trial points in the parametric domain of the curve or surface and check certain conditions specific to the given construction at these trial points. The trial points must be chosen in such a way that an initial approximation can be found for every solution. The typical condition for a certain construction is usually a change in the sign of the residual equation of the considered system, or a decrease in the residual of the equation below the required level. An initial approximation can be rather approximate; it is only important that it lie in the region of convergence of solutions of the system to one of the exact solutions.

Trial points in parametric domain should be placed frequently enough to not miss a solution—and at the same time, sparsely enough to avoid excessive computation. There are different strategies for working with curves and surfaces when selecting the trial points. For example, you can move from the minimum to the maximum parameter in steps of some magnitude, and verify compliance with a certain condition. Or you can carry out a preliminary splitting of the curve or surface by elements and use the parts in further work. The essence of working with curves and surfaces is in representation of every curve and surface by a set of simple objects and using them for making a decision on initiation of the iterative process. Simple objects can be line segments, plane patches, circumscribing polyhedra of the parts of objects, or other elements. To speed up the process, the objects can be sorted one way or another. When splitting curves and surfaces, it is required to define areas in the parametric domain of curves and surfaces that can be approximated by simple objects.

In this scheme of verification of typical conditions, it remains unclear what points can be considered “close” and which points should be selected next for verification. For curves and surfaces, it is convenient to measure these values in parametric units. Proximity and motion distances to neighboring points for the next verification are
values related to each other. Indeed, if parametric distance $\Delta$ is considered close, then the next search should be performed on parametric distance $\Delta$ from the given point. The length of the parametric step is related to the curvature of a geometric object. Increments of parameters $\Delta$ are called parametric steps. Moving steps along the parametric domain of a curve are related by the curvature, with an acceptable deviation angle of its tangent. Steps of motion along a surface parametric domain are related to an acceptable deviation angle of a surface normal via the corresponding curvature. The maximum allowable value of the deviation angle of the tangent or the normal is denoted by $\Delta \alpha$.

Step $\Delta t$ of curve $c(t)$ is calculated based on the condition that during the transition from point to point, the tangent vector of the curve deviates by an angle not exceeding $\Delta \alpha$. The increment of the parameter or parametric step $\Delta t$ varies from point to point and depends on the curvature of the curve. Let the parameter $t_0$ describe the current position of the point during the movement of the curve. The next value of the parameter $t_0 + \Delta t$ must be such that the tangent vector at the new point would deviate from the tangent to the curve vector at the preceding point by an angle not exceeding $\Delta \alpha$. For this we define the curvature of the curve in some neighborhood of the point $t_0$ and in accordance with the obtained curvature, choose the next point. If we assume the curvature of the curve is kept constant in a neighborhood of point $t_0$, then the curve deviates by angle $\Delta \alpha$, if the point is displaced along the arc by the distance

$$\Delta s = \frac{\Delta \alpha}{k},$$

where $k$ is the curvature of the curve at the given point. Assume that the length of the derivative of the curve is kept constant in the neighborhood of the considered point. Then the shift $\Delta s$ along the arc corresponds to the parameter increment

$$\Delta t = \frac{\Delta s}{|c'|} = \frac{\Delta \alpha}{k |c'|},$$

(3.12.1)

where $c'$ is derivative of the curve. Substituting the expression for the curvature of the curve into the last equation, we get a parameter step

$$\Delta t = \frac{\Delta \alpha |c'|^2}{|c' \times c''|},$$

(3.12.2)

where $c''$ is the second derivative of the curve. For some curves it is not necessary to perform calculations to determine the step $\Delta t$. For example, for the circle or its arc, $\Delta t = \Delta \alpha$; if the parameter is the central angle, we can assume $\Delta t = t_{\text{max}} - t_{\text{min}}$ for the line segment.

These arguments are based on the fact that the curve in the considered neighborhood can be approximated by a circular arc of finite radius. When the curvature at the considered point tends to zero, the length of the parametric step tends to infinity. The curvature of the curve at the considered point can be very small or even zero, though in the area close enough to the considered point the curvature can be
much larger. To cover these situations, we can limit the maximum parametric step, or make a small step in the parameter and repeat the calculations at the new point. If the length of the first derivative of the curve tends to zero at the given point, then the length of the parametric step also tends to zero. The length of the first derivative of the curve at the considered point can be very small, although in the region close enough to the considered point, the length of the derivative may be much larger. To cover these situations, we introduce a limit on the minimum parametric step. This limit may be different for different curves.

Steps $\Delta u$ and $\Delta v$ of surface $s(u,v)$ are calculated based on the condition that during the transition from point to point the normal to the surface deviates by an angle not exceeding a certain value $\Delta \alpha$. Steps in the surface parameters are calculated as steps of the corresponding coordinate curves of the surface. Let us fix one of the parameters and move along the other parameter. To calculate the steps along the parameters of the surface, substitute the curvatures along the coordinate lines of the surface in the right-hand part of (3.12.1). At $v=\text{const}$ or $u=\text{const}$, the line curvatures are respectively equal to $\mu_u = b_{11}/g_{11}$ or $\mu_v = b_{22}/g_{22}$, where $g_{11}$ and $g_{22}$ are the coefficients of the first quadratic form of the surface (2.1.4), and $b_{11}$ and $b_{22}$ are the coefficients of the second quadratic form of the surface (2.1.5). As a result, the step along the parameters of the surface is calculated by the formula

$$\Delta u = \frac{\Delta \alpha \sqrt{g_{11}}}{b_{11}} = \frac{\Delta \alpha |s_1|}{|m \cdot s_{11}|},$$

$$\Delta v = \frac{\Delta \alpha \sqrt{g_{22}}}{b_{22}} = \frac{\Delta \alpha |s_2|}{|m \cdot s_{22}|}.$$

Just like for the curves, we assume that the considered neighborhood of the surface point preserves the normal curvature along the parametric directions within one step. In the areas of abrupt change of the surface shape, one can impose a limit on maximum and minimum step size along the corresponding parameter, or make a small step along the corresponding parameter and repeat the calculations at the new point.

Parametric steps calculated by formulas (3.12.2), (3.12.3), of (3.12.4) do not depend on the size of curves and surfaces.

### 3.13. Precision of Geometric Constructions

In applied problems it is important to know with what accuracy the geometric constructions were performed. To describe the curves and the surfaces we use parametric representation; therefore the search for a certain solution implies finding the corresponding parameters. The parameters of the solution do not change when the interacting curves and surfaces are moved, rotated, or simultaneously transformed. In many cases the parameters of the curves and surfaces are known with some accuracy. We shall distinguish spatial uncertainty and parametric uncertainty. For different curves and surfaces the same spatial uncertainty corresponds to different parametric
uncertainty. Therefore, for normal interaction of the whole manifold of curves and surfaces, we should assume the global spatial uncertainty.

Let the following requirement be imposed: perform geometric constructions with spatial accuracy $\xi$. This means that two points in the space are considered coincident if the distance between them does not exceed $\xi$ (or, more conveniently, if the coordinates of the points coincide within an uncertainty $\xi$). Let the parameter $t_0$ correspond to some point $P_0$ of the curve $c(t)$. A point $P_1$ of the same curve with parameter $t_1 = t_0 \pm \varepsilon$, where $\varepsilon > 0$ and $\varepsilon$ is many times smaller than the parametric domain of the curve $t_{\text{max}} - t_{\text{min}}$, is located at the following distance from point $P_0$

$$r = \varepsilon | c'(t_0)|, \quad 0 < \varepsilon << |t_{\text{max}} - t_{\text{min}}|,$$

where $c'(t_0)$ is the derivative of the curve at the point $P_0$. If the following inequality holds,

$$\varepsilon \leq \frac{\xi}{|c'(t_0)|},$$

then points $P_0$ and $P_1$ of the curve $c(t)$ are indistinguishable for a given spatial uncertainty $\xi$. In (3.13.1) $\varepsilon$ is the parametric uncertainty for curve $c(t)$. Similarly, a point of surface $r(u,v)$ with parameters $u_0$ and $v_0$ is considered coincident with the points of the same surface with the parameters $u_1 = u_0 \pm \varepsilon_1$, $v_1 = v_0 \pm \varepsilon_2$, if the following inequalities hold:

$$\varepsilon_1 \leq \frac{\xi}{|r_1(u_0, v_0)|} \quad \text{and} \quad \varepsilon_2 \leq \frac{\xi}{|r_2(u_0, v_0)|},$$

where $r_1(u_0, v_0)$ and $r_2(u_0, v_0)$ are partial derivatives of the surface with respect to the first and second parameter respectively at the considered point, $\xi$ is spatial uncertainty, and $\varepsilon_1$ and $\varepsilon_2$ are parametric accuracies for the first and second parameters of surface $r(u,v)$.

In iterative methods of geometric constructions, the parameters of curves and surfaces are found with some uncertainty. Parameter refinement should be continued until the change of the absolute value of each parameter at the next iteration satisfies inequalities (3.13.1) and (3.13.2). But besides inequalities (3.13.1) and (3.13.2), it is necessary to achieve fulfillment of equalities of the given system of equations with accuracy not lower than $\xi$. But this does not guarantee that we achieve the required accuracy. Near the osculating points the solution converges very slowly. Therefore, in inequalities (3.13.1) and (3.13.2), one can introduce a coefficient $k$, which can be equal to several tens or even hundreds. Iterative processes of geometric constructions should continue until parameter changes are less than $\varepsilon/k$ and until the equation is satisfied with precision $\xi$.

In those cases when we do not know the parameters of the curve or surface, but it is required to specify their uncertainty, we can use average uncertainty. For this we have to appeal to a certain geometric dimension of a geometric object. For this purpose, we
can take the length of a curve or the diagonal of a circumscribing polyhedron of the surface. Assume that the parametric length of the considered curve or surface is not less than unity, and its dimensions are commensurate with model size $d$. Then, instead of uncertainties (3.13.1) and (3.13.2), we can use average uncertainties:

$$\varepsilon = \frac{\xi}{d} |t_{\text{max}} - t_{\text{min}}|, \quad \text{for curve } c(t), \quad t_{\text{min}} \leq t \leq t_{\text{max}};$$

$$\varepsilon_1 = \frac{\xi}{d} |u_{\text{max}} - u_{\text{min}}|, \quad \varepsilon_2 = \frac{\xi}{d} |v_{\text{max}} - v_{\text{min}}|, \quad \text{for surface } r(u,v), \quad u_{\text{min}} \leq u \leq u_{\text{max}}, \quad v_{\text{min}} \leq v \leq v_{\text{max}}.$$

When possible, the geometric construction should be carried out without the use of numerical methods. In these cases the accuracy of geometric constructions depends on the accuracy of the diagnosis of particular cases. For example, when a cylindrical surface is intersected by a plane orthogonal to its axis, the accuracy of the construction of the intersection line is defined by the accuracy with which the normal vector to the plane and the axis of the cylinder are parallel, taking into account the radius of the cylinder.

At the same time, $\xi$ and $\varepsilon$ should not be less than $10^{-n}$, where $n$ is the number of significant digits of the coordinate and parameter representation in computer memory. Otherwise, the numbers that differ by a relative value less than $10^{-n}$ are indistinguishable, and we cannot in principle ensure accuracy $\xi$ or $\varepsilon$.

Besides values $\xi$ and $\varepsilon$, the smallest possible size $d_{\text{min}}$ and the maximum possible size $d_{\text{max}}$ of the model play a role in geometric construction. This means that the intersection of a surface or a curve of size $d_{\text{min}}$ with a curve or a surface of size $d_{\text{max}}$ should be ensured. Let a parametric domain $|t_{\text{max}} - t_{\text{min}}|$, $|u_{\text{max}} - u_{\text{min}}|$, and $|v_{\text{max}} - v_{\text{min}}|$ be a few units in size. In this case, for large models, computed parametric uncertainties are very small, and may be less than $10^{-n}$, where $n$ is the number of precise digits of parameter representations. In this case it is impossible to ensure that the relative uncertainty of the parameter calculation be less than $\varepsilon$. On the other hand, if $d_{\text{min}}$ is commensurate with $\xi$, then for small models, $\varepsilon$ is commensurate with the entire parametric domain. Constructing models of this size is impossible.

The above indicates that the number of significant digits of real-number representation in the computer's memory is the starting point for determining the maximum precision that can be achieved by numerical methods.

**Exercises**

1. Describe an algorithm for computing the projection of a point on a circle.
2. Describe an algorithm for computing the nearest points of a line and a cylindrical surface.
3. Describe an algorithm for constructing a circle of a given radius tangent to two lines.
4. Describe an algorithm for constructing a curve of intersection of a plane and a cylindrical surface.