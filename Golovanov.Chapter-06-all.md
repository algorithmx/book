GEOMETRIC CONSTRAINTS

A complicated geometric model may consist of a large number of solids, surfaces, curves, points, and other elements that are related to each other. Geometric constraints model the relations between the elements of the model. Geometric constraints allow the creation of and control of such models, and are a part of the geometric model.

6.1. Geometric Model Control

Each element of the geometric model has its own data structure. Scalar quantities, vector components, and coordinates of the points stored in the data structures and subject to editing can serve as parameters of the model. Variables specially created for this purpose can represent the parameters. Using the parameters, elements of the model can be linked to each other and the model can be controlled. For example, items in an assembly can be positioned on the same axis, in the same plane; they can be joined by hinges or fixed in certain directions. Dimensions of some parts can be associated with the dimensions of other parts, or coupled by equations with any other parameters.

Geometric constraints are conditions imposed on the model elements and formulated as equations and inequalities. Geometric constraints simulate real dependences of the model elements on each other. Geometric constraints are also called variational relations.

Geometric constraints are necessary for the model shown in Fig. 6.1.1 to ensure movement of its elements in a specific way.

Fig. 6.1.1.

Geometric constraints simplify the modeling of similar parts. It is sufficient to create a dependence of the parts’ dimensions on one or more parameters. Specifying a set of values of the control parameters, we obtain a set of parts of a certain type. Fig. 6.1.2
shows a model where dependencies on several parameters are imposed on the model dimensions. Fig. 6.1.3 shows a similar model with different set of parameters.

We represent each geometric constraint as an object that describes one or more algebraic equations, and contains a list of parameters related by the equations. Interrogating the object reveals the equations and current parameter values. Unknowns in constraint equations are the changing model parameters. The same parameters can be involved in different constraints. A geometric constraint is considered satisfied if the algebraic equations described by the object are satisfied.

A geometric model is said to be in equilibrium when all its geometrical constraints are satisfied. During modeling, elements are modified or new elements added. If a part of a geometric constraint is no longer satisfied as the result of a modification, the geometric constraints make it possible to find new values of the parameters that restore the model to equilibrium. To do this, a system of equations is formed of the geometric constraints. The unknowns of the system are the model parameters that represent the model in a state of equilibrium. This system of equations is solved and the model is rebuilt according to the new values of the parameters.

Movement of the model shown in Fig. 6.1.1 can be simulated by turning the shaft by a small angle and then fixing the shaft. The geometric constraints are no longer satisfied. Solution of the system of geometric constraint equations will yield new parameter values that will satisfy the geometric constraints. After changing the parameters, the elements of the geometric model change their position relative to each other. As we rotate the shaft, we get a series of equilibrium states that simulate movement of the model elements.

We can perform manipulations on a geometric model. These manipulations can include editing the model, creating copies of elements of the model, changing the position of elements of the model relative to each other, and so on. By imposing geometric constraints on the model parameters, we can control the manipulations.

Geometric model control is modification of a model using geometric constraints. Controlling a geometric model is done as follows. At some stage, the model’s geometric constraints are satisfied. Further, the new values are assigned to one or several parameters, and these parameters are fixed. For example, we have changed the position of some element of the geometric model and want to know how this affects other elements of the model related to the element. Geometric model control can be done by changing the constants of the equation, which also brings the system of geometric constraints out of the equilibrium state. For example, we change the value of a certain dimension during construction of a similar model. As a result, some equations are not satisfied for the initial values of the parameters. The system of geometric constraints goes out of equilibrium when the new constraints are added to it. For
example, we have modeled two parts, and when constructing an assembly unit, using these parts, we want some two planes of the parts to be parallel to each other. In this case, a new geometric constraint arises that adds its own equations and unknowns to the system of equations.

Suppose we are given the set of geometric constraints, resulting in a system of $m$ equations

$$f_1(p_1, p_2, \ldots, p_n) = 0,$$
$$f_2(p_1, p_2, \ldots, p_n) = 0,$$
$$\ldots \ldots \ldots \ldots \ldots$$
$$f_m(p_1, p_2, \ldots, p_n) = 0,$$

for $n$ parameters $p_1, p_2, \ldots, p_n$ of the geometric model. The number of equations is generally not equal to the number of related parameters. The non-equilibrium system of equations of geometric constraints can be written as

$$f_1(p_1 + \Delta p_1, p_2 + \Delta p_2, \ldots, p_n + \Delta p_n) = 0,$$
$$f_2(p_1 + \Delta p_1, p_2 + \Delta p_2, \ldots, p_n + \Delta p_n) = 0,$$
$$\ldots \ldots \ldots \ldots \ldots$$
$$f_m(p_1 + \Delta p_1, p_2 + \Delta p_2, \ldots, p_n + \Delta p_n) = 0.$$ (6.1.1)

