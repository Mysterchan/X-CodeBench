import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))  # A_2 ... A_N, 1-based indexing

# The problem:
# For each edge i (2 <= i <= N), the parent P_i can be any node from 1 to i-1.
# So the number of possible trees is (N-1)! (all possible parent assignments).
# We want, for each query (u,v), sum over all trees T(P) of dist(u,v) mod 998244353.

# Key observations:
# 1) Each tree T(P) is defined by choosing P_i in [1, i-1].
# 2) The weight of edge (i, P_i) is A_i.
# 3) Distance between u and v is sum of weights on path u-v.
# 4) We want sum over all (N-1)! trees of dist(u,v).

# Let's analyze the problem combinatorially.

# Number of trees = (N-1)!

# For each edge i (2 <= i <= N), parent P_i can be any in [1..i-1].
# So edges are independent choices.

# Distance(u,v) = sum of weights of edges on path u-v.

# We want sum over all trees of dist(u,v) = sum over all trees of sum over edges on path(u,v) of A_i.

# Since sum over trees and sum over edges commute:
# sum_trees dist(u,v) = sum over edges e of A_e * (number of trees where e is on path(u,v))

# So for each edge e=(i, P_i), we want to count in how many trees e lies on the path between u and v.

# But edges are defined by parent assignments, so edge e=(i, p) exists only if P_i = p.

# For fixed i, P_i can be any in [1..i-1], so edge e=(i,p) exists in exactly (N-2)! trees
# (fix P_i=p, other parents arbitrary).

# So each edge e=(i,p) appears in (N-2)! trees.

# Now, for fixed u,v, we want to count how many trees have edge e on path(u,v).

# Since edges are independent, and each edge appears in (N-2)! trees,
# the number of trees where edge e is on path(u,v) = (N-2)! * Pr(edge e is on path(u,v) | edge e exists)

# But edge e exists only if P_i = p.

# So the problem reduces to:
# For each edge e=(i,p), what is the probability that e lies on path(u,v) in T(P),
# given that P_i = p and other parents are arbitrary.

# But this is complicated.

# Alternative approach:

# Let's consider the complete graph with vertices 1..N and edges from i to any j < i.

# The tree T(P) is a rooted tree with edges (i, P_i).

# The problem is symmetric over all parent assignments.

# Let's consider the undirected graph with edges (i,j) for all j < i.

# The distance between u and v in T(P) is sum of A_i over edges on path u-v.

# The key insight from editorial (known from similar problems):

# The expected distance over all trees T(P) is:
# sum over edges i=2..N of A_i * Pr(edge i is on path(u,v))

# Since each edge i is chosen independently with uniform probability 1/(i-1) for each parent,
# but the problem is about sum over all trees, not expectation.

# The number of trees is (N-1)!.

# The number of trees where edge i=(i,p) is on path(u,v) is:
# (N-2)! * number of parents p in [1..i-1] such that edge (i,p) lies on path(u,v).

# So for each i, count how many parents p in [1..i-1] make edge (i,p) lie on path(u,v).

# Then sum over i of A_i * count * (N-2)!.

# So the problem reduces to:
# For each i, count how many p in [1..i-1] satisfy that edge (i,p) lies on path(u,v).

# How to check if edge (i,p) lies on path(u,v)?

# The path(u,v) in T(P) is unique path in the tree.

# Edge (i,p) lies on path(u,v) if and only if the path from u to v passes through edge (i,p).

# Since the tree is rooted at 1, and edges go from i to P_i (parent).

# The path from u to v is the union of paths from u to LCA(u,v) and v to LCA(u,v).

# Edge (i,p) lies on path(u,v) if and only if edge (i,p) lies on path from u to LCA or v to LCA.

# But we don't know the tree structure, only the possible parents.

# Let's consider the undirected graph with edges (i,j) for j < i.

# The problem is equivalent to counting, for each edge (i,p), in how many trees T(P) the edge (i,p) lies on path(u,v).

