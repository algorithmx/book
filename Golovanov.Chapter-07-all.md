GEOMETRIC MODEL APPLICATIONS

Geometric models are meant for studying and manufacturing the modeled objects. Using geometric models, we can see how the modeled object will look, check its performance, and investigate its behavior under real-world conditions by numerical experiments. Using a geometric model, we can plan production of modeled objects. In addition, geometric models can be edited, and similar models can be built from them, minimizing time and other resources.

7.1. Geometric Model Content

A geometric model consists of a geometric description of the modeled object. We use boundary representation for the description. A boundary representation accurately describes the surface of the object being modeled. If the geometric model consists of a set of elements that are supposed to move or be edited in coordination with each other, then geometric constraints are included in the geometric model. If it is required to repeat the construction of the geometric model many times for the purpose of its modification or for creating similar models, then a description of the model construction process is included in the geometric model. The list of manipulations reflecting the algorithmic sequence of the model construction is called its build history. The build history contains all the data necessary to build the model. If the object modeling is performed for several purposes then the mathematical model describes not only the geometric properties of the object, but also its other properties. The geometric model may also contain the required physical properties of its elements, such as density, modulus of elasticity, temperature, and opacity, as attributes.

Fig. 7.1.1.
Thus, a geometric model generally includes a description of the shape of the modeled object, geometric constraints, build history, and attributes (see Fig. 7.1.1).

In some cases, a geometric model may contain only a description of the shape of the modeled object. The description of the shape is sufficient if the model does not need to be edited or to be used to construct similar models, and also if the model is not to be used as a simulation of a mechanism. In such cases, the geometric constraints, build history, and attributes will not be present.

Several geometric description data formats are supported by geometric modeling systems. During data transfer from one geometric modeling system to another, the geometric description is passed on in one way or another, and geometric constraints, build history, and attributes are often omitted.

### 7.2. Geometric Model Uses

Geometric models make it possible to determine the surface area, volume, and inertial characteristics of a designed object, and to measure the lengths and angles of its elements. They make it possible to calculate dimension chains, and to determine the possibility of assembling the designed object. If the object is a mechanism, the model can be used to simulate and test its functionality and to calculate its kinematic characteristics.

When modeling processes in a continuous medium, we use models consisting of finite elements. For this, the internal volume of the model is divided into finite elements—pyramids and prisms joined by common faces and vertices. Finite elements are endowed with physical and other properties needed for simulating the real-world behavior of the simulated model. A finite-element model can be based on the shell of a geometric model. Thus, using the geometric model, we can set up a numerical experiment to determine the stress-strain state, frequencies and modes of natural oscillations, and stability of structural elements, as well as thermal, optical, magnetic, and other properties of modeled object.

From the geometric model we can calculate the trajectory of a cutting tool for its machining. With a given fabrication technology, the geometric model makes it possible to design tooling and perform pre-production procedures, and also to fabrication feasibility with a specified method and quality. Also, the fabrication process can be graphically simulated. To fabricate the object, the information about the process production equipment and many other production factors are required in addition to the geometrical information.

Many of these problems form whole sections of process and product simulation, and are just as complex as the problem of constructing a geometric model. The geometric model is the starting point for further manipulations. When constructing a geometric model we do not use the laws of physics, and the radius vector of each point of the boundary between the outer and inner parts of the modeled object is known; so we have to compose and solve algebraic equations. But the problems involving physical laws lead to the greater complexity of differential and integral equations.

Geometric models are used in computer graphics. A model can be visualized by constructing its vector or raster image. Simplified copies of the model are usually used
for imaging. To construct a vector image, a "wire-frame" is constructed on the basis of the geometric model, which is projected onto a surface of the image. To construct a raster image, approximation of the surface of the geometric model by triangular (or other) plates is used. Moreover, we can simulate the flux of light beams incident to and returning from the surface of the model. At the same time, elements of a model can be provided with appropriate color, transparency, texture, reflectivity, and light-scattering characteristics, as well as with other physical properties. The model can be lighted by lights of different colors and intensities from different directions.

We consider the use of geometric models for constructing images of modeled objects and calculation of their inertial characteristics. We will see that geometric models may contain several different descriptions of the shape of a modeled object, each used for different purposes.

7.3. Vector Image Construction

To construct a vector image of a modeled object, besides the geometric model, it is necessary to know the relative position of the model, the vantage point from which it is viewed, and the image plane. When constructing a vector image of a modeled object, a wire-frame model is used.

A wire-frame model can be obtained from a geometric model as a collection of solids and shells, with the faces removed, and the edges and vertices retained. Vector images are more informative if they are supplemented with visible lines of the model outline, and the hidden lines of the wire-frame are not shown. The lines of the outline inside the faces divide them into parts that are visible and invisible from the vantage point. In general, there may be several silhouette lines for one surface. Each silhouette line is either closed or ends at the boundaries of the surface. For different lines of sight, there are different sets of silhouette lines; when the model is rotated, silhouette lines must be rebuilt.

The problem of constructing vector images is reduced to the problem of determining the visible parts of the curves of a wire-frame model. In Fig. 7.3.1 we see the image of a model with removed hidden lines, and lines of smooth transitions between the faces are thinner than the lines of the edges and the silhouette lines.

Fig. 7.3.1.
Using silhouette lines we can partition the surface of the imaged object into visible and conditionally invisible areas. Let the vector \( \mathbf{i} \) be directed from a vantage point to a given point of the object. Then those areas of the surface are invisible for which the dot product of the normal to the surface and the vector \( \mathbf{i} \) is positive. Areas of the surface for which the dot product of the normal to the surface and the vector \( \mathbf{i} \) is negative are visible, provided that they are not obstructed by other visible areas of the surface closer to the vantage point. Similarly, we can judge the visibility of the model elements. If the normals to the faces joining at an edge are directed away from the vantage point in a certain region, then this part of the edge is invisible. Otherwise this part of the edge can be seen from the vantage point, or may be covered by some face. Thus, for some model elements, we can immediately determine their invisibility from the vantage point; but to determine the visibility of other elements of the model, we need to perform additional manipulations.

Let us consider the algorithm for determining the visibility of the model elements. Construct a wire-frame model of the object consisting of outline lines, and lines the edges of faces are based on. Let the wire-frame model consist of three-dimensional curves \( c_i(t_i), i=1,2,...,n \). The corresponding parallel or central projection onto a given plane can be constructed for each three-dimensional curve. Next, define the points of the curves at which their visibility may change. To do this, we find all the points at which the projections of three-dimensional curves \( c_i(t_i), i=1,2,...,n \) intersect. Use these points to divide the curves into segments. Now every segment of the curve between the dividing points is either completely visible or completely invisible. Now we have to find the visible parts of the curves, construct the projections for them, and delete duplicate projections.

To determine the visibility of segments of curves \( c_i(t_i), i=1,2,...,n \) we choose an arbitrary point \( r \) inside every segment. Then, we construct a straight line \( l(t)=r+t\mathbf{i} \), passing through the point \( r \) and the vantage point, and directed away from the vantage point. For a parallel projection, vector \( \mathbf{i} \) is parallel to the normal to the projection plane; for a central projection, vector \( \mathbf{i} \) is proportional to the vector \( r-w \), where \( w \) is the vantage point. Let us find the point of intersection of this line with surfaces of the geometric model. If the values of parameter \( t \) of the curve are non-negative for all the points of intersection, then the considered segment of the curve is visible. If among the values of parameter \( t \) for the points of intersection there is at least one that is negative, then the segment of the curve is invisible, as it is covered by one of the model surfaces located closer to the observer than the point \( r \). Continue to carry out this procedure with segments of all the curves whose visibility from the vantage point is not immediately evident.

If necessary, construct planar projections of the visible segments of the curves of the wire-frame model.

Polylines are used to construct a vector image of a curve. If we construct a set of points belonging to a curve and arranged in ascending order with respect to a parameter, and connect these points by segments, we obtain a polyline approximating the given curve. To make the polyline look smooth, its segments should be sufficiently small.

A sequence of points that the polyline approximating the curve passes through is called a polygon of the curve.
A projection of a three-dimensional polygon onto a plane is also a polygon. Therefore, curves and surfaces on a computer screen are usually accompanied by polygons.

The distance between the points of a polygon must be such that the polygon appears smooth. We can use the maximum distance between the curve and its approximating polygon as a control parameter. Let the curve \( c(t) \) be given, and suppose we are at a point on the curve \( t_0 \), which is a point of a polygon. It is required to find the parameter \( t_1 \) of the next point of the polygon, such that the deviation of the curve from its polygon does not exceed the value \( \delta \). Suppose that the curve in the vicinity of the point is close to a circle osculating at this point (see Fig. 7.3.2). The radius \( \rho \) of the osculating circle is equal to the radius of curvature of the curve and is determined by the formula

$$\rho = \frac{|c'|^3}{|c' \times c''|}.$$

![Fig. 7.3.2.](image)

By the Pythagorean theorem \( \left( \frac{h}{2} \right)^2 = \rho^2 - (\rho - \delta)^2 \), the square of half of the length of the chord is \( \left( \frac{h}{2} \right)^2 \approx 2\rho\delta^2 - \delta^2 \). The whole length of the chord is equal to

$$h \approx 2\sqrt{\delta(2\rho - \delta)}.$$

If the curve is close to the arc of the osculating circle, and the arc angle is small enough, then we can assume that the chord length is approximately equal to the length of the arc of the curve, and the increment of the parameter \( \Delta t \) on the length of the arc of the curve can be taken to be

