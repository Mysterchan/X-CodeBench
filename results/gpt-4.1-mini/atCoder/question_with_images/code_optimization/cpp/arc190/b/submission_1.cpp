#include <bits/stdc++.h>
using namespace std;
#define int long long
const int mod = 998244353;

inline int read() {
    int a = 0, f = 1;
    char c = getchar();
    while (c < '0' || c > '9') {
        if (c == '-') f = -1;
        c = getchar();
    }
    while (c >= '0' && c <= '9') {
        a = a * 10 + c - '0';
        c = getchar();
    }
    return a * f;
}

int ksm(int a, int b) {
    int s = 1;
    while (b > 0) {
        if (b & 1) s = s * a % mod;
        a = a * a % mod;
        b >>= 1;
    }
    return s;
}

int n, a, b, q;
int *jc;

inline int C(int x, int y) {
    if (x < 0 || y < 0 || y > x) return 0;
    return jc[x] * ksm(jc[y], mod - 2) % mod * ksm(jc[x - y], mod - 2) % mod;
}

int32_t main() {
    n = read(); a = read(); b = read(); q = read();

    // Allocate factorial array dynamically to avoid stack overflow
    jc = new int[n + 1];
    jc[0] = 1;
    for (int i = 1; i <= n; i++) {
        jc[i] = jc[i - 1] * i % mod;
    }

    // Precompute f and g arrays with O(n) complexity
    // f[i][0], f[i][1], g[i][0], g[i][1] are stored in two arrays each
    // To save memory, we only keep current and previous values
    // But since queries are random access, we must store all values

    // Use vectors to avoid large stack allocation
    vector<int> f0(n + 1, 0), f1(n + 1, 0);
    vector<int> g0(n + 1, 0), g1(n + 1, 0);

    f0[0] = 1;
    g0[0] = 1;

    for (int i = 1; i <= n; i++) {
        int val = 0;
        if (i >= a) val = (val + C(i - 1, a - 1)) % mod;
        if (i >= n - a + 1 && i != n) val = (val + C(i - 1, n - a)) % mod;
        f1[i] = val;
        if (i != n) f0[i] = (f0[i - 1] * 2 % mod - f1[i] + mod) % mod;
    }

    for (int i = 1; i <= n; i++) {
        int val = 0;
        if (i >= b) val = (val + C(i - 1, b - 1)) % mod;
        if (i >= n - b + 1 && i != n) val = (val + C(i - 1, n - b)) % mod;
        g1[i] = val;
        if (i != n) g0[i] = (g0[i - 1] * 2 % mod - g1[i] + mod) % mod;
    }

    // Precompute powers of 4 to avoid repeated exponentiation
    // max ls = n, but Q <= 200000, so we can compute on the fly or cache
    // We'll compute on the fly using ksm

    while (q--) {
        int ls = read();
        int k = n - ls + 1;

        // Calculate the answer using the formula:
        // (f0[k]*g1[k] + f1[k]*g0[k] + f1[k]*g1[k]) * 4^(ls-2) mod
        // Handle ls=1 separately to avoid negative exponent
        int pow4 = (ls <= 1) ? 1 : ksm(4, ls - 2);

        int res = (f0[k] * g1[k]) % mod;
        res = (res + f1[k] * g0[k]) % mod;
        res = (res + f1[k] * g1[k]) % mod;
        res = (res * pow4) % mod;

        printf("%lld\n", res);
    }

    delete[] jc;
    return 0;
}