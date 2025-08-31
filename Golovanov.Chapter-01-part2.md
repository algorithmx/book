Construction of the family of the \( n+1 \) \( m \)-th-order B-splines of an open B-spline curve requires \( n+m+2 \) knots. The sequence of knots \( t_0, t_1, \ldots, t_{m+n+2} \) a B-spline curve is constructed on is called a knot vector. The shape of a B-spline curve depends not only on the location of its control points, but also on the knot values. In order to demonstrate the dependence of the curve shape on the knot values, we construct two B-spline curves of the same order on the same control points, but with different knot vectors.

Fig. 1.9.1 shows two B-curves and a polyline constructed on the same control points. The cubic B-spline curve with knot vector 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 is indicated in Fig. 1.9.1 by a solid line. The cubic B-spline curve with knot vector 0, 1, 11, 12, 22, 23, 33, 34, 44, 45, 55 is shown in Fig. 1.9.1 by a dashed line. Two different non-decreasing sequences of eleven numbers were taken as knot vectors. A polyline constructed on the control points of the B-spline curve is shown in Fig. 1.9.1 as a thin line.

Fig. 1.9.2 shows a cubic B-spline curve constructed on control points similar to those used for the B-spline curve shown in Fig. 1.9.1. But this time, the knot vector is 0, 0, 0, 0, 1, 2, 3, 4, 4, 4, 4. The B-spline curve shown in Fig. 1.9.2 has multiple knots at both ends of the knot vector and therefore passes through its end control points. To make an open curve pass through its first and last control point, the first B-spline should have the first \( m+1 \) of the \( m+2 \) knots upon which it is constructed be multiple, and the last B-spline should have the last \( m+1 \) of the \( m+2 \) knots upon which it is constructed be multiple. That is, for an open B-spline curve passing through its endpoints, the following equalities should be satisfied: \( t_0 = t_1 = \ldots = t_m \) and \( t_{n+1} = t_{n+2} = \ldots = t_{n+m+1} \). The parameter of a B-spline curve varies from knot value \( t_{\text{min}} = t_m \) to knot value \( t_{\text{max}} = t_{n+1} \).

The construction of a family of \( n+1 \) \( m \)-th order B-splines of a periodic closed B-spline curve requires \( n+2m+2 \) knots (the knot vector must be extended by \( m \) knots).
The sequence of knots should reflect the closedness: The first $2m$ knots must be separated by intervals similar to the intervals separating the last $2m$ knots. That is, for a closed B-spline curve, equalities $t_1 - t_0 = t_{n+2} - t_{n+1}$, $t_2 - t_1 = t_{n+3} - t_{n+2}$, ..., $t_{2m+1} - t_{2m} = t_{n+2m+2} - t_{n+2m+1}$ must be satisfied. Fig. 1.9.3 shows a periodic closed cubic B-spline curve with knot vector $-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11$ and a polyline constructed on eight control points of the B-spline curve.

![Fig. 1.9.3.](image)

The parameter of periodic closed B-spline curves varies from knot value $t_{\text{min}} = t_m$ to knot value $t_{\text{max}} = t_{n+m+1}$. The number of knots of a B-spline curve is always greater than the number of its control points; that’s why the knot vector is called an extended knot vector.

B-spline curves constructed on knot vectors that do not have multiple knots, or have them only at the beginning and at the end of the knot vector (for open curves), have continuous derivatives up to order $(m-1)$ over the entire domain. If a knot vector contains multiple knots in places other than the boundary, then the continuity of the corresponding curve derivatives is broken.

In accordance with the Cox-De Boor formula (1.8.5), the scheme for calculating one B-spline $N_j^m(t)$ formally looks like (the order of the B-spline increases from top to bottom, and knot numbers increase from left to right):

$$
\begin{align*}
N_j^0(t) & \quad N_{j+1}^0(t) \quad \ldots \quad N_{j+m-2}^0(t) \quad N_{j+m-1}^0(t) \quad N_{j+m}^0(t) \\
N_j^1(t) & \quad N_{j+1}^1(t) \quad \ldots \quad N_{j+m-2}^1(t) \quad N_{j+m-1}^1(t) \\
N_j^2(t) & \quad N_{j+1}^2(t) \quad \ldots \quad N_{j+m-2}^2(t) \\
\ldots & \quad \ldots \quad \ldots \\
N_j^{m-1}(t) & \quad N_{j+1}^{m-1}(t) \\
N_j^m(t)
\end{align*}
$$

Among all B-splines of nonzero order (1.8.13), only one is nonzero for any value of parameter $t$. Therefore, to calculate the radius vector of the B-spline curve, the following scheme is used. Using the parameter value $t$ and conditions $t_i \leq t < t_{i+1}$, the number $i$ of nonzero B-splines of order zero is determined, and the value of unnormalized B-spline curve is calculated:
$$ M_i^0(t) = \frac{1}{t_{i+1} - t_i}. $$  

(1.9.3)

Then, using the recurrence Cox-De Boor relation,

$$ M_j^m(t) = \frac{t_{j+m+1} - t}{t_{j+m+1} - t_j} M_{j+1}^{m-1}(t) + \frac{t - t_j}{t_{j+m+1} - t_i} M_j^{m-1}(t), $$  

(1.9.4)

all unnormalized B-splines nonzero at a given parameter \( t \) are consequently computed up to \( m \)-th order (the B-spline order increases downwards, and knot numbers increase from left to right):

$$
\begin{array}{cccc}
M_i^0(t) & M_{i-1}^1(t) & M_i^1(t) \\
M_{i-2}^2(t) & M_{i-1}^2(t) & M_i^2(t) \\
\vdots & \vdots & \vdots \\
M_{i-m+1}^{m-1}(t) & M_{i-2}^{m-1}(t) & M_{i-1}^{m-1}(t) & M_i^{m-1}(t) \\
M_{i-m}^m(t) & M_{i-m+1}^m(t) & M_{i-2}^m(t) & M_{i-1}^m(t) & M_i^m(t)
\end{array}
$$

This triangular table is calculated line by line, because the first-row element is known from (1.9.3), and each element of the next row can be constructed from two adjacent elements of the previous row using (1.9.4). When calculating the outer elements of each row, we use the fact that one of the elements in the previous row (missing in the table) is equal to zero. After this, B-splines are normalized

$$ N_j^m(t) = (t_{j+m+1} - t_j) M_j^m(t), \quad j = i - m, i - m + 1, \ldots, i $$

and substituted into the formula (1.9.1), which for \( t_i \leq t < t_{i+1} \) takes the form

$$ r(t) = \sum_{j=i-m}^{i} N_j^m(t) w_j p_j \sum_{j=i-m}^{i} N_j^m(t) w_j. $$

Using the relations (1.58), we can carry out simultaneous calculation of the B-splines and their derivatives. This calculation is used in iterative processes of intersection of curves.

Suppose for the parametric value \( t \), the number \( i \) of knot \( t_i \) is determined from the condition \( t_i \leq t < t_{i+1} \). Nonzero B-splines at a given parameter value \( t \) are: \( N_{i-m}^m(t), \)
Let us differentiate the numerator of the right-hand side of (1.9.1), taking into account (1.8.15). We obtain

$$
\frac{d(\text{wr})}{dt} = \frac{d}{dt} \left( \sum_{j=i-m}^{i} N_j^m w_j p_j \right) = \sum_{j=i-m}^{i} \frac{dN_j^m}{dt} w_j p_j =
$$

$$
m \sum_{j=i-m}^{i} N_j^{m-1} \frac{w_j p_j}{t_{j+m} - t_j} - m \sum_{j=i-m+1}^{i} N_j^{m-1} \frac{w_j p_j}{t_{j+m+1} - t_{j+1}} =
$$

$$
= mN_{i-m}^{m-1} \frac{w_{i-m} p_{i-m}}{t_i - t_{i-m}} + m \sum_{j=i-m+1}^{i} N_j^{m-1} \frac{w_j p_j}{t_{j+m} - t_j} -
$$

$$
- mN_{i+1}^{m-1} \frac{w_{i+1} p_{i+1}}{t_{i+1} - t_{i+1}} - m \sum_{j=i-m+1}^{i} N_j^{m-1} \frac{w_j p_j}{t_{j+m} - t_j} =
$$

$$
= m \sum_{j=i-m+1}^{i} N_j^{m-1} \frac{w_j p_j - w_{j-1} p_{j-1}}{t_{j+m} - t_j} = \sum_{j=i-m+1}^{i} N_j^{m-1} p_j^{(1)},
$$

where the following notation is introduced

$$
p_j^{(1)} = m \frac{w_j p_j - w_{j-1} p_{j-1}}{t_{j+m} - t_j}, \quad j = 1,2,...,n.
$$

In equation (1.9.5) we used the properties \( N_{i-m}^{m-1}(t) = 0 \) and \( N_{i+1}^{m-1}(t) = 0 \) for \( t_i \leq t < t_{i+1} \). Equation (1.9.5) shows that the first derivative of the function \( \sum_{j=i-m}^{i} N_j^m w_j p_j \) is a function similar to \( \sum_{j=i-m+1}^{i} N_j^{m-1} p_j^{(1)} \), with the order and number of terms less by one. Continuing the differentiation, we can find the derivative of the desired order for the numerator of the expression (1.9.1)

