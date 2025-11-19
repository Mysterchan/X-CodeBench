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

const int mod = 998244353;

int sum(int x, int y) { return (x + y >= mod ? x + y - mod : x + y); }
int diff(int x, int y) { return (x - y < 0 ? x - y + mod : x - y); }
int mul(int x, int y) { return (x * y) % mod; }
int binpow(int x, int y) {
    int ans = 1, pw = x;
    while (y) {
        if (y & 1) { ans = mul(ans, pw); }
        pw = mul(pw, pw);
        y >>= 1;
    }
    return ans;
}
int rev(int x) { return binpow(x, mod - 2); }
int divide(int x, int y) { return mul(x, rev(y)); }

void solve() {
    int n, m, d; cin >> n >> m >> d;
    vector<string> s(n);
    for (auto &u : s) cin >> u;

    vector<int> dp(m);
    for (int j = 0; j < m; j++) dp[j] = (s[n - 1][j] == 'X');
    for (int i = n - 1; i >= 0; i--) {
        vector<int> pref(m + 1, 0);
        for (int j = 0; j < m; j++) pref[j + 1] = sum(pref[j], dp[j]);

        for (int j = 0; j < m; j++) {
            dp[j] = mul((s[i][j] == 'X'), diff(pref[min(m, j + d + 1)], pref[max(0ll, j - d)]));
        }
        if (i > 0) {
            vector<int> newdp(m);
            for (int j = 0; j < m; j++) pref[j + 1] = sum(pref[j], dp[j]);
            int D = d - 1;
            for (int j= 0; j < m; j++) {
                newdp[j] = mul((s[i - 1][j] == 'X'), diff(pref[min(m, j + D + 1)], pref[max(0ll, j - D)]));
            }
            swap(dp, newdp);
        }
    }
    int ans = 0;
    for (int &x : dp) ans = sum(ans, x);
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
