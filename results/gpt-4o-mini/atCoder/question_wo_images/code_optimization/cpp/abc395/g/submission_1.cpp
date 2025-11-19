#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int MAXN = 80;
const ll inf = 1e18;

int n, k;
ll c[MAXN][MAXN];
ll dp[(1 << 8)][MAXN][MAXN];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> k;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j)
            cin >> c[i][j];

    // Floyd-Warshall to find min distances between all pairs
    for (int m = 1; m <= n; ++m)
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= n; ++j)
                c[i][j] = min(c[i][j], c[i][m] + c[m][j]);

    // Initialize DP
    for (int mask = 0; mask < (1 << k); ++mask)
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= n; ++j)
                dp[mask][i][j] = (mask == 0) ? 0 : inf;

    // Base cases
    for (int i = 0; i < k; ++i) {
        dp[1 << i][i + 1][i + 1] = 0;
    }

    // DP calculation
    for (int mask = 1; mask < (1 << k); ++mask) {
        for (int sub1 = mask; sub1; sub1 = (sub1 - 1) & mask) {
            int sub2 = mask ^ sub1;

            for (int b = 1; b <= n; ++b) {
                ll mn = inf;

                // Min distance from sub2 set to any vertex b
                for (int e = 1; e <= n; ++e) {
                    if (sub2)  // Only calculate if sub2 is not empty
                        mn = min(mn, dp[sub2][e][e] + c[b][e]);
                }

                // Update for each vertex pair in sub1
                for (int a = 1; a <= n; ++a) {
                    dp[mask][a][b] = min(dp[mask][a][b], dp[sub1][a][b] + mn);
                    dp[mask][b][a] = min(dp[mask][b][a], dp[sub1][b][a] + mn);
                }
            }
        }
    }

    int q;
    cin >> q;
    while (q--) {
        int s, t;
        cin >> s >> t;
        cout << dp[(1 << k) - 1][s][t] << '\n';
    }

    return 0;
}