$$\Delta t \approx \frac{h}{|c'|} = 2\sqrt{\delta(2\rho - \delta)} \frac{|c'|}{|c' \times c''|} = 2\sqrt{\delta \left( \frac{2|c'|}{|c' \times c''|} - \frac{\delta}{c' \cdot c'} \right)}.$$  

(7.3.1)
The change of parameter $\Delta t$ is called the parametric step. Thus, the parameter of the next point of the polygon can be assumed to be $t_1 = t_0 + \Delta t$. At an abrupt change in the direction or length of the second derivative at the point $t_1$, compared to the previous point, formula (7.3.1) yields an error; i.e., the deflection can be significantly larger than $\delta$. In this case, the step should be refined by determining the average radius of curvature of the curve in the considered segment.

The formula for calculating the parametric step between the points of a polygon (7.3.1) allows us to construct the polygon of the curve, displaced from the curve itself by no more than $\delta$. A projection of this polygon is also displaced from a projection of the curve by no more than $\delta$. If it is required to create an image $m$ times as large as the original one, the value of $\delta$ should be reduced by a factor of $m$.

Let us calculate the step of the parameter of the surface curve to construct its polygon. Let the point of some polygon of a surface $s(u_0, v_0)$ be determined by parameters $u_0$ and $v_0$. Let us find parameters $u_1$ and $v_1$ of the next point of the surface so that a three-dimensional segment from point $s(u_0, v_0)$ to point $s(u_1, v_1)$ is displaced from the surface by a distance not exceeding a specified value $\delta$. For this calculate the radius of curvature of the surface curve having the direction of the vector $[du\ dv]^T$. The radius of curvature of the normal section along the surface curve in the direction of the vector $[du\ dv]^T$ is determined by

$$\rho = \frac{g_{11}du^2 + 2g_{12}dudv + g_{22}dv^2}{b_{11}du^2 + 2b_{12}dudv + b_{22}dv^2},$$

(7.3.2)

where $g_{11}$, $g_{22}$ and $g_{12}$ are coefficients of the first quadratic form of the surface, and $b_{11}$, $b_{22}$ and $b_{12}$ are coefficients of the second quadratic form of the surface. Substituting (7.3.2) into (7.3.1) yields the increments for the parameters of the neighboring points in the polygon:

$$\Delta u \approx 2 \sqrt{\frac{\delta(2\rho - \delta)}{s_1 + s_2 \frac{dv}{du}}}, \quad \Delta v \approx 2 \sqrt{\frac{\delta(2\rho - \delta)}{s_1 \frac{du}{dv} + s_2}},$$

where $s_1 = \partial s/\partial u$ and $s_2 = \partial s/\partial v$ are derivatives of the radius vector of the surface at the considered point.

The radius of curvature (7.3.2) of the normal section of the surface in the direction of change of the first parameter is $\rho_u = g_{11}/b_{11}$, and the radius of curvature (7.3.2) of the normal section of the surface in the direction of change of the second parameter is $\rho_v = g_{22}/b_{22}$. In accordance with the curvature of the normal sections of the surface, the increment of the first parameter of the surface for the neighboring polygon point of the surface curve is

$$\Delta u \approx 2 \sqrt{\frac{\delta(2g_{11} - \delta)}{b_{11}}} \frac{1}{\sqrt{g_{11}}},$$

(7.3.3)
and the increment of the second parameter of the surface for the neighboring polygon point of the surface curve is

$$ \Delta v = 2 \sqrt{\frac{g_{22} - \delta}{b_{22}}} $$

(7.3.4)

The changes of parameters \( \Delta u \) and \( \Delta v \) are called parametric steps. For an abrupt change in direction or length of the second derivatives of the radius vector of a surface, formulas (7.3.3) and (7.3.4) give an error, and the steps should be refined by determining the average surface curvature at the considered segment.

For convenience, polygons belonging to the same object are combined in a polygon mesh. A set of polygons of a geometric model is called a mesh of polygons. The mesh of polygons of a curve consists of one polygon. The mesh of polygons of a surface consists of polygons of its borders, and possibly of several polygons of its surface curves. The mesh of polygons of a solid consists of polygons of the surface of its faces and polygons of its edges.

### 7.4. Optical Properties Modeling

To construct a realistic image of a modeled object, it is necessary to know its emittance, transparency, reflectivity, and its scattering characteristics, in different parts of the light spectrum. Moreover, we need information about the relative locations of the model, a vantage point, the image plane, light sources, and light-source spectrum and intensity. We characterize luminous flux by intensity—the energy flux density of the light wave.

Light arriving at the vantage point from the modeled object can be conditionally divided into the light emitted by the object, and light reflected and transmitted from other sources. Real objects absorb some part of the incident light, and transmit part and reflect part of the incident light. Distribution of the light incident to the object into an absorbed part, a transmitted part, and a reflected part depends on the light wavelength and on the physical properties of the object.

Most of the objects for which emitted light dominates in the light received from them radiate the light uniformly in all directions. If the radiating object is large, the visibility of its individual parts depends on the flow of energy emitted by them. The features of their shapes are seen as contours bounding a bright spot.

Perception of objects for which reflected and transmitted light dominate in the light received from them depends on the position of the vantage point, the position of light sources, the energy flow, and the optical properties of the object surface. When modeling reflected light it is customary to divide it into two parts: diffusely reflected and specularly reflected. This division is due to the laws describing the direction of rays of reflected light. If most of the light reflected from a surface can be described by the law of diffuse reflection, the surface is called opaque; if most of the light reflected
by the surface can be described by the law of specular reflection, it is called a mirror surface. Objects whose surfaces are capable of transmitting most of the incident light into their depths are called transparent. Light transmitted through a surface is also customarily divided into two parts: diffusely transmitted and directly transmitted. Directly transmitted light undergoes refraction. Transmitted light can be reflected from other surfaces.

We assume that the percentage of the emitted and absorbed light of the modeled object is negligible compared to that of the reflected and transmitted light. In this case, the light arriving at the vantage point is divided into four parts: diffusely reflected light; specularly reflected light; scattered light; and transmitted light.

For diffuse reflection, Lambert's cosine law is used. This law establishes a correspondence between the amount of reflected light and the cosine of the angle $\theta$ between the direction to a point source of light of intensity $I_p$ and the normal to the surface. The intensity of diffusely reflected light is determined by the formula

$$I_d = k_d I_p \cos \theta,$$

where $k_d$ is a diffuse reflection coefficient, depending on the material of the surface. The amount of diffusely reflected light does not depend on the observer's position. Matte surfaces reflect similar amounts of light energy in all directions, but this amount is proportional to $\cos \theta$.

Most of the incident light is reflected from a mirror surface in the direction lying in the same plane with the direction of the incident light and the normal $m$ at the point of incidence, and having an angle $\theta$ with the normal $m$, equal to the angle of incidence of the light (see Fig. 7.4.1). This direction is called the direction of the reflected light. When deviating by an angle $\alpha$ from this direction, the intensity of reflected light decreases sharply. Phong proposed to describe the change of the intensity of the specularly reflected light around the direction of the reflected light by the function $\cos^n \alpha$, where $n$ ranges from one to two hundred.

![Fig. 7.4.1.](image)

The amount of reflected light also depends on the angle of incidence $\theta$, but this dependence is weak. In our model, the dependence of the reflected light on the angle of incidence is replaced by the constant $f(\theta) = k_s$, which is chosen empirically such that the results are aesthetically acceptable. If the intensity of the light source is $I_p$, then the intensity of the specularly reflected light is determined by the Phong formula

$$I_s = k_s I_p \cos^n \alpha,$$

(7.4.1)
where $k_s$ is called the **coefficient of specular reflection** and $n$ is called the **coefficient of brightness**. The larger the $n$, the sharper and narrower the light flare.

The intensity of the scattered light is the same in all directions; hence, the same amount of scattered light arrives at the vantage point from each point of the surface. In the presence of only scattered light of intensity $I_a$ at the vantage point from each point of the object, light of intensity

$$I = k_a I_a,$$

arrives there, regardless of the orientation of the surface at these points, where $k_a$ is a coefficient determining both the diffusely and specularly reflected portions of the scattered light.

For simplicity, we assume that the percentage of diffusely transmitted light is small in comparison with that of the directly transmitted light, and omit the diffusely transmitted light from consideration. The directly transmitted light undergoes refraction at the interface between two media. The refracted ray is coplanar with the incident ray and with the normal $m$ at the point of incidence (see Fig. 7.4.2).

![Diagram](image)

Fig. 7.4.2.

Its direction forms an angle $\theta_1$ with the normal, and it is described by the law of refraction

$$n_0 \sin \theta = n_1 \sin \theta_1,$$

where $n_0$ is the refraction index of the media on the side of the incident light, and $n_1$ is the refraction index of the medium on the other side of the interface. For the intensity of the directly transmitted light, we adopt a law of change with direction analogous to law (7.4.1.) for directly reflected light:

$$I_u = k_d I_d \cos \beta,$$

where $\beta$ is the angle of deviation of the direction of the transmitted light from the direction to the vantage point.
For a transparent object, not only reflected light arrives at the vantage point from each point of the surface, but also light transmitted by the surface from the interior of the object. Light transmitted by the surface derive from reflection from other surfaces or from sources of light through a transparent object. In both cases, the light will go through the material and will be partially absorbed by it. The intensity of the light transmitted through the material decreases exponentially, and is described by the Beer–Lambert–Bouguer law

$$ I = I_0 e^{-\mu l}, $$

where \( I_0 \) is the intensity of the light at the entrance to the absorbing media, \( l \) is the distance traveled, and \( \mu \) is the light absorption coefficient of the media.

The intensity of light arriving at the vantage point from a non-radiating opaque object in our model is determined by the sum of three components:

$$ I = k_a I_a + I_p k_s \cos \theta + I_p k_s \cos^n \alpha. $$ (7.4.2)

Shading results obtained from formula (7.4.2) are realistic, but have a significant drawback. When two planar surfaces of the same color are parallel to each other and their projections overlap, the surfaces will be similarly shaded, and their images will merge—regardless of their distance from the vantage point. To eliminate this effect, the intensity of the light emanating from the surface is considered to be dependent on the distance, and we write the formula for calculation of the intensity of the light in the form

$$ I = \frac{k_a I_a}{1 + k_r (r - r_0)} + I_p \left( k_d \cos q + k_s \cos^n \alpha \right), $$ (7.4.3)

where \( r \) is the distance from the vantage point to the point on the surface, \( r_0 \) is the distance from the vantage point to the nearest point on the object, and \( k_r \) is the coefficient of influence of the remoteness of the point of the object on the intensity of light incoming from it. When \( k_r = 0 \), we obtain formula (7.4.2). The intensity of light from the nearest point also coincides with (7.4.2). The distance \( r_0 \) is introduced due to the fact that for parallel projection, the vantage point is placed at infinity. For central projections, we can assume that \( r_0 = 0 \); thus when the entire object recedes from the vantage point, we experience a decrease in its brightness.

If the modeled object is transparent, then besides reflected light, transmitted light arrives at the vantage point, and formula (7.4.3) takes the form

$$ I = \frac{k_a I_a}{1 + k_r (r - r_0)} + I_p \left( k_d \cos \theta + k_s \cos^n \alpha \right) + I_t k_t \cos^n \beta, $$ (7.4.4)

where \( I_t \) is the intensity of the light penetrating from the other side of the surface.

If there are multiple light sources, each of them contributes to the intensity of the light arriving at the vantage point. For multiple light sources, each of intensity \( I_{pi} \), formula (7.4.3) takes the form
$$ I = \frac{k_d I_a}{1 + k_r (r - r_0)} + \sum_i I_{pi} (k_d \cos q_i + k_s \cos^n \alpha_i). $$

Formula (7.4.4), which calculates the intensity of light coming from a transparent surface, is similarly changed. It takes the form

$$ I = \frac{k_d I_a}{1 + k_r (r - r_0)} + \sum_i I_{pi} (k_d \cos \theta_i + k_s \cos^n \alpha_i) + \sum_j I_{ij} k_t \cos^n \beta_j, $$

where \( I_{ij} \) is the intensity of the \( j \)-th transmitted light ray (penetrating from the other side of the surface).

Light and human perception are complex phenomena that are not fully explored. From experimental studies, it is known that light having a wavelength of a certain part of the spectrum is perceived by the eye as light of a certain color. The perceived color of the light depends on properties of the light source, the viewed surface, and the human visual system. Dependence of the intensity of light perceived by the eye on the human visual system is shown in Fig. 7.4.3.

![Fig. 7.4.3.](image)

The brightness of the circular areas within the two squares is the same, but the circle on the light background appears darker than the same circle on a dark background. This phenomenon is called simultaneous contrast. A similar phenomenon exists in the perception of color images. Depending on the color and brightness of the environment, colored areas may appear to have a different hue (seem to change color). In addition, the boundaries of regions of constant intensity appear brighter than the central parts of those regions. This phenomenon is called the Mach bands effect.

Representation of light as three components is used to produce color images. The eye’s sensitivity is not the same for different colors: It is greatest for green least for blue. Moreover, the eye does not perceive the absolute value of a color’s intensity, but rather its relative value. Hence, a linear distribution of intensity levels of light perceived by the human visual system becomes logarithmic.

We represent the intensity of incident light in the form of red, green, and blue components. Let us assume that all three components have equal intensity in white. This color model is an additive system of color mixing, and is called the RGB model (red, green, blue). These are the main colors of the RGB model. The corresponding complementary colors are cyan, magenta, and yellow. If the main color is combined in equal proportion with its complementary color, we obtain white. Thus, cyan can be represented as the sum of green and blue, magenta can be represented as the sum of
blue and red, and yellow can be represented as the sum of red and green. Other hues are obtained by mixing the primary colors in different proportions. This model is not unique, but it is widespread; representing color as a weighted sum of red, green, and blue is consistent with experimental data, and is easily implemented.

In accordance with the RGB model, the intensity of light incident to and reflected by an object can be represented as the sum of intensities of red, green, and blue:

$$ I = I_R + I_G + I_B. $$

The intensity of each color is determined by one of the above formulas, in which each color component is described by its coefficient; for example,

$$ I_R = \frac{k_{aR}I_a}{1 + k_r(r - r_0)} + I_p(k_{dR}\cos\theta + k_{sR}\cos^n\alpha) + I_tk_{tR}\cos^n\beta,$$

$$ I_G = \frac{k_{aG}I_a}{1 + k_r(r - r_0)} + I_p(k_{dG}\cos\theta + k_{sG}\cos^n\alpha) + I_tk_{tG}\cos^n\beta,$$

$$ I_B = \frac{k_{aB}I_a}{1 + k_r(r - r_0)} + I_p(k_{dB}\cos\theta + k_{sB}\cos^n\alpha) + I_tk_{tB}\cos^n\beta, \tag{7.4.5}$$

Intensities must be normalized at \( r = r_0 \). By varying the direction of the incident light and the values of the coefficients of diffuse reflection, specular reflection, and transmission for different components of light, we can choose the desired image of an object. If there are several light sources, each of them must be taken into account in formulas (7.4.5) by the corresponding terms.

### 7.5. Raster Image Construction

When constructing raster images, it is necessary both to determine the visible part of the geometric model and the color and brightness of each pixel in the image. If the modeled object is not transparent, the color of each pixel depends on the color of the face nearest to the observer at this point; and its brightness depends on the illumination of the object, the optical properties of its surface, and the orientation of the normal to the surface with respect to the rays of incident light and to the line connecting the considered point and the vantage point. If the modeled object is transparent, then the color of a pixel in the image depends on the color of several faces, on their optical properties, and on the orientation of their normals.

In general, for each point in an image, we construct a line passing through the considered point of the image and the vantage point, and find the point of intersection of this line with the displayed model. It is necessary to know the direction normal to the surface of the model at the intersection points, and the optical properties of the surface, such as its ability to emit radiation, to transmit and reflect light in different spectral ranges. According to the location of the light sources, the optical properties of
a point of the model, and direction of its normal, the color and brightness of an image point can be determined.

It is much simpler to define the points of intersection with lines of sight for planar surfaces than for curved surfaces; thus, a simplified model is sometimes used for construction of raster images, in which the surface of the model is approximated by a set of triangular plates. Fig. 7.5.1 shows a raster image of an opaque object constructed as a simplified model.

![Fig. 7.5.1.](image)

Simplified models consist of triangular plates. The normals to the surface of the model are calculated at the vertices of the triangles. The triangular plates are joined along their common sides. The normals at the vertices have their true direction, and are assumed to change from vertex to vertex according to the linear law within each triangle. At vertices $p_a$, $p_b$, and $p_c$ of some triangle, let the normals be described by unit vectors $m_a$, $m_b$, and $m_c$. We assign the direction of the following vector to the normal on the surface of the triangle

$$m(a,b,c) = am_a + bm_b + cm_c,$$

(7.5.1)

where $a$, $b$, $c$ are barycentric coordinates of point $p$ of the triangular plate (see Fig. 7.5.2).

![Fig. 7.5.2.](image)

The barycentric coordinates are defined by the system of equations

$$ax_a + bx_b + cx_c = x,$$
$$ay_a + by_b + cy_c = y,$$
$$a + b + c = 1,$$
where \( x_a \) and \( y_a \) are the coordinates of the projection of point \( p_a \); \( x_b \) and \( y_b \) are the coordinates of the projection of point \( p_b \); \( x_c \) and \( y_c \) are the coordinates of the projection of point \( p_c \); and \( x \) and \( y \) are the coordinates of the projection of point \( p \) onto some plane (say, the image plane). In general, vector \( m(a,b,c) \) does not have unit length, and therefore should be normalized.

In the approximation (7.5.1), the normals gradually change their direction when moving from one triangle to another. That is why the surface looks smooth on the raster images. This approach is used in the Phong method for shading of raster images. If the true direction of the normal to the plate is used within each triangular plate, then the image looks faceted due to Mach bands (see Fig. 7.5.3). The Phong method completely eliminates Mach bands. Let us consider the construction of a raster image of a model in the plane. It is simpler to search for the points of intersection of the line and the triangular plates if the search is performed in the local coordinate system associated with the image plane; thus, let us translate the simplified model to the local coordinate system associated with the image plane.

![Fig. 7.5.3.](image)

Let the construction of a raster image of the model be performed on the plane

$$
p(x,y) = q + x i_x + y i_y,$$

with its beginning at point \( q=[q_1 q_2 q_3]^T \) and orthogonal unit coordinate axes \( i_x=[x_1 x_2 x_3]^T \) and \( i_y=[y_1 y_2 y_3]^T \). Let us associate plane \( p(x,y) \) with the local coordinate system \( Qxyz \). A line-of-sight vector is directed perpendicular to the plane towards the basis vectors \( i_z=i_x \times i_y=[z_1 z_2 z_3]^T \). The global coordinates \( r_1, r_2, \) and \( r_3 \) of the point of the model and its local coordinates \( x, y, z \) are related by

$$\begin{bmatrix}
x \\
y \\
z
\end{bmatrix} =
\begin{bmatrix}
x_1 & x_2 & x_3 \\
y_1 & y_2 & y_3 \\
z_1 & z_2 & z_3
\end{bmatrix}
\begin{bmatrix}
r_1 - q_1 \\
r_2 - q_2 \\
r_3 - q_3
\end{bmatrix}.$$  

(7.5.2)

The components of the normal in the global coordinate system, \( m_1, m_2, \) and \( m_3 \), and the components of the normal in the image plane coordinate system, \( x_m, y_m, \) and \( z_m \), are related by
Let us translate the simplified model and the light sources into the local coordinate system using (7.5.2) and (7.5.3).

When the vantage point is infinitely distant from the image plane, the lines passing through the image points and the vantage point are parallel to each other, and orthogonal to the image plane.

When constructing a perspective image, we subject the simplified model to an additional transformation: the local coordinates \( x \) and \( y \) of the vertices of the triangular plates are multiplied by the factor

$$ k_p = \frac{w}{w - z},$$

where \( w \) is the distance from the viewpoint to the image plane, and the normals at the vertices of the triangular plates are rotated by the angle

$$\eta = \arccos \left( -\frac{(r-w) \cdot i_z}{|r-w|} \right) = \arccos \left( -\frac{z-w}{\sqrt{xx + yy + (z-w)(z-w)}} \right)$$

about the vector

$$ v = -\frac{(r-w) \times i_z}{|(r-w) \times i_z|} = \frac{1}{\sqrt{xx + yy}} \begin{pmatrix} -y \\ x \\ 0 \end{pmatrix},$$

where \( w \) is the radius vector of the vantage point; \( r \) is the radius vector of the surface point, at which the normal is computed; and \( i_z \) is the normal to the image plane. The rotation of vector \( m \) is described by

$$ m_p = (vv^T) \cdot m + \cos \eta (E - vv^T) m + \sin \eta v \times m.$$

Thus, we generate a perspective image in the same manner as we do a parallel image, but for an accordingly distorted simplified model.

To determine the color and brightness of an image point with coordinates \( x \) and \( y \), we find the intersection of the line orthogonal to the image plane passing through the considered point of the image within the simplified model. In the local coordinate system, this search is reduced to determining the triangular plates, in the projection of which lies the point with coordinates \( x \) and \( y \). The latter problem is a two-dimensional one. The points of the image are located within the projection of the plate with vertices \( p_a, p_b, \) and \( p_c \), if its barycentric coordinates \( a, b, \) and \( c, \) calculated relative to the vertices of the plate, take non-negative values. If at least one of the barycentric
coordinates is negative, it means that the triangular plate is not intersected by the passing through the image point and the plane orthogonal to the image. For intersecting triangular plates, we compute the direction of the normal and optical properties of the plates at the intersection points. If the modeled object is not transparent, then we are interested only in one triangular plate, for which the intersection point has the largest coordinate. Using the described method, we find the points of the surface of the model for the considered point of the image, the optical properties of the surface, the direction of the surface normal, direction to each light source, and the intensity and color range of each light source. Using this information, we can determine the color and brightness of the image point.

To create irregularities on the surface of the model we can use random variation of the normal. Fig. 7.5.4 shows a model whose surface normals have been assigned random deviations.

![Fig. 7.5.4.](image)

A pattern similar to wallpaper patterns can be drawn on the surface of a model. To draw a pattern on the surface, it is required to define a functional relationship between the image plane and the plane of the surface parameters.

In general, when the vantage point does not coincide with a light source, some part of the model surface is blocked from the source—that is, it is in shadow. The algorithm for determining the shading of points is similar to the algorithm for determining the visibility of points. If a point of the surface is visible from a light source, it is lighted. The points of the surface of a model that can be seen from the vantage point and from a light source transmit the reflected light of the source in the raster image. The points of the surface of the model that are visible from the vantage point, but not visible from a light source, are in shadow, and transmit only scattered and emitted light. Fig. 7.5.5 shows the image of a model taking shadow into account.

![Fig. 7.5.5.](image)
Sharp shadows are produced by point light sources. When a model is illuminated by the light of distributed sources, penumbra areas will appear. Penumbras appear in the image of a point of a model from which only a part of a distributed light source can be seen.

For transparent models, light reflected from both the nearest surface and from other surfaces arrives at the vantage point, and these surfaces can be seen through it. If the refraction of the light is not taken into account, then the light from all the surfaces intersecting with the line of sight arrives at the vantage point. Fig. 7.5.6 shows an image of a transparent object.

![Image](image)

Fig. 7.5.6.

When modeling light refraction, the line of sight must be shifted for hidden surfaces. The intensity of the light arriving from each surface is weakened due to the absorption of light by the substance. To determine which light rays arrive at the vantage point, ray tracing is used.

Tracing starts from the vantage point, and light rays are tracked to each light source. A light ray incident on a surface is divided into four main parts: diffusely transmitted light, directly transmitted refracted light, diffusely reflected light, and specularly reflected light. Similarly, a light ray emanating from a surface of the model is the sum of two reflected components of the light and two components of the light coming from behind the surface. Thus, whenever the ray traced from the vantage point arrives at the surface of the model, the appearance of several new rays is possible; that is, the traceable ray is split into several components. In general, diffusely reflected light and diffusely transmitted light can arrive from an infinite number of directions. That is why we usually trace the rays of light that appear as a result of specular reflection and refraction. As a result, when a traced ray approaches the surface of a transparent model, it is split into two parts. Scattered light and diffusely reflected light can be received from the surface nearest to the vantage point. For each traced ray, we must obtain its intersection with all the surfaces of the model. Using the surface properties, it is determined whether the light ray should be split at the points of intersection.

### 7.6. Triangulation

A surface of a modeled object can be approximated by a set of triangular plates. This is useful for constructing raster images, calculating inertial characteristics, determining the collision of model elements, generating finite elements, and other purposes. In the simplest case, such a model can be represented by an array of points in space, and by an array of triangles whose vertices refer to the points of the first array.
To obtain an image of the model without Mach bands, the array of points should be supplemented with the array of the normals synchronous to it at these points. For prompt access to the elements of the described model, the points and triangles can be grouped and sorted as needed. In more complicated cases, the model can be supplemented with the edges containing the information about the points and triangles linked by them.

A geometric model consisting of a set of triangular plates can be obtained from a geometric model in the form of a shell. For this, domains of the surfaces of the model are split into triangular and quadrangular sub-domains. A triangular plate can be constructed for each triangular sub-domain. A quadrilateral plate, or two triangular plates, dividing a sub-domain by a diagonal into two triangular sub-domains, can be constructed for each quadrilateral sub-domain. The combination of these plates approximates the surface of the model to a controllable degree of accuracy.

**Triangulation** is the name of the process and the result of constructing a finite number of non-overlapping triangles joined together by common sides.

Using triangulation, we can approximate the surface of a model by triangular plates. This problem is solved in the parameter plane of the surface, and is two-dimensional.

In the simplest case, the problem of triangulation is formulated as follows: Given a set of points in the plane, construct the maximum possible number of non-overlapping triangles with vertices at these points. The segments connecting the vertices of the triangles and being the sides of the triangles are called *edges*. In general, to construct a triangulation is to connect the given vertices by non-intersecting edges, so that in the resulting triangulation it is impossible to construct a new edge that does not intersect with existing edges. This problem may have several solutions; therefore, there are various types of triangulation having characteristic properties.

A triangulation is called **optimal** if the sum of the lengths of all edges is minimal among all possible triangulations constructed with the same original data.

Optimal triangulations are rarely used, due to the complexity of constructing them. Other triangulations that are not optimal are often used in practice. These include **greedy triangulation** and the **Delaunay triangulation** (Boris Delaunay).

A triangulation is called **greedy** if it is constructed by a "greedy" algorithm. Greedy algorithms are algorithms that never cancel what was previously done.

A greedy triangulation algorithm performs the following manipulations: It calculates the distances between all pairs of given vertices of the future triangulation, sorts them in ascending order, and constructs edges of triangles starting with the minimum distance using the sorted pairs of vertices, verifying their intersection with the existing edges. A new edge is constructed, if it does not intersect any edge already constructed. If all the distances between vertices are different, then the greedy triangulation is unambiguous; otherwise, it depends on the sequence of insertion of the edges of equal length.

A triangulation is called a **Delaunay triangulation**, if inside the circle circumscribed about a triangle there are no other vertices of triangles.

Delaunay triangulation does not allow the construction of unnecessarily elongated triangles. Delaunay triangulation is unique if no four vertices lie on a circle. Delaunay triangulations have useful properties and can be calculated quickly, and therefore are the most frequently used triangulations in practice.
Consider the construction of a Delaunay triangulation for a given set of two-dimensional points. Let us find the nearest point to an arbitrary chosen point. Construct an edge between the points. Try to construct a triangle on this edge, the third vertex of which is to the left or the right from the edge. Suppose it is required to construct a triangle whose side is edge \( AB \) (see Fig. 7.6.1).

![Fig. 7.6.1.](image)

A circle can be drawn through vertices \( A \) and \( B \) and any vertex \( V \) that is not collinear with them. The center of the circle passing through points \( A, B, \) and \( V \) lies on the intersection of the perpendiculars to the midpoints of segments \( AB, VB, \) and \( AV \). Let vertices \( A, B, \) and \( V \) be described by the two-dimensional radius vectors \( a=[x_a\ y_a]^T, b=[x_b\ y_b]^T, \) and \( v=[x_v\ y_v]^T, \) respectively. Let us construct the straight line

$$\begin{bmatrix}
x \\
y
\end{bmatrix} = \frac{1}{2} \begin{bmatrix}
x_a + x_b \\
y_a + y_b
\end{bmatrix} + t \begin{bmatrix}
y_a - y_b \\
x_b - x_a
\end{bmatrix},$$

perpendicular to segment \( AB, \) passing through its midpoint, and the straight line

$$\begin{bmatrix}
x \\
y
\end{bmatrix} = \frac{1}{2} \begin{bmatrix}
x_v + x_b \\
y_v + y_b
\end{bmatrix} + w \begin{bmatrix}
y_v - y_b \\
x_b - x_v
\end{bmatrix},$$

perpendicular to segment \( VB, \) passing through the midpoint of segment \( VB. \) At the point of intersection of the lines, the right-hand sides and left-hand sides of (7.3.1) and (7.3.2) are equal to each other. The intersection of lines (7.6.1) and (7.6.2) is found by solving the system of equations

$$\frac{1}{2}(x_a + x_b) + t(y_a - y_b) = \frac{1}{2}(x_v + x_b) + w(y_v - y_b)$$

$$\frac{1}{2}(y_a + y_b) + t(x_b - x_a) = \frac{1}{2}(y_v + y_b) + w(x_b - x_v)$$

for the parameters of the straight lines \( t \) and \( w, \) defining the position of the point on the straight lines. We are interested in parameter \( t. \) With the help of this parameter and (7.6.1), the position of the center of the circle, passing through vertices \( A, B, \) and \( V, \)
lying on a perpendicular to the midpoint of \( AB \), can be obtained. Solving the system of equations, this parameter is:

$$t = \frac{1}{2} \left( \frac{(x_v - x_b)(x_v - x_a) + (y_v - y_b)(y_v - y_a)}{(y_v - y_b)(x_b - x_a) - (x_v - x_b)(y_b - y_a)} \right).$$  

(7.6.3)

For the center of the circle lying at the middle of segment \( AB \), the value of parameter \( t \) is zero. For the centers of the circles lying to the left of segment \( AB \), parameter \( t > 0 \). For the centers of the circles lying to the right of segment \( AB \), parameter \( t < 0 \). We choose the vertex \( V \) as the third vertex of the Delaunay triangle, the corresponding circle of which does not contain other vertices on the same side relative to the segment \( AB \) that the vertex \( V \) lies on. We call such a vertex nearest. For the vertex that is nearest from the left of segment \( AB \), parameter \( t \) has a minimum value, and for the vertex that is nearest from the right of segment \( AB \), parameter \( t \) has a maximum value.

In general, two nearest vertices can be found for an edge: one on the left of the edge, the other on the right of the edge. Thus two adjacent Delaunay triangles can be constructed. It is possible to find only one nearest vertex for an edge with respect to which all the given points lie only on one side. An edge of the latter type is called a boundary edge. The Delaunay triangulation algorithm is executed until two adjacent triangles are constructed for each already existing inner edge, and one triangle is constructed for each boundary edge. As the result, we obtain a triangulation of the inner area of a convex polygon containing all the given vertices (see Fig. 7.6.2).

![Fig. 7.6.2.](image)

The Delaunay triangulation can be obtained from any other triangulation by rearranging adjacent triangles \( ABC \) and \( ADB \), that do not satisfy the Delaunay condition, into a pair of triangles \( ADC \) and \( BCD \), satisfying the Delaunay condition (see Fig. 7.6.3).

![Fig. 7.6.3.](image)
The triangulation problem can be formulated as follows: There is a partially constructed triangulation to which a new vertex is added; it is required to complete the triangulation.

Construction of the triangulation by sequentially adding points to the partially constructed triangulation is called **iterative triangulation**.

In this approach, first the position of the new vertex with respect to the existing triangulation is determined, and—depending on the result—certain manipulations are performed. If it coincides with the existing vertex, nothing is done. If the new vertex falls on some edge, then the edge is divided into two edges, and the triangles adjacent to the edge are divided into two smaller triangles. If the new vertex falls inside a triangle, then the triangle is removed, and construction of new triangles involving the new vertex is performed inside the formed polygon. Fig. 7.6.4 shows the process of inserting a new vertex $V$, falling into the triangulation.

![Fig. 7.6.4.](image)

If the new vertex does not fall inside the triangulation then there are boundary edges with which the vertex can form new triangles. In all cases, when new triangles appear, fulfillment of the Delaunay condition is checked for the new triangles and their neighbors. When the Delaunay condition is violated, local reconstruction of the triangulation is performed (see Fig. 7.6.3).

In practical triangulation problems, there are sometimes conditions besides the given vertices that tend to complicate things. Most commonly, the additional conditions are curves that must somehow be related to the triangulation. In some cases, the curves must be fitted into the triangulation; in other cases, the triangulation must be fitted into the given curves.

Suppose it is necessary to triangulate a two-dimensional parameter domain of a surface bounded by a closed polyline, containing a set of points within the domain. To solve this problem, orient the polyline bounding the domain so that the domain lies to the left of it. Construct an edge on each segment of the polyline. Each specified point and vertex of the polyline will be used as a vertex of the triangulation. Edges and vertices involved in the triangulation algorithm are called **active**. At the beginning, all the edges and vertices are active. The construction of triangles starts with an arbitrary boundary edge. For each edge we seek the vertex that lies to the left of it and that can be used to construct the triangle.

Let us find the nearest vertex to the selected edge, whose corresponding circle does not contain other vertices. Suppose the nearest vertex $V$ is found for the boundary edge $AB$. The right-hand side of (7.6.3) takes the minimum value for this vertex. Check if segments $AV$ and $BV$ intersect with active edges—that is, whether it is possible to construct a triangle $ABV$. If the construction of the triangle is impossible, then move on to the next edge; otherwise, construct the triangle $ABV$ and classify the edge $AB$ as inactive.
The term inactive designates edges and vertices that do not participate in the algorithm of triangulation. If there is no edge $BV$ among the boundary edges, then we construct a new boundary edge on the interval $VB$. But if there is an edge $BV$ among the boundary edges, then we classify it and the vertex $B$ as inactive. If there is no edge $VA$ among the boundary edges, then we construct a new boundary edge on the interval $AV$. But if there is an edge $VA$ among the boundary edges, then we classify it and the vertex $A$ as inactive.

The triangulation process is shown in Fig. 7.6.5, where the active edges are indicated by thick lines, while inactive edges are indicated by thin lines.

![Fig. 7.6.5](image)

The polyline formed by the active edges changes in the triangulation process. The region being triangulated decreases at the same time. The described algorithm can be used when there are no vertices within the bounded region, and for the region within which there are cutouts not belonging to them, described by polylines. In this case, along with the cutouts’ border, we also construct edges on the segments of the polylines, giving them an orientation such that the domain lies to the left of the edges. These edges are involved in the triangulation in the same way as the edges of the outer border. The process of triangulation of a region with one internal cutout is shown in Fig. 7.6.6.

![Fig. 7.6.6](image)
In the process of triangulation, the external and internal boundary polygons formed by the active edges will eventually merge. The triangulation is complete when the last triangle is constructed and all the vertices and edges become inactive.

7.7. Surface Triangulation

For approximation of a surface by triangular flat plates, joined together by common sides, triangulate the domain of the surface parameters and map it into three-dimensional space by constructing a triangular plate for each triangular sub-domain.

In general, the boundary of a surface is described by two-dimensional closed composite curves in the parameter space of the surface. Approximate the boundaries of the domain of parameters of the surface by two-dimensional closed polylines. Orient the polylines so that the domain of the parameters is on the left of the polygon segments. Construct a set of two-dimensional points within the domain. For points within the domain, take the points of intersection of the set of lines $u_i=\text{const}$, $i=1,2,\ldots,m$, with the set of lines $v_j=\text{const}$, $j=1,2,\ldots,n$. We control the dimensions of the sides of the triangles and the distance between the points of the set within the domain by the parametric steps of the boundary curves and parametric steps of the surface. As an example, consider a triangulation of a surface, shown in Fig. 7.7.1.

![Fig. 7.7.1.](image)

Construct the polylines that approximate the boundary curves $c_j(t)=s(u_j(t),v_j(t))$ of the surface $s(u,v)$ (see Fig. 7.7.2). If triangulation of the surface is performed to construct a raster image, the parametric steps along the boundary are calculated by formula (7.2.1), controlled by the deflection value $\delta$. If the surface triangulation is performed to calculate inertial characteristics, then the parametric steps along the boundary are calculated by formula (3.12.2), controlled by the angular deviation value $\Delta\alpha$.

Let the boundary curves of the domain of surface parameters $s(u,v)$ be located inside the rectangle defined by the maximum and minimum values of the parameters $u_{\min}, u_{\max}, v_{\min}, v_{\max}$. Let us divide the rectangular domain $u_{\min}\leq u\leq u_{\max}, v_{\min}\leq v\leq v_{\max}$, of the surface into rectangular sub-domains by the planar lines $u_i=\text{const}$, and $v_j=\text{const}$, $i=1,2,\ldots,m$, $j=1,2,\ldots,n$. If the surface is being triangulated in order to construct a raster image, the parametric steps $\Delta u_i=u_{i+1}-u_i$ between the adjacent lines $u_i=\text{const}$ in accordance with formula (7.3.3) are taken as equal to
$$ \Delta u_i = \min \left( 2 \sqrt{\delta \left( \frac{2}{b_{11}(u_i, v)} - \frac{\delta}{g_{11}(u_i, v)} \right)} \right), \text{ for all } v_{\min} \leq v \leq v_{\max}, $$

and the parametric steps \( \Delta v_j = v_{j+1} - v_j \) between the adjacent lines \( v_j = \text{const} \) in accordance with formula (7.3.4) are taken to equal

$$ \Delta v_j = \min \left( 2 \sqrt{\delta \left( \frac{2}{b_{22}(u, v_j)} - \frac{\delta}{g_{22}(u, v_j)} \right)} \right), \text{ for all } u_{\min} \leq u \leq u_{\max}. $$

If the surface is being triangulated to calculate its inertial characteristics, the parametric steps \( \Delta u_i = u_{i+1} - u_i \) between the adjacent lines \( u_i = \text{const} \) in accordance with formula (3.12.3) are taken to equal

$$ \Delta u_i = \min \left( \frac{\Delta \alpha \sqrt{g_{11}(u_i, v)}}{b_{11}(u_i, v)} \right), \text{ for all } v_{\min} \leq v \leq v_{\max}, $$

and the parametric steps \( \Delta v_j = v_{j+1} - v_j \) between the adjacent lines \( v_j = \text{const} \) in accordance with formula (3.12.4) are taken to equal

$$ \Delta v_j = \min \left( \frac{\Delta \alpha \sqrt{g_{22}(u, v_j)}}{b_{22}(u, v_j)} \right), \text{ for all } u_{\min} \leq u \leq u_{\max}. $$

Fig. 7.7.3 shows a partitioning of the domain \( u_{\min} \leq u \leq u_{\max}, \ v_{\min} \leq v \leq v_{\max} \) of the considered surface by the described method.

Define rectangles that are located within the domain of the surface, and discard the other rectangles (see Fig. 7.7.4). Triangulate the part of the surface domain that is not included in the rectangular sub-domains using the Delaunay algorithm for a bounded domain, described above. Fig. 7.7.5 shows a finite partition of the surface into quadrangular and triangular sub-domains.
Dividing each quadrangles by a diagonal into two triangles, we obtain the triangulation of the surface.

7.8. Shell Triangulation

A geometric model in the form of a shell can be the basis for a geometric model consisting of a set of triangular plates. For this we construct a set of triangles joining with each other along their common sides by triangulating the faces of the shell. A set of triangular plates with common normals at the common points is constructed for each face. Sets of triangular plates approximating adjacent faces of the shell are related to each other. If we triangulate some faces independently, then the plates of the triangulation will not be joined by common sides at the boundaries of the faces (see Fig. 7.8.1). The triangulation of an individual surface is different from the triangulation of the shell faces. In the latter case, the common sides and vertices of the boundary triangles for adjacent faces is consistent (see Fig. 7.8.2).

Triangles of adjacent faces are joined along the sides that coincide in the space. Otherwise, the triangulation will contain a slit. If the triangulation is performed to construct a raster image, each vertex of the triangle contains the normal to the model surface. Two different normals must be calculated at the coinciding vertices of adjacent triangles belonging to two different faces, one for one face and another for the other adjacent face. If during the transition from one triangle to another triangle of the same face, the normal changes smoothly, then during the transition from a triangle of one face to an adjacent triangle of another face the normal changes abruptly.
7.9. Inertial Properties

To calculate the inertial characteristics of a modeled object, we must know the density of the solids that model the individual elements of the object, as well as knowing the object geometry. We assume that the density of each solid is constant throughout its volume. This assumption allows us to reduce the volume integrals over the solid to the integral over the surface of the solid's face. We use the divergence theorem to calculate the volume integrals

$$ \iint_S m \cdot F(r) dS = \iiint_V \nabla \cdot F(r) dV, $$  

(7.9.1)

where \( m \) is the normal to the surface of the solid, \( F(r) \) is a vector function of the points of the solid, \( r \) is the radius vector of a point of the solid, and \( \nabla \) is the Hamiltonian nabla operator. Recall that the normal \( m \) is always directed outward from the solid. The inertial characteristics are calculated in the Cartesian rectangular system whose coordinates are denoted by \( x, y, \) and \( z \).

The surface area of a solid is the sum of areas of its faces, and can be calculated by the formula

$$ S = \sum_i \iint_{\Omega_i} \sqrt{g_{11} g_{22} - g_{12}^2} \, du_i dv_i, $$

where \( u_i \) and \( v_i \) are surface parameters of the \( i \)-th face of the solid; \( g_{11}(u_i, v_i), g_{12}(u_i, v_i), g_{21}(u_i, v_i), \) and \( g_{22}(u_i, v_i) \) is the coefficient of the first fundamental quadratic form of the surface; and \( \Omega_i \) is the parametric domain of the surface of the \( i \)-th face of the solid.

In the subsequent formulas for the inertial characteristics of a solid, we omit the summation sign and the face indices, assuming that the summation is being carried out.

Let us assume \( F(r) = r \) in (7.9.1). Then from the divergence theorem we obtain

$$ \iint_S m \cdot r dS = \iiint_V \nabla \cdot r dV = 3 \iiint_V dV = 3V, $$

where \( \nabla \cdot r = \left[ \frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z} \right] \cdot \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \frac{\partial}{\partial x} x + \frac{\partial}{\partial y} y + \frac{\partial}{\partial z} z = 1 + 1 + 1 = 3. \) The volume is calculated by the formula

