#include <bits/stdc++.h>
using namespace std;

constexpr int MOD = 998244353;

// Fast modular exponentiation
int modpow(int base, int exp, int mod = MOD) {
    int result = 1;
    int cur = base % mod;
    while (exp > 0) {
        if (exp & 1) result = (int)((1LL * result * cur) % mod);
        cur = (int)((1LL * cur * cur) % mod);
        exp >>= 1;
    }
    return result;
}

// Precompute smallest prime factor (spf) for factorization
// and mu (Möbius function) for all numbers up to maxN
struct MobiusSieve {
    int maxN;
    vector<int> spf, mu;
    MobiusSieve(int n) : maxN(n), spf(n+1), mu(n+1) {
        mu[1] = 1;
        for (int i = 2; i <= maxN; i++) {
            if (!spf[i]) {
                spf[i] = i;
                for (int j = i * 2; j <= maxN; j += i) {
                    if (!spf[j]) spf[j] = i;
                }
            }
            int p = spf[i];
            int x = i / p;
            if (x % p == 0) mu[i] = 0;
            else mu[i] = -mu[x];
        }
    }
};

// Precompute divisors for all numbers up to maxN
// Using a sieve approach to get divisors efficiently
vector<vector<int>> precompute_divisors(int maxN) {
    vector<vector<int>> divs(maxN+1);
    for (int i = 1; i <= maxN; i++) {
        for (int j = i; j <= maxN; j += i) {
            divs[j].push_back(i);
        }
    }
    return divs;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N; cin >> N;
    vector<int> A(N);
    int maxA = 0;
    for (int i = 0; i < N; i++) {
        cin >> A[i];
        if (A[i] > maxA) maxA = A[i];
    }

    // Precompute divisors and Möbius function
    auto divs = precompute_divisors(maxA);
    MobiusSieve ms(maxA);

    // dp[d] = exponent of prime factor corresponding to divisor d in the LCM factorization
    // Actually, dp[d] stores the exponent of the cyclotomic polynomial factor corresponding to d
    // We work modulo MOD-1 for exponents because of Fermat's little theorem on exponentiation
    const int MOD_EXP = MOD - 1;
    vector<int> dp(maxA+1, 0);
    vector<int> dp2(maxA+1, 0); // prefix sums for dp

    int64_t ans = 1;

    // We will maintain dp and dp2 as in original code but optimize inner loops

    // To speed up the inner loop, we precompute for each val:
    // For each divisor d of val:
    //   sum over q divides val/d of mu[q] * dp2[d*q]
    // This is a convolution over divisors, but we can do it efficiently by iterating over divisors.

    // To avoid recomputing mu and divisors repeatedly, we do the following:
    // For each val:
    //   For each divisor d of val:
    //     Let x = val/d
    //     We want sum_{q|x} mu[q]*dp2[d*q]
    //     We iterate over divisors q of x and accumulate accordingly.

    // This is the bottleneck in the original code.

    // Optimization:
    // Instead of recomputing for each val, we can precompute prefix sums of dp2 and use Möbius inversion.

    // But since val can be large and many, we keep the same approach but optimize loops and data structures.

    // We'll implement the same logic but with faster I/O and no unnecessary overhead.

    for (int val : A) {
        // For each divisor d of val
        for (int d : divs[val]) {
            int x = val / d;
            int64_t dlt = 0;
            // sum over q divides x of mu[q]*dp2[d*q]
            for (int q : divs[x]) {
                int idx = d * q;
                if (ms.mu[q] == 1) {
                    dlt += dp2[idx];
                } else if (ms.mu[q] == -1) {
                    dlt -= dp2[idx];
                }
            }
            dlt = ((-1 - dlt) % MOD_EXP + MOD_EXP) % MOD_EXP; // dlt = (MOD_EXP - 1 - dlt) mod MOD_EXP

            dp[d] = (dp[d] + dlt) % MOD_EXP;

            // f = 10^d - 1 mod MOD
            int f = modpow(10, d) - 1;
            if (f < 0) f += MOD;

            // ans = ans * f^dlt mod MOD
            // dlt can be zero or positive modulo MOD_EXP
            ans = (ans * modpow(f, (int)dlt)) % MOD;

            // Update dp2 for all divisors of d
            for (int d2 : divs[d]) {
                dp2[d2] = (dp2[d2] + (int)dlt) % MOD_EXP;
            }
        }
        // Output ans * inverse(9) mod MOD
        // Because R_n = (10^n - 1)/9, so we multiply by inverse(9) to get R_n mod MOD
        int inv9 = 443664157; // precomputed inverse of 9 mod 998244353
        cout << (ans * (int64_t)inv9 % MOD) << "\n";
    }

    return 0;
}