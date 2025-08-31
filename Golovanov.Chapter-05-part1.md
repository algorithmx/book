GEOMETRIC MODEL BUILDING

In geometric modeling, the process of constructing solids is similar to the manufacturing of the modeled object. Initially, the simple-shape solids are constructed, and then manipulations that allow obtaining more complex solids from the simple ones are performed. If necessary, auxiliary objects are constructed. Editing the model and creation of similar models can be done by changing the model parameters, followed by repeating the solid construction process, or by direct modification of the elements of already constructed solids.

5.1. Methods of Geometric Modeling

A solid is associated with a set of points located on the inner side of its shells, and points on the shells themselves. We can perform various operations on these points, including set-theoretic operations. An open solid is associated only with points on the shell itself, with different operations than can be performed on the points of a solid. Open solids are used when it is sufficient to reproduce only a part of the object being modeled.

A set of manipulations on solids leading to the formation of a solid of another shape is called an operation.

Geometric model construction methods have led to the emergence of the terms "surface modeling" (modeling using surfaces) and "solid modeling" (modeling with solids). In both cases the result of modeling is a set of solids describing the surface of the modeled object, but the process and the modeling techniques in the first case are different from those of the second case.

In surface modeling, we create and modify a surface that encompasses individual elements of the simulated object. These surfaces are cut, deformed, smoothed, and joined to each other. Then the resulting surfaces can be combined into a solid by forming faces and junctions from the surfaces. In surface modeling, the resultant solid is not necessarily closed. It may reflect only a portion of the simulated object. Surface modeling allows focusing on complex forms. The result of surface modeling is a set of shells which can have borders. A set of closed shells and open shells called open solids.

In solid modeling, we deal with solids, rather than with individual surfaces, from the very beginning. Surfaces of solids are presented as faces, preserving their original relationships to each other during the modeling process. The solids fully describe the shapes of the modeled objects. The process of solid construction begins with the construction of a simple-shape solid. Then the solid is changed as necessary. With one type of manipulations, volume can be added to or removed from the solid. With other types of manipulations, the solid can be deformed.
In geometric modeling, a solid can be also constructed through a process similar to sculpting. This can be done at any stage of model completeness, from a simple billet to an almost-finished model. The model is directly edited, deforming the solid as required, moving individual elements of the solid relative to each other, or deleting or copying individual elements of the solid. Direct editing of the model is sometimes called direct modeling.

Construction of a shell or solid begins with construction of auxiliary elements, such as a local coordinate system, control points, line segments, and other curves. Then solids are constructed using curves and other auxiliary elements. The methods for constructing solids discussed below include the formation of boundaries of faces and their junctions simultaneously.

5.2. Boolean Operations on Solids

Geometric modeling Boolean operations include union, intersection, and difference operations on the sets of points of two solids.

The solid operands are called the first solid and the second solid, in order of priority. The result of a union operation on two solids is a solid that contains the points belonging to the first or to the second solid. The result of the intersection operation on two solids is a solid that contains the points belonging to the first and to the second solid. The result of the difference operation on two solids is the solid that contains the points belonging to the first solid but not to the second solid.

Fig. 5.2.1 shows a pair solids before a Boolean operation is applied. Fig. 5.2.2 shows the result of a union operation on the solids; Fig. 5.2.3 shows the result of an intersection operation; and Fig. 5.2.4 and Fig. 5.2.5 show the results of a difference operation on the solids.

A difference operation on solids can be reduced to an intersection operation. To do this it is necessary to turn the second solid inside out and find the points of its volume belonging to the volume of the first solid. When turning the solid inside out, the attributes of direction coincidence of normals to faces and their surfaces are reversed, and loop directions are changed to their opposites. As a result, those points in space that previously were outside the solid become the points of the solid. All Boolean operations have many similarities and are performed by the same algorithm.
A union operation on solids can be briefly summarized as follows: It is necessary to find the edges of intersection of the solid faces, cut the intersecting faces by them, and take the parts of faces of the first solid that do not appear inside the second solid and the parts of the second solid that do not appear inside the first solid and construct the new solid using these parts.

Before the operation is started, we find pairs of similar faces in the united solids. Each such pair of faces is located on the same or similar surfaces, but may have different domains and normal orientation. We select pairs of faces having the same normal direction at the coinciding points among the similar faces. Such faces are called overlapping faces. Examples of overlapping faces are upper faces of the solids shown in Fig. 5.2.1. Let us not intersect such faces; instead, let us merge them.

