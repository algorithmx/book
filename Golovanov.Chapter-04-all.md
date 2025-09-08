GEOMETRIC MODEL

The main part of a geometric model is the description of the shape of the modeled object. In general, it is impossible to describe the shape of an object by a single surface; but it can be done with the help of a set of surfaces joined in a certain way. To describe the geometric shape of the modeled object, we use a boundary representation; this means construction of the bounding surfaces separating the modeled object from the rest of the space. We describe the boundary surface of the simulated object using shells. In this chapter we consider principles of description of the shape of the modeled object. For this purpose we use shells, faces, edges, vertices, and their data structures.

4.1. Shells

The geometric shape of a simulated object is described by a set of joined surfaces. Fig. 4.1.1 (on the left) shows several planes, cylindrical surfaces, and torus surfaces trimmed in a certain way. Curves are constructed along the edges of the surfaces. Fig. 4.1.1 (on the right) shows the same surfaces joined to each other. The surfaces are along along the curves. Using the surfaces shown in Fig. 4.1.1 we can describe the surface of the modeled object. This description is the main part of the geometric model.

Fig. 4.1.1.

To describe the geometric shape, we use shells, constructed from objects such as faces, edges, vertices, and loops.
A finite surface associated with the direction of a normal is called a face. The direction of the normal to the face is indicated by a special attribute. We say that the face is based on the surface and has the direction of its normal as an attribute. The attribute is positive if the normals to the face and the surface coincide; otherwise the attribute is negative.

The side of the face, when viewing from the direction toward the normal to the face, is referred to as the outer side; the other side of the face is referred to as the inner side.

We denote the face the same as we denote the surface. Sides of the surface are not equivalent with respect to its normal, since one side of the surface is always the outer side, and the other side is always the inner side. Unlike the surface, the direction of the normal to the face may be associated with either of its two sides.

Let the parameters of a face belong to a two-dimensional connected region $\Omega$. The boundaries of the face are mappings of a two-dimensional boundary of region $\Omega$ onto three-dimensional space. If the face has internal notches, it has one outer boundary and several inner boundaries. Every boundary of the face is closed. Let us divide every boundary into sections and choose parameters on them; i.e., we represent sections of the boundaries by curves which will be referred to as boundary curves.

We call a curve that has a direction an edge. The direction of an edge is indicated by a special attribute. We say that the edge is based on the curve and has direction as an attribute. The attribute is positive if the edge coincides with the curve, and negative if the edge is directed opposite to the curve. Unlike the curve, the edge can be directed as desired.

We use edges constructed on boundary curves of faces. An edge can be joined to another edge along a boundary curve. In this case the edge will be constructed on the curve of intersection of the adjacent faces. Faces having a common edge are called adjacent faces. The edge of the joining faces is described by an intersection curve (3.7.1).

In a face that is cyclic closed with respect to one or both parameters, there are segments of the boundary along which the face is joined with itself. The segment of the boundary and the edge constructed on it, along which the face is joined with itself, is referred to as a juncture.

An edge constructed on a free edge of the face is described by a surface curve (3.6.1), and is referred to as a boundary edge.

A section of a face boundary at a singular point may be a point, even if it corresponds to some curve in the parametric domain. An edge constructed on such a boundary segment is called a pole edge, and the corresponding three-dimensional point is a pole.

If the edge starts and ends at the same point it is called closed.

We call the point at which edges are joined a vertex. Vertices can be located only at ends of edges. Any finite number of edges can be joined at a vertex.

We call a sequence of edges spanning some boundary of a face a loop of the face. A loop, as a face boundary, is always closed. We direct the loop in such a way that the face is always located on the left if we are moving along the loop on the outer side of the face. The direction of the face edge may or may not coincide with the direction of the loop. The attribute characterizing coincidence of edge direction with loop direction is referred to as a flag. We assign a positive flag to an edge whose direction coincides with the direction of a loop, and a negative flag to an edge whose direction does not
coincide with the direction of a loop. Thus, a loop consists of a list of edges in the order of their sequence and a list of their corresponding flags.

We call a connected surface formed by a finite set of faces joined along common edges a shell. In geometric modeling, shells are used to describe the boundary surface separating a modeled object from the rest of a space. A shell may describe the whole boundary surface of a modeled object or just some part of it. A shell describing only a part of a boundary surface has borders. A shell is called closed if it has no borders. Otherwise it is called open.

4.2. Properties of Shells

Properties of shells independent of quantitative characteristics (lengths and angles) reflect a continuous connection among the points of the shells. These properties are referred to as topological.

The Euler characteristic of a shell links the number of its faces, edges, vertices, and loops. A shell contains $F$ faces, $E$ edges, $V$ vertices, and $L$ loops. The number of vertices, edges, faces, and loops of a shell are related by

$$F - E + V + (F - L) = H,$$

(4.2.1)

where $H$ is called the Euler characteristic of the shell. Formula (4.2.1) is called the Euler formula. If every face of a shell has one loop, then $F - L = 0$, and the term in parentheses on the left-hand side of (4.2.1) can be omitted.

The Euler characteristic is independent of the quantitative characteristics (length, area, volume and angles) of a shell, as well as of the decomposition of the shell by faces, edges, and vertices. This can be seen from Fig. 4.2.1, which shows various ways of decomposing part of a shell by faces, edges, and vertices.

![Fig. 4.2.1.](image)

