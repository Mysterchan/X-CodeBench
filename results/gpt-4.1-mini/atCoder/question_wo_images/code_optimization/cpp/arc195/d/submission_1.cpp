#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n; cin >> n;
    vector<int> a(n);
    for (int &x : a) cin >> x;

    // We want to find the minimal number of operations to empty the sequence.
    // The operations are:
    // 1) Swap adjacent elements.
    // 2) Delete a prefix of equal elements.

    // Key insight:
    // The minimal number of operations = n - (maximum number of blocks we can remove in one delete operation).
    // The original code tries to find the maximum number of "merged" blocks by swapping elements to bring equal elements together.

    // Optimized approach:
    // We can model the problem as follows:
    // - We want to partition the sequence into groups of equal elements that can be brought together by swaps.
    // - Each group removal counts as one delete operation.
    // - Swaps are needed to bring equal elements together, but each swap counts as one operation.
    // - The minimal total operations = number of swaps + number of deletes.
    //
    // The original code uses DP with O(n^2) in worst case.
    //
    // We can optimize by:
    // - Using a greedy approach to count the minimal number of delete operations after optimal swaps.
    // - The minimal number of operations = n - length of the longest chain of blocks that can be merged.
    //
    // We can compress the sequence into blocks of consecutive equal elements.
    // Then, we try to merge blocks of the same value by swapping adjacent blocks.
    //
    // The problem reduces to:
    // - Find the length of the longest chain of blocks of the same value that can be merged by swapping adjacent blocks.
    //
    // We can solve this by DP on blocks:
    // For each block, dp[block] = 1 + max(dp[prev_block]) where prev_block is the previous block with the same value.
    //
    // The answer = total number of blocks - max(dp[block]) + number of swaps needed.
    //
    // But swaps needed = number of blocks - 1 - max(dp[block]) (to bring all blocks of the same value together).
    //
    // Total operations = swaps + deletes = (blocks - 1 - max_chain) + (blocks - max_chain) = blocks + (blocks - 1) - 2*max_chain
    //
    // This is complicated, but the original editorial solution is:
    // The minimal operations = n - max number of blocks merged.
    //
    // So we just need to find max number of blocks merged.
    //
    // Implementation:
    // 1) Compress sequence into blocks.
    // 2) For each block, keep track of dp[value] = max dp for that value.
    // 3) dp[block] = dp[value] + 1
    // 4) Update dp[value] = dp[block]
    // 5) The answer = number of blocks - max dp[block]

    vector<int> blocks;
    blocks.reserve(n);
    for (int i = 0; i < n;) {
        int j = i;
        while (j < n && a[j] == a[i]) j++;
        blocks.push_back(a[i]);
        i = j;
    }

    unordered_map<int,int> dp;
    int max_dp = 0;
    for (int v : blocks) {
        int val = dp[v] + 1;
        dp[v] = val;
        if (val > max_dp) max_dp = val;
    }

    int ans = (int)blocks.size() - max_dp;
    cout << ans << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T; cin >> T;
    while (T--) solve();
    return 0;
}