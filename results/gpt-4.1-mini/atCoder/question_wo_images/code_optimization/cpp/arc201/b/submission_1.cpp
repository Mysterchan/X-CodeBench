#include <bits/stdc++.h>
using namespace std;

#define int long long

int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    const int BIT = 60;

    while (T--) {
        int N; 
        unsigned long long W;
        cin >> N >> W;

        vector<vector<int>> vals(BIT);
        for (int i = 0; i < N; i++) {
            int x, y; cin >> x >> y;
            vals[x].push_back(y);
        }

        // Sort each bucket descending and build prefix sums
        vector<vector<int>> prefix(BIT);
        for (int i = 0; i < BIT; i++) {
            sort(vals[i].rbegin(), vals[i].rend());
            prefix[i].push_back(0);
            for (auto v : vals[i]) prefix[i].push_back(prefix[i].back() + v);
        }

        // We'll try to pick items greedily from highest value sums per bit,
        // but we must consider the binary representation of W and carry overs.

        // dp[i][carry] = max value using bits [0..i-1] with carry from previous bit
        // carry can be 0 or 1
        // We'll process bits from 0 to 59

        // Since weights are powers of two, and we can pick any number of items per bit,
        // the total weight at bit i is number_of_items * 2^i.
        // The sum of weights at bit i plus carry from previous bit must not exceed W's bit i plus carry.

        // We'll use a bottom-up approach:
        // For each bit i, we try all possible number of items to pick (up to size of vals[i])
        // but we must be careful to prune search space.

        // To optimize, note that the maximum number of items we can pick at bit i is limited by:
        // (W >> i) + 2 (to allow carry overs)
        // But since W can be large, we cannot try all counts.

        // Instead, we use a greedy approach:
        // For each bit, we try to pick as many items as possible without exceeding W.

        // We'll implement a DP with states: dp[bit][carry] = max value
        // carry in {0,1}
        // For each bit, we try picking k items (0 <= k <= size(vals[i])) such that:
        // (k + carry) % 2 == (W >> i) & 1
        // and next carry = (k + carry) / 2

        // This is a classic knapsack with binary carry problem.

        vector<vector<int>> dp(BIT + 1, vector<int>(2, LLONG_MIN));
        dp[0][0] = 0;

        for (int i = 0; i < BIT; i++) {
            int bitW = (W >> i) & 1;
            int sz = (int)vals[i].size();

            // For each carry from previous bit
            vector<int> &pref = prefix[i];

            vector<int> ndp(2, LLONG_MIN);

            for (int carry = 0; carry <= 1; carry++) {
                if (dp[i][carry] == LLONG_MIN) continue;

                // We want to find k in [0, sz] such that (k + carry) % 2 == bitW
                // For each such k, next_carry = (k + carry) / 2
                // Update ndp[next_carry] = max(ndp[next_carry], dp[i][carry] + prefix[i][k])

                // Since k can be large, we only try k with parity = (bitW - carry + 2) % 2
                int parity = (bitW - carry + 2) % 2;

                // k starts from parity, increments by 2
                for (int k = parity; k <= sz; k += 2) {
                    int next_carry = (k + carry) / 2;
                    int val = dp[i][carry] + pref[k];
                    if (val > ndp[next_carry]) ndp[next_carry] = val;
                }
            }
            dp[i + 1] = move(ndp);
        }

        // After processing all bits, carry must be zero (no overflow)
        cout << max(dp[BIT][0], 0LL) << "\n";
    }

    return 0;
}