The Euler characteristic depends on the properties of the shell studied in topology. Using the Euler characteristic, one can estimate the possibility of establishing a one-to-one correspondence between shells. Consider two shells: a shell in the form of quadrangular prism, and a shell in the form of quadrangular prism with a square hole in the middle (Fig. 4.2.2).
The Euler characteristic of the first shell is equal to two. The Euler characteristic of the second shell is equal to zero. The second shell is not equivalent to the first shell; therefore the shells have different Euler characteristics.

Let us investigate the topological properties of a shell preserved in through different deformations. Let us assume that the shell is made of some supple material. We call the shape modification of a shell by stretching, compression, shear, or bending its surface that does not lead to tearing and does not require gluing of surfaces, a deformation. We say that two shells have the same topology if by deforming one shell we can obtain the other. By deforming the first shell shown in Fig. 4.2.2, we can obtain a sphere, while by deforming the second shell, we can obtain a torus (see Fig. 4.2.3). It is impossible to obtain a torus by any deformation of a sphere, since they have different topology.

A shell having the topology of a circle is called trivial. A trivial shell is open, has a single boundary, and can be represented by a single face. Let us answer the question: What is the minimum number of curves along which a shell can be cut into two trivial shells that can be drawn on the surface of the shell?

The connectivity of a shell is defined by the minimum number of curves along which the shell can be cut into two trivial shells. The curves must be closed or must begin and end at the boundaries of the shell. Let us denote the connectivity by $h$. If the shell connectivity is equal to $h$, then $h-1$ cuts are sufficient to turn the shell into a trivial one. A shell of connectivity $h$ can be split into two separate parts using $h$ cuts.

A trivial shell can be split into two separate parts by any curve drawn from one point of the boundary to another point not coincident with the first point. A trivial shell is called a simply connected shell.

Fig. 4.2.4 shows open shells having finite numbers of boundaries, which can be made flat by deformation.
If a flat shell has $L$ boundaries, we can draw $L-1$ curves on it and not cut the shell into two separate parts—for example, curves from the outer boundary to each inner boundary. Any subsequent curve starting and ending at the boundary of the shell cuts it into two parts. A flat shell with $L$ boundaries has connectivity equal to $L$.

A shell having the topology of a sphere can be cut into two separate parts that are simply connected shells along a closed curve on its surface. For a shell with torus topology, we need at least two closed curves on it to cut it into a simply connected shell. This method of cutting a torus surface is shown in Fig. 4.2.5. Using the definition, we find that the connectivity of a sphere is unity and connectivity of a torus is three. A cylindrical shell of finite length has connectivity equal to two. A method of cutting a cylindrical shell of finite length into a simply-connected shell is shown in Fig. 4.2.6.

Fig. 4.2.7 shows open shells obtained from closed shells.

If a hole with a single closed boundary is cut out of a closed shell of connectivity $h$, then the connectivity of the resulting open shell is equal to the connectivity of the initial closed shell. Every subsequent hole with a single closed boundary increases the
connectivity of the resulting shell by one. The connectivity of the open shells shown in Fig. 4.2.7 is respectively equal to: one, four, three, six. The series of cuts on these shells is constructed in a way similar to the corresponding series of cuts on a closed shell, but some of the curves are drawn from one boundary to the other boundary.

The **orientability** of a shell characterizes its property of having two sides. Shells having two sides are called **two-sided** or **orientable**. Shells having a single side are called **one-sided** or **non-orientable**.

An example of a one-sided shell is the Möbius strip; see Fig. 4.2.8. A Möbius strip can be obtained from a paper strip if its ends are rotated relative to each other at one hundred eighty degrees and then glued. Before the ends of the strip are glued, its sides can be painted in two different colors. If the painting is done after the ends are glued, it turns out that we paint the whole strip in one color.

An example of a closed shell is a one-sided Klein bottle. A Klein bottle has a single closed self-intersecting curve. Fig. 4.2.9 shows a semi-transparent Klein bottle.

![Fig. 4.2.8.](image1)

![Fig. 4.2.9.](image2)

A Klein bottle cannot serve as a vessel. The series of lines cutting the Klein bottle into two simply connected parts is similar to the series of lines of the torus. The connectivity of the Klein bottle is equal to three. If a Klein bottle is cut by its plane of symmetry, we obtain two non-closed self-intersecting shells, from which we can obtain two Möbius strips by deformation. Another example of a one-sided shell is a heptahedron.

One-sided shells are referred to as non-orientable because for such shells we can provide an orientation of traversal direction in the vicinity of some point and move along the shell until eventually we return to the initial point—but with the opposite direction of traversal.

**Topological type** characterizes a shell, like connectivity. Closed shells have odd connectivity. For such shells, the Euler characteristic $H$ is related to its connectivity $h$ by

$$H = 3 - h.$$

For closed orientable shells, the Euler formula can be expressed in the form

$$F - E + V + (F - L) = 3 - h.$$

From deforming a torus we can obtain a dumbbell-shaped shell, which we call a sphere with a handle. In general, any closed shell can be shaped by deformation into a
sphere with $G$ handles. For instance, if we take a thick plate, punch $G$ holes in it and round all the edges, we obtain an object the shell of which has the topology of a sphere with $G$ handles. Parameter $G$ (genus) characterizes the topological type of a shell. Fig. 4.2.10 shows a sphere with four handles.

![Fig. 4.2.10.](image)

