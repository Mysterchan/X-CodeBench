#include <bits/stdc++.h>
using namespace std;

#ifdef SAWALHY
#include "debug.hpp"
#else
#define debug(...) 0
#define debug_itr(...) 0
#define debug_bits(...) 0
#endif

#define int long long
#define ll long long
#define vi vector<int>
#define vvi vector<vector<int>>
#define pii pair<int, int>
#define vii vector<pii>
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()
#define minit(v, x) v = min(v, x)
#define maxit(v, x) v = max(v, x)

void solve() {
    int n, m, k;
    cin >> n >> m >> k;
    map<int, int> fr;
    for (int i = 0; i < k; i++) {
        int x, y;
        cin >> x >> y;
        fr[y]++;
    }
    auto [y, f] = *fr.rbegin();

    if (m == 1) {
        cout << "Yuyu\n";
        return;
    }

    if (n > 1) {
        if (f & 1) {
            cout << "Mimo\n";
        } else {
            cout << "Yuyu\n";
        }
        return;
    }

    int tot = 0;
    for (int i = y; i > 1; i--) {
        tot += tot + fr[i];
        tot &= 1;
    }
    if (tot & 1) {
        cout << "Mimo\n";
    } else {
        cout << "Yuyu\n";
    }
}

int32_t main(int32_t argc, char **argv) {
    cin.tie(nullptr)->sync_with_stdio(false);

    int T = 1;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        debug("-----", t);
        solve();
    }

    return 0;
}
