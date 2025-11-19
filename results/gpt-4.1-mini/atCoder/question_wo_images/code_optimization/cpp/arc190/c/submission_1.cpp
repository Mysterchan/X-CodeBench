#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const int MAX = 200000 + 5;
const ll mod = 998244353;

int H, W, Q, sh, sw;
vector<ll> A; // flattened grid A[h*W + w]
vector<ll> fact, invfact;

inline ll modpow(ll a, ll b) {
    ll res = 1;
    while (b) {
        if (b & 1) res = res * a % mod;
        a = a * a % mod;
        b >>= 1;
    }
    return res;
}

inline ll inv(ll x) {
    return modpow(x, mod - 2);
}

inline void precompute_factorials(int n) {
    fact.resize(n + 1);
    invfact.resize(n + 1);
    fact[0] = 1;
    for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i % mod;
    invfact[n] = inv(fact[n]);
    for (int i = n - 1; i >= 0; i--) invfact[i] = invfact[i + 1] * (i + 1) % mod;
}

inline ll comb(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invfact[r] % mod * invfact[n - r] % mod;
}

inline int idx(int h, int w) {
    return (h - 1) * W + (w - 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> H >> W;
    A.resize(H * W);
    for (int i = 0; i < H * W; i++) cin >> A[i];
    cin >> Q >> sh >> sw;

    precompute_factorials(H + W + 5);

    // Precompute C(h,w) = C(h+w-2, h-1) for all cells
    // We'll store C(h,w) in a vector for quick access
    // h in [1,H], w in [1,W]
    vector<ll> C(H * W);
    for (int h = 1; h <= H; h++) {
        for (int w = 1; w <= W; w++) {
            C[idx(h, w)] = comb(h + w - 2, h - 1);
        }
    }

    // Compute initial answer:
    // sum over all cells (h,w) of A[h,w] * C(h,w) * C(H - h + W - w, H - h)
    // where C(H - h + W - w, H - h) = number of paths from (h,w) to (H,W)
    // Precompute suffix combinations for (H - h + W - w, H - h)
    // We'll compute on the fly using comb

    // To avoid recomputing comb many times, we can precompute suffix combinations for all cells:
    // But since H*W <= 200000, we can compute on the fly.

    // We'll store suffixC[h][w] = C((H - h) + (W - w), H - h)
    // But to save memory, just compute on the fly.

    auto suffixC = [&](int h, int w) -> ll {
        int down = H - h;
        int right = W - w;
        return comb(down + right, down);
    };

    ll ans = 0;
    for (int h = 1; h <= H; h++) {
        for (int w = 1; w <= W; w++) {
            ll val = A[idx(h, w)];
            if (val == 0) continue;
            ll ways = C[idx(h, w)] * suffixC(h, w) % mod;
            ans = (ans + val * ways) % mod;
        }
    }

    // Current position of Takahashi
    int curh = sh, curw = sw;

    // Process queries
    for (int i = 0; i < Q; i++) {
        char d; ll a;
        cin >> d >> a;

        // Move Takahashi
        if (d == 'L') curw--;
        else if (d == 'R') curw++;
        else if (d == 'U') curh--;
        else if (d == 'D') curh++;

        // Update answer:
        // old_val = A[curh, curw]
        // new_val = a
        // delta = (new_val - old_val) * C(curh, curw) * suffixC(curh, curw)
        ll old_val = A[idx(curh, curw)];
        ll ways = C[idx(curh, curw)] * suffixC(curh, curw) % mod;
        ans = (ans + (a + mod - old_val) * ways) % mod;

        A[idx(curh, curw)] = a;

        cout << ans << "\n";
    }

    return 0;
}