mod = 998244353
W, H, L, R, D, U = map(int, input().split())
W += 1
H += 1

# Precompute factorials and inverse factorials for combinations
max_val = W + H + 5
fact = [1] * max_val
inv_fact = [1] * max_val
for i in range(1, max_val):
    fact[i] = fact[i - 1] * i % mod
inv_fact[-1] = pow(fact[-1], mod - 2, mod)
for i in range(max_val - 2, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

def comb(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % mod * inv_fact[n - r] % mod

def solve0(N, M):
    # Number of monotone paths from (0,0) to (N+1,M+1) minus some adjustments
    # Original: MD.Comb(N+M+2, N+1) - N*M - 2 - N - M
    res = comb(N + M + 2, N + 1)
    res -= N * M
    res -= 2
    res -= N + M
    return res % mod

def solve1(N, M):
    # Number of monotone paths from (0,0) to (N,M) minus 1
    res = comb(N + M, N) - 1
    return res % mod

ans = solve0(W, H)

# Subtract paths crossing the forbidden rectangle horizontally
for x in range(L, R + 1):
    left = solve1(x + 1, D)
    right = solve1(W - x, H - D)
    ans -= left * right
ans %= mod

# Subtract paths crossing the forbidden rectangle vertically
for y in range(D, U + 1):
    down = solve1(y + 1, L)
    up = solve1(H - y, W - L)
    ans -= down * up
ans %= mod

# Add back paths counted twice (intersection)
count_intersection = (R - L + 1) * (U - D + 1)
if count_intersection > 0:
    # solve1(N - x, M - y) is constant for all x,y in the forbidden rectangle
    # Because N-x and M-y vary, we must sum over all (x,y)
    # But original code sums solve1(N-x, M-y) over all x,y in forbidden rectangle
    # We can precompute prefix sums or do direct summation efficiently

    # To optimize, precompute prefix sums of solve1 for all possible values
    # But since W,H up to 1e6, direct precomputation is expensive.
    # Instead, note that solve1(a,b) = comb(a+b, a) -1
    # So sum over x in [L,R], y in [D,U] of solve1(W - x, H - y)
    # = sum_{x=L}^{R} sum_{y=D}^{U} (comb(W - x + H - y, W - x) -1)
    # = sum_{x=L}^{R} sum_{y=D}^{U} comb(W - x + H - y, W - x) - count_intersection

    # We can rewrite indices:
    # Let X = W - x, Y = H - y
    # x in [L,R] => X in [W - R, W - L]
    # y in [D,U] => Y in [H - U, H - D]

    # So sum over X in [W-R, W-L], Y in [H-U, H-D] of comb(X + Y, X) - count_intersection

    # We can precompute prefix sums of comb values over X+Y

    # Since ranges are contiguous and large, we can precompute prefix sums over X and Y

    # We'll precompute prefix sums of comb(x+y, x) over x and y in the required ranges.

    # To do this efficiently, we precompute prefix sums over x for fixed y, then over y.

    # But since ranges can be up to 1e6, we must do it in O(R-L+U-D) time.

    # We'll do 1D prefix sums over x for each y, then sum over y.

    # But since the ranges are large, we can do the summation in O((R-L+1)*(U-D+1)) which is up to 1e12, too large.

    # So we need a formula for sum_{x=a}^{b} comb(x + c, x)

    # Note: sum_{x=0}^{n} comb(x + k, x) = comb(n + k + 1, n)

    # Using this identity, we can compute sums efficiently.

    # sum_{x=a}^{b} comb(x + c, x) = sum_{x=0}^{b} comb(x + c, x) - sum_{x=0}^{a-1} comb(x + c, x)
    # = comb(b + c + 1, b) - comb(a - 1 + c + 1, a - 1) = comb(b + c + 1, b) - comb(a + c, a - 1)

    # Similarly for y.

    # So sum over x in [X1,X2], y in [Y1,Y2] of comb(X + Y, X) =
    # sum_{y=Y1}^{Y2} [comb(X2 + y + 1, X2) - comb(X1 -1 + y + 1, X1 -1)]

    # We can precompute prefix sums over y.

    X1 = W - R
    X2 = W - L
    Y1 = H - U
    Y2 = H - D

    def sum_comb_x_range(x1, x2, y):
        # sum_{x=x1}^{x2} comb(x + y, x)
        # = comb(x2 + y +1, x2) - comb(x1 -1 + y +1, x1 -1)
        if x1 > x2:
            return 0
        res = comb(x2 + y + 1, x2)
        if x1 > 0:
            res -= comb(x1 - 1 + y + 1, x1 - 1)
        return res % mod

    total = 0
    for y in range(Y1, Y2 + 1):
        total += sum_comb_x_range(X1, X2, y)
    total %= mod

    # subtract count_intersection for the -1 in solve1
    total -= count_intersection
    total %= mod

    ans += total
    ans %= mod

print(ans)