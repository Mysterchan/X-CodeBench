#include <assert.h>
#include <iostream>
using namespace std;
using ui = unsigned int;
using ll = long long;
using ull = unsigned long long;
using i128 = __int128;
using ld = long double;
using f128 = __float128;
const int mod = 998244353;
ll qpow(ll a, ll b) {
    ll ret = 1;
    while (b) {
        if (b & 1) {
            ret = ret * a % mod;
        }
        a = a * a % mod;
        b >>= 1;
    }
    return ret;
}
ll C(int n, int m) {
    if (m < 0 || n < 0 || n < m) {
        return 0;
    }
    ll p = 1, q = 1;
    for (int i = 1; i <= n; i++) {
        p = p * i % mod;
    }
    for (int i = 1; i <= m; i++) {
        q = q * i % mod;
    }
    for (int i = 1; i <= n - m; i++) {
        q = q * i % mod;
    }
    return p * qpow(q, mod - 2) % mod;
}
ll n, m;
ll ans, ans1, ans2, ans3, ans4;
void solve() {
    ans = 0;
    scanf("%lld %lld", &n, &m);
    ll cm2 = C(m, 2);
    ll cm3 = C(m, 3);
    ans1 = qpow(m + 1, n - 1);
    ans2 = cm2 * (qpow(4, n - 1) - qpow(3, n - 1)) % mod;
    ans3 = cm3 * ((qpow(4, n - 1) - 3 * qpow(3, n - 1) + 3 * qpow(2, n - 1) - 1) % mod) %
           mod;
    ans4 = m *
           ((qpow(m + 1, n - 1) - (m - 1) * (qpow(3, n - 1) - qpow(2, n - 1)) - qpow(2, n - 1)) %
            mod) %
           mod;
    ans = (ans1 + ans2 + ans3 + ans4) * qpow(2, m) % mod;
    printf("%lld\n", (ans + mod) % mod);
}
int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        solve();
    }
    return 0;
}
