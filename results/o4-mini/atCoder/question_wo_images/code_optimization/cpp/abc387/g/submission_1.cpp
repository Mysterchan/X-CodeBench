#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int MOD = 998244353;

ll modexp(ll a, ll e) {
    ll r = 1 % MOD;
    a %= MOD;
    while (e) {
        if (e & 1) r = (r * a) % MOD;
        a = (a * a) % MOD;
        e >>= 1;
    }
    return r;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    if (N == 1) {
        cout << 1 << "\n";
        return 0;
    }
    // Sieve primes up to N
    vector<bool> is_composite(N+1, false);
    vector<int> primes;
    for (int i = 2; i <= N; ++i) {
        if (!is_composite[i]) {
            primes.push_back(i);
            if ((ll)i * i <= N) {
                for (int j = i * i; j <= N; j += i) {
                    is_composite[j] = true;
                }
            }
        }
    }
    // Precompute factorials and inverse factorials
    vector<ll> fac(N+1), invfac(N+1);
    fac[0] = 1;
    for (int i = 1; i <= N; ++i) {
        fac[i] = fac[i-1] * i % MOD;
    }
    invfac[N] = modexp(fac[N], MOD-2);
    for (int i = N; i >= 1; --i) {
        invfac[i-1] = invfac[i] * i % MOD;
    }
    // Precompute powers N^i for i=0..N
    vector<ll> powN(N+1);
    powN[0] = 1;
    for (int i = 1; i <= N; ++i) {
        powN[i] = powN[i-1] * (ll)N % MOD;
    }
    ll inv2 = (MOD + 1) / 2;
    ll invN = modexp(N, MOD-2);

    // Count trees: N^(N-2)
    ll ans = powN[N-2];
    // Add unicyclic with one cycle of prime length p>=3
    for (int p : primes) {
        if (p < 3) continue;
        if (p < N) {
            int rem = N - p;
            // A_p = fac[N]/(2*(N-p)!)*N^(N-p-1)
            ll term = fac[N] * invfac[rem] % MOD;
            term = term * inv2 % MOD;
            term = term * powN[rem-1] % MOD;
            ans = (ans + term) % MOD;
        } else if (p == N) {
            // special case p == N: cycle on all vertices
            // A_N = fac[N]/2 * invN
            ll term = fac[N] * inv2 % MOD;
            term = term * invN % MOD;
            ans = (ans + term) % MOD;
        }
    }
    cout << ans << "\n";
    return 0;
}