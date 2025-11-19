import sys
input = sys.stdin.readline

n, p = map(int, input().split())
edge = n * (n - 1) // 2
mid = n // 2 + 1

# Precompute binomial coefficients
lim = 500
comb = [[0] * lim for _ in range(lim)]
for i in range(lim):
    comb[i][0] = 1
    if i < lim:
        comb[i][i] = 1
    for j in range(1, min(i, lim)):
        comb[i][j] = (comb[i-1][j] + comb[i-1][j-1]) % p

# Precompute c array
c = [[[0] * (edge + 1) for _ in range(mid)] for _ in range(mid)]
for px in range(mid):
    c[px][0][0] = 1
    for dx in range(n // 2):
        for pe in range(edge + 1):
            if c[px][dx][pe]:
                val = c[px][dx][pe]
                for de in range(1, edge + 1 - pe):
                    c[px][dx+1][pe+de] = (c[px][dx+1][pe+de] + val * comb[px][de]) % p

# Precompute sc array
sc = [[[0] * (edge + 1) for _ in range(mid)] for _ in range(mid)]
for px in range(mid):
    for dx in range(mid):
        max_internal = dx * (dx - 1) // 2
        for de in range(edge + 1):
            res = 0
            for pe in range(dx, min(de + 1, edge + 1)):
                if de - pe <= max_internal:
                    res = (res + c[px][dx][pe] * comb[max_internal][de - pe]) % p
            sc[px][dx][de] = res

# Use dictionary for sparse DP
dp = [{} for _ in range(2)]
dp[0][(0, 1, 0)] = 1

for e in range(edge + 1):
    curr = e & 1
    next_dp = 1 - curr
    dp[next_dp].clear()
    
    for (i, j, px), q in dp[curr].items():
        if e != i + j - 1:
            continue
        
        # Process transitions from layer 0
        if px > 0:
            for dx in range(1, min(n + 1 - i - j, mid - i)):
                coeff = (comb[n - i - j][dx] * q) % p
                for de in range(dx, edge + 1 - e):
                    new_e = e + de
                    new_i = i + dx
                    key = (new_i, j, dx)
                    val = (coeff * sc[px][dx][de]) % p
                    dp[next_dp][key] = (dp[next_dp].get(key, 0) + val) % p
        
        # Process transitions to layer 1
        for dx in range(1, min(n + 1 - i - j, mid - j)):
            coeff = (comb[n - i - j][dx] * q) % p
            for de in range(dx, edge + 1 - e):
                new_e = e + de
                new_j = j + dx
                key = (i, new_j, dx)
                val = (coeff * sc[px][dx][de]) % p
                dp[next_dp][key] = (dp[next_dp].get(key, 0) + val) % p

# Collect answers
tans = []
for m in range(n - 1, edge + 1):
    ans = 0
    curr = m & 1
    for (i, j, px), val in dp[curr].items():
        if i == mid - 1 and j == mid - 1 and i + j - 1 == m:
            ans = (ans + val) % p
    tans.append(ans)

print(*tans)