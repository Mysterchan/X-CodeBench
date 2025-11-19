#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const ll mod = 998244353;
ll fact[200001], inv_fact[200001];

ll power(ll x, ll y) {
    ll res = 1;
    x %= mod;
    while (y > 0) {
        if (y & 1) res = res * x % mod;
        x = x * x % mod;
        y >>= 1;
    }
    return res;
}

void precompute() {
    fact[0] = 1;
    for (int i = 1; i <= 200000; i++)
        fact[i] = fact[i-1] * i % mod;
    
    inv_fact[200000] = power(fact[200000], mod - 2);
    for (int i = 199999; i >= 0; i--)
        inv_fact[i] = inv_fact[i+1] * (i+1) % mod;
}

ll comb(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * inv_fact[r] % mod * inv_fact[n-r] % mod;
}

ll gcd(ll a, ll b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    precompute();
    
    ll h, w;
    cin >> h >> w;
    
    if (h % 2 == 0 || w % 2 == 0) {
        cout << 0 << '\n';
        return 0;
    }
    
    ll ans = 0;
    for (int i = 1; i <= h; i += 2) {
        if (gcd(i, w) == 1) {
            ans = (ans + comb(h, (i + h) / 2)) % mod;
        }
    }
    
    cout << ans * 2 % mod << '\n';
    
    return 0;
}