The characteristic of the topology of the shell more demonstrative than its connectivity is the number of handles $G$ of the sphere that can be the result of deformation of a closed shell. On a shell with topology of a sphere with $G$ handles can be drawn $2G$ closed curves by which it can be cut into a trivial shell. Any subsequent closed curve cuts the shell into two trivial shells. Thus, a sphere with $G$ handles has connectivity $h=2G+1$. Inserting the value of connectivity expressed by $G$ into (4.2.1) yields the formula for calculation of the number of faces $F$, edges $E$, vertices $V$, and loops $L$ with characteristic value $G$

$$F - E + V + (F - L) = 2(1 - G).$$

This formula is called the Euler-Poincare formula. The Euler-Poincare formula allows determination of the topological type of the shell if the number of faces, edges, vertices, and loops are known.

### 4.3. Manifold Shells

In general, a shell can intersect itself; have an edge or not; and extend to infinity. Among the many different shells, we select shells reflecting the geometric properties of real objects.

A shell satisfying the following five requirements is referred to as a manifold shell:

1. The shell is finite.
2. The shell does not intersect itself.
3. The shell is two-sided.
4. At any edge of the shell no more than two faces are joined, and in such a way that the outer side of one face transits to the outer side of the other face.
5. When traversing any vertex of the surface shell it is necessary to pass through all the faces adjacent to the vertex and to cross all edges coming out of it.
Since the outer side of each face transits into the outer side of the adjacent face, a manifold shell also has **outer** and **inner** sides.

In a manifold shell, an edge separating two faces is included in two loops. In the loop of one face, the edge is included with positive flag; in the loop of the other face it is included with negative flag. If the edge is located along the boundary of an open shell then the edge is included in only one loop.

In geometric modeling, manifold shells are generally used, since with the help of these shells we can easily and fully describe the geometric shape of modeled objects.

Non-manifold shells include: shells extended to infinity; self-intersecting shells; and one-sided shells.

![Fig. 4.3.1.](image1)

![Fig. 4.3.2.](image2)

A non-manifold shell is a shell at the edge of which more than two faces are joined, as edge $ED$ in Fig. 4.3.1. A non-manifold shell is a shell whose vertex can be circumnavigated without visiting all faces adjacent to the vertex, as vertex $V$ in Fig. 4.3.2.

### 4.4. Solids in Geometric Modeling

A closed manifold shell divides a three-dimensional space into two parts, one of which is finite. Let us call a closed manifold shell an **outer shell**, if its outer side is directed outward from the finite part of the space. Let us call a closed manifold shell an **inner shell**, if its outer side is directed into the finite part of the space.

In geometric modeling, a connected set of points located on the inner side of one outer and several inner shells, which are located inside the outer shell, together with the points of these shells, is called a **solid**.

A solid is described by the set of its shells. In most cases, a solid is described by one outer shell. The inner shells of a solid are its internal voids. Solids are among the basic elements of geometric modeling, but they are not the only ones. Open and non-manifold shells are as important as solids in reflecting geometrical properties of modeled objects.

With the help of solids, we can describe a boundary surface of a modeled object—i.e., its geometric shape. Solids constitute the bulk of a geometric model. Besides
solids, a geometric model may contain other components. The other components of a model are designed to allow the model to be edited. If model editing is not required, the model may consist only of solids; all other components of the model are not required.

4.5. Data Structures

A geometric model in boundary representation consists of solids, in the simplest case. Each solid consists of a set of shells. Each shell is a set of faces constructed on curves and surfaces, which in turn are described by points, vectors, integers, and symbolic expressions. Ultimately, a geometric model is a sequence of numbers arranged in a certain way into predetermined data structures.

Data structures represent the composition of the objects described by them. Here is one possible configuration of the data structures of faces, edges, vertices, shells, and solids. This configuration allows traversing from any edge or face to any other element of the shell and getting all the information about it.

The data structure of a vertex contains a point.

The data structure of an edge contains a curve and the attribute of direction coincidence of the edge with this curve. In addition, for convenience, an edge contains information about its initial and final vertex, and about which face is on the left and which is on the right from the edge, when viewed from the outer side of edges along the direction of the edge. Fig. 4.5.1 shows the data structure of an edge starting at vertex A and ending at vertex B.

![Diagram](image)

Fig. 4.5.1.

The data structure of an oriented edge contains the edge and the flag of the direction of motion along the edge. Oriented edges are introduced for the convenience of description of face loops.

The data structure of a face loop contains oriented edges in the order they appear; that is, it contains the edges in the order they appear and their corresponding flags of coincidence of the directions of edges with the direction of the loop.

The data structure of a face contains the surface, the attribute of the direction of the face normal with the direction of a normal to the surface, and the set of loops of the face. Loops of the face inherit properties of the boundary of the surface domain. The number of loops of a face is equal to the number of boundaries of the face surface. One of the boundaries of the face is the outer boundary, and contains the boundaries of
internal cutouts within it. The loop of the face enclosing the remaining loops is called the outer loop, and the rest are inner loops. The outer loop of a face is oriented counterclockwise, and inner loops are oriented clockwise, when looking toward the normal to the face. Loops of one face cannot intersect each other or themselves. In Fig. 4.5.2, arrows indicate the direction of the outer and two inner loops of the face.

Fig. 4.5.2.

