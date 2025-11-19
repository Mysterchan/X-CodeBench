#include <iostream>
using namespace std;
using ll = long long;

const int mod = 998244353;

ll qpow(ll a, ll b) {
    ll ret = 1;
    a %= mod;
    while (b) {
        if (b & 1) {
            ret = ret * a % mod;
        }
        a = a * a % mod;
        b >>= 1;
    }
    return ret;
}

void solve() {
    ll n, m;
    scanf("%lld %lld", &n, &m);
    
    // Precompute all powers we need
    ll pow2_m = qpow(2, m);
    ll pow2_n1 = qpow(2, n - 1);
    ll pow3_n1 = qpow(3, n - 1);
    ll pow4_n1 = qpow(4, n - 1);
    ll pow_m1_n1 = qpow(m + 1, n - 1);
    
    // Compute binomial coefficients directly
    ll cm2 = (m % mod) * ((m - 1) % mod) % mod * qpow(2, mod - 2) % mod;
    ll cm3 = (m % mod) * ((m - 1) % mod) % mod * ((m - 2) % mod) % mod * qpow(6, mod - 2) % mod;
    
    ll ans1 = pow_m1_n1;
    
    ll ans2 = cm2 * ((pow4_n1 - pow3_n1 + mod) % mod) % mod;
    
    ll temp3 = (pow4_n1 - 3 * pow3_n1 % mod + 3 * pow2_n1 % mod - 1 + 4 * mod) % mod;
    ll ans3 = cm3 * temp3 % mod;
    
    ll temp4 = (pow_m1_n1 - (m - 1) % mod * ((pow3_n1 - pow2_n1 + mod) % mod) % mod - pow2_n1 + 2 * mod) % mod;
    ll ans4 = (m % mod) * temp4 % mod;
    
    ll ans = (ans1 + ans2 + ans3 + ans4) % mod * pow2_m % mod;
    printf("%lld\n", ans);
}

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        solve();
    }
    return 0;
}