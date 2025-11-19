#include <bits/stdc++.h>
using namespace std;
#define int long long
const int mod = 998244353;

int n, fac[250010], inv[250010], f[250010];
vector<int> primes;
bool is_prime[250010];

int mod_inv(int x) {
    int res = 1, exp = mod - 2;
    while (exp > 0) {
        if (exp % 2 == 1) res = res * x % mod;
        x = x * x % mod;
        exp /= 2;
    }
    return res;
}

void preprocess() {
    is_prime[0] = is_prime[1] = true;
    for (int i = 2; i <= n; i++) {
        if (!is_prime[i]) {
            for (int j = i * 2; j <= n; j += i) {
                is_prime[j] = true;
            }
            if (i >= 3) primes.push_back(i);
        }
    }

    fac[0] = fac[1] = 1;
    for (int i = 2; i <= n; i++) {
        fac[i] = fac[i - 1] * i % mod;
    }

    inv[n] = mod_inv(fac[n]);
    for (int i = n - 1; i >= 0; i--) {
        inv[i] = inv[i + 1] * (i + 1) % mod;
    }
}

int count_graphs() {
    const int inv2 = mod_inv(2);
    f[0] = 1;
    
    for (int i = 1; i <= n; i++) {
        f[i] = f[i - 1] * n % mod;
        f[i - 1] = f[i - 1] * inv[i - 1] % mod;
        
        int coefficient = fac[i - 1] * inv2 % mod * n % mod;

        for (int j : primes) {
            if (j > i) break;
            f[i] = (f[i] + f[i - j] * j % mod * coefficient) % mod;
        }
    }

    return f[n] * mod_inv(n) % mod;
}

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> n;
    preprocess();
    cout << count_graphs() << '\n';
}