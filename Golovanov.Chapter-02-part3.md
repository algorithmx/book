0 \leq u \leq 1 \text{ and } 0 \leq v \leq 1; \text{ for example: } a = u, b = v(1-u), \text{ and } c = 1 - u - v + uv — or: a = u(1-v), b = v, \text{ and } c = 1 - u - v + uv.

2.11. Triangular Bezier Surfaces

Suppose there is a set of control points \( p_{ijk} \) located on the nodes of a triangular mesh. Fig. 2.11.1 shows a triangular mesh with six control points along each side. The points are arranged in a triangle, and there is the same number of points along each side of the triangle. Assume that this number is equal to \( n+1 \). In the example shown in Fig. 2.11.1, \( n=5 \). The total number of control points is \( (n+1)(n+2)/2 \). Each point index corresponds to a vertex of the triangle. The points at the vertices of the triangle have indexes equal to \( n \) (maximum value), and the values of their other two indexes equal to zero. The points in the row along one of the three sides of the triangle have zero indexes corresponding to the opposite vertices. The closer to the vertex the row in which the points lie, the more important the index of the vertex.

$$
\begin{array}{cccc}
p_{005} & & & \\
& p_{104} & p_{014} & \\
& p_{203} & p_{113} & p_{023} \\
& p_{302} & p_{212} & p_{122} & p_{032} \\
& p_{401} & p_{311} & p_{221} & p_{131} & p_{041} \\
& p_{500} & p_{410} & p_{320} & p_{230} & p_{140} & p_{050}
\end{array}
$$

Fig. 2.11.1.

The indexes of point \( p_{ijk} \) give the value of an integer distance from the point to the corresponding side of the triangle, measured by the number of separating rows. The sum of the indexes of the control point \( p_{ijk} \) is a constant,

$$
i + j + k = n. \tag{2.11.1}
$$

A triangular Bezier surface is described using barycentric coordinates \( a, b, \) and \( c \). We assume that the Bezier surface has the same parametric domain as the surface (2.10.10). The triangular Bezier surface constructed on control points \( p_{ijk} \) is described by the vector function

$$
r(a, b, c) = \sum_{i+j+k=n} B^n_{ijk}(a, b, c)p_{ijk} =
$$
$$ = \sum_{i,j,k=0,i+j+k=n} \frac{n!}{i!j!k!} a^i b^j c^k p_{ijk}, \quad (2.11.2) $$
$$ a \in [0, 1], \quad b \in [0, 1], \quad c \in [0, 1], \quad a + b + c = 1. $$

The summation in (2.11.2) is performed over all control points, and the three-index Bernstein functions have the form

$$ B^n_{ijk}(a,b,c) = \frac{n!}{i!j!k!} a^i b^j c^k, \quad (2.11.3) $$

where equality (2.11.1) must be satisfied. The triangular Bezier surface is shown in Fig. 2.11.2.

The boundary curves of the surface (2.11.2) are described by the vectors \( r(a,1-a,0), r(0,b,1-b), \) and \( r(1-c,0,c) \). They represent Bezier curves (1.4.1). We show this by the example of boundary curve \( r(a,1-a,0) \). For this curve, \( c = 0, k = 0, \) and functions (2.11.3) take the form

$$ B^n_{ij0}(a) = \frac{n!}{i!j!} a^i b^j = \frac{n!}{i!(n-i)!} a^i (1-a)^{n-i}, \quad (2.11.4) $$

which coincides with (1.4.2).

We can show that the three-index Bernstein functions satisfy the equation

$$ \sum_{i,j,k=0,i+j+k=n} B^n_{ijk}(a,b,c) = 1. \quad (2.11.5) $$

Let us perform summation (2.11.5) over the lines of the third index \( k = 0, 1, \ldots, n \). The \( k \)-th line of the third index contains \( m = n - k \) control points.

$$ \sum_{i,j,k=0,i+j+k=n} B^n_{ijk}(a,b,c) = \sum_{i,j,k=0,i+j+k=n} \frac{n!}{i!j!k!} a^i b^j c^k = $$
$$ = \sum_{k=0}^{n} \frac{n!}{k!(n-k)!} c^k \sum_{i=0}^{n-k} \frac{(n-k)!}{i!(n-k-i)!} a^i b^{n-k-i} = $$
$$ = \sum_{k=0}^{n} C^k_n c^k \sum_{i=0}^{n-k} C^i_{n-k} a^i b^{n-k-i} = \sum_{k=0}^{n} C^k_n c^k (a + b)^{n-k} = (a + b + c)^n = 1, $$

as required. If we assume that there is a triangular surface constructed on every three adjacent points \( p_{ijk}, p_{i-1,j+1,k}, \) and \( p_{i-1,j+1,k+1} \), then we obtain a control polyhedron providing an overall view of the surface. The control polyhedron of the triangular Bezier surface presented in Fig. 2.11.2 is shown in Fig. 2.11.3. The triangular Bezier surface does not pass through any of its control points except the three corner points.

The tree-index Bernstein functions satisfy the recursion relation
$$ B^n_{ijk} = aB^{n-1}_{i-1jk} + bB^{n-1}_{ij-1k} + cB^{n-1}_{ijk-1}. $$ (2.11.6)

This relation can be proved by direct substitution:

$$
aB^{n-1}_{i-1jk}(a,b,c) + bB^{n-1}_{ij-1k}(a,b,c) + cB^{n-1}_{ijk-1}(a,b,c) =
$$
$$
= a \frac{(n-1)!}{(i-1)!j!k!} a^{i-1}b^jc^k + b \frac{(n-1)!}{i!(j-1)!k!} a^ib^{j-1}c^k + c \frac{(n-1)!}{i!j!(k-1)!} a^ib^jc^{k-1} =
$$
$$
= \frac{i}{n} \frac{n!}{i!j!k!} a^ib^jc^k + \frac{j}{n} \frac{n!}{i!j!k!} a^ib^jc^k + \frac{k}{n} \frac{n!}{i!j!k!} a^ib^jc^k =
$$
$$
= \frac{i+j+k}{n} \frac{n!}{i!j!k!} a^ib^jc^k = B^n_{ijk}(a,b,c),
$$

as required, because (2.11.1). We start with calculation of the function

$$ B^0_{000}(a,b,c) = 1. $$

Then we obtain \( B^1_{100}(a,b,c)=a, \) \( B^1_{010}(a,b,c)=b, \) and \( B^1_{001}(a,b,c)=c. \) A Bernstein function with one of the indexes equal to a negative number is considered to be zero. Substitute recursion relation (2.11.6) into relation (2.11.2). Select out the endpoints and take into account that \( B^n_{n00}=a^n, \) \( B^n_{0n0}=b^n, \) \( B^n_{00n}=c^n, \) and \( B^n_{ijk}=b^ic^k, \) \( B^n_{i0k}=a^ic^k, \) \( B^n_{ij0}=a^ib^j; \) we thus obtain

$$
r(a,b,c) = \sum B^n_{ijk}p_{ijk} = \sum \left( aB^{n-1}_{i-1jk} + bB^{n-1}_{ij-1k} + cB^{n-1}_{ijk-1} \right)p_{ijk} =
$$
$$
= a \sum_{i,j,k=0,i+j+k=n-1} B^{n-1}_{ijk}p_{i+1jk} + b \sum_{i,j,k=0,i+j+k=n-1} B^{n-1}_{ijk}p_{ij+1k} + c \sum_{i,j,k=0,i+j+k=n-1} B^{n-1}_{ijk}p_{ijk+1} =
$$
$$
= a r_{i+1jk}^{(n-1)} + b r_{ij+1k}^{(n-1)} + c r_{ijk+1}^{(n-1)},
$$
where we introduce the notation

$$ r_{i+1jk}^{(n-1)} = \sum_{i+j+k=n-1} B_{ijk}^{n-1} p_{i+1jk}, $$

$$ r_{ij+1k}^{(n-1)} = \sum_{i+j+k=n-1} B_{ijk}^{n-1} p_{ij+1k}, $$

$$ r_{ijk+1}^{(n-1)} = \sum_{i+j+k=n-1} B_{ijk}^{n-1} p_{ijk+1}. $$

Performing the described manipulations with \( r_{i+1jk}^{(n-1)} \), \( r_{ij+1k}^{(n-1)} \), and \( r_{ijk+1}^{(n-1)} \), we obtain the equation

