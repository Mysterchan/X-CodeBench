#include<bits/stdc++.h>
using namespace std;

void solve() {
    int n, q;
    scanf("%d%d", &n, &q);
    vector<vector<char>> grid(n + 2, vector<char>(n + 2, '.'));
    
    for (int i = 1; i <= n; i++) {
        scanf("%s", &grid[i][1]);
    }
    
    vector<vector<int>> pre(n + 1, vector<int>(n + 1, 0));

    // Create a prefix sum array to count white cells in 2x2 blocks
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < n; j++) {
            if (grid[i][j] == '.' && grid[i][j + 1] == '.' && grid[i + 1][j] == '.' && grid[i + 1][j + 1] == '.') {
                pre[i][j] = 1;
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            pre[i][j] += pre[i][j - 1] + pre[i - 1][j] - pre[i - 1][j - 1];
        }
    }

    while (q--) {
        int u, d, l, r;
        scanf("%d%d%d%d", &u, &d, &l, &r);
        
        // Calculate the number of 2x2 white squares in the queried region
        int total = pre[d - 1][r - 1] - pre[d - 1][l - 1] - pre[u - 1][r - 1] + pre[u - 1][l - 1];
        printf("%d\n", total);
    }
}

int main() {
    solve();
    return 0;
}
