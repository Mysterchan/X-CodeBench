def count_unique_grids(H, W, C):
    MOD = 998244353
    # The number of unique grids can be calculated as (C * (C + 1)^(H + W - 2)) % MOD
    # (C + 1)^(H + W - 2) is the number of ways to color the remaining cells after choosing the first cell
    # We need to compute (C + 1)^(H + W - 2) % MOD using modular exponentiation
    def modular_exponentiation(base, exp, mod):
        result = 1
        base = base % mod
        while exp > 0:
            if (exp % 2) == 1:  # If exp is odd, multiply base with result
                result = (result * base) % mod
            exp = exp >> 1  # exp //= 2
            base = (base * base) % mod  # base = base^2 % mod
        return result

    if H == 1 and W == 1:
        return C % MOD  # Only one cell, can be colored in C ways

    # Calculate (C + 1)^(H + W - 2) % MOD
    ways_to_color_remaining = modular_exponentiation(C + 1, H + W - 2, MOD)
    
    # Total unique grids
    total_unique_grids = (C * ways_to_color_remaining) % MOD
    return total_unique_grids

# Read input
H, W, C = map(int, input().split())
# Output the result
print(count_unique_grids(H, W, C))