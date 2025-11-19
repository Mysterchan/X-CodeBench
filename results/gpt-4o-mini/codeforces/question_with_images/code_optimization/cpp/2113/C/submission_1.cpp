#include <bits/stdc++.h>
using namespace std;
#define int long long

int collectGold(const vector<vector<char>>& mat, int n, int m, int k) {
    int totalGold = 0;
    vector<vector<int>> goldCount(n + 1, vector<int>(m + 1, 0));
    
    // Precompute the total number of golds
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (mat[i][j] == 'g') {
                totalGold++;
                goldCount[i + 1][j + 1] = 1; // 1-based index for prefix sum
            }
        }
    }
    
    // Create prefix sum for gold count
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            goldCount[i][j] += goldCount[i - 1][j] + goldCount[i][j - 1] - goldCount[i - 1][j - 1];
        }
    }

    int maxGoldCollected = 0;
    
    // Check each empty cell for detonation
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (mat[i][j] == '.') {
                int r1 = max(0, i - k);
                int c1 = max(0, j - k);
                int r2 = min(n - 1, i + k);
                int c2 = min(m - 1, j + k);
                
                // Count golds on the boundary
                int collectedGold = 0;
                for (int x = r1; x <= r2; ++x) {
                    if (x == r1 || x == r2) {
                        for (int y = c1; y <= c2; ++y) {
                            if (mat[x][y] == 'g') {
                                collectedGold++;
                            }
                        }
                    }
                }
                for (int y = c1; y <= c2; ++y) {
                    if (y == c1 || y == c2) {
                        for (int x = r1; x <= r2; ++x) {
                            if (mat[x][y] == 'g') {
                                collectedGold++;
                            }
                        }
                    }
                }
                
                maxGoldCollected = max(maxGoldCollected, collectedGold);
            }
        }
    }

    return totalGold - maxGoldCollected;
}

void solve() {
    int n, m, k; 
    cin >> n >> m >> k;
    vector<vector<char>> mat(n, vector<char>(m));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> mat[i][j];
        }
    }
    
    cout << collectGold(mat, n, m, k) << endl;
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}