#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int MOD = 998244353;
const int MAXN = 400005;
ll fact[MAXN], invfact[MAXN];

ll modpow(ll a, ll e) {
    ll r = 1;
    while (e) {
        if (e & 1) r = r * a % MOD;
        a = a * a % MOD;
        e >>= 1;
    }
    return r;
}

ll nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    fact[0] = 1;
    for (int i = 1; i < MAXN; i++) fact[i] = fact[i-1] * i % MOD;
    invfact[MAXN-1] = modpow(fact[MAXN-1], MOD-2);
    for (int i = MAXN-1; i > 0; i--) invfact[i-1] = invfact[i] * i % MOD;

    ll inv2 = (MOD + 1) / 2;

    int T;
    cin >> T;
    while (T--) {
        ll H, W, K;
        cin >> H >> W >> K;
        ll need = H + W - 2;
        if (K < need) {
            cout << 0 << '\n';
            continue;
        }
        ll C0 = nCr((int)need, (int)(H-1));
        if (K == need) {
            cout << C0 << '\n';
            continue;
        }
        ll total_full = (H * (W - 1) + W * (H - 1)) % MOD;
        ll more = total_full - need;
        more %= MOD;
        if (more < 0) more += MOD;

        if (K == need + 1) {
            ll ans = C0 * more % MOD;
            cout << ans << '\n';
            continue;
        }
        // K == need + 2
        ll mul = more * ((more - 1 + MOD) % MOD) % MOD;
        mul = mul * inv2 % MOD;
        ll ans = C0 * mul % MOD;
        // subtract term1
        ll term1 = nCr((int)(need - 2), (int)(H - 2)) * ((need - 1) % MOD) % MOD;
        ans = (ans - term1) % MOD;
        // adjustments
        for (int t = 0; t < 2; t++) {
            ll nn = (t == 0 ? H : W);
            if (need - 1 >= 0 && nn <= need - 1) {
                ll c1 = nCr((int)(need - 1), (int)nn);
                ans = (ans + c1 * (need % MOD)) % MOD;
            }
            if (need >= 0 && nn + 1 <= need) {
                ll c2 = nCr((int)need, (int)(nn + 1));
                ans = (ans - 2 * c2 % MOD) % MOD;
            }
        }
        if (ans < 0) ans += MOD;
        cout << ans << '\n';
    }
    return 0;
}