$$
\frac{d^k(\text{wr})}{dt^k} = \frac{d^k}{dt^k} \left( \sum_{j=0}^{n} N_j^m w_j p_j \right) = \sum_{j=k}^{n} N_j^{m-k} p_j^{(k)},
$$

where \( p_j^{(k)} = (m + 1 - k) \frac{p_j^{(k-1)} - p_{j-1}^{(k-1)}}{t_{j+m+1-k} - t_j} \), \( k = 1,2,...,m \), \( j = k,k+1,...,n \),

\( p_j^{(0)} = w_j p_j \). For the derivatives of the denominator (1.9.1) we get an expression similar to (1.9.6),

$$
\frac{d^k w}{dt^k} = \frac{d^k}{dt^k} \left( \sum_{j=0}^{n} N_j^m w_j \right) = \sum_{j=k}^{n} N_j^{m-k} w_j^{(k)},
$$
where \( w_j^{(k)} = (m + 1 - k) \frac{w_j^{(k-1)} - w_{j-1}^{(k-1)}}{t_{j+m+1-k} - t_j}, \quad k = 1, 2, \ldots, m, \quad j = k, k+1, \ldots, n, \)

\( w_j^{(0)} = w_j. \)

The radius vector of a B-spline curve (1.9.1) is calculated as a quotient of two functions of the curve parameter \( t \). So when we calculate the derivative of a B-spline curve, the right-hand side of (1.9.1) should be considered as a composite function, the first derivative of which is equal to

$$
\frac{d r}{dt} = \frac{d}{dt} \left( \frac{wr}{w} \right) = \frac{1}{w} \frac{d(wr)}{dt} - \frac{wr}{w^2} \frac{dw}{dt},
$$

(1.9.8)

where

\( wr = \sum_{j=0}^{n} N_j^m(t) w_j p_j \) – numerator of the right-hand side of (1.9.1),

\( w = \sum_{j=0}^{n} N_j^m(t) w_j \) – denominator of the right-hand side of (1.9.1),

$$
\frac{d(wr)}{dt} = m \sum_{j=1}^{n} N_j^{m-1}(t) \frac{w_j p_j - w_{j-1} p_{j-1}}{t_{j+m} - t_j} $$ – derivative of the numerator,

$$
\frac{dw}{dt} = m \sum_{j=1}^{n} N_j^{m-1}(t) \frac{w_j - w_{j-1}}{t_{j+m} - t_j} $$ – derivative of the denominator.

In the same manner we calculate higher-order derivatives of the B-spline curve:

$$
\frac{d^{(k)} r}{dt^{(k)}} = \frac{d^{(k)}}{dt^{(k)}} \left( \frac{wr(t)}{w(t)} \right).
$$

It should be noted that the radius vector of a point and its weight (\( wr \) or \( w_j p_j \)) in the formulas for the B-spline curve appear as a single entity.

### 1.10. De Boor’s Algorithm

Let us use formula (1.8.12) to transform the numerator of expression (1.9.1) as follows:

$$
wr(t) = \sum_{j=0}^{n} N_j^m w_j p_j = \sum_{j=-m}^{i} N_j^m w_j p_j =
$$

$$
= \sum_{j=-m}^{i} \left( \frac{t_{j+m+1} - t}{t_{j+m+1} - t_{j+i}} N_{j+1}^{m-1} + \frac{t - t_j}{t_{j+m} - t_j} N_j^{m-1} \right) w_j p_j =
$$
$$ \frac{t_{i+m+1} - t}{t_{i+m} - t_j} N_{i+1}^{m-1} w_j p_i + \sum_{j=i-m+1}^{i} \frac{t_{j+m} - t}{t_{j+m} - t_j} N_{j}^{m-1} w_j p_{j-1} + \frac{t_{i+m} - t}{t_{i+m} - t_j} N_{i}^{m-1} w_j p_j = \sum_{j=i-m+1}^{i} N_{j}^{m-1} \left( \frac{t_{j+m} - t}{t_{j+m} - t_j} w_j p_{j-1} + \frac{t - t_j}{t_{j+m} - t_j} w_j p_j \right) = \sum_{j=i-m+1}^{i} N_{j}^{m-1} r_j^{(1)}, \tag{1.10.1} $$

where we introduce the notation

$$ r_j^{(1)} = \frac{t_{j+m} - t}{t_{j+m} - t_j} w_j p_{j-1} + \frac{t - t_j}{t_{j+m} - t_j} w_j p_j. $$

In (1.10.1) we use the fact that for \( t_i \leq t < t_{i+1} \) only \( N_{i-m}^m(t), N_{i-m+1}^m(t), \ldots, N_i^m(t) \) are nonzero, and also use equalities \( N_{i-m}^{m-1}(t) = 0 \) and \( N_i^{m-1}(t) = 0 \). We reduce the sum of \( m+1 \) terms to a sum of \( m \) terms and lower the order of the B-splines in this sum by one.

To further simplify the numerator of (1.9.1) in a similar way, we obtain

$$ wr(t) = \sum_{j=0}^{n} N_j^m w_j p_j = \sum_{j=i-m}^{i} N_j^m w_j p_j = \sum_{j=i-m+1}^{i} N_j^{m-1} r_j^{(1)} = \sum_{j=i-m+2}^{i} N_j^{m-2} r_j^{(2)} = \ldots = \sum_{j=i-m+m}^{i} N_j^0(t) r_j^{(m)} = r_i^{(m)}, \tag{1.10.2} $$

where we introduce the notation \( r_j^{(0)} = w_j p_j, r_j^{(k)} = \frac{t_{j+m+1-k} - t}{t_{j+m+1-k} - t_j} r_{j-1}^{(k-1)} + \frac{t - t_j}{t_{j+m+1-k} - t_j} r_j^{(k-1)}, \)

for \( k \) ranging from 1 to \( m \). We obtain a similar expression for the denominator of (1.9.1)

$$ w(t) = \sum_{j=0}^{n} N_j^m w_j = \sum_{j=i-m}^{i} N_j^m w_j = \sum_{j=i-m+1}^{i} N_j^{m-1} w_j^{(1)} = \sum_{j=i-m+2}^{i} N_j^{m-2} w_j^{(2)} = \ldots = \sum_{j=i-m+m}^{i} N_j^0(t) w_j^{(m)} = w_i^{(m)}, \tag{1.10.3} $$

where we introduce the notation \( w_j^{(0)} = w_j, w_j^{(k)} = \frac{t_{j+m+1-k} - t}{t_{j+m+1-k} - t_j} w_{j-1}^{(k-1)} + \frac{t - t_j}{t_{j+m+1-k} - t_j} w_j^{(k-1)}, \)

for \( k \) changing from 1 to \( m \).

We concluded that the position of the point of the B-spline curve (1.9.1) for a given parameter \( t_i \leq t < t_{i+1} \) can be determined by the formula
$$ r(t) = \frac{w_r(t)}{w(t)} = \frac{r_i^{(m)}}{w_i^{(m)}} $$ (1.10.4)

using recurrence relations

$$
\begin{align*}
r_j^{(k)} &= \frac{t_{j+m+1-k} - t}{t_{j+m+1-k} - t_j} r_{j-1}^{(k-1)} + \frac{t - t_j}{t_{j+m+1-k} - t_j} r_j^{(k-1)}, \\
w_j^{(k)} &= \frac{t_{j+m+1-k} - t}{t_{j+m+1-k} - t_j} w_{j-1}^{(k-1)} + \frac{t - t_j}{t_{j+m+1-k} - t_j} w_j^{(k-1)},
\end{align*}
$$

starting with values \( r_j^{(0)} = w_j p_j \), \( w_j^{(0)} = w_j \). These relations are generalization of De Casteljau's algorithm, and are called De Boor's algorithm.

$$
\begin{array}{ccccccc}
r_{i-m}^{(0)} & r_{i-m+1}^{(0)} & r_{i-m+2}^{(0)} & \ldots & r_{i-2}^{(0)} & r_{i-1}^{(0)} & r_i^{(0)} \\
r_{i-m+1}^{(1)} & r_{i-m+2}^{(1)} & \ldots & r_{i-2}^{(1)} & r_{i-1}^{(1)} & r_i^{(1)} \\
r_{i-m+2}^{(2)} & \ldots & r_{i-2}^{(2)} & r_{i-1}^{(2)} & r_i^{(2)} \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
r_{i-2}^{(m-2)} & r_{i-1}^{(m-2)} & r_i^{(m-2)} \\
r_{i-1}^{(m-1)} & r_i^{(m-1)} \\
r_i^{(m)}
\end{array}
$$

Fig. 1.10.1.

An algorithm for calculating the radius vector of the point of the B-spline curve for parameter \( t_i \leq t < t_{i+1} \) is illustrated in Fig. 1.10.1.

### 1.11. Point and Knot Insertion in a B-Spline Curve

The number of knots and control points of a B-spline curve can be increased, while keeping the shape and parametric length of the curve the same. Let us insert an additional knot \( v \) into a sequence of knots \( t_0, t_1, \ldots, t_{m+n+2} \) of the curve (1.9.2).

Let the value \( v \) satisfy the conditions \( t_{\min} < v < t_{\max} \) and let it not coincide with any of the knots of the \( m \)-th-order B-spline curve. We can find the number \( i \) of the knot \( t_i \) from the condition \( t_i \leq v < t_{i+1} \) and construct the sequence of knots \( v_0 = t_0, v_1 = t_1, \ldots, v_i = t_i, \)
The new curve must have the number of its knots and control points increased by one. The radius vector of the new curve is described by the formula