We start the operation with the construction of the intersection curves of the faces of the first solid with the faces of the second solid. Construct the new edges on the basis of the intersection curves of the faces of the first and second solid. We assign the direction of the cross product of the normal to the face of the first solid and the normal to the face of the second solid to the new edges: $t_e = m_1 \times m_2$. The vector of the face normal of the first solid $m_1$ and the vector of the face normal of the second solid $m_2$ are calculated at the point of intersection of the faces. The direction of the edge is determined by the attribute of coincidence with the direction of the intersection curve. Fig. 5.2.6 shows the new edge of intersection of the face of the first solid with the face of the second solid.
The new edges are constructed in such a way that they lie totally inside the loops of the faces of the initial solids. The new edges can be joined to the boundaries of the face by their vertices. Next, cut the original edges of the solid the new edges are joined to, since only a part of the original face is included in the result of the Boolean operation. At points $A$ and $B$, Fig. 5.2.6, the original edges of the faces should be cut along two edges. The cutting of the original edge is carried out by bisecting the curve the edge is based on. Since each edge of the initial solids is included in the loops of two adjacent faces, then after the cutting of the original edges is completed, it is necessary to adjust the loops by taking the cut edges into account.

To cut each of the faces shown in Fig. 5.2.6 into parts, it is necessary to construct their loops, and change the boundary describing the parametric domain of the surface face in accordance with the loops. Fig. 5.2.7 shows two intersected faces (the thin line with the arrowheads indicates the direction of the loops of the faces of the initial solids) and the intersection edge. Fig. 5.2.8 shows those parts of the faces that will be included in the union of the solids (the thin line with the arrowheads indicates the direction of the loops of the faces of the result of the Boolean operation).

We can see in Fig. 5.2.8 with which flags the intersection edges should be included into the loops of faces of the first and second solid.

**Lemma 1.** In a Boolean union of two solids, the new edges are directed along $m_1 \times m_2$; they are included in the loops of faces of the first solid with a negative flag, and in the loops of faces of the second solid—with a positive flag.
Indeed, the result of this operation must contain the part of the face of the first solid lying outside the second solid and the part of the face of the second solid lying outside the first solid. Suppose we are moving along some new edge on the external side of the faces of the solids. Part of the face of the first solid lying outside the second solid is located to the right of the new edge relative to us; hence, the new edge is included in the face loop of the first solid with a negative flag. Part of the face of the second solid lying outside the first solid is located to the left of the new edge relative to us; hence, the new edge is included in the face loop of the second solid with a positive flag.

The initial edges of the solids remaining in the result of the Boolean operation are included in the reconstructed loops, preserving their flags. After the intersection of the solid faces, we obtain a set of new edges oriented in a certain way, joined with each other and with the edges of the original solids at the vertices. An example of the construction of the new edges is shown in Fig. 5.2.9. Not all the new edges of intersected faces are included in the result of the operation; some new edges must be discarded (or should not be constructed).

In a union operation on solids, only new edges whose adjacent faces are continued beyond one of the solids are required. An example of determining necessary new edges is shown in Fig 5.2.10.

Next, reconstruct the loops of the overlapping faces. Faces may overlap completely or partially. The normals $m_1$ and $m_2$ of the overlapping faces have the same direction at the common points. The overlapping faces can be transferred to a common surface. There might be more than two such faces. Before assembling the loops, the overlapping faces and their edges must be brought to a common carrier—the surface of one of the overlapping faces. The initial edges of the overlapping faces of the first solid lying inside the second solid and the initial edges of the overlapping faces of the second solid lying inside the first solid are not included in the shell obtained as the result of the Boolean union.

Construction of a loop of an overlapping face is started with an edge that will be included in the result of the operation. To continue the loop, we find all edges joining with the considered edge at the corresponding vertex among the new and initial edges of the face. Among these edges, we choose the edge that forms the greatest angle relative to the angles of other joining edges, when viewed from the external side of the face, with the angle measured in the clockwise direction. Insert the selected edge in the
loop's list. The construction of the loop is complete when the next edge is joined to the initial edge. Newly constructed loops of overlapping faces are sorted by groups, each of which consists of an external loop and its constituent internal loops. An example of the reconstruction of overlapping faces is shown in Fig. 5.2.11.

