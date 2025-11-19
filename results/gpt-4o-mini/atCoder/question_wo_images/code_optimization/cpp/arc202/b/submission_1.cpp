#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll mod = 998244353;

ll mod_inv(ll a, ll m) {
    ll m0 = m, y = 0, x = 1;
    if (m == 1) return 0;
    while (a > 1) {
        ll q = a / m;
        ll t = m;
        m = a % m, a = t;
        t = y;
        y = x - q * y;
        x = t;
    }
    if (x < 0) x += m0;
    return x;
}

ll comb(int n, int r, ll *fact) {
    if (r > n || r < 0) return 0;
    return fact[n] * mod_inv(fact[r], mod) % mod * mod_inv(fact[n - r], mod) % mod;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int h, w;
    cin >> h >> w;

    if (h % 2 == 0 || w % 2 == 0) {
        cout << 0 << '\n';
        return 0;
    }

    // Precompute factorials
    ll fact[200001];
    fact[0] = 1;
    for (int i = 1; i <= 200000; i++) {
        fact[i] = fact[i - 1] * i % mod;
    }

    ll ans = 0;
    for (int i = 1; i <= h; i += 2) {
        if (__gcd(i, w) == 1) {
            ans = (ans + comb(h, (i + h) / 2, fact)) % mod;
        }
    }
    
    cout << (ans * 2) % mod << '\n';
    return 0;
}
