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
    ll n;
    cin >> n;
    vector<ll> p(n+1, 0);
    vector<ll> q(n+1, 0);
    vector<ll> s(n+1, 0);
    rep2(i,1,n+1) cin >> p[i];
    rep2(i,1,n+1) cin >> q[i];

    rep2(i,1,n+1) {
        s[q[i]] = q[p[i]];
    }
    rep2(i,1,n+1) {
        cout << s[i] << (i==n ? '\n' : ' ');
    }

    return;
}

int main() {
    solve();
    return 0;
}