Next, reconstruct the loops of the intersected faces. Begin the construction of a loop of an intersected face with a new edge. To continue the loop, we find all edges among the new and initial edges of the face joining with the considered edge at the corresponding vertex. Among the found edges choose the edge that forms the greatest angle relative to the angles of other joining edges, when viewed from the external side of the face, with the angle measured counterclockwise direction. For example, several edges are joined to the new edge $BA$ at point $A$; see Fig. 5.2.12. To continue the loop that started with edge $BA$, choose edge $AC$.

![Fig. 5.2.11.](image)

![Fig. 5.2.12.](image)

Insert the selected edge into the loop's list. Construction of the loop is finished when the next edge is joined to the initial edge. We continue reconstruction of the loops of the face until all of its new edges are used up. In this way, we construct several new loops of the considered face of the first solid in the general case.

Sort the newly constructed loops of the reconstructed face by groups, each of which consists of an external loop and its constituent internal loops. One or more initial loops may remain intact in the considered face. Intact loops are initial loops of the face with none of their edges included in the reconstructed loops. Select those intact loops that must be included in the description of the reconstructed face. These are the original internal loops of the face lying inside the new external loops. If a new external loop has not been found for some new internal loops, and they lie within the initial external loop, then the external intact loop of the face should be included in the reconstructed face.

If we obtain more than one external loop as a result of sorting, then it indicates that several faces appeared from the initial face as a result of the operation. The result of reconstructing the intersecting faces is shown in Fig. 5.2.13.

The described reconstruction of loops is performed for each intersected face of the first and second solid. New edges must be included in the reconstructed loops of faces of the first solid with negative flag, while in the loops of faces of the second solid, new edges must be included with positive flag.

We have reconstructed the overlapping and intersected faces of merged solids. All of them are included in the shell resulting from the Boolean operation. It is also necessary to add the faces that do not intersect in the operation and are related to the
intersected faces, to the faces in the shell of the solid. To do this, examine the edges included in the shell resulting from the operation, and include the adjacent faces of the edges in the shell if they're not there. Continuing this process for all the edges of all the added faces, we obtain the shell of the Boolean operation resultant (see Fig. 5.2.14).

![Fig. 5.2.13.](image)

![Fig. 5.2.14.](image)

The **operation of solid intersection** can be briefly summarized as follows: It is necessary to find the edges of intersection of solid faces, cut the intersected faces by the intersection edges, take the parts of the faces of the first solid that have fallen into the second solid and the parts of the faces of the second solid that have fallen inside the first solid, and construct the new solid using these parts.

The solid intersection operation is similar to the union operation. Before starting the operation, find pairs of similar faces and pairs of overlapping faces in the intersecting solids among the similar faces. Just as in the union operation, we construct new edges and cut with them the edges of the original solids. We also assign the direction of the cross product of the normal to the face of the first solid and the normal to the face of the second solid—$t_e = m_1 \times m_2$—to the new edges.

Fig. 5.2.7 shows the intersecting faces of the solids slicing each other. The part of the face of the first solid lying inside the second solid and the part of the face of the second solid lying inside the first solid are included in the result of the solid intersection (Fig. 5.2.15). In Fig. 5.2.15 it is apparent with which flags the edges of intersection in the loops of faces of the first and second solid should be included.

**Lemma 2.** In the Boolean operation of intersection of two solids, the new edges directed along $m_1 \times m_2$ are included in the loops of faces of the first solid with a positive flag, and in the loops of faces of the second solid—with a negative flag.

![Fig. 5.2.15.](image)
Indeed, the result of the intersection operation must contain the part of the face of the first solid lying inside the second solid and the part of the face of the second solid lying inside the first solid. Suppose we are moving along some new edge, being on the external side of the faces of the solids. Part of the face of the first solid lying inside the second solid is located on the left of the new edge relative to us, and hence, the new edge is included in the face loop of the first solid with a positive flag. Part of the face of the second solid lying inside the first solid is located to the right of the new edge relative to us, and hence, the new edge is included in the face loop of the second solid with a negative flag.

The initial edges of solids that remain unchanged in the result of the Boolean operation are included in the reconstructed loops, preserving their flags.

As in the union operation, not all new edges of the intersected faces are included in the resultant of the intersection operation; some new edges must be discarded (or should not be constructed).

In a solids intersection operation, only those new edges are required whose adjacent face have a continuation into one of the solids.

