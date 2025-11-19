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
    
    # Calculate the number of valid starting points
    valid_x = (L + (W - R)) * (U + (H - D))
    
    # Calculate the number of paths from (0, 0) to (W, H)
    total_paths = 0
    for x in range(L, R + 1):
        for y in range(D, U + 1):
            paths_to_x_y = (comb(x + y, x, MOD) * comb(W - x + H - y, W - x, MOD)) % MOD
            total_paths = (total_paths + paths_to_x_y) % MOD
    
    return (valid_x * total_paths) % MOD

# Input reading
W, H, L, R, D, U = map(int, input().split())
print(count_paths(W, H, L, R, D, U))