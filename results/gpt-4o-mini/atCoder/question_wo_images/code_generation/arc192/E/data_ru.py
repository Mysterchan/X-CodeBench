def modinv(a, p):
    return pow(a, p - 2, p)

def comb(n, k, p):
    if k > n or k < 0:
        return 0
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator = (numerator * (n - i)) % p
        denominator = (denominator * (i + 1)) % p
    return (numerator * modinv(denominator, p)) % p

def count_paths(W, H, L, R, D, U):
    MOD = 998244353
    
    # Count blocks in each of the four regions
    total_paths = 0
    
    # Region 1: x < L and y < D
    if L > 0 and D > 0:
        total_paths += comb(L + D - 2, L - 1, MOD)
        total_paths %= MOD
    
    # Region 2: L <= x <= R and y < D
    if D > 0 and L <= R:
        for x in range(L, R + 1):
            total_paths += comb(x + D - 1, x, MOD)
            total_paths %= MOD
    
    # Region 3: x < L and D <= y <= U
    if L > 0 and U >= D:
        for y in range(D, U + 1):
            total_paths += comb(L + y - 1, L - 1, MOD)
            total_paths %= MOD
    
    # Region 4: L <= x <= R and D <= y <= U
    if L <= R and U >= D:
        for x in range(L, R + 1):
            for y in range(D, U + 1):
                total_paths += comb(x + y, x, MOD)
                total_paths %= MOD
    
    # Region 5: x > R and y < D
    if R < W and D > 0:
        for x in range(R + 1, W + 1):
            total_paths += comb(x + D - 1, x, MOD)
            total_paths %= MOD
    
    # Region 6: x > R and D <= y <= U
    if R < W and U >= D:
        for y in range(D, U + 1):
            total_paths += comb(W + y, W, MOD)
            total_paths %= MOD
    
    # Region 7: x < L and y > U
    if L > 0 and U < H:
        for x in range(L):
            total_paths += comb(x + (H - U - 1), x, MOD)
            total_paths %= MOD
    
    # Region 8: L <= x <= R and y > U
    if L <= R and U < H:
        for x in range(L, R + 1):
            total_paths += comb(x + (H - U - 1), x, MOD)
            total_paths %= MOD
    
    # Region 9: x > R and y > U
    if R < W and U < H:
        for x in range(R + 1, W + 1):
            total_paths += comb(x + (H - U - 1), x, MOD)
            total_paths %= MOD
    
    return total_paths

W, H, L, R, D, U = map(int, input().split())
print(count_paths(W, H, L, R, D, U))