$$ r_{ijk}^{(0)} = B_{000}^{(a,b,c)} p_{ijk} = p_{ijk}. $$

Denote \( r(a,b,c) \) as \( r_{000}^{(n)} \). As a result, we obtain the recursive relation for calculating a point of a triangular Bezier surface

$$ r_{ijk}^{(m)} = a r_{i+1jk}^{(m-1)} + b r_{ij+1k}^{(m-1)} + c r_{ijk+1}^{(m-1)}, \tag{2.11.7} $$

where \( i+j+k=n-m \ (i,j,k \geq 0) \), \( r_{ijk}^{(0)} = p_{ijk} \), and \( r_{000}^{(n)} = r(a,b,c) \). The algorithm described by relations (2.11.7) is called De Casteljau's algorithm. Points \( r_{ijk}^{(m)} \) obtained from the calculations are called De Casteljau's points. De Casteljau's algorithm allows us to calculate any point of a triangular Bezier surface using the control points, and without knowing anything about the Bernstein functions. Coefficients \( a \), \( b \), and \( c \) of the coordinates of points \( r_{i+1jk}^{(m-1)} \), \( r_{ij+1k}^{(m-1)} \), and \( r_{ijk+1}^{(m-1)} \) are the barycentric coordinates. A triangular Bezier surface can be defined as a surface whose points are determined by recursive relation (2.11.7) on a set of control points.

From a triangular Bezier surface of \( n \)-th degree we proceed to the triangular surface of \((n+1)\)-th degree just as we did for Bezier curves. To do this, we multiply the right-hand side of (2.11.2) by the sum \( a+b+c \), which is equal to 1, and obtain

$$ r(a,b,c) = \sum_{i+j+k=n} B_{ijk}^n p_{ijk} = \sum_{i+j+k=n} \frac{n!}{i!j!k!} a^i b^j c^k p_{ijk} (a+b+c) = $$

$$ = \sum_{i+j+k=n} \frac{n!}{i!j!k!} a^i b^j c^k p_{ijk} + \sum_{i+j+k=n} \frac{n!}{i!j!k!} a^i b^{j+1} c^k p_{ijk} + \sum_{i+j+k=n} \frac{n!}{i!j!k!} a^i b^j c^{k+1} p_{ijk} = $$

$$ = \sum_{i+j+k=n} \frac{(n+1)!}{(i+1)!j!k!} a^{i+1} b^j c^k p_{ijk} + \sum_{i+j+k=n} \frac{(n+1)!}{i!(j+1)!k!} a^i b^{j+1} c^k p_{ijk} + \sum_{i+j+k=n} \frac{(n+1)!}{i!j!(k+1)!} a^i b^j c^{k+1} p_{ijk}. $$
$$ \sum_{i,j,k=0}^{n+1} \frac{(n+1)!}{iljlk!} a^ib^jc^k \frac{ip_{i-1jk}}{n+1} + \sum_{i,j,k=0}^{n+1} \frac{(n+1)!}{iljlk!} a^ib^jc^k \frac{jp_{ij-k}}{n+1} + \sum_{i,j,k=0}^{n+1} \frac{(n+1)!}{iljlk!} a^ib^jc^k \frac{kp_{ijk-1}}{n+1} = \sum_{i,j,k=0}^{n+1} B^{n+1}_{ijk} p^*_{ijk} $$  

(2.11.8)

where \( p^*_{ijk} = \frac{ip_{i-1jk} + jp_{ij-k} + kp_{ijk-1}}{n+1} \) are new control points. The number of new control points in each row along the three sides of the triangle is increased. The points at the corners of the triangular mesh remain the same: \( p^*_{n+100} = p_{n00}, \ p^*_{0n+10} = p_{0n0}, \ p^*_{00n+1} = p_{00n} \). Relation (2.11.8) describes the same surface as relation (2.11.2) does, but via other control points.

Let a triangular Bezier surface be constructed on a set of control points \( p_{ijk} \) making up the triangular mesh shown in Fig. 2.11.1. Assign the weight \( w_{ijk} \) to each point \( p_{ijk} \).

The triangular rational Bezier surface is described by the vector function

$$ r(a,b,c) = \frac{\sum_{i,j,k=0}^{n} B^n_{ijk}(a,b,c)w_{ijk}p_{ijk}}{\sum_{i,j,k=0}^{n} B^n_{ijk}(a,b,c)w_{ijk}}, \quad (2.11.9) $$

$$ a \in [0,1], \quad b \in [0,1], \quad c \in [0,1], \quad a+b+c=1, $$

where the summation is performed over all control points. Because of (2.11.5), the Bezier surface (2.11.2) is a special case of a rational surface (2.11.9) on points of the same weights. The larger the weight of the point, the closer the surface passes to it. Recall that it is not the absolute value of the weight of each point but rather the ratio of the points' weights that provides this indication. If the weights of all characteristic points are the same, then we get an ordinary Bezier surface (2.11.2).

Fig. 2.11.4.
In terms of homogeneous coordinates, the extended radius vector (1.6.3) of the triangular Bezier surface is defined by

$$ R(a,b,c) = \sum_{i,j,k=0,i+j+k=n} B^n_{ijk}(a,b,c)w_{ijk}P_{ijk}, $$

where \( P_{ijk} = [w_{ijk}p_{ijk} w_{ijk}]^T \) are extended radius vectors of the control points of the surface. Fig. 2.11.4 shows a triangular Bezier surface, similar to the surface presented in Fig. 2.11.2, with the weight of its midpoint equal to four.

### 2.12. Homogeneous Divided Differences

Homogeneous divided differences are used to construct spline surfaces. Homogeneous simplex splines, analogous to B-splines, are constructed based on homogeneous divided differences.

Suppose we are given planar points \( p_1 = [u_1 v_1]^T \), \( p_2 = [u_2 v_2]^T \), and \( p_3 = [u_3 v_3]^T \). Let us recall that each lowercase letters in bold italics denote the point or vector in two-dimensional space. Each of the planar points gets the third coordinate in homogeneous coordinates. We denote the third coordinates as \( w_1, w_2, \) and \( w_3 \), respectively. Consider the function

$$
d(p_1, p_2, p_3) = \begin{vmatrix}
u_1 & u_2 & u_3 \\
v_1 & v_2 & v_3 \\
w_1 & w_2 & w_3
\end{vmatrix} =
w_1u_2v_3 + w_2u_3v_1 + w_3u_1v_2 - w_1v_2u_3 - w_2v_3u_1 - w_3v_1u_2.
$$  

(2.12.1)

We assume that all planar points have a third coordinate. This coordinate is the weight of the point, equal to unity unless otherwise stated. As you can see, if among the arguments of the function (2.12.1), two points are the same, or all three points lie on a straight line, then this function is zero. The function \( d(p_1, p_2, p_3) \) does not change under cyclic permutation of the points. When permuting two adjacent points, the function \( d(p_1, p_2, p_3) \) changes its sign. So this function has the properties:

$$
d(p, p, p) = d(p, p, q) = d(p, q, p) = d(q, p, p) = 0,
$$  

(2.12.2)

$$
d(p_1, p_2, p_3) = d(p_2, p_3, p_1) = d(p_3, p_1, p_2) = -d(p_2, p_1, p_3) = -d(p_1, p_3, p_2) = -d(p_3, p_2, p_1).
$$  

(2.12.3)

Function (2.12.1) is linear in each argument; i.e., for the point specified by (2.10.1) the following equality holds:

$$
d(r, q, \lambda_1p_1 + \lambda_2p_2 + \lambda_3p_3) = \lambda_1d(r, q, p_1) + \lambda_2d(r, q, p_2) + \lambda_3d(r, q, p_3).
$$  

(2.12.4)
Suppose there is a set of planar points \( p_1, p_2, \ldots, p_m, m \geq 3 \), and a function \( f(r, q, \ldots) \), whose arguments are the planar points. Let all points of the set be different and let no triples of points of the set lie on a straight line. We say that this set forms a normal sequence of points. Consider the relation

$$
\frac{f(p_i, p_j, \ldots)}{\prod_{n=1}^{m} d(p_i, p_j, p_n)}, \quad i \neq j.
$$

(2.12.5)

For the normal sequence, all the factors \( d(p_i, p_j, p_n) \) in (2.12.5) are non-zero. The relation (2.12.5) corresponds to the pair of points, \( p_i \) and \( p_j \). There are \( m-2 \) factors in the denominator (2.12.5). If the function \( f \) has the property