$$ r(t) = \sum_{j=0}^{n+1} N_j^m(t) q_j . $$

The B-splines of the new curve are denoted by the underlined symbols. Because of knot values the following equalities will hold:

$$ N_j^m(t) = \underline{N}_j^m(t), \quad j = 0, 1, \ldots, i - m - 1, $$
$$ N_j^m(t) = \underline{N}_{j+1}^m(t), \quad j = i + 1, i + 2, \ldots, n, $$
$$ N_j^m(t) = \frac{v_{j+m+2} - v}{v_{j+m+2} - v_j} \underline{N}_{j+1}^m(t) + \frac{v - v_j}{v_{j+m+2} - v_j} \underline{N}_j^m(t), \quad j = i - m, i - m + 1, \ldots, i. $$

For unnormalized B-splines the last equation has the form

$$ M_j^m(t) = \frac{v_{j+m+2} - v}{v_{j+m+2} - v_j} M_{j+1}^m(t) + \frac{v - v_j}{v_{j+m+2} - v_j} M_j^m(t), \quad j = i - m, i - m + 1, \ldots, i. $$ (1.11.1)

Equation (1.11.1) is proved by induction. Direct substitution shows that equality (1.11.1) holds for unnormalized B-spline curves of order zero:

$$ \frac{1}{t_{i+1} - t_i} = \frac{v_{i+2} - v}{v_{i+2} - v_i} \frac{1}{v_{i+2} - v_{i+1}}. $$

Suppose that (1.11.1) holds for unnormalized B-splines of order \((m-1)\). We need to make sure that it also holds for an unnormalized order-\(m\) B-spline under this assumption. To do this we substitute (1.11.1) for \(M_{j+1}^{m-1}(t)\) and \(M_j^{m-1}(t)\) in (1.8.5) and obtain

$$ M_j^m(t) = \frac{t_{j+m+1} - t}{t_{j+m+1} - t_j} \left( \frac{v_{j+m+2} - v}{v_{j+m+2} - v_j} M_{j+2}^{m-1}(t) + \frac{v - v_j}{v_{j+m+2} - v_j} M_{j+1}^{m-1}(t) \right) + $$
$$ + \frac{t - t_j}{t_{j+m+1} - t_j} \left( \frac{v_{j+m+1} - v}{v_{j+m+1} - v_j} M_{j+1}^{m-1}(t) + \frac{v - v_j}{v_{j+m+1} - v_j} M_j^{m-1}(t) \right) = $$
$$ = \frac{t_{j+m+1} - t}{t_{j+m+1} - t_j} \frac{v_{j+m+2} - v}{v_{j+m+2} - v_j} M_{j+2}^{m-1}(t) + \frac{t - t_j}{t_{j+m+1} - t_j} \frac{v_{j+m+1} - v}{v_{j+m+1} - v_j} M_{j+1}^{m-1}(t) + $$
$$ + \frac{t_{j+m+1} - t}{t_{j+m+1} - t_j} \frac{v - v_j}{v_{j+m+2} - v_j} M_{j+1}^{m-1}(t) + \frac{t - t_j}{t_{j+m+1} - t_j} \frac{v - v_j}{v_{j+m+1} - v_j} M_j^{m-1}(t). $$

In the second and the third terms, we make the substitution using the equality
$$
\frac{(t-t_j)(v_{j+m+1}-v)}{v_{j+m+1}-v_j} + \frac{(t_{j+m+1}-t)(v-v_{j+1})}{v_{j+m+2}-v_{j+1}} = \frac{(v_{j+m+2}-v)(t-v_{j+1})}{v_{j+m+2}-v_{j+1}} + \frac{(v-v_j)(v_{j+m+1}-t)}{v_{j+m+1}-v_j},
$$

which can be verified by direct calculation. After substitution we get:

$$
M_j^m(t) = \frac{v_{j+m+2}-v}{v_{j+m+2}-v_j} M_{j+2}^{m-1}(t) + \frac{v_{j+m+2}-v}{v_{j+m+2}-v_j} \frac{t-v_{j+1}}{v_{j+m+2}-v_{j+1}} M_{j+1}^{m-1}(t) +
\frac{v-v_j}{v_{j+m+2}-v_j} \frac{v_{j+m+1}-t}{v_{j+m+1}-v_j} M_{j+1}^{m-1}(t) + \frac{v-v_j}{v_{j+m+2}-v_j} \frac{t-v_j}{v_{j+m+2}-v_j} M_j^{m-1}(t) =
\frac{v_{j+m+2}-v}{v_{j+m+2}-v_j} M_{j+1}^{m}(t) + \frac{v-v_j}{v_{j+m+2}-v_j} M_j^{m}(t),
$$

which completes the proof.

For the new curve, we must have

$$
\sum_{j=0}^{n} N_j^m(t)p_j = \sum_{j=0}^{n+1} N_j^m(t)q_j.
$$

From independence of B-splines, we obtain equalities

$$
p_j = q_j, \quad j = 0, 1, \ldots, i-m-1,
$$
$$
p_j = q_{j+1}, \quad j = i+1, i+2, \ldots, n,
$$
$$
\sum_{j=i-m}^{i} N_j^m(t)p_j = \sum_{j=i-m}^{i+1} N_j^m(t)q_j.
$$

Let us insert the expression for a B-spline of the curve (1.9.2) in terms of the B-spline of the new curve into the last equality

$$
\left( \frac{v_{i+2}-v}{v_{i+2}-v_{i-m+1}} N_{i-m+1}^m(t) + \frac{v-v_{i-m}}{v_{i+1}-v_{i-m}} N_{i-m}^m(t) \right) p_{i-m} +
\left( \frac{v_{i+3}-v}{v_{i+3}-v_{i-m+2}} N_{i-m+2}^m(t) + \frac{v-v_{i-m+1}}{v_{i+2}-v_{i-m+1}} N_{i-m+1}^m(t) \right) p_{i-m+1} +
\ldots +
\left( \frac{v_{i+m+2}-v}{v_{i+m+2}-v_{i+1}} N_{i+1}^m(t) + \frac{v-v_i}{v_{i+m+1}-v_i} N_i^m(t) \right) p_i =
N_{i-m}^m(t)q_{i-m} + N_{i-m+1}^m(t)q_{i-m+1} + \ldots + N_i^m(t)q_i + N_{i+1}^m(t)q_{i+1}.
$$

After regrouping terms, we obtain
$$ N_{i-m}^m(t)(q_{i-m} - p_{i-m}) + N_{i-m+1}^m(t)\left( q_{i-m+1} - \frac{v-t_{i-m+1}}{t_{i+1}-t_{i-m+1}}p_{i-m+1} - \frac{t_{i+1}-v}{t_{i+1}-t_{i-m+1}}p_{i-m} \right) + \ldots + N_i^m(t)\left( q_i - \frac{v-t_i}{t_{i+m}-t_i}p_i - \frac{t_{i+m}-v}{t_{i+m}-t_i}p_{i-1} \right) + N_{i+1}^m(t)(q_{i+1} - p_i) = 0. $$

We now introduce the notation \( \alpha_j = \frac{v-t_j}{t_{j+m}-t_j} \) for \( j = i-m+1, i-m+2, \ldots, i \) and derive the equations expressing the control points of new curve through the control points \( p_j \):

$$
\begin{align*}
q_j &= p_j, & j &= 0, 1, \ldots, i-m, \\
q_j &= \alpha_j p_j + (1-\alpha_j)p_{j-1}, & j &= i-m+1, i-m+2, \ldots, i, \\
q_{j+1} &= p_j, & j &= i+1, i+2, \ldots, n.
\end{align*}
$$

To insert the knot \( v \) (\( t_i \leq v < t_{i+1} \)) into the curve (1.9.1), the control points in the obtained equalities must be multiplied by their weights. The weights of the control points of the new curve are expressed in terms of the weights of the control points of the original curve by similar formulas:

$$
\begin{align*}
w_j &= w_j, & j &= 0, 1, \ldots, i-m, \\
w_j &= \alpha_j w_j + (1-\alpha_j)w_{j-1}, & j &= i-m+1, i-m+2, \ldots, i, \\
w_{j+1} &= w_j, & j &= i+1, i+2, \ldots, n.
\end{align*}
$$

The inserted knot may coincide with a knot existing in the sequence of knots of the B-spline curve—for example, \( v = t_i \). Thus, the new knot can be inserted several times, provided it does not exceed the order of multiplicity of the B-spline curve.

### 1.12. Examples of B-Spline Curves

As an illustration, let us construct B-spline curves on \( n+1 \) control points with knots of integer values. Parameterization with equidistant values of knots is called uniform.

Let the first \( m+1 \) knots of an open B-spline curve have zero values: \( t_0 = t_1 = \ldots = t_m = 0 \); let the next \( n-m \) knots have integer values from 1 to \( n-m \): \( t_{n+1} = i, i=1, 2, \ldots, n-m \); and let the remaining \( m+1 \) knots be set to \( n-m+1 \): \( t_{n+1} = t_{n+2} = \ldots = t_{n+m+1} = n-m+1 \). The parameter of the open B-spline curve varies from \( t_m = 0 \) to \( t_{n+1} = n-m+1 \). Fig. 1.12.1 shows a set of cubic B-spline curves constructed on an extended sequence of knots 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 6, 6, 6 for nine control points.
A B-spline curve constructed on these points and its control polyline are shown in Fig. 1.12.2. Similar to the Bezier curve, the B-spline curve does not pass through its control points except at its endpoints. The parameter $t$ of the curve shown in Fig. 1.12.2 takes values in the interval $0 \leq t \leq 6$.