Thus, the face contains information about all the vertices and edges joining it to other faces. From the edges we can get information about the adjacent faces—or about their absence. This data structure of edges and faces establishes bidirectional connections between them. Finding ourselves on one of the objects, we can traverse the whole shell and get information about all its objects.

The data structure of a shell contains its constituent faces and its attribute of closedness.

The data structure of a solid contains its constituent shells, and may also contain the sequence and methods of construction of these shells.

Let us illustrate the general principles of description of a geometric shape of modeled objects by the example of the elementary solids.

4.6. Elementary Solids

The elementary solids are a prism, a cylinder, a cone, a sphere, and a torus. Elementary solids are composed of a single shell. For each elementary solid, choose the local rectangular Cartesian coordinate system with radius-vector of the origin denoted as $p$ and basis vectors denoted by $i_x, i_y,$ and $i_z$.

A rectangular prism is composed of six faces. Let us place the origin of a local Cartesian coordinate system at one of the vertices of the prism and direct its basis vectors along the edges joined at this vertex, as in Fig. 4.6.1. Let the solid have length $x$ in the direction of basis vector $i_x$, length $y$ in the direction of basis vector $i_y$, and length $z$ in the direction of basis vector $i_z$.

Each face of the prism is a part of the plane with the attribute of orientation of the plane normal outside of the solid, and with one loop. The faces of the prism are described by the surfaces

$$
\begin{align*}
r_1(u_1,v_1) &= p + u_1i_x + v_1i_y, & u_1 \in [0, x], & v_1 \in [0, y], \\
r_2(u_2,v_2) &= p + u_2i_y + v_2i_z, & u_2 \in [0, y], & v_2 \in [0, z], \\
r_3(u_3,v_3) &= p + u_3i_x + v_3i_z, & u_3 \in [0, x], & v_3 \in [0, z],
\end{align*}
$$
$$ r_4(u_4,v_4) = p + u_4i_x + v_4i_y + z i_z, \quad u_4 \in [0, x], \quad v_4 \in [0, y], $$
$$ r_5(u_5,v_5) = p + u_5i_y + v_5i_z + x i_x, \quad u_5 \in [0, y], \quad v_5 \in [0, z], $$
$$ r_6(u_6,v_6) = p + u_6i_x + v_6i_z + y i_y, \quad u_6 \in [0, x], \quad v_6 \in [0, z]. $$

Normals to surfaces $r_3, r_4,$ and $r_5$ coincide with the normals to the corresponding faces, and the normals to the surfaces $r_1, r_2,$ and $r_6$ have the opposite directions to the normals to the corresponding faces. This information is contained in the face in the form of the attribute of coincidence of normals. A rectangular prism has twelve edges. Each face consists of the curves of surfaces that intersect with adjacent faces, and an attribute of coincidence of the edge direction with the direction of the intersection curve. Each intersection curve consists of two surface curves: one on the surface of one face, and the other on the surface of the other face. Both surface curves have the same geometric and parametric length and fully coincide in the space. Each curve on the surface is a combination of the surface and the planar curve in the parameter space.

![Fig. 4.6.1.](image1)

![Fig. 4.6.2.](image2)

Let us describe the loop of the first face based on the surface $r_1$. Edges for the loop are constructed on the curves of intersection of surface $r_1$ and surfaces $r_3, r_5, r_6,$ and $r_2$:

$$
e_{13}(t) = \begin{cases} 
r_1(xt,0) & r_3(xt,0) \\
\end{cases}, \quad e_{15}(t) = \begin{cases} 
r_1(x,yt) & r_5(yt,0) \\
\end{cases}, \quad e_{16}(t) = \begin{cases} 
r_1(xt,y) & r_6(xt,0) \\
\end{cases}, \quad e_{12}(t) = \begin{cases} 
r_1(0,yt) & r_2(yt,0) \\
\end{cases}
$$

Let the direction of each edge coincide with the direction of the corresponding curve that we put in the coincidence attributes of the directions of the edges and the curves on which they are based. A loop of the first face is described by the list of curves on which the edges are based, with plus or minus signs corresponding to the flags of the edges: $+e_{12}, +e_{16}, -e_{15},$ and $-e_{13}$. If the edge enters the loop with a positive flag, then by moving along the loop, the edge is traversed from start to end. If the edge enters the loop with a negative flag, then by moving along the loop, the edge is traversed from end to start. For the loop it does not matter from which edge the list is started. The list of edges is cyclic closed. What is important is the sequence of edges, and the coincidence of the direction of edges with the direction of the loop. Recall that when
moving along the loop the edge always lies to the left, if we move along the outer side of the face.

The remaining faces and edges of the prism have a similar structure. Eight vertices are located in the corners of the prism. The orientation of the loops of faces of a rectangular prism is shown in Fig. 4.6.2. Lines with arrows indicate the motion near the loops of the three faces of the prism.

A cylinder has three faces, three edges, and two vertices. Let us place the origin of a local coordinate system $p$ in the center of one of the end faces of the cylinder, and direct basis vector $i_z$ along its axis. Suppose the cylinder has radius $r$ and length $h$.

Let the side face of the solid be based on a cylindrical surface

$$
r_1(u_1,v_1) = p + r \cos u_1 i_x + r \sin u_1 i_y + h v_1 i_z,
$$

where $u_1 \in [0, 2\pi]$, $v_1 \in [0, 1]$.

The normals to the surface $r_1$ and its faces have the same directions. Let the faces of the base be based on the planes

