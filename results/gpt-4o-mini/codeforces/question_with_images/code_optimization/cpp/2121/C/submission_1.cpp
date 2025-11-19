#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        vector<vector<int>> matrix(n, vector<int>(m));
        int max_val = 0;
        
        // Read the matrix and determine the initial maximum value
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> matrix[i][j];
                max_val = max(max_val, matrix[i][j]);
            }
        }

        // Find the current maximum values in each row and column
        vector<int> row_max(n, 0), col_max(m, 0);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                row_max[i] = max(row_max[i], matrix[i][j]);
                col_max[j] = max(col_max[j], matrix[i][j]);
            }
        }

        // Calculate the minimum possible maximum value after one operation
        int min_possible_max = max_val;
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                int new_max = max(row_max[r] - 1, col_max[c] - 1);
                // Check if the current cell affects the new maximum
                if (matrix[r][c] == row_max[r] || matrix[r][c] == col_max[c]) {
                    new_max = max(new_max, row_max[r] + col_max[c] - matrix[r][c] - 1);
                }
                min_possible_max = min(min_possible_max, new_max);
            }
        }

        cout << min_possible_max << '\n';
    }
    return 0;
}