import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

N = int(input())
Y = list(map(int, input().split()))

# Y is a permutation of 1..N
# Points: (i, Y[i-1]) for i in [1..N]

# We want sum of bounding box areas of all subsets S with |S|>=2.
# Bounding box area = (max_x - min_x) * (max_y - min_y)
# Here x-coordinates are fixed: points are at x=1..N
# So max_x - min_x = max_i - min_i = length of the subset in x-axis
# max_y - min_y depends on Y values in subset.

# Key observations:
# - x-coordinates are fixed and sorted: 1..N
# - Y is a permutation of 1..N

# We want sum over all subsets S with size >= 2 of:
# (max_x - min_x) * (max_y - min_y)

# We can rewrite sum over all subsets S:
# sum_S (max_x - min_x)*(max_y - min_y)
# = sum_S (max_x - min_x)*(max_y) - sum_S (max_x - min_x)*(min_y)

# But this is complicated.

# Instead, use linearity and combinational counting:

# Let's fix the interval [l, r] (1 <= l < r <= N)
# The x-range is fixed: r - l
# For subsets S that have min_x = l and max_x = r,
# the bounding box width is (r - l).
# The height is (max_y - min_y) over points in S.

# For subsets S with min_x=l and max_x=r, S must include points l and r,
# and any subset of points in (l+1, r-1).

# So for each interval [l, r], consider subsets S containing points l and r,
# and any subset of points in (l+1, r-1).

# The number of such subsets is 2^(r-l-1).

# For these subsets, the bounding box width is (r-l).

# The height (max_y - min_y) depends on the subset chosen inside (l+1, r-1).

# But since subsets can be any subset of points in (l+1, r-1),
# the max_y and min_y can vary.

# To handle this, we consider the contribution of max_y and min_y separately.

# Let's define arrays:
# For each interval [l, r], we want sum over subsets S containing l and r:
# sum_S (max_y - min_y) * (r - l)

# We can write:
# sum_S (max_y - min_y) = sum_S max_y - sum_S min_y

# We can compute sum over subsets of max_y and min_y contributions.

# But this is complicated.

# Alternative approach:

# Since Y is a permutation of 1..N, we can use the following approach:

# The total sum of bounding box areas over all subsets S with size >= 2 is:
# sum_{l<r} (r - l) * sum over subsets S with min_x=l, max_x=r of (max_y - min_y)

# For fixed l,r, subsets S must include points l and r,
# and any subset of points in (l+1, r-1).

# The number of subsets is 2^{r-l-1}.

# For these subsets, max_y and min_y depend on the subset chosen in (l+1, r-1).

# Let's define:
# For interval [l,r], define M = {Y[l], Y[l+1], ..., Y[r]} (points in interval)
# We want sum over subsets S of M that include Y[l] and Y[r] of (max_y - min_y).

# Since Y[l] and Y[r] are fixed in S, min_y <= min(Y[l], Y[r]) and max_y >= max(Y[l], Y[r]).

# The points in (l+1, r-1) can increase max_y or decrease min_y.

# The sum over subsets of (max_y - min_y) can be computed by:
# sum over subsets T of points in (l+1, r-1) of (max of Y[l], Y[r], max(T) - min of Y[l], Y[r], min(T))

# This is complicated.

# Instead, use the known approach from editorial of similar problems:

# The total sum of bounding box areas over all subsets with size >= 2 is:
# sum_{l<r} (r - l) * (Y_max - Y_min) * 2^{r-l-1}

# where Y_max = max_{i in [l,r]} Y[i], Y_min = min_{i in [l,r]} Y[i]

# Because for subsets containing l and r, the bounding box width is fixed (r-l),
# and the height can be any value between Y_min and Y_max depending on subset,
# but the sum over all subsets of (max_y - min_y) is (Y_max - Y_min) * 2^{r-l-1}.

# So the problem reduces to:
# sum over all intervals [l,r], l<r of (r-l) * (max_{l..r} Y - min_{l..r} Y) * 2^{r-l-1}

# We can precompute powers of 2.