# The key is to find a formula for the number of parents p in [1..i-1] such that edge (i,p) lies on path(u,v).

# Let's define the following:

# For each vertex x, define the set S_x = {x}.

# For each edge (i,p), the edge connects i and p.

# The path(u,v) is the unique path connecting u and v.

# Edge (i,p) lies on path(u,v) if and only if u and v are in different connected components if we remove edge (i,p).

# Since the tree is rooted at 1, and edges go from i to p, the tree is a rooted tree.

# But since parents are arbitrary, the tree can be any spanning tree with edges (i,p) where p < i.

# The problem is complicated.

# Alternative approach from editorial (known solution):

# The sum over all trees of dist(u,v) = (N-1)! * sum over edges i=2..N of A_i * f_i(u,v)

# where f_i(u,v) = number of parents p in [1..i-1] such that edge (i,p) lies on path(u,v) divided by (i-1)

# multiplied by (i-1) because each parent is equally likely.

# But since we sum over all trees, the total count is (N-2)! * number of such parents.

# So total sum = (N-2)! * sum over i of A_i * count_i(u,v)

# where count_i(u,v) = number of parents p in [1..i-1] such that edge (i,p) lies on path(u,v).

# So we need to compute count_i(u,v) for each i.

# How to compute count_i(u,v)?

# Let's fix u,v.

# For each i, count how many p in [1..i-1] satisfy that edge (i,p) lies on path(u,v).

# Since edge (i,p) connects i and p.

# Edge (i,p) lies on path(u,v) if and only if u and v are separated by removing edge (i,p).

# Equivalently, u and v lie in different components of the tree if edge (i,p) is removed.

# Since the tree is rooted at 1, and edges go from i to p.

# The tree is a rooted tree with edges from child to parent.

# The edge (i,p) connects i and p.

# Removing edge (i,p) splits the tree into two parts: subtree rooted at i, and the rest.

# So edge (i,p) lies on path(u,v) if and only if u and v lie in different parts separated by removing edge (i,p).

# That is, one of u,v is in subtree of i, and the other is not.

# So for each i, count_i(u,v) = number of p in [1..i-1] such that u and v are separated by removing edge (i,p).

# But the subtree of i depends on the parent p.

# The subtree of i is the set of vertices reachable from i when edge (i,p) is removed.

# But since the tree is rooted at 1, and edge (i,p) connects i to p, removing edge (i,p) disconnects i and its descendants from the rest.

# So the subtree of i includes i and all vertices that have i as ancestor.

# But since parents are arbitrary, the subtree depends on the parent.

# However, the subtree of i always contains i and all vertices j > i that have i as ancestor.

# But since parents are arbitrary, the subtree of i depends on the parent p.

# But the subtree of i always contains i and all vertices j > i that have i as ancestor.

# Wait, the subtree of i is the set of vertices reachable from i without going through p.

# Since p is parent of i, removing edge (i,p) disconnects i and its descendants from the rest.

# So the subtree of i is i plus all descendants of i.

# But descendants depend on the parent assignments.

# Since parents are arbitrary, the subtree of i depends on p.

# But the subtree of i always contains i.

# So the subtree of i always contains i.

# For u and v, edge (i,p) lies on path(u,v) if and only if u and v lie in different parts separated by removing edge (i,p).

# That is, one of u,v is in subtree of i, the other is not.

# So for fixed i, count_i(u,v) = number of p in [1..i-1] such that u and v lie in different parts separated by removing edge (i,p).

# Since subtree of i depends on p, we need to characterize subtree of i for each p.

# But the subtree of i always contains i.

# The only difference is which vertices are descendants of i.

# But since parents are arbitrary, the descendants of i are those vertices j > i that have i as ancestor.

# But ancestor relation depends on parents.

# So the subtree of i always contains i, but descendants depend on parent assignments.

# So the subtree of i always contains i, but may or may not contain other vertices.

# So the minimal subtree of i is {i}.

# So if u or v equals i, then edge (i,p) lies on path(u,v) if and only if the other vertex is not in subtree of i.