The unknowns of this system are variations of the model parameters $\Delta p_1, \Delta p_2, \ldots, \Delta p_n$. After solving system of equations (6.1.1), the model should be reconstructed according to the new values of parameters $p_i + \Delta p_i, i=1,2,\ldots,n$. If the non-equilibrium system of equations of geometric constraints cannot be solved, then we should return to the previous equilibrium state of the geometrical model and constants of equations, under which the geometric constraint equations are satisfied.

Usually geometric constraints are divided into three-dimensional and two-dimensional. Three-dimensional geometric constraints link the elements of separate assembly units. Two-dimensional geometric constraints link the elements of separate sketches. The system of equations of assembly units and the systems of equations of sketches are solved independently. All these systems can be linked by global variables of the model, which must be known at the time of formation of the individual systems of equations.

### 6.2. Creation of Geometric Constraints

Any model parameters can be linked by geometric constraints. A system of equations should be able to change these parameters during the solution and get a response to these changes. In the process of solving the system, geometric constraints usually do not change parameters of the model directly, but only the parameters of objects which we call "special." **Special objects** replace the model elements in the geometric constraints. Special objects are simplified copies of model elements. The number of parameters a special object provides for modification in the system of equations should be equal to the number of degrees of freedom of the object. After the
geometric constraint equations are satisfied, the special objects pass information to the geometric model.

We can use a point as a special object. Each point has three degrees of freedom, and is described by three numbers. Each special point can control the position of several points of the model. For example, if some special point passes its coordinates to the center of a sphere of the model and to the control point of a spline surface of the model, then the center of the sphere and the control point of the surface coincide under any modifications of the model. After the system of equations reaches equilibrium, each special point equates the coordinates of the points linked to it to the point's own coordinates.

We can use a plane as a special object. Each plane has three degrees of freedom, and is described by three numbers. We can use a sphere as a special object. A sphere has four degrees of freedom, including change of radius, and is described by four numbers. A straight line can be obtained by intersecting two planes. A sphere and a plane intersecting it provide a circle. We can use other geometric objects as special objects.

Consider some geometric constraints that can be created using points as special objects. Suppose there are two points, \( p_1 \) and \( p_2 \), global coordinates of which are, respectively, \( x_1, y_1, z_1 \) and \( x_2, y_2, z_2 \). We can impose a geometric constraint on points \( p_1 \) and \( p_2 \)—the linear dimension described by the equation

$$
\sqrt{(x_2 + \Delta x_2 - x_1 - \Delta x_1)^2 + (y_2 + \Delta y_2 - y_1 - \Delta y_1)^2 + (z_2 + \Delta z_2 - z_1 - \Delta z_1)^2} - d = 0, \quad (6.2.1)
$$

where \( d \) is the desired dimension, and \( \Delta x_1, \Delta y_1, \Delta z_1 \) and \( \Delta x_2, \Delta y_2, \Delta z_2 \) are a variation of the coordinates of the related points to be determined. The linear dimension is shown in Fig. 6.2.1.

![Fig. 6.2.1.](image)

The geometric constraint imposed on points \( p_1 \) and \( p_2 \), which is the dimension along one of the coordinates, is described by one of the equations

$$
|x_2 + \Delta x_2 - x_1 - \Delta x_1| = d_x, \quad |y_2 + \Delta y_2 - y_1 - \Delta y_1| = d_y, \quad |z_2 + \Delta z_2 - z_1 - \Delta z_1| = d_z,
$$

where \( d_x, d_y, d_z \) are the desired dimensions. One of these equations, applied to the segment \( r(t) = (1-t)p_1 + tp_2 \), can make the segment parallel to the corresponding
coordinate plane. Two of these equations can make the segment parallel to one of the coordinate axes.

The geometric constraint ensuring the coincidence of points \( p_1 \) and \( p_2 \) is described by the equations

$$
x_2 + \Delta x_2 - x_1 - \Delta x_1 = 0,
$$
$$
y_2 + \Delta y_2 - y_1 - \Delta y_1 = 0,
$$
$$
z_2 + \Delta z_2 - z_1 - \Delta z_1 = 0.
$$

Construct the following equation to fix some parameter of the geometric model:

$$
p + \Delta p - p_0 = 0,
$$

where \( p \) is the current value of the parameter, \( \Delta p \) is the variation of the parameter subject to the determination, and \( p_0 \) is the given value of the parameter that must be preserved.

We can fix a solid, or some dimension of the solid, with fixing equations. Equations for fixed parameters can be isolated from a system into a separate group. The system of equations for the fixed parameters and the system of equations for the other parameters do not depend on each other, and can be solved separately.

