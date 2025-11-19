#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const ll mod = 998244353;
const int MAX = 200000;

ll fact[MAX + 1], inv_fact[MAX + 1];

// Fast exponentiation modulo mod
ll modpow(ll base, ll exp) {
    ll res = 1;
    while (exp > 0) {
        if (exp & 1) res = res * base % mod;
        base = base * base % mod;
        exp >>= 1;
    }
    return res;
}

// Modular inverse using Fermat's little theorem
ll inv(ll x) {
    return modpow(x, mod - 2);
}

// Precompute factorials and inverse factorials
void precompute_factorials() {
    fact[0] = 1;
    for (int i = 1; i <= MAX; i++) fact[i] = fact[i - 1] * i % mod;
    inv_fact[MAX] = inv(fact[MAX]);
    for (int i = MAX - 1; i >= 0; i--) inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod;
}

// Compute nCr modulo mod
ll comb(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * inv_fact[r] % mod * inv_fact[n - r] % mod;
}

// Compute gcd using built-in function for speed
inline ll gcd_fast(ll a, ll b) {
    while (b) {
        ll t = b;
        b = a % b;
        a = t;
    }
    return a;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute_factorials();

    int h, w;
    cin >> h >> w;

    // If either dimension is even, no tours exist
    if ((h & 1) == 0 || (w & 1) == 0) {
        cout << 0 << '\n';
        return 0;
    }

    // Since h and w are odd, iterate over odd i in [1, h]
    // sum comb(h, (i + h)/2) for gcd(i, w) == 1
    ll ans = 0;
    for (int i = 1; i <= h; i += 2) {
        if (gcd_fast(i, w) == 1) {
            ans += comb(h, (i + h) / 2);
            if (ans >= mod) ans -= mod;
        }
    }

    // Multiply by 2 as per problem statement
    ans = (ans * 2) % mod;

    cout << ans << '\n';

    return 0;
}