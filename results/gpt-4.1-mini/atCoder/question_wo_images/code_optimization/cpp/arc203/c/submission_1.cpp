#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int MOD = 998244353;

namespace tools {
    ll qpow(ll x, ll n) {
        ll res = 1;
        x %= MOD;
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
    vector<ll> fact, ifact;

    void init(int n) {
        fact.resize(n + 1);
        ifact.resize(n + 1);
        fact[0] = 1;
        for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i % MOD;
        ifact[n] = tools::inv(fact[n]);
        for (int i = n - 1; i >= 0; i--) ifact[i] = ifact[i + 1] * (i + 1) % MOD;
    }

    ll nCr(int n, int r) {
        if (r < 0 || r > n) return 0;
        return fact[n] * ifact[r] % MOD * ifact[n - r] % MOD;
    }
}

inline ll norm(ll x) {
    x %= MOD;
    if (x < 0) x += MOD;
    return x;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;

    // Precompute max needed factorial size:
    // max need = H+W-2 <= 4*10^5 (since H,W <= 2*10^5)
    // We'll precompute factorials up to 400000 once.
    // But input T can be large, so we must pre-read all inputs first to find max need.

    // To avoid overhead, we can precompute factorials up to 400000 once.
    const int MAX = 400000;
    comb::init(MAX);

    while (T--) {
        int H, W, K;
        cin >> H >> W >> K;
        ll need = (ll)H + W - 2;
        if (K < need) {
            cout << 0 << "\n";
            continue;
        }

        ll total_full = (ll)(H - 1) * W + (ll)(W - 1) * H;
        if (K > total_full) {
            // Can't choose more walls than total walls
            cout << 0 << "\n";
            continue;
        }

        ll ans = comb::nCr((int)need, H - 1);
        ans = norm(ans);

        if (K == need) {
            cout << ans << "\n";
            continue;
        }

        ll more = norm(total_full - need);

        if (K == need + 1) {
            ans = norm(ans * more);
            cout << ans << "\n";
            continue;
        }

        // For K >= need + 2, original code uses a formula involving combinations and corrections.
        // But the problem constraints and sample suggest only K up to H+W is relevant.
        // The original code only handles up to K = need + 2.
        // For K > need + 2, answer is 0 (since max K = H+W and total walls can be larger).
        // But problem states K ≤ H+W, so K ≤ need + 2 at most (since need = H+W-2).

        if (K > need + 2) {
            cout << 0 << "\n";
            continue;
        }

        // K == need + 2 case:
        // Use the formula from original code:

        ll inv2 = tools::inv(2);
        ll mul = more * ((more - 1 + MOD) % MOD) % MOD;
        mul = mul * inv2 % MOD;
        ans = ans * mul % MOD;

        ll term1 = comb::nCr((int)need - 2, H - 2) * ((need - 1) % MOD) % MOD;
        ans = norm(ans - term1);

        for (int t = 0; t < 2; t++) {
            int nn = (t == 0 ? H : W);
            int mm = (t == 0 ? W : H);
            if (need - 1 >= 0 && nn <= need - 1 && nn >= 0) {
                ll c1 = comb::nCr((int)need - 1, nn) % MOD;
                ll add = c1 * (need % MOD) % MOD;
                ans = norm(ans + add);
            }
            if (need >= 0 && nn + 1 <= need && nn + 1 >= 0) {
                ll c2 = comb::nCr((int)need, nn + 1) % MOD;
                ll sub = (2 % MOD) * c2 % MOD;
                ans = norm(ans - sub);
            }
        }

        cout << ans << "\n";
    }

    return 0;
}