# Now, we need to efficiently compute sum over all intervals of (r-l)*(max - min)*2^{r-l-1}.

# We can split:
# sum_{l<r} (r-l)*max_{l..r}*2^{r-l-1} - sum_{l<r} (r-l)*min_{l..r}*2^{r-l-1}

# So we compute separately:
# S_max = sum_{l<r} (r-l)*max_{l..r}*2^{r-l-1}
# S_min = sum_{l<r} (r-l)*min_{l..r}*2^{r-l-1}

# Then answer = (S_max - S_min) % MOD

# To compute S_max and S_min efficiently, we use a monotonic stack approach.

# For S_max:
# For each element Y[i], find the intervals where Y[i] is the maximum.
# For each such interval, sum over all subintervals where Y[i] is max:
# sum_{l<=i<=r} (r-l)*2^{r-l-1}

# Similarly for S_min.

# We can use the standard approach:

# For each i:
# - find left boundary L where Y[i] is strictly greater than all elements in (L+1..i-1)
# - find right boundary R where Y[i] is greater or equal to all elements in (i+1..R-1)

# Then Y[i] is the max in all intervals [l,r] with L < l <= i <= r < R

# For each such interval, length = r - l

# sum over all l,r with L < l <= i <= r < R of (r-l)*2^{r-l-1} * Y[i]

# We can precompute prefix sums of 2^{k} and k*2^{k} to compute sum over lengths efficiently.

# Similarly for min.

# Implementation details:

# 1. Precompute pow2 and prefix sums:
# pow2[k] = 2^k mod MOD for k=0..N
# prefix_pow2[k] = sum_{j=0}^{k} pow2[j]
# prefix_k_pow2[k] = sum_{j=0}^{k} j*pow2[j]

# 2. For each i, find left and right boundaries for max and min using monotonic stacks.

# 3. For each i, compute contribution to S_max and S_min.

# 4. Compute answer = (S_max - S_min) % MOD

# Code follows:

pow2 = [1]*(N+1)
for i in range(1, N+1):
    pow2[i] = pow2[i-1]*2 % MOD

prefix_pow2 = [0]*(N+1)
prefix_k_pow2 = [0]*(N+1)
for i in range(N+1):
    prefix_pow2[i] = (prefix_pow2[i-1] + pow2[i]) % MOD if i>0 else pow2[0]
    prefix_k_pow2[i] = (prefix_k_pow2[i-1] + i*pow2[i]) % MOD if i>0 else 0

def get_sum(l, r):
    # sum_{k=l}^r pow2[k]
    if l > r:
        return 0
    return (prefix_pow2[r] - prefix_pow2[l-1]) % MOD if l>0 else prefix_pow2[r]

def get_sum_k(l, r):
    # sum_{k=l}^r k*pow2[k]
    if l > r:
        return 0
    return (prefix_k_pow2[r] - prefix_k_pow2[l-1]) % MOD if l>0 else prefix_k_pow2[r]

