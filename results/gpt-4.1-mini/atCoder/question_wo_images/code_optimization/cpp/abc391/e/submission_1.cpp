#include <bits/stdc++.h>
using namespace std;

int n;
string s;
vector<string> ve;
vector<vector<int>> dp0, dp1;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> s;
    ve.resize(n + 2);
    ve[n + 1] = s;

    // Build the majority strings from bottom up
    for (int i = n + 1; i >= 2; i--) {
        string &cur = ve[i];
        string &prev = ve[i - 1];
        prev.reserve(cur.size() / 3);
        for (int j = 0; j < (int)cur.size(); j += 3) {
            int cnt0 = (cur[j] == '0') + (cur[j + 1] == '0') + (cur[j + 2] == '0');
            int cnt1 = 3 - cnt0;
            prev.push_back(cnt0 > cnt1 ? '0' : '1');
        }
    }

    // dp0[i][j]: minimal changes to make subtree rooted at (i,j) result in '0'
    // dp1[i][j]: minimal changes to make subtree rooted at (i,j) result in '1'
    dp0.assign(n + 2, vector<int>());
    dp1.assign(n + 2, vector<int>());

    // Initialize dp at bottom layer (leaves)
    int len = (int)ve[n + 1].size();
    dp0[n + 1].resize(len);
    dp1[n + 1].resize(len);
    for (int i = 0; i < len; i++) {
        dp0[n + 1][i] = (ve[n + 1][i] == '0') ? 0 : 1;
        dp1[n + 1][i] = (ve[n + 1][i] == '1') ? 0 : 1;
    }

    // Bottom-up DP
    for (int level = n; level >= 1; level--) {
        int length = (int)ve[level].size();
        dp0[level].resize(length);
        dp1[level].resize(length);

        for (int i = 0; i < length; i++) {
            int base = i * 3;
            // For the three children at level+1
            // We want minimal changes to get majority 0 or 1 at this node

            // For each child, we have dp0 and dp1 costs
            // We try all combinations of children values to get majority 0 or 1

            // To get majority 0: at least 2 children are 0
            // To get majority 1: at least 2 children are 1

            // We'll try all 8 combinations (2^3) of children values and pick minimal cost
            int best0 = INT_MAX;
            int best1 = INT_MAX;

            // Children indices
            int c0 = base, c1 = base + 1, c2 = base + 2;

            // For each combination of children values (0 or 1)
            for (int mask = 0; mask < 8; mask++) {
                int cnt0 = 0, cnt1 = 0;
                int cost = 0;

                // child 0
                if (mask & 1) {
                    cost += dp1[level + 1][c0];
                    cnt1++;
                } else {
                    cost += dp0[level + 1][c0];
                    cnt0++;
                }
                // child 1
                if (mask & 2) {
                    cost += dp1[level + 1][c1];
                    cnt1++;
                } else {
                    cost += dp0[level + 1][c1];
                    cnt0++;
                }
                // child 2
                if (mask & 4) {
                    cost += dp1[level + 1][c2];
                    cnt1++;
                } else {
                    cost += dp0[level + 1][c2];
                    cnt0++;
                }

                if (cnt0 >= 2) {
                    best0 = min(best0, cost);
                }
                if (cnt1 >= 2) {
                    best1 = min(best1, cost);
                }
            }
            dp0[level][i] = best0;
            dp1[level][i] = best1;
        }
    }

    // The original final value is ve[1][0]
    // We want minimal changes to flip it
    char final_val = ve[1][0];
    int ans = (final_val == '0') ? dp1[1][0] : dp0[1][0];
    cout << ans << "\n";

    return 0;
}