$$ V = \frac{1}{3} \iint_S m \cdot r dS = \frac{1}{3} \iint_{\Omega} m \cdot r \sqrt{g_{11} g_{22} - g_{12}^2} \, du dv. $$
The weight of the solid is obtained by multiplying the volume by the density of the solid $\rho$:

$$M = \rho V = \frac{\rho}{3} \iiint_{\Omega} m \cdot r \sqrt{g_{11} g_{22} - g_{12}^2} \, dudv.$$  

The coordinates of the center of mass of the solid—$x_c$, $y_c$, and $z_c$—are determined by dividing the relevant static moments by the solid weight:

$$x_c = \frac{1}{M} \iiint_{V} \rho x \, dV, \quad y_c = \frac{1}{M} \iiint_{V} \rho y \, dV, \quad z_c = \frac{1}{M} \iiint_{V} \rho z \, dV,$$

where $\rho$ is the density of the solid. To calculate the static moments of the solid, we assume sequentially $F(r) = xr$, $F(r) = yr$, and $F(r) = zr$ in (7.9.1). Then from the divergence theorem we obtain

$$\iint_{S} m \cdot (xr) \, dS = \iiint_{V} \nabla \cdot (xr) \, dV = 4 \iiint_{V} xdV,$$

$$\iint_{S} m \cdot (yr) \, dS = \iiint_{V} \nabla \cdot (yr) \, dV = 4 \iiint_{V} ydV,$$

