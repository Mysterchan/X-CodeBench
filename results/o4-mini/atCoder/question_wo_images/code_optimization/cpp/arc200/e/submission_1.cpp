#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll mod = 998244353;
inline ll addmod(ll a, ll b) { a += b; return (a >= mod ? a - mod : a); }
inline ll submod(ll a, ll b) { a -= b; return (a < 0 ? a + mod : a); }
inline ll mulmod(ll a, ll b) { return (ll)((__int128)a * b % mod); }
ll qpow(ll a, ll b) {
    ll r = 1;
    a %= mod;
    while (b) {
        if (b & 1) r = mulmod(r, a);
        a = mulmod(a, a);
        b >>= 1;
    }
    return r;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    const ll inv2 = 499122177;    // 2^{-1} mod
    const ll inv6 = 166374059;    // 6^{-1} mod

    int T;
    cin >> T;
    while (T--) {
        ll n, m;
        cin >> n >> m;
        ll mm = m % mod;
        ll e = n - 1;
        // compute needed powers
        ll p2 = qpow(2, e);
        ll p3 = qpow(3, e);
        ll p_m1 = qpow(addmod(mm, 1), e);
        ll p2m = qpow(2, mm);
        // compute C(m,2) and C(m,3)
        ll C2 = mulmod(mulmod(mm, submod(mm, 1)), inv2);
        ll C3 = mulmod(mulmod(mulmod(mm, submod(mm, 1)), submod(mm, 2)), inv6);
        // term1
        ll term1 = p_m1;
        // term2 = C2 * (4^{n-1} - 3^{n-1})
        ll p4 = mulmod(p2, p2);
        ll term2 = mulmod(C2, submod(p4, p3));
        // term3 = C3 * (4^{n-1} - 3*3^{n-1} + 3*2^{n-1} - 1)
        ll tmp = p4;
        tmp = submod(tmp, mulmod(3, p3));
        tmp = addmod(tmp, mulmod(3, p2));
        tmp = submod(tmp, 1);
        ll term3 = mulmod(C3, tmp);
        // term4 = m * ( (m+1)^{n-1} - (m-1)*(3^{n-1} - 2^{n-1}) - 2^{n-1} )
        ll diff32 = submod(p3, p2);
        ll part = mulmod(submod(mm, 1), diff32);
        ll tmp2 = submod(p_m1, part);
        tmp2 = submod(tmp2, p2);
        ll term4 = mulmod(mm, tmp2);
        // sum up
        ll sum = term1;
        sum = addmod(sum, term2);
        sum = addmod(sum, term3);
        sum = addmod(sum, term4);
        // final multiply by 2^m
        ll ans = mulmod(sum, p2m);
        cout << ans << '\n';
    }
    return 0;
}