Before assembling loops, the overlapping faces and their edges must be brought to a common carrier—to the surface of one of the overlapping faces. In a solids intersection operation, the initial edges of the overlapping faces of the first solid lying outside the second solid, and the initial edges of the overlapping faces of the second solid lying outside the first solid, are not included in the shell obtained as the result.

Reconstruction of the face loops in the intersection operation is similar to loop reconstruction in the union operation.

Construction of a loop of an overlapping face is started with an edge that will be included in the resultant of the operation. To continue the loop, we find all edges joining with the considered edge at the corresponding vertex among the new and initial edges of the face. Among these, edges choose the edge that forms the greatest angle relative to the angles of other joining edges, when viewed from the external side of the face, measuring the angle clockwise. Insert the selected edge into the loop’s list. The construction of the loop is completed when the next edge is joined to the initial edge.

Construction of a loop of an intersecting face is started with a new edge. To continue the loop, we find all edges joining the considered edge at the corresponding vertex among the new and initial edges of the face. Among these edges, choose the edge that forms the greatest angle relative to the angles of other joining edges, when viewed from the external side of the face, with the angle measured counterclockwise. Insert the selected edge into the loop’s list. Loop construction is complete when the next edge is joined with the initial edge.

Divide the newly constructed and original loops of each reconstructed face into groups. Each group consists of the external loop and its constituent internal loops. Reconstruct the faces with the help of these groups. If we obtain more than one external loop as a result of sorting, it indicates that several faces appeared from the initial face as the result of the operation.

Loop reconstruction is performed for each intersecting face of the first and the second solid. In a solid intersection operation, new edges must be included in the reconstructed loops of the faces of the first solid with a positive flag, and in the loops of the faces of the second solid with a negative flag.

Include the reconstructed overlapping and intersecting faces of the intersecting solids in the shell of the Boolean operation resultant. Add the faces related to the faces
in the shell of the new solid to the faces of the new solid.

The operation of difference of solids is reduced to the Boolean operation of intersection of the first solid with the inside-out second solid. The inside-out second solid is obtained from the original solid by redirecting the face normals and loops of the faces. Redirecting the face normal is performed by changing the attribute of coincidence of the surface normal and its face normal. Redirecting loops of the face is performed by rebuilding the list of edges (reversing the order of the edges in the list), and by changing the values of flags of the edges in the lists.

5.3. An Algorithm for Boolean Operations

All Boolean operations follow a common algorithm. Let us divide the algorithm into five steps and consider them in the example of the difference operation of solids shown in Fig. 5.3.1.

![Fig. 5.3.1.](image)

Before starting the difference operation, turn the solid being subtracted inside-out. The first step is the construction of the new edges, along which the faces of the solids-operands intersect (see Fig. 5.3.2). The second step is to select essential edges for the operation being performed from among the new edges (see Fig. 5.3.3). In the union operation, the set of essential edges is different.

![Fig. 5.3.2.](image) ![Fig. 5.3.3.](image)

The third step is the construction of the overlapping faces (see Fig. 5.3.4). The fourth
step is the reconstruction of the intersecting faces (see Fig. 5.3.5).

The fifth step is the formation of the shell of the new solid from the reconstructed faces and the original faces of the solid-operands related to them (see Fig. 5.3.6). Let us consider some features of these manipulations.

When performing Boolean operations, the most time-consuming process—requiring a certain precision—is the construction of the new edges of intersecting faces. New edges should join with each other and with the original edges of the faces at the vertices. New edges should not intersect each other outside the endpoints. Fig. 5.3.7 shows two cylindrical solids of the same diameter with intersecting axes. When the cylindrical faces are intersected, at least four new edges should be constructed in Boolean operations. The vertices should be located at the points $A$ and $B$ (at the contact points of the cylinders).

In Boolean operations it is possible for some face of one solid to intersect the other solid along its edge. Another possible case is when during the construction of new intersection edges of the faces of one solid with the faces of the other solid, two new edges coincide with each other and with the original edge of one of the solids. All the edges are different, since different faces are joined along them. Fig. 5.3.8 shows two solids, on which performing Boolean operations yields new edges coincident with the original edges of one of the solids.
Following the common algorithm, we obtain eight new edges in this case, half of which must be discarded (or should not be constructed).

