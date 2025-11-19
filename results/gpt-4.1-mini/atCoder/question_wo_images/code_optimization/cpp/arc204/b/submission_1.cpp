#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;
    int NK = N * K;

    vector<int> P(NK);
    for (int i = 0; i < NK; i++) {
        cin >> P[i];
        P[i]--;
    }

    vector<bool> visited(NK, false);
    int ans = 0;

    // For each cycle in the permutation
    for (int i = 0; i < NK; i++) {
        if (visited[i]) continue;
        vector<int> cycle;
        for (int cur = i; !visited[cur]; cur = P[cur]) {
            visited[cur] = true;
            cycle.push_back(cur);
        }

        int M = (int)cycle.size();
        if (M <= 1) continue;

        // Group cycle elements by their residue mod N
        vector<vector<int>> groups(N);
        for (int idx = 0; idx < M; idx++) {
            groups[cycle[idx] % N].push_back(idx);
        }

        // The problem reduces to finding the maximum number of "good" edges in the cycle,
        // where an edge between positions i and j is "good" if |i-j| mod N == 0.
        // The DP in the original code is O(M^3), which is too slow.
        // We optimize by using a divide-and-conquer approach on the cycle:
        // The maximum number of points in a cycle is equal to the maximum number of 
        // non-crossing chords between indices in the cycle where chords connect indices 
        // with the same residue mod N and the chord length is a multiple of N.
        //
        // Since the cycle is a permutation cycle, the minimal number of swaps to sort it is M-1.
        // The maximum points is the maximum number of edges (swaps) where |i-j| mod N == 0.
        //
        // We can solve this by DP on intervals of the cycle:
        // dp[l][r] = max points in sub-interval [l, r) of the cycle (indices modulo M)
        //
        // To handle the cycle, we fix a start point and consider the linearized cycle of length M.
        // Then we do DP on intervals of length from 1 to M.
        //
        // For each interval [l, r), we try to pair l with some k in (l+1, r) where cycle[l] % N == cycle[k] % N
        // and the distance (k - l) is multiple of N.
        // Then dp[l][r] = max over k of dp[l+1][k] + dp[k+1][r] + 1
        // or dp[l+1][r] if no pairing.
        //
        // Since M <= N*K <= 5000, and K <= 10, M can be up to 5000.
        // O(M^3) is too large, but we can optimize by only considering pairs with same residue mod N,
        // and only pairs where (k - l) % N == 0.
        //
        // We implement DP with memoization and pruning.

        // To handle the cycle, we double the cycle array to avoid modulo complications
        vector<int> doubled_cycle(2 * M);
        for (int i = 0; i < 2 * M; i++) {
            doubled_cycle[i] = cycle[i % M];
        }

        // Precompute residue for each position
        vector<int> residue(M);
        for (int i = 0; i < M; i++) residue[i] = cycle[i] % N;

        // We'll do DP on intervals [l, r) with length <= M
        // dp[l][r] = max points in interval [l, r)
        // We'll only compute dp for intervals of length <= M starting at 0
        // and take dp[0][M] as answer.

        // To speed up, we store positions of each residue in the interval
        // and only try to pair l with positions k where residue[l] == residue[k] and (k - l) % N == 0

        // Since (k - l) % N == 0, and residue[l] == residue[k], we only consider k = l + t*N for t >=1 and k < r

        // Implement DP with O(M^2) complexity

        vector<vector<int>> dp(M + 1, vector<int>(M + 1, 0));

        for (int length = 2; length <= M; length++) {
            for (int l = 0; l + length <= M; l++) {
                int r = l + length;
                int res = dp[l + 1][r]; // no pairing at l
                int start_residue = residue[l];
                // try to pair l with k where k = l + t*N < r and residue[k] == start_residue
                for (int k = l + N; k < r; k += N) {
                    if (residue[k] == start_residue) {
                        int val = dp[l + 1][k] + dp[k + 1][r] + 1;
                        if (val > res) res = val;
                    }
                }
                dp[l][r] = res;
            }
        }

        ans += dp[0][M];
    }

    cout << ans << "\n";
    return 0;
}