$$\iint_{S} m \cdot (zr) \, dS = \iiint_{V} \nabla \cdot (zr) \, dV = 4 \iiint_{V} zdV,$$

where $\nabla \cdot (xr) = \begin{bmatrix} \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \end{bmatrix} \cdot \begin{bmatrix} xx \\ xy \\ xz \end{bmatrix} = \frac{\partial}{\partial x} x^2 + \frac{\partial}{\partial y} xy + \frac{\partial}{\partial z} xz = 2x + x + x = 4x,$

$$\nabla \cdot (yr) = \begin{bmatrix} \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \end{bmatrix} \cdot \begin{bmatrix} yx \\ yy \\ yz \end{bmatrix} = \frac{\partial}{\partial x} yx + \frac{\partial}{\partial y} y^2 + \frac{\partial}{\partial z} yz = y + 2y + y = 4y,$$

$$\nabla \cdot (zr) = \begin{bmatrix} \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \end{bmatrix} \cdot \begin{bmatrix} zx \\ zy \\ zz \end{bmatrix} = \frac{\partial}{\partial x} zx + \frac{\partial}{\partial y} zy + \frac{\partial}{\partial z} z^2 = z + z + 2z = 4z.$$

The coordinates of the solid’s center of mass are calculated by the formula

$$x_c = \frac{1}{4V} \iint_{S} m \cdot (xr) \, dS = \frac{1}{4V} \iiint_{\Omega} m \cdot (xr) \sqrt{g_{11} g_{22} - g_{12}^2} \, dudv,$$