Geometric constraints can be set between any elements of the model, and these constraints can also be of any kind—as long as they can be presented in the form of equations for some special objects. The set of special objects is expanded so that it is possible to impose all the necessary geometric constraints on the elements of the model. For example, let us assume that we want to determine the linear dimension between a certain point of the curve \( r_1(t_1) \) and a certain point of the curve \( r_2(t_2) \). Assume that the curves are segments for simplicity:

$$
r_1(t_1) = (1-t_1)p_1 + t_1p_3,
$$
$$
r_2(t_2) = (1-t_2)p_2 + t_2p_4,
$$

reference points of which are associated with the specific points; we consider the midpoints of the segments as the linking points. The midpoints of the segments are determined by parameters \( t_1=1/2, t_2=1/2 \). The linear dimension (6.2.1) for the midpoints of the segments links twelve parameters, which are the changes in the coordinates of the special points that control the reference points of the segments.

Geometric model parameters may be linked by algebraic equations; for example,

$$
f(a+\Delta a, b+\Delta b, ..., c+\Delta c) = 0,
$$

where \( a, b, c \) are model parameters, and \( \Delta a, \Delta b, ..., \Delta c \) are desired changes of the parameters. These constraints can link not only the described model parameters, but also special variables. Special variables are created to control the geometric model. For example, to make several parameters of the various elements of the geometric model dependent on a common parameter, we introduce a special variable and a set of algebraic constraints that describe the required dependencies of the model parameters on the special variable.

Geometric model parameters can be related by algebraic inequalities. In the process of solving a system of geometric constraint equations, inequalities are replaced
by the corresponding equations. Suppose, for example, it is required to relate the parameters of the model \(a\) and \(b\) by the inequality \(a > b\). During the solution, inequality \(a > b\) is replaced by the equation

$$
a + \Delta a - b - \Delta b = e,
$$

where \(e = a + \Delta a - b - \Delta b\), if \(a + \Delta a > b + \Delta b\), and \(e = 0\), if \(a + \Delta a \leq b + \Delta b\). If the inequality is satisfied at the next iteration, it is replaced by the identity; if inequality is not satisfied, it is replaced by the strict equality. Geometric constraints built on inequalities are called non-strict geometric constraints.

### 6.3. Positioning of a Set of Solids

To determine the geometric relationships between the elements of a model of some assembly, the parts of which are represented by a set of solids, it is convenient to use the local coordinate systems as special objects of the geometric constraints. Every solid is associated with a local coordinate system, the position of which is described in the global Cartesian coordinate system. Thus, the positions of the solids relative to each other are reduced to the change in the position of the coordinate systems associated with the solids.

Every solid in three-dimensional space has six degrees of freedom: three translational and three rotational. Let us introduce six parameters for each solid: three rotational angles and three translations. Denote the translations of the \(j\)-th solid along the first, second, and third global axis by \(\Delta x_j\), \(\Delta y_j\), and \(\Delta z_j\) respectively, and denote the rotation angles of the \(j\)-th solid around an axis passing through the origin of the local coordinate system parallel to the first, second, and third global axis, respectively, by \(\Delta \alpha_j\), \(\Delta \beta_j\), \(\Delta \gamma_j\). Let us call these rotation axes the first, second, and third, respectively. If the position of the \(j\)-th solid does not require changes, then \(\Delta \alpha_j\), \(\Delta \beta_j\), \(\Delta \gamma_j\), \(\Delta x_j\), \(\Delta y_j\), and \(\Delta z_j\) are zeros. If it is required to change the position of the \(i\)-th solid, then this change is made in four steps: Rotate the solid around the first axis by angle \(\Delta \alpha_i\); rotate the solid about the second axis by angle \(\Delta \beta_i\); rotate the solid around the third axis by angle \(\Delta \gamma_i\); and displace the solid by the vector \([\Delta x_i, \Delta y_i, \Delta z_i]^T\). An example of a local coordinate system and the parameters of a solid is shown in Fig. 6.3.1.

![Fig. 6.3.1](image-url)
After changing the \( j \)-th solid position, point \( a \) of the solid is described by the radius-vector \( o_j + M_j(a - o_j) \), where \( o_j \) is the origin of the \( j \)-th local coordinate system, and vector \( n \) of the \( j \)-th solid takes the value \( M_j n \). Matrix \( M_j \) is represented in expanded form (1.14.7), and the radius-vectors of the points and vectors—in the forms (1.14.8) and (1.14.9) respectively. Matrix \( M_j \) describes the change of position of the \( j \)-th solid, and is expressed in terms of quantities \( \Delta \alpha_j, \Delta \beta_j, \Delta \gamma_j, \Delta x_j, \Delta y_j, \Delta z_j \). Matrix \( M_j \) is obtained by the product of three rotation matrices and a displacement matrix: \( M_j = M_\Delta M_\gamma M_\beta M_\alpha \),

