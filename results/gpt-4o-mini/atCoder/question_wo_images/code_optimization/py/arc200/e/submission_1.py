def solve():
    MOD = 998244353

    def main(n, m):
        if n == 1:
            return m + 1

        # Basic combinations for counting
        pow_m = pow(m, n - 1, MOD)
        pow2_n_minus_1 = pow(2, n - 1, MOD)

        # Start calculating answer
        ans = pow_m
        
        # Adjusting answer for constraints
        ans += pow_m - pow2_n_minus_1
        ans += (pow2_n_minus_1 - 1) * (m - 1) * pow(2, MOD - 2, MOD) % MOD
        ans %= MOD

        if n >= 4:
            pow4_n_minus_1 = pow(4, n - 1, MOD)
            pow3_n_minus_1 = pow(3, n - 1, MOD)

            ans += pow4_n_minus_1 - 3 * pow3_n_minus_1 + 3 * pow2_n_minus_1 - 1
            ans %= MOD

            # Calculate combinations
            mC3 = m * (m - 1) % MOD * (m - 2) % MOD * pow(6, MOD - 2, MOD) % MOD  # Using modular inverse of 6
            mC2 = m * (m - 1) // 2 % MOD

            ans += (pow4_n_minus_1 - 3 * pow3_n_minus_1 + 3 * pow2_n_minus_1 - 1) * (mC3 + mC2) % MOD
            ans %= MOD

        ans *= pow(2, m, MOD)
        ans %= MOD

        return ans

    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        ans = main(n, m)
        print(ans)

solve()