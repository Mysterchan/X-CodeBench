#include<bits/stdc++.h>
using namespace std;
#define int long long
const int MOD = 998244353;

inline int modinv(int a, int mod) {
    int x = 1, y = 0, m0 = mod, q, temp;
    while (a > 1) {
        q = a / mod;
        temp = mod;
        mod = a % mod, a = temp;
        temp = y;
        y = x - q * y, x = temp;
    }
    return (x + m0) % m0;
}

int factorials[10000005];

void precompute_factorials(int n) {
    factorials[0] = 1;
    for (int i = 1; i <= n; i++)
        factorials[i] = factorials[i - 1] * i % MOD;
}

int binomial_coeff(int n, int k) {
    if (n < k || k < 0) return 0;
    return factorials[n] * modinv(factorials[k], MOD) % MOD * modinv(factorials[n - k], MOD) % MOD;
}

int calculate_count(int n, int a, int b, int k) {
    int valid_positions_a = 0, valid_positions_b = 0;

    if (k >= a) valid_positions_a += binomial_coeff(k - 1, a - 1);
    if (k >= n - a + 1 && k != n) valid_positions_a += binomial_coeff(k - 1, n - a);
    valid_positions_a %= MOD;

    if (k >= b) valid_positions_b += binomial_coeff(k - 1, b - 1);
    if (k >= n - b + 1 && k != n) valid_positions_b += binomial_coeff(k - 1, n - b);
    valid_positions_b %= MOD;

    return (valid_positions_a * valid_positions_b) % MOD;
}

void solve() {
    int n, a, b, q;
    cin >> n >> a >> b >> q;

    precompute_factorials(n);
    
    // Listening to the queries
    while (q--) {
        int k_query;
        cin >> k_query;
        int k = n - k_query + 1;
        int count = calculate_count(n, a, b, k);
        
        // The result needs to be multiplied by an additional factor of 4^(k_query - 2)
        if (k_query > 2) {
            count = (count * mod_exp(4, k_query - 2)) % MOD;
        }
        
        cout << count << "\n";
    }
}

int mod_exp(int base, int exp) {
    int result = 1;
    while (exp) {
        if (exp % 2) result = result * base % MOD;
        base = base * base % MOD;
        exp /= 2;
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}