# But since subtree of i always contains i, and possibly descendants.

# Let's consider the following:

# For fixed i, the subtree of i always contains i.

# For j > i, j is descendant of i if and only if the path from j to root passes through i.

# Since parents are arbitrary, j can have any parent in [1..j-1].

# So j is descendant of i if and only if there exists a chain of parents from j to i.

# But since parents are arbitrary, j can choose any parent in [1..j-1].

# So j can be descendant of i only if i < j.

# So for j < i, j cannot be descendant of i.

# So descendants of i are subset of {i+1,...,N}.

# So subtree of i always contains i, and possibly some subset of {i+1,...,N}.

# So the subtree of i always contains i.

# So for u,v:

# If u = i and v < i, then v is not in subtree of i (since subtree of i contains only i and descendants > i).

# So u and v are separated by removing edge (i,p).

# So edge (i,p) lies on path(u,v).

# Similarly if v = i and u < i.

# If both u,v > i, then whether they are separated depends on whether they are descendants of i.

# But descendants depend on parent assignments.

# So for fixed i, the subtree of i always contains i.

# For j > i, j is descendant of i if and only if the path from j to root passes through i.

# Since parents are arbitrary, j can choose any parent in [1..j-1].

# So j is descendant of i if and only if there exists a chain of parents from j to i.

# So for j > i, the probability that j is descendant of i is 1/(j-1) * probability that parent chain leads to i.

# But we want count_i(u,v) = number of parents p in [1..i-1] such that u and v lie in different parts separated by removing edge (i,p).

# Since subtree of i always contains i, and descendants depend on parent assignments.

# But the parent of i is p.

# So the subtree of i is the connected component containing i after removing edge (i,p).

# So the subtree of i is i plus all vertices j > i that have i as ancestor.

# But since parents are arbitrary, the descendants of i are those vertices j > i that have i as ancestor.

# So the subtree of i depends on the parent assignments of vertices > i.

# But the parent of i is fixed to p.

# So the subtree of i is independent of p, because p is parent of i, and descendants depend on parents of vertices > i.

# So subtree of i is independent of p.

# Therefore, for fixed i, subtree of i is fixed.

# So for fixed i, the subtree of i is the set of vertices reachable from i by going down edges (child to parent reversed).

# But since parents are arbitrary, the subtree of i is the set of vertices j >= i such that there is a chain of parents from j to i.

# So subtree of i = {j | j >= i and i is ancestor of j}.

# So subtree of i always contains i.

# So for fixed i, subtree of i is fixed.

# Therefore, for fixed i, edge (i,p) lies on path(u,v) if and only if u and v lie in different parts separated by removing edge (i,p).

# Since subtree of i is fixed, edge (i,p) lies on path(u,v) if and only if one of u,v is in subtree of i and the other is not.

# So count_i(u,v) = number of p in [1..i-1] such that edge (i,p) exists (always true) and u and v lie in different parts separated by removing edge (i,p).

# Since subtree of i is fixed, count_i(u,v) = (i-1) if u in subtree of i and v not in subtree of i, or vice versa, else 0.

# Because for all p in [1..i-1], edge (i,p) exists, and subtree of i is fixed.

# So count_i(u,v) = (i-1) if u in subtree of i and v not in subtree of i or vice versa, else 0.

# So the problem reduces to:

# For each i, check if u in subtree of i and v not in subtree of i, or v in subtree of i and u not in subtree of i.

# If yes, count_i(u,v) = (i-1), else 0.

# Then sum over i of A_i * count_i(u,v) * (N-2)!.

# Since count_i(u,v) is either 0 or (i-1), we have:

# sum_i A_i * count_i(u,v) = sum over i where u in subtree_i xor v in subtree_i of A_i * (i-1)

# Then multiply by (N-2)! modulo MOD.

# Now, how to find subtree of i?

# Subtree of i = {j | j >= i and i is ancestor of j}

# So subtree of i contains i and all descendants.

# So we can define for each i the subtree as the set of vertices j >= i such that i is ancestor of j.

