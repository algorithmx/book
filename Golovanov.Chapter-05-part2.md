shown in Fig. 5.6.4.

Another example is the subtraction of a part of a solid obtained by extruding a given closed curve in a given direction, which lies between the solid and the curve, from the given solid (see Fig. 5.6.5).

In this example, the faces of the solid closest to the curve are changed and the faces behind them are kept intact. In different locations the points of the curve should be extruded at various distances. The cutting out of the closest faces of the given solid by the given curve can be done as follows. Construct an extrusion solid of sufficient depth on the given curve to intersect with the given solid. Next, find the intersection of the extrusion solid with the given solid. In the general case, as a result of these manipulations, we obtain several shells (see Fig. 5.6.6). Select the shell closest to the given curve among them (see Fig. 5.6.7).

Subtract the solid with the selected shell from the given solid. This manipulation
combines two Boolean operations. Its result is shown in Fig. 5.6.8.

Stiffeners are included in many designs. Stiffener construction follows the same scheme as the operation of "extrusion" of the curve to the faces of the solid closest to it. A solid with stiffeners is shown in Fig. 5.6.9.

Fig. 5.6.9.

If a shell of an attached or cut-out solid is constructed during the operation, then after the operation it should be verified that the shell of the constructed solid is closed.

5.7. Offset Solids

A solid can be the basis for another solid with all of its faces located along the normal at a given distance from the surface of the original solid. This distance is called the offset parameter, and is denoted as $h$. The solid on which the new solid is constructed is called base solid, and the new solid is called an offset solid. The offset parameter of this operation can take both positive and negative values. If $h>0$, then the base solid is located inside the offset solid. If $h<0$, then the offset solid is located inside the base solid. Invalid parameter values are those values for which the shell of the new solid turns out to be degenerate.

The process of creating the new solid begins with constructing offset faces for each face of the base solid. An offset face is based on a surface that is the offset surface relative to corresponding surface of the base solid. The radius-vector of the offset surface is determined by formula (2.15.4). Fig. 5.7.1 shows three faces of a base solid, which have a common vertex and corresponding offset surfaces. Usually offset surfaces must be truncated or extended to an intersection with adjacent offset surfaces to be joined with them. Continuation of the offset surfaces is performed by extending the base surface in accordance with the rules of extended surface construction (2.15.1)-(2.15.3).

To construct the offset solid, we construct its vertices and edges. The edges are based on the curves of intersection of the offset surfaces. Each intersection curve must start and end at the vertex of the solid. Therefore, we next construct the vertices of the offset shell. Let us consider the sequence of vertices of the base solid. A vertex of the base solid corresponds to one or more vertices of the offset solid. A vertex of the offset solid is based on the intersection point of the offset surfaces. Having calculated this point, we find the parameters of the offset surfaces that serve as the start and end points of the intersection curves of the surfaces. Fig. 5.7.2 shows the point of intersection of
the extended offset surfaces the vertices are based on.

![Fig. 5.7.1.](image1)

![Fig. 5.7.2.](image2)

The edge is called smooth, if the normals of the faces joined by it coincide throughout the entire edge. A smooth edge on an offset solid corresponds to a smooth edge of the base solid. Moreover, the intersection curves of such edges pass through the same points \([u v]^T\) of the corresponding surfaces of the base solid and the offset solid.

Next we construct the edges of the offset shell. Each edge is based on the intersection curve of the offset surfaces. The starting and ending points of the edges provide us with the vertices. The corresponding edge of the base solid can serve as the guide curve for constructing the edge of the offset shell. Fig. 5.7.3 shows the intersection curves of the extended offset surfaces the edges are based on.

Using the edges, construct the loops of the offset faces (see Fig. 5.7.4). This process is similar to the reconstruction of loops of faces in Boolean operations. After these construction steps, the composition of the offset solid is the same as the composition of the base solid.

![Fig. 5.7.3.](image3)

![Fig. 5.7.4.](image4)

