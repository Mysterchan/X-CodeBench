#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i,a,b) for(int i=(a); i<(b); ++i)
const int MOD = 1000000007;
ll modpow(ll a, ll e) {
    ll r = 1;
    a %= MOD;
    while (e) {
        if (e & 1) r = r * a % MOD;
        a = a * a % MOD;
        e >>= 1;
    }
    return r;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        ll n, m;
        int k;
        cin >> n >> m >> k;
        ll B_total = 2 * n + 2 * m - 8;
        ll fixed_on_B = 0;
        int S_fixed = 0;
        rep(i, 0, k) {
            ll x, y;
            int c;
            cin >> x >> y >> c;
            bool border = (x == 1 || x == n || y == 1 || y == m);
            bool corner = ((x == 1 || x == n) && (y == 1 || y == m));
            if (border && !corner) {
                fixed_on_B++;
                S_fixed ^= c;
            }
        }
        ll N_unknown = n * m - k;
        ll U_B = B_total - fixed_on_B;
        ll ans;
        if (U_B == 0) {
            ans = (S_fixed == 0 ? modpow(2, N_unknown) : 0);
        } else {
            ans = modpow(2, N_unknown - 1);
        }
        cout << ans << "\n";
    }
    return 0;
}