def calc_contrib(L, R, i):
    # For element at i, with boundaries L,R (exclusive)
    # intervals [l,r] with L < l <= i <= r < R
    # length = r - l
    # sum over all l,r of (r-l)*2^{r-l-1}
    # = sum_{length=1}^{R-L-1} (length)*2^{length-1} * number of intervals with length
    # number of intervals with length k = number of l,r with r-l=k and L<l<=i<=r<R
    # l in (L+1..i), r = l + k
    # r < R => l + k < R => l < R - k
    # l <= i => l <= i
    # So l in [max(L+1, i - k + 1), min(i, R - k -1)]
    # But this is complicated.

    # Alternative approach:
    # Number of intervals with length k containing i:
    # left_count = i - L
    # right_count = R - i
    # For length k, number of intervals containing i is:
    # count_k = number of pairs (l,r) with r-l = k, l <= i <= r, L < l <= i, r < R
    # l in [max(L+1, r - k), i]
    # r = l + k
    # r < R => l + k < R => l < R - k
    # So l in [L+1, min(i, R - k -1)]

    # Actually, the number of intervals of length k containing i is:
    # count_k = number of l with L < l <= i and l + k < R
    # So l <= i and l < R - k
    # So l in [L+1, min(i, R - k -1)]

    # count_k = max(0, min(i, R - k -1) - (L+1) + 1)

    # sum over k=1 to R-L-1 of k*2^{k-1}*count_k

    length_max = R - L -1
    if length_max <= 0:
        return 0

    left = L +1
    right = i

    res = 0
    # To optimize, we can iterate k from 1 to length_max
    # but length_max can be up to N ~ 2e5, too slow.

    # We can split k into ranges where count_k > 0:
    # count_k > 0 iff min(i, R - k -1) >= left
    # i >= left always true since i > L
    # So min(i, R - k -1) >= left
    # => R - k -1 >= left or i >= left
    # For k:
    # R - k -1 >= left => k <= R - left -1

    # Also k <= length_max

    # So k in [1, min(length_max, R - left -1)]

    k_max = min(length_max, R - left -1)
    if k_max < 1:
        return 0

    # For k in [1, k_max]:
    # count_k = min(i, R - k -1) - left +1
    # Since k <= R - left -1, R - k -1 >= left
    # min(i, R - k -1) = min(i, R - k -1)

    # We can split k into two parts:
    # For k where R - k -1 >= i, min(i, R - k -1) = i
    # For k where R - k -1 < i, min(i, R - k -1) = R - k -1

    # Solve R - k -1 >= i => k <= R - i -1

    k1 = min(k_max, R - i -1)
    k2 = k_max

    # sum over k=1 to k1:
    # count_k = i - left +1 = fixed
    # sum_k = (i - left +1) * sum_{k=1}^{k1} k*2^{k-1}

    fixed_count = (i - left +1) % MOD
    if k1 >= 1:
        # sum_{k=1}^{k1} k*2^{k-1} = ?
        # Use prefix sums:
        # sum_{k=1}^{k1} k*2^{k-1} = (prefix_k_pow2[k1] - prefix_k_pow2[0]) / 2
        # Because prefix_k_pow2 is sum k*2^k, we want k*2^{k-1} = (k*2^k)/2
        # So sum k*2^{k-1} = (sum k*2^k)/2

        total_k_pow2 = prefix_k_pow2[k1] - prefix_k_pow2[0]
        total_k_pow2 %= MOD
        sum_k = total_k_pow2 * pow(2, MOD-2, MOD) % MOD  # divide by 2 modulo
        res += fixed_count * sum_k
        res %= MOD

    # sum over k=k1+1 to k2:
    # count_k = (R - k -1) - left +1 = R - k - left
    # sum_k = sum_{k=k1+1}^{k2} k*2^{k-1} * (R - k - left)

    # = sum_{k=k1+1}^{k2} k*2^{k-1}*(R - left) - sum_{k=k1+1}^{k2} k*2^{k-1}*k

    # = (R - left)*sum_{k=k1+1}^{k2} k*2^{k-1} - sum_{k=k1+1}^{k2} k^2*2^{k-1}

    # We have prefix sums for k*2^k but not for k^2*2^{k-1}.

    # To avoid complexity, we can precompute k^2*2^{k-1} prefix sums.

# To handle this complexity, we use a simpler approach:

# We can rewrite the sum over intervals where Y[i] is max as:

# Number of intervals where Y[i] is max:
# count = (i - L) * (R - i)

# sum over all intervals [l,r] with L < l <= i <= r < R of (r-l)*2^{r-l-1}

# We can write sum over length k=1 to R-L-1 of k*2^{k-1} * number of intervals with length k containing i

# Number of intervals with length k containing i is:
# count_k = number of l with L < l <= i and l + k < R
# l <= i and l < R - k
# So l in [L+1, min(i, R - k -1)]
# count_k = max(0, min(i, R - k -1) - (L+1) + 1)

# We can precompute for each i:
# left_count = i - L
# right_count = R - i

# The total number of intervals is left_count * right_count

