import sys
input = sys.stdin.readline

mod = 998244353

h, w = map(int, input().split())
if h < w:
    h, w = w, h

# Precompute factorials and inverse factorials for combinations
max_n = w + 10
fac = [1] * (max_n + 1)
finv = [1] * (max_n + 1)
for i in range(2, max_n + 1):
    fac[i] = fac[i - 1] * i % mod
finv[max_n] = pow(fac[max_n], mod - 2, mod)
for i in range(max_n, 0, -1):
    finv[i - 1] = finv[i] * i % mod

def comb(n, r):
    if r < 0 or r > n:
        return 0
    return fac[n] * finv[r] % mod * finv[n - r] % mod

# dp[i][j]: sum of values for i rows and j columns chosen
# cnt[i][j]: count of ways for i rows and j columns chosen
dp = [0] * (w + 1)
cnt = [0] * (w + 1)
cnt[0] = 1

for i in range(h):
    ndp = [0] * (w + 1)
    ncnt = [0] * (w + 1)
    for j in range(w + 1):
        c = cnt[j]
        d = dp[j]
        if c == 0:
            continue
        max_k = w - j
        # Instead of looping over k, we use prefix sums to optimize
        # But since w <= 2*10^5 and h*w <= 2*10^5, direct loop is acceptable here
        # However, we can optimize by precomputing comb values for fixed j
        # Precompute comb(k+j+1, j) for k in [0, max_k]
        # and comb(k+j+1, j-1) similarly
        # We'll do this once per j

        # Precompute comb arrays for current j
        comb_j = [0] * (max_k + 1)
        comb_jm1 = [0] * (max_k + 1)
        for k in range(max_k + 1):
            comb_j[k] = comb(k + j + 1, j)
            comb_jm1[k] = comb(k + j + 1, j - 1) if j - 1 >= 0 else 0

        for k in range(max_k + 1):
            val_c = c * comb_j[k] % mod
            ndp[k + j] = (ndp[k + j] + d * comb_j[k]) % mod
            ndp[k + j] = (ndp[k + j] + val_c * k * i) % mod
            ndp[k + j] = (ndp[k + j] + c * comb_jm1[k]) % mod
            ncnt[k + j] = (ncnt[k + j] + val_c) % mod

    dp, cnt = ndp, ncnt

ans = 0
for j in range(w + 1):
    c = cnt[j]
    d = dp[j]
    if c == 0 and d == 0:
        continue
    val = (d * comb(w, j) + c * h * (w - j) * comb(w, j)) % mod
    ans = (ans + val) % mod

print(ans)