$$y_c = \frac{1}{4V} \iint_{S} m \cdot (yr) \, dS = \frac{1}{4V} \iiint_{\Omega} m \cdot (yr) \sqrt{g_{11} g_{22} - g_{12}^2} \, dudv,$$
$$ z_c = \frac{1}{4V} \iint_S m \cdot (zr) dS = \frac{1}{4V} \iiint_\Omega m \cdot (zr) \sqrt{g_{11} g_{22} - g_{12}^2} dudv. $$

The solid's axial moments of inertia are determined by the formulas:

$$ J_{xx} = \iiint_V \rho (y^2 + z^2) dV, \quad J_{yy} = \iiint_V \rho (z^2 + x^2) dV, \quad J_{zz} = \iiint_V \rho (x^2 + y^2) dV. $$

The centrifugal moments of inertia of the solid are determined by the formulas:

$$ J_{xy} = J_{yx} = \iiint_V \rho xy dV, \quad J_{yz} = J_{zy} = \iiint_V \rho yz dV, \quad J_{zx} = J_{xz} = \iiint_V \rho xz dV. $$

Moments of inertia are introduced when a rigid solid rotation around a fixed point is considered. When the origin of the coordinate system is superposed with a fixed point, the velocity of a point of the solid is defined by the relation \( v = \omega \times r \), where \( \omega \) is the vector of the instantaneous angular velocity of the solid and \( r \) is the radius vector of a point of the solid. The vector of angular momentum of the solid is