$$
r_2(u_2,v_2) = p + u_2 i_x + v_2 i_y,
$$
$$
r_3(u_3,v_3) = p + u_3 i_x + v_3 i_y + h i_z,
$$

where parameters $u_2$ and $v_2$ lie inside circle $u_2(t) = r \cos t$, $v_2(t) = r \sin t$, $0 \leq t \leq 2\pi$, and parameters $u_3$ and $v_3$ lie inside circle $u_3(t) = r \cos t$, $v_3(t) = r \sin t$, $t \in [0, 2\pi]$. The normals to surface $r_2$ and its faces have opposite directions, and the normal to surface $r_3$ and its faces coincide. Surface $r_1$ intersects with surfaces $r_2$ and $r_3$ along the curves

$$
e_{12}(t) = \begin{cases} 
r_1(t,0) \\ r_2(r \cos t, r \sin t)
\end{cases}, \quad e_{13}(t) = \begin{cases} 
r_1(t,h) \\ r_3(r \cos t, r \sin t)
\end{cases},
$$

$t \in [0, 2\pi]$.

The cylindrical surface $r_1$ of the side face is cyclic closed with respect to the first parameter. The edge constructed on the closing line of the shell is a juncture. The juncture, like any other edge, is based on the curve of intersection, which in this case has the form

$$
e_{11}(t) = \begin{cases} 
r_1(0,ht) \\ r_1(2\pi,ht)
\end{cases}, \quad t \in [0, 1].
$$

Let the direction of each edge of the cylinder coincide with the intersection curve it is based on. The loop of the cylindrical face is described by the list of curves the edges are based on, with signs of their flags corresponding to these edges: $+e_{12}, +e_{11}, -e_{13},$ and $-e_{11}$. The loop of the second face consists of one edge based on curve $e_{12}$ with negative flag. The loop of the third face consists of one edge based on curve $e_{13}$ with positive flag. The vertices are located at the points of junction of curves $e_{12}$ and $e_{13}$ with curve $e_{11}$.
The cylinder is shown in Fig. 4.6.3. The thin line indicates the juncture of a cylindrical face and the lines with arrowheads indicate motion near the loops of the two faces of the solid.

Fig. 4.6.3.

Construction of a cone is similar to that of a cylindrical solid. Let us show the differences between a cylindrical solid and a conical solid. The side face of a cone is based on a conical surface

$$ r_1(u_1,v_1) = p + (r + hv_1 \tan \gamma)(\cos u_1 i_x + \sin u_1 i_y) + hv_1 i_z, $$
$$ u_1 \in [0, 2\pi], \quad v_1 \in [0, 1]. $$

One of the base faces is based on the surface

$$ r_3(u_3,v_3) = p + u_3 i_x + v_3 i_y + h i_z, $$

where parameters $u_3$ and $v_3$ lie inside circle $u_3(t) = (r + htg \gamma) \cos t, \quad v_3(t) = (r + htg \gamma) \sin t, \quad t \in [0, 2\pi]$. Surface $r_1$ intersects with surface $r_3$ along the curve

$$ e_{13}(t) = \begin{cases} 
r_1(t,h) \\ 
r_3((r + htg \gamma) \cos t, (r + htg \gamma) \sin t) 
\end{cases}, \quad t \in [0, 2\pi]. $$

In general, a cone has three faces. If $r > 0$ and $r + htg \gamma = 0$, or $r = 0$ and $\gamma > 0$, then one of the end faces degenerates to a point. A face that degenerates to a point can be excluded from solid, and then the shell of the solid has a pole. A cone with a pole at its top vertex is shown in Fig. 4.6.4. The thin line indicates the juncture of the conical face, and the line with an arrowhead indicates the motion near the loop of this face.

A sphere has a single face, three edges, and two vertices. The origin of a local coordinate system $p$ is placed at the center of the sphere and describes the solid by the surface

$$ r(u,v) = p + r \cos v (\cos u i_x + \sin u i_y) + r \sin v i_z, $$
$$ u \in [0, 2\pi], \quad v \in [-\pi/2, \pi/2]. $$

One of the edges is a juncture based on the curve
$$ e(t) = \begin{cases} r(0,t) & t \in [-\pi/2, \pi/2], \\ r(2\pi,t) & t \in [0, 2\pi]. \end{cases} $$

The other two edges are poles. The pole edges are based on the curves

$$ e_1(t) = r\left(-\frac{\pi}{2}, t\right), \quad e_2(t) = r\left(\frac{\pi}{2}, t\right), $$
$$ t \in [0, 2\pi]. $$

The pole edges are points, but the planar curves in the parameter space of the spherical surface have non-zero length at the poles and are line segments.

The loop of the sphere face is described by the list of curves the edges are based on, with signs of the flags corresponding to these edges: $+e_1, +e, -e_2,$ and $-e.$ Juncture $e$ enters the list of the edges of the loop twice—once with positive flag, and the second time with negative flag.

A sphere is shown in Fig. 4.6.5. The thin line shows the juncture of the spherical face, and the line with an arrowhead shows the motion near the loop of this face.

Fig. 4.6.5.

Fig. 4.6.6.

A torus has one face, two edges, and one vertex. Let us place the origin of a local coordinate system $p$ of a torus-shaped solid at its center and direct the basis vector $i_z$ along the axis of symmetry. Let the large radius of the torus be $R,$ the small radius of the torus be $r,$ and $R>r.$ The face of the torus is based on the surface

