#include<bits/stdc++.h>
using namespace std;

const int mod = 998244353;
const int MAXN = 250010;

int n;
bool nsp[MAXN];
int fac[MAXN], inv[MAXN];
int f[MAXN];
vector<int> prm;

inline void Add(int &x, int y) {
    x += y;
    if(x >= mod) x -= mod;
}

int fpm(int x, int y) {
    int ans = 1;
    for(; y; y >>= 1, x = (long long)x * x % mod)
        if(y & 1) ans = (long long)ans * x % mod;
    return ans;
}

void work() {
    cin >> n;
    
    // Optimized sieve
    for(int i = 2; i * i <= n; i++) {
        if(!nsp[i]) {
            for(int j = i * i; j <= n; j += i) {
                nsp[j] = 1;
            }
        }
    }
    
    // Collect primes >= 3
    prm.reserve(n / 6); // Approximate prime count
    for(int i = 3; i <= n; i++) {
        if(!nsp[i]) {
            prm.push_back(i);
        }
    }
    
    // Precompute factorials and inverses
    fac[0] = fac[1] = inv[0] = inv[1] = 1;
    for(int i = 2; i <= n; i++) {
        fac[i] = (long long)fac[i-1] * i % mod;
        inv[i] = (long long)(mod - mod/i) * inv[mod%i] % mod;
    }
    for(int i = 2; i <= n; i++) {
        inv[i] = (long long)inv[i] * inv[i-1] % mod;
    }
    
    const int inv2 = fpm(2, mod-2);
    const long long n_mod = n;
    
    f[0] = 1;
    long long pow_n = 1;
    
    for(int i = 1; i <= n; i++) {
        pow_n = pow_n * n_mod % mod;
        f[i] = pow_n;
        
        long long coe = (long long)fac[i-1] * inv2 % mod * n_mod % mod;
        long long fi_minus_1_inv = (long long)f[i-1] * inv[i-1] % mod;
        
        for(int j : prm) {
            if(j > i) break;
            int idx = i - j;
            long long term = (long long)f[idx] * j % mod * coe % mod;
            Add(f[i], term);
        }
    }
    
    cout << (long long)f[n] * fpm(n, mod-3) % mod << '\n';
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    work();
}