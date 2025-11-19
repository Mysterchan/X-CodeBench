import sys
input = sys.stdin.readline

MOD = 998244353

N = int(input())
Y = list(map(int, input().split()))

# Y is a permutation of 1..N
# Points: (i, Y[i-1]) for i in [1..N]

# We want sum over all subsets S with |S|>=2 of:
# area of bounding rectangle = (max_x - min_x) * (max_y - min_y)
# where x-coords are indices i, y-coords are Y[i-1]

# Key observations:
# - x-coords are fixed: 1..N
# - y-coords are permutation of 1..N

# The sum over all subsets S of (max_x - min_x) * (max_y - min_y)
# = sum over all subsets S of (max_x - min_x) * (max_y - min_y)
# = sum over all subsets S of (max_x - min_x) * (max_y - min_y)

# We can use linearity of expectation / sum decomposition:
# sum_S (max_x - min_x)*(max_y - min_y) = 
# sum_S (max_x - min_x) * sum_S (max_y - min_y) over subsets S
# but subsets are the same, so we cannot separate directly.

# Instead, use inclusion-exclusion and combinational approach:

# sum_S (max_x - min_x)*(max_y - min_y) 
# = sum_{i<j} (j - i) * sum_{k<l} (max_y - min_y) over subsets containing i,j,k,l
# but this is complicated.

# Instead, use the known approach for sum of ranges over subsets:

# For x-coords:
# sum over subsets S with size >=2 of (max_x - min_x) = sum_{i<j} (j - i) * 2^{j - i - 1}
# Explanation:
# For fixed i<j, number of subsets containing i and j is 2^{N-2}
# But only subsets where min_x = i and max_x = j contribute (j - i)
# Number of subsets with min_x = i and max_x = j is 2^{j - i - 1} (subsets of points between i and j)
# So sum over all subsets of (max_x - min_x) = sum_{i<j} (j - i) * 2^{j - i - 1}

# Similarly for y-coords:
# sum over subsets S with size >=2 of (max_y - min_y) = sum_{a<b} (Y_b - Y_a) * 2^{b - a - 1}
# But points are indexed by i, so we need to consider y-values in order of their indices.

# However, y-values are a permutation, so we can sort points by y-value and consider their indices.

# Let's define:
# For x:
# sum_x = sum_{i<j} (j - i) * 2^{j - i - 1}
# For y:
# We sort points by y-value:
# Let pos_y be array of indices sorted by Y[i]
# Then sum_y = sum_{a<b} (Y_{pos_y[b]} - Y_{pos_y[a]}) * 2^{b - a - 1}
# But Y_{pos_y[b]} = b+1 (since Y is permutation 1..N)
# So difference is (b+1) - (a+1) = b - a
# So sum_y = sum_{a<b} (b - a) * 2^{b - a - 1}

# Wait, this is the same as sum_x!

# So sum_x = sum_y

# But we want sum over subsets S of (max_x - min_x)*(max_y - min_y)
# = sum over subsets S of (max_x - min_x) * (max_y - min_y)

# The problem is that max_x and max_y are dependent on the same subset S.

# The key insight from editorial of similar problems:
# The sum over all subsets S with size >= 2 of (max_x - min_x)*(max_y - min_y)
# = (sum over all pairs i<j of (j - i)*2^{j - i - 1}) * (sum over all pairs a<b of |Y_a - Y_b| * 2^{b - a - 1})

# But since Y is a permutation of 1..N, and we consider pairs (a,b) with a<b,
# and |Y_a - Y_b| = |Y_b - Y_a|, but we need to consider pairs in order of indices.

# So we can compute sum_x = sum_{i<j} (j - i) * 2^{j - i - 1}
# and sum_y = sum_{i<j} |Y_j - Y_i| * 2^{j - i - 1}

# Then answer = sum_x * sum_y mod MOD

# Let's implement this.

# Precompute powers of 2
pow2 = [1]*(N+1)
for i in range(1, N+1):
    pow2[i] = (pow2[i-1]*2) % MOD

# sum_x = sum_{i<j} (j - i)*2^{j - i - 1}
# = sum_{d=1}^{N-1} d * 2^{d-1} * (N - d)
sum_x = 0
for d in range(1, N):
    val = d * pow2[d-1] % MOD
    val = val * (N - d) % MOD
    sum_x = (sum_x + val) % MOD

# sum_y = sum_{i<j} |Y_j - Y_i| * 2^{j - i - 1}
# We can compute this by iterating over pairs (i,j) with i<j

