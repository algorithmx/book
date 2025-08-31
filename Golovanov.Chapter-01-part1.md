INTRODUCTION

The development of computers makes it possible to create numerical models of various objects and to perform experiments with them. Numerical models are used in systems that are used for design (CAD), engineering (CAE), and manufacturing (CAM) of the modeled object. In all these systems it is necessary to describe the geometric shape of the modeled object up to certain precision. During the development of these systems (a new branch of mathematics) called "geometric modeling" was created. Geometric modeling studies the methods used to construct numerical geometric models of real and imaginary objects, as well as methods to control these models.

A geometric model consists of a shape description for the modeled object along with a description of the relationships among the model elements. To allow changes of these models and creation of similar models, the construction tree describing the sequence and methods used in model construction is frequently included with the model. The elements of a geometric model are usually provided by attributes carrying information about their physical and other properties.

The development of geometric modeling began with computer drawing systems. Wireframe and surface modeling came later on. Parametric and solid modeling systems have dramatically changed the way designers work. They made it possible for designers to capture their ideas in three-dimensional models and not just in flat drawings. To describe the relationship of model elements, variational methods have been used. Another step in the development of geometric modeling was direct modeling, which further empowered engineers and designers by circumventing the constraints of history-based modelers.

The objects around us occupy a finite amount of space. In order to model these objects we need to describe the part of the space they occupy. In certain cases it can be done using the volume elements of the modeled object. These volume elements are called voxels. Often such volume elements are cubes, prisms, or pyramids. These models are used in the cases where the attributes of the volume elements are more important than the geometric shape of the whole model.

Within certain accuracy limitations, the geometric shape of an object can be described using flat faces. This kind of description is called polygonal representation. A polygonal representation describes curved surfaces using a set of triangular or quadrangular plates. Usage of flat faces significantly simplifies work with the model. Polygonal models are typically based on measurements of real objects, or on other models. Polygonal representation is widely used for visualization of geometric models.

Many objects can be constructed using translational and rotational motion. Surface elements of such objects can be specified by a plane, a spherical surface, a
cylindrical surface, a conical surface, or a toroidal surface. All of these surfaces divide the space into two parts, and one can specify on which side of the surface the internal volume of the modeled object is situated. With the help of these surfaces, it is possible to construct a geometric model by performing operations on primitives. The primitives usually include a rectangular prism, a triangular prism, a sphere, a cylinder, a cone, and a torus. This approach is called constructive solid geometry. Nowadays constructive solid geometry is rarely used.

The most general way to describe the geometric form of a modeled object is to use free-form surfaces, represented explicitly. In this approach, a surface representation of the modeled object is given by a set of faces joined along the edges. The faces contain information about their boundaries and relations to their neighbors. They are joined so that the outer side of one face merges into the outer side of the adjacent face. Faces may have an arbitrary form. This approach to describing a modeled object is called boundary representation. It makes it possible to perform many operations on models while maintaining a standard representation of their internal organization. A boundary representation contains a precise description of the boundary of the modeled object that separates it from the rest of the space. Boundary representation is used in all modern CAD systems.

Variational relations are established between the elements of a geometric model to align points, axes, and surfaces, as well as to specify tangency and many other relations. Interdependencies of model elements are called geometric constraints. Different dimensions of one or several objects may be related to each other. Using these relations one can easily edit the model and create similar models. Typically, there is more than one way to satisfy a set of geometric constraints. Most computer-aided design systems have modules that impose geometric constraints on the elements of the geometric model. Geometric modeling studies methods of finding a solution that meets the demands posed by an actual problem.

Geometric modeling relies on different areas of mathematics, primarily differential geometry and numerical methods. Geometric modeling is closely related to programming; it takes advantage of the features of object-orientation: encapsulation, inheritance, polymorphism. For example, object-oriented programming allows creation of curves and surfaces that have some set of common methods, hiding the implementation of these methods for each particular curve and surface as well as data used to create them.

The geometric model is used in rendering the modeled object, checking the correct assemblage of the object from its elements, performing kinematic verification, calculating inertial characteristics, computing the trajectory of cutting tools, designing equipment, and other preliminary stages of modeled object production. Geometric models can help carry out numerical experiments and manufacture the modeled object. Attributes of the model elements describing physical and other properties of the modeled object are used for this purpose.

Geometric modeling can reduce the time and material costs for production of designed objects and improve their quality. Geometric modeling automates the work of designers, engineers, architects, and technologists, enabling them to avoid routine operations and concentrate on the creative aspects of their work.
CURVES

A geometric model contains a description of a shape of a modeled object. A geometric shape is described by surfaces. Curves are used for constructing the surfaces. Geometric design begins with curves. Geometric modeling uses curves that are easy to manipulate. Curves are controlled by changing the data used to construct them. The curves may be constructed using analytic functions, a set of points, or other curves and surfaces.

1.1. Curves

Suppose we have a Cartesian coordinate system with a fixed orthonormal basis in three-dimensional Euclidean space. A column of point coordinates and vector components will be denoted by lowercase letters, in bold—for example,

$$ \mathbf{p} = \begin{bmatrix} p_1 \\ p_2 \\ p_3 \end{bmatrix}. $$

A transformation that converts the origin of the Cartesian coordinate system to a point in space with specified coordinates is called a radius vector. The position of a point in space will be described by its radius vector.

The scalar product of vectors \( \mathbf{a} \) and \( \mathbf{b} \) will be denoted as \( \mathbf{a} \cdot \mathbf{b} \). The vector product of \( \mathbf{a} \) and \( \mathbf{b} \) will be denoted as \( \mathbf{a} \times \mathbf{b} \).

A curve is a vector function

$$ \mathbf{r}(t) = \begin{bmatrix} r_1(t) \\ r_2(t) \\ r_3(t) \end{bmatrix}, \quad (1.1.1) $$

of the scalar parameter \( t \), taking values in the interval \([t_{\text{min}}, t_{\text{max}}]\). Let the coordinates \( r_1(t), r_2(t), r_3(t) \) of the curve's point \( \mathbf{r}(t) \) be single-valued continuous functions of the parameter \( t \). This is called a parametric description of the curve.

A point of the curve is called regular if the length of the first derivative with respect to the parameter does not become zero at this point. Otherwise, the point is called singular.

A curve is called periodic if there exists \( p > 0 \), such that \( \mathbf{r}(t + kp) = \mathbf{r}(t) \), where \( k \)
is an integer. To avoid an ambiguity, the domain of periodic curve must lie within one period. A periodic curve is called a cyclic closed curve, if \( p = t_{\text{max}} - t_{\text{min}} \).

The parameter domain of the curve is a segment \([t_{\text{min}}, t_{\text{max}}]\) in one-dimensional space. The curve is a continuous mapping of the segment of the numerical axis onto three-dimensional space.

Here we introduce the notation for derivatives of the curve:

$$
r' = \frac{dr}{dt}, \quad r'' = \frac{d^2r}{dt^2}, \quad r''' = \frac{d^3r}{dt^3}.
$$

At a regular point, the derivative of the curve is a vector directed along the tangent to the curve in the direction in which the parameter increases. The unit vector

$$
t = \frac{r'}{s'}, \quad (1.1.2)
$$