$$
f(r, q, \ldots) = (-1)^{m-2} f(q, r, \ldots),
$$

(2.12.6)

then the relation (2.12.5) does not change sign during permutation of points \( p_i \) and \( p_j \).

The homogeneous divided difference for function \( f(r, q, \ldots) \) with the property (2.12.6) on the sequence of points \( p_1, p_2, \ldots, p_m, m \geq 3 \) is determined by formula

$$
f[p_1, p_2, \ldots, p_m] = \sum_{i=1}^{m} \sum_{j=i+1}^{m} \frac{f(p_i, p_j, \ldots)}{\prod_{n=1}^{m} d(p_i, p_j, p_n)}.
$$

(2.12.7)

Denote the sequence of points \( p_1, p_2, \ldots, p_m \): \( P = \{p_1, p_2, \ldots, p_m\} \) and denote the divided difference \( f[p_1, p_2, \ldots, p_m] \) for the function \( f \) by \( f[P] \). Other notations can be also seen in the literature: \([p_1, p_2, \ldots, p_m]f\) and \([P]f\).

Homogeneous divided differences have the following properties.

**Property 1.** Since values of all the right-hand side terms in (2.12.7) are independent of the order of points \( p_i \) and \( p_j \), the divided difference is a symmetric function of its arguments; i.e., the value \( f[P] \) does not depend on the order of the points \( p_1, p_2, \ldots, p_m \) in the parameter list:

$$
f[P] = f[p_1, p_2, \ldots, p_m] = f[p_2, p_1, \ldots, p_m] = \ldots = f[p_m, p_1, \ldots, p_j].
$$

(2.12.8)

**Property 2.** If \( f(r, q, \ldots) = k_g g(r, q, \ldots) + k_h h(r, q, \ldots) \), then

$$
f[P] = k_g g[P] + k_h h[P],
$$

(2.12.9)

since every expression (2.12.5) consists of two components.

**Property 3.** Let point \( p \) belong to sequence \( P \). Then the divided difference of the function \( f(r, q, \ldots) = d(r, q, p) g(r, q, \ldots) \) is determined by the formula

$$
f[P] = g[P \setminus p],
$$

(2.12.10)
where $g[P \setminus p]$ is the divided difference for the function $g(r,q,...)$ on the sequence of points $P \setminus p$ obtained from the sequence $P$ by excluding the point $p$. Indeed, the summands

$$\frac{d(p_i, p_j, p) g(p_i, p_j, ...)}{\prod_{n=1}^{m} d(p_i, p_j, p_n)}, \quad i \neq j,$$

in which point $p$ is equal to $p_i$ or $p_j$, vanish due to (2.12.2). In the remaining summands, the similar non-zero multipliers $d(p_i, p_j, p)$ are canceled. Thereby the divided difference for the function $g(r,q,...)$ is calculated, and the sequence of points it is constructed on does not contain point $p$.

**Property 4.** This property is a consequence of the previous property. Let point $p$ be represented by relation (2.10.1) in terms of three points of the sequence $p_1, p_2, ..., p_m$:

$$p = \sum \lambda_i p_i, \quad \lambda_i \geq 0, \quad p_i \in P.$$  \hspace{1cm} (2.12.11)

Then the divided difference of the function $f(r,q,...)=d(r,q,p)g(r,q,...)$ is determined by the formula

$$f[P] = \sum \lambda_i g[P \setminus p_i],$$  \hspace{1cm} (2.12.12)

where $g[P \setminus p_i]$ is the divided difference for the function $g(r,q,...)$ on the sequence of points $P \setminus p_i$ obtained from the sequence $P$ by excluding the point $p_i$.

Given some non-intersecting domains in two-dimensional space, every planar point cannot belong to more than one domain. To determine to which of two-dimensional domains the point, of a line joining two domains, or coinciding with the point of junction of several domains, belongs, we introduce the concept of a **half-open convex hull**.

Let $[V]$ denote a convex hull completely covered by a convex polygon $V$, and $[V)$ denote a half-open convex hull of the polygon. Not all points on the edge of the convex hull $[V]$ belong to half-open convex hull $[V)$. The point $p=[u v]^T$ belongs to a half-open convex hull $[V)$ if there are $\varepsilon > 0$ and $\eta > 0$ such that the points $p=[u v]^T$, $p_1=[u+\varepsilon v]^T$, and $p_2=[u+\varepsilon v+\eta]^T$ belong to $[V)$.

Fig. 2.12.1 shows a half-open convex hull. For the domain shown in Fig. 2.12.1, inner points of the polygon and the points of the solid lines belong to $[V)$, and the points of dashed lines and the points of their junction with solid lines do not belong to $[V)$.
For the half-open convex hull \([V]\) and the point \(p\), define the function

$$
\delta_{[V]}(p) = \begin{cases} 
1, & \text{if } p \in [V] \\
0, & \text{if } p \notin [V]
\end{cases}
$$

determining whether the point \(p\) belongs to half-open convex hull or not.

Consider the power function of planar points

$$
f_n(r, q, p) = (d(r, q, p))^n \cdot d(r, q, x) \cdot \frac{\delta_{[r, q, x]}(p)}{|d(r, q, x)|},
$$

where \(x\) is an arbitrary planar point, \(\delta_{[r, q, x]}(p)\) is a function (2.12.13) specifying point \(p\)’s belonging to a half-open convex hull \([r, q, x]\) constructed on the triangle with vertices at points \(r, q,\) and \(x\).

Compute the homogeneous divided difference for the power function \(f_{m-3}(r, q, p)\) on the sequence of points \(P=\{p_1, p_2, \ldots, p_m\}\):

$$
f_{m-3}[P] = \sum_{i=1}^{m} \sum_{j=i+1}^{m} \frac{(d(p_i, p_j, p))^{m-3} \cdot d(p_i, p_j, x) \cdot \delta_{[p_i, p_j, x]}(p)}{\prod_{n=1, n \neq i, n \neq j}^{m} d(p_i, p_j, p_n)} \cdot \frac{\delta_{[p_i, p_j, x]}(p)}{|d(p_i, p_j, x)|}.
$$

