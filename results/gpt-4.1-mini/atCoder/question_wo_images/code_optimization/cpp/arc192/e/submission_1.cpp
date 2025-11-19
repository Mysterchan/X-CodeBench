#include <bits/stdc++.h>
using namespace std;
using ll = long long;
constexpr ll M = 998244353;
constexpr int MAXN = 2000004;

ll fc[MAXN], inv[MAXN], invfc[MAXN];

// Modular exponentiation
ll modpow(ll a, ll b) {
    ll res = 1;
    while (b) {
        if (b & 1) res = res * a % M;
        a = a * a % M;
        b >>= 1;
    }
    return res;
}

// Precompute factorials and inverse factorials
void init() {
    fc[0] = 1;
    for (int i = 1; i < MAXN; i++) fc[i] = fc[i - 1] * i % M;
    inv[1] = 1;
    for (int i = 2; i < MAXN; i++) inv[i] = M - M / i * inv[M % i] % M;
    invfc[0] = 1;
    for (int i = 1; i < MAXN; i++) invfc[i] = invfc[i - 1] * inv[i] % M;
}

// Compute nCr modulo M
ll C(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fc[n] * invfc[r] % M * invfc[n - r] % M;
}

// Compute number of paths from (x1,y1) to (x2,y2) moving only right/up
ll paths(int x1, int y1, int x2, int y2) {
    if (x2 < x1 || y2 < y1) return 0;
    int dx = x2 - x1, dy = y2 - y1;
    return C(dx + dy, dx);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    init();

    int W, H, L, R, D, U;
    cin >> W >> H >> L >> R >> D >> U;

    // The town blocks are all points (x,y) with 0 <= x <= W, 0 <= y <= H,
    // except those with L <= x <= R and D <= y <= U (excluded rectangle).

    // We want the number of possible paths Snuke could have taken:
    // - Start at any block
    // - Move only right or up to blocks
    // - Count all possible paths modulo M

    // The problem reduces to counting all paths starting and ending in the allowed region,
    // moving only right/up, and summing over all possible start/end points.

    // The allowed region is the big rectangle minus the forbidden rectangle inside.

    // The key insight:
    // The allowed blocks form two disjoint parts separated by the forbidden rectangle:
    // 1) Left-bottom region: x < L or y < D
    // 2) Right-top region: x > R or y > U

    // But since the forbidden rectangle is contiguous, the allowed region is:
    // (0 <= x <= W, 0 <= y <= H) \ (L <= x <= R, D <= y <= U)

    // The paths can only move right/up, so any path crossing the forbidden rectangle is impossible.

    // The total number of paths is sum over all start and end points in allowed region,
    // where end >= start coordinate-wise, and path is monotone right/up.

    // The problem is solved by inclusion-exclusion on the forbidden rectangle.

    // We use the formula from the editorial (or original code logic):
    // Let x0 = L-1, x1 = R, y0 = D-1, y1 = U
    // Define:
    // F(a,b) = number of paths from (0,0) to (a,b) avoiding forbidden rectangle
    // G(a,b) = number of paths from (a,b) to (W,H) avoiding forbidden rectangle

    // The answer = sum over all (x,y) in allowed region of number of paths starting at (x,y)
    // and moving right/up to any allowed block.

    // The original code uses a clever inclusion-exclusion with precomputed factorials.

    // We'll implement the same logic but cleaner and faster.

    // Precompute x and y arrays as in original code:
    // x[0] = L-1, x[1] = R, x[2] = L, x[3] = R+1, x[4] = L-1, x[5] = R+1
    // y[0] = D-1, y[1] = U, y[2] = D, y[3] = U+1, y[4] = D-1, y[5] = U+1

    int x[6], y[6];
    x[0] = L - 1; x[1] = R;
    x[2] = L;     x[3] = R + 1;
    x[4] = L - 1; x[5] = R + 1;

    y[0] = D - 1; y[1] = U;
    y[2] = D;     y[3] = U + 1;
    y[4] = D - 1; y[5] = U + 1;

    // Function F(a,b) as in original code:
    // F(a,b) = C(a - x0 + b - y1, a - x0) + C(a - x1 + b - y0, a - x1)
    //          - C(a - x0 + b - y0, a - x0) - C(a - x1 + b - y1, a - x1)
    // with modulo M and careful bounds.

    auto F = [&](int a, int b) -> ll {
        ll res = 0;
        auto c = [&](int n, int r) -> ll {
            if (n < 0 || r < 0 || r > n) return 0;
            return C(n, r);
        };
        res += c(a - x[0] + b - y[1], a - x[0]);
        res += c(a - x[1] + b - y[0], a - x[1]);
        res -= c(a - x[0] + b - y[0], a - x[0]);
        res -= c(a - x[1] + b - y[1], a - x[1]);
        res %= M;
        if (res < 0) res += M;
        return res;
    };

    // Function G(a,b) as in original code:
    // G(a,b) = C(x4 - a + y5 - b, x4 - a) + C(x5 - a + y4 - b, x5 - a)
    //          - C(x4 - a + y4 - b, x4 - a) - C(x5 - a + y5 - b, x5 - a)

    auto G = [&](int a, int b) -> ll {
        ll res = 0;
        auto c = [&](int n, int r) -> ll {
            if (n < 0 || r < 0 || r > n) return 0;
            return C(n, r);
        };
        res += c(x[4] - a + y[5] - b, x[4] - a);
        res += c(x[5] - a + y[4] - b, x[5] - a);
        res -= c(x[4] - a + y[4] - b, x[4] - a);
        res -= c(x[5] - a + y[5] - b, x[5] - a);
        res %= M;
        if (res < 0) res += M;
        return res;
    };

    ll ans = 0;

    // Sum over i in [L, R+1], j = D-1
    for (int i = x[2]; i <= x[3]; i++) {
        ll val = (M - F(i, y[2] - 1) * G(i, y[2]) % M * (y[2] + i) % M) % M;
        ans = (ans + val) % M;
    }
    // Sum over j in [D, U], i = L-1
    for (int j = y[2]; j <= y[3]; j++) {
        ll val = (M - F(x[2] - 1, j) * G(x[2], j) % M * (x[2] + j) % M) % M;
        ans = (ans + val) % M;
    }
    // Sum over i in [L, R+1], j = U+1
    for (int i = x[2]; i <= x[3]; i++) {
        ll val = F(i, y[3]) * G(i, y[3] + 1) % M * (y[3] + i + 1) % M;
        ans = (ans + val) % M;
    }
    // Sum over j in [D, U], i = R+1
    for (int j = y[2]; j <= y[3]; j++) {
        ll val = F(x[3], j) * G(x[3] + 1, j) % M * (x[3] + j + 1) % M;
        ans = (ans + val) % M;
    }

    cout << ans << "\n";
    return 0;
}