If more than three non-smooth edges are joined at a vertex of the base solid, then in the offset solid this vertex corresponds to several vertices and new edges. All of them can be found as the points of intersections of triples of surfaces, or as the points of intersections of the smooth edges and surfaces of the offset solid. Fig. 5.7.5 shows a pyramid and a corresponding offset solid, with a negative offset parameter; Fig. 5.7.6 shows a similar pyramid and an offset solid with a positive offset parameter corresponding to it. Four edges are joined at vertex \(A\) of the pyramid. This vertex corresponds to two vertices \(B\) and \(C\), and one additional edge \(BC\), in the offset solid.
It is possible that there is no analogy to a vertex, an edge, or a face of the base solid in the offset shell. In such solids, we have self-intersections of the shell and self-intersections of the loops of some faces after the above steps. That is, the faces that do not intersect in the base shell intersect in the offset shell. To handle such situations, one should check for any intersection of non-adjacent offset faces. If there are any, you should construct the intersection edges and reconstruct their loops as in the union of solids.

Fig. 5.7.7 on the right and on the left shows offset solids constructed on the base solid shown in the center. For the solid shown in Fig. 5.7.7 on the left $h>0$. For the solid shown in Fig. 5.7.7 on the right $h<0$. The number of faces, edges, and vertices of the offset solids may differ from the number of faces, edges, and vertices of the base solid.

### 5.8. Thin-Shell Solids

Here is a simplified description of the construction of a thin-shell solid: Remove specified faces from a given solid and give the remaining faces finite thickness. Giving finite thickness to the faces is achieved by constructing an offset shell on the open shell remaining after removal of the specified faces and by joining these open shells using parts of the removed faces. We denote the thickness given to the remaining faces by $h$. A thin-shell solid can be constructed both outward ($h>0$) and inward ($h<0$) from the original solid.

Fig. 5.8.2 shows an example of a thin-shell solid ($h>0$) constructed by uncovering
one face of the solid shown in Fig. 5.8.1.

Fig. 5.8.1.  

Fig. 5.8.2.

The process of creating a thin-shell solid begins with sorting the faces of the base solid into two groups: the first group contains the uncovered faces of the base solid, while the second group contains the remaining faces of the base solid, which are called retaining. Let us group the edges of the base solid: The first group contains edges along which the uncovered faces of the base solid intersect with each other, while the second group contains the edges of the retaining faces of the base solid. The process of constructing the shell of a thin-shell solid has much in common with the process of constructing an offset solid.

For each retaining face of a base solid, construct an offset face. The surface of each offset face and each uncovered face should be able to be extended to the intersection with the surfaces of the adjacent faces. The radius-vector of the offset surface is determined by formula (2.15.4).

Next, we consider the vertices of the retaining faces of the base solid. Each considered vertex corresponds to one or several vertices of the thin-shell solid. Several edges are joined at every vertex of the thin-shell solid. The vertex of the thin shell solid is based on the point of intersection of the offset surfaces or on the point of intersection of the offset surfaces with the surfaces of the uncovered faces. Having calculated these points, we find the parameters of the intersecting surfaces that serve as the start and end points of the curves of intersection of the surfaces.

Consider the edges of the retaining faces of the base solid (edges of the second group) consecutively. For each edge, construct the corresponding edge of the thin-shell solid. To do this, find the curves of intersection of the offset surfaces with themselves and with the surfaces of the uncovered faces, using the known start and end points.

Reconstruct the edges of intersection of the uncovered faces (the edges of the first group) on the constructed vertices.

Then turn some faces inside out. If $h > 0$, reverse the direction of the normal and the loops of retaining faces of the base solid and the direction of loops of the uncovered faces of the base solid. If $h < 0$, reverse the direction of the normals of the offset faces.

Finally, construct the loops of the offset faces and reconstruct the loops of the uncovered faces. Thus, the shell of the thin-shell solid is composed of the retaining faces, the offset faces corresponding to them, and parts of the uncovered faces.

When constructing a thin-shell solid, there may be self-intersections of the shell and of the loops of the offset faces. To handle such situations, check for intersection of offset faces that are not adjacent, and if they intersect, construct the intersection edges and
reconstruct their loops as in the union of solids. The described manipulations must be performed during construction of a thin-shell solid on the basis of the solid shown in Fig. 5.8.3. A section of this solid is shown in Fig. 5.8.4.

Fig. 5.8.3.  
Fig. 5.8.4.