In the presence of new edges coinciding with the original edges of solids, we carry out the following verification. Construct two vectors in the plane of each of the two intersecting faces that are orthogonal to the new edge. In Fig. 5.3.9 the vectors are $a_1$ and $b_1$ for the face with normal $m_1$, and $a_2$ and $b_2$ for the face with normal $m_2$. Vectors $a_1$ and $a_2$ turn to the left of the new edge when moving along the new edge on the external side of the corresponding face. Vectors $b_1$ and $b_2$ turn to the right of the new edge at the corresponding faces, when moving along the new edge on the external side of the corresponding face.

If the face has no continuation from the new edge in the direction of some vector $a_1$, $a_2$, $b_1$, or $b_2$ (the new edge partially or completely coincides with the original edge of the solid), then the corresponding vector is set equal to zero (see Figs. 5.3.10, 5.3.11).
Using vectors $a_1$, $a_2$, $b_1$, and $b_2$, and normals $m_1$ and $m_2$, it is possible to determine whether this new edge is to be used in the operation or to be discarded. To do this, the following rule should be fulfilled.

**Rule 1.** Let $r_1(u,v)$ and $r_2(a,b)$ be intersecting faces of the first and second solid respectively, for which a new edge can be constructed. If $r_1(u,v)$ has a continuation to the right of the new edge outside the second solid, then the loops of face $r_1(u,v)$ should be reconstructed in a union operation on solids. If $r_2(a,b)$ has a continuation to the left of the new edge outside the first solid, then the loops of the face $r_2(a,b)$ should be reconstructed in a union operation on solids.

Thus, in a Boolean operation of solid union, the following conditions must be met for the new edge:

$$m_1 \cdot a_2 > 0 \quad \text{and} \quad m_2 \cdot b_1 > 0.$$  

(5.3.1)

Otherwise, the considered new edge in a Boolean operation of union of solids should not be constructed (if it is constructed, it must be discarded).

**Rule 2.** Let $r_1(u,v)$ and $r_2(a,b)$ be intersecting faces of the first and second solid respectively, for which a new edge can be constructed. If $r_1(u,v)$ has a continuation to the left of the new edge inside the second solid, then the loops of face $r_1(u,v)$ should be reconstructed in a Boolean operation of intersection of solids. If $r_2(a,b)$ has a continuation to the right of the new edge inside the first solid, then the loops of face $r_2(a,b)$ should be reconstructed in a Boolean operation of intersection of solids.

Thus, the following conditions for the new edge must be met in a Boolean operation of the intersection of solids:

$$m_1 \cdot b_2 < 0 \quad \text{and} \quad m_2 \cdot a_1 < 0.$$  

(5.3.2)

Otherwise the considered new edge in the Boolean operations of intersection of solids should not be constructed (if it is constructed, it must be discarded).

To answer the question whether the face of the solid extends inside or outside another solid from the new edge, one should be able to determine the position of a point $p$ relative to the solid: whether the point $p$ belongs to the inner space of the solid, whether it lies on the surface of the solid, or whether it is located outside the solid. To do this, let us find the point $p_0$ nearest to point $p$ on the face of one of the solid shells. Then we construct the vector $v = p - p_0$ from the nearest point $p_0$ to the point $p$, and compute the normal to shell $m$ at point $p_0$. The method of calculating the normal to the shell depends on what would be the closest point of the shell. The nearest point of the shell can be either the projection of point $p$ onto one of the faces, or the projection of point $p$ onto one of the edges; or it can be one of the vertices of the shell. If the nearest point of the shell is the projection of point $p$ onto one of the faces, then the normal to this face at the projection point can be taken as the normal to the shell $m$. If the nearest point of the shell is the projection of point $p$ onto one of the edges, then the normalized sum of normals of the faces joined at the considered edge at the point of projection is taken as the normal to the shell $m$ at the edge. If the nearest point of the shell is a vertex of the shell, then the normalized sum of the normals to the edges joined at the considered vertex at the projection point is taken as a normal to the shell $m$ at the vertex.
To determine the position of the point relative to the solid, let us use the principle of solids construction according to which the normal to the surface of the solid is directed outward from the solid. The location of the point relative to the solid shell is determined by the dot product of the vector \( \mathbf{v} \) and the normal \( \mathbf{m} \) at the nearest point of the shells of the solid. If the length of vector \( \mathbf{v} \) is zero, then \( \mathbf{v} \cdot \mathbf{m} = 0 \), and point \( p \) is located on the surface of the solid; if \( \mathbf{v} \cdot \mathbf{m} > 0 \), then point \( p \) is located outside the solid; and if \( \mathbf{v} \cdot \mathbf{m} < 0 \), then point \( p \) is located inside the solid.