Let the knots of a closed periodic B-spline curve be: $t_i = i - m$, $i = 0, 1, 2, ..., n + 2m + 1$. The parameter of the closed B-spline curve takes values from $t_m = 0$ to $t_{n+m+1} = n + 1$. Fig. 1.12.3 shows a set of cubic B-splines constructed on an extended sequence of knots $-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9$ for six control points. For a closed curve, all B-splines are similar to each other.

A closed periodic B-spline curve constructed on these points and its control polyline are shown in Fig. 1.12.4. The parameter of the curve shown in Fig. 1.12.4 takes values in the interval $0 \leq t \leq 6$.
Fig. 1.12.4.

Fig. 1.12.5 shows the B-spline curves of the first, third, fifth, and seventh order constructed on the same eight control points. One can see in Fig. 1.12.5 that the higher order of the curve the smoother it is. The first order B-spline curve coincides with the control polyline.

Fig. 1.12.6 illustrates the influence of control point weight $p_4$ on the shape of the fifth-order curve (the weights of the other control points are equal to 1).

The greater the weight of a vertex, the closer to it the B-spline curve passes. In general, the weight of a vertex may be zero or negative. In practice, B-spline curves of the second and third order are most frequently used.

1.13. B-Spline Curves and Bezier Curves

Let us show that Bezier curves are special cases of B-spline curves. To do this we
modify the B-spline indexing. We assign an index equal to index of the first knot to a B-spline. Similarly, a B-spline curve can be assigned an index equal to the index of the last knot.

We define a B-spline with its index being equal to the last knot in the sequence on which it is constructed. Using this B-spline we will construct B-spline curves and derive De Boor's algorithm for them.

In addition to (1.8.1) we define a B-spline of order \( m \) constructed on a non-decreasing sequence of knots \( t_{i-m-1}, t_{i-m}, \ldots, t_i \) by the equality

$$
N^m_i(t) = (t_i - t_{i-m-1}) \sigma_m[t_{i-m-1}, t_{i-m}, \ldots, t_i].
$$  

(1.13.1)

Alongside (1.8.2) we define the unnormalized B-spline of order \( m \) constructed on a non-decreasing sequence of knots \( t_{i-m-1}, t_{i-m}, \ldots, t_i \) by the equality

$$
M^m_i(t) = \sigma_m[t_{i-m-1}, t_{i-m}, \ldots, t_i].
$$  

(1.13.2)

We noted earlier that a B-spline may be associated with any knot of the sequence it is constructed on by its subscript index. In formulas (1.13.1) and (1.13.2) B-spline index \( i \) points to the last knot of the sequence, and is located after the index \( m \) characterizing the B-spline order. From the definitions it follows that \( N_{i-m-1}^m(t) = N^m_i(t) \) and \( M_{i-m-1}^m(t) = M^m_i(t) \).

With definition (1.13.1) most of the B-spline's properties remain unchanged, because the divided difference does not depend on the way knots on which it is constructed are ordered. There will be some changes in recurrence relations bounded to the non-decreasing sequence of knots \( t_{i-m-1}, t_{i-m}, \ldots, t_i \) that is used in the B-spline curves.

If we reduce all indexes in (1.8.4) by \( m+1 \), we get

$$
\sigma_m[t_{i-m-1}, t_{i-m}, \ldots, t_i] = \frac{t_i - t}{t_i - t_{i-m-1}} \sigma_{m-1}[t_{i-m}, t_{i-m+1}, \ldots, t_i] + \frac{t - t_{i-m-1}}{t_i - t_{i-m-1}} \sigma_{m-1}[t_{i-m-1}, t_{i-m}, \ldots, t_{i-1}].
$$

Let us write the last equation using the definition (1.13.2) and obtain the Cox-De Boor formula for unnormalized B-splines associated with the last knot of the sequences they are constructed on:

$$
M^m_i(t) = \frac{t_i - t}{t_i - t_{i-m-1}} M^{m-1}_{i-1}(t) + \frac{t - t_{i-m-1}}{t_i - t_{i-m-1}} M^{m-1}_{i-1}(t).
$$  

(1.13.3)

Recurrence relation (1.13.3) begins with unnormalized B-splines of order zero:

$$
M^0_j(t) = \begin{cases} 
\frac{1}{t_j - t_{j-1}}, & \text{if } t_{j-1} \leq t < t_j, \\
0, & \text{in other cases}
\end{cases}
$$  

(1.13.4)
Using the equality \( N^m_i = (t_i - t_{i-m-1})M^m_i(t) \), we obtain the Cox-De Boor formula for B-splines associated with the last knot of non-decreasing sequences on which they are constructed from (1.13.1):

$$
N^m_i(t) = \frac{t_i - t}{t_i - t_{i-m}} N^{m-1}_i(t) + \frac{t - t_{i-m-1}}{t_{i-1} - t_{i-m-1}} N^{m-1}_{i-1}(t).
$$  

(1.13.5)

A recurrence relation (1.13.5) begins with B-splines of order zero

$$
N^0_j(t) = \begin{cases} 
1, & \text{if } t_{j-1} \leq t < t_j \\
0, & \text{otherwise}
\end{cases}.
$$

(1.13.6)

Using the definition of the divided difference (1.7.2) we obtain

$$
N^m_i = (t_{i-m-1} - t_i) \sigma_m[t_{i-m}, t_{i-m+1}, \ldots, t_i] =
\sigma_m[t_{i-m}, t_{i-m+1}, \ldots, t_i] - \sigma_m[t_{i-m-1}, t_{i-m}, \ldots, t_{i-1}].
$$

(1.13.7)

We calculate the derivative of the B-spline \( N^m_i(t) \) with the help of (1.13.7):

$$
\frac{dN^m_i(t)}{dt} = \frac{d\sigma_m[t_{i-m}, t_{i-m+1}, \ldots, t_i]}{dt} - \frac{d\sigma_m[t_{i-m-1}, t_{i-m}, \ldots, t_{i-1}]}{dt}.
$$

Substituting the derivatives of the truncated power function with respect to \( t \)

$$
\frac{d\sigma_m}{dt} = -m(z - t)^{m-1}_+ = -m\sigma_{m-1},
$$

in the last expression we get

$$
\frac{dN^m_i(t)}{dt} = -m\sigma_{m-1}[t_{i-m}, t_{i-m+1}, \ldots, t_i] + m\sigma_{m-1}[t_{i-m-1}, t_{i-m}, \ldots, t_{i-1}] =
-mM^{m-1}_i(t) + mM^{m-1}_{i-1}(t) =
-\frac{m}{t_i - t_{i-m}} N^{m-1}_i(t) + \frac{m}{t_{i-1} - t_{i-m-1}} N^{m-1}_{i-1}(t).
$$

(1.13.8)

Similarly, we obtain the formula for the derivative of the unnormalized B-spline \( M^m_i(t) \)

$$
\frac{dM^m_i(t)}{dt} = m \frac{M^{m-1}_{i-1}(t) - M^{m-1}_i(t)}{t_i - t_{i-m-1}}.
$$

Suppose we are given an infinite (or long enough) non-decreasing sequence of knots \( t_i \) and a B-spline of order \( m \) is constructed on every \( m+2 \) consecutive knots. By
definition (1.13.1), only \( m+1 \) B-splines are nonzero at any \( t_{i-1} < t < t_i \)—namely, \( N^m_i(t) \), \( N^m_{i+1}(t) \), ..., \( N^m_{i+m}(t) \)—and their sum is equal to 1. It is necessary to use (1.13.7) instead of (1.8.9) in formula (1.8.10) in order to prove this property.

B-splines \( N^m_{i-m}(t) \) and \( N^m_i(t) \) constructed on the same sequence of knots coincide; therefore, the B-spline curve (1.9.1) coincides with the curve

$$
r(t) = \frac{\sum_{j=0}^{n} N^m_j(t) w_j p_j}{\sum_{j=0}^{n} N^m_j(t) w_j}
$$

(1.13.9)

after decreasing indexes for all knots of the curve (1.9.1) by \( m+1 \). Curve (1.13.9) is distinguished from curve (1.9.1) only by recurrence relations used to calculate the radius vector and the derivatives of the curve.

The \( k \)-th derivative of the numerator on the right-hand side of (1.13.9) is

$$
\frac{d^k(w r)}{dt^k} = \frac{d^k}{dt^k} \left( \sum_{j=0}^{n} N^m_j w_j p_j \right) = \sum_{j=0}^{n-k} N^{m-k}_j p^{(k)}_j ,
$$

(1.13.10)

where \( p^{(k)}_j = (m + 1 - k) \frac{p^{(k-1)}_{j+1} - p^{(k-1)}_j}{t_j - t_{j-m-1+k}} , \quad k = 1,2,...,m , \quad j = 0,1,...,n-k , \quad p^{(0)}_j = w_j p_j . \)

The \( k \)-th derivative of the denominator on the right-hand side of (1.13.9) is

$$
\frac{d^k w}{dt^k} = \frac{d^k}{dt^k} \left( \sum_{j=0}^{n} N^m_j w_j \right) = \sum_{j=0}^{n-k} N^{m-k}_j w^{(k)}_j ,
$$

