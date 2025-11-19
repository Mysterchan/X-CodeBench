MOD = 998244353

H, W = map(int, input().split())

def pow_mod(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

# Precompute powers
W1_H = pow_mod(W + 1, H, MOD)
W1_H1 = pow_mod(W + 1, H - 1, MOD)
H1_W = pow_mod(H + 1, W, MOD)
H1_W1 = pow_mod(H + 1, W - 1, MOD)

# Sum of (W - j + 1) for j = 1 to W
sum_W_j = W * (W + 1) // 2 % MOD

# Sum of (H - i + 1) for i = 1 to H
sum_H_i = H * (H + 1) // 2 % MOD

# First term: sum over all (i,j) of (W-j+1) * (W+1)^(H-1) * (H+1)^W
term1 = (H * sum_W_j % MOD) * W1_H1 % MOD * H1_W % MOD

# Second term: sum over all (i,j) of (H-i+1) * (H+1)^(W-1) * (W+1)^H
term2 = (W * sum_H_i % MOD) * H1_W1 % MOD * W1_H % MOD

# Third term: sum over all (i,j) of (W-j+1) * (H-i+1) * (W+1)^(H-1) * (H+1)^(W-1)
term3 = (sum_W_j * sum_H_i % MOD) * W1_H1 % MOD * H1_W1 % MOD

result = (term1 + term2 - term3) % MOD
print(result)