If any of the solid-operands has voids and, therefore, is described by several shells, then the shells that are not changed by the operation and the shells of the resultant of the Boolean operation should be verified for their inclusion into each other. In the general case, the resultant of the Boolean operation may also have several shells.

### 5.4. Sectioned Solids

The algorithm for Boolean operations allows slicing of a solid by an open shell. The slicing shell should completely cross over the solid. The result of this operation is a new solid that is a part of the original solid, lying inside or outside of the slicing shell. The open slicing shell is called an incomplete solid.

![Fig. 5.4.1](image1)

![Fig. 5.4.2](image2)

When slicing a solid by a shell, we perform the operation of intersection of the solid with the part of the space lying to one side of the slicing shell. If it is required to construct the part of the solid lying on the external side of the slicing shell, then perform the Boolean operation of subtraction of the incomplete solid from the given solid. If it is required to construct that part of the solid that lies on the inner side of the slicing shell, then perform the Boolean operation of intersection of the given solid with the incomplete solid. Fig. 5.4.1 shows a solid in the form of a rectangular parallelepiped; a slicing shell; a normal to the shell; and the intersecting edges of the solid faces with the shell. Fig. 5.4.2 shows the sliced solid.

In this particular case, the solid can be sliced by a plane. Using this operation, we can obtain a complex slice of the solid. For this, the shell of the incomplete solid should be composed of several faces joined to each other. To obtain a complex slice, take a composite curve in the plane and construct an incomplete extrusion solid on it, so that it intersects the given solid as desired. Next, perform the Boolean operation on the given solid and on the incomplete solid. Fig. 5.4.3 shows the initial solid and Fig. 5.4.4 shows the result of a complex slicing of the solid.
5.5. Symmetric Solids

Suppose we are given a solid and a plane. Let us construct a solid symmetrical to the given solid with respect to the given plane. The symmetric solid is a mirror image of the given solid. The geometry of the solid is described by points, curves, and surfaces, constructed from vectors and scalars. Therefore, the construction of the symmetric solid ultimately reduces to a symmetry transformation of the radius-vectors of the points, free vectors, and scalars. Scalars do not change under symmetry transformation; free vectors change their direction; and points change their positions.

Let the plane of symmetry pass through \( p_0 \), and a normal to the plane be described by a vector of unit length \( i = [i_1 \ i_2 \ i_3]^T \) (see Fig. 5.5.1). Let us determine the coordinates of point \( r \) symmetrical to point \( r_0 \) relative to the plane.

Construct a vector \( p = r_0 - p_0 \), and represent it as a sum of two vectors: the projection onto the plane of symmetry and a component \( n \), perpendicular to the plane of symmetry:

$$
p = (p - n) + n,
$$

where \( n = (p \cdot i) i \). After mirroring the vector \( p \), its component \( n \)—normal to the plane—changes and becomes equal to \(-n\). Projection \((p - (p \cdot i) i)\) of vector \( p \) onto the plane of symmetry does not change. The location of the point symmetrical to point \( r_0 \) is described by the radius-vector

$$
r = p_0 + (p - (p \cdot i) i) - (p \cdot i) i = p_0 + (E - 2 i i^T) \cdot p = p_0 + A \cdot (r_0 - p_0),
$$
where symmetry transformation matrix $A$ is defined by the equality

$$
A = \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix} - 2 \begin{bmatrix}
i_1 i_1 & i_1 i_2 & i_1 i_3 \\
i_2 i_1 & i_2 i_2 & i_2 i_3 \\
i_3 i_1 & i_3 i_2 & i_3 i_3
\end{bmatrix}.
$$

(5.5.1)

After the symmetry transformation with respect to this plane, free vector $v_0$ is described by the radius-vector

$$
v = A v_0.
$$

After the symmetry transformation, all the points and surface curves remain unchanged. Surface normals reverse their directions. If we perform the transformation only on the solid geometric data using matrix (5.5.1), we obtain a mirror image of the solid turned inside-out. Thus, the construction of the symmetric solid reduces to the transformation of its copy using matrix (5.5.1) and reorientation of the directions of normals to the faces and the directions of loops of the faces. Redirection of the face normal is performed by changing the attribute of coincidence of the surface normal and its face normal. Redirection of the loops of the face is performed by rebuilding the list of the edges (reversing their order) and by changing the values of the flags of the edges in the lists.

