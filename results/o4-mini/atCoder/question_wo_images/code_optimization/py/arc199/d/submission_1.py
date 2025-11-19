#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int MOD = 998244353;

int add(int a, int b) {
    a += b;
    if (a >= MOD) a -= MOD;
    return a;
}
int mul(ll a, ll b) {
    return (int)( (a * b) % MOD );
}
int modpow(int a, ll e = MOD-2) {
    ll r = 1, x = a;
    while (e) {
        if (e & 1) r = (r * x) % MOD;
        x = (x * x) % MOD;
        e >>= 1;
    }
    return (int)r;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int H, W;
    cin >> H >> W;
    // ensure H >= W
    if (H < W) swap(H, W);
    int h = H, w = W;

    // Precompute factorials up to N = H+W+5
    int N = H + W + 5;
    vector<int> fac(N), ifac(N);
    fac[0] = 1;
    for (int i = 1; i < N; i++) fac[i] = mul(fac[i-1], i);
    ifac[N-1] = modpow(fac[N-1]);
    for (int i = N-1; i > 0; i--) ifac[i-1] = mul(ifac[i], i);

    auto comb = [&](int n, int k)->int {
        if (k < 0 || k > n || n < 0) return 0;
        return mul(fac[n], mul(ifac[k], ifac[n-k]));
    };

    // dp and cnt arrays of size w+1
    vector<int> cnt(w+1, 0), dp(w+1, 0);
    cnt[0] = 1;
    // Temporary next arrays
    vector<int> nxt_cnt(w+1), nxt_dp(w+1);

    // DP over rows
    for (int i = 0; i < h; i++) {
        // zero next arrays
        fill(nxt_cnt.begin(), nxt_cnt.end(), 0);
        fill(nxt_dp.begin(), nxt_dp.end(), 0);

        for (int j = 0; j <= w; j++) {
            if (cnt[j] == 0 && dp[j] == 0) continue;
            int c_j = cnt[j];
            int d_j = dp[j];
            for (int k = 0; k + j <= w; k++) {
                int t = j + k;
                // C(t+1, j)
                int c1 = comb(t+1, j);
                // update cnt
                ll v_cnt = (ll)c_j * c1 % MOD;
                nxt_cnt[t] = add(nxt_cnt[t], (int)v_cnt);
                // update dp from dp[j]
                ll v_dp = (ll)d_j * c1 % MOD;
                nxt_dp[t] = add(nxt_dp[t], (int)v_dp);
                // update dp from cnt[j] * k * i * C(t+1,j)
                if (k != 0 && i != 0) {
                    ll v = (ll)c_j * k % MOD * i % MOD * c1 % MOD;
                    nxt_dp[t] = add(nxt_dp[t], (int)v);
                }
                // update dp from cnt[j] * C(t+1, j-1)
                if (j >= 1) {
                    int c2 = comb(t+1, j-1);
                    ll v2 = (ll)c_j * c2 % MOD;
                    nxt_dp[t] = add(nxt_dp[t], (int)v2);
                }
            }
        }
        // swap for next iteration
        cnt.swap(nxt_cnt);
        dp.swap(nxt_dp);
    }

    // Compute final answer
    ll ans = 0;
    for (int j = 0; j <= w; j++) {
        if (dp[j]) {
            ll v = (ll)dp[j] * comb(w, j) % MOD;
            ans = (ans + v) % MOD;
        }
        if (cnt[j]) {
            ll v = (ll)cnt[j] * (ll)h % MOD * (w - j) % MOD * comb(w, j) % MOD;
            ans = (ans + v) % MOD;
        }
    }
    cout << ans << "\n";
    return 0;
}