$$
M_\Delta = \begin{bmatrix}
1 & 0 & 0 & \Delta x_j \\
0 & 1 & 0 & \Delta y_j \\
0 & 0 & 1 & \Delta z_j \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

— matrix of displacement by vector \([ \Delta x_j, \Delta y_j, \Delta z_j ]^T \),

$$
M_\gamma = \begin{bmatrix}
\cos \Delta \gamma_j & -\sin \Delta \gamma_j & 0 & 0 \\
\sin \Delta \gamma_j & \cos \Delta \gamma_j & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

— matrix of rotation by angle \( \Delta \gamma_j \),

$$
M_\beta = \begin{bmatrix}
\cos \Delta \beta_j & 0 & \sin \Delta \beta_j & 0 \\
-\sin \Delta \beta_j & 0 & \cos \Delta \beta_j & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

— matrix of rotation by angle \( \Delta \beta_j \),

$$
M_\alpha = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \cos \Delta \alpha_j & -\sin \Delta \alpha_j & 0 \\
0 & \sin \Delta \alpha_j & \cos \Delta \alpha_j & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

— matrix of rotation by angle \( \Delta \alpha_j \).

When imposing geometric constraints on the solids of the model, we use markers. Markers help to get the positions of the points and the directions of the vectors in the global coordinate system. A marker is described by a starting point, by the vector of the normal, and by the vector of direction orthogonal to the normal vector. The position of the marker in the local coordinate system associated with the solid must be known and fixed. Knowing the position of the marker in the local coordinate system, we can obtain the coordinates of its starting point and the components of its vectors in the global coordinate system, in which geometric constraint equations are formed. For every geometric constraint linking two solids, two markers are constructed. For each solid, we can construct as many markers as the number of geometric constraints linking the solid with other solids. With the help of markers, we compose equations by combination of which geometric constraints can be constructed.

In order to match a given point \( a_j \) of the \( j \)-th solid with a given point \( a_k \) of the \( k \)-th solid, construct two markers with origins at the matching points, and require the satisfaction of the vector equality

$$
o_j + M_j(a_j - o_j) = o_k + M_k(a_k - o_k).
$$
This equality removes three degrees of freedom from one of the solids.

To set the distance $d$ between a given point $a_j$ of the $j$-th solid and a given point $a_k$ of the $k$-th solid, construct two markers with origins at the matching points, and require satisfaction of equation

$$| o_j + M_j(a_j - o_j) - o_k - M_k(a_k - o_k) | = d. $$

To locate a given point $b_j$ of the $j$-th solid at distance $d$ from a given plane of the $k$-th solid, construct a marker with its starting point at $b_j$, and a marker whose starting point and normal coincide with the starting point and the normal of the given plane of the $k$-th solid; and require satisfaction of the equality

$$ (o_j + M_j(b_j - o_j) - o_k) \cdot (M_k n_k) = d, $$

where $n_k$ is the normal to the given plane of the $k$-th solid. This equation reduces the number of degrees of freedom of one of the solids by one. In the particular case when $d=0$, the above equation describes the coincidence of the point and the plane.

In order to match a given point $c_j$ of the $j$-th solid with a given axis of the $k$-th solid, construct a marker starting at point $c_j$ and a marker with its starting point and normal coinciding with the origin and the direction of the given axis of the $k$-th solid; and require satisfaction of equality

$$ (o_j + M_j(c_j - o_j) - o_k) \cdot (M_k d_k) = 0, $$

where $d_k$ is the vector of the marker direction of the $k$-th solid orthogonal to the given axis. The above equation reduces the number of degrees of freedom of one of the solids by two.

To make the given axis of the $j$-th solid parallel to a given plane of the $k$-th solid, construct two markers. Superpose the starting point and the normal of the first marker with the starting point and the direction of the given axis of the $j$-th solid; superpose the starting point and the normal of the second marker with the beginning and the normal of the given plane of the $k$-th solid, and require satisfaction of equality

$$ (M_j n_j) \cdot (M_k n_k) = 0, $$

where $n_j$ is the direction of the given axis of the $j$-th solid, and $n_k$ is the normal to the given plane of the $k$-th solid. This equation reduces the number of degrees of freedom of one of the solids by one.

To set the given angle $\theta$, $0 < \theta < \pi$, between a given plane of the $j$-th solid and a given plane of the $k$-th solid, construct two markers with starting points and normals coinciding with the starting points and normals of the given planes, and require satisfaction of equality

$$ (M_j n_j) \cdot (M_k n_k) = \cos \theta, $$
where \( n_j \) is the normal to the plane of the \( j \)-th solid, and \( n_k \) is the normal to the given plane of the \( k \)-th solid. This equation reduces the number of degrees of freedom of one of the solids by one. In the particular case of \( \cos \theta = 0 \), this equation describes the orthogonality of the planes of the two solids.

