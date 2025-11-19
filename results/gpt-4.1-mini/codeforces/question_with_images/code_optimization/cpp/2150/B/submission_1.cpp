#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int MAXN = 200000 + 5, MOD = 998244353;

ll modpow(ll a, int b) {
    ll r = 1;
    while (b) {
        if (b & 1) r = r * a % MOD;
        a = a * a % MOD;
        b >>= 1;
    }
    return r;
}

int n, a[MAXN], b[MAXN];
ll invFac[MAXN], fac[MAXN];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    fac[0] = 1;
    for (int i = 1; i < MAXN; i++) fac[i] = fac[i - 1] * i % MOD;
    invFac[MAXN - 1] = modpow(fac[MAXN - 1], MOD - 2);
    for (int i = MAXN - 2; i >= 0; i--) invFac[i] = invFac[i + 1] * (i + 1) % MOD;

    int T; cin >> T;
    while (T--) {
        cin >> n;
        for (int i = 1; i <= n; i++) cin >> a[i];
        fill(b + 1, b + n + 1, 0);

        // Count how many times each min(i, n+1 - i) appears
        for (int i = 1; i <= n; i++) {
            b[min(i, n + 1 - i)]++;
        }

        ll ans = 1;
        int c = 0;
        // Process from largest to smallest k
        for (int i = n; i >= 1; i--) {
            c += b[i];
            // Multiply by inverse factorial of a[i]
            ans = ans * invFac[a[i]] % MOD;
            // Multiply by permutations: P(c, a[i]) = c! / (c - a[i])!
            if (a[i] > c) {
                ans = 0;
                break;
            }
            for (int j = 0; j < a[i]; j++) {
                ans = ans * (c - j) % MOD;
            }
            c -= a[i];
        }

        cout << (c == 0 ? ans : 0) << '\n';
    }

    return 0;
}