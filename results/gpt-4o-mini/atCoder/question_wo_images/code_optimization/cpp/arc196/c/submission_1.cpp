#include <bits/stdc++.h>
using namespace std;
#define MOD 998244353

int main() {
    ios::sync_with_stdio(0), cin.tie(0);

    int n;
    string S;
    cin >> n >> S;

    if (S[0] == 'W' || S[2 * n - 1] == 'B') {
        cout << "0\n";
        return 0;
    }

    int whiteCount = 0, blackCount = 0;
    vector<int> pre(n + 1, 0);
    
    for (int i = 0; i < 2 * n; i++) {
        if (S[i] == 'W') {
            whiteCount++;
        } else {
            blackCount++;
        }
        if (S[i] == 'W') {
            pre[whiteCount] = blackCount;
        }
    }

    vector<long long> fact(n + 1, 1), invFact(n + 1, 1);
    
    for (int i = 2; i <= n; i++) {
        fact[i] = fact[i - 1] * i % MOD;
    }
    invFact[n] = modInverse(fact[n]);
    for (int i = n - 1; i >= 1; i--) {
        invFact[i] = invFact[i + 1] * (i + 1) % MOD;
    }

    auto comb = [&](int x, int y) {
        if (x > y || x < 0) return 0LL;
        return fact[y] * invFact[x] % MOD * invFact[y - x] % MOD;
    };

    vector<long long> f(n + 1, 0);
    
    for (int i = 1; i <= n; i++) {
        if (pre[i] <= i) {
            f[i] = comb(pre[i], i);
        }
    }

    vector<long long> sum(n + 1, 0);
    
    function<void(int, int)> solve = [&](int l, int r) {
        if (l == r) return;

        int mid = (l + r) / 2;
        solve(l, mid);
        for (int i = l; i <= mid; i++) {
            sum[pre[i]] = (sum[pre[i]] + f[i]) % MOD;
        }

        if (pre[l] <= r) {
            vector<long long> res(r - pre[l] + 2, 0);
            for (int i = pre[l]; i <= r; i++) res[i - pre[l]] = comb(0, i - pre[l]);
            for (int i = mid + 1; i <= r; i++) {
                if (i >= pre[i]) {
                    f[i] = (f[i] - res[i - pre[l]] * invFact[i - pre[i]] % MOD + MOD) % MOD;
                }
            }
        }

        for (int i = pre[l]; i <= pre[mid]; i++) {
            sum[i] = 0;
        }
        solve(mid + 1, r);
    };

    solve(1, n);
  
    cout << f[n] << '\n';
}

long long modInverse(long long a) {
    long long m = MOD, m0 = m, y = 0, x = 1;
    if (m == 1) return 0;
    while (a > 1) {
        long long q = a / m;
        long long t = m;
        m = a % m, a = t, t = y;
        y = x - q * y, x = t;
    }
    if (x < 0) x += m0;
    return x;
}
