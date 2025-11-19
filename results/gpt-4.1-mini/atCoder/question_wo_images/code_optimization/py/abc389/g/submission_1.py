import sys
input = sys.stdin.readline

n, p = map(int, input().split())
edge = n * (n - 1) // 2
mid = n // 2 + 1

# Precompute combinations modulo p using Pascal's triangle
comb = [[0] * (mid) for _ in range(mid)]
for i in range(mid):
    comb[i][0] = 1
    for j in range(1, i + 1):
        comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % p

# Precompute combinations for up to edge edges (n*(n-1)/2)
# Use a 1D array for combinations to save memory and speed up
max_comb = edge + 1
fact = [1] * (max_comb)
inv_fact = [1] * (max_comb)

for i in range(1, max_comb):
    fact[i] = fact[i - 1] * i % p

# Fermat's little theorem for inverse factorial
inv_fact[max_comb - 1] = pow(fact[max_comb - 1], p - 2, p)
for i in reversed(range(max_comb - 1)):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % p

def nCr(n, r):
    if r > n or r < 0:
        return 0
    return fact[n] * inv_fact[r] % p * inv_fact[n - r] % p

# Precompute c[px][dx][pe]: number of ways to choose pe edges among px vertices and dx new vertices
# c[px][dx][pe] = number of ways to add dx vertices connected to px vertices with pe edges
# We optimize by using DP with prefix sums and only valid ranges

c = [[[0] * (edge + 1) for _ in range(mid)] for _ in range(mid)]
for px in range(mid):
    c[px][0][0] = 1
    for dx in range(n // 2):
        # max edges between px and dx vertices is px*dx
        max_edges = px * (dx + 1)
        # Use prefix sums to speed up inner loop
        prefix = [0] * (edge + 2)
        for pe in range(edge + 1):
            prefix[pe + 1] = (prefix[pe] + c[px][dx][pe]) % p
        for de in range(px * (dx + 1) + 1):
            if de > edge:
                break
            # c[px][dx+1][de] = sum over pe of c[px][dx][pe] * comb[px][de - pe]
            # but comb[px][k] = 0 if k > px or k < 0, so only k in [0, px]
            # So for each de, sum over pe in [de - px, de]
            low = max(0, de - px)
            high = de
            val = (prefix[high + 1] - prefix[low]) % p
            c[px][dx + 1][de] = val

# Precompute sc[px][dx][de]: sum over pe in [dx, de] of c[px][dx][pe] * comb[dx*(dx-1)//2][de - pe]
# comb for edges inside dx vertices (complete graph edges)
max_inner_edges = (n // 2) * (n // 2 - 1) // 2
comb_inner = [[0] * (max_inner_edges + 1) for _ in range(max_inner_edges + 1)]
for i in range(max_inner_edges + 1):
    comb_inner[i][0] = 1
    for j in range(1, i + 1):
        comb_inner[i][j] = (comb_inner[i - 1][j] + comb_inner[i - 1][j - 1]) % p

sc = [[[0] * (edge + 1) for _ in range(mid)] for _ in range(mid)]
for px in range(mid):
    for dx in range(mid):
        max_inner = dx * (dx - 1) // 2
        for de in range(edge + 1):
            res = 0
            # pe ranges from dx to de, but c[px][dx][pe] = 0 if pe < dx or pe > edge
            start = dx
            end = min(de, edge)
            # To speed up, we can precompute prefix sums for c[px][dx] and comb_inner[max_inner]
            # But since dx and px are small (<=16), direct loop is acceptable
            for pe in range(start, end + 1):
                if pe > edge or de - pe > max_inner:
                    continue
                res += c[px][dx][pe] * comb_inner[max_inner][de - pe]
            sc[px][dx][de] = res % p

# DP dimensions:
# dp[flag][e][i][j][px]
# flag: 0 or 1 (offset c4)
# e: edges used
# i: count of vertices in one partition
# j: count of vertices in other partition
# px: parameter related to BFS layers

# To reduce memory and speed up, use dictionary or sparse representation
# But since n <= 30, mid <= 16, edge <= 435, we can use arrays with careful indexing

c1 = mid
c2 = mid * mid
c3 = mid * mid * mid
c4 = (edge + 1) * mid * mid * mid

dp = [0] * (2 * (edge + 1) * mid * mid * mid)
# Initial state: dp[flag=1][e=0][i=0][j=0][px=1] = 1
dp[c2 + 1] = 1

for e in range(edge + 1):
    max_i = min(mid, e + 2)
    for i_ in range(max_i):
        max_j = min(mid, e - i_ + 2)
        for j_ in range(max_j):
            for px in range(1, mid):
                # flag=1 state
                idx1 = c4 + e * c3 + i_ * c2 + j_ * c1 + px
                val1 = dp[idx1]
                if val1:
                    q = val1 % p
                    rem = n - i_ - j_
                    max_dx = min(rem, mid - i_)
                    for dx in range(1, max_dx):
                        max_de = edge - e
                        for de in range(dx, max_de + 1):
                            comb_val = comb[rem][dx]
                            sc_val = sc[px][dx][de]
                            if sc_val == 0 or comb_val == 0:
                                continue
                            idx2 = (e + de) * c3 + (i_ + dx) * c2 + j_ * c1 + dx
                            dp[idx2] = (dp[idx2] + q * comb_val % p * sc_val) % p
                # flag=0 state
                idx0 = e * c3 + i_ * c2 + j_ * c1 + px
                val0 = dp[idx0]
                if val0:
                    q = val0 % p
                    rem = n - i_ - j_
                    max_dx = min(rem, mid - j_)
                    for dx in range(1, max_dx):
                        max_de = edge - e
                        for de in range(dx, max_de + 1):
                            comb_val = comb[rem][dx]
                            sc_val = sc[px][dx][de]
                            if sc_val == 0 or comb_val == 0:
                                continue
                            idx2 = c4 + (e + de) * c3 + i_ * c2 + (j_ + dx) * c1 + dx
                            dp[idx2] = (dp[idx2] + q * comb_val % p * sc_val) % p

tans = []
for m in range(n - 1, edge + 1):
    ans = 0
    off = m * c3 + (mid - 1) * c2 + (mid - 1) * c1
    for px in range(mid):
        ans = (ans + dp[off + px] + dp[c4 + off + px]) % p
    tans.append(ans)

print(*tans)