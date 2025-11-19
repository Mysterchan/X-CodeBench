MOD = 998244353

def modinv(a, m=MOD):
    return pow(a, m - 2, m)

def precompute_factorials(n):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (n + 1)
    inv_fact[n] = modinv(fact[n])
    for i in range(n - 1, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    return fact, inv_fact

def comb(n, k, fact, inv_fact):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

def count_paths(x1, y1, x2, y2, fact, inv_fact):
    if x2 < x1 or y2 < y1:
        return 0
    dx = x2 - x1
    dy = y2 - y1
    return comb(dx + dy, dx, fact, inv_fact)

W, H, L, R, D, U = map(int, input().split())

max_val = W + H + 10
fact, inv_fact = precompute_factorials(max_val)

total = 0

# Case 1: Start from left region (x < L)
if L > 0:
    for x in range(L):
        for y in range(H + 1):
            paths_to_end = 0
            # End in left region
            for ex in range(x, L):
                for ey in range(y, H + 1):
                    paths_to_end = (paths_to_end + count_paths(x, y, ex, ey, fact, inv_fact)) % MOD
            # End in right region
            if R < W:
                for ex in range(R + 1, W + 1):
                    for ey in range(y, H + 1):
                        paths_to_end = (paths_to_end + count_paths(x, y, ex, ey, fact, inv_fact)) % MOD
            # End in bottom region
            if D > 0:
                for ex in range(x, W + 1):
                    for ey in range(y, min(D, H + 1)):
                        paths_to_end = (paths_to_end + count_paths(x, y, ex, ey, fact, inv_fact)) % MOD
            # End in top region
            if U < H:
                for ex in range(x, W + 1):
                    for ey in range(max(y, U + 1), H + 1):
                        paths_to_end = (paths_to_end + count_paths(x, y, ex, ey, fact, inv_fact)) % MOD
            total = (total + paths_to_end) % MOD

# Case 2: Start from right region (x > R)
if R < W:
    for x in range(R + 1, W + 1):
        for y in range(H + 1):
            paths_to_end = count_paths(x, y, W, H, fact, inv_fact)
            total = (total + paths_to_end) % MOD

# Case 3: Start from bottom region (y < D, L <= x <= R)
if D > 0:
    for x in range(L, R + 1):
        for y in range(D):
            paths_to_end = count_paths(x, y, W, H, fact, inv_fact)
            total = (total + paths_to_end) % MOD

# Case 4: Start from top region (y > U, L <= x <= R)
if U < H:
    for x in range(L, R + 1):
        for y in range(U + 1, H + 1):
            paths_to_end = count_paths(x, y, W, H, fact, inv_fact)
            total = (total + paths_to_end) % MOD

print(total)