Let a plane of symmetry intersect a solid. Let us imagine that the shell of the solid is bisected by the plane, one of the sliced parts is removed, and the other part is glued to its mirror copy. We obtain a solid that is symmetric about the plane. This solid consists of two halves, one of which coincides with a part of the original solid. The symmetry plane can be a flat face of the original solid. The construction of such a symmetric solid has much in common with the union operations on solids.

Without loss of generality, we construct the symmetrical solid based on its part that is located behind the plane of symmetry. First, we construct curves of intersection of the solid faces with the plane. If the face is described by radius-vector $r(u,v)$, then the curve of intersection with the plane of symmetry $p(x,y)$ for this face is represented in the form

$$
e_p(t) = \begin{cases}
r(u(t), v(t)) & t \in [t_{\text{min}}, t_{\text{max}}] \\
p(x(t), y(t))
\end{cases}.
$$

This curve consists of two planar curves—$[u(t) \ v(t)]^T$, on surface $r(u,v)$, and $[x(t) \ y(t)]^T$, on the plane of symmetry. Construct new edges on the basis of the intersection curves. With the help of the attribute of direction coincidence of the edge and its intersection curve, let us give the new edges the direction of the cross product of the face normal with the normal to the plane: $t_e = m_f \times m_p$. After constructing the new edges, determine the points of their intersection with the original edges of the solid, construct the vertices at these points, and slice the edges apart by these vertices.

Then construct a copy of the part of the solid’s shell lying above the plane,
making it symmetric relative to the plane.

Now all we have to do is join the symmetric halves of the solid along the edges of the intersection of the solid with the plane of symmetry. But before that, we should substitute the curves on the symmetric shell for the curves on planes belonging to the intersection curves of the new edges. To do this, instead of curves $e_p$, we place the following curves at the edges:

$$e(t) = \begin{cases} r(u(t), v(t)) \\ r'_p(u(t), v(t)) \end{cases}, \quad t \in [t_{\text{min}}, t_{\text{max}}].$$

Curve $e(t)$ contains two planar curves—$[u(t) \ v(t)]^T$ lies on the surface $r(u,v)$, and its copy lies on the symmetric copy $r'_p(u,v)$ of surface $r(u,v)$. Now each intersection edge is based on two symmetric halves of the desired solid.

Finally, we reconstruct the loops of solid faces intersected by the plane. Reconstruction of the loops of a face is described in detail in the Boolean operation of union of solids. Each intersection edge should be included in a loop of the original face with a negative flag, and in the loop of its symmetric part with a positive flag.

Add non-intersecting faces of the solid that are associated with the intersecting faces and the symmetric copies corresponding to these non-intersecting faces. In this way we obtain the shell of the symmetric solid.

In constructing the symmetric shell, we consider all the cases of coincidence of the new edges and the initial edges of the solid and partial overlapping of faces, described in the Boolean operations on solids. Moreover, the existence of several shells in the original solid should be taken into account.

Fig. 5.5.2.

Fig. 5.5.3.
Fig. 5.5.2 shows an initial solid and a plane of symmetry. Fig. 5.5.3 shows the result of symmetric solid construction. Fig. 5.5.4 shows the result of sequential execution of two operations of the construction of the symmetric solid relative to mutually orthogonal planes of symmetry.

5.6. Solids with Supplementary Elements

In practice, it is often required to perform a Boolean operation when the shell of one of the operands is not fully defined and must be completed during the operation. For example, suppose that it is required to add a part of a solid obtained by extruding a given closed curve in a given direction, which lies between a solid and a curve, to the given solid (see Fig. 5.6.1).

In this case it is required to extrude the given curve to the nearest faces of the given solid. The closest faces might be different in different places along the given curve, so the points of the curve should be extruded at various distances.

This operation can be performed as follows. Construct the extrusion solid of sufficient depth to intersect with the given solid on the given curve. Next, subtract the given solid from the extrusion solid. As a result of such an operation in the general case, we obtain several shells (see Fig. 5.6.2). Choose the closest to the given curve from them (see Fig. 5.6.3). Combine the given solid with the solid with the selected shell. This manipulation involves two Boolean operations. When performing them it is sufficient to construct the edges of intersection just once. The result of this operation is