For a given plane of the \( j \)-th solid to be parallel to a given plane of the \( k \)-th solid, construct two markers whose starting points and normals coincide with the starting points and normals of the given planes, and require satisfaction of equalities

$$
(M_j n_j) \cdot (M_k d_k) = 0, \quad (M_j n_j) \cdot (M_k (n_k \times d_k)) = 0,
$$

where \( n_j \) is the normal to the given plane of the \( j \)-th solid, \( n_k \) is the normal of the given plane of the \( k \)-th solid, and \( d_k \) is the direction vector of the marker of the \( k \)-th solid orthogonal to the normal \( n_k \). This equation reduces the number of degrees of freedom of one of the solids by two.

With the help of these equations, we construct the geometric constraints that establish the relationships between the elements of the model. Solving the system of equations of geometric constraints, we find changes in the model parameters. Adjust the model in accordance with the found solution. For example, if \( \Delta \alpha_j = \Delta \beta_j = \Delta \gamma_j = \Delta x_j = \Delta y_j = \Delta z_j = 0 \), then matrix \( M_j \) is the identity matrix, and the position of the \( j \)-th solid is not required to change. Otherwise, rotate and move the \( j \)-th solid in accordance with matrix \( M_j \). As a result, the equations imposed by the geometric constraints are satisfied.

### 6.4. Solution of Geometric Constraints Equations

A peculiarity of systems of equations of geometric constraints is the inequality of the number of equations to the number of parameters. The number of parameters can reach several thousand. At the same time, the geometric model must quickly respond when the geometric constraints are out of equilibrium.

Solution of a system of geometric constraint equations is complicated by the inequality of the number of equations and the number of unknowns. If the number of equations is less than the number of unknowns, then the system of geometric constraints has multiple solutions, from which we must select the most suitable. If the number of equations exceeds the number of unknowns, then it is necessary to find the geometric restrictions that may be satisfied; the remaining constraints can be discarded. In general, systems of geometric constraint equations are solved by numerical methods. In certain cases, they can be solved without using numerical methods.

When using numerical methods, solution of a system of equations of geometric constraints depends on the initial approximation with which the iterative process is started. To make an initial approximation located inside a region of convergence to the desired solution, we must avoid significant deviations of the geometric constraints from their equilibrium states. For example, if the geometric constraints are disturbed from the equilibrium state by moving some point of the geometric object, then the solution
should be sought, not for the final position of the point, but for several of its intermediate positions, gradually shifting from its initial position to its final position. Similarly, after a significant change in the value of a certain dimension, one should seek solutions for several intermediate values of this dimension, moving gradually from the initial value to the new value. For a numerical solution, it is desirable that non-zero increments of the parameters are of the same order. Normalization of the parameters is used to achieve this.

To find the response of geometric constraints when they are out of equilibrium, methods that may impose additional geometric constraints are used to force the model parameters to follow some rules and split the problem into a number of subproblems, the consecutive solution of which allows us to solve the original problem.

6.5. The Conservative Method

If the number of unknowns is more than the number of equations of a system, it is possible to formulate a criterion for the behavior of parameters of geometric models. One of the simplest and most effective criteria is the requirement for conservative behavior of the model parameters. Let us formulate the parameter behavior criterion as follows: The sum of the squares of changes of the parameters related by the geometric constraints—i.e., the response of the geometric model to a perturbation—should have a minimum value. This criterion puts all the variable parameters on an equal footing. This criterion is expressed by the minimum of the function

$$\psi(\Delta p_1, \Delta p_2, ..., \Delta p_n) = \frac{1}{2} (\Delta p_1^2 + \Delta p_2^2 + ... + \Delta p_n^2),$$

(6.5.1)

where $\Delta p_1, \Delta p_2, ..., \Delta p_n$ are variations of the parameters $p_1, p_2, ..., p_n$. Search for the minimum of function (6.5.1) subject to equations (6.1.1) leads to the problem of finding the minimum of the function,

$$F(\Delta p_1, \Delta p_2, ..., \Delta p_n) = \frac{1}{2} (\Delta p_1^2 + \Delta p_2^2 + ... + \Delta p_n^2) +$$

$$+ \lambda_1 f_1(p_1 + \Delta p_1, p_2 + \Delta p_2, ..., p_n + \Delta p_n) +$$

$$+ \lambda_2 f_2(p_1 + \Delta p_1, p_2 + \Delta p_2, ..., p_n + \Delta p_n) +$$

$$+ \lambda_m f_m(p_1 + \Delta p_1, p_2 + \Delta p_2, ..., p_n + \Delta p_n),$$

where $\lambda_1, \lambda_2, ..., \lambda_m$ are Lagrange multipliers. To satisfy the necessary conditions for a minimum of this function, it is required, along with (6.1.1), to satisfy the equations

