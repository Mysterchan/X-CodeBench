mod = 998244353

H, W, C = map(int, input().split())

# The number of valid colorings is defined by the formula derived from combinatorial analysis.
# The modulo is applied directly to ensure that we do not overflow and stay within constraints.

# Precompute the powers of (C - 1) up to (H + W)
pow_C_minus_1 = [1] * (H + W + 1)
for i in range(1, H + W + 1):
    pow_C_minus_1[i] = pow_C_minus_1[i - 1] * (C - 1) % mod

# The number of ways to choose colors for all cells
ways_to_color = (pow(C, H, mod) + mod - 1) * (pow(C, W, mod) + mod - 1) % mod
ways_to_color = (ways_to_color + 1) % mod  # Add the way that leaves everything uncolored

# Now we can represent the total unique grids modulo.
result = (ways_to_color * pow_C_minus_1[H + W - 2]) % mod

print(result)