#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k; cin >> n >> k;
    vector<vector<ll>> c(n, vector<ll>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> c[i][j];

    // Floyd-Warshall to get shortest paths
    for (int m = 0; m < n; m++)
        for (int i = 0; i < n; i++) {
            ll ci_m = c[i][m];
            for (int j = 0; j < n; j++) {
                ll val = ci_m + c[m][j];
                if (val < c[i][j]) c[i][j] = val;
            }
        }

    int full_mask = (1 << k) - 1;

    // dp[mask][a][b]: minimal cost of connected subgraph containing terminals in mask,
    // with endpoints a,b (vertices in [0..n-1])
    // We'll store dp as vector<vector<vector<ll>>> but to optimize memory and speed,
    // we use 3D vector with dimensions [1<<k][n][n].
    // Initialize dp with INF except dp[0][i][j] = c[i][j]

    vector<vector<vector<ll>>> dp(full_mask + 1, vector<vector<ll>>(n, vector<ll>(n, INF)));

    // Base case: dp[0][i][j] = c[i][j]
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            dp[0][i][j] = c[i][j];

    // For single terminals: dp[1<<i][i][i] = 0 (terminal i+1 at vertex i)
    for (int i = 0; i < k; i++)
        dp[1 << i][i][i] = 0;

    // Precompute all subsets of full_mask in increasing order of bits
    // For each mask, combine smaller subsets sub1 and sub2 = mask ^ sub1
    // To avoid recomputing sub1 multiple times, iterate sub1 from (mask-1) & mask down to 0

    // Optimization: For each mask, iterate sub1 as submask of mask (excluding 0 and mask)
    // and combine dp[sub1] and dp[sub2]

    // To speed up, we precompute for each mask the list of submasks (excluding 0 and mask)
    // but since k <= 8, we can just iterate all submasks.

    for (int mask = 1; mask <= full_mask; mask++) {
        if ((mask & (mask - 1)) == 0) continue; // single bit masks already set

        // Iterate sub1 as proper submask of mask (excluding 0 and mask)
        for (int sub1 = (mask - 1) & mask; sub1 > 0; sub1 = (sub1 - 1) & mask) {
            int sub2 = mask ^ sub1;

            // For each pair (a,b), try to combine dp[sub1][a][b] and dp[sub2]
            // The original code is O(n^4), we optimize by:
            // For fixed b, precompute mn_e = min over e of dp[sub2][e][e] + c[b][e]
            // and for fixed d, precompute mn_e = min over e of dp[sub2][d][e] + c[b][e]

            // We'll do two steps:
            // 1) For each b, compute mn1[b] = min_e dp[sub2][e][e] + c[b][e]
            // 2) For each d, compute mn2[d][b] = min_e dp[sub2][d][e] + c[b][e]

            // Then update dp[mask][a][b] and dp[mask][a][d]

            // Precompute mn1[b]
            vector<ll> mn1(n, INF);
            for (int b = 0; b < n; b++) {
                ll best = INF;
                for (int e = 0; e < n; e++) {
                    ll val = dp[sub2][e][e] + c[b][e];
                    if (val < best) best = val;
                }
                mn1[b] = best;
            }

            // Precompute mn2[d][b]
            // To save memory, compute on the fly inside loops

            // Update dp[mask][a][b]
            for (int a = 0; a < n; a++) {
                for (int b = 0; b < n; b++) {
                    ll val = dp[sub1][a][b] + mn1[b];
                    if (val < dp[mask][a][b]) dp[mask][a][b] = val;
                }
            }

            // For dp[mask][a][d], we do:
            // For each b,d,a:
            // dp[mask][a][d] = min(dp[mask][a][d], dp[sub1][a][b] + min_e dp[sub2][d][e] + c[b][e])

            // To optimize, for each d, precompute for each b the min_e dp[sub2][d][e] + c[b][e]
            // We'll do this inside loops to save memory.

            for (int d = 0; d < n; d++) {
                // For each b, compute min_e dp[sub2][d][e] + c[b][e]
                // We'll store in vector mn_b(n)
                vector<ll> mn_b(n, INF);
                for (int b = 0; b < n; b++) {
                    ll best = INF;
                    for (int e = 0; e < n; e++) {
                        ll val = dp[sub2][d][e] + c[b][e];
                        if (val < best) best = val;
                    }
                    mn_b[b] = best;
                }
                // Now update dp[mask][a][d]
                for (int a = 0; a < n; a++) {
                    for (int b = 0; b < n; b++) {
                        ll val = dp[sub1][a][b] + mn_b[b];
                        if (val < dp[mask][a][d]) dp[mask][a][d] = val;
                    }
                }
            }
        }
    }

    int Q; cin >> Q;
    while (Q--) {
        int s, t; cin >> s >> t;
        s--; t--;
        cout << dp[full_mask][s][t] << "\n";
    }

    return 0;
}