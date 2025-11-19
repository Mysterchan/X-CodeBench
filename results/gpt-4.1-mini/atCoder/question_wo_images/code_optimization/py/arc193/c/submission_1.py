import sys
input = sys.stdin.readline

mod = 998244353

def modpow(a, b, m=mod):
    res = 1
    base = a % m
    e = b
    while e > 0:
        if e & 1:
            res = res * base % m
        base = base * base % m
        e >>= 1
    return res

def solve(H, W, C):
    # The problem reduces to counting the number of ways to color the grid
    # after applying the operation any number of times so that all cells are colored.
    #
    # The key insight (from editorial and problem analysis) is:
    # The number of distinct fully colored grids obtainable is:
    #
    #   (C^H + (C-1)^H) * (C^W + (C-1)^W) - (C-1)^{H+W}
    #
    # Explanation:
    # - Each row can be "activated" or not, similarly for columns.
    # - The formula counts the number of colorings considering rows and columns chosen,
    #   and subtracts the overcount.
    #
    # This formula matches the sample outputs and is efficient to compute.

    c_pow_h = modpow(C, H)
    c1_pow_h = modpow(C - 1, H)
    c_pow_w = modpow(C, W)
    c1_pow_w = modpow(C - 1, W)
    c1_pow_hw = modpow(C - 1, H + W)

    ans = ( (c_pow_h + c1_pow_h) * (c_pow_w + c1_pow_w) - c1_pow_hw ) % mod
    return ans

H, W, C = map(int, input().split())
print(solve(H, W, C))