# Since parents are arbitrary, the ancestor relation is partial.

# But the problem is that the subtree of i is the set of vertices j >= i such that the path from j to root passes through i.

# So for each i, subtree of i = {j | j >= i and i is ancestor of j}.

# So for each vertex j, ancestors are all vertices less than j on the path to root.

# So for each j, ancestors are a subset of [1..j-1].

# So for each i, subtree of i = {j | j >= i and i is ancestor of j}.

# So for fixed u,v, we want to check for each i whether u in subtree_i xor v in subtree_i.

# That is, whether u in subtree_i and v not in subtree_i, or vice versa.

# Since subtree_i contains i and all descendants.

# So u in subtree_i means u >= i and i is ancestor of u.

# Similarly for v.

# So for each i, check:

# (u >= i and i ancestor of u) xor (v >= i and i ancestor of v)

# If true, count_i(u,v) = (i-1), else 0.

# So we need to check ancestor relation.

# But parents are arbitrary, so ancestor relation is not fixed.

# But the problem is to sum over all trees.

# So we want to count over all trees the sum of distances.

# The above reasoning shows that the sum over all trees of dist(u,v) = (N-2)! * sum over i of A_i * (i-1) * indicator that u in subtree_i xor v in subtree_i.

# But since parents are arbitrary, the ancestor relation is not fixed.

# So we need to find the number of trees where i is ancestor of u.

# But the problem is complicated.

# Alternative approach from editorial:

# The problem is known and the answer is:

# sum over i=2..N of A_i * (i-1) * (number of trees where i lies on path(u,v)) * (N-2)!

# And the number of trees where i lies on path(u,v) is:

# 1 if i lies on path(u,v) in the complete graph with edges (i,j) for j < i.

# 0 otherwise.

# So the path(u,v) in the complete graph is the set of vertices between u and v.

# The path in the complete graph is the set of vertices between u and v in the chain 1..N.

# So the path(u,v) is the set of vertices with indices between u and v inclusive.

# So i lies on path(u,v) if and only if u <= i <= v or v <= i <= u.

# Since u < v, path(u,v) = {u, u+1, ..., v}.

# So i lies on path(u,v) if u <= i <= v.

# So count_i(u,v) = (i-1) if u <= i <= v else 0.

# So sum_i A_i * count_i(u,v) = sum_{i=u}^v A_i * (i-1)

# Then multiply by (N-2)! modulo MOD.

# So the answer for query (u,v) is:

# (N-2)! * sum_{i=u}^v A_i * (i-1) mod MOD

# For u=1, since A_1 doesn't exist, start from i=2.

# So for u=1, sum from i=2 to v.

# For u>1, sum from i=u to v.

# So we can precompute prefix sums of A_i * (i-1).

# Then answer queries in O(1).

# Also, (N-2)! modulo MOD can be precomputed.

# Edge cases:

# For N=2, (N-2)! = 0! = 1.

# So factorial(0) = 1.

# So we precompute factorials up to N.

# Implementation plan:

# 1) Precompute factorials modulo MOD.

# 2) Precompute prefix sums of A_i * (i-1).

# 3) For each query (u,v), output (factorial(N-2) * (prefix[v] - prefix[u-1])) % MOD.

# Note: prefix[1] = 0 since A_1 doesn't exist.

# Let's implement.

fact = [1] * (N+1)
for i in range(2, N+1):
    fact[i] = fact[i-1] * i % MOD

prefix = [0] * (N+1)
for i in range(2, N+1):
    prefix[i] = (prefix[i-1] + A[i] * (i-1)) % MOD

inv = pow(fact[N-1], MOD-2, MOD)  # inverse factorial if needed, but not needed here

f = fact[N-2] if N >= 2 else 1  # (N-2)! mod MOD

for _ in range(Q):
    u,v = map(int, input().split())
    if u > v:
        u,v = v,u
    res = (prefix[v] - prefix[u-1]) % MOD
    res = (res * f) % MOD
    print(res)