$$ r(u,v) = p + (R+r\cos v)(\cos u i_x + \sin u i_y) + r \sin v i_z, $$
$$ u \in [0, 2\pi], \quad v \in [-\pi, \pi], $$

and the two edges are based on the curves

$$ e_1(t) = \begin{cases} r(t,-\pi) & t \in [0, 2\pi], \\ r(t,\pi) & t \in [-\pi, \pi]. \end{cases} $$
$$ e_2(t) = \begin{cases} r(0,t) & t \in [0, 2\pi], \\ r(2\pi,t) & t \in [-\pi, \pi]. \end{cases} $$

The vertex is located at the intersection of edges $p+(R-r)i_x.$ The surface of the torus is cyclic closed with respect to both parameters; therefore both edges of the shell of this
solid are closed and are junctures. The normal to the surface and the edges of the torus have the same direction. The face has one loop. The loop of the face is described by the list of curves the edges are based on with signs of the flags corresponding to these edges: $+e_1, +e_2, -e_1,$ and $-e_2$. The torus, its junctures, and the motion near the loop of the face are shown in Fig. 4.6.6.

Shells of all other solids are constructed according to the general rules and have the same structure as the shells of the elementary solids. Methods of constructing complex solid shells are considered in the next chapter.

### 4.7. Solids Constructed by Curve Translation

Let us construct a solid by translating a composite curve along a given path. Let the translation path be described by curve $g(v)$, which we call the **guide curve**. A curve moving along a translation path is called a **generator curve**. The guide curve and generator curve should not have self-intersections. If the generator curve is not closed, then in general a solid cannot be constructed on the basis of this curve. Usually, a closed composite curve is created from an open curve by “giving it a thickness,” using offset curves. In general, a generator curve is a closed composite curve. If the generator is a planar curve, then we can construct a solid with flat ends.

Let the generator curve $c(u)$ lie on the plane

$$
r(x,y) = p + x i_x + y i_y,
$$

and let it be a closed composite curve composed of $k$ segments joined to each other

$$
c_i(u) = p + x_i(u) i_x + y_i(u) i_y, \quad u \in [u_{\text{min}}, u_{\text{max}}], \quad i = 1, 2, \ldots, k.
$$

Let the closed generator curve be traversed in the counterclockwise direction when viewed towards the vector of the derivative of the guide curve at its start point. If the guide curve $g(v)$ is not closed, then the shell of the solid has end faces. The end faces of swept solids are planes whose domain $\Omega$ is described by the curves $x=x_i(u), y=y_i(u)$. If the guide curve is closed, then the shell of the solid does not have end faces. The side faces of the shell of the solid are based on the surfaces generated by moving the generator curve segments $c_i(u)$ along the guide curve $g(v)$. The number of side faces is equal to the number of segments of the generator curve. Depending on the type of the translation path $g(v)$, one can construct several types of solids.

An **evolution solid** is obtained by plane-parallel translation of the generator curve along a monotonic guide curve. The side faces of an evolution solid are described by surfaces (2.3.1), where the generator curves are the curves (4.7.2). The first end face of the solid is described by a plane (4.7.1) with domain $\Omega$. The second end face is based on a copy of the plane of the first end face shifted by the vector $d=g(v_{\text{max}})-g(v_{\text{min}})$. The evolution solid does not intersect itself, if the dot product of the normal to the plane
(4.7.1) and the derivative of the guide curve does not change sign. An evolution solid is shown in Fig. 4.7.1.

An extrusion solid is obtained when the guide curve is a line segment $g(v) = (1-v)p_1 + vp_2, \ 0 \leq v \leq 1$. The first end face of the extrusion solid is described by plane (4.7.1) with domain $\Omega$. The second end face is based on a copy of the plane of the first end face shifted by the vector $d = p_2 - p_1$. Suppose that a closed generator curve is traversed in counterclockwise, when viewed toward the vector $d$. The side faces of the extrusion solid are described by surfaces (2.3.2), where the generator curves are the curves (4.7.2).

![Fig. 4.7.1.](image1)

![Fig. 4.7.2.](image2)

An extrusion solid constructed on a closed composite curve is shown in Fig. 4.7.2.

In some cases it is required to construct an extrusion solid with sloping side faces. In this case we construct an offset curve for the planar generator curve and move it by the vector $d$. If the generation curve is a composite curve, then the offset curve should also be composite and must contain the same number of segments. In general, the side faces of the extrusion solid with slope are ruled surfaces, each of which is constructed on a segment (4.7.2), and the corresponding segment of the offset curve is displaced by vector $d$. The tangent of the slope angle of the side faces is equal to the ratio of the offset to the length of the extrusion.

A revolution solid is obtained when the guide curve is a circle or arc. Let the axis of rotation pass through point $p$, and its direction be specified by the unit vector $i = (i_1, i_2, i_3)$. The side faces of the solid of revolution are described by surfaces (2.3.3), where the generator curves are the curves (4.7.2).

![Fig. 4.7.3.](image3)

![Fig. 4.7.4.](image4)

The rotation axis should not intersect the side faces. For the solid not to be turned inside out, the rotation axis direction and traversal of the generator must be consistent. Let us specify the positive direction of the rotation axis for the closed generator curve. Suppose we are on the side of the plane (4.7.1) where motion along the generation curve appears to be counterclockwise. Accept the direction of vector $i$ when viewing along which the generator curve is on the left as the positive direction of the rotation.
axis. If the rotation angle is $2\pi$, then the shell of the solid has torus topology; otherwise it has prism topology. In the former case the shell does not have end faces. A solid of revolution with prism topology is shown in Fig. 4.7.3.