# The sum over all intervals of length k is:
# sum_{k=1}^{length_max} k*2^{k-1} * count_k

# We can precompute prefix sums of k*2^{k-1} and k^2*2^{k-1} to compute this efficiently.

# Let's precompute prefix sums for k*2^{k-1} and k^2*2^{k-1}:

max_len = N
prefix_k_pow2_half = [0]*(max_len+1)  # sum k*2^{k-1}
prefix_k2_pow2_half = [0]*(max_len+1) # sum k^2*2^{k-1}

for k in range(1, max_len+1):
    val = k * pow2[k-1] % MOD
    prefix_k_pow2_half[k] = (prefix_k_pow2_half[k-1] + val) % MOD
    val2 = k * k % MOD * pow2[k-1] % MOD
    prefix_k2_pow2_half[k] = (prefix_k2_pow2_half[k-1] + val2) % MOD

def sum_k_pow2(l, r):
    if l > r:
        return 0
    return (prefix_k_pow2_half[r] - prefix_k_pow2_half[l-1]) % MOD if l>0 else prefix_k_pow2_half[r]

def sum_k2_pow2(l, r):
    if l > r:
        return 0
    return (prefix_k2_pow2_half[r] - prefix_k2_pow2_half[l-1]) % MOD if l>0 else prefix_k2_pow2_half[r]

def contribution(L, R, i):
    # L,R exclusive boundaries
    left_count = i - L
    right_count = R - i
    length_max = R - L -1
    if length_max <= 0:
        return 0

    res = 0
    # sum over k=1 to length_max of k*2^{k-1} * count_k
    # count_k = max(0, min(i, R - k -1) - (L+1) +1)
    # = max(0, min(i, R - k -1) - L)

    # Define f(k) = min(i, R - k -1) - L
    # For k where R - k -1 >= i, f(k) = i - L
    # For k where R - k -1 < i, f(k) = R - k -1 - L

    # Find k0 where R - k0 -1 = i => k0 = R - i -1

    k0 = R - i -1
    if k0 < 1:
        k0 = 0
    if k0 > length_max:
        k0 = length_max

    # For k in [1, k0]:
    # count_k = i - L
    c1 = (i - L) % MOD
    if k0 >= 1:
        s1 = sum_k_pow2(1, k0)
        res += c1 * s1
        res %= MOD

    # For k in [k0+1, length_max]:
    # count_k = R - k -1 - L = (R - L -1) - k = length_max - k
    if k0 < length_max:
        s2_1 = sum_k_pow2(k0+1, length_max)  # sum k*2^{k-1}
        s2_2 = sum_k2_pow2(k0+1, length_max) # sum k^2*2^{k-1}
        res += length_max * s2_1 - s2_2
        res %= MOD

    return res

# Monotonic stack for max:
stack = []
Lmax = [-1]*N
Rmax = [N]*N

for i in range(N):
    while stack and Y[stack[-1]] < Y[i]:
        Rmax[stack[-1]] = i
        stack.pop()
    stack.append(i)
stack.clear()
for i in range(N-1, -1, -1):
    while stack and Y[stack[-1]] <= Y[i]:
        Lmax[stack[-1]] = i
        stack.pop()
    stack.append(i)

# Monotonic stack for min:
stack.clear()
Lmin = [-1]*N
Rmin = [N]*N

for i in range(N):
    while stack and Y[stack[-1]] > Y[i]:
        Rmin[stack[-1]] = i
        stack.pop()
    stack.append(i)
stack.clear()
for i in range(N-1, -1, -1):
    while stack and Y[stack[-1]] >= Y[i]:
        Lmin[stack[-1]] = i
        stack.pop()
    stack.append(i)

Smax = 0
for i in range(N):
    c = contribution(Lmax[i], Rmax[i], i)
    Smax += Y[i] * c
    Smax %= MOD

Smin = 0
for i in range(N):
    c = contribution(Lmin[i], Rmin[i], i)
    Smin += Y[i] * c
    Smin %= MOD

ans = (Smax - Smin) % MOD
print(ans)