#include <vector>
#include <iostream>

#define ll long long

using namespace std;

const int N = 2e5 + 10;
const ll p = 998244353;

int mn[N];
ll f[N], invf[N], g[N];
bool used[N];
vector <int> prime;

ll qpow (ll base, int k) {
    ll ret = 1;
    while (k) {
        if (k & 1) ret = ret * base % p;
        base = base * base % p;
        k >>= 1;
    }
    return ret;
}

ll inv (ll a) {
    return qpow (a, p - 2);
}

void prework () {
    for (int i = 1; i <= 2e5; i ++) g[i] = (g[i - 1] * 10 + 1) % p, invf[i] = inv (g[i]);
    for (int i = 2; i <= 2e5; i ++) {
        if (!mn[i]) {
            for (int j = 2; j * i <= 2e5; j ++) mn[j * i] = true;
            for (int j = 2e5 / i; j; j --) g[j * i] = g[j * i] * invf[j] % p, invf[j * i] = invf[j * i] * g[j] % p;
        }
    }
}

int main (void) {

    prework ();
    int t; scanf ("%d", &t);
    ll ans = 1;
    while (t --) {
        int u; scanf ("%d", &u);
        if (!used[u])
        for (int i = 1; i * i <= u; i ++) {
            if (u % i) continue;
            if (!used[i]) used[i] = true, ans = ans * g[i] % p;
            if (!used[u / i]) used[u / i] = true, ans = ans * g[u / i] % p;
        }
        printf ("%lld\n", ans);
    }

    return 0;
}