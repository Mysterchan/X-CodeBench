MOD = 998244353

def modinv(a, m=MOD):
    return pow(a, m-2, m)

def precompute_factorials(n):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i-1] * i % MOD
    inv_fact = [1] * (n + 1)
    inv_fact[n] = modinv(fact[n])
    for i in range(n-1, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
    return fact, inv_fact

def comb(n, k, fact, inv_fact):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n-k] % MOD

W, H, L, R, D, U = map(int, input().split())

max_val = W + H + 1
fact, inv_fact = precompute_factorials(max_val)

# Count valid districts
total_districts = (W+1)*(H+1) - (R-L+1)*(U-D+1)

result = total_districts  # Paths of length 0

# Count paths that move
# Split into 4 regions
regions = []
if L > 0:
    regions.append((0, L-1, 0, H))
if R < W:
    regions.append((R+1, W, 0, H))
if D > 0:
    regions.append((L, R, 0, D-1))
if U < H:
    regions.append((L, R, U+1, H))

for x1_min, x1_max, y1_min, y1_max in regions:
    for x2_min, x2_max, y2_min, y2_max in regions:
        for x1 in range(x1_min, x1_max+1):
            for y1 in range(y1_min, y1_max+1):
                for x2 in range(max(x1, x2_min), x2_max+1):
                    for y2 in range(max(y1, y2_min), y2_max+1):
                        if x1 == x2 and y1 == y2:
                            continue
                        
                        dx = x2 - x1
                        dy = y2 - y1
                        paths = comb(dx + dy, dx, fact, inv_fact)
                        
                        # Check if path goes through forbidden region
                        if x1 <= R and L <= x2 and y1 <= U and D <= y2:
                            # Subtract paths going through forbidden region
                            for mx in range(max(L, x1), min(R, x2)+1):
                                for my in range(max(D, y1), min(U, y2)+1):
                                    bad = comb((mx-x1)+(my-y1), mx-x1, fact, inv_fact)
                                    bad = bad * comb((x2-mx)+(y2-my), x2-mx, fact, inv_fact) % MOD
                                    paths = (paths - bad) % MOD
                        
                        result = (result + paths) % MOD

print(result)