$$\Delta p_1 + \lambda_1 \frac{\partial f_1}{\partial p_1} + \lambda_2 \frac{\partial f_2}{\partial p_1} + ... + \lambda_m \frac{\partial f_m}{\partial p_1} = 0,$$
$$ \Delta p_2 + \lambda_1 \frac{\partial f_1}{\partial p_2} + \lambda_2 \frac{\partial f_2}{\partial p_2} + \ldots + \lambda_m \frac{\partial f_m}{\partial p_2} = 0, $$
$$ \ldots \ldots \ldots \ldots \ldots \ldots $$
$$ \Delta p_n + \lambda_1 \frac{\partial f_1}{\partial p_n} + \lambda_2 \frac{\partial f_2}{\partial p_n} + \ldots + \lambda_m \frac{\partial f_m}{\partial p_n} = 0. $$ (6.5.2)

We have arrived at the system of \( n+m \) equations (6.1.1) and (6.5.2) for \( n+m \) unknowns \( \Delta p_1, \Delta p_2, \ldots, \Delta p_n, \lambda_1, \lambda_2, \ldots, \lambda_m \). The initial approximation of the Lagrange multipliers can be set equal to zero. In the process of solving, they can also be considered close to zero, which simplifies solution of the system.

Let us apply the conservative method for determining the changes of position of point \( p_1=[x_1 y_1 z_1]^T \) of the first solid and point \( p_2=[x_2 y_2 z_2]^T \) of the second solid upon imposing geometric constraints (6.2.1) specifying distance \( d \) between points \( p_1 \) and \( p_2 \).

The sum of the squares of changes of displacement of the related points is described by the function

$$ \Psi = \frac{1}{2} \left( \Delta x_1^2 + \Delta y_1^2 + \Delta z_1^2 + \Delta x_2^2 + \Delta y_2^2 + \Delta z_2^2 \right). $$

Use the method of Lagrange multipliers to find the minimum of the function \( y \) under condition (6.2.1). A necessary condition for a minimum of function \( y \) under condition (6.2.1) is the vanishing of the partial derivatives, with respect to parameters \( \Delta x_1, \Delta y_1, \Delta z_1, \Delta x_2, \Delta y_2, \) and \( \Delta z_2 \), of the function

$$ F = \frac{1}{2} \left( \Delta x_1^2 + \Delta y_1^2 + \Delta z_1^2 + \Delta x_2^2 + \Delta y_2^2 + \Delta z_2^2 \right) + $$
$$ + \lambda \sqrt{(x_2 + \Delta x_2 - x_1 - \Delta x_1)^2 + (y_2 + \Delta y_2 - y_1 - \Delta y_1)^2 + (z_2 + \Delta z_2 - z_1 - \Delta z_1)^2 - d}, $$

where \( \lambda \) is a multiplier to be determined. The desired changes in the coordinates of the points and the multiplier \( \lambda \) are found from the system of equations

$$ \sqrt{(x_2 + \Delta x_2 - x_1 - \Delta x_1)^2 + (y_2 + \Delta y_2 - y_1 - \Delta y_1)^2 + (z_2 + \Delta z_2 - z_1 - \Delta z_1)^2} - d = 0, $$
$$ \Delta x_1 + \lambda \frac{x_1 + \Delta x_1 - x_2 - \Delta x_2}{\sqrt{(x_2 + \Delta x_2 - x_1 - \Delta x_1)^2 + (y_2 + \Delta y_2 - y_1 - \Delta y_1)^2 + (z_2 + \Delta z_2 - z_1 - \Delta z_1)^2}} = 0, $$
$$ \Delta y_1 + \lambda \frac{y_1 + \Delta y_1 - y_2 - \Delta y_2}{\sqrt{(x_2 + \Delta x_2 - x_1 - \Delta x_1)^2 + (y_2 + \Delta y_2 - y_1 - \Delta y_1)^2 + (z_2 + \Delta z_2 - z_1 - \Delta z_1)^2}} = 0, $$
$$ \Delta z_1 + \lambda \frac{z_1 + \Delta z_1 - z_2 - \Delta z_2}{\sqrt{(x_2 + \Delta x_2 - x_1 - \Delta x_1)^2 + (y_2 + \Delta y_2 - y_1 - \Delta y_1)^2 + (z_2 + \Delta z_2 - z_1 - \Delta z_1)^2}} = 0, $$
$$ \Delta x_2 + \lambda \frac{x_2 + \Delta x_2 - x_1 - \Delta x_1}{\sqrt{(x_2 + \Delta x_2 - x_1 - \Delta x_1)^2 + (y_2 + \Delta y_2 - y_1 - \Delta y_1)^2 + (z_2 + \Delta z_2 - z_1 - \Delta z_1)^2}} = 0, $$
$$ \Delta y_2 + \lambda \frac{y_2 + \Delta y_2 - y_1 - \Delta y_1}{\sqrt{(x_2 + \Delta x_2 - x_1 - \Delta x_1)^2 + (y_2 + \Delta y_2 - y_1 - \Delta y_1)^2 + (z_2 + \Delta z_2 - z_1 - \Delta z_1)^2}} = 0, $$
$$ \Delta z_2 + \lambda \frac{z_2 + \Delta z_2 - z_1 - \Delta z_1}{\sqrt{(x_2 + \Delta x_2 - x_1 - \Delta x_1)^2 + (y_2 + \Delta y_2 - y_1 - \Delta y_1)^2 + (z_2 + \Delta z_2 - z_1 - \Delta z_1)^2}} = 0. $$

