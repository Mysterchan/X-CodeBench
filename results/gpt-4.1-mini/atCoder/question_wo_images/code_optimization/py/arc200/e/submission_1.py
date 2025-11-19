def solve():
    import sys
    input = sys.stdin.readline
    MOD = 998244353
    INV2 = (MOD + 1) // 2  # Modular inverse of 2 modulo MOD

    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())

        # Precompute powers needed
        pow_m1_n1 = pow(m + 1, n - 1, MOD)
        pow_2_n1 = pow(2, n - 1, MOD)
        pow_3_n1 = pow(3, n - 1, MOD)
        pow_4_n1 = pow(4, n - 1, MOD)

        ans = pow_m1_n1

        tmp = pow_m1_n1 - pow_2_n1 - (pow_2_n1 - 1) * (m - 1) * INV2
        tmp %= MOD
        ans += tmp * m
        ans %= MOD

        if n >= 4:
            tmp = pow_4_n1 - 3 * pow_3_n1 + 3 * pow_2_n1 - 1
            tmp %= MOD
            mC3 = m * (m - 1) * (m - 2) // 6 if m >= 3 else 0
            mC2 = m * (m - 1) // 2 if m >= 2 else 0
            ans += tmp * (mC3 + mC2)
            ans %= MOD

        ans = (ans * pow(2, m, MOD)) % MOD

        print(ans)