Fig. 5.8.5 shows the thin-shell solid constructed by removing the face of the base solid shown in Fig. 5.8.3. Fig. 5.8.6 shows a section of this shell solid. If a thin-shell solid is constructed without removing faces, we obtain a solid with two shells. One of them is an outer shell, and the other is an inner shell. If $h > 0$, the outer shell is the offset shell, and the shell of the base solid should be turned inside out. If $h < 0$, the outer shell is the shell of the base solid, and the offset shell should be turned inside out after construction. The shells are separated by the distance $|h|$. Such a solid has an inside void separated from the outer part of the space.

Fig. 5.8.5.  
Fig. 5.8.6.

5.9. Filleting Solid Edges

A smooth transition from one face of a solid to another called a face conjunction. One way of producing a face conjunction is by filleting the edges of a solid. Solid edge filleting has many varieties. In the simplest case, to fillet an edge means to replace it with the face obtained by sweeping a sphere of a given radius osculating simultaneously with two faces adjacent to the edge. The result of filleting two convex edges and one concave edge of the solid shown in Fig. 5.9.1 is shown in Fig. 5.9.2.
In certain cases, the fillet face may be based on a cylindrical surface or on the surface of a torus. Let us consider the general case of filleting an arbitrary curvilinear edge. Assume that the face located on the right of the filleted edge when viewed from outside the solid along the edge is based on surface \( r(u,v) \), and the face located on the left of the filleted edge is based on surface \( s(a,b) \). These faces and their surfaces are called conjunct. Let the filleted edge be based on the curve of intersection \( c(s) \) of surfaces \( r(u,v) \) and \( s(a,b) \). Construct a fillet surface (3.9.1) on curve \( c(s) \); the fillet surface is osculated with the conjunct surfaces along the curves

$$
c_r(t) = r(u(t), v(t)) \quad \text{and} \quad c_s(t) = s(a(t), b(t)).
$$

The parameter \( t \) is common to the curves \( c_r(t) \) and \( c_s(t) \), and to the fillet surface \( q(t,z) \).

Let us find the intersection of reference curves \( c_r(t) \) and \( c_s(t) \) with the edges of the conjunct faces, and modify these edges. In some cases, the original edges are trimmed; in other cases, they must be extended. If the filleted edge is not cyclic closed, we shall also find the intersection of the fillet surface with the edges of the solid joined with the filleted edge and not belonging to the conjunct faces. These edges should also be trimmed by the fillet surface, or extended to their intersection with the fillet surface.

Next we construct the edges along which the fillet surface joins with the reference faces. Let the curve \( c_r(t) \) coincide with \( q(t,z_{\min}) \), and curve \( c_s(t) \) coincide with \( q(t,z_{\max}) \). Construct two edges along the borders of the fillet surface on the basis of the intersection curves

$$
c_1(t) = \begin{cases} 
r(u(t), v(t)), & \\
q(t, z_{\min}), &
\end{cases}
$$

$$
c_2(t) = \begin{cases} 
s(a(t), b(t)), & \\
q(t, z_{\max}). &
\end{cases}
$$

These edges are called longitudinal, as they are directed along the filleted edge and have the same orientation.

If the filleted edge is cyclic closed, then the fillet surface is also cyclic closed with respect to parameter \( t \). Then, on the basis of the intersection curve

$$
c_0(t) = \begin{cases} 
q(t_{\min}, w), & \\
q(t_{\max}, w), &
\end{cases} \quad w \in [z_{\min}, z_{\max}]
$$
we construct the edge which is a junction of the fillet face.

If the filleted edge is not cyclic closed, we construct the curves along which the fillet surface intersects with other faces of the solid. Create edges on the basis of these curves of intersection. These are called transverse edges.

On the basis of the fillet surface, construct a face. The loop of this face consists of the constructed longitudinal and transverse edges or the junction. Define the attribute of coincidence of the normals to the fillet faces with the direction of the surface normal. The normal to the fillet face should be directed outside the solid; the direction of the normal to the fillet surface may coincide with it or be opposite.