(1.13.11)

where \( w^{(k)}_j = (m + 1 - k) \frac{w^{(k-1)}_{j+1} - w^{(k-1)}_j}{t_j - t_{j-m-1+k}} , \quad k = 1,2,...,m , \quad j = 0,1,...,n-k , \quad w^{(0)}_j = w_j . \)

Proofs of (1.13.10) and (1.13.11) are similar to the proofs of (1.9.6) and (1.9.7).

Let us transform the numerator of (1.13.9) using the formula (1.13.5) as follows:

$$
w r(t) = \sum_{j=0}^{n} N^m_j w_j p_j = \sum_{j=i}^{i+m} N^m_j w_j p_j =
$$

$$
= \sum_{j=i}^{i+m-1} N^{m-1}_j \left( \frac{t_j - t}{t_j - t_{j-m}} w_j p_j + \frac{t - t_{j-m}}{t_j - t_{j-m}} w_{j+1} p_{j+1} \right) = \sum_{j=i}^{i+m-1} N^{m-1}_j r^{(1)}_j =
$$

$$
= \sum_{j=i}^{i+m-2} N^{m-2}_j \left( \frac{t_j - t}{t_j - t_{j-m+1}} r^{(1)}_j + \frac{t - t_{j-m+1}}{t_j - t_{j-m+1}} r^{(1)}_{j+1} \right) =
$$

$$
= \sum_{j=i}^{i+m-2} N^{m-2}_j r^{(2)}_j = \ldots = \sum_{j=i}^{i+m-m} N^0_j(t) r^{(m)}_j = r^{(m)}_i ,
$$
where we introduced the notation \( r^{(0)}_j = w_j p_j \), \( r^{(k)}_j = \frac{t_j - t}{t_j - t_{j-m-1+k}} r^{(k-1)}_j + \frac{t - t_{j-m-1+k}}{t_j - t_{j-m-1+k}} r^{(k-1)}_{j+1} \)

for \( k \) in the range from 1 to \( m \). For the denominator of (1.13.9), we obtain a similar expression

$$
w(t) = \sum_{j=1}^{i+m} N^m_j w_j = \sum_{j=1}^{i+m-1} N^{m-1}_j w^{(1)}_j = \sum_{j=1}^{i+m-2} N^{m-2}_j w^{(2)}_j = \ldots = w^{(m)}_i ,
$$

where we introduced the notation \( w^{(0)}_j = w_j \), \( w^{(k)}_j = \frac{t_j - t}{t_j - t_{j-m-1+k}} w^{(k-1)}_j + \frac{t - t_{j-m-1+k}}{t_j - t_{j-m-1+k}} w^{(k-1)}_{j+1} \)

for \( k \) in the range from 1 to \( m \).

We have developed De Boor's algorithm for calculating the radius vector of the point of the B-spline curve (1.13.9) in determining B-splines (1.13.1) for the parameter \( t_{i-1} \leq t < t_i \)

$$
r(t) = \frac{w r(t)}{w(t)} = \frac{r^{(m)}_i}{w^{(m)}_i} ,
$$

where \( r^{(m)}_i \) and \( w^{(m)}_i \) are calculated using recurrence relations

$$
r^{(k)}_j = \frac{t_j - t}{t_j - t_{j-m-1+k}} r^{(k-1)}_j + \frac{t - t_{j-m-1+k}}{t_j - t_{j-m-1+k}} r^{(k-1)}_{j+1} ,
$$

$$
w^{(k)}_j = \frac{t_j - t}{t_j - t_{j-m-1+k}} w^{(k-1)}_j + \frac{t - t_{j-m-1+k}}{t_j - t_{j-m-1+k}} w^{(k-1)}_{j+1} ,
$$

starting with \( r^{(0)}_j = w_j p_j \), \( w^{(0)}_j = w_j \).

The B-spline curves (1.9.1) and (1.13.9) are equivalent and their only difference lies in the choice between the definition of B-splines as in (1.8.1) or as in (1.13.1).

Consider the special case of B-spline curve for which B-splines of \( n \)-th order \( N^n_i(t) \), \( i=0,1,\ldots,n \) are constructed on a sequence of knots \( t_{-1-n}=t_{-n}=\ldots=t_{-1}=0 \), \( t_0=t_1=\ldots=t_n=1 \). Recurrence relation (1.13.3) for such a sequence takes the form

$$
M^n_i(t) = (1-t) M^{n-1}_i(t) + t M^{n-1}_{i-1}(t) .
$$

Since every B-spline is nonzero on the interval \( 0 \leq t \leq 1 \), then B-splines are related by

$$
N^n_i(t) = (1-t) N^{n-1}_i(t) + t N^{n-1}_{i-1}(t) ,
$$

