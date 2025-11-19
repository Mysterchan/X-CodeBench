#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)(n); i++)
#define rep2(i, s, n) for (ll i = (ll)(s); i < (ll)(n); i++)


void vec1print(vector<ll> vec) {
    rep(i, vec.size()) {
        cout << vec[i] << endl;
    }
}
void vec2print(vector<ll> vec) {
    rep(i, vec.size()) {
        cout << vec[i] << " ";
    }
    cout << endl;
}

int minval(vector<ll> vec) {
    return *min_element(begin(vec), end(vec));
}
int maxval(vector<ll> vec) {
    return *max_element(begin(vec), end(vec));
}

void solve() {
    ll h, w, hmin = 1000, hmax = -1, wmin = 1000, wmax = -1;
    cin >> h >> w;
    bool flag = true;
    vector<string> s(h);
    rep(i, h) {
        cin >> s[i];
        rep(j, w) {
            if (s[i][j] == '#') {
                hmin = min(hmin, i);
                hmax = max(hmax, i);
                wmin = min(wmin, j);
                wmax = max(wmax, j);
            }
        }
    }
    for (int i = hmin; i <= hmax; i++) {
        for (int j = wmin; j <= wmax; j++) {
            if (s[i][j] == '.') {
                flag = false;
            }
        }
    }
    if (flag) cout << "Yes" << endl;
    else cout << "No" << endl;

    return;
}

int main() {
    solve();
    return 0;
}