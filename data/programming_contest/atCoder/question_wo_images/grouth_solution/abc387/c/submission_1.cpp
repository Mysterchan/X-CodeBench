#include <bits/stdc++.h>
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define ff first
#define ss second

using namespace std;
using ll = long long;

const ll mod = 1e9 + 7;
const ll INF = 1e18;
const ll N = (2e5 + 10) * 30;
const ll con = 37;

ll dx[4] = {-1, 1, 0, 0};
ll dy[4] = {0, 0, -1, 1};

ll binpow(ll x, ll n){
    ll ans = 1;
    while(n){
        if(n & 1) ans = ans * x;
        x = x * x;
        n /= 2;
    }
    return ans;
}

ll get(ll r){
    vector<int> f;
    while (r) {
        f.pb(r % 10);
        r /= 10;
    }
    reverse(all(f));
    int n = f.size();
    ll ans = 0;
    for (int i = 1; i <= n; i++) {
        if (i == n) {
            ans++;
            break;
        }
        ans += binpow(f[0], n - 1 - i) * min(f[0], f[i]);
        if (f[i] >= f[0]) break;
    }
    for (int i = 0; i < n; i++) {
        int mx = (i ? 9 : f[0] - 1);
        for (int j = 1; j <= mx; j++) {
            ans += binpow(j, n - 1 - i);
        }
    }
    return ans;
}

void solve(){
    ll l, r;
    cin >> l >> r;
    cout << get(r) - get(l - 1);
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    ll t = 1;
    // cin >> t;
    while(t--){
        solve();
    }
    
    return 0;
}