$$ L = \iiint_V (r \times v) \rho dV = \iiint_V (r^2 \omega - (r \cdot \omega) r) \rho dV = J \cdot \omega, $$

where the term \( J \) is called an inertia tensor, and is defined by a matrix whose elements are the axial moments of inertia and centrifugal moments of inertia with the opposite sign:

$$ J = \begin{bmatrix}
J_{xx} & -J_{xy} & -J_{xz} \\
-J_{yx} & J_{yy} & -J_{yz} \\
-J_{zx} & -J_{zy} & J_{zz}
\end{bmatrix}. $$

To calculate the moment of inertia, let us assume \( F(r) = x^2 r \), \( F(r) = y^2 r \), \( F(r) = z^2 r \), \( F(r) = yz r \), \( F(r) = zx r \), and \( F(r) = xy r \) in (7.9.1). Then from the divergence theorem we obtain

$$ \iint_S m \cdot (x^2 r) dS = 5 \iiint_V x^2 dV, \quad \iint_S m \cdot (y^2 r) dS = 5 \iiint_V y^2 dV, $$
$$ \iint_S m \cdot (z^2 r) dS = 5 \iiint_V z^2 dV, $$
$$ \iint_S m \cdot (xy r) dS = 5 \iiint_V xy dV, \quad \iint_S m \cdot (yz r) dS = 5 \iiint_V yz dV, $$
$$ \iint_S m \cdot (zx r) dS = 5 \iiint_V zx dV. $$
The moments of inertia are calculated by the formulas

$$ J_{xx} = \frac{\rho}{5} \iint_S (y^2 + z^2) m \cdot r dS = \frac{\rho}{5} \iint_\Omega (y^2 + z^2) m \cdot r \sqrt{g_{11} g_{22} - g_{11}^2} dudv, $$

$$ J_{yy} = \frac{\rho}{5} \iint_S (z^2 + x^2) m \cdot r dS = \frac{\rho}{5} \iint_\Omega (z^2 + x^2) m \cdot r \sqrt{g_{11} g_{22} - g_{11}^2} dudv, $$

$$ J_{zz} = \frac{\rho}{5} \iint_S (x^2 + y^2) m \cdot r dS = \frac{\rho}{5} \iint_\Omega (x^2 + y^2) m \cdot r \sqrt{g_{11} g_{22} - g_{11}^2} dudv, $$

$$ J_{xy} = \frac{\rho}{5} \iint_S xy m \cdot r dS = \frac{\rho}{5} \iint_\Omega xy m \cdot r \sqrt{g_{11} g_{22} - g_{11}^2} dudv, $$

$$ J_{yz} = \frac{\rho}{5} \iint_S yz m \cdot r dS = \frac{\rho}{5} \iint_\Omega yz m \cdot r \sqrt{g_{11} g_{22} - g_{11}^2} dudv, $$

$$ J_{xz} = \frac{\rho}{5} \iint_S xz m \cdot r dS = \frac{\rho}{5} \iint_\Omega xz m \cdot r \sqrt{g_{11} g_{22} - g_{11}^2} dudv. $$

### 7.10. Calculation of Inertial Characteristics

In numerical integration over a surface, the domain of the face parameters is divided into small rectangular and triangular sub-domains. The calculation accuracy depends on the size of the sub-domains. As the control parameter of the integration domain partition, we use the angular deviation \( \Delta \alpha \). The size of each sub-domain is determined by the following condition: The angular deviation of the surface normal in the sub-domain must not exceed a predetermined value \( \Delta \alpha \). In the manner described above, we replace the two-dimensional parameter domain by a set quadrangles and triangles joining with each other.

Let us compute the definite integral

$$ I = \iint_D f(u,v) dudv \tag{7.10.1}$$

on the convex quadrangle region, using the Gaussian quadrature formulas. Suppose that the vertices of the quadrangle region are located at the points \( p_a = [u_a, v_a]^T \), \( p_b = [u_b, v_b]^T \), \( p_c = [u_c, v_c]^T \), and \( p_d = [u_d, v_d]^T \) on the plane of parameters (see Fig. 7.10.1).
Change the variables in the double integral (7.10.1). For an arbitrary convex quadrangle region we introduce the new parameters \( x \) and \( y \), related to parameters \( u \) and \( v \) by the relations

$$ u(x,y) = u_a \frac{1-x-y+xy}{4} + u_b \frac{1+x-y-xy}{4} + u_c \frac{1+x+y+xy}{4} + u_d \frac{1-x+y-xy}{4},$$

$$ v(x,y) = v_a \frac{1-x-y+xy}{4} + v_b \frac{1+x-y-xy}{4} + v_c \frac{1+x+y+xy}{4} + v_d \frac{1-x+y-xy}{4}. \tag{7.10.2}$$

Points \( p_a, p_b, p_c, \) and \( p_d \) correspond to parameters \( x_a=-1, y_a=-1; x_b=1, y_b=-1; x_c=1, y_c=1; \) and \( x_d=1, y_d=1 \). Functions (7.10.2) are continuous, have continuous first-order partial derivatives, and map the square with vertices \( x=\pm 1, y=\pm 1 \) onto the given quadrangle integration domain. This mapping is unambiguous and has a non-zero Jacobian

$$ J(x,y) = \begin{vmatrix}
\frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} \\
\frac{\partial v}{\partial x} & \frac{\partial v}{\partial y}
\end{vmatrix}.$$

Integration using Gaussian quadrature formulas is performed with respect to each parameter of the surface. After replacing the parameters, integral (7.10.1) can be calculated as a weighted sum of the values of the integrand in the domain of integration:

$$\iint_{\Omega} f(u,v)dudv = \sum_{i=1}^{m} \sum_{j=1}^{n} w_i z_j f(u(x_i, y_j), v(x_i, y_j)) J(x_i, y_j), \tag{7.10.3}$$

where \( x_1, x_2, \ldots, x_m \) are roots of the Legendre polynomial of degree \( m \), \( w_1, w_2, \ldots, w_m \) are the corresponding weighting factors, \( y_1, y_2, \ldots, y_n \) are roots of the Legendre polynomial of degree \( n \), and \( z_1, z_2, \ldots, z_n \) are the corresponding weighting factors. The roots \( x_i, i=1,\ldots,m \) of
the Legendre polynomial of degree \( m \) and their corresponding weighting factors are shown in Table 7.10.1.