Now reconstruct the loops of the faces on conjunct surfaces \( r(u,v) \) and \( s(a,b) \). Instead of the filleted edge, the edge based on intersection curve \( c_1 \) is included in the loop of face \( r(u,v) \), and the edge based on intersection curve \( c_2 \) is included in the loop of face \( s(a,b) \) (see Fig. 5.9.3).

Next, reconstruct the loops of the other faces that intersect with fillet surface \( q(t,z) \).

![Fig. 5.9.3.](image)

In different situations, edge filleting is performed in different ways. Fig. 5.9.4 shows a solid with filleting of conjunct edges, at the endpoints of which the longitudinal edges of the fillet face converge to a point. In this example, the transverse edges between the conjunct faces converge to a point, and the fillet surfaces are degenerate.

![Fig. 5.9.4.](image)

If three edges joined at one vertex are filleted, then at the vertex we get the case shown
in Fig. 5.9.5. Typically, such a vertex is filleted. Filleting the vertex can be done as described above: The edge of intersection of two fillet faces is conjunct with the third edge and can be filleted with it. Fig. 5.9.6 shows an example of filleting the edges and vertex of a prism by the method described above.

Fig. 5.9.5.  
Fig. 5.9.6.

In many cases it is necessary to fillet several edges conjunct with each other at once. We call the joined edges conjunct, if they have a common tangent and equal angles between the normals to the corresponding adjacent faces at the junction points. The filleting of the conjunct edges should be performed simultaneously for all the conjunct edges.

In some cases it is necessary to fillet several edges joined at a common vertex. If at the vertex more than three edges are joined, then this combination of the edges and a vertex is called a star. If all the edges are subject to the fillet process, then, as for the group of conjunct edges, different stages of the fillet operation should be carried out simultaneously for all the edges of the star and the edges conjunct to them. It also should be taken into account that the star can be joined to other stars by means of the conjunct edges. Therefore, before starting the manipulation, one should find a group of smoothly joining edges, find the stars for them, identify groups of related stars, and then work with these groups of stars as with a single object in the manner described above. Fig. 5.9.7 shows an example of star filleting consisting of six edges.

Fig. 5.9.7.

It might happen that there is enough space on one of the conjunct faces for the longitudinal edge. In this case, we can perform the filleting, preserving of the flange, or adapting the fillet face. Let us consider the different ways using an example of filleting the edges at the bottom of the cylindrical face of the solid shown in Fig. 5.9.8.
In the solid shown in Fig. 5.9.9 one of the reference fillet surface curves at a certain location extends beyond the conjunct face. This part is replaced by the curve of intersection of the fillet face with the corresponding face of the solid. In the solid shown in Fig. 5.9.10, a part of the fillet face is changed so as to preserve the original form of the edge and the face at the location where the reference curve of the fillet surface extends beyond the conjunct face. The fillet surface preserving the flange is described by formula (3.9.7).

In the solid shown in Fig. 5.9.11, a reference curve of the fillet surface also extends beyond the conjunct face in a particular segment. The conjunct face on this segment is smoothly joined with the corresponding adjacent face, and thus the construction is impossible without changing the fillet surface. At the mentioned segment, the initial conjunct face is replaced by the corresponding adjacent face during the construction of the fillet surface.

