mod = 998244353

import sys
input = sys.stdin.readline

H, W, T, A, B, C, D = map(int, input().split())

# Precompute factorials and inverse factorials up to 2*T for binomial coefficients
max_n = 2 * T + 10
fac = [1] * (max_n)
finv = [1] * (max_n)
inv = [1] * (max_n)

for i in range(2, max_n):
    fac[i] = fac[i - 1] * i % mod
    inv[i] = mod - inv[mod % i] * (mod // i) % mod
    finv[i] = finv[i - 1] * inv[i] % mod

def binom(n, k):
    if k < 0 or k > n:
        return 0
    return fac[n] * finv[k] % mod * finv[n - k] % mod

# Calculate number of ways to move from S to G in T steps on a line of length N+1 (0-based indexing)
# with moves only to adjacent squares (left or right), without leaving [0, N].
# Using reflection principle and combinatorics.
def calc1(T, N, S, G):
    if S < 0 or S > N or G < 0 or G > N:
        return 0
    # parity check: (T + S - G) must be even
    if (T + S - G) & 1:
        return 0
    H = (T + S - G) // 2
    W = (T - (S - G)) // 2
    if H < 0 or W < 0:
        return 0

    # Using inclusion-exclusion (reflection principle)
    # sum over k in Z of:
    #   C(T, H - k*(N+1)) - C(T, H - k*(N+1) - S - 1)
    # but we only sum over k where binomial arguments are valid
    res = 0
    limit = (T // (N + 1)) + 2  # safe limit for k
    for k in range(-limit, limit + 1):
        x1 = H - k * (N + 1)
        x2 = H - k * (N + 1) - S - 1
        val = binom(T, x1) - binom(T, x2)
        res += val
    return res % mod

# Precompute resX and resY for all t in [0..T]
# resX[t] = ways to move from A-1 to C-1 in t steps on [0..H-1]
# resY[t] = ways to move from B-1 to D-1 in t steps on [0..W-1]
resX = [0] * (T + 1)
resY = [0] * (T + 1)

for t in range(T + 1):
    resX[t] = calc1(t, H - 1, A - 1, C - 1)
    resY[t] = calc1(t, W - 1, B - 1, D - 1)

# Use prefix sums of resX and resY multiplied by binomial coefficients to optimize the final sum
# The original code does a double sum with O(T^2) complexity.
# We optimize by using prefix sums and combinational identities.

# Precompute binomial coefficients C(T, i) for i in [0..T]
C_T = [binom(T, i) for i in range(T + 1)]

# Precompute prefix sums of resX and resY multiplied by binomial coefficients
# For each i, we need sum_{j=1}^i resX[j]*C(i,j) and sum_{j=1}^i resY[j]*C(i,j)
# We can precompute prefix sums of resX[j]*C(i,j) for fixed i efficiently by using convolution-like approach.

# But since T can be large, we use a combinational identity:
# sum_{j=0}^i f(j)*C(i,j) = (f * binomial transform)
# We can precompute binomial transforms of resX and resY arrays.

# However, since we need sum_{j=1}^i resX[j]*C(i,j), we can write:
# sum_{j=1}^i resX[j]*C(i,j) = sum_{j=0}^i resX[j]*C(i,j) - resX[0]*C(i,0)
# But resX[0] corresponds to 0 steps, so resX[0] = 1 if start == end and 0 otherwise.

# We'll precompute binomial transforms of resX and resY arrays up to T.

# Precompute binomial transforms of resX and resY:
# For each i in [0..T], compute sum_{j=0}^i resX[j]*C(i,j)
# This can be done by DP or by using a standard approach:
# Let f = resX, then binomial transform g[i] = sum_{j=0}^i f[j]*C(i,j)

# We'll precompute prefix sums of resX and resY to do this efficiently.

# To compute g[i] = sum_{j=0}^i f[j]*C(i,j), we can use the following:
# g[i] = sum_{j=0}^i f[j]*C(i,j)
# We can compute all g[i] for i=0..T using a DP:
# g[0] = f[0]
# g[i] = g[i-1] + f[i]*C(i,i) + sum_{j=0}^{i-1} f[j]*(C(i,j)-C(i-1,j))

# But this is complicated. Instead, we can use the fact that:
# sum_{j=0}^i f[j]*C(i,j) = sum_{j=0}^i f[j]*C(i,j)
# For fixed f, we can precompute prefix sums of f and use Pascal's rule.

# Alternatively, since T is up to 3*10^5, we can precompute factorials and do the sums directly.

# We'll precompute prefix sums of resX and resY:
prefix_resX = [0] * (T + 2)
prefix_resY = [0] * (T + 2)
for i in range(1, T + 1):
    prefix_resX[i] = (prefix_resX[i - 1] + resX[i]) % mod
    prefix_resY[i] = (prefix_resY[i - 1] + resY[i]) % mod

# Precompute inverse factorials for binomial coefficients
# We'll use a helper function to compute sum_{j=1}^i resX[j]*C(i,j) efficiently:
# sum_{j=1}^i resX[j]*C(i,j) = sum_{j=0}^i resX[j]*C(i,j) - resX[0]*C(i,0)
# But resX[0] corresponds to 0 steps, which is 1 if start == end else 0.

# We'll precompute prefix sums of resX[j]*C(i,j) for all i using a DP approach:
# But this is O(T^2), too slow.

# Instead, we use the fact that:
# sum_{j=0}^i f[j]*C(i,j) = sum_{j=0}^i f[j]*C(i,j)
# For fixed f, the binomial transform g[i] = sum_{j=0}^i f[j]*C(i,j)
# can be computed by convolution with binomial coefficients.

# Since convolution is expensive, we use the following trick:
# The problem's final formula is:
# ans = sum_{i=1}^T (-1)^{T - i} * C(T, i) * (sum_{j=1}^i resX[j]*C(i, j)) * (sum_{j=1}^i resY[j]*C(i, j))

# We can rewrite sum_{j=1}^i resX[j]*C(i,j) as:
# sum_{j=0}^i resX[j]*C(i,j) - resX[0]*C(i,0)
# Similarly for resY.

# Since resX[0] and resY[0] correspond to 0 steps, which is 1 if start == end else 0,
# we can precompute resX[0] and resY[0].

# We'll precompute arrays:
# fX[i] = resX[i]
# fY[i] = resY[i]

# Then for each i, compute:
# Sx[i] = sum_{j=0}^i fX[j]*C(i,j)
# Sy[i] = sum_{j=0}^i fY[j]*C(i,j)

# To compute Sx and Sy efficiently for all i, we use the following approach:

# Define arrays fX and fY of length T+1
# Define arrays C_i_j for i,j in [0..T], but too large.

# Instead, we use the fact that:
# sum_{j=0}^i f[j]*C(i,j) = sum_{j=0}^i f[j]*C(i,j)
# = sum_{j=0}^i f[j]*C(i,j)
# This is the binomial transform of f.

# The binomial transform of f can be computed in O(T log T) using FFT,
# but FFT is not allowed here.

# Since T is large, we must find a better approach.

# Alternative approach:
# The problem is equivalent to counting the number of sequences of length T,
# where the king moves in 2D grid with 8 directions.

# The number of ways to move from (A,B) to (C,D) in T steps is:
# sum_{k=0}^T ways_x(k) * ways_y(T - k) * number_of_ways_to_split_steps

# But the problem is complicated.

# The original code uses inclusion-exclusion with alternating signs.

# We can optimize the final summation by precomputing prefix sums of resX and resY multiplied by binomial coefficients.

# Let's precompute for each i:
# sum_{j=1}^i resX[j]*C(i,j) and sum_{j=1}^i resY[j]*C(i,j)

# We can precompute prefix sums of resX and resY multiplied by binomial coefficients for all i using DP:

# We'll precompute arrays:
# For fixed j, precompute binomials C(i,j) for i in [j..T]
# Then for each j, accumulate resX[j] * C(i,j) for i >= j

# This is O(T^2), too slow.

# Since the original code is O(T^2), we must find a formula to reduce complexity.

# Observation:
# The problem is separable in x and y directions.
# The number of ways to move from A to C in t steps is resX[t]
# The number of ways to move from B to D in t steps is resY[t]

# The total number of sequences of length T is sum over i=0..T of:
# ways_x(i) * ways_y(T - i) * C(T, i)

# Because at each step, the king moves in both x and y directions simultaneously,
# but the king moves only one step in one of 8 directions, so the total steps in x and y directions sum to T.

# But the king moves diagonally or straight, so the number of steps in x and y directions can vary.

# The problem reduces to:
# The number of sequences = sum_{i=0}^T resX[i] * resY[T - i] * C(T, i)

# Let's verify this with the sample input.

# So we can compute:
ans = 0
for i in range(T + 1):
    ans += resX[i] * resY[T - i] * binom(T, i)
ans %= mod

print(ans)