This system of equations has the solution

$$ \Delta x_1 = \frac{d-g}{2g}(x_1 - x_2), \quad \Delta y_1 = \frac{d-g}{2g}(y_1 - y_2), \quad \Delta z_1 = \frac{d-g}{2g}(z_1 - z_2), $$
$$ \Delta x_2 = \frac{d-g}{2g}(x_2 - x_1), \quad \Delta y_2 = \frac{d-g}{2g}(y_2 - y_1), \quad \Delta z_2 = \frac{d-g}{2g}(z_2 - z_1), $$
$$ \lambda = \frac{g-d}{2}, $$

where \( g = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2} \). It can be proved that the found solution is the point of the minimum of function \( F \). The points are moved by the same distance along the straight line passing through points \( p_1 \) and \( p_2 \). In this formulation of the problem, the points are equal, and the equations and the solution of the system of equations are symmetric.

If we fix point \( p_1 \) in this example, function \( F \) takes the form

$$ F = \frac{1}{2}(\Delta x_2^2 + \Delta y_2^2 + \Delta z_2^2) + \lambda \left( \sqrt{(x_2 + \Delta x_2 - x_1)^2 + (y_2 + \Delta y_2 - y_1)^2 + (z_2 + \Delta z_2 - z_1)^2} - d \right). $$

This function reaches a minimum at the change in coordinates of point \( p_2 \) and at the multiplier \( \lambda \):

$$ \Delta x_2 = \frac{d-g}{g}(x_2 - x_1), \quad \Delta y_2 = \frac{d-g}{g}(y_2 - y_1), \quad \Delta z_2 = \frac{d-g}{g}(z_2 - z_1), $$
$$ \lambda = g-d, $$

where \( g = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2} \). Point \( p_2 \) is moved along the straight line passing through points \( p_1 \) and \( p_2 \).

### 6.6. The Decomposition Method

When using the decomposition method for solving a system of equations of geometric constraints, the original problem is divided into a number of subproblems, and consecutive solutions of these subproblems allow us to solve the original problem.
This division of the problem is called decomposition. The decomposition is performed by analyzing the graph of the problem. Depending on the objective, decomposition may be carried out in various ways. In general, the initial system of equations is broken up into subsystems as a result of the decomposition. Decomposition is carried out by analyzing the degrees of freedom of the graph constructed for the model elements, and the geometric constraints. The geometric model can be represented as a graph, where the vertices of the graph are the geometric constraints and the elements of the model. Each edge of the graph represents a connection between two elements of the model by means of the geometric constraints imposed on these elements. Each element of the geometric model is associated with a number of added degrees of freedom $g_i$, and each of the geometric constraints is associated with a number of removed degrees of freedom $c_i$. We can formally define the number of degrees of freedom for the graph, which is equal to $\Sigma g_i - \Sigma c_i$.

Let the elements of the model be solids. Changing the position of the solids is done by rotation and translation of the local coordinate systems rigidly connected to the solids. Before a solid is fixed it has six degrees of freedom: three translational and three rotational. Each degree of freedom corresponds to a parameter describing the rotation or translation of the solid’s local coordinate system. Every solid is associated with six unknowns in the system of equations for the geometric constraints. A model consisting of $n$ loose and unrelated solids has $6n$ degrees of freedom. Each geometric constraint removes a number of degrees of freedom by limiting the relative motion of the solids of the model. A geometric constraint is imposed between pairs of solids. If one of the solids of a pair is fixed, then after geometric constraints are imposed, the number of degrees of freedom in another solid is reduced by a certain number. If the geometric constraints imposed between the two solids remove all six degrees of freedom, then the two solids are rigidly connected.

The minimum number of model elements forming a whole rigid unit is two. The maximum number of model elements forming a whole rigid unit can be quite large. If it is found that some elements of a model form a whole rigid unit, then the graph of the model can be rewritten by placing the rigidly connected elements in one vertex.

Let $k_i$ be the number of geometric constraints removing $i$ degrees of freedom of a model consisting of $n$ solids. Then the formal number of degrees of freedom of the model with geometric constraints that do not contradict or duplicate each other is equal to

