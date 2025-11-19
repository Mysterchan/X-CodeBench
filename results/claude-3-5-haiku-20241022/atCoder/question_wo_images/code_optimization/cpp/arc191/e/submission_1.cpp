#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const ll MOD = 998244353;

ll power(ll a, ll b, ll mod) {
    ll res = 1;
    a %= mod;
    while (b > 0) {
        if (b & 1) res = res * a % mod;
        a = a * a % mod;
        b >>= 1;
    }
    return res;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    
    int n;
    ll x, y;
    cin >> n >> x >> y;
    
    vector<ll> a(n), b(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i] >> b[i];
    }
    
    ll max_a = *max_element(a.begin(), a.end());
    
    if (x % 2 == y % 2 || max_a == 0) {
        int even = 0, odd = 0;
        for (int i = 0; i < n; i++) {
            ll c = a[i] * (x + 1) + b[i];
            if (c % 2 == 0) even++;
            else odd++;
        }
        
        ll ans = 0;
        vector<ll> fact(odd + 1), inv_fact(odd + 1);
        fact[0] = 1;
        for (int i = 1; i <= odd; i++) {
            fact[i] = fact[i-1] * i % MOD;
        }
        inv_fact[odd] = power(fact[odd], MOD - 2, MOD);
        for (int i = odd - 1; i >= 0; i--) {
            inv_fact[i] = inv_fact[i+1] * (i+1) % MOD;
        }
        
        for (int i = (odd + 1) / 2; i <= odd; i++) {
            ll binom = fact[odd] * inv_fact[i] % MOD * inv_fact[odd - i] % MOD;
            ans = (ans + binom) % MOD;
        }
        
        ans = ans * power(2, even, MOD) % MOD;
        cout << ans << '\n';
        return 0;
    }
    
    // x % 2 != y % 2
    int ta = 0, ao = 0, fi = 0, se = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] == 0) {
            if (b[i] % 2 == 1) fi++;
            else se++;
        } else if (a[i] == 1) {
            if (b[i] % 2 == 0 && x % 2 == 0) ta++;
            if (b[i] % 2 == 0 && y % 2 == 0) ao++;
            if (b[i] % 2 == 1) fi++;
        } else {
            if (x % 2 == 0) ta++;
            if (y % 2 == 0) ao++;
        }
    }
    
    int total = ta + ao;
    int max_deg = total + 2 * fi;
    vector<ll> dp(max_deg + 1, 0);
    dp[0] = 1;
    
    // Multiply by (1+x)^total
    for (int deg = 0; deg <= total; deg++) {
        ll binom = 1;
        for (int j = 0; j < deg; j++) {
            binom = binom * (total - j) % MOD * power(j + 1, MOD - 2, MOD) % MOD;
        }
        dp[deg] = binom;
    }
    
    // Multiply by (1+x²)^fi
    for (int iter = 0; iter < fi; iter++) {
        for (int i = max_deg; i >= 2; i--) {
            dp[i] = (dp[i] + dp[i-2]) % MOD;
        }
    }
    
    ll ans = 0;
    for (int i = ao + fi + 1; i <= max_deg; i++) {
        ans = (ans + dp[i]) % MOD;
    }
    
    ans = ans * power(2, se, MOD) % MOD;
    cout << ans << '\n';
    
    return 0;
}