which starts with B-spline \( N^0_0(t) = 1 \). Comparing the obtained recurrence relation with (1.4.4), we arrive at the conclusion that \( N^n_i(t) = B^n_i(t) \) on the sequence of knots \( t_{-1-n}=
$t_n = \ldots = t_{n-1} = 0$, $t_0 = t_1 = \ldots = t_n = 1$. The equality of the special case of the B-splines $N^n_i(t)$ and the Bernstein functions $B^n_i(t)$ implies an equality of the special case of the B-spline curve (1.13.9) and the rational Bezier curve (1.6.2). As $N_{i-n-1}^n(t) = N^n_i(t)$ B-splines $N^n_i(t)$ are equal to Bernstein functions $B^n_i(t)$ on the sequence of knots $t_0 = t_1 = \ldots = t_n = 0$, $t_{n+1} = t_{n+2} = \ldots = t_{2n+1} = 1$, and therefore the special case of the B-spline curve (1.9.1) coincides with the rational Bezier curve (1.6.2). Thus, we see that the B-spline curve is a generalization of the Bezier curve.

### 1.14. Special Cases of B-Spline Curves

Construct two first-order B-splines on the sequence of knots $t_0 = t_1 = 0$, $t_2 = t_3 = 1$

$$N_0^1(t) = \frac{t_2 - t}{t_2 - t_1} N_1^0(t) = 1 - t,$$

$$N_1^1(t) = \frac{t - t_1}{t_2 - t_1} N_1^0(t) = t.$$

The B-spline curve (1.9.2) based on these B-splines is a line segment

$$r(t) = N_0^1 p_0 + N_1^1 p_1 = (1 - t)p_0 + tp_1,$$

joining the points $p_0$ and $p_1$.

If we construct the B-spline curve (1.9.2) with $n+1$ vertices on the sequence of knots $t_0 = t_1 < t_2 < \ldots < t_{n+1} = t_{n+2}$ based on the B-splines of the first order, it will be a polyline. The domain of the parameter of the B-spline curve in this case is $t_1 \leq t \leq t_{n+2}$. B-splines of the first order are defined by equality

$$N_i^1(t) = \begin{cases} \frac{t - t_i}{t_{i+1} - t_i}, & \text{if } t_i \leq t < t_{i+1}, \\ \frac{t_{i+2} - t}{t_{i+2} - t_{i+1}}, & \text{if } t_{i+1} \leq t < t_{i+2}, \\ 0, & \text{if } t < t_i \text{ or } t \geq t_{i+2}. \end{cases}$$

We see that $N_i^1(t)$ are piecewise linear functions taking values $N_i^1(t_{i+1}) = 1$ and $N_j^1(t_{i+1}) = 0$, $j \neq i$. Fig. 1.14.1 shows the first-order B-splines for an open polyline constructed on six control points.
A closed polyline can be constructed on the sequence of knots $t_0 = -1$, $t_1 = 0$, $t_2 = 1$, ..., $t_i = i-1$, ..., $t_{n+2} = n+1$, $t_{n+3} = n+2$ as a special case of the B-spline curve (1.9.2). The parameter of the B-spline curve in this case varies within the range $t_1 \leq t \leq t_{n+2}$. The first-order B-splines for periodic closed polylines constructed on four control points are shown in Fig. 1.14.2.

Consider a NURBS representation of the Lagrange spline. Suppose we need to construct the B-spline curve passing through points $a_i$ for parameter values $x_i$, $i=0,1,...,n$. We can construct the B-spline curve of $n$-th order (1.9.2) on the sequence of knots: $t_0 = t_1 = ... = t_n = x_0$, $t_{n+1} = t_{n+2} = ... = t_{2n+1} = x_n$. The sequence contains $2n+2$ knots in total. The B-spline curve contains $n+1$ control points. The weight of each control point is set equal to 1. The control points $p_i$, $i=0,1,...,n$ of the B-spline curve can be found from the system of equations

$$N_0^n(x_0)p_0 + N_1^n(x_0)p_1 + ... + N_n^n(x_0)p_n = a_0$$
$$N_0^n(x_1)p_0 + N_1^n(x_1)p_1 + ... + N_n^n(x_1)p_n = a_1$$
$$...$$
$$N_0^n(x_n)p_0 + N_1^n(x_n)p_1 + ... + N_n^n(x_n)p_n = a_n$$

The determinant of this system of equations is not zero if there are no coincident points among $x_i$. Since B-splines $N_j^n(t)$ are polynomials of degree $n$ on the interval $[x_0,x_n]$, the constructed B-spline curve is a polynomial function of degree $n$, and it
coincides with the Lagrange and Newton splines.

Consider a NURBS representation of an open cubic spline passing through the points \(a_i\) at the parameter values \(x_i, i=0,1,...,n\) and having the derivatives of the radius vector at the endpoints \(q_0\) and \(q_n\). A cubic spline is a piecewise polynomial function of the third degree of the parameter having continuous derivatives up to the second order.

Therefore, we will use B-splines of the third order \(N_j^3(t)\) to construct a B-spline curve coinciding with the cubic spline. To match the start and end points of the spline and the B-spline curve, the four start and the four end knots of the sequence must have a multiplicity equal to four. We can construct the following sequence of knots: \(t_0 = t_1 = t_2 = t_3 = x_0, t_4 = x_1, t_5 = x_2, ..., t_{n+3} = x_n, t_{n+4} = t_{n+5} = t_{n+6} = x_n\). The sequence contains \(n+7\) knots in total. The B-spline curve contains \(n+3\) control points. The weight of each control point is set equal to 1. Thus, the B-spline curve that coincides with the cubic spline will have the form

$$
r(t) = \sum_{j=0}^{n+3} N_j^3(t)p_j.
$$

The B-spline curve, as well as the cubic spline, will have a domain \(x_0 \leq t \leq x_n\).

The control points \(p_j, j=0,1,...,n+2\) can be found from the following conditions:

$$
r(x_0) = a_0, \quad \frac{dr}{dt}(x_0) = q_0,
$$
$$
r(x_i) = a_i, \quad i = 1,2,...,n,
$$
$$
\frac{dr}{dt}(x_n) = q_n, \quad r(x_n) = a_n.
$$

These conditions lead to a system of \(n+3\) equations:

$$
N_0^3(x_0)p_0 + N_1^3(x_0)p_1 + ... + N_{n+2}^3(x_0)p_{n+2} = a_0,
$$
$$
3N_1^2(x_0) \frac{p_1 - p_0}{t_5 - t_2} + 3N_2^2(x_0) \frac{p_2 - p_1}{t_6 - t_3} + ... + 3N_{n+2}^2(x_0) \frac{p_{n+2} - p_{n+1}}{t_{n+5} - t_{n+2}} = q_0,
$$
$$
N_0^3(x_1)p_0 + N_1^3(x_1)p_1 + ... + N_{n+2}^3(x_1)p_{n+2} = a_1,
$$
$$
N_0^3(x_2)p_0 + N_1^3(x_2)p_1 + ... + N_{n+2}^3(x_2)p_{n+2} = a_2,
$$
$$
... ...
$$
$$
N_0^3(x_{n-1})p_0 + N_1^3(x_{n-1})p_1 + ... + N_{n+2}^3(x_{n-1})p_{n+2} = a_{n-1},
$$
$$
3N_1^2(x_n) \frac{p_1 - p_0}{t_5 - t_2} + 3N_2^2(x_n) \frac{p_2 - p_1}{t_6 - t_3} + ... + 3N_{n+2}^2(x_n) \frac{p_{n+2} - p_{n+1}}{t_{n+5} - t_{n+2}} = q_n,
$$
$$
N_0^3(x_n)p_0 + N_1^3(x_n)p_1 + ... + N_{n+2}^3(x_n)p_{n+2} = a_n.
$$

Using (1.9.3) and (1.9.4), we define the values of the B-splines at the parametric values \(t=x_i, i=0,1,...,n\). Only one B-spline of the third order \(N_0^3(x_0) = 1\) and one B-
spline of the second order \( N_1^2(x_0) = 1 \) are nonzero for the parameter \( t=x_0 \). For the parameter \( t=x_n \), the B-spline of the third order \( N_{n+2}^3(x_n) = 1 \) and one B-spline of the second order \( N_{n+2}^2(x_n) = 1 \) are nonzero too. For each parameter value \( t=x_{j-3}=t_j \), \( j=4,5,\ldots,n+2 \) only three B-splines of the third order are nonzero:

$$
N_{j-3}^3(t_j) = \frac{t_{j+1}-t_j}{t_{j+1}-t_{j-2}} \cdot \frac{t_{j+1}-t_j}{t_{j+1}-t_{j-1}},
$$

$$
N_{j-2}^3(t_j) = \frac{t_j-t_{j-1}}{t_{j+2}-t_{j-1}} \cdot \frac{t_{j+2}-t_j}{t_{j+1}-t_{j-1}} + \frac{t_{j+1}-t_j}{t_{j+1}-t_{j-2}} \cdot \frac{t_j-t_{j-2}}{t_{j+1}-t_{j-1}},
$$

$$
N_{j-1}^3(t_j) = \frac{t_j-t_{j-1}}{t_{j+2}-t_{j-1}} \cdot \frac{t_j-t_{j-1}}{t_{j+1}-t_{j-1}}
$$

(1.14.1)

and two B-splines of the second order:

$$
N_{j-2}^2(t_j) = \frac{t_{j+1}-t_j}{t_{j+1}-t_{j-1}},
$$

$$
N_{j-1}^2(t_j) = \frac{t_j-t_{j-1}}{t_{j+1}-t_{j-1}}.
$$

(1.14.2)

After substituting (1.14.1) and (1.14.2), the system of equations for determining the control points takes the following form:

$$
\begin{bmatrix}
1 & 0 & 0 & 0 & 0 & \cdots & 0 & 0 & 0 & 0 \\
a_{10} & a_{11} & 0 & 0 & 0 & \cdots & 0 & 0 & 0 & 0 \\
0 & a_{21} & a_{22} & a_{23} & 0 & \cdots & 0 & 0 & 0 & 0 \\
0 & 0 & a_{32} & a_{33} & a_{34} & \cdots & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & a_{43} & a_{44} & \cdots & 0 & 0 & 0 & 0 \\
\vdots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \vdots \\
0 & 0 & 0 & 0 & 0 & \cdots & a_{n-1,n-1} & a_{n-1,n} & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & \cdots & a_{n,n-1} & a_{n,n} & a_{n,n+1} & 0 \\
0 & 0 & 0 & 0 & 0 & \cdots & 0 & 0 & a_{n+1,n+1} & a_{n+1,n+2} \\
0 & 0 & 0 & 0 & 0 & \cdots & 0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
p_0 \\
p_1 \\
p_2 \\
p_3 \\
p_4 \\
\vdots \\
p_{n-1} \\
p_n \\
p_{n+1} \\
p_{n+2}
\end{bmatrix}
=
\begin{bmatrix}
a_0 \\
a_1 \\
a_2 \\
a_3 \\
a_4 \\
\vdots \\
a_{n-2} \\
a_{n-1} \\
a_n \\
a_{n+1}
\end{bmatrix}
$$

Fig. 1.14.3 shows a third-order B-spline curve coinciding with a cubic spline constructed on six points (\( n=5 \)).
Fig. 1.14.4 shows a set of $B$-splines of the third-order $B$-spline curve shown in Fig. 1.14.3 coinciding with the cubic spline.

For a closed periodic cubic spline, the control points $p_j$, $j=0,1,...,n$ can be found from the conditions: $r(x_i) = a_i$, $i=0,1,...,n$. The number of the control points of a $B$-spline curve is equal to the number of given points of the spline.

Consider a NURBS representation of an open composite Hermite spline of the third order (1.3.10) with parametric values $x_i$ passing through points $a_i$ and having the derivatives $q_i$ at these points, where $i=0,1,2,...,n$ are point numbers. A Hermite spline is a composite curve of the third degree with discontinuous second- and third-order derivatives at the points $x_i$. Therefore, we will use $B$-splines of the third order $N^3_i(t)$ with multiple knots to construct a $B$-spline curve. In order to match the start and end points of the spline and the $B$-spline curve, the four start and four end knots of the sequence must have a multiplicity of four, and the rest of the knots of the sequence must have a multiplicity of two. Let us construct the following sequence of knots:

$t_0=t_1=t_2=t_3=x_0$, $t_4=t_5=x_1$, $t_6=t_7=x_2$, $t_8=t_9=x_3$, ..., $t_{2i+2}=t_{2i+3}=x_i$, ..., $t_{2n}=t_{2n+1}=x_{n-1}$, $t_{2n+2}=t_{2n+3}=t_{2n+4}=t_{2n+5}=x_n$. The sequence has $2(n+1)+4$ knots in total. The $B$-spline curve will contain $2n+2$ control points. The weight of each control point is set equal to 1. Thus, a $B$-spline curve coinciding with the Hermite spline has the following form:
The B-spline curve, as well as the Hermite spline, will have a domain \( x_0 \leq t \leq x_n \).

The start and end control points of the B-spline curve are equal to the start and end control points of the spline, respectively: \( p_0 = a_0, \ p_{2n+1} = a_n \). The control points of the B-spline curve adjacent to them are constructed as follows:

$$
p_1 = a_0 + \frac{x_1 - x_0}{3} q_0, \quad p_{2n} = a_n - \frac{x_n - x_{n-1}}{3} q_n.
$$

Next we construct a pair of control points of the B-spline curve on the basis of each "internal" control point \( a_i, i=1,2,...,n-1 \) of the Hermite spline as follows:

$$
p_{2i} = a_i - \frac{x_i - x_{i-1}}{3} q_i, \quad p_{2i+1} = a_i + \frac{x_{i+1} - x_i}{3} q_i. \tag{1.14.3}
$$

Using (1.9.3) and (1.9.4), we define the values of the B-splines at the parametric values \( t=x_i, i=0,1,...,n \). Only one B-spline of the third order \( N_0^3(x_0)=1 \) and one B-spline of the second order \( N_1^2(x_0)=1 \) are nonzero for the parameter \( t=x_0 \). For the parameter \( t=x_n \) also only one third-order B-spline \( N_{2n+1}^3(x_n)=1 \) and one second-order B-spline \( N_{2n+1}^2(x_n)=1 \) are nonzero. From (1.14.1) it follows that for each parameter value \( t=t_j=t_{j-1}, j=5,6,...,2n+1 \) only two third-order B-splines are nonzero:

$$
N_{j-3}^3(t_j) = \frac{t_{j+1} - t_j}{t_{j+1} - t_{j-2}} \cdot \frac{t_{j+1} - t_j}{t_{j+1} - t_{j-1}}, \quad N_{j-2}^3(t_j) = \frac{t_{j+1} - t_j}{t_{j+1} - t_{j-2}} \cdot \frac{t_j - t_{j-2}}{t_{j+1} - t_{j-1}}.
$$

Or after substitution \( t_{2i+2}=t_{2i+3}=x_i, i=1,2,...,n-1 \):

$$
N_{2i}^3(x_i) = \frac{x_{i+1} - x_i}{x_{i+1} - x_{i-1}}, \quad N_{2i+1}^3(x_i) = \frac{x_i - x_{i-1}}{x_{i+1} - x_{i-1}}.
$$

From (1.14.2) it follows that for each parameter value \( t=t_j=t_{j-1}, j=5,6,...,2n+1 \), only one second-order B-spline is nonzero:

$$
N_{j-2}^2(t_j) = \frac{t_{j+1} - t_j}{t_{j+1} - t_{j-1}}.
$$

Or after substitution \( t_{2i+2}=t_{2i+3}=x_i, i=1,2,...,n-1 \): \( N_{2i+1}^2(x_i)=1 \). Let us verify that at parameter values \( t=x_i, i=0,1,...,n \), the B-spline curve has radius vector \( a_i \) and derivatives \( q_i \) by direct substitution. Indeed,
$$ r(x_0) = N_0^3(x_0)p_0 = a_0, $$
$$ r(x_i) = N_{2i}^3(x_i)p_{2i} + N_{2i+1}^3(x_i)p_{2i+1} = a_i, $$
$$ r(x_n) = N_{2n+1}^3(x_n)p_{2n+1} = a_n, $$

and according to (1.9.5) and (1.14.3),

$$ \frac{dr}{dt}(x_0) = 3N_1^2(x_0)\frac{p_1 - p_0}{t_4 - t_1} = q_0, $$
$$ \frac{dr}{dt}(x_i) = 3N_{2i+1}^2(x_i)\frac{p_{2i+1} - p_{2i}}{t_{2i+4} - t_{2i+1}} = q_i, $$
$$ \frac{dr}{dt}(x_n) = 3N_{2n+1}^2(x_n)\frac{p_{2n+1} - p_{2n}}{t_{2n+4} - t_{2n+1}} = q_n. $$

Fig. 1.14.5 shows the third-order B-curve coinciding with the composite Hermite spline constructed on four points \( n=3 \).

![Fig. 1.14.5](image)

Fig. 1.14.6 shows a set of B-splines of the third-order B-spline curve coinciding with a composite Hermite spline also shown in Fig. 1.14.5.

For the periodic closed Hermite spline, the sequence of knots of the B-spline curve contains only knots of multiplicity two. The control points can be found by formulas (1.14.3). The number of control points of the B-spline curve is equal to double the number of the given points of the spline.

![Fig. 1.14.6](image)
Consider a NURBS representation of a second-order curve. We showed that curves of the second order can be represented as rational Bezier curves. A B-spline curve is a generalization of a rational Bezier curve. Therefore some part of any second-order curve can be represented as a quadratic B-spline curve constructed on three points, on the basis of the sequence of knots $t_0 = t_1 = t_2 < t_3 = t_4 = t_5$.

A periodic closed curve of the second order can be completely represented in the form of a B-spline curve having multiple knots. Fig. 1.14.7 shows an elliptical B-spline curve of the second order and its control polyline.

![Fig. 1.14.7](image)

It was constructed on the points $p_0, p_1, p_2, p_3, p_4, p_5, p_6, p_7$. Its control polyline is a rectangle circumscribed about the elliptical curve. The weights of the control points are: $w_0 = w_2 = w_4 = w_6 = 1$, $w_1 = w_3 = w_5 = w_7 = \cos(\pi/4)$. The sequence of knots has the form $t_0 = -1$, $t_1 = t_2 = 0$, $t_3 = t_4 = 1$, $t_5 = t_6 = 2$, $t_7 = t_8 = 3$, $t_9 = t_{10} = 4$, $t_{11} = t_{12} = 5$. If we want the length of a parametric curve shown in Fig. 1.14.7 to be equal to $2\pi$, then instead of the sequence of the knots mentioned above we can use the sequence: $t_0 = -\pi/2$, $t_1 = t_2 = 0$, $t_3 = t_4 = \pi/2$, $t_5 = t_6 = \pi$, $t_7 = t_8 = 3\pi/2$, $t_9 = t_{10} = 2\pi$, $t_{11} = t_{12} = 2\pi + \pi/2$. The B-spline curve can have breakpoints with multiple knots.

![Fig. 1.14.8](image)

Fig. 1.14.8 shows a set of B-splines of the quadratic B-spline curve coinciding with the ellipse also shown in Fig. 1.14.7.

### 1.15. Curves Constructed on Other Curves

Curves may be constructed on the basis of other curves. We consider the extended, trimmed, equidistant, remade, reference, and bridge curves. A curve which is
the basis for construction of a new curve is called its base curve. A curve of the same type as the constructed curve should not be used as the base curve.

An extended curve may be constructed on the basis of any curve by changing the domain of the curve parameter. Suppose it is required to extend the curve $r_b(t)$, $t_{\text{min}} \leq t \leq t_{\text{max}}$ by expanding the domain of the parameters to $a + t_{\text{min}} \leq t \leq t_{\text{max}} + b$. When $a < 0$ and $b > 0$, the curve is extended beyond its limits; when $a > 0$ and $b < 0$ the curve is trimmed.

If the curve is not periodic and its parameter goes beyond the limits of the domain, the curve may be continued in accordance with the rule for calculation of the radius vector of the curve. Such curves include analytic curves and curves based on the curves with the known rule of the radius vector calculation. For example, the radius vector of the cylindrical helix continues to change according to the rule for a cylindrical helix outside the domain.

In general, in the absence of calculation rule for the non-periodic curve outside its domain, we continue the curve along the tangent it has at the corresponding endpoint. The radius vector of the extended curve is calculated by the formula

$$
r(t) = \begin{cases} 
r_b(t_{\text{min}}) + (t - t_{\text{min}}) \frac{dr_b}{dt} \bigg|_{t_{\text{min}}} & \text{if } t < t_{\text{min}}, \\
r_b(t), & \text{if } t_{\text{min}} \leq t \leq t_{\text{max}}, \\
r_b(t_{\text{max}}) + (t - t_{\text{max}}) \frac{dr_b}{dt} \bigg|_{t_{\text{max}}} & \text{if } t_{\text{max}} > t.
\end{cases}
$$

(1.15.1)

If the base curve is periodic, we can perform a cyclic recalculation of the parameter when it is out of the domain. In this case, the radius vector of the extended curve is calculated using the formula

$$
r(t) = r_b(t - p \cdot \Phi((t - t_{\text{min}})/p)),
$$

(1.15.2)

where $p$ is the period of basic curve and $\Phi(w)$ is a function to calculate the maximum integer less than $w$.

An extended curve should not be used as the base curve for another extended curve. One should use the base curve of the initial extended curve as a base curve, with corresponding recalculation of the parameters $a$ and $b$.

The radius vector—not only extended curve, but of any curve with its parameter out of the domain—can be computed using (1.15.1) or (1.15.2).

A trimmed curve is some part of any curve with the opposite or the same direction. Let the parameter $t$ of the base curve vary in the range $t_{\text{min}} \leq t \leq t_{\text{max}}$. We define a trimmed curve as the part of the base curve starting at parameter $t_1$ and ending at parameter $t_2$. The direction of the trimmed curve may coincide with the direction of the base curve, or be opposite—for example, if $t_2 < t_1$. If the curve is periodic and closed, there are two ways to progress from point $t_1$ to point $t_2$: in the positive direction of the base curve and in the opposite direction. To overcome this ambiguity, one
introduces a sign parameter that takes values of +1 or -1 and describes the coincidence of directions of the closed curve and the base curve. The parameter of the trimmed curve \( w_{\text{min}} = 0 \) corresponds to the parameter of the base curve \( t_1 \), while the parameter of the trimmed curve \( w_{\text{max}} = s \) corresponds to the parameter of the base curve \( t_2 \), where \( s \) is the parametric distance between \( t_2 \) and \( t_1 \) (provided that the curve is closed). If the curve is open, then \( s = |t_2 - t_1| \). The radius vector of the trimmed curve is described by

$$
r(w) = r_b(t + w \cdot \text{sign}), \quad 0 \leq w \leq s,
$$

(1.15.3)

where \( r_b(t) \) is the base curve.

A trimmed curve should not be used as the base curve for another trimmed curve. One should use the base curve of the initial trimmed curve as a base curve, with appropriate recalculation of the trimming parameters.

A trimmed curve may be used to change the direction of the curve. In this case \( t_1 = t_{\text{max}}, t_2 = t_{\text{min}}, \) and \( \text{sign} = -1 \).

A trimmed curve may be used to change the position of the starting point of the periodic closed curve. For this purpose, the base curve must be periodic and closed, and \( t_1 = t_2 \). In this case the trimmed curve will also be periodic and closed.

A remade curve may be constructed on the basis of any curve by changing the values of its extreme parameters. Suppose it is required that the curve \( r_b(t), t_{\text{min}} \leq t \leq t_{\text{max}} \) has the domain of the parameter \( w_{\text{min}} \leq w \leq w_{\text{max}} \). Let us construct the remade curve for this case

$$
r(w) = r_b(t(w)), \quad w_{\text{min}} \leq w \leq w_{\text{max}},
$$

(1.15.4)

where \( t(w) = t_{\text{min}} + \frac{w_{\text{max}} - w}{w_{\text{max}} - w_{\text{min}}} \cdot (t_{\text{max}} - t_{\text{min}}) \).

A remade curve should not be used as the base curve for another remade curve. Instead, one should use the base curve of the initial remade curve for this purpose.

A remade curve coincides with the base curve, but has a different parameter domain. A curve with a modified parameter length is used to align the parameter domains of the two curves.

An offset curve is described by the vector function

$$
r(t) = r_b(t) + a \times t_b(t),
$$

(1.15.5)

where \( r_b(t) \) is the basis curve, \( t_b(t) = \frac{r_b}{\sqrt{r_b \cdot r_b}} \) is the unit vector tangent to the base curve at a given point, and \( a \) is a given vector. The parameter domain of the offset curve may coincide with the parameter domain of the base curve, and may be extended according to the rules of the extended curve construction.

The offset curve justifies its name if \( r_b(t) \) is a planar curve and vector \( a \) is orthogonal to the plane of the base curve. In this case the second term on the right-hand
side of (1.15.5) is a vector that lies in the plane of the base curve, orthogonal to it, and of length \(a\). As a result, we get a curve every point of which is separated from the corresponding point of the base curve by the length of vector \(a\) along the normal. Fig. 1.15.1 shows an example of the offset curve.

![Fig. 1.15.1.](image)

The offset curve should not be used as the base curve for another offset curve. Instead, one should use the base curve of the initial offset curve for this purpose, with appropriate recalculation of the offset vector. For example, if you want to build an offset curve based on the offset curve \(r'(t) = r_b(t) + a \times t_b(t)\), then as the base curve you should take the curve \(r_b(t)\), and the offset vector must be equal to \(a + a'\).

The reference curve is a curve every point of which is obtained by a transformation of the corresponding point of the base curve. The parameter domain of the reference curve coincides with the parameter domain of the base curve. The radius vector of the reference curve is described by

$$ r(t) = M \cdot r_b(t), $$  

(1.15.6)

where \(r_b(t)\) is the basis curve and \(M\) is the extended transformation matrix.

An extended matrix contains the matrix of transformation and a translation along the vector. In the general case, a transformation of the radius vector of the point \(r_0\) has the following form:

$$ r = A \cdot r_0 + t, $$

where \(A\) is a transformation matrix (rotation, symmetry transformation, scaling) and \(t\) a translation vector. Extended matrix \(M\) is the matrix \(A\) padded with zeros at the bottom and with components of the translation vector \(t\) on the right side. It has the form

$$ M = \begin{bmatrix} A & t \\ 0 & 1 \end{bmatrix}. $$  

(1.15.7)

Let us construct the extended matrix of transformation of a curve from the local coordinate system to the global coordinate system as an example. Let the curve \(r_b(t)\) be described in the local Cartesian coordinate system. Suppose we need to work with it in the global Cartesian coordinate system. Let the origin of the local coordinate system be located at point \(p\) with global coordinates \(p_1, p_2, p_3\), and let basis vectors \(i_x = [x_1 x_2 x_3]^T\),
of the local system be described in the global system by the coordinates \( x_1, x_2, x_3, y_1, y_2, y_3, z_1, z_2, z_3 \), respectively. Then the extended transformation matrix has the form

$$
M = \begin{bmatrix}
x_1 & y_1 & z_1 & p_1 \\
x_2 & y_2 & z_2 & p_2 \\
x_3 & y_3 & z_3 & p_3 \\
0 & 0 & 0 & 1
\end{bmatrix}.
$$

When working with an extended matrix, it is assumed that the radius vectors with coordinates \( r_1, r_2, r_3 \) are described by the column matrix

$$
r = \begin{bmatrix}
r_1 \\
r_2 \\
r_3 \\
1
\end{bmatrix},
$$

and free vectors with components \( v_1, v_2, v_3 \) are described by means of column-matrix

$$
v = \begin{bmatrix}
v_1 \\
v_2 \\
v_3 \\
0
\end{bmatrix}.
$$

A reference curve should not be used as the base curve for another reference curve. Instead, one should use the base curve of the initial reference curve for this purpose, with appropriate recalculation of the transformation matrix. For example, if it is required to construct a reference curve based on the reference curve \( r(t) = M^t r_b(t) \), one should use the curve \( r_b(t) \), and a transformation matrix would be a product of matrices \( M \cdot M' \).

A bridge curve smoothly connects the endpoints of two curves. For example, suppose we need to smoothly conjugate the end of curve \( a(t) \) with the beginning of curve \( b(t) \). The radius vector of the bridge curve is described by

$$
r(w) = a(t_{\text{max}})(1 - 3w^2 + 2w^3) + b(t_{\text{min}})(3w^2 - 2w^3) +
a'(t_{\text{max}})(w - 2w^2 + w^3)k_a + b'(t_{\text{min}})(-w^2 + w^3)k_b,
$$

where \( w \in [0,1] \),

$$
a'(t_{\text{max}}) = \frac{da(t)}{dt} \bigg|_{t=t_{\text{max}}}
$$

is the derivative of the radius vector of the first conjugated
curve, and \( b'(t_{\text{min}}) = \frac{db(t)}{dt} \bigg|_{t=t_{\text{min}}} \) is the derivative of the radius vector of the second conjugated curve, with \( k_a \) and \( k_b \) as normalization coefficients for derivatives \( a'(t_{\text{max}}) \) and \( b'(t_{\text{min}}) \), respectively. Coefficients \( k_a \) and \( k_b \) are calculated by division of the distance between the conjugating points of the curves by the length of the derivatives \( a'(t_{\text{max}}) \) and \( b'(t_{\text{min}}) \).

1.16. Contours

A composite curve is based on other curves and is the most general form of a curve. The curves forming a composite curve are called segments. To construct a composite curve, the following conditions must be satisfied: The beginning of each subsequent segment must coincide with the end of the previous segment. Closed composite curves are called contours. In a contour, the beginning of the first segment should coincide with the end of the last segment. If the segments of a composite curve are not smoothly joined, the composite curve has breakpoints. In general, the derivatives of the composite curve at the points of conjugation are non-continuous in length and direction. A composite curve is shown in Fig. 1.16.1.

Let the composite curve consist of \( n \) segments

$$ r_i(w_i), \quad w_{\text{min}} \leq w \leq w_{\text{max}}, \quad i = 1, 2, \ldots, n. $$

The initial value of parameter \( t \) of the composite curve is set equal to zero. The parametric length of the composite curve is assumed to be equal to the sum of the parametric lengths of constituent segments \( t_{\text{min}} = 0, \quad t_{\text{max}} = \sum_{i=1}^{n} (w_{i_{\text{max}}} - w_{i_{\text{min}}}). \)

![Fig. 1.16.1](image)

When calculating the radius vector of a composite curve, it is first necessary to define the segment to which the value of the parameter of the composite curve corresponds. Next, we need to determine the corresponding value of the parameter of this segment; and, finally, we calculate the radius vector of the segment, which is the radius vector of the composite curve. Let \( k \) be the number of the segment for parameter \( t \) of the
composite curve. Suppose the following relation holds for this \( k \)

$$
\sum_{i=1}^{k-1} (w_{i,\text{max}} - w_{i,\text{min}}) \leq t < \sum_{i=1}^{k} (w_{i,\text{max}} - w_{i,\text{min}}).
$$

Then, in accordance with what was said before, the radius vector of the composite curve is defined by the equality

$$
r(t) = r_k \left( w_{k,\text{min}} + t - \sum_{i=1}^{k-1} (w_{i,\text{max}} - w_{i,\text{min}}) \right) = r_k(w_k), \quad 0 \leq t \leq t_{\text{max}},
$$  

(1.16.1)

where the parameter of the \( k \)-th segment is equal to

$$
w_k = w_{k,\text{min}} + t - \sum_{i=1}^{k-1} (w_{i,\text{max}} - w_{i,\text{min}}).
$$  

(1.16.2)

Conspicuously, the approach for calculation of the radius vector of a composite curve is similar to that for calculating the radius vector of a polyline and a Hermite spline.

Composite curves should not be used as segments of other composite curves; but that does not mean one cannot construct a composite curve from a set of composite curves. If we need to construct a composite curve based on other composite curves, the latter should not be considered as single curves but as sets of curves that make them up.

**Exercises**

1. Calculate the maximum and minimum curvature of an ellipse.
2. Describe a cardioid by a vector function.
3. Express the first derivative of a Bezier curve at the endpoints by the radius vectors of the endpoints.
4. Express a parabola in the form of a B-spline curve.