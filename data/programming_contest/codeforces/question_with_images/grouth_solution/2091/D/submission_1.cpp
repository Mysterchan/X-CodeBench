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
    int n, m, k; cin >> n >> m >> k;
    auto check = [&](int x) -> bool {
        int full = m / (x + 1);
        int mx_uch = (m - full) * n;
        return mx_uch >= k;
    };
    int L = 0, R = m;
    while (R - L > 1) {
        int M = (L+R)/2;
        if(check(M))R=M;
        else L=M;
    }
    cout << R << '\n';
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
