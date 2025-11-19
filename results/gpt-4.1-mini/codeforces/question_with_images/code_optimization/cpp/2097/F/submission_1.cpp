#include <bits/stdc++.h>
#define int long long
using namespace std;

const int INF = 1e18;

int n, m;
int s[20];
int a[2005][20], b[2005][20], c[2005][20];
int dp[2005][1 << 12];
int f[1 << 12][13][2][2];

inline void chk(int &x, int y) {
    if (y < x) x = y;
}

void solve() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) cin >> s[i];

    // Initialize dp for day 0
    for (int mask = 0; mask < (1 << n); mask++) {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            if (!(mask & (1 << i))) sum += s[i];
        }
        dp[0][mask] = sum;
    }

    for (int day = 1; day <= m; day++) {
        for (int i = 0; i < n; i++) cin >> a[day][i];
        for (int i = 0; i < n; i++) cin >> b[day][i];
        for (int i = 0; i < n; i++) cin >> c[day][i];

        // Reset f array to INF
        int full_mask = (1 << n);
        for (int mask = 0; mask < full_mask; mask++) {
            for (int k = 0; k <= n; k++) {
                for (int x = 0; x < 2; x++) {
                    for (int y = 0; y < 2; y++) {
                        f[mask][k][x][y] = INF;
                    }
                }
            }
        }

        // Base case for k=0
        for (int mask = 0; mask < full_mask; mask++) {
            int bit0 = (mask & 1);
            int bit1 = (mask >> 1) & 1;
            int bitn_1 = (mask >> (n - 1)) & 1;

            // Option 1: remove luggage from airport 0 (clear bit 0)
            int mask_clear0 = mask & (~1);
            int val1 = dp[day - 1][mask] + a[day][1] * bit1 + b[day][0] * bit0 + c[day][n - 1] * bitn_1;
            chk(f[mask_clear0][0][bit0][bit0], val1);

            // Option 2: keep luggage at airport 0 (set bit 0)
            int mask_set0 = mask | 1;
            chk(f[mask_set0][0][bit0][bit0], dp[day - 1][mask]);
        }

        // DP over airports 1..n-1
        for (int k = 1; k < n; k++) {
            for (int mask = 0; mask < full_mask; mask++) {
                for (int x = 0; x < 2; x++) {
                    for (int y = 0; y < 2; y++) {
                        int cur = f[mask][k - 1][x][y];
                        if (cur == INF) continue;

                        // Option 1: keep luggage at airport k (set bit k)
                        int mask_set = mask | (1 << k);
                        chk(f[mask_set][k][x][(mask >> k) & 1], cur);

                        // Option 2: remove luggage at airport k (clear bit k)
                        int mask_clear = mask & (~(1 << k));
                        int next_bit = 0;
                        if (k < n - 1) {
                            next_bit = (mask >> (k + 1)) & 1;
                            int val = cur + a[day][k + 1] * next_bit + b[day][k] * ((mask >> k) & 1) + c[day][k - 1] * y;
                            chk(f[mask_clear][k][x][(mask >> k) & 1], val);
                        } else {
                            // k == n-1, wrap around
                            int val = cur + a[day][0] * x + b[day][k] * ((mask >> k) & 1) + c[day][k - 1] * y;
                            chk(f[mask_clear][k][x][(mask >> k) & 1], val);
                        }
                    }
                }
            }
        }

        // Compute dp for day
        for (int mask = 0; mask < full_mask; mask++) dp[day][mask] = INF;
        for (int mask = 0; mask < full_mask; mask++) {
            for (int x = 0; x < 2; x++) {
                for (int y = 0; y < 2; y++) {
                    chk(dp[day][mask], f[mask][n - 1][x][y]);
                }
            }
        }

        cout << dp[day][0] << "\n";
    }
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) solve();

    return 0;
}