| \( m \) | \( x_i \) | Weighting factors |
|-------|----------|------------------|
| 1     | 0        | 2                |
| 2     | ±0.57735026918962576450 | 1               |
|       | ±0.77459666924148337703 | 5/9             |
| 3     | 0        | 8/9              |
|       | ±0.33998104358485626480 | 0.65214515486254614262 |
|       | ±0.86113631159405257522 | 0.34785484513745385737 |
| 4     | 0        | 0.56888888888888888889 |
|       | ±0.53846931010568309103 | 0.47862867049936646804 |
|       | ±0.90617984593866399279 | 0.23692688505618908751 |
| 5     | 0        | 0.46791393457269104738 |
|       | ±0.23861918608319690863 | 0.36076157304813860756 |
|       | ±0.66120938646626451366 | 0.17132449237917034504 |
| 6     | 0        | 0.41795918367346938775 |
|       | ±0.40584515137739716690 | 0.38183005050511894495 |
|       | ±0.74153118559939443986 | 0.27970539148927666790 |
|       | ±0.94910791234275852452 | 0.12948496616886969327 |
| 7     | 0        | 0.36268378337836198296 |
|       | ±0.18343464249564980493 | 0.31370664587788728733 |
|       | ±0.52553240991632898581 | 0.22238103445337447054 |
|       | ±0.96028985649753623168 | 0.10122853629037625915 |

The roots of the Legendre polynomials and the weighting factors are determined from the condition that (7.10.3) is an exact equality if \( f(x,y)J(x,y)=p_{2m-1}(x)p_{2n-1}(y) \), where \( p_{2m-1}(x) \) and \( p_{2n-1}(y) \) are polynomials of degree \( 2m-1 \) and \( 2n-1 \), respectively.

Let us compute the definite integral

$$ I = \iint_A f(u,v)\,dudv \tag{7.10.4}$$

on the triangle domain of the parameters of the surface. Suppose the vertices of the triangle domain are located at the points \( p_a=[u_a\ v_a]^T \), \( p_b=[u_b\ v_b]^T \), and \( p_c=[u_c\ v_c]^T \) on the parametric plane (see Fig. 7.10.2). For triangular domains, it is convenient to use three barycentric coordinates, \( a \), \( b \), and \( c \), computed at points \( p_a \), \( p_b \), and \( p_c \), instead of coordinates \( u \) and \( v \).
The coordinates of an arbitrary point \( p = [u \ v]^T \) are represented by barycentric coordinates \( a, b, \) and \( c, \) using the formulas

$$ u = au_a + bu_b + cu_c; \quad v = av_a + bv_b + cv_c. \tag{7.10.5}$$

The barycentric coordinates satisfy the equation: \( a + b + c = 1. \) The integrable function \( f(u,v) \) is represented as a function of the barycentric coordinates \( f(a,b,c) = f(u(a,b,c),v(a,b,c)). \) Only two of three barycentric coordinates are independent. Without loss of generality, we choose the first two barycentric coordinates as independent variables. Use the equalities (7.10.5) in the form

$$ u = a(u_a - u_c) + b(u_b - u_c) + u_c, \quad v = a(v_a - v_c) + b(v_b - v_c) + v_c $$

to rewrite integral (7.10.4) as

$$\iint_{\Delta} f(u,v) \, du \, dv = \iint_{\Delta} f(u(a,b,c),v(a,b,c)) J(a,b,c) \, da \, db =$$

$$\int_0^1 \left( \int_0^{1-a} f(u(a,b),v(a,b)) J(a,b) \, db \right) da,$$

where \( J(a,b) = \begin{vmatrix} \frac{\partial u}{\partial a} & \frac{\partial u}{\partial b} \\ \frac{\partial v}{\partial a} & \frac{\partial v}{\partial b} \end{vmatrix} \) is the Jacobian of the coordinate transformation.

With the transition to barycentric coordinates, and replacing the parameters, integral (7.10.4) can be calculated as a weighted sum of the values of the integrand in the domain of integration:

$$\iint_{\Delta} f(u,v) \, du \, dv = \sum_{i=1}^m w_i f(u(a_i,b_i,c_i),v(a_i,b_i,c_i)),$$  

$$(7.10.6)$$
where \( S = 0.5J(a,b) \) is the area of the triangle \( p_a p_b p_c \). The barycentric coordinates \( a_i, b_i, c_i, i=1,\ldots,m \) and weighting factors for cubature formulas for the triangular region are given in Table 7.10.2.

| \( m \) | \( a_i \) | \( b_i \) | \( c_i \) | Weighting factors |
|-------|--------|--------|--------|-----------------|
| 1     | 1/3    | 1/3    | 1/3    | 1               |
| 3     | 2/3    | 1/6    | 1/6    | 1/3             |
|       | 1/6    | 2/3    | 1/6    | 1/3             |
|       | 1/6    | 1/6    | 2/3    | 1/3             |
| 4     | 1/3    | 1/3    | 1/3    | -0.5625         |
|       | \( a \) | \( b \) | \( b \) | 0.5208333333333333 |
|       | \( b \) | \( a \) | \( b \) | 0.5208333333333333 |
|       | \( b \) | \( b \) | \( a \) | 0.5208333333333333 |
| where \( a = 0.6 \) | \( b = 0.2 \) |

The barycentric coordinates \( a_i, b_i, c_i \), and weighting factors \( w_i \) for cubature formulas for a triangular region defined by the condition that (7.10.6) is an exact equality if

$$ f(u(a,b,c),v(a,b,c)) = (A_m a^m + B_m b^m + C_m c^m)$$

is a polynomial of degree \( m \).

### 7.11. Principal Moments of Inertia

In a parallel translation of the origin of the Cartesian coordinate system, the inertia tensor of the solid and its components changes. Let the origin of the Cartesian coordinate system be translated to the center of mass of a solid, \( c \), having in the original system the coordinates \( x_c, y_c, \) and \( z_c \). The coordinate system with the origin at the center of mass of the object is called the **central coordinate system** for this object.
In the central coordinate system, the radius vector of a point of the solid is \( r = r - c \), and the components of the inertia tensor are

$$ J_{xx} = \iiint (y^2 + z^2 - 2yy_c - 2zz_c + y_c^2 + z_c^2) \rho dV = J_{xx} - (y_c^2 + z_c^2)M,$$

$$ J_{yy} = \iiint (z^2 + x^2 - 2zz_c - 2xx_c + z_c^2 + x_c^2) \rho dV = J_{yy} - (z_c^2 + x_c^2)M,$$

$$ J_{zz} = \iiint (x^2 + y^2 - 2xx_c - 2yy_c + x_c^2 + y_c^2) \rho dV = J_{zz} - (x_c^2 + y_c^2)M,$$

$$ J_{yz} = \iiint (yz - yz_c - zy_c + y_c z_c) \rho dV = J_{yz} - y_c z_c M,$$

$$ J_{zx} = \iiint (zx - zx_c - xz_c + z_c x_c) \rho dV = J_{zx} - z_c x_c M,$$

$$ J_{xy} = \iiint (xy - xy_c - yx_c + x_c y_c) \rho dV = J_{xy} - x_c y_c M.$$

The moments of inertia in the central coordinate system are called the **central moments of inertia**.

In the formula \( L = J \omega \), the momentum vector \( L \) generally does not coincide with the direction of the angular velocity vector \( \omega \). As a result, during rotation of the solid about a predetermined axis, reactions arise at points of attachment of the solid; these reactions depend on the absolute value of the angular velocity. This rotation is dynamically unstable.

Let us find such directions for the given inertia tensor \( J \) for which the direction of the momentum vector \( L \) coincides with the direction of the angular velocity vector \( \omega \). Let this direction be determined by the unit vector \( e = [x \ y \ z]^T \); then the vector \( Je \) will be proportional to the vector \( e \):

$$ Je - \lambda e = 0,$$

where \( \lambda \) is an as-yet-unknown scalar. Projecting this equation onto the coordinate axes, we obtain three equations:

$$(J_{xx} - \lambda)x - J_{xy}y - J_{xz}z = 0,$$

$$-J_{yx}x + (J_{yy} - \lambda)y - J_{yz}z = 0,$$

$$-J_{zx}x - J_{zy}y + (J_{zz} - \lambda)z = 0,$$

which can be considered as a homogeneous system of linear algebraic equations \( x, y, \) and \( z \). A trivial solution does not suit us because we want to find a vector for which

$$
x^2 + y^2 + z^2 = 1.$$

System (7.11.1) has non-trivial solutions when the determinant of the system is zero:
This equality holds when scalar $\lambda$ satisfies

$$\lambda^3 - I_1 \lambda^2 + I_2 \lambda - I_3 = 0,$$

where $I_1 = J_{xx} + J_{yy} + J_{zz}$,

$$I_2 = \begin{vmatrix} J_{xx} & -J_{xy} \\ -J_{yx} & J_{yy} \end{vmatrix} + \begin{vmatrix} J_{yy} & -J_{yz} \\ -J_{zy} & J_{zz} \end{vmatrix} + \begin{vmatrix} J_{zz} & -J_{zx} \\ -J_{xz} & J_{xx} \end{vmatrix}, \quad I_3 = \begin{vmatrix} J_{xx} & -J_{xy} & -J_{xz} \\ -J_{yx} & J_{yy} & -J_{yz} \\ -J_{zx} & -J_{zy} & J_{zz} \end{vmatrix}.$$  

Equation (7.11.3) is called the characteristic equation of the inertia tensor. Roots $\lambda_1$, $\lambda_2$, and $\lambda_3$ of the characteristic equation are real-valued, since the matrix of the inertia tensor is symmetric. Scalars $\lambda_1$, $\lambda_2$, and $\lambda_3$ are eigenvalues of the moments of inertia matrix. Each $\lambda_i$, $i=1,2,3$, corresponds to an eigenvector $e_i$.

Let us assume that the eigenvalues of the inertia matrix, $\lambda_1$ and $\lambda_2$, are different. Then the corresponding eigenvectors, $e_1$ and $e_2$, are orthogonal. Indeed, for the given eigenvalues, the following equalities are satisfied:

$$J \cdot e_1 - \lambda_1 e_1 = 0, \quad J \cdot e_2 - \lambda_2 e_2 = 0.$$

Compute the inner product of the first equation with $e_2$, and the second with $e_1$, and subtract the second from the first. Using the symmetry of the inertia tensor, we obtain

$$(\lambda_2 - \lambda_1) e_1 \cdot e_2 = 0.$$  

The last equality, and the assumption $\lambda_2 \neq \lambda_1$, imply that eigenvectors $e_1$ and $e_2$ are orthogonal. Similarly, we can prove the orthogonality of other eigenvectors. The eigenvector determines the principal direction of the inertia tensor in the space. If two of the three eigenvalues of the matrix of inertia are equal, then we can define only one of the principal directions, and other principal directions can be any directions orthogonal to the determined direction. If all three eigenvalues of the matrix of inertia are equal, then the principal directions can be any directions in space. In any case, we can obtain three mutually orthogonal principal directions.

