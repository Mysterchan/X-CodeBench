#include <iostream>

using namespace std;

const int N = 1e6 + 10;
const int p = 998244353;

int fac[N], ifac[N];

int qpow (int base, int k) {
    int ret = 1;
    while (k) {
        if (k & 1) ret = ret * 1ll * base % p;
        base = base * 1ll * base % p;
        k >>= 1;
    }
    return ret;
}

int comb (int n, int m) {
    if (n < 0 || m < 0) return 0;
    return fac[n] * 1ll * ifac[m] % p * ifac[n - m] % p;
}

int comb2 (long long x) {
    return x * (x - 1) % p * ifac[2] % p;
}

int main (void) {

    int up = 1e6; fac[0] = 1;
    for (int i = 1; i <= up; i ++) fac[i] = fac[i - 1] * 1ll * i % p;
    ifac[up] = qpow (fac[up], p - 2); for (int i = up - 1; ~i; i --) ifac[i] = ifac[i + 1] * 1ll * (1 + i) % p;

    int t;scanf ("%d", &t);
    while (t --) {
        int n, m, k; scanf ("%d%d%d", &n, &m, &k);
        if (k < n + m - 2) puts ("0");
        else if (k == n + m - 2) printf ("%d\n", comb (n + m - 2, n - 1));
        else if (k == n + m - 1) printf ("%d\n", comb (n + m - 2, n - 1) * 1ll * 2 * (n - 1) % p * (m - 1) % p);
        else printf ("%d\n", ((comb (n + m - 2, n - 1) * 1ll * comb2 (2ll * (n - 1) * (m - 1) % p) - comb (n + m - 4, n - 2) * 1ll * (n + m - 3) % p) % p + comb (n + m - 2, n + 1) * 1ll * (n - 1) % p + comb (n + m - 2, m + 1) * 1ll * (m - 1) % p + p) % p );
    }

    return 0;
}