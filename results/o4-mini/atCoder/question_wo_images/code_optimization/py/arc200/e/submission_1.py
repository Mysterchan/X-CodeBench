#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
const int MOD = 998244353;

int64 modpow(int64 a, int64 e) {
    int64 r = 1 % MOD;
    a %= MOD;
    while (e > 0) {
        if (e & 1) r = (r * a) % MOD;
        a = (a * a) % MOD;
        e >>= 1;
    }
    return r;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    const int64 INV2 = (MOD + 1) / 2;
    const int64 INV6 = modpow(6, MOD - 2);

    while (T--) {
        int64 n, m;
        cin >> n >> m;
        // ans = (m+1)^(n-1)
        int64 pow_m1 = modpow(m + 1, n - 1);
        int64 ans = pow_m1;

        // tmp = (m+1)^(n-1) - 2^(n-1) - ((2^(n-1) - 1)*(m-1)/2)
        int64 p2_n1 = modpow(2, n - 1);
        int64 term = ( (p2_n1 - 1 + MOD) % MOD ) * ((m - 1) % MOD) % MOD * INV2 % MOD;
        int64 tmp = (pow_m1 - p2_n1 - term) % MOD;
        if (tmp < 0) tmp += MOD;
        ans = (ans + tmp * (m % MOD)) % MOD;

        if (n >= 4) {
            // tmp2 = 4^(n-1) - 3*3^(n-1) + 3*2^(n-1) - 1
            int64 p4_n1 = modpow(4, n - 1);
            int64 p3_n1 = modpow(3, n - 1);
            int64 tmp2 = (p4_n1
                          - 3 * p3_n1 % MOD
                          + 3 * p2_n1 % MOD
                          - 1) % MOD;
            if (tmp2 < 0) tmp2 += MOD;
            // mC3 + mC2
            int64 mm = m % MOD;
            int64 mC2 = mm * ((mm - 1 + MOD) % MOD) % MOD * INV2 % MOD;
            int64 mC3 = mm * ((mm - 1 + MOD) % MOD) % MOD * ((mm - 2 + MOD) % MOD) % MOD * INV6 % MOD;
            int64 sumC = (mC2 + mC3) % MOD;
            ans = (ans + tmp2 * sumC) % MOD;
        }

        // multiply by 2^m
        ans = ans * modpow(2, m) % MOD;
        cout << ans << "\n";
    }

    return 0;
}