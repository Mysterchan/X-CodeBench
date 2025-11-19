#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    while (t--) {
        int n, m; cin >> n >> m;
        vector<vector<int>> a(n, vector<int>(m));
        vector<int> row_max(n, 0), col_max(m, 0);
        int global_max = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> a[i][j];
                if (a[i][j] > row_max[i]) row_max[i] = a[i][j];
                if (a[i][j] > col_max[j]) col_max[j] = a[i][j];
                if (a[i][j] > global_max) global_max = a[i][j];
            }
        }

        // We want to minimize max( max_row_except_r, max_col_except_c, a[r][c]-1 )
        // After operation: 
        // - row r and column c cells decrease by 1
        // - others remain same
        // So max in matrix after operation is max of:
        //   max row max except r (unchanged)
        //   max col max except c (unchanged)
        //   max in row r and col c after decrement (which is a[r][c]-1)
        //
        // We try all pairs (r,c) where a[r][c] == global_max (only these can reduce max)
        // and pick minimal max after operation.

        // To speed up, precompute max_row_except and max_col_except for each row and column:
        // But since max_row and max_col are single values, max_row_except_r = max of all row_max except r
        // Similarly for columns.

        // Precompute max_row_except for each row:
        // max_row_except_r = max of row_max for all rows except r
        // Similarly for columns.

        // To do this efficiently, find top two max in row_max and col_max arrays.

        int max_row1 = 0, max_row2 = 0, max_row1_idx = -1;
        for (int i = 0; i < n; i++) {
            if (row_max[i] > max_row1) {
                max_row2 = max_row1;
                max_row1 = row_max[i];
                max_row1_idx = i;
            } else if (row_max[i] > max_row2) {
                max_row2 = row_max[i];
            }
        }

        int max_col1 = 0, max_col2 = 0, max_col1_idx = -1;
        for (int j = 0; j < m; j++) {
            if (col_max[j] > max_col1) {
                max_col2 = max_col1;
                max_col1 = col_max[j];
                max_col1_idx = j;
            } else if (col_max[j] > max_col2) {
                max_col2 = col_max[j];
            }
        }

        int ans = 101;

        for (int i = 0; i < n; i++) {
            int max_row_except = (i == max_row1_idx) ? max_row2 : max_row1;
            for (int j = 0; j < m; j++) {
                if (a[i][j] == global_max) {
                    int max_col_except = (j == max_col1_idx) ? max_col2 : max_col1;
                    int candidate = max({max_row_except, max_col_except, a[i][j] - 1});
                    if (candidate < ans) ans = candidate;
                }
            }
        }

        cout << ans << '\n';
    }
}