#include <bits/stdc++.h>

using namespace std;

const int N = 200010, M = 19;
int n, m, a[N], f[1<<M][M];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> m;
    for(int i = 1; i <= n; ++i) {
        string s;
        cin >> s;
        a[i] = 0;
        for(int j = 0; j < m; ++j) {
            if(s[j] == '1') a[i] |= 1<<j;
        }
        f[a[i]][0]++;
    }
    for(int j = 1; j <= m; j++) {
        for(int x = 0; x < (1<<m); x++) {
            for(int c = m; c >= 0; c--) {
                f[x][c] = f[x][c] + (c? f[x^(1<<j - 1)][c - 1]: 0);
            }
        }
    }
    int ans = 1e9;
    for(int x = 0; x < (1<<m); ++x) {
        int sum = 0;
        for(int c = 0; c <= m; ++c) {
            sum += f[x][c] * min(c, m - c);
        }
        ans = min(ans, sum);
    }
    cout << ans << endl;
    return 0;
}