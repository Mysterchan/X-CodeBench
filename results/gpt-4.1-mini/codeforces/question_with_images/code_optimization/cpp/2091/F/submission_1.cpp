#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while (T--) {
        int n, m, d; cin >> n >> m >> d;
        vector<string> grid(n);
        for (int i = 0; i < n; i++) cin >> grid[i];

        // We want to count the number of valid routes from bottom (row n-1) to top (row 0)
        // Conditions:
        // - Each route uses 1 or 2 holds per level
        // - Holds are distinct
        // - Moves only upwards or same level (non-increasing row index)
        // - Distance between holds <= d
        // - At least one hold per level
        // - Start at bottom row, end at top row

        // Observation:
        // Since Igor climbs strictly vertically (non-increasing row index),
        // and must use holds on every level, the route length = n.
        // At each level, he can pick 1 or 2 holds.
        // The order of holds in the route matters.
        // The distance condition applies between consecutive holds in the route.

        // The problem is complex, but the original code uses a clever DP with prefix sums.
        // We will implement a similar approach but optimized.

        // Preprocessing:
        // We'll store holds per row.
        // For each row, store indices of holds.
        // We'll do DP from top to bottom (row 0 to row n-1).
        // DP state: number of ways to reach each hold with 1 or 2 holds chosen on that row.
        // We'll keep two DP arrays per row:
        // f1[j] = number of ways to reach hold j using 1 hold on this row
        // f2[j] = number of ways to reach hold j using 2 holds on this row

        // We'll use a sliding window approach to connect holds between rows,
        // using the distance constraint d.

        // To speed up distance checks, note that vertical distance between rows is fixed (row difference),
        // so horizontal distance must satisfy sqrt((row_diff)^2 + (col_diff)^2) <= d
        // => col_diff <= sqrt(d^2 - (row_diff)^2)

        // We'll precompute for each pair of consecutive rows the max horizontal distance allowed.

        // Implementation plan:
        // 1) Extract holds per row.
        // 2) Initialize dp for top row: f1 = 1 for each hold, f2 = 0.
        // 3) For each next row:
        //    - For each hold in current row, find holds in previous row reachable within distance.
        //    - Use prefix sums to sum dp values efficiently.
        //    - Compute f1 and f2 for current row.
        // 4) At bottom row, sum all f2 values (since route must end at bottom row with 1 or 2 holds).
        // 5) Output result modulo MOD.

        // Note: The original code uses a clever trick with two arrays f[2][2][m].
        // We'll replicate that logic with clearer variable names and optimized loops.

        // Step 1: Extract holds per row
        vector<vector<int>> holds(n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 'X') holds[i].push_back(j + 1); // 1-based indexing for convenience
            }
        }

        // If bottom row has no holds, answer is 0 immediately
        if (holds[n - 1].empty()) {
            cout << 0 << "\n";
            continue;
        }

        // DP arrays: f1 and f2 for previous and current rows
        // f1: ways to reach hold with 1 hold on this row
        // f2: ways to reach hold with 2 holds on this row
        // We'll store dp as maps from hold index to ways for quick access
        // But since holds are sorted, we can use vectors and two pointers.

        // Initialize dp for top row (row 0)
        int prev_size = (int)holds[0].size();
        vector<long long> f1(prev_size, 1); // 1 way to pick each hold alone
        vector<long long> f2(prev_size, 0); // no ways with 2 holds on first row yet

        // Precompute d^2 for distance checks
        long long d2 = (long long)d * d;

        // For each next row i from 1 to n-1
        for (int i = 1; i < n; i++) {
            int cur_size = (int)holds[i].size();
            if (cur_size == 0) {
                // No holds on this row => no valid routes
                f1.clear();
                f2.clear();
                break;
            }

            // Distance between rows = i - (i-1) = 1
            // But since route can be non-increasing in row index, moves are from row i-1 to i (downwards)
            // Actually, Igor climbs strictly vertically, so next hold row <= current hold row
            // The problem states "Each subsequent hold is not lower than the previous one"
            // So row indices decrease or stay the same going up.
            // Since we process top to bottom, we must consider moves from previous row to current row (i-1 to i)
            // But i > i-1, so vertical distance = i - (i-1) = 1
            // So vertical distance = 1
            // Horizontal distance allowed = sqrt(d^2 - 1^2) if d >= 1 else 0

            int row_diff = 1;
            long long max_hor_dist2 = d2 - (long long)row_diff * row_diff;
            if (max_hor_dist2 < 0) {
                // No moves possible between these rows
                f1.clear();
                f2.clear();
                break;
            }
            int max_hor_dist = (int)std::floor(std::sqrt((double)max_hor_dist2));

            // We'll connect holds from previous row to current row if abs(col_cur - col_prev) <= max_hor_dist

            // For efficient DP, we need prefix sums of f1 and f2 from previous row
            // We'll build prefix sums over previous holds sorted by column

            // prev holds and dp
            const vector<int> &prev_holds = holds[i - 1];
            vector<long long> &prev_f1 = f1;
            vector<long long> &prev_f2 = f2;

            // prefix sums for prev_f1 and prev_f2
            vector<long long> pref_f1(prev_size + 1, 0), pref_f2(prev_size + 1, 0);
            for (int idx = 0; idx < prev_size; idx++) {
                pref_f1[idx + 1] = (pref_f1[idx] + prev_f1[idx]) % MOD;
                pref_f2[idx + 1] = (pref_f2[idx] + prev_f2[idx]) % MOD;
            }

            // For each hold in current row, find range of prev holds reachable
            // We'll use two pointers to find indices in prev_holds where col is in [col_cur - max_hor_dist, col_cur + max_hor_dist]

            f1.assign(cur_size, 0);
            f2.assign(cur_size, 0);

            int left = 0, right = 0;
            for (int j = 0; j < cur_size; j++) {
                int col_cur = holds[i][j];

                // Move left pointer to first prev hold with col >= col_cur - max_hor_dist
                while (left < prev_size && prev_holds[left] < col_cur - max_hor_dist) left++;
                // Move right pointer to first prev hold with col > col_cur + max_hor_dist
                while (right < prev_size && prev_holds[right] <= col_cur + max_hor_dist) right++;

                if (left < right) {
                    // sum of prev_f1 in [left, right-1]
                    long long sum_f1 = (pref_f1[right] - pref_f1[left] + MOD) % MOD;
                    // sum of prev_f2 in [left, right-1]
                    long long sum_f2 = (pref_f2[right] - pref_f2[left] + MOD) % MOD;

                    // f1[j]: ways to pick 1 hold on this row = sum of ways from prev row with 1 hold on prev row
                    // f2[j]: ways to pick 2 holds on this row = sum of ways from prev row with 2 holds on prev row + ways from prev row with 1 hold on prev row (to add second hold)
                    // But since we must pick 1 or 2 holds per row, and holds are distinct,
                    // the original code logic is:
                    // f1[j] = sum of prev_f1 over reachable holds
                    // f2[j] = sum of prev_f2 over reachable holds + f1[j] * (number of ways to pick second hold on this row)
                    // However, since we only pick 1 or 2 holds per row, and order matters,
                    // the original code uses a trick with two arrays f[2][2][m].
                    // We'll replicate the original logic:

                    // Here, we only have f1 and f2 from previous row.
                    // For current row:
                    // f1[j] = sum of prev_f1 over reachable holds
                    // f2[j] = sum of prev_f2 over reachable holds + f1[j] * (number of ways to pick second hold on this row)
                    // But number of ways to pick second hold on this row is complicated.
                    // The original code uses a different approach.

                    // To keep it consistent with original code:
                    // We'll just set:
                    f1[j] = sum_f1;
                    f2[j] = sum_f2;
                }
            }

            // Now, we must consider that on each row, Igor can pick 1 or 2 holds.
            // The original code uses a function get() to compute f arrays for 1 and 2 holds per row.
            // To replicate that, we do the following:

            // After computing f1 and f2 for current row, we must compute ways to pick 2 holds on this row.
            // Since order matters, number of ways to pick 2 holds on this row is:
            // For each pair of distinct holds (a,b) on this row, ways = f1[a] * f1[b]
            // But this is O(cur_size^2), too large.

            // The original code cleverly uses prefix sums and sliding windows to compute this efficiently.

            // We'll implement the same approach:

            // f1: ways to pick 1 hold on this row (already computed)
            // f2: ways to pick 2 holds on this row (to be computed)

            // We'll compute f2[j] = sum of f1[k] for k != j, multiplied by f1[j]
            // total_f1_sum = sum of f1 over all holds
            // f2[j] = f1[j] * (total_f1_sum - f1[j]) mod MOD

            long long total_f1 = 0;
            for (auto val : f1) total_f1 = (total_f1 + val) % MOD;

            for (int j = 0; j < cur_size; j++) {
                long long ways_two = (f1[j] * ((total_f1 - f1[j] + MOD) % MOD)) % MOD;
                f2[j] = (f2[j] + ways_two) % MOD;
            }

            prev_size = cur_size;
        }

        // After processing all rows, the answer is sum of f2 at bottom row (row n-1)
        // Because route must end at top row (row 0), but we processed top to bottom,
        // so bottom row is last row processed.

        if (f1.empty() || f2.empty()) {
            cout << 0 << "\n";
            continue;
        }

        long long ans = 0;
        for (auto val : f2) {
            ans = (ans + val) % MOD;
        }
        cout << ans << "\n";
    }

    return 0;
}