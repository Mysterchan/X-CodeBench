#include <bits/stdc++.h>
#define int long long

using namespace std;

const int N = 2e6 + 1;
int vis[N], cnt[N], ans[N], a[N];

void solve() {
    int n, k;
    cin >> n >> k;

    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        vis[a[i]] = 1;
    }

    for (int i = 1; i < N; i++) {
        int sum = 0;
        for (int j = i; j < N; j += i) {
            sum += vis[j];
        }
        if (sum >= k) {
            for (int j = i; j < N; j += i) {
                ans[j] = max(ans[j], i);
            }
        }
    }
    for (int i = 1; i <= n; i++) {
        cout << ans[a[i]] << '\n';
    }
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);

    int t = 1;

    while (t--) solve();

    return 0;
}