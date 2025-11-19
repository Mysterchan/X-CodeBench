def count_colorings(H, W, C):
    MOD = 998244353
    
    # Calculate the number of ways to color the grid
    # Each cell can be colored in C ways, and there are H * W cells
    # However, we need to consider that all cells must be colored
    # The number of valid configurations is C * (C - 1)^(H + W - 1)
    
    # Total cells
    total_cells = H * W
    
    # Calculate (C - 1)^(H + W - 1) % MOD
    exponent = H + W - 1
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
    
    # Calculate the number of ways
    if C == 1:
        return 1 if H == 1 and W == 1 else 0
    
    ways = (C * mod_exp(base, exponent, MOD)) % MOD
    return ways

# Read input
H, W, C = map(int, input().split())
# Output the result
print(count_colorings(H, W, C))