Three mutually orthogonal principal directions corresponding to eigenvectors $e_1$, $e_2$, and $e_3$ define the principal axes of inertia of the solid, and are the basis vectors of the main coordinate system. If the unit vectors of the new Cartesian coordinate system are oriented along the principal directions, then the axial moments of inertia are equal to the eigenvalues of the matrix of inertia, and the centrifugal moments of inertia are equal to zero; i.e., $J_{11} = \lambda_1$, $J_{22} = \lambda_2$, $J_{33} = \lambda_3$, $J_{12} = 0$, $J_{23} = 0$, and $J_{13} = 0$. Indeed, equalities $Je_i = \lambda_i e_i$, $i=1,2,3$, are satisfied for the principal directions. Then $e_k \cdot Je_i = \lambda_i \delta_{ik}$, which
proves the initial assertion made. The matrix of the inertia tensor in the main coordinate system has the form

$$
J = \begin{bmatrix}
\lambda_1 & 0 & 0 \\
0 & \lambda_2 & 0 \\
0 & 0 & \lambda_3
\end{bmatrix} = \begin{bmatrix}
J_{11} & 0 & 0 \\
0 & J_{22} & 0 \\
0 & 0 & J_{33}
\end{bmatrix}.$$

The coordinate system in which all the centrifugal moments of inertia of the solid are zero is called the principal coordinate system. The moments of inertia, \(J_{11}, J_{22},\) and \(J_{33}\), in the main coordinate system are called principal moments of inertia. The principal directions of the inertia tensor depend on the fixed point of the solid (that is, on the choice of the origin of the coordinate system). The central coordinate system in which all centrifugal moments of inertia of the solid are zero is called the principal central coordinate system. The moments of inertia in the principal central coordinate system are called principal central moments of inertia. The directions of the principal axes of inertia of the solid lie in the planes of symmetry. The origin of the principal central coordinate system is located in the center of mass of the solid.

Let us find the principal axes of inertia. Let the principal moment of inertia \(\lambda_i\) correspond to the principal direction defined by the unit vector \(e_i = [x_i, y_i, z_i]^T\). There are three possible cases of relations between the roots of the characteristic equation. The first case is when all the roots of the characteristic equation are distinct; the second case is when two of the three roots of the characteristic equation are equal and different from the third root; and the third case is when all three roots of the characteristic equation are equal.

If all the roots of the characteristic equation are different (\(\lambda_1 \neq \lambda_2 \neq \lambda_3\)), then for each \(\lambda_i\) form the system of equations (7.11.1):

$$(J_{11} - \lambda_i)x_i + J_{12}y_i + J_{13}z_i = 0,$$
$$
J_{12}x_i + (J_{22} - \lambda_i)y_i + J_{23}z_i = 0,$$
$$
J_{13}x_i + J_{23}y_i + (J_{33} - \lambda_i)z_i = 0.$$

Among these three equations one is a linear combination of the other two, since the determinant of system (7.11.2) is equal to zero. We need to figure out which two of the three equations are linearly independent. For this, we compute the determinants

$$
A_1 = \begin{vmatrix}
J_{22} - \lambda_i & J_{23} \\
J_{23} & J_{33} - \lambda_i
\end{vmatrix},$$
$$
A_2 = \begin{vmatrix}
J_{33} - \lambda_i & J_{13} \\
J_{13} & J_{11} - \lambda_i
\end{vmatrix},$$
$$
A_3 = \begin{vmatrix}
J_{11} - \lambda_i & J_{12} \\
J_{12} & J_{22} - \lambda_i
\end{vmatrix}.$$

At least one of them must be non-zero. Let \(A_2 \neq 0\). Then the components of the corresponding principal vector are found from the system of equations

$$(J_{11} - \lambda_i)x_i + J_{12}y_i + J_{13}z_i = 0,$$
$$
J_{13}x_i + J_{23}y_i + (J_{33} - \lambda_i)z_i = 0,$$
$$
x_i^2 + y_i^2 + z_i^2 = 1.$$
Having solved these three equations, we determine the eigenvectors \( e_i = [x_i, y_i, z_i]^T \) for each eigenvalue \( \lambda_i, i=1,2,3 \).

If two of the three roots of the characteristic equation are equal—for example, \( \lambda_1 = \lambda_2 \neq \lambda_3 \)—then the basis vector \( e_3 = [x_3, y_3, z_3]^T \) can be found as described above. The other two basis vectors can be any unit vectors that are mutually orthogonal, and orthogonal to vector \( e_3 \).

If \( \lambda_1 = \lambda_2 = \lambda_3 \), the eigenvectors can be any three mutually orthogonal unit vectors, and \( \lambda_i = I_1/3 \).

To determine the eigenvalues of the matrix of inertia, we must solve cubic equation (7.11.3). Replace the unknown \( \lambda \) in equation (7.11.3) by the new unknown \( \chi \), related to \( \lambda \) by the equality \( \lambda = \chi + I_1/3 \). We obtain an incomplete cubic equation for \( \chi \) that does not contain any factor with the square of the new unknown:

$$\chi^3 + p \chi + q = 0,$$

where

$$
p = -\frac{1}{3}I_1^2 + I_2,$$

$$
q = -\frac{2}{27}I_1^3 + \frac{1}{3}I_1I_2 - I_3.$$

A solution of incomplete cubic equation (7.11.4) can be found using the Cardano formula:

$$\chi_i = \sqrt[3]{-\frac{q}{2} + \sqrt{\left(\frac{q}{2}\right)^2 + \left(\frac{p}{3}\right)^3}} + \sqrt[3]{-\frac{q}{2} - \sqrt{\left(\frac{q}{2}\right)^2 + \left(\frac{p}{3}\right)^3}}.$$

In the Cardano formula, the cubic radicals are summed,

$$\gamma_1 = \sqrt[3]{-\frac{q}{2} + \sqrt{\left(\frac{q}{2}\right)^2 + \left(\frac{p}{3}\right)^3}}, \quad \gamma_2 = \sqrt[3]{-\frac{q}{2} - \sqrt{\left(\frac{q}{2}\right)^2 + \left(\frac{p}{3}\right)^3}},$$

satisfying the condition \( \gamma_1\gamma_2 = -p/3 \). Thus, the roots of the incomplete cubic equation (7.11.4) are

$$\chi_1 = \gamma_1 + \gamma_2, \quad \chi_2 = \varepsilon\gamma_1 + \varepsilon^2\gamma_2, \quad \chi_3 = \varepsilon^2\gamma_1 + \varepsilon\gamma_2,$$

where \( \varepsilon = -1/2 + i\sqrt{3}/2 \) is cube root of unity and \( \varepsilon^2 = -1/2 - i\sqrt{3}/2 \) is the square of this cube root of unity.

The Cardano formula allows finding three roots, which are complex in general, of the cubic equation (7.11.4). The coefficients of the cubic equation may generally be complex. For calculating the principal moments of inertia, coefficients (7.11.5) and
(7.11.6) of the incomplete cubic equation, as well as invariants $I_1$, $I_2$, and $I_3$, are real numbers. In the Cardano formula, the term

$$D = -4p^3 - 27q^2$$

is called the **discriminant** of the incomplete cubic equation (7.11.4). If coefficients $p$ and $q$ are real numbers, then the discriminant is also a real number, and can take values: $D<0$, $D=0$, or $D>0$.

If $D<0$, then the numbers under each of the cubic radical signs in the Cardano formulas are real. The cube root of a real number has one real and two complex conjugate values. Let the real values of these cubic radicals be $\gamma_1$ and $\gamma_2$; then the cubic equation with real coefficients has one real root and two complex conjugate roots:

$$\chi_1 = \gamma_1 + \gamma_2, \quad \chi_2 = \frac{\gamma_1 + \gamma_2}{2} + i\sqrt{3} \frac{\gamma_1 - \gamma_2}{2}, \quad \chi_3 = \frac{\gamma_1 + \gamma_2}{2} - i\sqrt{3} \frac{\gamma_1 - \gamma_2}{2}.$$  

If $D=0$, then $\gamma_1 = \gamma_2 = \sqrt[3]{-q/2}$, $\varepsilon + \varepsilon^2 = -1$, and the cubic equation with real coefficients has three real roots, two of which are identical, and the third is the sum of the first two, with the opposite sign:

$$\chi_1 = 2\sqrt[3]{-q/2}, \quad \chi_2 = -\sqrt[3]{-q/2}, \quad \chi_3 = -\sqrt[3]{-q/2}.$$  

If $D>0$, then the numbers under the signs of the cubic radicals in the Cardano formula are complex conjugate, cube roots of which are complex numbers in general. Among the roots of a cubic equation with real coefficients, one must be a real number; hence, $\gamma_1$ and $\gamma_2$ are complex conjugate numbers:

$$\gamma_1 = -r (\cos(\gamma/3) + i\sin(\gamma/3)), \quad \gamma_2 = -r (\cos(\gamma/3) - i\sin(\gamma/3)),$$

where $r = \frac{q}{|q|} \sqrt{\frac{|p|}{3}}$ (the sign of $r$ must coincide with the sign of $q$), and

$$\gamma = \arccos\left(\frac{q}{2r^3}\right).$$

Thus, if $D>0$, then the cubic equation with real coefficients has three real roots

$$\chi_1 = -2r \cos(\gamma/3),$$

$$\chi_2 = r (\cos(\gamma/3) + \sqrt{3} \sin(\gamma/3)) = 2r \cos(\pi/3 - \gamma/3),$$

$$\chi_3 = r (\cos(\gamma/3) - \sqrt{3} \sin(\gamma/3)) = 2r \cos(\pi/3 + \gamma/3).$$

All the roots, $\lambda_1$, $\lambda_2$, and $\lambda_3$, of the characteristic cubic equation (7.11.3) are real numbers, and are defined by the formula
$$\lambda_1 = \frac{I_1}{3} - 2r \cos(\gamma/3), \quad \lambda_2 = \frac{I_1}{3} + 2r \cos(\pi/3 - \gamma/3), \quad \lambda_3 = \frac{I_1}{3} + 2r \cos(\pi/3 + \gamma/3),$$

where

$$
p = -\frac{1}{3} I_1^2 + I_2, \quad q = -\frac{2}{27} I_1^3 + \frac{1}{3} I_1 I_2 - I_3, \quad r = \frac{q}{|q|} \sqrt{\frac{|p|}{3}},$$

$$\gamma = \arccos\left(\frac{q}{2r^3}\right).$$

Possible special cases: if \( p = 0 \), then \( \lambda_1 = \lambda_2 = \lambda_3 = \frac{I_1}{3} \), if \( D = 0 \), then

$$\lambda_1 = \frac{I_1}{3} - 2\sqrt[3]{\frac{q}{2}}, \quad \lambda_2 = \lambda_3 = \frac{I_1}{3} + \sqrt[3]{\frac{q}{2}}.$$

**Exercises**

1. Where are geometric models used?
2. Describe an algorithm for constructing a vector image of a solid.
3. Describe an algorithm for constructing a raster image of a solid.
4. Compare different triangulation algorithms.