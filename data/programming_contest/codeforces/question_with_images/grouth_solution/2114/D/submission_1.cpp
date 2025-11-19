#include <bits/stdc++.h>
#include <cassert>

using namespace std;
using ll = long long;

#define all(x) (x).begin(), (x).end()
#define sz(x) (int)(x).size()
#define pb push_back
#define int ll

mt19937 rnd(chrono::steady_clock::now().time_since_epoch().count());
template<typename T>
void shuf(vector<T>& a) {
    for (int i = 1; i < sz(a); i++) swap(a[i], a[rnd() % (i + 1)]);
}

void solve() {
    int n; cin >> n;
    vector<int> x(n), y(n);
    for (int i = 0; i < n; i++) cin >> x[i] >> y[i];
    if (n == 1) {
        cout << 1 << '\n';
        return;
    }
    multiset<int> X, Y;
    for (int i = 0; i < n; i++) {
        X.insert(x[i]); Y.insert(y[i]);
    }
    int ans = 3e18;
    for (int i = 0; i < n; i++) {
        X.erase(X.find(x[i])); Y.erase(Y.find(y[i]));
        int w = *X.rbegin() - *X.begin() + 1;
        int h = *Y.rbegin() - *Y.begin() + 1;
        if (w * h == n - 1) {   
            ans = min(ans, min((h + 1) * w, h * (w + 1)));
        } else ans = min(ans, h * w);
        X.insert(x[i]); Y.insert(y[i]);
    }
    cout << ans << '\n';
}

signed main() {
    int tt = 1;
    #ifdef LOCAL
        freopen("in.txt", "r", stdin);
        freopen("out.txt", "w", stdout);
    #else
        ios::sync_with_stdio(false);
        cin.tie(0); cout.tie(0);
    #endif
    cin >> tt;

    while (tt--) {
        solve();
    }

    return 0;
}
