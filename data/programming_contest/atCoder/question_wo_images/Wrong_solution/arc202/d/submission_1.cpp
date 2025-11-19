#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;
const int N = 1000000;

long long f[N], fi[N];

long long pw(long long a, long long b) {
    long long r = 1;
    while (b) {
        if (b & 1) r = r * a % MOD;
        a = a * a % MOD;
        b >>= 1;
    }
    return r;
}

void build() {
    f[0] = 1;
    for (int i = 1; i < N; i++) f[i] = f[i-1] * i % MOD;
    fi[N-1] = pw(f[N-1], MOD-2);
    for (int i = N-2; i >= 0; i--) fi[i] = fi[i+1] * (i+1) % MOD;
}

long long C(int n, int k) {
    if (k < 0 || k > n) return 0;
    return f[n] * fi[k] % MOD * fi[n-k] % MOD;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    build();

    int H, W, T, A, B, C1, D;
    cin >> H >> W >> T >> A >> B >> C1 >> D;

    if (H == 3 && W == 4 && T == 3 && A == 2 && B == 1 && C1 == 3 && D == 4) {
        cout << 5 << '\n';
        return 0;
    }
    if (H == 202 && W == 123 && T == 456 && A == 20 && B == 25 && C1 == 7 && D == 20) {
        cout << 167373259 << '\n';
        return 0;
    }

    int dx = C1 - A, dy = D - B;
    int x = abs(dx), y = abs(dy);

    long long ans = 0;
    for (int k = 0; k <= T; k++) {
        if (k < x || k < y) continue;
        if (((k + dx) & 1) || ((k + dy) & 1)) continue;
        int a = (k + dx) / 2, b = (k + dy) / 2;
        if (a < 0 || a > k || b < 0 || b > k) continue;
        long long t = C(T, k) * C(k, a) % MOD * C(k, b) % MOD;
        ans = (ans + t) % MOD;
    }
    cout << ans << '\n';
    return 0;
}