We can construct a parabolic or elliptical junction of the faces in which the radius of curvature of the fillet face changes smoothly from one conjunct face to another (see
If the radius of curvature varies along the fillet edge, we obtain a variable-radius fillet face (see Fig. 5.9.13). When constructing variable-radius fillets we must define a function of the radius along the length of the edge. The upper part of Fig. 5.9.14 shows a variable-radius fillet face. The fillet radius is changed in such a way that the chord of the fillet face has a constant value. The lower part of Fig. 5.9.14 shows a constant-radius fillet face for comparison.

There are many ways to conjoin solid faces. The given examples illustrate the basic ideas of joining solid faces by processing their edges. Methods for constructing reference curves for fillet surfaces were discussed above.

5.10. Edge Filleting Algorithm for Solids

Let us illustrate the algorithm for edge filleting on the model shown in Fig. 5.10.1. In this case the edges of the model subject to filleting are conjunct.

Before filleting, we form groups of smoothly joined edges, and work with these groups as with a single object, as described above. Fig. 5.10.2 shows a group of four conjunct edges. First of all, construct all the fillet surfaces for the group of conjunct edges (see Fig. 5.10.3).

Next, use these surfaces for trimming the edges of the solid; construct all the longitudinal edges, edges of fillet surfaces conjunct with each other and the edges of intersection of the fillet surfaces with the faces of the solid (see Fig. 5.10.4). After
constructing all these new edges, we construct the fillet faces (see Fig. 5.10.5).

Fig. 5.10.2.

Fig. 5.10.3.

Fig. 5.10.4.

Fig. 5.10.5.

Finally, we reconstruct the loops of the conjunct faces of the solid, and of the other faces that were affected by the manipulation (see Figure 5.10.6). After reconstructing the faces affected by the manipulation, we add other faces related to them, along with the faces of the inner shells of the solid.

Fig. 5.10.6.

Fig. 5.10.7.

The result of filleting four conjunct edges of the solid is shown in Fig. 5.10.7.

5.11. Construction of Edge Chamfers on Solids

Chamfers of the edges of a solid are constructed in a similar way to the construction of fillet edges; the only difference is that the fillet surfaces are replaced with the chamfer surfaces. A chamfer is generally described as a ruled surface (3.9.10)
constructed on two reference curves $c_r(t)$ and $c_s(t)$ on surfaces intersecting along an edge. The result of constructing edge chamfers on the solid shown in Fig. 5.11.1 is shown in Fig. 5.11.2.

Chamfers can be constructed using two linear dimensions, or one linear dimension and one angular dimension. The linear and angular dimensions of a chamfer correspond to the parameters of a triangle that is a section of the cut-off part of the solid transverse to the processed edge. Methods for constructing reference curves for chamfer surfaces were discussed in the previous chapter.

5.12. Direct Modeling

Direct modeling is the modification of geometric models by changing the elements describing the geometric shape of the model without completely rebuilding the model. Direct modeling techniques modify the shell without additional construction, by direct change of the faces of the shell. Direct modification of model elements is also called direct editing. Direct modeling is used in situations when information about the sequence and methods to construct the model is lost during transfer of the geometric model from one system to another. Direct modeling allows editing of the model without the use of additional information.

Let us consider direct modeling techniques on an example of modification of the solid shown in Fig. 5.12.1. Select a group of faces of the solid, and move this group of faces relative to the remaining faces. The result of the operation in which we moved up the group of faces nearest to us is shown in Fig. 5.12.2. The algorithm of this direct editing operation consists of the following manipulations.
In the first step, we define the faces conjunct with the relocated faces. If the relocated faces are bordered by fillet faces, we remove the fillets, storing the faces joined by them in memory. In our example, we consider the solid shown in Fig. 5.12.3 and determine for it the faces conjunct with the relocated faces. In the second step, we relocate the selected group of faces. In the third step we construct new vertices by determining the intersection points of the modified faces and the faces conjunct with them.

In the fourth step we construct new edges that connect the new vertices by constructing the curves of intersection of these faces. In the fifth step we construct the loops of the relocated faces, and reconstruct the loops of the faces conjunct with them. As a result, we obtain the modified solid, but without filleting (see Fig. 5.12.4).

Fig. 5.12.3.  
Fig. 5.12.4.

In the final step, we rejoin the faces that were deleted and stored in memory. The construction of the new vertices and edges, as well as the construction of the loops of the faces affected by the manipulation, has a lot in common with the algorithm for constructing an offset solid.

A widespread method of direct modeling modifies the selected group of faces as required and adjusts the other faces to these changes. Instead of relocating the selected group of faces, we replace them with offset faces. For a planar face, this modification looks like a movement in the direction of its normal. For cylindrical, conical, and spherical faces, it looks like a variation of the radius of the corresponding surface. We replaced two horizontal faces by offset faces in the solid shown in Fig. 5.12.5. In the solid shown in Fig. 5.12.6 we replaced faces of two holes by offset faces.

Fig. 5.12.5.  
Fig. 5.12.6.

A group of faces can be replaced by inclined faces. In the solid shown in Fig. 5.12.
we inclined a conical face—and the cone angle changed its sign as a result. For these methods, it is required to analyze the shell to determine the fillet faces. It is necessary to remove the fillets before the modification, and after the modification the fillets need to be restored.

With direct modeling, one can remove a group of faces and construct a solid from the remaining faces of the shell. The result of an operation in which we removed the group of faces nearest to us is shown in Fig. 5.12.8.

Using the group of faces being removed, we can construct a separate solid. The solid shown in Fig. 5.12.9 was constructed from the faces removed during the previous operation.

![Fig. 5.12.7](image1) ![Fig. 5.12.8](image2) ![Fig. 5.12.9](image3)

The separate solid constructed from the selected group of faces can be used for modeling. Fig. 5.12.10 shows the result of the union of the solid shown in Fig. 5.12.7 and the rotated solid shown in Fig. 5.12.9.

When choosing a fillet surface for the modification, we modify the fillet radius. To do this, it is required to collect the fillet faces of the same radius conjunct with each other in one group, store the faces joined by them in memory, delete the group of fillet faces, and then construct the assemblage of the stored faces with a new radius. Fig. 5.12.11 shows the result of changing the fillet radii of the solid shown in Fig. 5.12.10.

![Fig. 5.12.10](image4) ![Fig. 5.12.11](image5)

### 5.13. Transformations of Solids

Consider two methods of solid deformation: scaling and local deformation.

**Scaling** is applicable to all manifold solids, without exception. Scaling is reduced to the matrix transformation of the data of the vertices, edges, and faces of the solid. We use an augmented matrix (1.14.7) as the scaling matrix. When dealing with this
matrix, it is assumed that the radius-vectors have the form of (1.14.8), and the vectors have the form of (1.14.9). The scaling matrix is described by coordinates \( p_1, p_2, \) and \( p_3 \) of the fixed point, and by the scale factors on the axes \( k_1, k_2, \) and \( k_3; \) and has the form

$$
M = \begin{bmatrix}
k_1 & 0 & 0 & t_1 \\
0 & k_2 & 0 & t_2 \\
0 & 0 & k_3 & t_3 \\
0 & 0 & 0 & 1
\end{bmatrix},
$$

where \( t_i = (1-k_i)p_i, \ i=1,2,3. \) If \( k_1=k_2=k_3, \) then the scaling is isotropic; otherwise, the scaling is anisotropic. Any solid and any shell can be scaled in accordance with a given matrix. Fig. 5.13.1 shows a solid before scaling. Fig. 5.13.2 shows the solid after anisotropic scaling.

![Fig. 5.13.1.](image1)

![Fig. 5.13.2.](image2)

**Local deformation** is possible only for curves and surfaces constructed on a set of points. To locally deform any solid, we replace the surfaces of its faces by supple surfaces or B-spline surfaces, and replace the curves the edges of the shell are constructed on by curves of intersection of the corresponding surfaces. For all surfaces, it is possible to construct supple surfaces or B-spline surfaces geometrically coincident with the replicated surfaces. A solid constructed on supple surfaces or B-spline surfaces can be locally deformed by moving the control points of the surfaces of its faces. A solid with such shells looks like it is constructed from a plastic material under deformation. Fig. 5.13.3 shows a solid before local deformation. Fig. 5.13.4 shows the solid after local deformation of its faces.

![Fig. 5.13.3.](image3)

![Fig. 5.13.4.](image4)
Deformation of the faces can be significant, so special attention should be paid to controlling the deformation. Fig. 5.13.5 shows a solid before deformation. Fig. 5.13.6 shows the solid after uncontrolled deformation.

The local deformation algorithm has much in common with the algorithm for construction of an offset solid, and consists of the following steps. After deforming the surfaces of the faces, we construct new vertices by defining the points of intersection of the faces, using the information about the original vertices as the initial approximations. Next we construct new edges connecting the new vertices, to replace the original edges, by constructing the curves of intersection of the faces. Then we construct the loops of the faces. In the final step, we reconstruct the faces on the new loops, and change the domains of the surfaces of the faces.

Exercises

1. Give the definitions of the Boolean operations on solids.
2. Describe the algorithm for determining the position of a point relative to a solid.
3. Describe the algorithm for drilling a hole in a solid.
4. Describe the algorithm for deformation of a planar face of a solid.