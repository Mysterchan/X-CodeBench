#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> s(n);
        for (int i = 0; i < n; i++) {
            cin >> s[i];
        }

        // Handle fixed values
        vector<int> fixedIndexes;
        for (int i = 0; i < n; ++i) {
            if (s[i] != -1) {
                fixedIndexes.push_back(i);
            }
        }

        // Pre-check for instantaneous rejection
        bool valid = true;
        for (int i = 0; i < fixedIndexes.size(); ++i) {
            if (s[fixedIndexes[i]] > fixedIndexes[i]) {
                valid = false;
                break;
            }
        }

        if (!valid) {
            cout << 0 << endl;
            continue;
        }

        // Count number of free and constrained positions
        int freePositions = n - fixedIndexes.size();
        vector<int> nonFixed(n, 0);
        for (int i = 0; i < n; i++) {
            if (s[i] == -1) {
                nonFixed[i] = 1; // Mark non-fixed index
            }
        }

        // Generate valid scores
        vector<vector<long long>> dp(n + 1, vector<long long>(n + 1, 0));
        dp[0][0] = 1; // base case

        for (int i = 0; i < n; i++) {
            if (s[i] != -1) {
                // Propagate fixed values
                for (int j = n; j >= s[i]; j--) {
                    dp[j][i + 1] = (dp[j][i + 1] + dp[j - s[i]][i]) % MOD;
                }
            } else {
                // Free values can take any score from 0 to n-1
                for (int j = 0; j <= n; j++) {
                    dp[j][i + 1] = (dp[j][i + 1] + dp[j][i]) % MOD;
                    if (j > 0) {
                        dp[j][i + 1] = (dp[j][i + 1] + dp[j - 1][i]) % MOD;
                    }
                }
            }
        }

        cout << dp[freePositions][n] << endl;
    }
    return 0;
}