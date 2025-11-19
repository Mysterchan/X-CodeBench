#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int n, m, k; cin >> n >> m >> k;
        vector<string> mat(n);
        for (int i = 0; i < n; i++) cin >> mat[i];

        // Precompute total gold count
        int total_gold = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (mat[i][j] == 'g') total_gold++;

        // We want to find the minimal gold inside the inner square for any empty cell
        // The explosion square is (2k+1) x (2k+1)
        // Inner square is (2k-1) x (2k-1) centered at (x,y)
        // Gold inside inner square disappears, gold on boundary is collected

        // To quickly get number of gold in any rectangle, build prefix sums
        vector<vector<int>> prefix(n + 1, vector<int>(m + 1, 0));
        for (int i = 0; i < n; i++) {
            int row_sum = 0;
            for (int j = 0; j < m; j++) {
                row_sum += (mat[i][j] == 'g' ? 1 : 0);
                prefix[i + 1][j + 1] = prefix[i][j + 1] + row_sum;
            }
        }

        // Function to get gold count in rectangle [r1,r2] x [c1,c2], inclusive
        auto get_gold = [&](int r1, int c1, int r2, int c2) -> int {
            if (r1 > r2 || c1 > c2) return 0;
            r1 = max(r1, 0);
            c1 = max(c1, 0);
            r2 = min(r2, n - 1);
            c2 = min(c2, m - 1);
            if (r1 > r2 || c1 > c2) return 0;
            return prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] - prefix[r2 + 1][c1] + prefix[r1][c1];
        };

        int side = 2 * k + 1;
        int inner_side = side - 2; // 2k-1

        int min_inner_gold = INT_MAX;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (mat[i][j] == '.') {
                    // Inner square boundaries
                    int r1 = i - k + 1;
                    int c1 = j - k + 1;
                    int r2 = i + k - 1;
                    int c2 = j + k - 1;

                    int inner_gold = get_gold(r1, c1, r2, c2);
                    if (inner_gold < min_inner_gold) {
                        min_inner_gold = inner_gold;
                    }
                }
            }
        }

        if (min_inner_gold == INT_MAX) {
            // No empty cell found (problem guarantees at least one empty cell, but just in case)
            cout << 0 << "\n";
        } else {
            // Maximum gold collected = total_gold - minimal gold destroyed inside inner square
            cout << total_gold - min_inner_gold << "\n";
        }
    }

    return 0;
}