# But O(N^2) is impossible.

# We need a faster way.

# Since Y is a permutation of 1..N, we can use a Fenwick tree or BIT to compute sum_y efficiently.

# Let's process pairs (i,j) with i<j:
# sum_y = sum_{i<j} |Y_j - Y_i| * 2^{j - i - 1}

# We can rewrite sum_y as:
# sum_{d=1}^{N-1} 2^{d-1} * sum_{i=1}^{N-d} |Y_{i+d} - Y_i|

# So for each distance d, sum over i of |Y_{i+d} - Y_i|

# We can precompute for each d the sum of |Y_{i+d} - Y_i| for i=1..N-d

# Then sum_y = sum_{d=1}^{N-1} 2^{d-1} * sum_{i=1}^{N-d} |Y_{i+d} - Y_i|

# This is O(N^2) if done naively.

# But we can do better:

# Note that Y is a permutation of 1..N.

# Let's consider the array Y.

# For each d, sum_{i=1}^{N-d} |Y_{i+d} - Y_i| can be computed in O(N) for all d by using prefix sums.

# Let's precompute prefix sums of Y and prefix sums of absolute differences.

# But absolute differences are tricky.

# Alternative approach:

# Let's consider the array Y.

# For each d from 1 to N-1:
# sum_{i=1}^{N-d} |Y_{i+d} - Y_i| = ?

# We can precompute for all d in O(N) using the following:

# For fixed d, define array A_d = [|Y_{i+d} - Y_i| for i=1..N-d]

# sum over i of A_d[i] = ?

# We can precompute prefix sums of Y to get sum of Y_{i+d} and sum of Y_i.

# But absolute value complicates.

# Since Y is a permutation, values are distinct.

# Let's try to rewrite sum_{i=1}^{N-d} |Y_{i+d} - Y_i| = sum_{i=1}^{N-d} (Y_{i+d} - Y_i) if Y_{i+d} > Y_i else (Y_i - Y_{i+d})

# But no direct pattern.

# Alternative approach:

# Let's consider the array of pairs (Y_i, i).

# Sort by Y_i.

# Then for each pair (i,j), |Y_j - Y_i| = |j - i| because Y is a permutation of 1..N.

# Wait, no, Y_i is value, i is index.

# But Y is permutation of 1..N, so values are 1..N in some order.

# So difference in Y-values is |Y_j - Y_i|.

# But we want sum over i<j of (j - i) * 2^{j - i - 1} for x, and sum over i<j of |Y_j - Y_i| * 2^{j - i - 1} for y.

# Let's try to compute sum_y similarly to sum_x but with Y-values sorted by index.

# Let's define an array A = Y

# We want sum_{i<j} (A_j - A_i) * 2^{j - i - 1} (since A_j > A_i or vice versa, but sum over all pairs)

# But absolute value complicates.

# Let's split sum_y into two parts:

# sum_y = sum_{i<j, A_j > A_i} (A_j - A_i) * 2^{j - i - 1} + sum_{i<j, A_j < A_i} (A_i - A_j) * 2^{j - i - 1}

# sum_y = sum_{i<j} (A_j - A_i) * sgn(A_j - A_i) * 2^{j - i - 1}

# But sgn is ±1, so sum_y = sum_{i<j} |A_j - A_i| * 2^{j - i - 1}

# Let's consider the array A.

# We can try to compute sum_y by sorting pairs by A_i.

# Let's try to fix the approach:

# Let's consider the array A = Y.

# For each pair (i,j), i<j, contribution is |A_j - A_i| * 2^{j - i - 1}

# Let's fix the difference d = j - i.

# For each d in [1..N-1], sum_{i=1}^{N-d} |A_{i+d} - A_i| * 2^{d-1}

# So sum_y = sum_{d=1}^{N-1} 2^{d-1} * sum_{i=1}^{N-d} |A_{i+d} - A_i|

# So we need to compute sum_{i=1}^{N-d} |A_{i+d} - A_i| for all d.

# This is O(N^2) if done naively.

# But we can precompute prefix sums of A and prefix sums of absolute differences.

# Let's try to precompute prefix sums of A:

# prefix_A[i] = sum_{k=1}^i A_k

# Then sum_{i=1}^{N-d} (A_{i+d} - A_i) = prefix_A[N] - prefix_A[d] - (prefix_A[N-d] - prefix_A[0]) = ?

# But this is sum of differences without absolute value.

