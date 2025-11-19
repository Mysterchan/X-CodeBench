#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int mod = 1e9+7;

// Fast exponentiation modulo mod
int power(int x, int n) {
    int ans = 1 % mod;
    while (n > 0) {
        if (n & 1) ans = (1LL * ans * x) % mod;
        x = (1LL * x * x) % mod;
        n >>= 1;
    }
    return ans;
}

// Modular inverse using Fermat's little theorem (mod is prime)
int modInv(int n) {
    return power(n, mod - 2);
}

// Precompute factorials and inverse factorials up to maxN
// to compute combinations efficiently modulo mod
struct Comb {
    int maxN;
    vector<int> fact, invFact;
    Comb(int n) : maxN(n), fact(n+1), invFact(n+1) {
        fact[0] = 1;
        for (int i = 1; i <= maxN; i++) {
            fact[i] = (1LL * fact[i-1] * i) % mod;
        }
        invFact[maxN] = modInv(fact[maxN]);
        for (int i = maxN - 1; i >= 0; i--) {
            invFact[i] = (1LL * invFact[i+1] * (i+1)) % mod;
        }
    }
    int nCr(int n, int r) {
        if (r > n || r < 0) return 0;
        return (1LL * fact[n] * ((1LL * invFact[r] * invFact[n-r]) % mod)) % mod;
    }
};

// Lucas theorem for nCr modulo mod (mod prime)
// but since max(a,b,k) <= 1e5, precomputation suffices
// so no need for Lucas here

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t; cin >> t;

    // max sum of max(a,b,k) over all test cases <= 1e5
    // So precompute factorials up to 3*1e5 to be safe
    // Because (a-1)*k + 1 can be up to ~1e10 theoretically,
    // but problem constraints limit sum of max(a,b,k) to 1e5,
    // so (a-1)*k can be up to 1e10 in worst case? No, since a,b,k <= 1e5,
    // max (a-1)*k <= 1e10 which is too large for factorial precomputation.
    // So we must use Lucas theorem or a different approach.

    // But the original code uses comb_lr which uses Lucas theorem.
    // We'll implement Lucas theorem with precomputed factorials up to mod-1 (which is huge).
    // Instead, since mod=1e9+7 is large prime, and a,b,k <= 1e5,
    // (a-1)*k + 1 can be up to 1e10, so we must implement Lucas theorem.

    // We'll implement comb_small for nCr mod mod for n,k < mod
    // and comb_lr for large n,k using Lucas theorem.

    // Precompute factorials up to mod-1 is impossible.
    // So we precompute factorials up to maxN = 1e5 (max input)
    // and implement Lucas theorem for large n,k.

    // Let's implement comb_small and comb_lr as in original code but optimized.

    const int MAX = 100000; // max a,b,k
    vector<int> fact(MAX+1), invFact(MAX+1);

    fact[0] = 1;
    for (int i = 1; i <= MAX; i++) fact[i] = (1LL * fact[i-1] * i) % mod;
    invFact[MAX] = modInv(fact[MAX]);
    for (int i = MAX-1; i >= 0; i--) invFact[i] = (1LL * invFact[i+1] * (i+1)) % mod;

    auto comb_small = [&](int n, int k) -> int {
        if (k < 0 || k > n) return 0;
        return (1LL * fact[n] * ((1LL * invFact[k] * invFact[n-k]) % mod)) % mod;
    };

    // Lucas theorem for nCr mod prime
    function<int(long long,long long)> comb_lr = [&](long long n, long long k) -> int {
        if (k > n) return 0;
        if (k == 0 || k == n) return 1;
        int res = 1;
        while (n > 0 || k > 0) {
            int ni = n % mod;
            int ki = k % mod;
            if (ki > ni) return 0;
            res = (1LL * res * comb_small(ni, ki)) % mod;
            n /= mod;
            k /= mod;
        }
        return res;
    };

    while (t--) {
        ll a, b, k; cin >> a >> b >> k;

        // n = (a-1)*k + 1 mod
        ll n = ((a - 1) * k) % mod + 1;

        // m = ((b-1)*k * C((a-1)*k + 1, a) + 1) mod
        // Use comb_lr for C((a-1)*k + 1, a)
        ll comb_val = comb_lr((a - 1) * k + 1, a);
        ll m = ((b - 1) * k) % mod;
        m = (m * comb_val) % mod;
        m = (m + 1) % mod;

        cout << n << " " << m << "\n";
    }

    return 0;
}