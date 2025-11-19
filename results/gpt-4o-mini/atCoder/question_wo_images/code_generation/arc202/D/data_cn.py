MOD = 998244353

def mod_inv(a, p):
    return pow(a, p - 2, p)

def comb(n, k):
    if n < k or k < 0:
        return 0
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator = numerator * (n - i) % MOD
        denominator = denominator * (i + 1) % MOD
    return numerator * mod_inv(denominator, MOD) % MOD

def count_paths(H, W, T, A, B, C, D):
    delta_row = C - A
    delta_col = D - B
    
    if (abs(delta_row) + abs(delta_col)) % 2 != T % 2 or (abs(delta_row) + abs(delta_col)) > T:
        return 0
    
    x = (T + delta_row) // 2
    y = (T - delta_row) // 2
    p = (T + delta_col) // 2
    q = (T - delta_col) // 2
    
    if any(v < 0 for v in [x, y, p, q]) or (x + y > T) or (p + q > T):
        return 0
    
    # Compute combinations:
    paths_row = comb(T, x) * comb(T - x, p) % MOD
    return paths_row

def main():
    import sys
    input = sys.stdin.read
    H, W, T, A, B, C, D = map(int, input().strip().split())
    
    result = count_paths(H, W, T, A, B, C, D)
    print(result)

if __name__ == "__main__":
    main()