# So we cannot use prefix sums directly for absolute values.

# Alternative approach:

# Since Y is a permutation of 1..N, values are distinct.

# Let's consider the array A.

# For each d, sum_{i=1}^{N-d} |A_{i+d} - A_i| = sum_{i=1}^{N-d} (A_{i+d} - A_i) if A_{i+d} > A_i else (A_i - A_{i+d})

# But no direct pattern.

# Let's try to compute sum_y by a different approach:

# sum_y = sum_{i<j} |Y_j - Y_i| * 2^{j - i - 1}

# Let's fix the difference in Y-values: for each pair (u,v) with u<v, find all pairs (i,j) with Y_i = u, Y_j = v, i<j.

# But Y is a permutation, so for each value v in 1..N, we know its position pos[v] = index of value v in Y.

# So for each pair (u,v), u<v, positions are pos[u], pos[v].

# If pos[u] < pos[v], then pair (pos[u], pos[v]) contributes (v - u) * 2^{pos[v] - pos[u] - 1}

# If pos[v] < pos[u], then pair (pos[v], pos[u]) contributes (v - u) * 2^{pos[u] - pos[v] - 1}

# So sum_y = sum_{u<v} (v - u) * 2^{|pos[v] - pos[u]| - 1}

# So we can iterate over all pairs u<v, compute contribution.

# But O(N^2) is impossible.

# We need a faster way.

# Let's fix the difference d = |pos[v] - pos[u]|.

# For each d in [1..N-1], sum over pairs (u,v) with |pos[v] - pos[u]| = d of (v - u) * 2^{d - 1}

# So sum_y = sum_{d=1}^{N-1} 2^{d-1} * sum_{pairs (u,v): |pos[v] - pos[u]|=d, u<v} (v - u)

# We can rewrite sum_y = sum_{d=1}^{N-1} 2^{d-1} * S_d, where S_d = sum over pairs (u,v) with |pos[v] - pos[u]|=d and u<v of (v - u)

# Now, for each d, we want to compute S_d efficiently.

# Let's create an array pos_of_value where pos_of_value[v] = position of value v in Y (1-based)

pos_of_value = [0]*(N+1)
for i, val in enumerate(Y, 1):
    pos_of_value[val] = i

# For each d, we want sum over pairs (u,v) with |pos[v] - pos[u]|=d and u<v of (v - u)

# Let's fix d and consider pairs (u,v) with u<v and |pos[v] - pos[u]|=d

# For each u in [1..N], v in [u+1..N], if |pos[v] - pos[u]|=d, add (v - u)

# Let's consider all pairs (u,v) with u<v.

# For each d, we want sum over pairs (u,v) with |pos[v] - pos[u]|=d of (v - u)

# Let's fix d and iterate over all pairs (u,v) with u<v.

# But this is O(N^2).

# Alternative approach:

# For each d, we want sum over pairs (u,v) with |pos[v] - pos[u]|=d and u<v of (v - u)

# Let's consider the array pos_of_value.

# For each d, we want to find all pairs (u,v) with u<v and |pos[v] - pos[u]|=d.

# Let's fix d and for each i in [1..N-d], consider pairs (u,v) with pos[v] - pos[u] = d.

# So for each i in [1..N-d], we want pairs (u,v) with pos[v] = i + d and pos[u] = i.

# So for each i in [1..N-d], find values u and v such that pos_of_value[u] = i and pos_of_value[v] = i + d.

# So for each i, u = value with pos_of_value[u] = i, v = value with pos_of_value[v] = i + d.

# So u = value_at_pos[i], v = value_at_pos[i + d]

# value_at_pos is inverse of pos_of_value.

value_at_pos = [0]*(N+1)
for v in range(1, N+1):
    value_at_pos[pos_of_value[v]] = v

# Now for each d in [1..N-1], sum over i=1 to N-d of (v - u) where u = value_at_pos[i], v = value_at_pos[i + d]

# sum_d = sum_{i=1}^{N-d} (value_at_pos[i + d] - value_at_pos[i])

# Then sum_y = sum_{d=1}^{N-1} 2^{d-1} * sum_d

sum_y = 0
for d in range(1, N):
    s = 0
    for i in range(1, N - d + 1):
        s += value_at_pos[i + d] - value_at_pos[i]
    s %= MOD
    sum_y += s * pow2[d - 1]
    sum_y %= MOD

# Now answer = sum_x * sum_y % MOD

ans = sum_x * sum_y % MOD

print(ans)