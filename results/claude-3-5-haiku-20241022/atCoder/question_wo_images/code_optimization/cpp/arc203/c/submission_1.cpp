#define TEST
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int MOD = 998244353;
const int MAXN = 400005;

namespace tools {
ll qpow(ll x, ll n) {
    x %= MOD;
    ll res = 1;
    while (n) {
        if (n & 1) res = (res * x) % MOD;
        x = (x * x) % MOD;
        n >>= 1;
    }
    return res;
}

ll inv(ll x) {
    return qpow(x, MOD - 2);
}
}

namespace comb {
vector<ll> _fact;
vector<ll> _ifact;

void init(int n) {
    _fact.resize(n + 1);
    _fact[0] = 1;
    for (int i = 1; i <= n; i++)
        _fact[i] = _fact[i - 1] * i % MOD;

    _ifact.resize(n + 1);
    _ifact[n] = tools::inv(_fact[n]);
    for (int i = n - 1; i >= 0; i--)
        _ifact[i] = _ifact[i + 1] * (i + 1) % MOD;
}

ll nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return _fact[n] * _ifact[r] % MOD * _ifact[n - r] % MOD;
}
}

ll norm(ll x) {
    x %= MOD;
    if (x < 0) x += MOD;
    return x;
}

void solve() {
    int n0, m0, k;
    cin >> n0 >> m0 >> k;
    
    ll n = n0, m = m0;
    ll need = n + m - 2;
    
    if (k < need) {
        cout << 0 << '\n';
        return;
    }

    ll total_full = (n - 1) * m + (m - 1) * n;
    ll ans = comb::nCr(need, (int)(n - 1));
    ans = norm(ans);

    if (k == need) {
        cout << ans << '\n';
        return;
    }

    ll more = norm(total_full - need);

    if (k == need + 1) {
        ans = norm(ans * more);
        cout << ans << '\n';
        return;
    }

    ll inv2 = tools::inv(2);
    ll mul = more * ((more - 1 + MOD) % MOD) % MOD;
    mul = mul * inv2 % MOD;
    ans = ans * mul % MOD;

    ll term1 = comb::nCr(need - 2, (int)(n - 2)) * ((need - 1) % MOD) % MOD;
    ans = norm(ans - term1);

    for (int t = 0; t < 2; t++) {
        ll nn = (t == 0 ? n0 : m0);
        ll mm = (t == 0 ? m0 : n0);
        if (need - 1 >= 0 && nn <= need - 1 && nn >= 0) {
            ll c1 = comb::nCr(need - 1, (int)nn) % MOD;
            ll add = c1 * (need % MOD) % MOD;
            ans = norm(ans + add);
        }
        if (need >= 0 && nn + 1 <= need && nn + 1 >= 0) {
            ll c2 = comb::nCr(need, (int)(nn + 1)) % MOD;
            ll sub = (2 % MOD) * c2 % MOD;
            ans = norm(ans - sub);
        }
    }

    cout << ans << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    comb::init(MAXN);
    
    int t;
    cin >> t;
    while (t--) solve();
    
    return 0;
}