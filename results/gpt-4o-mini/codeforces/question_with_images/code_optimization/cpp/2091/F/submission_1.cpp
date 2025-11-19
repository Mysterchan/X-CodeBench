#include <bits/stdc++.h>
#define int long long
using namespace std;

const int N = 2010, mod = 998244353;
char ar[N][N];
int n, m, d;
int f[N][2];

int dist(int i1, int j1, int i2, int j2) {
    return (i1 - i2) * (i1 - i2) + (j1 - j2) * (j1 - j2); // Compare squared distance to avoid sqrt
}

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    while (T--) {
        cin >> n >> m >> d;
        d *= d; // Use squared distance
        
        vector<vector<int>> holds(n + 1); // holds[i] contains columns of holds in row i
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                char c;
                cin >> c;
                if (c == 'X') holds[i].push_back(j);
            }
        }

        memset(f, 0, sizeof(f));
        for (auto col : holds[1]) {
            f[col][0]++; // First row initialization (only if holds exist)
        }

        for (int i = 2; i <= n; ++i) {
            int current = 1 - ((i + 1) & 1); 
            int previous = 1 - current; // alternating rows

            for (int j = 1; j <= m; ++j) f[j][current] = 0; // Reset current row
            for (auto col_cur : holds[i]) {
                for (auto col_prev : holds[i - 1]) {
                    if (dist(i, col_cur, i - 1, col_prev) <= d) {
                        f[col_cur][current] = (f[col_cur][current] + f[col_prev][previous]) % mod;
                    }
                }
            }
        }

        int ans = 0;
        for (auto col : holds[n]) {
            ans = (ans + f[col][(n + 1) & 1]) % mod; // Aggregate results from the last row
        }
        cout << ans << '\n';
    }
    return 0;
}