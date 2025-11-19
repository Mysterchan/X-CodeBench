#include <iostream>
using namespace std;

const int mod = 998244353;

long long qpow(long long a, long long b) {
    long long ret = 1;
    while (b > 0) {
        if (b & 1) {
            ret = ret * a % mod;
        }
        a = a * a % mod;
        b >>= 1;
    }
    return ret;
}

long long C(int n, int m) {
    if (m < 0 || n < 0 || n < m) return 0;
    long long num = 1, denom = 1;
    for (int i = 1; i <= m; i++) {
        num = num * (n - i + 1) % mod;
        denom = denom * i % mod;
    }
    return num * qpow(denom, mod - 2) % mod;
}

void solve() {
    long long n, m;
    cin >> n >> m;

    long long cm2 = C(m, 2);
    long long cm3 = C(m, 3);
    long long ans1 = qpow(m + 1, n - 1);
    long long ans2 = cm2 * (qpow(4, n - 1) - qpow(3, n - 1) + mod) % mod;
    long long ans3 = cm3 * ((qpow(4, n - 1) - 3 * qpow(3, n - 1) + 3 * qpow(2, n - 1) - 1 + mod) % mod) % mod;
    long long ans4 = m * ((qpow(m + 1, n - 1) - (m - 1) * (qpow(3, n - 1) - qpow(2, n - 1) + mod) % mod - qpow(2, n - 1) + mod) % mod) % mod;

    long long ans = (ans1 + ans2 + ans3 + ans4) * qpow(2, m) % mod;
    cout << (ans + mod) % mod << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int T;
    cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}