Fig. 4.7.4 shows a solid of revolution that can be constructed on an open composite planar curve. Perpendiculars are dropped from the endpoints of the generator curve to the rotation axis. The perpendiculars are then used to construct the corresponding faces. Unlike the previous example, the solid shown in Fig. 4.7.4. is osculating with the rotation axis. These solids are called spheroids.

A swept solid is a generalization of the extrusion solid and solid of revolution for an arbitrary guide curve. A swept solid is obtained by translating a planar closed generator curve along an arbitrary guide curve while maintaining the angle between the generator curve and the tangent vector $\mathbf{g}'(v)$ to the guide curve at the current point. The side faces of a swept solid are described by surfaces (2.3.7), where the generator curves are the curves (4.7.2). A swept solid is shown on the Fig. 4.7.5.

If the guide curve is closed, then we obtain a swept solid with torus topology. If the guide curve is not closed, we obtain a swept solid with the topology of a prism. The side faces of the swept solid should not intersect themselves. Fig. 4.7.6 shows a swept solid constructed on a cyclic closed guide curve.

Let us describe the loop of the side face of a swept solid based on the surface $r_i(u,v)$, $u_{\text{min}} \leq u \leq u_{\text{max}}, v_{\text{min}} \leq v \leq v_{\text{max}}$. For this construct, the curves of intersection of surface $r_i(u,v)$ with the adjacent side surfaces are

$$e_{i-1}(t) = \begin{cases} r_{i-1}(u_{i-1\text{max}}, t) \\ r_i(u_{i\text{min}}, t) \end{cases}, \quad e_i(t) = \begin{cases} r_i(u_{i\text{max}}, t) \\ r_{i+1}(u_{i+1\text{min}}, t) \end{cases}, \quad i \in [v_{\text{min}}, v_{\text{max}}].$$

Construct the curve of intersection of surface $r_i(u,v)$ with the plane of the first end side at the open guide curve:

$$e_{ii}(u) = \begin{cases} c_i(u) \\ r_i(u, v_{\text{min}}) \end{cases}, \quad u \in [u_{\text{min}}, u_{\text{max}}]$$
and the curve of intersection of surface $r_i(u,v)$ with the plane of the second end side:

$$e_{2i}(u) = \begin{cases} a_i(u) \\ r_i(u,v_{\text{max}}) \end{cases}, \quad u \in [u_{\text{min}}, u_{\text{max}}],$$

where $a_i(u)$ is a boundary segment of the second end side, corresponding to segment $c_i(u)$. Let the direction of each edge coincide with the direction of the curve it is based on. The edges of the loop of the $i$-th face of the swept solid are shown in Fig. 4.7.7. A side face of a swept solid has one loop described by a list of edges with flag sign: corresponding to these edges: $+e_{1i}$, $+e_i$, $-e_{2i}$, and $-e_{i-1}$. At the closed guide curve instead of curves $e_{1i}$ and $e_{2i}$, construct the curve of the juncture

$$e_{0i}(u) = \begin{cases} r_i(u,v_{\text{min}}) \\ r_i(u,v_{\text{max}}) \end{cases}, \quad u \in [u_{\text{min}}, u_{\text{max}}].$$

The normals to the side face and the surface coincide.

![Fig. 4.7.7.](image)

If the guide curve is not closed, then the solid has two end faces. The loop of the first end face consists of $k$ edges based on curves $e_{1i}$, $i=k,k-1,\ldots,1$ with negative flag. The normals to the first end face and to the surface are oppositely directed. The loop of the second end face consists of $k$ edges, based on the curves $e_{2i}$, $i=1,2,\ldots,k$ with positive flag. The normals of the second end face and the surface coincide.

### 4.8. Lofted Solids

Let us construct a solid on planar sections specified by a set of curves $r_j(u)$, $j=0,1,\ldots,n$. If the curves $r_j(u)$ are composite, then they must consist of the same number of segments; therefore in each side face of the shell, one segment (4.7.2) from each curve is used. Curves that the side faces are constructed on must have the same parametric length. If all the curves of the set are closed, then it is possible to construct a lofted solid on them. The lofted solid may have two end faces constructed on the boundary curves. The end faces of the solid are planes bounded by these curves. The side faces of the shell may be Lagrange surfaces (2.4.2) or lofted surfaces (2.4.3).

Let us orient the curves of the set so that they are traversed counterclockwise when the curve $c_j(u)$ is viewed from the center of gravity of curve $r_{j+1}(u)$. Assign the value of the
second parameter $v = v_j, j=0,1,...,n$ of the side face surface to each curve $r_j(u)$. For the surfaces passing through the curves of the set with the parameter $v_i$, the surface must coincide with curve $r_j(u)$. The second parameter of surface $v$ between curves $r_j(u)$ and $r_m(u)$ varies from $v_j$ to $v_m$. Note that the shape of the surface depends on parameter values $v_j, j=0,1,...,n$. We get the correct surface when the differences between parameter values $v_j - v_{j-1}$ are proportional to the average distance $|r_j(u) - r_{j-1}(u)|$ between the curves. Fig. 4.8.1 shows the lofted surface constructed on curves $r_j(u), j=0,1,...,n$. A solid constructed on plane sections is shown in Fig. 4.8.2.

