#include <bits/stdc++.h>
#define pb push_back
#define sz(x) (int)x.size()
#define all(x) x.begin(), x.end()
#define f first
#define s second

using namespace std;
using ll = long long;
using pii = pair <int, int>;

const int N = 2e5 + 5, mod = 998244353;
const ll inf = 1e18;

int n, k, c[100][100];
ll dp[(1 << 8)][100][100];

int main() {
    ios :: sync_with_stdio(0);
    cin.tie(0), cout.tie(0);
    cin >> n >> k;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            cin >> c[i][j];
        }
    }
    for (int m = 1; m <= n; ++m) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) 
                c[i][j] = min(c[i][j], c[i][m] + c[m][j]);
        }
    }
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j)
            dp[0][i][j] = c[i][j];
    }
    for (int mask = 1; mask < (1 << k); ++mask) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                dp[mask][i][j] = inf;
            }
        }
    }
    for (int i = 0; i < k; ++i) {
        dp[(1 << i)][i + 1][i + 1] = 0;
    }
    
    vector<ll> mn_b(n + 1), mn_bd(n + 1);
    
    for (int mask = 1; mask < (1 << k); ++mask) {
        for (int sub1 = mask; ; sub1 = (sub1 - 1) & mask) {
            int sub2 = (mask ^ sub1);
            
            for (int b = 1; b <= n; ++b) {
                mn_b[b] = inf;
                for (int e = 1; e <= n; ++e) {
                    mn_b[b] = min(mn_b[b], dp[sub2][e][e] + c[b][e]);
                }
            }
            
            for (int b = 1; b <= n; ++b) {
                for (int a = 1; a <= n; ++a) 
                    dp[mask][a][b] = min(dp[mask][a][b], dp[sub1][a][b] + mn_b[b]);
                
                for (int d = 1; d <= n; ++d) {
                    mn_bd[d] = inf;
                    for (int e = 1; e <= n; ++e)
                        mn_bd[d] = min(mn_bd[d], dp[sub2][d][e] + c[b][e]);
                }
                
                for (int d = 1; d <= n; ++d) {
                    for (int a = 1; a <= n; ++a)
                        dp[mask][a][d] = min(dp[mask][a][d], dp[sub1][a][b] + mn_bd[d]);
                }
            }
            if (sub1 == 0) break;
        }
    }
    int q;
    cin >> q;
    while (q--) {
        int s, t;
        cin >> s >> t;
        cout << dp[(1 << k) - 1][s][t] << '\n';
    }
    return 0;
}