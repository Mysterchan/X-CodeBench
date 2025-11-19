def count_colored_grids(H, W, C):
    MOD = 998244353
    
    # The number of ways to color the grid is given by:
    # (C * (C + 1)^(H + W - 2)) % MOD
    # where (H + W - 2) is the number of additional choices we can make after the first cell.
    
    # Calculate (C + 1)^(H + W - 2) % MOD
    exponent = H + W - 2
    base = C + 1
    
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
# Print the result
print(count_colored_grids(H, W, C))