where \( s' = \sqrt{r' \cdot r'} \) is the length of the first derivative of the curve, is called a tangent vector. The length of the first derivative depends on the parameterization method. If the arc length of the curve, measured from some of its points, is used as a parameter, then the length of the derivative is equal to unity. The vector function \( r(s) \), where \( s \) is arc length, is called a curve with natural parameterization.

Suppose we are given a curve with natural parameterization. Then the tangent vector is the first derivative of the curve:

$$
t = \frac{dr}{ds}.
$$

Construct a plane perpendicular to the first derivative at a given point of the curve. This plane is called the normal plane of the curve. The plane in which the first and the second derivatives of the curve lie is called an osculating plane. If the second derivative of the curve is parallel to the first derivative, or its length is equal to zero, one can take any plane in which the first derivative of the curve is situated as the osculating plane. A point of the curve at which the vectors of the first and the second derivatives of the curve are collinear is called a rectifying point. Rectifying points do not depend on the parameterization of the curve. The name osculating plane is due to the fact that it passes through a given point on the curve with the highest order of tangency, and can be defined as the limiting position of the plane constructed on three infinitely close points of the curve. A plane that is perpendicular to both a normal and an osculating plane is called a rectifying plane.

The unit vector orthogonal to the tangent vector lying in the osculating plane and directed towards the second derivative (in the direction of the concavity of the curve) is called the principal normal of the curve. Denote the principal normal as \( n \). Vectors of the first and the second derivatives of the curve with natural parameterization are orthogonal, because

$$
\frac{d(t \cdot t)}{ds} = 2t \cdot \frac{dt}{ds} = 2t \cdot \frac{d^2r}{ds^2} = 0.
$$

Hence, the second derivative of the curve with natural parameterization is directed along the principal normal.
$$
\frac{dt}{ds} = \frac{d^2 r}{ds^2} = kn.
$$

The coefficient \( k \) denotes the curvature of the curve. The inverted value of the curvature is equal to the radius of the circle tangent to the curve at the given point.

A unit vector along the line of intersection of the normal and the rectifying planes that forms a right-handed triple with the tangent and normal vectors is called a binormal of the curve, and is denoted as \( b \). A tangent vector \( t \), principal normal \( n \), and binormal \( b \) of the curve are shown in Fig. 1.1.1.

![Fig. 1.1.1.](image)

By definition, the binormal is orthogonal to the tangent vector and to the principal normal. Therefore, it follows that

$$
\frac{d(b \cdot t)}{ds} = t \cdot \frac{db}{ds} + b \cdot \frac{dt}{ds} = t \cdot \frac{db}{ds} = 0,
$$

$$
\frac{d(b \cdot b)}{ds} = 2b \cdot \frac{db}{ds} = 0.
$$

Thus, the derivative of the binormal with respect to the arc length of the curve is orthogonal to vectors \( t \) and \( b \), and hence it is parallel to the principal normal. It is usually written in the form

$$
\frac{db}{ds} = -\chi n.
$$

The coefficient \( \chi \) is called the torsion of the curve.

Using the derivatives of tangent and binormal vectors of the curve with natural parameterization, we find the derivative of the normal with respect to arc length:

$$
\frac{dn}{ds} = \frac{d(b \times t)}{ds} = \frac{db}{ds} \times t + b \times \frac{dt}{ds} = -\chi n \times t + kb \times n = \chi b - kt.
$$

The Frenet-Serret formulae
$$
\frac{dt}{ds} = kn, \quad \frac{dn}{ds} = \chi b - kt, \quad \frac{db}{ds} = -\chi n
$$

express the differential relations between tangent vector \( t \), principal normal \( n \), and binormal \( b \). Vectors \( t, n, \) and \( b \) are related by

$$
b = t \times n, \quad t = n \times b, \quad n = b \times t
$$

and can be used as the unit vectors of the local coordinate system associated with the curve.

The set of the normal, osculating, and rectifying planes, and the vectors \( t, n, b \), is called the moving trihedral of the curve. The torsion of the curve is equal to the angular rotation velocity of the moving trihedral around the tangent vector as it moves along the curve. When the torsion is zero, the curve is planar. The total vector of the angular rotation velocity of the moving trihedral with respect to the path traveled along the curve is called the Darboux vector. It is equal to

$$
\omega = kb + \chi t.
$$

The Darboux vector provides a mechanical meaning to the Frenet-Serret formulae, with which the latter have the form

$$
\frac{dt}{ds} = \omega \times t, \quad \frac{dn}{ds} = \omega \times n, \quad \frac{db}{ds} = \omega \times b.
$$

The curvature and torsion of a curve with natural parameterization can be calculated using the following formulae:

$$
k = \left| \frac{d^2 r}{ds^2} \right|, \quad \chi = \frac{1}{k^2} \left( \frac{dr}{ds} \times \frac{d^2 r}{ds^2} \right) \cdot \frac{d^3 r}{ds^3}.
$$

Typically, the parameterization of the curve is not natural. Using the above formulae for a curve with natural parameterization, we obtain the formulae relating the principal normal, binormal, curvature, and torsion to the derivatives of the curve for arbitrary parameterization. The derivatives of a curve with different parameterization are related by:

$$
\frac{dr}{dt} = \frac{dr}{ds} \frac{ds}{dt},
$$

$$
\frac{d^2 r}{dt^2} = \frac{d^2 r}{ds^2} \left( \frac{ds}{dt} \right)^2 + \frac{dr}{ds} \frac{d^2 s}{dt^2},
$$

$$
\frac{d^3 r}{dt^3} = \frac{d^3 r}{ds^3} \left( \frac{ds}{dt} \right)^3 + 3 \frac{d^2 r}{ds^2} \frac{ds}{dt} \frac{d^2 s}{dt^2} + \frac{dr}{ds} \frac{d^3 s}{dt^3}.
$$
In the general case, the curvature of the curve is calculated by the formula

$$ k = \frac{|r' \times r''|}{|r'|^3}. $$  

(1.1.3)

At the points of the curve with nonzero curvature, the principal normal, binormal, curvature radius \( \rho \), and torsion of the curve are calculated by the formulae

$$ k_n = \frac{r'' - r' \cdot r''}{|r'|^2}, \quad b = \frac{r' \times r''}{k |r'|^3}, \quad \rho = \frac{|r'|^3}{|r' \times r''|}, \quad \chi = \frac{(r' \times r'') \cdot r'''}{|r' \times r''|^2}. $$  

(1.1.4)

It is obvious from the above formulae that the curvature is always non-negative, but the torsion may have any sign. If the curvature is zero, then the directions of the principal normal, binormal, and torsion are not defined. If the curvature is zero at every point of the curve, then the curve is a segment of a straight line. In this case the principal normal may have any direction in the normal plane. If the first, second, and third derivatives of the curve are parallel, then the torsion of the curve is zero and the curve is planar.

1.2. Analytic Curves

We will designate curves as analytic curves if their coordinates in some local coordinate system can be described by analytic functions without using points, vectors, or other curves.

Local coordinate systems, in which the curves have the canonical form, are used for analytic curves.

Construct a local rectangular Cartesian coordinate system with the origin at point \( p \) and the basis vectors \( i_x, i_y, i_z \). The curve with coordinates in the local system \( x(t), y(t), z(t) \) is described by the vector function

$$ r(t) = p + x(t) i_x + y(t) i_y + z(t) i_z. $$  

(1.2.1)

Let \( p_i \) be coordinates of the origin \( p \) of the local coordinate system, \( x_i \) – components of the basis vector \( i_x \), \( y_i \) – components of the basis vector \( i_y \), and \( z_i \) – components of the basis vector \( i_z \), \( i=1,2,3 \). Then the analytical curve is a function

$$
\begin{bmatrix}
r_1(t) \\
r_2(t) \\
r_3(t)
\end{bmatrix} =
\begin{bmatrix}
p_1 \\
p_2 \\
p_3
\end{bmatrix} +
\begin{bmatrix}
x_1 & y_1 & z_1 \\
x_2 & y_2 & z_2 \\
x_3 & y_3 & z_3
\end{bmatrix} \cdot
\begin{bmatrix}
x(t) \\
y(t) \\
z(t)
\end{bmatrix}.
$$

The coordinates of the curve (1.2.1) are
$$ r_i(t) = p_i + x(t) i_x + y(t) i_y + z(t) i_z. $$

By changing the position or orientation of the analytic curve described in this way, the coordinates of the origin of the local coordinate system and its basis vectors change, but analytic functions of the curve remain unchanged, keeping their canonical form.

Let us consider examples of analytic curves. We describe an elliptical arc by the vector function

$$ r(t) = p + a \cos t i_x + b \sin t i_y, \quad (1.2.2) $$
$$ t_{\text{min}} \leq t \leq t_{\text{max}}, $$

where \( a \) and \( b \) are the ellipse's semi-axes, \( 0 \leq t_{\text{min}} < 2\pi \) is the initial arc parameter, and \( t_{\text{min}} < t_{\text{max}} < a + 2\pi \) is the final arc parameter. We place the origin \( p \) of the local coordinate system at the center of the ellipse. The basis vectors \( i_x \) and \( i_y \) are directed along its semi-axes. Scalar functions \( x(t) = a \cos t \) and \( y(t) = b \sin t \) of the ellipse are related by equation

$$ \left( \frac{x}{a} \right)^2 + \left( \frac{y}{b} \right)^2 = 1. $$

With the domain of the parameter \( t_{\text{max}} = t_{\text{min}} + 2\pi \) we get an ellipse. An ellipse is a periodic closed curve. It is shown in Fig. 1.2.1.

![Fig. 1.2.1.](image)

If \( t_{\text{max}} - t_{\text{min}} < 2\pi \), then we get an elliptical arc. When \( a = b \) and \( t_{\text{max}} = t_{\text{min}} + 2\pi \), we get a circle.

A hyperbolic arc can be described by the vector function

$$ r(t) = p + a \cosh t i_x + b \sinh t i_y, \quad (1.2.3) $$
$$ t_{\text{min}} \leq t \leq t_{\text{max}}, $$

where \( a \) and \( b \) are the real and imaginary semi-axes of the hyperbola, \( t_{\text{min}} \) is the initial arc parameter, and \( t_{\text{min}} < t_{\text{max}} \) is the final arc parameter. Scalar functions \( x(t) = a \cosh t \) and \( y(t) = b \sinh t \) of a hyperbola are related by the equation

$$ \left( \frac{x}{a} \right)^2 - \left( \frac{y}{b} \right)^2 = 1. $$

We can describe a parabolic arc by the vector function

$$ r(t) = p + ft^2 i_x + 2ft i_y, $$
$$ t_{\text{min}} \leq t \leq t_{\text{max}}, $$

where \( f \) is the focal length of the parabola, \( t_{\text{min}} \) is the initial arc parameter, and \( t_{\text{min}} < t_{\text{max}} \) is the final arc parameter. The scalar functions \( x(t) = ft^2 \) and \( y(t) = 2ft \) of a parabola are related by the equation

$$ 4fx - y^2 = 0. $$

The focus of the parabola is located at the point with radius vector \( p + fi_x \). The directrix of the parabola is a straight line \( r(w) = p - f i_x + w i_y \).

A helix of radius \( r \), with step \( h \) and parametric length \( t_{\text{max}} - t_{\text{min}} \), can be described by the vector function

$$ r(t) = p + r \cos t i_x + r \sin t i_y + \frac{ht}{2\pi} i_z. $$ (1.2.3)

We set the origin of the helix's local coordinate system at the intersection point of the axis and the end plane of the helix. The basis vector \( i_z \) is directed along the helix's axis. If the basis vectors in the local coordinate system are orthogonal and have equal lengths, we get a cylindrical helix; see Fig. 1.2.2.

![Fig. 1.2.2.](image)

When \( h = 0 \), formula (1.2.3) describes the radius vector of a circle or its arc in the plane of the basis vectors \( i_x \) and \( i_y \).

### 1.3. Curves Constructed on a Set of Points

Consider the curves passing through the given points \( p_0, p_1, \ldots, p_n \) when the parameter values are \( t_0, t_1, \ldots, t_n \). Points \( p_i, i = 0, 1, \ldots, n \) are called control points of the curve, and the parameters \( t_i, i = 0, 1, \ldots, n \) are called knots. The knot parameter value for each subsequent control point \( p_{i+1} \) must be greater than the knot parameter value of the previous control point \( p_i; t_i < t_{i+1}, i = 0, \ldots, n-1 \). Curves constructed on a set of equidistant knots are called uniform curves. For uniform curves the following equality is satisfied:

$$ t_i - t_{i-1} = t_{i+1} - t_i. $$

Curves constructed on a set of non-equidistant knots are called non-uniform curves.

A polyline is the simplest curve constructed on a set of points. It consists of segments sequentially connecting the given points. A radius vector of a polyline is
defined by

$$ r(t) = \frac{t_{i+1} - t}{t_{i+1} - t_i} p_i + \frac{t - t_i}{t_{i+1} - t_i} p_{i+1}, $$  

(1.3.1)

where \( t_i \leq t \leq t_{i+1} \). The first derivative of the polyline at control points \( p_i \) has a discontinuity in length and direction. In some cases the parameter value at point \( p_i \) can be taken as the point number: \( t_i = i \). A polyline is shown in Fig. 1.3.1.

A polyline may be closed; in this case, the first control point is also the last one. The polyline has a number of favorable properties: to work with it require minimal computations, and the projection of a polyline is also a polyline.

![Fig. 1.3.1.](image)

We get a line segment when the polyline contains a single segment. The radius vector of the segment constructed on points \( p_0 \) and \( p_1 \) is calculated by the formula

$$ r(t) = (1-t)p_0 + tp_1, \quad 0 \leq t \leq 1. $$

Curves constructed on a set of points and having a certain smoothness are called splines. The term "spline" for curves is borrowed from the name of a drawing tool—an elastic flexible ruler that can be bent so as to pass through particular points.

The Lagrange interpolation formula allows constructing a curve on given points as

$$ r(t) = \sum_{i=0}^{n} L_i^n(t)p_i, \quad t \in [t_0, t_n], $$  

(1.3.2)

where the coefficients \( L_i^n(t) \) are equal to unity at \( t = t_i \) and equal to zero at the remaining knots \( t_j, j \neq i \).

The coefficients \( L_i^n(t) \) are polynomials of degree \( n-1 \)

$$ L_i^n(t) = \lambda_i(t - t_0)...(t - t_{i-1})(t - t_{i+1})...(t - t_n). $$

Setting \( L_i^n(t_i) = 1 \) implies that \( \frac{1}{\lambda_i} = (t_i - t_0)...(t_i - t_{i-1})(t_i - t_{i+1})...(t_i - t_n) \) and
Thus, the radius vector of the Lagrange spline is described by

$$ r(t) = \sum_{i=0}^{n} \frac{\prod_{j=0, j \neq i}^{n} (t - t_j)}{\prod_{j=0, j \neq i}^{n} (t_i - t_j)} p_i. $$  

(1.3.4)

The Lagrange spline can be written as

$$ r(t) = \sum_{i=0}^{n} \frac{W_{0,n}(t)}{(t - t_i)W_{0,n}'(t_i)} p_i, $$

where \( W_{0,n}(t) = (t - t_0)(t - t_1)...(t - t_{n-1})(t - t_n) \) and

$$ W_{0,n}'(t_i) = \left. \frac{dW_{0,n}}{dt} \right|_{t_i} = (t_i - t_0)...(t_i - t_{i-1})(t_i - t_{i+1})...(t_i - t_n). $$

The shape of the spline is affected not only by the location of the control points, but also by the values of the knots. In Fig. 1.3.2, we see a Lagrange spline in which the change of the knot parameter values is proportional to the distance between adjacent points

$$ \frac{t_{i+1} - t_i}{t_i - t_{i-1}} \approx \frac{|p_{i+1} - p_i|}{|p_i - p_{i-1}|}. $$

A Lagrange spline with uniform parameterization (\( t_i = i \)) is shown in Fig. 1.3.2 by the thin dashed line. One can see from Fig. 1.3.2 that the shape of the curve is influenced not only by the positions of the control points, but also by the corresponding parameter values—i.e., by the curve parameterization.
The Newton spline passing through the given points takes the form

$$ r(t) = a_0 + a_1(t - t_0) + a_2(t - t_0)(t - t_1) + \ldots + a_n(t - t_0)(t - t_1)\ldots(t - t_{n-1}). $$ (1.3.5)

We derive vectors \( a_i \) from the conditions for the vector function \( r(t) \) to pass through the points \( p_i \) at parameter values \( t_i, i=0,1,\ldots,n \)

$$
\begin{align*}
p_0 &= a_0, \\
p_1 &= a_0 + a_1(t_1 - t_0), \\
p_2 &= a_0 + a_1(t_2 - t_0) + a_2(t_2 - t_0)(t_2 - t_1), \\
&\vdots \\
p_n &= a_0 + a_1(t_n - t_0) + a_2(t_n - t_0)(t_n - t_1) + \ldots + a_n(t_n - t_0)(t_n - t_1)\ldots(t_n - t_{n-1}). \quad (1.3.6)
\end{align*}
$$

The matrix of this system of equations is triangular and the system can be solved by direct iteration. The first equation of the system (1.3.6) provides \( a_0 \). Substituting this result into the second equation will yield \( a_1 \). From the third equation we find \( a_2 \), and continue similarly until we reach \( a_n \). Inserting an additional point \( p_{n+1} \) into the spline will extend the system (1.3.6) by one more equation, leaving the other equations unchanged. This is an advantage of the Newton spline over the Lagrange spline in the construction of curves with an increasing number of points. Formulas (1.3.2) and (1.3.5) describe the same curve. Lagrange and Newton splines are rarely used in geometric modeling because of their behavior, including strong dependence on the parametric values at the control points.

We construct a cubic spline, with continuous first and the second derivatives of the radius vector, on a given set of control points. We describe the radius vector of the curve at each segment between adjacent control points by a cubic polynomial. We
denote the second derivatives of the radius vector of the spline at control points \( t_i \) as \( s_i \). The second derivative of the radius vector of the spline on the segment \( t_i \leq t \leq t_{i+1} \), by definition, is a linear function of the parameter \( t \):

$$
\frac{d^2 r}{dt^2} = s_i \frac{t_{i+1} - t}{t_{i+1} - t_i} + s_{i+1} \frac{t - t_i}{t_{i+1} - t_i}.
$$

After double integration we obtain

$$
r(t) = s_i \frac{(t_{i+1} - t)^3}{6(t_{i+1} - t_i)} + s_{i+1} \frac{(t - t_i)^3}{6(t_{i+1} - t_i)} + c_1 t + c_2.
$$

Integration constants \( c_1 \) and \( c_2 \) can be determined from the boundary conditions of the segment \( r(t_i) = p_i \) and \( r(t_{i+1}) = p_{i+1} \). After calculation we obtain

$$
r(t) = s_i \frac{(t_{i+1} - t)^3}{6(t_{i+1} - t_i)} + s_{i+1} \frac{(t - t_i)^3}{6(t_{i+1} - t_i)} + \left( \frac{p_i}{t_{i+1} - t_i} - s_i \frac{t_{i+1} - t_i}{6} \right)(t_{i+1} - t) + \\
+ \left( \frac{p_{i+1}}{t_{i+1} - t_i} - s_{i+1} \frac{t_{i+1} - t_i}{6} \right)(t - t_i).
$$ (1.3.7)

Equation (1.3.7) describes a cubic polynomial on interval \( t_i \leq t \leq t_{i+1} \) and contains two unknown variables, \( s_i \) and \( s_{i+1} \). To define them, we set the first derivative of the spline at the right end of the segment \( t_{i+1} \leq t \leq t_i \) to the first derivative of the spline at the left end of the segment \( t_i \leq t \leq t_{i+1} \). After differentiating (1.3.7) and by substituting \( t = t_i \), we obtain

$$
\left. \frac{dr}{dt} \right|_{t_i} = \frac{(2s_i + s_{i+1})(t_{i+1} - t_i)}{6} + \frac{p_{i+1} - p_i}{t_{i+1} - t_i}.
$$

After replacing \( i \) in (1.3.7) by \( i-1 \), we differentiate it and substitute \( t = t_i \). We get

$$
\left. \frac{dr}{dt} \right|_{t_i} = \frac{(2s_i + s_{i-1})(t_i - t_{i-1})}{6} + \frac{p_i - p_{i-1}}{t_i - t_{i-1}}.
$$

Equating the right-hand sides of the last two relations, we arrive at the following equation:

$$
s_{i-1}(t_i - t_{i-1}) + 2s_i(t_{i+1} - t_{i-1}) + s_{i+1}(t_{i+1} - t_i) = 6 \frac{p_{i+1} - p_i}{t_{i+1} - t_i} - 6 \frac{p_i - p_{i-1}}{t_i - t_{i-1}}.
$$ (1.3.8)

These equations can be constructed for \( n-1 \) control points. The \( n+1 \) unknowns of
the vectors, $s_n$, must be determined. Two missing equations to determine all the unknowns are built from the boundary conditions of the curve. For example, if we assume that the ends of the curve are free, then we have $s_0 = s_n = 0$. In some cases, if we have $s_0 = s_1$, $s_n = s_{n-1}$, then the spline will have constant curvature at the endpoints. Additional conditions depend on the geometric conditions in each particular case. If it is necessary to construct a closed curve, then the number of unknowns will be the same as the number of equations. Thus, the unknown vectors of the second derivatives $s_i$ at the control points can be found from a system of linear equations. The matrix of this system of linear equations is tridiagonal, which simplifies the system. The right-hand side of (1.3.7) can be written as

$$ r(t) = (1 - w)p_i + wp_{i+1} + \left( (-2w + 3w^2 - w^3)s_i + (-w + w^3)s_{i+1} \right) \frac{(t_{i+1} - t_i)^2}{6}, $$

where $w = \frac{t - t_i}{t_{i+1} - t_i}$, and $t_i \leq t \leq t_{i+1}$. The resulting curve is called a cubic spline.

The shape of the spline is affected by the locations of the control points and by the knot values. If the parameter knot values can be chosen at will, then in order to avoid loops and unreasonable spline bending, it is desirable to use parameterization proportional to the natural parameterization of the spline. In natural parameterization of the curve, that parameter is assumed to be the length of the curve measured from a certain starting point. Good results are also obtained by parameterization, in which the change of parameter knot values is proportional to the distance between adjacent points.

Fig. 1.3.3 shows a cubic spline with parameter knot values changing in proportion to the distance between adjacent points. The thin dashed line in Fig. 1.3.3 indicates a cubic spline with uniform parameterization ($t_i = i$). With uniform parameterization, the shape of the spline is larger since the points are less evenly spaced.

It is possible to construct splines of higher degree by analogy with a cubic spline, when the third and higher-order derivatives of the radius vector are continuous at the control points. In the limiting case, when continuity of $n$-order derivatives at $n+1$ control points is preserved, we have a Lagrange or a Newton spline.

If we are given a sequence of $m+1$ points through which the curve must pass, and the derivatives of its radius vector at these points, we can use this information to construct a spline that is described by a polynomial of degree $2m+1$. These types of
splines are named after the French mathematician C. Hermite. We consider the special case of a Hermite spline for \( m = 1 \).

A polyline can be regarded as a composite curve constructed from segments of a straight line. By analogy, one can construct a composite cubic curve consisting of third-order Hermite splines smoothly conjoined to each other. Let us construct a composite Hermite spline passing through a given sequence of points and having the given derivatives at these points. Let the radius vectors of these points be \( p_i \), the derivative vectors of the curve at these points be \( q_i \), and the parameter value at these points be \( t_i \) (\( t_i < t_{i+1} \)), where \( i = 0, 1, 2, \ldots, n - 1 \) — point numbers. Within the segment between the points \( p_i \) and \( p_{i+1} \), the composite Hermite spline is a third-degree polynomial of the local parameter \( w \)

$$
r(w) = a_0 + wa_1 + w^2a_2 + w^3a_3, \quad w = \frac{t - t_i}{t_{i+1} - t_i},
$$

as in Fig. 1.3.4.

![Fig. 1.3.4.](image)

The local parameter \( w \) varies from 0 to 1. We find vectors \( a_j, j = 0, 1, 2, 3 \) from the boundary conditions of the curve segment

$$
r_i(0) = p_i, \quad r_i(1) = p_{i+1}, \quad r_i'(0) = q_i, \quad r_i'(1) = q_{i+1}.
$$

After solving this system of equations and by substituting the values \( a_0, a_1, a_2, a_3 \) we obtain the relation for the radius vector of the Hermite spline

$$
r(t) = (1 - 3w^2 + 2w^3)p_i + (3w^2 - 2w^3)p_{i+1} + (w - 2w^2 + w^3)(t_{i+1} - t_i)q_i + (-w^2 + w^3)(t_{i+1} - t_i)q_{i+1} =
$$
$$
= \alpha_0(w)p_i + \alpha_1(w)p_{i+1} + \beta_0(w)(t_{i+1} - t_i)q_i + \beta_1(w)(t_{i+1} - t_i)q_{i+1},
$$

where \( w = \frac{t - t_i}{t_{i+1} - t_i}, \quad t_i \leq t \leq t_{i+1} \). The following notation for functions is introduced in (1.3.10):

$$
\begin{align*}
\alpha_0(w) &= 1 - 3w^2 + 2w^3, \\
\alpha_1(w) &= 3w^2 - 2w^3, \\
\beta_0(w) &= w - 2w^2 + w^3, \\
\beta_1(w) &= -w^2 + w^3.
\end{align*}
$$
The Hermite spline can be constructed when the derivatives at the control points are not given. If derivatives $q_i$ are unknown, they can be determined by constructing a vector Lagrange polynomial of second degree on three adjacent points $p_{i-1}, p_i, p_{i+1}$:

$$p(t) = p_{i-1} \frac{(t-t_i)(t-t_{i+1})}{(t_{i-1}-t_i)(t_{i-1}-t_{i+1})} + p_i \frac{(t-t_{i-1})(t-t_{i+1})}{(t_i-t_{i-1})(t_i-t_{i+1})} + p_{i+1} \frac{(t-t_{i-1})(t-t_i)}{(t_{i+1}-t_{i-1})(t_{i+1}-t_i)},$$

and, using $q_i$ as its derivative at $t=t_i$,

$$q_i = p_{i-1} \frac{t_i-t_{i+1}}{(t_{i-1}-t_i)(t_{i-1}-t_{i+1})} + p_i \frac{2t_i-t_{i-1}-t_{i+1}}{(t_i-t_{i-1})(t_i-t_{i+1})} + p_{i+1} \frac{t_i-t_{i-1}}{(t_{i+1}-t_{i-1})(t_{i+1}-t_i)}.$$

Derivatives at the endpoints of the spline can be derived from the condition that the second derivatives of the radius vector must vanish at these points. For this purpose we calculate the second derivatives for corresponding segments using (1.3.10) and by substitution of appropriate parameter values. As a result we obtain

$$q_0 = \frac{3}{2} \frac{p_1-p_0}{t_1-t_0} - \frac{1}{2} q_1,$$

$$q_n = \frac{3}{2} \frac{p_n-p_{n-1}}{t_n-t_{n-1}} - \frac{1}{2} q_{n-1}.$$

A third-degree composite Hermite spline with change of knot-parameter values proportional to the distance between adjacent control points is shown in Fig. 1.3.5. The thin dashed line in Fig. 1.3.5 indicates the composite Hermite spline of third degree with uniform parameterization ($t_i=i$).

![Fig. 1.3.5.](image)

A composite Hermite spline gives a reasonable approximation and requires less computation than the splines mentioned earlier. The second derivatives of the composite Hermite spline generally do not preserve continuity at the control points.

In Fig. 1.3.6 there are: A Lagrange spline (1), a cubic spline (2), and a composite Hermite spline (3), constructed using the identical data. We see that the splines behave differently.
Hermite and cubic splines are constructed for the purpose of an approximation. For ergonomic purposes, we use curves, which we shall consider further.

1.4. Bezier Curves

F. De Casteljau—and independently, P. Bezier—suggested the construction of curves where each point is calculated as a weighted sum of the given control points \( p_i \), \( i=0,1,\ldots,n \). These curves were named Bezier curves.

A Bezier curve of the first order (\( n=1 \)) is a segment

$$
r(t) = (1-t)p_0 + tp_1.
$$

The radius vector of the second-order (\( n=2 \)) Bezier curve is described by the relation

$$
r(t) = (1-t)^2p_0 + 2(1-t)tp_1 + t^2p_2.
$$

The radius vector of the cubic Bezier curve (\( n=3 \)) is described by the relation

$$
r(t) = (1-t)^3p_0 + 3(1-t)^2tp_1 + 3(1-t)t^2p_2 + t^3p_3.
$$

Fig. 1.4.1 shows a cubic Bezier curve and a polyline constructed on the same control points.
In the general case, the Bezier curve is described by the formula

$$ r(t) = \sum_{i=0}^{n} B^n_i(t)p_i = \sum_{i=0}^{n} \frac{n!}{i!(n-i)!} t^i (1-t)^{n-i} p_i , \quad t \in [0,1]. $$  

(1.4.1)

Points \( p_i \) are used in construction of the control polyline of the Bezier curve. Fig. 1.4.2 shows a Bezier curve constructed on eight points, as well as its control polyline.

The parameter domain of a Bezier curve of any degree lies in the unit interval: \( 0 \leq t \leq 1 \). A Bezier curve does not pass through any of its control points except the endpoints. Its control polyline is tangent to the Bezier curve at the endpoints. The smoothness of the Bezier curve is defined by the number of points. A Bezier curve can be given any desired shape by moving one or more control points.

A.R. Forrest established a link between coefficients at the control points of the Bezier curve and Bernstein polynomials. The coefficients at the control points of a Bezier curve are Bernstein functions

$$ r^{(n-1)}_i(t) = \sum_{i=0}^{n-1} B^{n-1}_i(t)p_{i+1}. $$  

(1.4.2)

A set of Bernstein functions for \( n \) is called its Bernstein basis. The coefficients at
$t^i(1-t)^{n-i}$ in (1.4.2) are equal to coefficients $r(t) = \sum_{i=0}^{n} f_i(t)p_i$, of the binomial formula: $Lr(t) = \sum_{i=1}^{n} f_i(t)p_{i-1}$. From this it follows that the Bernstein basis is a partition of unity:

$$r(t) = ((1-t)+tE)^n p_0$$

(1.4.3)

Fig. 1.4.3 and Fig. 1.4.4 show the Bernstein bases of third and fourth order, respectively.

Among Bernstein polynomials, only zero- and maximum-degree polynomials have maximum possible values $B^n_0(0) = 1$, $B^n_n(1) = 1$; that is why the Bezier curve passes only through initial $p_0$ and end $p_n$ points.

Bernstein functions satisfy the recurrence relation

$$B^n_i(t) = tB^{n-1}_{i-1}(t) + (1-t)B^{n-1}_i(t).$$

(1.4.4)

This relation is proved by direct substitution:

$$tB^{n-1}_{i-1}(t) + (1-t)B^{n-1}_i(t) = \frac{i}{n} \frac{n!}{i!(n-i)!} t^i(1-t)^{n-i} + \frac{n-i}{n} \frac{n!}{i!(n-i)!} t^i(1-t)^{n-i} = B^n_i(t).$$

Using this recurrence relation, we can compute all Bernstein functions. We start our calculations with the function $B^0_0(t) = 1$, then we obtain $B^1_0(t) = t$, $B^1_0(t) = 1-t$, ..., $B^n_0(t) = (1-t)^n$, $B^n_n(t) = t^n$. In this calculation it is assumed that the functions with one negative index are equal to zero.

Substitute the recurrence relation (1.4.4) into (1.4.1), single out the endpoints, and use the fact that $B^n_0(t) = (1-t)^n$, $B^n_n(t) = t^n$ to obtain
$$ r(t) = p_0(1-t)^n + p_n t^n + \sum_{i=1}^{n-1} \left( t B_{n-i}^{n-1}(t) + (1-t) B_{n-i}^{n-1}(t) \right) p_i = $$
$$ = (1-t) \left( p_0(1-t)^{n-1} + \sum_{i=1}^{n-1} B_{n-i}^{n-1}(t)p_i \right) + t \left( p_n t^{n-1} + \sum_{i=1}^{n-1} B_{n-i}^{n-1}(t)p_i \right) = $$
$$ = (1-t) \sum_{i=0}^{n-1} B_{n-i}^{n-1}(t)p_i + t \sum_{i=0}^{n-1} B_{n-i}^{n-1}(t)p_{i+1} = $$
$$ (1-t)r_0^{(n-1)}(t) + tr_1^{(n-1)}(t), $$

where \( r_0^{(n-1)}(t) = \sum_{i=0}^{n-1} B_{n-i}^{n-1}(t)p_i, \quad r_1^{(n-1)}(t) = \sum_{i=0}^{n-1} B_{n-i}^{n-1}(t)p_{i+1}. \)

Continuing this process of decomposition for \( r_0^{(n-1)} \) and \( r_1^{(n-1)} \), we finally arrive at the following equalities

$$ r_i^{(0)} = \sum_{j=0}^{i} B_{i-j}^{0}(t)p_j = p_i, \quad i = 0,1,...,n. $$

Denoting \( r(t) \) as \( r_0^{(n)}(t) \), and \( p_i \) as \( r_i^{(0)} \) we obtain a recurrence relation for calculating the point of the Bezier curve at \( k \)-th iteration of the recurrence relation

$$ r_i^{(k)} = (1-t)r_i^{(k-1)} + tr_{i+1}^{(k-1)}, \quad i + k \leq n. $$ (1.4.5)

The algorithm described by (1.4.5) is called De Casteljau’s algorithm. De Casteljau’s algorithm allows us to calculate any point of the Bezier curve using the control points without knowing anything about the Bernstein functions. A Bezier curve can be defined as a curve with points defined by the recurrence relation (1.4.5).

We illustrate De Casteljau’s algorithm by an example of quadratic Bezier curve; see Fig. 1.4.5.

![Fig. 1.4.5.](image)

A point with an arbitrary parameter \( t \) of a quadratic Bezier curve has the property that the tangent line at this point divides vectors \( p_1 - p_0 \) and \( p_2 - p_1 \) in the ratio \( \frac{t}{1-t} \). This follows from the notation of the Bezier curve of the second degree in the form
$$ r(t) = (1-t)(p_0 + (p_1 - p_0)(1-t)) + t(p_1 + (p_2 - p_1)t). $$

A point of the curve divides the segment of the tangent confined inside the control polyline in the same ratio. Thus, \( r_0^{(0)} = p_0, r_1^{(0)} = p_1, r_2^{(0)} = p_2 \), point A has the radius vector \( r_0^{(1)} \), point B has the radius vector \( r_1^{(1)} \), point C has the radius vector \( r_0^{(2)} = r(t) \). For the curves represented as \( r(t) = \sum_{i=0}^{n} f_i(t)p_i \), we define right-shift operator \( E \) and left-shift operator \( L \). The effects of these operators are described by

$$ Er(t) = \sum_{i=0}^{n-1} f_i(t)p_{i+1}, \quad Lr(t) = \sum_{i=1}^{n} f_i(t)p_{i-1}. $$

The shift operators are used in a compact form of De Casteljau's algorithm. If an operator is repeated \( i \) times, we use the powers of operators \( E \) and \( L \), for example \( E^i \) and \( L^i \).

Let us represent the control points \( p_i \) as curves \( p_i = \sum_{j=0}^{n} \delta_{ij} p_j \), where \( \delta_{ij} = 1 \) for \( i = j \) and \( \delta_{ij} = 0 \) for \( i \neq j \).

The Bezier curve constructed on the control points \( p_i, i = 0, 1, \ldots, n \), may be written as

$$ r(t) = ((1-t) + tE)^n p_0 \quad \text{or} \quad r(t) = ((1-t)L + t)^n p_n. $$

Indeed, \( ((1-t) + tE)^n p_0 = \sum_{i=0}^{n} C_{nt}^i (1-t)^{n-i} E^i p_0 = \sum_{i=0}^{n} B_{ni}(t)p_i \) due to \( E^i p_0 = p_i \).

Similarly, \( ((1-t)L + t)^n p_0 = \sum_{i=0}^{n} C_{nt}^i (1-t)^{n-i} L^{n-i} p_n = \sum_{i=0}^{n} B_{ni}(t)p_i \) due to \( L^{n-i} p_n = p_i \).

### 1.5. Bezier Curves and Conic Sections

A quadratic Bezier curve

$$ r(t) = (1-t)^2 p_0 + 2(1-t)t p_1 + t^2 p_2 $$  

(1.5.1)

is a planar curve and represents the second-degree polynomial of a parameter. Ellipses, parabolas, and hyperbolas are represented as second-degree functions of the coordinates. A question arises: is it possible to represent some part of a conic section by a second-order Bezier curve?

Suppose \( l_1 = a_1 x + b_1 y + c_1 \) and \( l_2 = a_2 x + b_2 y + c_2 \), where \( x \) and \( y \) are Cartesian
coordinates in some two-dimensional space, and \(a_1, b_1, c_1, a_2, b_2, c_2\) are some numbers. Then equalities \(l_1=0\) and \(l_2=0\) are equations for straight lines in two-dimensional space. Let \(l_1=0\) and \(l_2=0\) be the equations of two distinct straight lines. Then equation \(l_1l_2=0\) describes a conic section in this plane. Let us choose another pair of straight lines described by equations \(l_3=0\) and \(l_4=0\) \((l_3=a_3x+b_3y+c_3, l_4=a_4x+b_4y+c_4)\). Suppose the second pair of lines intersect the first pair of lines, and result in the equation

$$(1-\lambda)l_1l_2 + \lambda l_3l_4 = 0,$$  

(1.5.2)

where \(\lambda\) — some parameter. The equation (1.5.2) describes a family of conic sections passing through the four points of intersection of two pairs of lines; see Fig. 1.5.1. As line \(l_3\) approaches line \(l_4\), point \(A\) approaches point \(B\), point \(C\) approaches point \(D\), and chords \(AB\) and \(CD\) tend to the tangent lines of the conic sections of the set. When lines \(l_3\) and \(l_4\) coincide,

$$(1-\lambda)l_1l_2 + \lambda l_3^2 = 0,$$  

(1.5.3)

which represents a family of conic sections tangent to the lines \(l_1\) and \(l_2\) at their points of intersection with the line \(l_3\) (see Fig. 1.5.2). If we specify yet another point \(R\), distinct from points \(A\) and \(C\), we thereby define a conic section and the parameter \(\lambda\) in (1.5.3). The conic section in this case is defined by four points: \(A, C, R,\) and \(E\) as the point of intersection of straight lines \(l_1\) and \(l_2\).

Let us try to describe the part of a conic section which lies inside triangle \(AEC\) by a quadratic Bezier curve constructed on the control polyline with vertices \(A, E,\) and \(C\). Let the radius vectors of the points \(A, E, C\) be equal to \(p_0, p_1, p_2\), respectively. We introduce an oblique coordinate system in the plane with its origin at \(p_1\), and its coordinate basis being vectors \(p_0-p_1\) and \(p_2-p_1\). The coordinates of this system are denoted by \(u\) and \(v\). In the oblique system \(uv\), vector \(p_0\) has coordinates \(u=1\) and \(v=0\);
vector \( p_1 \) has coordinates \( u=0 \) and \( v=0 \); and vector \( p_2 \) has coordinates \( u=0 \) and \( v=1 \). The position of an arbitrary point with coordinates \( u \) and \( v \) is then described by the radius vector

$$
r(u,v) = p_1 + u(p_0 - p_1) + v(p_2 - p_1).
$$  

(1.5.4)

In an oblique coordinate system, straight lines \( l_1, l_2, l_3 \) are described by equations \( v=0 \), \( u=0 \), and \( u+v-1=0 \), respectively. Substituting them into (1.5.3), we obtain the equation

$$
(1-\lambda)uv + \lambda(u+v-1)^2 = 0,
$$

(1.5.5)

which describes a family of conic sections in the oblique coordinate system. Denote the left-hand side of equation (1.5.5) as \( S(u,v) \).

Suppose we choose some conic section from the family of (1.5.3), for which the parameter \( \lambda \) in (1.5.3) is known. Let us choose some point \( r \) of the conic section inside the triangle with vertices at points \( p_0, p_1, p_2 \); see Fig. 1.5.3.

![Fig. 1.5.3.](image)

Let the coordinates of the point be \( 0<u_0<1 \) and \( 0<v_0<1 \). In general, we can assume that the conic section is described by the function (1.5.4), in which the parameters \( u \) and \( v \) are related by (1.5.5). Let us express the radius vector of the conic section as a function of one parameter, which in turn is a function of \( u \) and \( v \). In order to do this, we need the tangent to the conic section at \( r(u_0,v_0) \) and also the points of intersection of this tangent with the axes of the oblique coordinate system to be known.

A tangent to the conic section (1.5.5), written as \( S(u,v) = 0 \), at the point with coordinates \( u=u_0 \) and \( v=v_0 \), is described by the equation

$$
\left. \frac{\partial S}{\partial u} \right|_{u_0,v_0} (u-u_0) + \left. \frac{\partial S}{\partial v} \right|_{u_0,v_0} (v-v_0) = 0.
$$

If we take into account the fact that \( u_0, v_0 \) satisfy (1.5.5), derivatives \( \partial S/\partial u \) and \( \partial S/\partial v \) at \( r(u_0,v_0) \) are equal to
$$
\frac{\partial S}{\partial u}\bigg|_{u_0,v_0} = (1 - \lambda)v_0 + 2\lambda(u_0 + v_0 - 1) = \lambda \frac{(u_0 + v_0 - 1)(u_0 - v_0 + 1)}{u_0},
$$

$$
\frac{\partial S}{\partial v}\bigg|_{u_0,v_0} = (1 - \lambda)u_0 + 2\lambda(u_0 + v_0 - 1) = \lambda \frac{(u_0 + v_0 - 1)(v_0 - u_0 + 1)}{v_0}.
$$

Thus, the equation of the tangent to the conic section at \( r(u_0,v_0) \) has the form

$$
(u_0 - v_0 + 1)v_0(u - u_0) + (v_0 - u_0 + 1)u_0(v - v_0) = 0.
$$

It intersects the coordinate axes \( u \) and \( v \) at the points

$$
u_1 = u_0 + u_0 \frac{v_0 - u_0 + 1}{u_0 - v_0 + 1} = \frac{2u_0}{u_0 - v_0 + 1}, \quad v_1 = 0,
$$

$$
v_2 = v_0 + v_0 \frac{u_0 - v_0 + 1}{v_0 - u_0 + 1} = \frac{2v_0}{v_0 - u_0 + 1}, \quad u_2 = 0,
$$

as shown in Fig. 1.5.4.

The tangent to the conic section divides vectors \( p_0 - p_1 \) and \( p_1 - p_2 \) into segments. We denote the ratios of the segment lengths as

$$
z_1 = \frac{u_1}{1 - u_1} = \frac{2u_0}{1 - u_0 - v_0}, \quad z_2 = \frac{v_2}{1 - v_2} = \frac{2v_0}{1 - u_0 - v_0}. \tag{1.5.6}
$$

Point \( r(u_0,v_0) \) of the conic section can be characterized by coordinates \( u_0, v_0 \), or by coordinates \( u_1, v_2 \), or by the ratios \( z_1, z_2 \). Let us consider the last characterization. We express \( u_0 \) and \( v_0 \) using \( z_1 \) and \( z_2 \) and (1.5.6)

$$
u_0 = \frac{z_1}{2 + z_1 + z_2}, \quad v_0 = \frac{z_2}{2 + z_1 + z_2}. \tag{1.5.7}
$$
Substituting (1.5.7) into (1.5.4), we obtain the radius vector of the conic section as a function of parameters \( z_1 \) and \( z_2 \).

$$
r(z_1, z_2) = \frac{z_1 p_0 + 2p_1 + z_2 p_2}{z_1 + 2 + z_2}. \tag{1.5.8}
$$

Parameters \( z_1 \) and \( z_2 \) are related by

$$
z_1 z_2 = \frac{4u_0 v_0}{(1 - u_0 - v_0)^2} = \frac{-4\lambda}{1 - \lambda},
$$

i.e., the product \( z_1 z_2 = \text{const} \) for a given conic section. Practically, the radius vector of the conic section depends on a single parameter.

Let us introduce the parameter \( t \) for the conic section. Parameters \( z_1 \) and \( z_2 \) depend on \( t \). From (1.5.5) it follows that

$$
\frac{u_0 v_0}{(1 - u_0 - v_0)^2} = \frac{\lambda}{\lambda - 1}.
$$

Substituting this into (1.5.6), we obtain

$$
z_1 = \frac{1}{w} \sqrt{\frac{u_0}{v_0}}, \quad z_2 = \frac{1}{w} \sqrt{\frac{v_0}{u_0}},
$$

where \( w = \sqrt{\frac{\lambda - 1}{4\lambda}} \) – constant coefficients. For conic section parameter \( t \), we use

$$
t = \frac{\sqrt{v_0}}{\sqrt{u_0} + \sqrt{v_0}}. \text{Then}
$$

$$
z_1 = \frac{1}{w} \left( \frac{1 - t}{t} \right), \quad z_2 = \frac{1}{w} \left( \frac{t}{1 - t} \right). \tag{1.5.9}
$$

We substitute these last equalities in (1.5.8) to express the radius vector of the conic section (1.5.4) as a function of a single parameter \( t \)

$$
r(t) = \frac{(1 - t)^2 p_0 + 2t(1 - t)wp_1 + t^2 p_2}{(1 - t)^2 + 2t(1 - t)w + t^2}. \tag{1.5.10}
$$

The coefficient

$$
w = \frac{1}{k} = \sqrt{\frac{\lambda - 1}{4\lambda}} = \frac{1 - u_0 - v_0}{\sqrt{4u_0 v_0}} = \frac{1}{\sqrt{z_1 z_2}}, \tag{1.5.11}
$$
is called the weight of the point \( p_1 \).

Let us compare the expressions for the radius vector of the second-order Bezier curve (1.5.1) and for the radius vector of the conic section (1.5.10). They are similar when \( w = 1 \), which is valid for one of the curves from the conic section family with \( \lambda = -1/3 \). The conic section (1.5.5) for \( \lambda = -1/3 \) is described by the equation

$$
u^2 - 2uv + v^2 - 2u - 2v + 1 = 0
$$

and represents a parabola. Indeed, if we introduce new variables \( x = u - v, \ y = 2u + 2v - 1 \), they will be related by the parabolic equation

$$
y = x^2.
$$

Let us consider the relation (1.5.10) as a generalization of the quadratic curve—which, in special cases, allows us to obtain both the second-order Bezier curve and the conic section.

We can now answer the question posed above: While it is impossible to describe the conic section in the general case by the second-order Bezier curve, it can be done using a similar curve (1.5.10). The second-order Bezier curve can also be described as a special case of the curve (1.5.10).

Let us use (1.5.10) to construct an arc of a circle with radius \( \rho \) and opening angle \( \alpha \), as shown in Fig. 1.5.5. By \( p_0 \) and \( p_2 \) we denote the radius vectors of the arc endpoints, and by \( p_1 \) we denote the point of intersection of the lines tangent to the arc at its endpoints.

![Fig. 1.5.5.](image)

Using the symmetry of the arc about line \( OC \), we find the weight \( w \) from (1.5.11). From similarity of triangles it follows that

$$
\frac{1}{w} = z_1 = z_2 = \frac{BC}{AB},
$$

The lengths of segments \( BC \) and \( AB \) are calculated from the radius \( \rho \) and the opening angle \( \alpha \)

$$
AB = \rho(1 - \cos(\alpha/2)), \quad BC = CO - BO = \frac{\rho}{\cos(\alpha/2)} - \rho = \rho \frac{1 - \cos(\alpha/2)}{\cos(\alpha/2)}.
$$
Therefore, \( w = \frac{AB}{BC} = \cos\left(\frac{\alpha}{2}\right) \).

Thus, the arc of a circle with radius \( p \) and opening angle \( \alpha \) can be constructed as a quadratic curve (1.5.10) given by points \( p_0, p_2, \) and \( p_1 \), with midpoint weight \( w = \cos(\alpha/2) \). The radius vector of the arc is described by the function

$$
r(t) = \frac{(1-t)^2p_0 + 2t(1-t)\cos(\alpha/2)p_1 + t^2p_2}{(1-t)^2 + 2t(1-t)\cos(\alpha/2) + t^2}, \quad t \in [0,1], \tag{1.5.12}
$$

where the points are related by

$$
|p_0 - p_1| = |p_2 - p_1| = p \tan(\alpha/2);
$$
$$
(p_0 - p_1) \cdot (p_2 - p_1) = |p_0 - p_1||p_2 - p_1|\cos\alpha.
$$

The parametric arc length is equal to unity. Formula (1.5.12) is valid in the range of angles \( 0 < \alpha < 2\pi \). Fig. 1.5.6 and 1.5.7 show circular arcs with angles \( 2/3\pi \) and \( 4/3\pi \) respectively. The two arcs have the same control points, but in the first case the weight of the midpoint is equal to 0.5, while in the second case, the weight of the midpoint is equal to -0.5.

Construct a quarter-ellipse on three vertices \( p_0, p_1 \) and \( p_2 \) with the help of (1.5.10); see Fig. 1.5.8. Vectors \( p_0 - p_1 \) and \( p_2 - p_1 \) are orthogonal. The lengths of these vectors are \( a = |p_0 - p_1| \) and \( b = |p_2 - p_1| \); the vectors define the semi-axes of the ellipse. In oblique coordinates \( u \) and \( v \), shown in Fig. 1.5.4, the equation of an ellipse is given by the equation of a circle: \((u - 1)^2 + (v - 1)^2 = 1\), corresponding to \( \lambda = -1 \) in (1.5.5). In accordance with (1.5.11), the weight of the point \( p_1 \) is

$$
w = \frac{\sqrt{2}}{2},
$$

the same as for a quarter-circle arc.
Consider the general case of constructing a conic section. We assume that the three vertices of the control polyline of the curve, \( p_0, p_1, p_2 \), and the fourth point \( r \), situated on the conic section, are known. Point \( r \) must lie in the same plane as the points \( p_0, p_1, p_2 \); see Fig. 1.5.9.

Construct the conic section in the form (1.5.10), assuming the weight of the vertex \( p_1 \) to be a function of the position of the fourth point \( r \) relative to the first three points:

$$
w(r) = \frac{1 - u_0 - v_0}{\sqrt{4u_0v_0}}.
$$

Oblique coordinates \( u_0 \) and \( v_0 \) of point \( r \)—used to calculate the weight—are equal to the ratios of the vector lengths \( |r-r_v|/|p_0-p_1| \) and \( |r-r_u|/|p_2-p_1| \) respectively. Denote the triangle area \( p_1p_0r \) as \( S_1 \), the triangle area \( p_1p_2r \) as \( S_2 \), and the triangle area \( p_0p_1p_2 \) as \( S \); then

$$
u_0 = \frac{|r-r_v|}{|p_0-p_1|} = \frac{S_2}{S}, \quad v_0 = \frac{|r-r_u|}{|p_2-p_1|} = \frac{S_1}{S}.
$$

This is derived from relations \( S=0.5|p_0-p_1||p_2-p_1|\sin\alpha \), \( S_1=0.5|p_0-p_1||r-r_u|\sin\alpha \), and \( S_2=0.5|p_2-p_1||r-r_v|\sin\alpha \), where \( \alpha \) — angle \( p_0p_1p_2 \). In our notation midpoint weight is
expressed in terms of the triangle areas by

$$ w = \frac{S - S_1 - S_2}{\sqrt{4S_1S_2}}. $$

The weight \( w \) of point \( p_1 \) can be found if \( S_1S_2 \neq 0 \)—that is, if the point \( r \) does not belong to lines \( p_0p_1 \) and \( p_2p_1 \). In general, weight may be either positive or negative. As can be seen from Fig. 1.5.6 and Fig. 1.5.7, if the point \( r \) is located inside the triangle \( p_0p_1p_2 \), the weight of point \( p_1 \) is positive. But if point \( r \) is located outside the triangle \( p_0p_1p_2 \), the weight of the point \( p_1 \) is negative.

The sign of the second invariant \( I = \frac{3\lambda^2 - 2\lambda - 1}{4} \) of the conic section (1.5.5) describes the type of a curve: if \( I > 0 \), then the conic section is elliptical; if \( I < 0 \), then it is hyperbolic; and if \( I = 0 \), it is parabolic. From (1.5.11) it follows that at \( |w| < 1 \), the curve (1.5.10) describes a segment of an ellipse; at \( |w| > 1 \) it (1.5.10) describes a segment of a hyperbola; and at \( |w| = 1 \), curve (1.5.10) describes a segment of a parabola.

### 1.6. Rational Bezier Curves

Formula (1.5.10) has an asymmetrical form, because the coefficient \( w \) is attributed only to the point \( p_1 \). By multiplying the numerator and denominator of the right-hand side of (1.5.10) by some number \( w_0 \), we obtain

$$ r(t) = \frac{(1-t)^2 w_0 p_0 + 2t(1-t) w_1 p_1 + t^2 w_2 p_2}{(1-t)^2 w_0 + 2t(1-t) w_1 + t^2 w_2}, $$

where \( w_1 = w_0 w \). Replace \( w_0 \) by some number \( w_2 \) in the last terms of numerator and denominator of the right-hand side of the equality. After these manipulations, control points \( p_0, p_1, p_2 \) will have coefficients \( w_0, w_1, w_2 \) respectively, and the formula (1.5.10) will have a symmetric form. As a result, we obtain the curve

$$ r(t) = \frac{(1-t)^2 w_0 p_0 + 2t(1-t) w_1 p_1 + t^2 w_2 p_2}{(1-t)^2 w_0 + 2t(1-t) w_1 + t^2 w_2} = \sum_{i=0}^{2} B_i^2 w_i p_i, \quad (1.6.1) $$

Coefficients \( w_0, w_1, w_2 \) are called the weights of the control points.

We use this result to generalize Bezier curves of arbitrary degree. By analogy with (1.6.1) we can write out the formula for calculating the radius vector of the Bezier curve constructed on an arbitrary number of vertices \( n \) in the form
$$ r(t) = \frac{\sum_{i=0}^{n} B''_i(t) w_i p_i}{\sum_{i=0}^{n} B''_i(t) w_i}, \quad t \in [0,1], \quad (1.6.2) $$

where \( B''_i(t) \) – Bernstein functions (1.4.2). In general, each control point \( p_i \) of the curve (1.6.2) has its own weight \( w_i \). Curves having weights attributed to their control points are called rational. Curve (1.6.2) is called a rational Bezier curve of degree \( n \).

In general, we can always transfer from a rational Bezier curve of degree \( n \) to a rational Bezier curve of degree \( n+1 \). To do this we need to multiply the numerator and the denominator of the right-hand side of equation (1.6.2) by a number \( t+(1-t) \), which is equal to unity, and rearrange the terms.

Let us illustrate this by an example of a rational quadratic Bezier curve. Multiplying the numerator and the denominator of the right-hand side of (1.6.1) by the number \( t+(1-t) \) that is equal to unity, rearranging terms by order of multiplication of \( t \) and \( (1-t) \), we get the following expression as a result:

$$ r(t) = \frac{(1-t)^3 w_0 p_0 + t(1-t)^2 (2w_1 p_1 + w_0 p_0) + t^2 (1-t)(2w_1 p_1 + w_2 p_2) + t^3 w_2 p_2}{(1-t)^3 w_0 + t(1-t)^2 (2w_1 + w_0) + t^2 (1-t)(2w_1 + w_2) + t^3 w_2}. $$

We can represent the right-hand side of this equality by a cubic Bezier curve. To do this, we introduce the notation for weights and vertices on the right-hand side of the last expression

$$ w_0^* = w_0, \quad w_1^* = \frac{2w_1 + w_0}{3}, \quad w_2^* = \frac{2w_1 + w_2}{3}, \quad w_0^* = w_2, $$
$$ p_0^* = p_0, \quad p_1^* = \frac{2w_1 p_1 + w_0 p_0}{3w_1^*}, \quad p_2^* = \frac{2w_1 p_1 + w_2 p_2}{3w_2^*}, \quad p_3^* = p_2. $$

With this the quadratic curve (1.6.1) takes the form of a cubic curve (omit the asterisks in the notation of the control points and the weights):

$$ r(t) = \frac{(1-t)^3 w_0 p_0 + 3t(1-t)^2 w_1 p_1 + 3t^2 (1-t)w_2 p_2 + t^3 w_3 p_3}{(1-t)^3 w_0 + 3t(1-t)^2 w_1 + 3t^2 (1-t)w_2 + t^3 w_3} = \frac{\sum_{i=0}^{3} B^3_i w_i p_i}{\sum_{i=0}^{3} B^3_i w_i}. $$

The resulting cubic curve is identical to the original quadratic curve, but its control polyline and control-point weights are different. Multiplying the numerator and the denominator of the right-hand side of the last equality by nonzero \( t+(1-t) \), we turn it into a rational Bezier curve of the fourth degree, which describes the same conic section. This process can be continued further.

If we assume that in the denominator of the right-hand side of (1.6.2), \( w(t) \) is the weight of the radius vector of the curve \( r(t) \), then it can be regarded as an additional
coordinate. The formula for its calculation using vertex weights is identical to the formula for calculation of the coordinates of the radius vector through coordinates of the vertices. It is convenient to use homogeneous coordinates when dealing with points that have weights

$$
P = \begin{bmatrix} wp_1 \\ wp_2 \\ wp_3 \\ w \end{bmatrix} = \begin{bmatrix} wp \\ w \end{bmatrix},
$$

where \( p_1, p_2, p_3 \) are the coordinates of the point \( p \), and \( w \) is the weight of the point. In terms of homogeneous coordinates, the radius vector of a rational Bezier curve is described by an equation that is similar to the equation for the Bezier curve (1.4.1) in its form

$$
R(t) = \sum_{i=0}^{n} B^n_i(t)p_i, \quad t \in [0,1].
$$

The weight of the point is subject to the same transformation as its coordinates, so one can work with homogeneous coordinates of the radius vector without isolation of the Cartesian coordinates. We obtain the Cartesian coordinates of a rational curve by dividing the homogeneous coordinates by the additional coordinate.

The radius vector of a rational curve is calculated as the quotient of two functions of the curve parameter; thus, when calculating the derivative of a rational curve, the right-hand side should be viewed as a composite function. If we denote the radius vector of a rational curve as \( r = \frac{wr}{w} \), then the derivative of the radius vector of the rational curve is determined by the formula

$$
\frac{dr}{dt} = \frac{1}{w} \frac{d(wr)}{dt} - \frac{wr}{w^2} \frac{dw}{dt}.
$$

If the weights of all the control points are equal, then they can be taken outside the summation and eliminated. Then, with the help of Bernstein polynomials (1.4.3), the rational Bezier curve (1.6.2.) becomes equal to an ordinary Bezier curve (1.4.1).

The presence of weights of the control points provides additional opportunities for editing the curve. Replace the weight \( w_j \) with \( w_j + \Delta w \). Then the curve (1.6.2) changes to the curve

$$
r^*(t) = \frac{\sum_{i=0}^{n} B^n_i(t)w_ip_i + B^n_j(t)\Delta wp_j}{\sum_{i=0}^{n} B^n_i(t)w_i + B^n_j(t)\Delta w} = \frac{r(t) + \delta(t)p_j}{1 + \delta(t)},
$$

where \( \delta(t) = \frac{B^n_j(t)\Delta w}{\sum_{i=0}^{n} B^n_i(t)w_i} \). Hence, for any \( \Delta w > 0 \), the point of the original curve is
translated to the point \( p_j \) and its new position \( r(t)^* \) divides the segment starting at \( r(t) \) and ending at the point \( p_j \) in the ratio \( 1:\delta(t) \). Fig. 1.6.1 shows rational Bezier curves of the fifth degree constructed on the same control points with weights equal to unity for all points, except the point \( p_3 \). We see that the greater the relative weight of the point, the closer the rational Bezier curve to this point. If the weight of the point is negative, then the point seems to push away the curve.

![Diagram](image)

Fig. 1.6.1.

Despite great capabilities, Bezier curves have some limitations—namely, the order of curves is tightly connected with the number of points; the parameter domain of the curves is predetermined; and curves cannot be periodic and closed.

### 1.7. Divided Differences

Divided differences are used to construct splines. Scalar functions are constructed on the basis of divided differences. Scalar functions are generalizations of Bernstein functions and are widely used in geometric modeling.

Suppose we know the values \( f(t_i) \) of some function \( f(t) \) for the parameter values \( t_i \). The first-order divided differences are the following:

$$
f[t_0, t_1] = \frac{f(t_1) - f(t_0)}{t_1 - t_0}. \tag{1.7.1}
$$

The second-order divided differences of are calculated using the first-order divided differences:

$$
f[t_0, t_1, t_2] = \frac{f[t_1, t_2] - f[t_0, t_1]}{t_2 - t_0}.
$$
Divided differences of \( m \)-th order are calculated using the divided differences of \((m-1)\)-th order

$$
f[t_0, t_1, \ldots, t_m] = \frac{f[t_1, t_2, \ldots, t_m] - f[t_0, t_1, \ldots, t_{m-1}]}{t_m - t_0}.
$$  

(1.7.2)

Parameters \( t_i, i=0,1,\ldots,m \) are called knots. Divided differences are denoted by the symbol of the function upon which they were constructed, with the list of knots inside square brackets. The notation \([t_1, t_2, \ldots, t_m]f\) is also used in the literature on divided differences. The order of the divided difference is one less than the number of knots in the square brackets. Zero-order divided differences are considered to be function values at the knots \( f(t_i) = f(t_i) \).

The divided difference of \( m \)-th order is expressed by the values of the function \( f(t) \) at the knots by the relation

$$
f[t_0, t_1, \ldots, t_m] = \sum_{j=0}^{m} \frac{f(t_j)}{(t_j - t_0)(t_j - t_1) \cdots (t_j - t_{j-1})(t_j - t_{j+1}) \cdots (t_j - t_m)} = \sum_{j=0}^{m} W_{0,m}'(t_j),
$$

(1.7.3)

where \( W_{0,m}'(t_j) = (t_j - t_0)(t_j - t_1) \cdots (t_j - t_{j-1})(t_j - t_{j+1}) \cdots (t_j - t_m) \) is the derivative of the function \( W_{0,m}(t) = (t - t_0)(t - t_1) \cdots (t - t_{m-1})(t - t_m) \), calculated at \( t=t_j \). Indices in the function notation \( W_{0,m}(t) \) denote the numbers of the initial and the final knot. Equation (1.7.3) is proved by induction. For the first-order divided difference, the formula (1.7.3) is similar to (1.7.1); i.e., equality (1.7.3) holds for \( m=1 \). Let us assume that (1.7.3) holds for the divided differences of \((m-1)\)-th order and make sure that (1.7.3) holds for the divided differences of \( m \)-th order under this assumption. To do this, we find the difference of equalities

$$
f[t_1, t_2, \ldots, t_m] = \sum_{j=1}^{m} \frac{(t_j - t_0)f(t_j)}{(t_j - t_0)W_{1,m}'(t_j)} \quad \text{and} \quad f[t_0, t_1, \ldots, t_{m-1}] = \sum_{j=0}^{m-1} \frac{(t_j - t_m)f(t_j)}{(t_j - t_m)W_{0,m-1}'(t_j)},
$$

where corresponding terms in the right-hand sides are reduced to a common denominator. As a result, we get

$$
f[t_1, t_2, \ldots, t_m] - f[t_0, t_1, \ldots, t_{m-1}] =
$$

$$
= \frac{(t_m - t_0)f(t_0)}{W_{0,m}'(t_0)} + \sum_{j=1}^{m-1} \frac{(t_j - t_0)f(t_j) - (t_j - t_m)f(t_j)}{W_{0,m}'(t_j)} + \frac{(t_m - t_0)f(t_m)}{W_{0,m}'(t_m)} = (t_m - t_0) \sum_{j=0}^{m} \frac{f(t_j)}{W_{0,m}'(t_j)},
$$

which, after dividing by \((t_m - t_0)\) and considering (1.7.2), implies (1.7.3).

From equation (1.7.3) it can be seen that the divided difference does not depend on the order of knots \( t_0, t_1, \ldots, t_m \) in the argument list.

Divided differences can be constructed on a sequence with coincident knots. Knots with coinciding values are called multiple knots. Thus if \( t_1 = t_2 = \ldots = t_k \), then we
say that the knot has multiplicity $k$. If the first-order divided difference is constructed on multiple knots, it is equal to derivative of the function at this point

$$f[t_i, t_j] = \lim_{t \to t_i} \frac{f(t) - f(t_i)}{t - t_i} = \left. \frac{df}{dt} \right|_{t_i} = f'(t_i).$$

The $m$-th order divided difference constructed on a knot with multiplicity $m+1$ is equal to the $m$-th derivative of the function calculated at the given knot and divided by $m!$

$$f[t_1, t_2, \ldots, t_m] = \frac{1}{m!} \left. \frac{d^m f}{dt^m} \right|_{t_i} = \frac{f^{(m)}(t_i)}{m!}. \quad (1.7.4)$$

If $p(t)$ is an $m$-th degree polynomial of parameter $t$ and we know the values of the polynomial $p(t_i)$ at the knots $t_i$, then the first-order divided difference

$$p[t, t_i] = \frac{p(t_i) - p(t)}{t_i - t}$$

is a polynomial of degree $(m-1)$. Indeed, the function $p(t_i) - p(t)$ has a root $t_i$ and therefore, according to the Bezout theorem, is exactly divisible by $t_i - t$. The second-order divided difference

$$p[t, t_1, t_2] = \frac{p[t_1, t_2] - p[t, t_1]}{t_2 - t}$$

is a polynomial of degree $(m-2)$. Indeed, the function $p[t_1, t_2] - p[t, t_1]$ has a root $t_2$ and therefore, according to Bezout theorem, is exactly divisible by $t_2 - t$. Similar arguments lead to the fact that the divided difference of order $m$ is a polynomial of degree zero

$$p[t, t_1, t_2, \ldots, t_m] = \text{const},$$

and the $(m+1)$-th order divided difference of an $m$-th degree polynomial is equal to zero:

$$p[t, t_1, t_2, \ldots, t_{m+1}] = 0.$$

Let $p(t)$ be an interpolation polynomial of a function $f(t)$ coinciding with it in $m+1$ knots $t_i$, $p(t_i) = f(t_i)$, $i=0,1,\ldots,m$; then divided differences constructed on the knots $t_i$ for the functions $p(t)$ and $f(t)$ are equal. From the definition of the divided difference for the function $p(t)$ constructed on a sequence of knots $t_0, t_1, \ldots, t_m$,
$$ p[t_0, t_1, \ldots, t_m] = \frac{p[t_0, t_1, \ldots, t_{m-1}] - p[t_0, t_1, \ldots, t_{m-2}]}{t_m - t} $$

and from equalities of the divided differences \( p[t_0, t_1, \ldots, t_m] = f[t_0, t_1, \ldots, t_m] \) follow equalities:

$$
\begin{align*}
p[t_0, t_1, \ldots, t_{m-1}] &= f[t_0, t_1, \ldots, t_m] + (t - t_m)p[t_0, t_1, \ldots, t_m], \\
p[t_0, t_1, \ldots, t_{m-2}] &= f[t_0, t_1, \ldots, t_{m-1}] + (t - t_{m-1})p[t_0, t_1, \ldots, t_{m-1}], \\
&\vdots \\
p[t_0, t_1] &= f[t_0, t_1] + (t - t_1)p[t_0, t_1], \\
p[t] &= f[t_0] + (t - t_0)p[t_0].
\end{align*}
$$

Since \( p(t) = p[t] \), we can substitute each of these equations in the preceding one, starting from the last equation. This yields the Newton interpolation formula for the function \( f(t) \)

$$
p(t) = f[t_0] + f[t_0, t_1](t - t_0) + \ldots + f[t_0, t_1, \ldots, t_m](t - t_0)(t - t_1)\ldots(t - t_{m-1}). \tag{1.7.5}
$$

Thus, the coefficients of the Newton polynomial are corresponding divided differences of the interpolated function. If the interpolation (1.7.5) is performed over \( m+1 \) multiple knots \( t_0 = t_1 = \ldots = t_m \), then in accordance with (1.7.4), the divided differences are proportional to the derivative of the corresponding order of the interpolated function—and as a result we obtain a truncated Taylor series.

It is known that for a given set of values of the function \( f(t_i) \) at the knots \( t_i \), \( i=0,1,\ldots,m \), one can construct a unique polynomial of degree \( m \), coinciding at knots \( t_i \) with a given function. From the Newton interpolation formula (1.7.5), we see that the divided difference \( f[t_0, t_1, \ldots, t_m] \) of \( m \)-th order on a given sequence of \( m+1 \) knots is equal to the coefficient at the highest power of the argument \( t^m \) of the polynomial of degree \( m \), whose values at given knots are in agreement with the function \( f(t) \). This property can be taken as a definition of the divided difference.

**Property 1.** If \( f(t) = a_0 + a_1t + a_2t^2 + \ldots + a_mt^m \) (polynomial of degree \( m \)), then

$$
f[t_0, t_1, \ldots, t_m] = a_m, \quad f[t_0, t_1, \ldots, t_{m+1}] = 0, \tag{1.7.6}
$$

for any additional knot \( t_{m+1} \).

**Property 2.** By the uniqueness of such polynomial and by (1.7.3) any divided difference is a symmetric function of its arguments; i.e., the value \( f[t_0, t_1, \ldots, t_m] \) does not depend on the order of the knots \( t_0, t_1, \ldots, t_m \) in the argument list. The divided difference is expressed by the values of the function \( f(t) \) at the knots using the formula (1.7.3). If some knots are multiple, then the divided difference is expressed in terms of the values of the \( f(t) \) at simple knots and its derivatives at the multiple knots.

**Property 3.** If \( f(t) = k_g g(t) + k_h h(t) \), then
$$ f[t_0, t_1, \ldots, t_m] = k_s g[t_0, t_1, \ldots, t_m] + k_h h[t_0, t_1, \ldots, t_m]. $$

This equality follows from the uniqueness of the interpolation polynomial.

**Property 4.** If \( f(t) = g(t)h(t) \), then

$$
f[t_0, t_1, \ldots, t_m] = \sum_{k=0}^{m} g[t_0, t_1, \ldots, t_k] \cdot h[t_k, t_{k+1}, \ldots, t_m].
$$ (1.7.7)

To prove this formula we approximate each of the functions \( g(t) \) and \( h(t) \) by the polynomial (1.7.5), and multiply one by another. The coefficient at the highest degree \( t^m \) of the resulting polynomial is equal to the right-hand side of (1.7.7), as required. Equation (1.7.7) is called the **Leibniz formula**.

**Property 5.** If the polynomial \( p_{m-1}(t) \) of degree \( m-1 \) on the sequence of \( t_0, t_1, \ldots, t_{m-1} \) is constructed for the function \( f(t) \), then

$$
f(t) = p_{m-1}(t) + f[t_0, t_1, \ldots, t_{m-1}, t](t-t_0)(t-t_1)\ldots(t-t_{m-1}).
$$

To derive this equality we consider \( t \) as an additional knot in the sequence of knots, and the equality is regarded as a necessary condition for a polynomial of degree \( m \) at an additional knot.

Consider a **truncated power function with shifted origin**

$$
\sigma_m(z) = (z-t)^m_+ = (\max(0, z-t))^m.
$$ (1.7.8)

Functions \( \sigma_m(z) \) are plotted in Fig. 1.7.1. The higher the degree of the function \( \sigma_m(z) \), the smoother it is at the point \( z=t \).

![Fig. 1.7.1.](image)

The parameter \( t \) determines the shift of the origin of the truncated power function. A truncated power function with a shifted origin is equal to zero at \( z \leq t \) and equal to \( (z-t)^m \) otherwise. The function \( \sigma_m(z) \) is continuous and piecewise monotonic at \( m>0 \); for \( m=0 \) it has a jump at \( z=t \), equal to unity. The function \( \sigma_m(z) \) has continuous derivatives up to order \( (m-1) \); the \( m \)-th order derivative has a discontinuity at \( z=t \). Function (1.7.8) is special because its derivatives are the same functions but with their degree reduced by one.

The divided differences \( \sigma_m[t_0, t_1, \ldots, t_{m+1}] \) of the truncated power function with shifted origin have properties that allow them to be used to construct rational curves.
The divided difference is calculated at a fixed parameter $t$, but it is a function of the parameter $t$. If all $t_i < t$, $i = 0, 1, \ldots, m+1$, then all $\sigma_m(t_i) = 0$, and the divided difference $\sigma_m[t_0, t_1, \ldots, t_{m+1}]$ is equal to zero. If all $t_i > t$, $i = 0, 1, \ldots, m+1$, then the divided difference $\sigma_m[t_0, t_1, \ldots, t_{m+1}]$ is equal to zero, since all knots are located on the segment, where the function is a polynomial of degree less than $(m+1)$. Only when the parameter $t$ of the origin shift lies within the segment formed by the sequence of knots $t_0, t_1, \ldots, t_{m+1}$ ($\min(t_0, t_1, \ldots, t_{m+1}) \leq t \leq \max(t_0, t_1, \ldots, t_{m+1})$), the divided difference $\sigma_m[t_0, t_1, \ldots, t_{m+1}]$ of the truncated power function of degree $m$ does not vanish.

### 1.8. B-Splines

B-splines are scalar functions with a set of useful properties. B-splines are constructed on divided differences and are used to construct curves. The fundamentals of B-spline theory were laid by J.C. Ferguson and I.J. Schoenberg. W.J. Gordon and R.F. Riesenfeld established a link between Bezier curves and B-splines, and showed that B-splines are generalizations of Bernstein functions. Bezier curves, rational curves (which in certain cases describe conic sections), and other curves can be based on B-splines.

A **B-spline** for a sequence of $m+2$ knots is the divided difference of $(m+1)$-th order of the truncated power function with shifted origin of $m$-th degree multiplied by the difference between the maximum and minimum knot values of the sequence.

A B-spline constructed on a sequence of knots $t_i, t_{i+1}, \ldots, t_{i+m+1}$ is defined by

$$N^m_i(t) = (t_{\text{min}} - t_{\text{max}}) \sigma_m[t_i, t_{i+1}, \ldots, t_{i+m+1}],$$

(1.8.1)

where $t_{\text{max}} = \max(t_i, t_{i+1}, \ldots, t_{i+m+1})$, $t_{\text{min}} = \min(t_i, t_{i+1}, \ldots, t_{i+m+1})$ are the maximum and minimum knot values of the sequence. Indices in B-spline notation are intended to characterize the sequence of knots constructed on which they are constructed, and may have different meanings in different publications. In some publications, the B-spline is ascribed an order equal to the degree of the truncated power function, while in others, B-spline has an order equal to the order of the divided difference. Furthermore, the B-spline is assigned to one of the knots of the sequence. We assume that the order of the B-spline is equal to the power of the function it is constructed on, and assign it to the first knot. Fig. 1.8.1 shows B-splines of zero, first and second order.

![Fig. 1.8.1](image-url)
Fig. 1.8.2 shows a B-spline of the third order $N_1^3(t) = (t_5 - t_1)\sigma_3[t_1, t_2, t_3, t_4, t_5]$ and a B-spline of the fifth order $N_5^5(t) = (t_9 - t_3)\sigma_5[t_3, t_4, t_5, t_6, t_7, t_8, t_9]$, constructed on equidistant knots.

If the sequence of knots a B-spline is constructed on contains multiple knots, then the derivatives of the B-spline lose their continuity. Fig. 1.8.3 shows B-splines of the third order with multiple knots $N_1^3(t) = (t_2 - t_1)\sigma_3[t_1, t_2, t_3, t_4, t_5]$, $N_3^3(t) = (t_5 - t_3)\sigma_3[t_3, t_4, t_5, t_6, t_7]$, $N_6^3(t) = (t_8 - t_6)\sigma_3[t_6, t_7, t_8]$. 

Index $m$ in (1.8.1) indicates the order of the B-spline and index $i$ points to the first knot in the sequence. The position of index $i$ before index $m$ indicates that the $i$-th knot is the first knot of the sequence. Later we will define B-spline $N_{m+i+m+1}(t)$, having an index of the last knot in the sequence, which will be indicated by positioning of the index $i+m+1$ after the index $m$. B-splines $N_i^m(t)$ and $N_{m+i+m+1}(t)$ constructed on the same sequence of knots are identical.

To calculate B-splines, divided differences of the truncated exponential function called unnormalized B-splines are introduced.

An unnormalized B-spline for a sequence of $m+2$ knots is the divided difference of the $(m+1)$-th order of the truncated power function with shifted origin of $m$-th degree.

An unnormalized B-spline constructed on a sequence of knots $t_i, t_{i+1}, \ldots, t_{i+m+1}$ is defined by

$$M_i^m(t) = \sigma_m[t_i, t_{i+1}, \ldots, t_{i+m+1}].$$  \hspace{1cm} (1.8.2)

In the notation for unnormalized B-splines in (1.8.2), index $i$ indicates the first knot of the sequence, and index $m$ indicates the order of the B-spline.
A B-spline and an unnormalized B-spline are linked by a coefficient, and except for a factor, have the same definition. Calculation of B-splines is performed with the help of unnormalized B-splines.

Suppose there is a sequence of \( m+2 \) knots \( t_0, t_1, \ldots, t_{m+1} \), where at least two have distinct values. Suppose that \( t_i \neq t_{i+m+1} \). Let us use the Leibniz formula (1.7.7) to calculate the B-spline. We represent the function \( \sigma_m(z) = (z-t)^m \) as a product \( \sigma_m(z) = g(z)\sigma_{m-1}(z) \), where \( \sigma_{m-1}(z) = (z-t)^{m-1} \) and \( g(z) = (z-t) \). Then the divided difference is

$$
\sigma_m[t_0, t_1, \ldots, t_{i+m+1}] = g[t_0]\sigma_{m-1}[t_0, t_1, \ldots, t_{i+m+1}] + g[t_1]\sigma_{m-1}[t_1, t_2, \ldots, t_{i+m+1}] + \cdots + g[t_{i+m+1}]\sigma_{m-1}[t_{i+m+1}, t_{i+m+2}, \ldots, t_{i+m+1}] = 0 + \cdots + 0 = (t_i - t)\sigma_{m-1}[t_0, t_1, \ldots, t_{i+m+1}] + \sigma_{m-1}[t_1, t_2, \ldots, t_{i+m+1}].
$$

(1.8.3)

In (1.8.3) we used the fact that the divided differences of higher orders for the function \( g(z) \) are equal to zero. We substitute \( \sigma_{m-1}[t_0, t_1, \ldots, t_{i+m+1}] \) in (1.8.3) by the definition of divided difference (1.7.2)

$$
\sigma_{m-1}[t_0, t_1, \ldots, t_{i+m+1}] = \frac{\sigma_{m-1}[t_1, t_2, \ldots, t_{i+m+1}] - \sigma_{m-1}[t_0, t_1, \ldots, t_{i+m}]}{t_{i+m+1} - t_i}
$$

and get

$$
\sigma_m[t_0, t_1, \ldots, t_{i+m+1}] =
\frac{t_i - t}{t_{i+m+1} - t_i} \left( \sigma_{m-1}[t_1, t_2, \ldots, t_{i+m+1}] - \sigma_{m-1}[t_0, t_1, \ldots, t_{i+m}] \right) + \frac{t_{i+m+1} - t_i}{t_{i+m+1} - t_i} \sigma_{m-1}[t_1, t_2, \ldots, t_{i+m+1}] =
\frac{t_{i+m+1} - t}{t_{i+m+1} - t_i} \sigma_{m-1}[t_1, t_2, \ldots, t_{i+m+1}] + \frac{t - t_i}{t_{i+m+1} - t_i} \sigma_{m-1}[t_0, t_1, \ldots, t_{i+m}].
$$

(1.8.4)

Let us rewrite (1.8.4) using the definition of an unnormalized B-spline in (1.8.2) to obtain the formula

$$
M_i^m(t) = \frac{t_{i+m+1} - t}{t_{i+m+1} - t_i} M_{i+1}^{m-1}(t) + \frac{t - t_i}{t_{i+m+1} - t_i} M_i^{m-1}(t).
$$

(1.8.5)

The recurrence relation (1.8.5) was obtained independently by Mansfield, M.G. Cox and C. De Boor, and is called the Cox-De Boor formula. This relation is central to the theory of B-splines. It encourages us to forget about divided differences and to define the B-spline of \( m \)-th order for a sequence of \( m+2 \) knots \( t_0, t_1, \ldots, t_{i+m+1} \) as a function computed by the recurrence relation (1.8.5) with initial values

$$
M_i^0(t) = \begin{cases} 
\frac{1}{|t_{i+1} - t_i|}, & \text{if } \min(t_i, t_{i+1}) \leq t < \max(t_i, t_{i+1}), \\
0, & \text{in other cases}.
\end{cases}
$$

(1.8.6)
Equation (1.8.6) expresses an unnormalized B-spline of order zero by the divided difference of the first order for the function $\sigma_0(z) = (z - t)^0_+$. 

Let's forget for a moment about indexing in formula (1.8.5) and consider the function, using its barycentric coordinates. Suppose we are given an arbitrary sequence of $m+2$ knots, in which at least two knots have distinct values. Recall that the divided difference does not depend on the order of the knots in the argument list. We choose two arbitrary not-coinciding knots, $t_a$ and $t_b$, from the sequence of $m+2$ knots. Let us introduce barycentric coordinates on the basis of these two knots:

$$a(t) = \frac{t_b - t}{t_b - t_a}, \quad b(t) = \frac{t_a - t}{t_a - t_b}.$$  

We introduce the following notations. A sequence of $m+2$ knots $t_i, t_{i+1}, ..., t_{i+m+1}$ is denoted as $T$. The sequence of $m+1$ knots obtained from $T$ by removing the knot $t_a$ is denoted as $T\setminus a$. The sequence of $m+1$ knots obtained from $T$ by removing the knot $t_b$ is denoted as $T\setminus b$. The $(m+1)$-th order divided difference of the truncated power function $(z-t)^m_+$ on the sequence of knots $T$ is denoted as $M^T(t)$. The $m$-th order divided difference of the truncated power function $(z-t)^{m-1}_+$ on the sequence of knots $T\setminus a$ is denoted as $M^{T\setminus a}(t)$. The $m$-th order divided difference of the truncated power function $(z-t)^{m-1}_+$ on the set of knots $T\setminus b$ is denoted as $M^{T\setminus b}(t)$. Then the Cox-De Boor formula (1.8.5) for unnormalized B-splines on the sequence of knots $T$ takes the form

$$M^T(t) = a(t)M^{T\setminus a}(t) + b(t)M^{T\setminus b}(t). \quad (1.8.7)$$

Since the divided difference is a symmetric function of its arguments, the last recurrence relation does not depend on the choice of the knots $t_a$ and $t_b$. Recurrence relation (1.8.7) starts with evaluation of unnormalized B-splines of order zero (1.8.6).

For a visual representation of (1.8.5) we assume that the knots of the sequence are arranged in ascending order of their value: $t_i \leq t_{i+1} \leq ... \leq t_{i+m+1}$. Then one of the two B-splines of $(m-1)$-th order will be adjacent to the start point of the calculated B-spline, and the other—to the endpoint of the calculated B-spline; see Fig. 1.8.4. Each of the two $(m-1)$-th order B-splines is multiplied by a factor proportional to parameter $t$, the distance from the end knot of the given sequence to which the $(m-1)$-th order B-spline adjoins. The sum of these two coefficients $a(t), b(t)$ is equal to one.

![Fig. 1.8.4.](image-url)
With the help of B-splines, we can construct curves based on points whose B-spline binding-knot index is equal to the index of the point. Therefore, a non-decreasing sequence of knots is used to construct curves, because the knots are related to the curve parameter. In addition, the family of B-splines constructed on a non-decreasing sequence of knots for a given parameter \( t \) has certain properties. Thus, in practice, B-splines are constructed on knots that belong to a part of the total sequence of knots arranged in sequential order.

**Property 1.** Let B-spline \( N_i^m(t) \) be constructed on a non-decreasing sequence of \( m+2 \) knots \( t_i, t_{i+1}, \ldots, t_{i+m+1} \). Then the B-spline \( N_i^m(t) \) is nonzero only in the region \( t_i \leq t < t_{i+m+1} \) and \( N_i^m(t) = 0 \) for \( t < t_i \) and \( t > t_{i+m+1} \). Indeed, once \( t < t_i \), the truncated function becomes \( \sigma_m(z) = (z-t)^m \) between points \( t_i \) and \( t_{i+m+1} \), and considering that \( (z-t)^m \) is a polynomial of degree less than \( m+1 \), any \((m+1)\)-th-order divided difference constructed on this polynomial is zero. Once \( t > t_{i+m+1} \), the divided difference is equal to zero due to the fact that \( \sigma_m(z) = 0 \) between the knots \( t_i \) and \( t_{i+m+1} \). Only when \( t_i \leq t < t_{i+m+1} \), the divided difference \( \sigma_m[t_i, t_{i+1}, \ldots, t_{i+m+1}] \) is nonzero. Thus, B-splines are local functions taking nonzero values on the interval containing the constructing knots of the B-spline.

**Property 2.** \( N_i^m(t) \geq 0 \) — that is, B-splines take non-negative values for any values of the parameter. This follows from the above properties and the recurrence relation (1.8.5) for the non-decreasing sequence of knots.

**Property 3.** Suppose we are given an infinite (or long enough) non-decreasing sequence of knots \( t_i \) and on every \((m+2)\) knots of the sequence an \( m \)-th order B-spline is constructed. We can show that for any \( t_i \leq t < t_{i+1} \), only \( m+1 \) B-splines are nonzero—namely, \( N_{i-m}^m(t), N_{i+1-m}^m(t), \ldots, N_i^m(t) \), and their sum is equal to 1. Indeed, all B-splines \( N_j^m(t) \), where \( j < i-m \), are equal to zero, as they were constructed on knots where \( \sigma_m(z) = 0 \); all B-splines \( N_j^m(t) \), where \( j \geq i+1 \), are equal to zero, as they were constructed on knots where \( \sigma_m(z) = (z-t)^m \) is a polynomial of degree less than \( m+1 \).

Thus, the sum of all B-splines with \( t_i \leq t < t_{i+1} \) depends on the final number of B-splines:

$$
\sum_{j=i-m}^{i} N_j^m(t) = \sum_{j=i-m}^{i} N_j^m(t).
$$

(1.8.8)

If we use the definition of divided difference (1.7.2), then the B-spline (1.8.1) can be written as

$$
N_j^m(t) = \sigma_m[t_{j+1}, t_{j+2}, \ldots, t_{j+m+1}] - \sigma_m[t_j, t_{j+1}, \ldots, t_{j+m}].
$$

(1.8.9)

Using (1.8.8) and (1.8.9), we find the sum of all B-splines with \( t_i \leq t < t_{i+1} \).
$$ \sum_{j=i-m}^{i} N_j^m(t) = \sum_{j=i-m}^{i} (\sigma_m[t_{j+1}, t_{j+2}, \ldots, t_{j+m+1}] - \sigma_m[t_{j}, t_{j+1}, \ldots, t_{j+m}]) = $$
$$ = \sum_{j=i-m}^{i} \sigma_m[t_{j+1}, t_{j+2}, \ldots, t_{j+m+1}] - \sum_{j=i-m}^{i} \sigma_m[t_{j}, t_{j+1}, \ldots, t_{j+m}] = $$
$$ = \sigma_m[t_{i+1}, t_{i+2}, \ldots, t_{i+m+1}] - \sigma_m[t_{i-m}, t_{i+1-m}, \ldots, t_i] = 1 - 0 = 1. \quad (1.8.10) $$

In (1.8.10) we used \( \sigma_m[t_{i+1}, t_{i+2}, \ldots, t_{i+m+1}] = 1 \) as the coefficient at the highest power of the argument in the polynomial \((z-t)^m\) describing the truncated power function on an open interval \(t_{i+1} < z < t_{i+m+1}\). In addition, the truncated power function is zero on the interval \(t_{i-m} < z < t_i\) and hence its divided difference \( \sigma_m[t_{i-m}, t_{i+1-m}, \ldots, t_i] = 0 \). Since the segment \(t_i \leq t < t_{i+1}\) was chosen arbitrarily, a similar equation holds for any other segment. Thus, for any \(t\), the sum of all B-splines is subject to the equality

$$ \sum_j N_j^m(t) = 1. \quad (1.8.11) $$

Relation (1.8.11) for the B-splines is analogous to relation (1.4.3) for the Bernstein basis. Thus, the family of all nonzero functions \(N_j^m(t)\) is a partition of unity for any fixed parameter \(t\).

**Property 4.** For a non-decreasing sequence of knots \(t_i, t_{i+1}, \ldots, t_{i+m+1}\), a B-spline is computed using the recurrence relation

$$ N_i^m(t) = \frac{t_{i+m+1} - t}{t_{i+m+1} - t_{i+1}} N_{i+1}^{m-1}(t) + \frac{t - t_i}{t_{i+m} - t_i} N_i^{m-1}(t), \quad (1.8.12) $$

starting with the order-zero B-spline

$$ N_j^0(t) = \begin{cases} 1, & \text{if } t_j \leq t < t_{j+1} \\ 0, & \text{in other cases} \end{cases}. \quad (1.8.13) $$

Equation (1.8.12) follows from the Cox-De Boor recurrence formula (1.8.5), one just need to substitute the relations between B-splines and corresponding unnormalized B-splines

$$ N_i^m(t) = (t_{i+m+1} - t_i) M_i^m(t). \quad (1.8.14) $$

**Property 5.** The derivative of an order-\(m\) B-spline is expressed by B-splines of order \((m-1)\). To prove this, we differentiate a B-spline constructed on a non-decreasing sequence of knots \(t_i, t_{i+1}, \ldots, t_{i+m+1}\) and represented as (1.8.9):
$$ \frac{dN_i^m(t)}{dt} = \frac{d\sigma_m[t_{i+1}, t_{i+2}, \ldots, t_{i+m+1}]}{dt} - \frac{d\sigma_m[t_i, t_{i+1}, \ldots, t_{i+m}]}{dt}. $$

If we substitute \( t \)-derivatives of a truncated power function in the last expression

$$ \frac{d\sigma_m}{dt} = -m(z-t)^{m-1}_+ = -m\sigma_{m-1}, $$

we get

$$ \frac{dN_i^m(t)}{dt} = -m\sigma_{m-1}[t_{i+1}, t_{i+2}, \ldots, t_{i+m+1}] + m\sigma_{m-1}[t_i, t_{i+1}, \ldots, t_{i+m}] = $$
$$ = -mM_{i+1}^{m-1}(t) + mM_i^{m-1}(t) = $$
$$ = -\frac{m}{t_{i+m+1} - t_{i+1}} N_{i+1}^{m-1}(t) + \frac{m}{t_{i+m} - t_i} N_i^{m-1}(t). $$ (1.8.15)

Similarly, we obtain that the derivative of a non-normalized B-spline of order \( m \) is expressed by unnormalized B-splines of \((m-1)\)-th order by the formula

$$ \frac{dM_i^m(t)}{dt} = m \frac{M_i^{m-1}(t) - M_{i+1}^{m-1}(t)}{t_{i+m+1} - t_i}. $$

**Property 6.** Let a B-spline be constructed on a non-decreasing sequence of knots \( t_i, t_{i+1}, \ldots, t_{i+m+1} \). From equation (1.8.12) and equation (1.8.15), it follows that the B-spline of order \( m \) is an \( m \)-times differentiable function. In the absence of multiple knots, the B-spline and its derivatives up to order \((m-1)\) order are continuous functions and are equal to zero at \( t=t_i \) and \( t=t_{i+m+1} \).

**Property 7.** The area under any unnormalized B-spline satisfies the following equality

$$ \int_{-\infty}^{\infty} M_i^m(t) dt = \int_{t_{\min}}^{t_{\max}} M_i^m(t) dt = \frac{1}{m+1}, $$ (1.8.16)

where \( t_{\max} \) and \( t_{\min} \) are the maximum and minimum knot values of the sequence used to evaluate the B-spline. We obtain the equation (1.8.16) by integrating the truncated power function (1.7.8) within the specified limits

$$ \int_{t_{\min}}^{t_{\max}} (z-t)^m_+ dt = \frac{1}{m+1} (z-t_{\min})^{m+1}_+ - \frac{1}{m+1} (z-t_{\max})^{m+1}_+ $$

and calculating the \((m+1)\)-order divided difference of the obtained function on the sequence of B-spline knots. The second term on the right-hand side is equal to zero in
the range \( t_{\text{min}} \leq z \leq t_{\text{max}} \) and the first term is an \((m+1)\)-th-degree polynomial. In accordance with (1.7.6), the order-(\(m+1\))-divided difference of this polynomial is equal to the coefficient at \( z^{m+1} \)—i.e., is equal to \(1/(m+1)\), which proves (1.8.16).

From (1.8.16) follows the equality

$$
\int_{-\infty}^{\infty} N_i^m(t) dt = (t_{\text{max}} - t_{\text{min}}) \int_{t_{\text{min}}}^{t_{\text{max}}} M_i^m(t) dt = \frac{t_{\text{max}} - t_{\text{min}}}{m + 1},
$$

which is used to calculate the area under B-spline.

### 1.9. B-Spline Curves

The foundations of B-spline curve theory were laid by S.A. Coons and C. De Boor. K.J. Versprille developed the theory of B-spline curves further and used it in engineering.

Construct a non-uniform rational curve based on B-splines \( N_j^m(t) \) on the control points \( p_j \) having weights \( w_j, j=0,1,...,n \) (\( n \geq m \)). Calculate the radius vector of the curve using the formula

$$
r(t) = \frac{\sum_{j=0}^{n} N_j^m(t) w_j p_j}{\sum_{j=0}^{n} N_j^m(t) w_j}.
$$  

(1.9.1)

Each of the \( m \)-th-order B-splines \( N_j^m(t) \) is constructed on a non-decreasing sequence of \( m+2 \) knots \( t_0, t_1, ..., t_{m+1} \). In the general case, the curve (1.9.1) is non-uniform and rational. The non-uniformity of the curve suggests that its knots are not evenly spaced, and its rationality indicates the presence of the weights of the control points, which results in the presence of the denominator in (1.9.1). Curve (1.9.1) is called a NURBS curve or B-spline curve. "NURBS" stands for "Non-Uniform Rational B-Spline."

When all the control points of curve (1.9.1) have equal weights, then by (1.8.11), the radius vector of the B-spline curve is calculated by the formula

$$
r(t) = \sum_{j=0}^{n} N_j^m(t) p_j.
$$  

(1.9.2)

Formula (1.9.1) has the same form in terms of homogeneous coordinates (1.6.3):

$$
R(t) = \sum_{j=0}^{n} N_j^m(t) P_j.
$$