$$m_n = 6n - k_1 - 2k_2 - 3k_3 - 4k_4 - 5k_5 - 6k_6.$$  \hspace{1cm} (6.6.1)

The formal number of degrees of freedom characterizes the mobility of a model. A graph constructed for a model may contain loops. If the graph constructed for a certain set of model elements is a loop and the formal number of degrees of freedom of these elements is less than or equal to six, then this set of model elements represents a whole rigid unit.

The minimum number of elements of a loop that does not contain fully fixed elements and forms a whole rigid unit is equal to three. If a loop does not contain fully fixed items, the maximum number of elements of the loop forming a rigid unit is equal to six. Indeed, the number of vertices in the loop is equal to the number of edges; thus, $k_1 + k_2 + k_3 + k_4 + k_5 + k_6 = n$. Suppose that a loop does not contain fully fixed items—i.e., $k_6 = 0$. The left-hand side of (6.6.1) takes a minimum value at $k_5 = n$, and $k_1 = k_2 = k_3 = k_4 = 0$.
Thus, the equation $6 = 6n - 5n$ implies that the maximum number of elements of the model forming a rigid unit is equal to six. Analyzing the graph, we can find groups of model elements that are rigid units, and simplify the solution of the system of equations of the geometric constraints by selecting out the equations for these groups into separate subsystems. The process of searching for groups of model elements that are rigid units is included in the decomposition.

A subgraph of the group of model elements and geometric constraints that forms a rigid unit is called a **cluster**. A result of decomposition is a selection of clusters from the system of equations.

Using formal analysis of the number of degrees of freedom, we can select subgraphs whose corresponding subproblems can be solved independently. To do this it is necessary to find subgraph units and articulation points. An articulation point can be a solid in the given space, through which and only through which one group of objects is related to another group of objects. If an articulation point is found for two subgraphs, the problem can be divided into two independent subproblems, and the subproblems can be solved one by one.

As an example, we construct a graph for the two-dimensional sketch shown in Fig. 6.6.1. Point $p_1$ of the sketch is fixed. Point $p_2$ is related to point $p_1$ by horizontal dimension $a$ and by the horizontality of segment $p_1p_2$. Point $p_3$ is related to point $p_2$ by vertical dimension $b$ and the fixed angle $p_1p_2p_3$. Point $p_4$ is related to point $p_1$ by the verticality of segment $p_1p_4$ and by the horizontality of segment $p_3p_4$. The graph of the elements and geometric constraints of the sketch is shown in Fig. 6.6.2. The sketch has eight degrees of freedom. The geometric constraints remove all eight degrees of freedom. The formal number of degrees of freedom of the sketch is zero.

![Fig. 6.6.1](image1)

![Fig. 6.6.2](image2)

The cluster in this example is the subgraph consisting of point $p_1$, point $p_2$, point $p_3$, horizontal dimension $a$, vertical dimension $b$ and angle $p_1p_2p_3$. If point $p_1$ is unfixed, then the cluster receives two degrees of freedom and can be moved in two-dimensional space. If the horizontality of segment $p_1p_2$ is removed, then the cluster gets another degree of freedom, and can be rotated. We see that this cluster behaves as a solid in two-dimensional space. In this example, the cluster is fixed. Using decomposition, the complete system of equations can be divided into two subsystems: a system of equations for the cluster, and a system of equations for the remaining objects. First the system of equations for the cluster must be solved, and then the system of equations for point $p_4$ must be solved.
The decomposition procedure is applied to the system of equations iteratively until after yet another division at least one cluster is found. The graph of the system of equations is rewritten for every iteration. The procedure stops when no more clusters are found. Thus, the decomposition may have many levels. At each level, the problem has dimension less than the dimension of the original problem. Graph analysis is a powerful tool for decomposition, but it does not use geometric information, and relies only on discrete data; thus, the correctness of the results of the decomposition depends on how correctly the graph showing the geometric constraints and degrees of freedom of the model elements is constructed.

As a result of the decomposition, the initial problem is reduced to a problem of smaller dimension for clusters and objects that are not included in the clusters. First, the position of model elements satisfying the geometric constraints is determined for each cluster individually, and then the corresponding system of equations for the clusters and the model elements that are not included in the clusters is solved. The arrangement of the model elements within a single cluster is carried out by solving the corresponding system of equations. For each cluster, its own most effective method is used.

After solving the system of equations of the geometric constraints, reconstruction of the model is carried out in accordance with the found solution.

Exercises

1. How can the elements of a model be linked using geometric constraints?
2. How can a geometrically similar model be constructed using geometric constraints?
3. Describe the algorithm for solving a system of equations of geometric constraints.
4. Formulate your criteria of behavior of geometric model parameters.