#include <bits/stdc++.h>

#define MOD 998244353

using namespace std;

typedef long long ll;

ll factorial[300001], inv_factorial[300001];

ll mod_inverse(ll a, ll mod) {
    ll m0 = mod, y = 0, x = 1;
    if (mod == 1) return 0;
    while (a > 1) {
        ll q = a / mod, t = mod;
        mod = a % mod, a = t, t = y;
        y = x - q * y, x = t;
    }
    return (x + m0) % m0;
}

void precompute_factorials(int n) {
    factorial[0] = 1;
    for (int i = 1; i <= n; ++i)
        factorial[i] = factorial[i - 1] * i % MOD;

    inv_factorial[n] = mod_inverse(factorial[n], MOD);
    for (int i = n - 1; i >= 0; --i)
        inv_factorial[i] = inv_factorial[i + 1] * (i + 1) % MOD;
}

ll binomial(ll n, ll k) {
    if (k > n || k < 0) return 0;
    return factorial[n] * inv_factorial[k] % MOD * inv_factorial[n - k] % MOD;
}

ll count_paths(int H, int W, int T, int A, int B, int C, int D) {
    int delta_x = abs(C - A);
    int delta_y = abs(D - B);
    if ((delta_x + delta_y) > T || (T - delta_x - delta_y) % 2 != 0) return 0;

    int free_steps = (T - delta_x - delta_y) / 2;
    return binomial(free_steps + free_steps + delta_x + delta_y, free_steps + delta_x);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H, W, T, A, B, C, D;
    cin >> H >> W >> T >> A >> B >> C >> D;

    precompute_factorials(T);
    cout << count_paths(H, W, T, A, B, C, D) << "\n";
    return 0;
}
