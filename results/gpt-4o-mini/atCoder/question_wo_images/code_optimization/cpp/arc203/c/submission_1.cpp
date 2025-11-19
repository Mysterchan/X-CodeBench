#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int MOD = 998244353;

namespace comb {
    vector<ll> fact, ifact;

    void init(int n) {
        fact.resize(n + 1);
        ifact.resize(n + 1);
        fact[0] = 1;
        for (int i = 1; i <= n; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        ifact[n] = pow(fact[n], MOD - 2); // Fermat's Little Theorem for inverse
        for (int i = n - 1; i >= 0; i--) {
            ifact[i] = ifact[i + 1] * (i + 1) % MOD;
        }
    }

    ll nCr(int n, int r) {
        if (r < 0 || r > n) return 0;
        return fact[n] * ifact[r] % MOD * ifact[n - r] % MOD;
    }
}

ll norm(ll x) {
    x %= MOD;
    return (x < 0) ? (x + MOD) : x;
}

void solve() {
    int H, W, K;
    cin >> H >> W >> K;
    
    if (K < H + W - 2) {
        cout << 0 << '\n';
        return;
    }

    comb::init(H + W - 2);

    ll total_full = (H - 1) * 1LL * W + (W - 1) * 1LL * H;
    ll ans = comb::nCr(H + W - 2, H - 1);
    ans = norm(ans);

    if (K == H + W - 2) {
        cout << ans << '\n';
        return;
    }

    ll excess_walls = norm(total_full - (H + W - 2));

    if (K == H + W - 1) {
        ans = norm(ans * excess_walls);
        cout << ans << '\n';
        return;
    }

    ll inv2 = pow(2, MOD - 2); // Modular inverse of 2
    ll additional_ways = norm(excess_walls * (excess_walls - 1) % MOD * inv2 % MOD);
    ans = ans * additional_ways % MOD;

    ans = norm(ans - comb::nCr(H + W - 4, H - 2) * (H + W - 3) % MOD);

    for (int t = 0; t < 2; t++) {
        ll N = (t == 0 ? H : W);
        if (H + W - 3 >= 0 && N <= H + W - 3) {
            ll a1 = comb::nCr(H + W - 3, N);
            ans = norm(ans + a1 * (H + W - 2) % MOD);
        }
        if (H + W - 4 >= 0 && N + 1 <= H + W - 4) {
            ll a2 = comb::nCr(H + W - 4, N + 1);
            ans = norm(ans - 2 * a2 % MOD);
        }
    }

    cout << ans << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while (T--) solve();
    return 0;
}
