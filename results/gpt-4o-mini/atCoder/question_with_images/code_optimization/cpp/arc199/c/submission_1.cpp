#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::vector;

constexpr int mod = 998244353;

vector<vector<bool>> g;

int count_good_trees(int n, int m, const vector<vector<int>>& permutations) {
    g.assign(n, vector<bool>(n, true));

    for (int i = 1; i < m; ++i) {
        const auto& sequence = permutations[i];

        for (int l = 0; l < n; ++l) {
            int mn = n, mx = -1;

            for (int r = l; r < n; ++r) {
                mn = std::min(mn, sequence[r]);
                mx = std::max(mx, sequence[r]);

                // Check if current segment [l, r] is valid
                g[l][r] = g[l][r] && (mx - mn == r - l);
            }
        }
    }

    // Initialize dp arrays
    vector<vector<int>> dp0(n + 1, vector<int>(n + 1, 0));
    vector<vector<int>> dp1(n + 1, vector<int>(n + 1, 0));

    // Base cases for dp functions
    for (int i = 0; i < n; ++i) {
        dp0[i][i] = 1; // Only one way to form tree with one node
        dp1[i][i] = 1; // Only one way to form tree with one node
    }

    // Fill dp0 and dp1
    for (int length = 2; length <= n; ++length) {
        for (int l = 0; l + length - 1 < n; ++l) {
            int r = l + length - 1;
            for (int root = l; root <= r; ++root) {
                dp0[l][r] = (dp0[l][r] + (1LL * dp1[l][root - 1] * dp0[root + 1][r]) % mod) % mod;
                if (g[l][r]) {
                    dp1[l][r] = (dp1[l][r] + (1LL * dp0[l][root - 1] * dp0[root + 1][r]) % mod) % mod;
                }
            }
        }
    }

    return dp0[0][n - 1];
}

int main() {
    std::ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> permutations(m, vector<int>(n));

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> permutations[i][j];
            permutations[i][j]--; // Use zero-based indexing
        }
    }

    cout << count_good_trees(n, m, permutations) << '\n';

    return 0;
}