Assign to this divided difference an order equal to the power of function (2.12.14) and introduce for it the notation: \(f_{m-3}[P]=M(p|p_1, p_2, \ldots, p_m)=M'(p)\).

Besides these properties, the homogeneous divided difference (2.12.15) of a power function of planar points has the following properties.

**Property 5.** At \(m=3\) the divided difference (2.12.15) takes the value

$$
M(p|p_1, p_2, p_3) = \begin{cases} 
\frac{1}{|d(p_1, p_2, p_3)|}, & \text{if } p \in [p_1, p_2, p_3] \\
0, & \text{if } p \notin [p_1, p_2, p_3]
\end{cases}
$$
Let us prove this assertion. On a sequence of three points \( p_1, p_2, p_3 \)

$$
M(p | p_1, p_2, p_3) = \frac{d(p_1, p_2, x)}{d(p_1, p_2, p_3)} \delta_{[p_1, p_2, x]}(p) + \frac{d(p_2, p_3, x)}{d(p_2, p_3, p_1)} \delta_{[p_2, p_3, x]}(p) + \frac{d(p_3, p_1, x)}{d(p_3, p_1, p_2)} \delta_{[p_3, p_1, x]}(p).
$$

Expressing the point \( x \) by the points of the sequence \( x = \lambda_1 p_1 + \lambda_2 p_2 + \lambda_3 p_3 \) and using the equality (2.12.4), we obtain

$$
M(p | p_1, p_2, p_3) = \lambda_3 \frac{\delta_{[p_1, p_2, x]}(p)}{\lambda_3 d(p_1, p_2, p_3)} + \lambda_1 \frac{\delta_{[p_2, p_3, x]}(p)}{\lambda_1 d(p_2, p_3, p_1)} + \lambda_2 \frac{\delta_{[p_3, p_1, x]}(p)}{\lambda_2 d(p_3, p_1, p_2)}. \tag{2.12.17}
$$

If the point \( x \) is inside the triangle with vertices at points \( p_1, p_2, \) and \( p_3 \), or on its boundary, then all \( \lambda_i \geq 0, i=1,2,3 \). There is no more than one non-zero term on the right-hand side of (2.12.17) (from the definition of the half-open convex hull), and we arrive at formula (2.12.16). If point \( x \) is outside the triangle with vertices at the points \( p_1, p_2, \) and \( p_3 \), barycentric coordinates \( \lambda_i, i=1,2,3 \), have different signs. In this case, there may be two, one, or no non-zero terms on the right-hand side of (2.12.17). There is one non-zero term, if the point \( p \) is inside the triangle with vertices at points \( p_1, p_2, \) and \( p_3 \), the corresponding \( \lambda_i > 0 \), and we again arrive at formula (2.12.16). Point \( p \) can be outside the triangle with vertices at points \( p_1, p_2, \) and \( p_3 \), but inside of two of the triangles with vertices at the points \( x, p_2, \) and \( p_3 \), with vertices at points \( p_1, x, \) and \( p_3 \), and with vertices at points \( p_1, p_2, \) and \( x \). In this case, two terms on the right-hand side of (2.12.17) are non-zero. If point \( p \) (like point \( x \)) is outside the triangle with vertices at the points \( p_1, p_2, \) and \( p_3 \), the corresponding \( \lambda_i \) have different signs and the divided difference is equal to zero. If point \( p \) is outside of the mentioned triangles, then all terms on the right-hand side of (2.12.17) are zero. Thus, in all cases, we come to the formula (2.12.16). The order-zero divided difference is a discontinuous constant function.

**Property 6.** At \( m>3 \), power function (2.12.14) is represented as \( f_k(r,q,p)=d(r,q,p)f_{k-1}(r,q,p) \), and point \( p \), with the help of (2.12.11), is expressed by three points of the sequence \( p_1, p_2, ..., p_m \). For function (2.12.15), property (2.12.12) takes the form

$$
M(p | p_1, p_2, ..., p_m) = \sum_i \lambda_i M(p | p_1, p_2, ..., p_m \setminus p_i), \tag{2.12.18}
$$

where \( M(p | p_1, p_2, ..., p_m \setminus p_i) \) is the divided difference of the function \( f_{m-4}(r,q,p) \) on the sequence of points obtained from the initial sequence by excluding point \( p_i \) from it. The expansion (2.12.18) does not depend on the choice of points used to describe point \( p \) in formula (2.12.11). When argument \( p \) of the divided difference (2.12.15) is equal to one of the points from sequence \( P \), from (2.12.18) it follows that
$$ M(p \mid p_1, p_2, \ldots, p_m) = M(p \mid p_1, p_2, \ldots, p_m \setminus p), \quad p \in P. $$ (2.12.19)

Repeatedly applying (2.12.18) to the right-hand side terms, we arrive at the conclusion that the divided difference is represented by the sum of non-zero divided differences (2.12.16) multiplied by the positive values of barycentric coordinates. The following properties follow from this fact.

**Property 7.** From properties (2.12.16) and (2.12.18) it follows that the divided difference (2.12.15) does not depend on the point \( x \).

**Property 8.** The divided difference (2.12.15) is a function of the point \( p \).

**Property 9.** For the sequence of points \( p_1, p_2, \ldots, p_m \) it is possible to construct a convex polygon \( V \) containing all points of the sequence whose vertices are also points of the sequence (some of the points of the sequence may lie inside polygon \( V \)). The divided difference (2.12.15) is non-zero on a half-open convex hull \([V]\) constructed for the given sequence \( p_1, p_2, \ldots, p_m \). In other words, the homogeneous divided differences for the power function are local functions. Their support is a half-open convex hull outlined by the given sequence of points.

**Property 10.** The divided difference (2.12.15) takes non-negative values.

**Property 11.** At \( m > 3 \) the divided difference (2.12.15) is equal to zero on the boundary of the convex hull \([V]\), constructed for the sequence \( p_1, p_2, \ldots, p_m \). Let us show this. If the point \( p \) coincides with one of the vertices of the convex hull \([V]\), then in accordance with (2.12.19), the divided difference is computed on the convex hull not containing the point \( p \), and it is equal to zero. Let \( p \) belong to the segment \( p_i p_j \) lying on the boundary of the convex hull \([V]\). Express the point \( p \) in terms of the points of the boundary segment and one more arbitrary point \( p_k \) of the sequence: \( p = \lambda_i p_i + \lambda_j p_j + \lambda_k p_k \) which does not coincide with any boundary segment points. Since point \( p \) lies on segment \( p_i p_j \), then \( \lambda_k = 0 \). Then in accordance with (2.12.18)

$$
M(p \mid p_1, p_2, \ldots, p_m) = \lambda_i M(p \mid p_1, p_2, \ldots, p_m \setminus p_i) + \lambda_j M(p \mid p_1, p_2, \ldots, p_m \setminus p_j).
$$

But the divided difference \( M(p \mid p_1, p_2, \ldots, p_m \setminus p_i) = 0 \) and the divided difference \( M(p \mid p_1, p_2, \ldots, p_m \setminus p_j) = 0 \) due to the fact that point \( p \) does not belong either to the half-open domain \([p_1, p_2, \ldots, p_m \setminus p_i)\), or to the half-open domain \([p_1, p_2, \ldots, p_m \setminus p_j)\). Indeed, if one excludes the point \( p_i \) or \( p_j \), which is the vertex of the polygon \( V \), from the convex hull \([V]\), then the newly obtained domain does not contain the interval \( p_i p_j \).

Consider the directional derivative of the function of planar points. Suppose we are given a planar unit vector \( t = [u_t, v_t, w_t]^T \) defining a certain direction, and the function \( f(p, \ldots) \), one of the arguments of which is a planar point \( p = [u_p, v_p, w_p]^T \). The expression

$$
\frac{\partial f}{\partial u_p} u_t + \frac{\partial f}{\partial v_p} v_t + \frac{\partial f}{\partial w_p} w_t = \frac{\partial f}{\partial t}
$$

is called the derivative of the function \( f(p, \ldots) \) along the direction of vector \( t \). The derivative of the function along direction \( t \) is a dot product of the gradient of function \( f(p, \ldots) \) and vector \( t \). We assume that the planar vectors have the third coordinate, the weight of the vector. Express the planar vector in three barycentric coordinates with
respect to three points with the help of (2.10.6). Then in the case of unit weights of the points, we find the weight of a planar vector to be zero, due to the (2.10.7). Then the derivative of the function $d(r,q,p)$ along direction $t$ with respect to parameter $p$ is equal to

$$\frac{\partial(d(r,q,p))}{\partial t} = d(r,q,t). \quad (2.12.20)$$

The derivatives of the function $d(r,q,p)$ along direction $t$ with respect to other parameters are determined similarly.

Let the planar unit vector $t$ be expressed by any three points in the form:

$$t = \sum_i \alpha_i p_i, \quad p_i \in P. \quad (2.12.21)$$

where $\alpha_i$ are barycentric coordinates (2.10.6) of the vector $t$. Then the derivative of the function $d(r,q,p)$ with respect to the last parameter along direction $t$ is equal to

$$\frac{\partial}{\partial t} d(r,q,p) = \sum_i \alpha_i d(r,q,p_i). \quad (2.12.22)$$

The directional derivative of the power function of the planar points (2.12.14) is a function similar to the power function itself. Indeed,

$$\frac{\partial(f_n(r,q,p))}{\partial t} = n(d(r,q,p))^{n-1} d(r,q,x) \cdot \delta_{[r,q,x]}(p) \cdot \frac{\partial(d(r,q,p))}{\partial t} =$$

$$= n(d(r,q,p))^{n-1} d(r,q,x) \cdot \delta_{[r,q,x]}(p) \cdot \sum_i \alpha_i d(r,q,p_i).$$

Let us find the derivative of the homogeneous divided difference $M(p | p_1, p_2, \ldots, p_m)$ with respect to argument $p$ along direction $t$. By analogy with (2.12.21), express vector $t$ by three arbitrary points of the sequence $p_1, p_2, \ldots, p_m$ and obtain

$$\frac{\partial}{\partial t} M(p | p_1, p_2, \ldots, p_m) =$$

$$=(m-3) \sum_{i=1}^m \sum_{j=i+1}^m \frac{(d(p_i, p_j, p))^{m-4} \cdot d(p_i, p_j, x)}{\prod_{n=1}^m d(p_i, p_j, p_n)} \delta_{[p_i, p_j, x]}(p) \frac{\partial d(p_i, p_j, p)}{\partial t} =$$

$$=(m-3) \sum_k \alpha_k M(p | p_1, p_2, \ldots, p_m \setminus p_k), \quad (2.12.23)$$
where \( M(p \mid p_1, p_2, \ldots, p_m \setminus p_k) \) is the divided difference for the function \( f_{m-4}(r, q, p) \) on the sequence of points obtained from the initial sequence by excluding points \( p_k \) from it. Indeed, after substituting (2.12.22), the terms

$$
\alpha_k(m-3) \frac{(d(p_i, p_j, p))^{m-4} \cdot d(p_i, p_j, x)}{\prod_{n=1, n \neq i, n \neq j}^m d(p_i, p_j, p_n)} \delta_{[p_i, p_j, x]}(p) \frac{d(p_i, p_j, p_k)}{d(p_i, p_j, x)}, \quad i \neq j, \quad p_k \in P
$$

with point \( p_k \) equal to \( p_i \) or \( p_j \) are zero, due to (2.12.2). In the remaining terms the same nonzero multipliers \( d(p_i, p_j, p_k) \) are canceled out.

Formula (2.12.23) shows that the derivative of a homogeneous divided difference is expressed in terms of lower-order divided differences. Formula (2.12.23) does not depend on the choice of points used to express vector \( t \).

### 2.13. Homogeneous Simplex Splines

We now define homogeneous simplex splines based on homogeneous divided differences. Equation (2.12.18) offers to forget about the homogeneous divided differences of the power function of planar points (2.12.15) and to define the homogeneous simplex spline for the sequence of planar points as a function computed by recurrence relation (2.12.18) with initial values of (2.12.16). Beside that we also extend the recurrence relation on the sequences with coincident points. The coincident points are called **multiple**. The homogeneous divided difference (2.12.16) with two or all three of the points upon which it was constructed on coincident is zero, due to the degeneracy of its half-open convex hull.

Homogeneous simplex splines are a generalization of the three-index Bernstein function, and they are analogs of B-splines. Surfaces can be constructed based on homogeneous simplex splines.

The **homogeneous simplex spline** of order \( n \) constructed on a sequence of points \( P = \{p_1, p_2, \ldots, p_m\}, m = n + 3 \), at least three of which do not lie on one line, is defined as a function computed by the recurrence relations

$$
M^P(p) = aM^{P_a}(p) + bM^{P_b}(p) + cM^{P_c}(p),
$$

at the initial values

$$
M^T(p) = \begin{cases} 
\frac{1}{|d(p_i, p_j, p_k)|}, & \text{if } p \in [p_i, p_j, p_k) \\
0, & \text{if } p \notin [p_i, p_j, p_k)
\end{cases}
$$
where \(a\), \(b\), and \(c\) are barycentric coordinates (2.10.4) of point \(p\) relative to points \(p_a\), \(p_b\), and \(p_c\). \(M^{p_a}(p)\), \(M^{p_b}(p)\), and \(M^{p_c}(p)\) are homogeneous simplex splines of order \((n-1)\) constructed on the sequences of points obtained from sequence \(P\) by excluding points \(p_a\), \(p_b\), and \(p_c\) respectively from it; \(M^0(p)\) is the order-zero homogeneous simplex spline constructed on three points \(p_a\), \(p_b\), and \(p_c\); and function \(d(p_a, p_b, p_c)\) is calculated by formula (2.12.1).

Points \(p_a\), \(p_b\), and \(p_c\) of the sequence of points \(P\) must not lie on one straight line or coincide. Such a triple of points in sequence \(P\) always exists, by definition. Points \(p_1\), \(p_2\), ..., \(p_m\) of the sequence are called knots. Computation of the value of the homogeneous simplex spline of \(n\)-th order begins with the computation of the values of homogeneous simplex splines of order-zero on the triangular domains. Suppose the vertices of the triangle \(T\) are the points \(p_a\), \(p_b\), and \(p_c\). The value of the order-zero homogeneous simplex spline in the triangular domain \(T\) is not zero, if domain \(T\) is non-degenerate and argument \(p\) belongs to the half-open convex hull \([p_a, p_b, p_c]\).

Let us construct for the sequence \(P=\{p_1, p_2, ..., p_m\}\), \(m \geq 3\) the convex polygon \(V\) with vertices at the points of the sequence. Construct it in such a way that all points of the given sequence belong to \([V]\). In the general case, some points of the given sequence lie at the vertices of the polygon \(V\), while others—on its sides, for example—are inside polygon \(V\). The half-open convex hull \([V]\) of polygon \(V\) is called the carrier or the domain of the homogeneous simplex spline \(M^0(p)\).

Let us pay attention to the analogy between the Cox-De Boor formula (1.8.7) and formula (2.13.1). Both formulas describe the recurrence relation for the \((m-\lambda)\)-th order spline constructed on the sequence of \(m\) knots, where \(\lambda\) is the number of barycentric coordinates. In both cases, the calculation starts with order-zero splines for \(\lambda\) distinct knots.

The homogeneous simplex spline (2.13.1) coincides with the homogeneous divided difference of the power function on a normal sequence of points \(P\). If there is a sequence of multiple knots, the computing algorithm for homogeneous simplex spline remains the same (2.12.18). The homogeneous simplex spline inherits the properties of the homogeneous divided difference of the power function.

**Property 1.** The order-zero homogeneous simplex spline is a discontinuous constant function of the point \(p\) position. The order-zero homogeneous simplex spline is a non-negative function within its triangular domain \(T\). If the vertices of triangle \(T\) coincide, or lie on one line, the order-zero homogeneous simplex spline \(M^0(p)\) is zero.

**Property 2.** The homogeneous simplex spline \(M^0(p)\) takes non-negative values. It differs from zero within its half-open convex hull \([V]\) and is zero outside of \([V]\).

**Property 3.** The result of formula (2.13.1) does not depend on the chosen triples of points \(p_a\), \(p_b\), and \(p_c\).

**Property 4.** The homogeneous simplex spline (2.13.1) is a function of point \(p\).

**Property 5.** The order-zero homogeneous simplex spline (2.13.1) is zero on the boundary of the convex hull \([V]\) constructed on the normal sequence \(p_1, p_2, ..., p_m\).

**Property 6.** In general, the homogeneous simplex spline of \(n\)-th order is a piecewise polynomial function of degree \(n\) having continuous derivatives up to the \((n-1)\)-th order. In our notation, the homogeneous simplex spline order is equal to the highest degree of the polynomials describing it.
We can calculate the derivative of the homogeneous simplex spline in the direction of a vector in the parameter plane. Suppose there is a unit planar vector \( t = [u \ v \ 0]^T \). With the help of formulas (2.10.9), this vector can be described via barycentric components \( \alpha, \beta, \gamma \) relative to the points \( p_a, p_b, p_c \) through the equation

$$
t = \alpha \ p_a + \beta \ p_b + \gamma \ p_c.
$$

In accordance with the derivative of the homogeneous divided difference (2.12.23), the derivative of a homogeneous simplex spline (2.13.1) in the direction of \( t \) is calculated by the formula

$$
\frac{\partial M^p(p)}{\partial t} = n \left( \alpha M^{p,a}(p) + \beta M^{p,b}(p) + \gamma M^{p,c}(p) \right).
$$  

(2.13.3)

The derivatives of the simplex \( n \)-th order splines are determined by the homogeneous simplex splines of \((n-1)\)-th order. Any three distinct knots of the differentiable homogeneous simplex spline that do not lie on one line can be taken as points \( p_a, p_b, p_c \).

We can express an arbitrary point \( p \) by a linear combination of all the points in sequence \( P \). That is, the expression (2.12.11) can be used in the form

$$
p = \sum_{i=1}^{m} \lambda_i \ p_i, \quad p_i \in P.
$$  

(2.13.4)

Then the formula (2.13.1) for calculation of the homogeneous simplex spline is symmetrical relative to the knots:

$$
M^p(p) = \sum_{i=1}^{m} \lambda_i \ M^{p,i}(p).
$$  

(2.13.5)

Similarly, we can represent unit vector \( t \) by a linear combination of all the knots. Then formula (2.13.3) for the derivative of the homogeneous simplex spline in the direction of \( t \) also has symmetrical form:

$$
\frac{\partial M^p(p)}{\partial t} = (m-3) \sum_{i=1}^{m} \alpha_i \ M^{p,i}(p).
$$  

(2.13.6)

Three-index Bernstein functions (2.11.3) are special cases of homogeneous simplex splines. The Bernstein function

$$
B_{ijk}^n(a,b,c) = \frac{n!}{i! \ j! \ k!} a^i b^j c^k
$$

up to the factor is a homogeneous simplex spline of \( n \)-th order constructed on a sequence of \((n+3)\) knots, among which \((i+1)\) knots coincide with point \( p_a, (j+1)\) knots
coincide with point $p_b$, and $(k+1)$ knots coincide with point $p_c$. Let points $p_a, p_b, p_c$ be the vertices of triangle $T$. We can construct

$$C_{n+2}^2 = \frac{(n+2)!}{2!n!} = \frac{(n+1)(n+2)}{2}$$

homogeneous simplex splines of $n$-th order on triangular domain $T$. These homogeneous simplex splines and the corresponding Bernstein functions are related by the equation

$$M_{ijk}(p) = \frac{1}{\Delta_{abc}} \frac{n!}{i!j!k!} a^ib^jc^k,$$

(2.13.7)

where $p = ap_a + bp_b + cp_c$, and $\Delta_{abc}$ is double the area of triangle $T$. Homogeneous simplex spline $M_{ijk}(p)$ is constructed on the following sequence of knots: $p_a$, of multiplicity $(i+1)$; $p_b$, of multiplicity $(j+1)$; and $p_c$, of multiplicity $(k+1)$.

Fig. 2.13.1 illustrates the order-zero homogeneous simplex spline constructed on a triangular domain (the homogeneous simplex spline value is measured in the direction perpendicular to the plane parameter of the spline).

Fig. 2.13.2 shows a first-order homogeneous simplex spline constructed on a rectangular domain.

Fig. 2.13.3 shows a first-order homogeneous simplex spline constructed on a triangular domain. Fig. 2.13.4 illustrates a second-order homogeneous simplex spline constructed on five distinct knots.
A sequence of homogeneous simplex spline points may contain multiple knots. In multiple knots, higher-order derivatives of the homogeneous simplex spline lose their smoothness. Fig. 2.13.5 shows a third-order homogeneous simplex spline constructed on six knots forming a triangular domain. There are two coinciding knots at each vertex of the triangular domain.

Fig. 2.13.5.

Some knots of a homogeneous simplex spline can lie inside its convex polygon. Fig. 2.13.6 shows a third-order homogeneous simplex spline constructed on six vertices, three of which lie at the vertices of the triangular domain, with the other three knots coincident at the center of this triangular domain. The derivatives at the center of such a spline lose continuity.

Fig. 2.13.6.

Fig. 2.13.7.

Fig. 2.13.8.
Some homogeneous simplex spline knots can lie on the boundary of its convex polygon. Fig. 2.13.7 shows a third-order homogeneous simplex spline constructed on six knots, five of which lie along the triangle's side. Fig. 2.13.8 shows a third-order homogeneous simplex spline constructed on six knots, four of which lie at one of the triangle vertices.

In places of knot concentration, the homogeneous simplex spline value is much larger than in elsewhere. If all knots of a homogeneous simplex spline are located at the vertices of a convex polygon, then the higher the order of the spline, the smaller the value of the spline in its central part. Fig. 2.13.9 shows a homogeneous simplex spline with knots located at the vertices of a regular octagon. Fig. 2.13.10 shows a fifth-order homogeneous simplex spline constructed on a quadrangular domain, with four knots within the quadrangular domain.

### 2.14. S-Spline Surfaces

Surfaces constructed using homogeneous simplex splines are called *S*-spline surfaces. They are constructed as a weighted sum of some control points. Each control point is included in the sum with a factor that is a function of planar point coordinates on the parametric domain of the surface. Each such function is nonzero on some bounded two-dimensional domain.

Consider the *S*-spline surface that uses third-order homogeneous simplex splines. For each control point, construct a third-order homogeneous simplex spline on six planar points located at the vertices of a regular hexagon (see Fig. 2.14.1).
The centers of the hexagons are arranged in a regular grid in which any three centers of the domains of adjacent homogeneous simplex splines are located at the vertices of an equilateral triangle. Centers of the domains of the homogeneous simplex splines and the domain boundary of one of them are shown in Fig. 2.14.2. Hexagonal areas of adjacent homogeneous simplex splines partly overlap:

![Fig. 2.14.2.](image)

The $S$-spline surface is described by the vector function

$$ r(p) = \frac{\sum_i M^p_i(p) w_i r_i}{\sum_i M^p_i(p) w_i}, $$

(2.14.1)

where $p=[u v]^T \in \Omega$.

The radius vector of the surface (2.14.1) is a function of parameters $u$ and $v$. The derivative of the vector function (2.14.1) with respect to the first parameter is calculated as follows:

$$ \frac{\partial r}{\partial u} = \frac{\sum_i \frac{\partial M^p_i(p)}{\partial t} w_i r_i}{\sum_i M^p_i(p) w_i} - \frac{\sum_i M^p_i(p) w_i r_i}{\left(\sum_i M^p_i(p) w_i\right)^2} \sum_i \frac{\partial M^p_i(p)}{\partial t} w_i, $$

where $t=[1 0]^T$. The derivative of vector function (2.14.1) with respect to the second parameter is calculated using a similar formula, with $t=[0 1]^T$. A fragment of the $S$-spline surface (2.14.1) and its control points are shown in Fig. 2.14.3.

One of the methods of constructing surfaces basing on homogeneous simplex splines was offered by W. Dahmen, C. Micchelli, and H. Seidel. Surfaces constructed by this method are called DMS-splines. The domain of a DMS-spline is a regular triangulation of some two-dimensional domain.
2.15. Surfaces Constructed on Other Surfaces

Surfaces can be constructed on the basis of other surfaces. Let us consider extended, offset, and reference surfaces. A surface used as the basis for construction of a new surface is called its base surface. A surface of a type similar to the type of the surface being constructed should not be used as a base surface.

An extended surface can be constructed on the basis of any surface by changing its parametric domains. Suppose it is required to extend the surface $b(u,v)$, $u_{\text{min}} \leq u \leq u_{\text{max}}$, and $v_{\text{min}} \leq v \leq v_{\text{max}}$, by expansion of its parametric domain to $a_u + u_{\text{min}} \leq u \leq u_{\text{max}} + b_u$, $a_v + v_{\text{min}} \leq v \leq v_{\text{max}} + b_v$. If $a_u \leq 0$, $a_v \leq 0$, $b_u \geq 0$, and $b_v \geq 0$, then the surface is expanded beyond its limits. If $a_u > 0$, $a_v > 0$, $b_u < 0$, and $b_v < 0$, then the surface is truncated.

If the surface is not cyclic and its expanded parameter goes beyond the domain, the surface can be continued in accordance with the calculation rule for the radius vector of the surface. Such surfaces include analytical surfaces and surfaces that are constructed on curves or surfaces based on the radius vector calculation.

In the general case, when there is no rule for the behavior of a non-cyclic surface outside of its domain, continue the surface along a tangent to the nearest boundary and calculate the necessary geometric characteristics using the extended surface. The radius vector of the extended surface is calculated by the formulas

$$r(u,v) = b(u,v),$$

(2.15.1)

if $u_{\text{min}} \leq u \leq u_{\text{max}}, v_{\text{min}} \leq v \leq v_{\text{max}}$;

$$r(u,v) = b(u_0,v) + (u - u_0) \frac{\partial b}{\partial u} \bigg|_{u_0,v},$$

if $v_{\text{min}} \leq v \leq v_{\text{max}},$ and the parameter $u$ is beyond the boundary value $u_0$;

$$r(u,v) = b(u,v_0) + (v - v_0) \frac{\partial b}{\partial v} \bigg|_{u,v_0},$$

if $u_{\text{min}} \leq u \leq u_{\text{max}},$ and the parameter $v$ is beyond the boundary value $v_0$;
$$ r(u,v) = b(u_0, v_0) + (u - u_0) \frac{\partial b}{\partial u} \bigg|_{u_0, v_0} + (v - v_0) \frac{\partial b}{\partial v} \bigg|_{u_0, v_0} + (u - u_0)(v - v_0) \frac{\partial^2 b}{\partial u \partial v} \bigg|_{u_0, v_0}, $$

if parameters \( u \) and \( v \) are beyond boundary values \( u_0 \) and \( v_0 \), respectively.

Boundary value \( u_0 \) is \( u_{\text{min}} \) or \( u_{\text{max}} \); boundary value \( v_0 \) is \( v_{\text{min}} \) or \( v_{\text{max}} \). Fig. 2.15.1 shows the extended surface and its base surface (indicated by thin lines).

![Fig. 2.15.1.](image)

If the surface is cyclic with respect to any of the parameters, then, if this parameter is beyond its domain, perform a cyclic recalculation. If surface \( b(u,v) \) is cyclic with respect to the first parameter, the radius vector of the extended surface is calculated by the formula

$$ r(u,v) = b(u - p_u \cdot \Phi((u - u_{\text{min}})/p_u), v), \tag{2.15.2} $$

where \( p_u \) is the period of the parameter of the base surface, and \( \Phi(w) \) is a function that computes the largest integer not exceeding \( w \). If surface \( b(u,v) \) is cyclic with respect to the second parameter, the radius vector of the extended surface is calculated by the formula

$$ r(u,v) = b(u, v - p_v \cdot \Phi((v - v_{\text{min}})/p_v)), \tag{2.15.3} $$

where \( p_v \) – period of the second parameter of the base surface, \( \Phi(w) \) – function that computes the largest integer not exceeding \( w \).

Other extended surface should not be used as a base surface for the extended surface. Instead, one should use the base surface of the former with the corresponding recalculation of parameters \( a_u, a_v, b_u, b_v \).

Formulas (2.15.1) – (2.15.3) can be used to calculate the radius vector of the surface and its derivatives when the parameters of the surface are outside of their domain.

An offset surface is described by the vector function

$$ r(u,v) = b(u,v) + h m(u,v), \tag{2.15.4} $$

$$ u, v \in \Omega, $$
where $b(u,v)$ is the base surface, $h$ is the distance from the base surface, $m(u,v)$ is the normal of the base surface, and $\Omega$ is the parametric domain of the base surface. The normal $m(u,v)$ has unit length and the direction of vector $b_u \times b_v$. The parametric domain of the offset surface $\Omega$ may coincide with the parametric domain of the base surface, and can be extended in accordance with the rules of construction of the extended surface. Fig. 2.15.2 shows an offset surface and its base surface (indicated by the thin lines).

![Fig. 2.15.2.](image)

You should not use another offset surface as the base surface for an offset surface one; rather, use its base surface, recalculating its offset length. That is, if it is required to construct an offset surface at distance $h_2$ from another offset surface $r_1(u,v) = b(u,v) + h_1 m(t)$, then surface $b(u,v)$ should be used as the base surface while setting the offset length equal to $h = h_2 + h_1$.

A reference surface is a surface every point of which is obtained by a transformation of the corresponding point of the base surface. The reference surface is described by the vector function

$$r(u,v) = M \cdot b(u,v),$$

$$u, v \in \Omega,$$

(2.15.5)

where $b(u,v), u,v \in \Omega$ are the base surface, $\Omega$ is the parametric domain of the base surface, and $M$ is the extended transformation matrix (1.15.7) of the base surface. When working with the extended matrix, we assume that the radius vectors are used in the form (1.15.8), and the free vectors are used in the form (1.15.9). The parametric domain of the reference surface coincides with the parametric domain of the base surface. The reference surface can be used to work with surface $b(u,v)$ described in some local Cartesian coordinate system in the global Cartesian coordinate system.

Do not use another reference surface as the base surface for the reference surface; instead, take its base surface, with a corresponding recalculation of the transformation matrix. For example, if it is required to construct a reference surface on the basis of a reference surface $r'(u,v) = M' \cdot b(u,v)$, then the surface $b(u,v)$ should be used as the base surface, and the transformation matrix obtained as a product of matrices $M'M'$.
2.16. Supple Surfaces

To correct the form of a surface, you can base a supple surface on it. We call the initial surface on which the supple surface is constructed the base surface.

A supple surface is an offset surface with a variable distance from the base surface. It is described by the vector function

$$ r(u,v) = b(u,v) + h(u,v) m(u,v), $$  

(2.16.1)

where \( b(u,v) \) is the base surface, \( h(u,v) \) is transformation function of the surface, and \( m(u,v) \) is the normal of the base surface. The parametric domain of a supple surface coincides with the domain of the base surface. The normal \( m(u,v) \) has unit length, and is directed along the vector \( b_u \times b_v \). The function \( h(u,v) \) specifies the way the surface is deformed along its normal. At points where \( h(u,v) \) is zero, the supple surface coincides with the base surface. If \( h(u,v) \) is constant, then the supple surface coincides with the offset surface.

The function of the surface deformation \( h(u,v) \) is defined by

$$ h(u,v) = \sum_{i=0}^{n} \sum_{j=0}^{m} N_i^l(v) N_j^k(u) h_{ij}, $$  

(2.16.2)

where \( N_i^l(v) \) and \( N_j^k(u) \) are B-splines (1.8.1), and \( h_{ij}, i=0,1,...,n, j=0,1,...,m \) is the collection of surface deviations at points located at the nodes of a rectangular grid having \( n+1 \) rows, with \( m+1 \) points in each row. The deformation function \( h(u,v) \) is similar to vector function (2.8.1) describing the B-spline surface. The only difference between the deformation function \( h(u,v) \) and function (2.8.1) is that function (2.8.1) is a vector function and determined by the control points \( p_{ij} \), while the deformation function is a scalar function, determined by the deviations \( h_{ij} \) of the surface along the normal to the given points.

B-splines \( N_j^k(u) \) are constructed on the non-decreasing sequence of \( k+2 \) knots \( u_j, u_{j+1},..., u_{j+k-1} \). B-splines \( N_i^l(v) \) are constructed on the non-decreasing sequence of \( l+2 \) knots \( v_i, v_{i+1},..., v_{i+l-1} \). For a base surface open with respect to the first (second) parameter, the first and last \( k+1 \) (\( l+1 \)) knots of the sequence must coincide. For a base surface cyclic closed with respect to the first (second) parameter, the corresponding sequence of knots should reflect the closedness: The first \( 2k(2l) \) knots must go through intervals repeating the intervals at which the last \( 2k(2l) \) knots go. The knot values should be consistent with the minimum and maximum parameters of the base surface. Let the knot numbering start with zero; then \( u_k = u_{\min}, u_{m+k+1} = u_{\max}, v_l = v_{\min}, \) and \( v_{n+l+1} = v_{\max} \), where \( u_{\min} \) and \( u_{\max} \) are the minimum and maximum values of the first parameter of the base surface, and \( v_{\min} \) and \( v_{\max} \) are the minimum and maximum values of the second parameter of the base surface. Fig. 2.16.1 shows a cylindrical surface; Fig. 2.16.2 shows a supple surface constructed on the basis of the cylindrical surface.
Generalization of the supple surface is the surface described by the vector function

$$ r(u, v) = b(u, v) + \sum_{i=0}^{n} \sum_{j=0}^{m} N_i^j(v) N_k^j(u) s_{ij}, $$

where \( s_{ij}, i=0,1,...,n, j=0,1,...,m \) is the collection of surface deviations at points located at the nodes of a rectangular grid having \( n+1 \) rows, with \( m+1 \) points in each row. The deviation \( s_{ij} \) is a vector in a local coordinate system with basis \( b_1, b_2, m \) at the node of a rectangular grid, where \( b_1 = \frac{\partial b(u,v)}{\partial u} \) and \( b_2 = \frac{\partial b(u,v)}{\partial v} \) are the partial derivatives with respect to the parameters of the base surface, \( m=m(u,v) \) is the normal of the base surface at the node.

### 2.17. Surface Based on Triangulation

Suppose we have a set of control points in a space on which we can build a triangulation. The term 'triangulation' denotes a connected polyhedral surface formed by a set of triangular plates joined to one another along their common sides. The vertices of the plates are the control points of the set. The triangular plates should not intersect each other. No more than one triangular plate may be joined to any side of each triangular plate. Sides of triangular plates having no neighbors are called boundary sides.

Now that we have constructed a triangulation on the specified control points, construct a two-dimensional triangulation in some parameter space of the surface we are creating. The two-dimensional triangulation must be synchronized with the spatial triangulation. A planar point must correspond to each control point, and a two-dimensional triangle in the parameter space must correspond to each flat plate in the two-dimensional space. Two-dimensional triangles should also be joined by common sides and must not intersect with each other. The surface based on this triangulation is a mapping of the two-dimensional triangulation in the parametric domain of this surface onto the three-dimensional space.
Now let us replace the flat triangular plates by curvilinear triangular surfaces joined to one another along their common curves. To do this at each control point, we define the common normal for all the triangular plates joining at this point. You can take the average of the normals of the plates joined at a given point as a normal at the control point. The sides of the triangular plates are curved in such way that they approach its control points in a direction perpendicular to the normals at these points.

Fig. 2.17.1 shows the curved side of the triangle connecting control points \( p_i \) and \( p_j \). The curved side of the triangle is described by a cubic Hermite spline (1.3.10), which in this case takes the form

$$
r_{ij}(t) = p_i(1-3t^2+2t^3) + p_j(3t^2-2t^3) + v_{ij}(t-2t^2+t^3) - v_{ji}(c-t^2+t^3),
$$

where \( 0 \leq t \leq 1 \). In (2.17.1) vectors \( v_{ij} \) and \( v_{ji} \) are equal to vectors \( p_j-p_i \) and \( p_i-p_j \), with subtracted components along normals \( m_i \) and \( m_j \) respectively:

$$
v_{ij} = (p_j-p_i) - m_i(m_i \cdot (p_j-p_i)), \quad v_{ji} = (p_i-p_j) - m_j(m_j \cdot (p_i-p_j)).
$$

Replace the flat triangular plates by the curvilinear triangular surfaces (2.10.11) each constructed on three curves (2.17.1). Fig. 2.17.2 shows the triangular surface

$$
r_{ijk}(a,b,c) = a(r_k(1-b)+r_j(c)-p_i) + b(r_j(1-c)+r_k(a)-p_k) + c(r_j(1-a)+r_k(b)-p_j),
$$

\( 0 \leq a \leq 1, \quad 0 \leq b \leq 1, \quad 0 \leq c \leq 1, \quad a+b+c=1, \)

constructed on three curves \( r_{ij}(t), r_{jk}(t) \) and \( r_{ki}(t) \) describing the sides of curvilinear triangle \( p_i p_k p_j \).

Fig. 2.17.2.
Arguments \(a\), \(b\), and \(c\) of triangular surface (2.17.2) are the barycentric coordinates (2.10.4) of a planar point in the parametric space of the surface. The barycentric coordinates \(a\), \(b\), and \(c\) of planar point \(p\) are calculated using two-dimensional points \(p_i = [u_i \ v_i]^T\), \(p_k = [u_k \ v_k]^T\), and \(p_j = [u_j \ v_j]^T\) corresponding to control points \(p_i\), \(p_k\), and \(p_j\), so

$$
p = a p_i + b p_k + c p_j.
$$

A surface based on the triangulation consists of the curvilinear triangles (2.17.2) joined to one another along their common curves. The internal data of the surface consists of a set of control points in the space, the corresponding set of surface normals at these control points, and a set of planar points in the parametric domain of the surface corresponding to the control points and a set of triangles. Each triangle is described by three numbers of vertices from the set of control points.

You can construct a surface based on a triangulation of any surface with rectangular parameter domains. To do this, fill the rectangular parametric domain with two-dimensional triangles joined along their common edges, whose vertices do not intersect each other. We compute the control point and its normal for each vertex of the two-dimensional triangulation. Using these data, we construct the surface based on the triangulation approximating the original surface.

### 2.18. Surface with Arbitrary Boundary

In the general case, the parametric domain of a surface is described by two-dimensional closed composite curves; i.e., by two-dimensional contours. The contour segments can be any two-dimensional curves except composite curves. The beginning of each subsequent contour segment coincides with the end of the previous segment. In the general case, the derivatives of the contour are discontinuous with respect to length and direction at the junctions of the segments.

Let the two-dimensional contour \(c(t)\) contain \(n\) segments \(r_i(w_i)\), where \(w_{i\text{min}} \leq w_i \leq w_{i\text{max}}\) and \(i = 1, 2, \ldots, n\). The initial value of the contour parameter is set to zero. The parametric length of the contour is set equal to the sum of parametric lengths of its constituent segments

$$
t_{\text{min}} = 0, \quad t_{\text{max}} = \sum_{i=1}^{n} (w_{i\text{max}} - w_{i\text{min}}).
$$

In calculating the radius vector of the contour, you must first define the segment to which the value of the contour parameter corresponds. The number of the segment \(k\) to which the given contour parameter \(t\) corresponds is found from the condition

$$
\sum_{i=1}^{k-1} (w_{i\text{max}} - w_{i\text{min}}) \leq t < \sum_{i=1}^{k} (w_{i\text{max}} - w_{i\text{min}}).
$$
The corresponding value of the intrinsic parameter $w_k$ of the found segment is determined by the formula

$$w_k = w_{k\min} + t - \sum_{i=1}^{k-1} (w_{i\max} - w_{i\min}).$$

The radius vector of the two-dimensional contour for the given parameter $t$ is equal to the radius vector of the found segment:

$$r(t) = r_k(w_k).$$

Using a contour, you can describe the boundary of a two-dimensional domain of any form and size.

A surface whose boundary is two-dimensional contours is called a **curve-bounded surface**. A curve-bounded surface is the most general case of a surface, and it consists of some surface and a set of two-dimensional contours. A curve-bounded surface can be constructed on the basis of any other surface. The initial surface is called a **base surface**. Let $b(u,v)$ be a radius vector of the base surface. The radius vector of a curve-bounded surface is described by the same law as the base surface, but with a different parametric domain

$$r(u,v) = b(u,v),$$

$$u, v \in \Omega,$$

where $\Omega$ is the parametric domain, which is a two-dimensional connected domain. In general, the parametric domain $\Omega$ of the curve-bounded surface $r(u,v)$ may extend beyond the parametric domain of the base surface $b(u,v)$. Outside of the parametric domain of the base surface, the radius vector $r(u,v)$ is calculated in accordance with the rules of construction of the extended surface.

Let the domain boundaries of the surface $\Omega$ be described by $m$ two-dimensional contours $c_j(t_j)=[u_j(t_j) \ v_j(t_j)]^T$, $t_{j\min} \leq t_j \leq t_{j\max}$, $j=1,2,...,m$. We require that the boundary contours satisfy the following conditions: Contours should not intersect with themselves or with each other. One of the contours must contain all the other contours within the domain it encloses. The encompassing contour is called the **external contour**, and the contours lying inside of it are called **internal contours**. The internal contours cannot be nested within each other. To determine the position of a planar point relative to the surface parametric domain quickly, the contours are oriented, so that when moving along the border, the surface is always on the same side. Let the external contour be oriented so that its path-tracing is carried out in the anti-clockwise direction when viewed from the surface towards its normal; then the inner contours should be oriented in the opposite direction.

A simple example of the curve-bounded surface is the plane bounded by one contour $c(t)$. The plane passing through point $p$ and parallel to orthonormal basis vectors $i_x$ and $i_y$ is described by the vector function

$$r(u,v) = p + u i_x + v i_y,$$

$$u, v \in \Omega.$$
The boundary of the domain $\Omega$ is described by one two-dimensional contour $c(t)=[u(t)$ $v(t)]^T$, $t_{\text{min}} \leq t \leq t_{\text{max}}$. The boundary of the considered plane is described by three-dimensional curve

$$r(t) = p + u(t) i_x + v(t) i_y,$$

$t_{\text{min}} \leq t \leq t_{\text{max}}.$

Fig. 2.18.1 shows a spline surface having a rectangular parametric domain and closed composite curves on it. Fig. 2.18.2 shows a surface bounded by contours constructed on the basis of the spline surface.

![Fig. 2.18.1](image1)

![Fig. 2.18.2](image2)

You should not use a curve-bounded surface as the base surface for the curve-bounded surface; instead, use its base surface. Curve-bounded surfaces must be constructed after all the others. For example, if it is required to construct an offset surface for a curve-bounded surface, then the offset surface based on the base surface $b(u,v)$ should first be constructed, and then the curve-bounded surfaces should be constructed based on the offset surface.

**Exercises**

1. Calculate the length of one turn of a cylindrical helix.
2. Calculate the curvature of the latitude circles on the globe using the Meusnier Theorem.
3. Describe the surface of a torus with an elliptical section by a vector function.
4. Express the surface of a torus with an elliptical section as a B-spline surface.
5. Describe the part of the plane bounded by an ellipse by a vector function.