Depending on the location of the plane sections, the solid may have prism or torus topology. A solid with prism topology has two end faces. The loops of solid faces constructed on sections are constructed similarly to loops of faces of swept solids.

If, besides the plane sections, the guide curve is given, then we can construct a lofted solid with a guide curve. The side faces of such a solid are based on surfaces (2.4.9). Fig. 4.8.3 shows a surface (2.4.9) constructed on curves $r_0(u)$ and $r_1(u)$ and a guide curve $g(v)$. A solid constructed on plane sections with a guide curve is shown in Fig. 4.8.4.

All other parameters of a solid constructed on plane sections with a guide curve are similar to the parameters of a solid constructed on plane sections without a guide curve.
4.9. Solids Constructed from Surfaces

An arbitrary surface can be a basis for a solid in the form of a finite thickness sheet. Suppose we are given a surface $b(u,v)$, $u,v \in \Omega$. Select the thickness of a sheet $h$ and construct an offset surface corresponding to it:

$$
r(u,v) = b(u,v) + h m(u,v),
$$

where $m(u,v)$ is the normal to the surface $b(u,v)$. Construct two main faces of the sheet solid on surfaces $b(u,v)$ and $r(u,v)$. The faces joining these main faces are called side faces. If domain $\Omega$ of the parameters of surface $b(u,v)$ has a rectangular shape, then the sheet solid has four side faces. In general, a sheet solid has as many side faces as the number of curves in the composite curve describing the domain of the surface parameters $b(u,v)$. Let the domain $\Omega$ be bounded by a composite curve containing $k$ segments:

$$
c_i[u_i(t), v_i(t)]^T,
$$

$t \in [t_{\text{min}}, t_{\text{max}}]$, $i = 1, 2, \ldots, k$.

Each segment corresponds to two three-dimensional curves: $b(u_i(t), v_i(t))$ and $r(u_i(t), v_i(t))$, on which we can construct a side surface. In general, the $i$-th side face is based on the ruled surface

$$
s_i(t,w) = (1-w)b(u_i(t), v_i(t)) + wr(u_i(t), v_i(t)),
$$

$t \in [t_{\text{min}}, t_{\text{max}}]$, $w \in [0, 1]$.

When $h > 0$, the directions of normals to the side faces coincide with the directions of normals to their surfaces. The direction of a normal to a face, based on an offset surface at $h > 0$, coincides with the direction of the surface normal. The direction of a normal to the face based on surface $b(u,v)$ at $h > 0$ is opposite to that of the surface normal. When $h < 0$, the directions of normals to the faces change to the opposite direction.

Let $h > 0$. Then the loop of the first main face consists of $k$ edges based on the curves

$$
e_{i_1}(t) = \begin{cases} 
b(u_i(t), v_i(t)) & t \in [t_{\text{min}}, t_{\text{max}}], \\
s_i(t,0) & i = k, k-1, \ldots, 1
\end{cases}
$$

with negative flag. The normals to the first main face and to the surface $b(u,v)$ are oppositely directed. The loop of the second main face consists of $k$ edges based on the curves
$$ e_{2i}(t) = \begin{cases} r(u_i(t), v_i(t)) & t \in [t_{\text{min}}, t_{\text{max}}], \\ s_i(t, 1) & i = 1, 2, \ldots, k \end{cases} $$

with positive flag. The normals to the second main face and to the surface $r(u,v)$ coincide. To describe the loop of the side face of the solid based on surface $s_i(t,w)$, construct the curves of intersection of this surface with the adjacent side surfaces:

$$ e_{i-1}(w) = \begin{cases} s_{i-1}(t_{i-1\text{max}}, w)   \\ s_i(t_{i\text{min}}, w)  \end{cases} $$
$$e_i(w) = \begin{cases} s_i(t_{i\text{max}}, w)  \\ s_{i+1}(t_{i+1\text{min}}, w)  \end{cases} $$

$w \in [0, 1]$.

Let the direction of each edge coincide with the direction of the curve it is based on. Each side edge of the solid has one loop described by the list of edges with signs of the flags corresponding to these edges: $+e_1, +e_i, -e_2,$ and $-e_{i-1}$. The normals to the side face and its surface coincide.

If surface $b(u,v)$ is closed with respect to one of the parameters, then the sheet solid has the shape of a pipe and topology of a torus. If the surface is closed in both parametric directions, then we obtain a solid with an internal void. Such a solid with $h > 0$ has its outer shell based on surface $r(u,v)$ and its inner shell based on surface $b(u,v)$; when $h < 0$, the outer shell is based on surface $b(u,v)$, and the inner shell is based on surface $r(u,v)$. Fig. 4.9.1 shows a spline surface with the boundary in the form of a closed composite curve. A solid with the shape of a sheet constructed on the abovementioned surface is shown in Fig. 4.9.2.

![Fig. 4.9.1](image)

![Fig. 4.9.2](image)

Using a solid in the form of a sheet it is possible to model the details of car bodies and airframes. To construct the solid it is sufficient to know the basic surface $b(u,v)$ and the thickness of the solid $h$.

**Exercises**

1. Which representations can be used for a geometric model?
2. Construct a solid in the form of a tetrahedron.
3. Construct a solid in the form of a cylinder cut along its axis.
4. Construct a solid in the form of a torus cut along its axis.
