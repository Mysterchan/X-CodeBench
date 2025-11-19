#include <bits/stdc++.h>
using namespace std;
#define MOD 998244353
#define N 200005

typedef long long ll;

ll factorial[N], inv_factorial[N];
ll prefix_sum[N], suffix_sum[N];

ll mod_inverse(ll a, ll mod) {
    ll res = 1, exp = mod - 2;
    while (exp) {
        if (exp % 2) res = res * a % mod;
        a = a * a % mod;
        exp /= 2;
    }
    return res;
}

void precompute() {
    factorial[0] = 1;
    for (int i = 1; i < N; ++i) {
        factorial[i] = factorial[i - 1] * i % MOD;
    }
    inv_factorial[N - 1] = mod_inverse(factorial[N - 1], MOD);
    for (int i = N - 2; i >= 0; --i) {
        inv_factorial[i] = inv_factorial[i + 1] * (i + 1) % MOD;
    }
}

ll comb(ll n, ll k) {
    if (k < 0 || k > n) return 0;
    return factorial[n] * inv_factorial[k] % MOD * inv_factorial[n - k] % MOD;
}

int n, q;
ll a[N];

void solve() {
    cin >> n >> q;
    for (int i = 2; i <= n; ++i) {
        cin >> a[i];
    }

    // Precompute prefix sums for weights and suffix sums
    for (int i = 2; i <= n; ++i) {
        prefix_sum[i] = (prefix_sum[i - 1] + a[i] * factorial[i - 1]) % MOD;
        suffix_sum[i] = (suffix_sum[i] + (i - 1) * factorial[i - 1]) % MOD;
    }

    while (q--) {
        int u, v;
        cin >> u >> v;

        ll ans = (fact_v - suffix_sum[u] + prefix_sum[v]) % MOD;
        ans = (ans + a[u] * factorial[u - 1] % MOD * (factorial[n - 1] * inv_factorial[v - 1]) % MOD) % MOD;
        
        cout << ans << "\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    precompute();
    solve();
    
    return 0;
}
