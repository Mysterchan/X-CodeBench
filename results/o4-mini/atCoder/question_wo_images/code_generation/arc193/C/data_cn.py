def count_colored_grids(H, W, C):
    MOD = 998244353
    # The number of ways to color the grid is C * (C - 1)^(H + W - 2)
    # We need to calculate (C - 1)^(H + W - 2) % MOD
    if H == 1 and W == 1:
        return C % MOD
    
    exponent = H + W - 2
    base = C - 1
    
    # Fast exponentiation
    def mod_exp(base, exp, mod):
        result = 1
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp //= 2
        return result
    
    ways = (C * mod_exp(base, exponent, MOD)) % MOD
    return ways

# Read input
H, W, C = map(int, input().split())
# Output the result
print(count_colored_grids(H, W, C))