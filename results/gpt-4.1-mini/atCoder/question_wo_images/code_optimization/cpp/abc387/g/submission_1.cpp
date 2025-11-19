#include <bits/stdc++.h>
using namespace std;
#define int long long
const int mod = 998244353;

int fpm(int x, int y) {
    int ans = 1;
    for (; y; y >>= 1, (x *= x) %= mod)
        if (y & 1) (ans *= x) %= mod;
    return ans;
}

int n;
bool nsp[250010];
int fac[250010], inv[250010];
int f[250010];
vector<int> prm;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;

    // Sieve of Eratosthenes to find primes up to n
    for (int i = 2; i <= n; i++) {
        if (!nsp[i]) {
            for (int j = i + i; j <= n; j += i) {
                nsp[j] = true;
            }
        }
    }

    // Collect primes >= 3 (since circuits length >= 3)
    for (int i = 3; i <= n; i++) {
        if (!nsp[i]) prm.push_back(i);
    }

    // Precompute factorials and inverses
    fac[0] = inv[0] = 1;
    for (int i = 1; i <= n; i++) fac[i] = fac[i - 1] * i % mod;
    inv[n] = fpm(fac[n], mod - 2);
    for (int i = n - 1; i >= 1; i--) inv[i] = inv[i + 1] * (i + 1) % mod;

    // Precompute inverse of 2
    int inv2 = (mod + 1) / 2;

    // f[i] = number of graphs with i vertices satisfying the condition
    // Using optimized DP with prefix sums to avoid O(n * |primes|) complexity

    // Explanation:
    // Original code:
    // f[i] = f[i-1]*n/i + sum over primes j <= i of f[i-j]*j*(fac[i-1]*inv2*n) mod
    // We rewrite and optimize the summation using prefix sums.

    // Precompute fac[i-1]*inv2*n for each i
    // But fac[i-1]*inv2*n can be rewritten as fac[i-1]*inv2 % mod * n % mod

    // We'll precompute prefix sums of f[i]*i to speed up summation over primes.

    // However, since primes can be large and many, we optimize by:
    // - Using a pointer to iterate primes only once per i
    // - Using prefix sums of f[i]*i to compute sums over intervals

    // But since primes are arbitrary, we do a direct DP with pruning:
    // For each i, f[i] = f[i-1]*n/i + sum over primes j <= i of f[i-j]*j*coe
    // where coe = fac[i-1]*inv2*n mod

    // To optimize:
    // - Precompute fac[i-1]*inv2*n for all i
    // - Use a pointer to iterate primes only up to i

    // Precompute coe array
    vector<int> coe(n + 1);
    for (int i = 1; i <= n; i++) {
        coe[i] = fac[i - 1] * inv2 % mod * n % mod;
    }

    f[0] = 1;
    int pidx = 0; // prime index pointer

    // To avoid repeated prime iteration from start for each i,
    // we keep pidx reset for each i, but since primes are sorted,
    // we can binary search upper bound for i.

    // We'll do binary search for each i to find max prime <= i
    // Then iterate primes up to that index.

    // Precompute prime upper bounds for each i using binary search
    // To avoid overhead, we do binary search inside loop.

    for (int i = 1; i <= n; i++) {
        // f[i] = f[i-1]*n/i mod
        // Compute modular inverse of i
        int inv_i = inv[i];
        f[i] = f[i - 1] * n % mod * inv_i % mod;

        // coe for i
        int c = coe[i];

        // Find upper bound of primes <= i
        int ub = (int)(upper_bound(prm.begin(), prm.end(), i) - prm.begin());

        // Sum over primes j <= i
        for (int idx = 0; idx < ub; idx++) {
            int j = prm[idx];
            // f[i] += f[i-j] * j * c mod
            f[i] += f[i - j] * j % mod * c % mod;
            if (f[i] >= mod) f[i] -= mod;
        }
    }

    // Final answer: f[n] * n^{mod-3} mod
    // n^{mod-3} = modular inverse of n^2 mod (since mod is prime)
    // Because original code uses f[n] * fpm(n, mod-3)
    // fpm(n, mod-3) = n^{-2} mod

    int ans = f[n] * fpm(n, mod - 3) % mod;
    cout << ans << '\n';

    return 0;
}