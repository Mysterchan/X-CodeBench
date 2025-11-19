#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <deque>

typedef long long ll;
#define int ll

using namespace std;

int f(vector<vector<int>> matrix, int &x, int &y, int &n, int &m) {
    for (int i = 0; i < m; i++) {
        --matrix[x][i];
    }
    for (int i = 0; i < n; i++) {
        --matrix[i][y];
    }
    ++matrix[x][y];
    int maxi = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            maxi = max(maxi, matrix[i][j]);
        }
    }
    return maxi;
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while(t--) {
        int n, m;
        cin >> n >> m;
        vector<vector<int>> matrix(n, vector<int>(m));
        int maxi = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> matrix[i][j];
                maxi = max(maxi, matrix[i][j]);
            }
        }
        set<int> x, y;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (matrix[i][j] == maxi) {
                    x.insert(i);
                    y.insert(j);
                }
            }
        }
        int ans = 101;
        for (int xi : x) {
            for (int yi : y) {
                int maxi1 = f(matrix, xi, yi, n, m);
                ans = min(ans, maxi1);
            }
        }
        cout << ans << '\n';
    }
}