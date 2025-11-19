#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H, W;
    cin >> H >> W;
    int N = H * W;
    vector<ll> A(N);
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            cin >> A[i * W + j];
        }
    }

    // Precompute neighbors for each cell (right and down)
    vector<vector<int>> neighbors(N);
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            int idx = i * W + j;
            if (j + 1 < W) neighbors[idx].push_back(idx + 1);
            if (i + 1 < H) neighbors[idx].push_back(idx + W);
        }
    }

    // DP: dp[mask] = max XOR of uncovered cells for the subset of covered cells = mask
    // mask bit = 1 means cell is covered by domino
    // We want to maximize XOR of uncovered cells = XOR of cells not in mask
    // We'll build dp by adding dominoes (pairs of adjacent cells) to smaller masks

    // Since N <= 20, dp size = 2^N ~ 1 million, feasible with bitset and careful implementation

    // Initialize dp with -1 (unvisited)
    vector<ll> dp(1 << N, -1);
    dp[0] = 0;
    // Precompute XOR of all cells
    ll total_xor = 0;
    for (ll x : A) total_xor ^= x;

    // We'll iterate over dp states in increasing order of bits set
    // For each state, try to add a domino (two adjacent uncovered cells)
    // uncovered cells = bits not set in mask

    // To speed up, we iterate over states and for each uncovered cell try to place dominoes

    for (int mask = 0; mask < (1 << N); mask++) {
        if (dp[mask] == -1) continue;
        // Current uncovered XOR = total_xor ^ XOR of covered cells
        // But we don't store XOR of covered cells, so we compute uncovered XOR on the fly:
        // dp[mask] stores max uncovered XOR for this mask, so no need to recompute here.

        // Try to place dominoes on uncovered cells
        // Find first uncovered cell to try domino placements
        int first_uncovered = -1;
        for (int i = 0; i < N; i++) {
            if ((mask & (1 << i)) == 0) {
                first_uncovered = i;
                break;
            }
        }
        if (first_uncovered == -1) continue; // all covered, no more dominoes

        // Try to place domino with neighbors of first_uncovered
        for (int nb : neighbors[first_uncovered]) {
            if ((mask & (1 << nb)) == 0) {
                int nmask = mask | (1 << first_uncovered) | (1 << nb);
                // uncovered XOR after covering these two cells:
                // dp[nmask] = max(dp[nmask], dp[mask] ^ A[first_uncovered] ^ A[nb])
                // Because dp[mask] is XOR of uncovered cells in mask,
                // covering two cells removes their values from uncovered XOR,
                // so uncovered XOR changes by XORing these two cell values.
                ll val = dp[mask] ^ A[first_uncovered] ^ A[nb];
                if (val > dp[nmask]) dp[nmask] = val;
            }
        }
        // Also consider not placing domino on first_uncovered (skip it)
        // But skipping is implicitly handled by dp[mask] itself (no change)
        // So no action needed here.
    }

    // The answer is the maximum dp value over all masks
    ll ans = 0;
    for (ll x : dp) {
        if (x > ans) ans = x;
    }
    cout << ans << "\n";

    return 0;
}