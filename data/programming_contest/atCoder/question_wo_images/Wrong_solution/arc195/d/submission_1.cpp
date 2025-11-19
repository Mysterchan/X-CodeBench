#include <bits/stdc++.h>
using namespace std;
#define int long long
const int N = 2e5 + 5;
int n, a[N], dp[N];
void solve() {
    for (int i = 1; i <= n + 1; i++) a[i] = 0, dp[i] = 0;
    cin >> n;
    int ans = 0;
    for (int i = 1; i <= n; i++) cin >> a[i], ans += (i == 1 || a[i] != a[i - 1]);
    for (int i = n - 3; i >= 1; i--) {
        if (a[i] == a[i + 2] && a[i + 1] == a[i + 3] && a[i] != a[i + 1]) {
            dp[i] = dp[i + 3] + 1;
        } 
        dp[i] = max(dp[i], dp[i + 1]);
    }
    cout << ans - dp[1] << "\n";
}
signed main() {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int t = 1; cin >> t;
    while (t--) solve();
    return 0;
}
