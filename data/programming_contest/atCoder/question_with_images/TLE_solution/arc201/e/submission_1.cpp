#include <bits/stdc++.h>
#define pb push_back
#define sz(x) (int)x.size()
#define all(x) x.begin(), x.end()
#define f first
#define s second

using namespace std;
using ll = long long;
using pii = pair <int, int>;

const int N = 2e5 + 10, mod = 998244353;

int n, a[N];
int pw[N], rpw[N];

void add(int &x, int y) {
    x += y;
    if (x >= mod)
        x -= mod;
}

int bin_pw(int x, int y) {
    int res = 1;
    while (y) {
        if (y & 1)
            res = res * 1ll * x % mod;
        x = x * 1ll * x % mod;
        y >>= 1;
    }
    return res;
}

int main() {
    ios :: sync_with_stdio(0);
    cin.tie(0), cout.tie(0);
    cin >> n;
    pw[0] = rpw[0] = 1;
    for (int i = 1; i <= n + 3; ++i) {
        if (i <= n)
            cin >> a[i];
        pw[i] = pw[i - 1];
        add(pw[i], pw[i - 1]);
        rpw[i] = bin_pw(pw[i], mod - 2);
    }
    auto get = [&] (int i, int j) {

        vector <int> vals;
        for (int k = i; k <= j; ++k) vals.pb(a[k]);
        sort(all(vals));
        vector <int> psum(sz(vals));
        psum[0] = vals[0];
        for (int k = 1; k < j - i + 1; ++k) {
            psum[k] = psum[k - 1];
            add(psum[k], vals[k] * 1ll * pw[k] % mod);
        }

        int x = min(a[i], a[j]), y = max(a[i], a[j]);
        int L = lower_bound(all(vals), x) - vals.begin();
        int R = lower_bound(all(vals), y) - vals.begin();

        int res = 0;
        for (int mn_ind = 0; mn_ind < L; ++mn_ind) {

            int sum = (psum[sz(vals) - 1] - psum[R]) * 1ll * rpw[mn_ind + 3] % mod;
            add(res, sum);
            add(res, mod - (vals[mn_ind] * 1ll * (pw[sz(vals) - mn_ind - 3] - pw[R + 1 - mn_ind - 3] + mod) % mod));

            add(res, (vals[R] - vals[mn_ind]) * 1ll * pw[R - mn_ind - 2] % mod);
        }
        for (int mx_ind = sz(vals) - 1; mx_ind > R; mx_ind--) {
            int cnt = mx_ind - L - 2;
            add(res, (vals[mx_ind] - vals[L]) * 1ll * pw[cnt] % mod);
        }
        add(res, (vals[R] - vals[L]) * 1ll * pw[R - L - 1] % mod);
    

        return res;
    };
    int ans = 0;
    for (int i = 1; i <= n; ++i) {
        for (int j = i + 1; j <= n; ++j) {
            add(ans, (j - i) * 1ll * get(i, j) % mod);
        }
    }
    cout << ans;
    return 0;
}