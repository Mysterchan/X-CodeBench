#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int mod = 998244353;

// Fast exponentiation modulo mod
ll qpow(ll a, ll b) {
    ll ret = 1 % mod;
    a %= mod;
    while (b > 0) {
        if (b & 1) ret = ret * a % mod;
        a = a * a % mod;
        b >>= 1;
    }
    return ret;
}

// Precompute factorials and inverse factorials for combinations
// Since M < 998244353, we can precompute factorials up to max M in input
// But M can be up to 998244352, which is too large to precompute factorials for all test cases.
// However, we only need C(m,2) and C(m,3), which can be computed directly using formula:
// C(m,2) = m*(m-1)/2 mod
// C(m,3) = m*(m-1)*(m-2)/6 mod

inline ll modinv(ll a) {
    // Fermat's little theorem since mod is prime
    return qpow(a, mod - 2);
}

inline ll C2(ll m) {
    if (m < 2) return 0;
    return (m * (m - 1) % mod) * modinv(2) % mod;
}

inline ll C3(ll m) {
    if (m < 3) return 0;
    return (m * (m - 1) % mod) * (m - 2) % mod * modinv(6) % mod;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while (T--) {
        ll n, m; cin >> n >> m;

        // Compute combinations
        ll cm2 = C2(m);
        ll cm3 = C3(m);

        // Precompute powers needed
        // qpow base and exponent can be large, but qpow is O(log n)
        // Use modulo arithmetic carefully

        // To avoid negative modulo results, define a helper function
        auto mod_sub = [](ll a, ll b) -> ll {
            a %= mod; b %= mod;
            ll res = a - b;
            if (res < 0) res += mod;
            return res;
        };

        auto mod_add = [](ll a, ll b) -> ll {
            a %= mod; b %= mod;
            ll res = a + b;
            if (res >= mod) res -= mod;
            return res;
        };

        ll p_m1 = mod_add(m, 1); // m+1 mod
        ll p_m1_pow = qpow(p_m1, n - 1);
        ll p_4 = qpow(4, n - 1);
        ll p_3 = qpow(3, n - 1);
        ll p_2 = qpow(2, n - 1);

        // Compute ans1 = (m+1)^(n-1)
        ll ans1 = p_m1_pow;

        // ans2 = C(m,2) * (4^(n-1) - 3^(n-1))
        ll ans2 = cm2 * mod_sub(p_4, p_3) % mod;

        // ans3 = C(m,3) * (4^(n-1) - 3*3^(n-1) + 3*2^(n-1) - 1)
        ll temp = mod_sub(p_4, (3 * p_3) % mod);
        temp = mod_add(temp, (3 * p_2) % mod);
        temp = mod_sub(temp, 1);
        ll ans3 = cm3 * temp % mod;

        // ans4 = m * ((m+1)^(n-1) - (m-1)*(3^(n-1) - 2^(n-1)) - 2^(n-1))
        ll part = mod_sub(p_3, p_2);
        part = (m - 1 + mod) % mod * part % mod;
        part = mod_add(part, p_2);
        part = mod_sub(p_m1_pow, part);
        ll ans4 = (m % mod) * part % mod;

        // final answer = (ans1 + ans2 + ans3 + ans4) * 2^m mod
        ll pow2m = qpow(2, m);
        ll ans = (ans1 + ans2) % mod;
        ans = (ans + ans3) % mod;
        ans = (ans + ans4) % mod;
        ans = ans * pow2m % mod;

        cout << ans << "\n";
    }

    return 0;
}