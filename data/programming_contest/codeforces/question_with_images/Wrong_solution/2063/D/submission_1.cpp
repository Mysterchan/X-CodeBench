#include <bits/stdc++.h>
#define ent '\n'
#define int long long

#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma GCC optimize("Ofast,unroll-loops,fast-math,O3")

using namespace std;

const int maxn = 5e5 + 12;

int prefa[maxn], prefb[maxn];
int a[maxn], b[maxn];
int n, m, k;

int get(int x, int y) {
    if(n - 2 * x < y || m - 2 * y < x || x < 0 || y < 0) return -1e18;
    return prefa[n] - prefa[n - x] - prefa[x] + prefb[m] - prefb[m - y] - prefb[y];
}

void solve() {
    cin >> n >> m;
    for(int i = 1; i <= n; i++) {
        cin >> a[i];
    }
    for(int i = 1; i <= m; i++) {
        cin >> b[i];
    }

    sort(a + 1, a + n + 1);
    sort(b + 1, b + m + 1);
    int cnt = m - n, ans = 0;
    for(int i = 1; i <= n; i++) {
        prefa[i] = prefa[i - 1] + a[i];
    }
    for(int i = 1; i <= m; i++) {
        prefb[i] = prefb[i - 1] + b[i];
    }
    k = min({n, m, (n + m) / 3});
    cout << k << ent;

    int x = 0, y = 0;
    for(int i = 1; i <= k; i++) {
        int nx = -1, ny = -1;
        for(int x1 = max(0ll, x - 5); x1 <= x + 5; x1++) {
            int y1 = i - x1;
            if(get(x1, y1) > get(nx, ny)) {
                nx = x1, ny = y1;
            }
        }
        cout << get(nx, ny) << ' ';
    }
    cout << ent;
}

int32_t main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }
}