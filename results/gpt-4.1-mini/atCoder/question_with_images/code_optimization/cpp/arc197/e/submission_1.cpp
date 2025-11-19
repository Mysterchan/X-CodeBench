#include <bits/stdc++.h>
#define int long long
using namespace std;
const int MOD = 998244353;

int add(int x,int y) {
    x += y;
    if (x >= MOD) x -= MOD;
    return x;
}

int mult(int x,int y) {
    return (x * y) % MOD;
}

// Sum of first x natural numbers modulo MOD
int s(int x) {
    if (x <= 0) return 0;
    if (x % 2 == 0) return mult(x / 2, x + 1);
    else return mult(x, (x + 1) / 2);
}

int sum_j_s(int n) {
    // sum_{j=1}^n j * s(n+1 - j)
    // = sum_{j=1}^n j * ((n+1 - j)*(n+2 - j)/2)
    // = (1/2) * sum_{j=1}^n j * (n+1 - j) * (n+2 - j)
    // We derive a closed form:
    // sum_j j*(n+1-j)*(n+2-j) = n(n+1)(n+2)(n+3)/12
    // So sum_j j*s(n+1-j) = (1/2) * n(n+1)(n+2)(n+3)/12 = n(n+1)(n+2)(n+3)/24

    if (n <= 0) return 0;
    int a = n % MOD;
    int b = (n + 1) % MOD;
    int c = (n + 2) % MOD;
    int d = (n + 3) % MOD;

    // Compute numerator = a*b*c*d mod MOD
    int64_t numerator = (int64_t)a * b % MOD;
    numerator = numerator * c % MOD;
    numerator = numerator * d % MOD;

    // Modular inverse of 24 mod MOD
    // 24 = 2^3 * 3
    // inv(24) = pow(24, MOD-2, MOD)
    static int inv24 = 0;
    if (inv24 == 0) {
        int base = 24, exp = MOD - 2, res = 1;
        while (exp) {
            if (exp & 1) res = (int)((int64_t)res * base % MOD);
            base = (int)((int64_t)base * base % MOD);
            exp >>= 1;
        }
        inv24 = res;
    }

    return (int)((numerator * inv24) % MOD);
}

void solve() {
    int n, h, w;
    cin >> n >> h >> w;
    if (h < 2 * n || w < 2 * n) {
        cout << 0 << '\n';
        return;
    }
    int H = h - 2 * n + 1;
    int W = w - 2 * n + 1;

    int sH = s(H);
    int sW = s(W);

    int todos = mult(mult(sW, sW), mult(sH, sH));

    int minush = sum_j_s(H - 1);
    int minusw = sum_j_s(W - 1);

    int sub = mult(2, mult(minush, minusw));
    todos = add(todos, MOD - sub);

    cout << todos << '\n';
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    while (t--) solve();
}