#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int MAXN = 200000;
const ll MOD = 998244353;

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
    vector<int> A(N);
    int maxA = 0;
    for(int i = 0; i < N; i++){
        cin >> A[i];
        if (A[i] > maxA) maxA = A[i];
    }
    // compute mu[1..maxA] by linear sieve
    vector<int> mu(maxA+1, 0), primes;
    vector<bool> is_comp(maxA+1, false);
    mu[1] = 1;
    for(int i = 2; i <= maxA; i++){
        if (!is_comp[i]) {
            primes.push_back(i);
            mu[i] = -1;
        }
        for(int p: primes){
            ll v = (ll)i * p;
            if (v > maxA) break;
            is_comp[v] = true;
            if (i % p == 0) {
                mu[v] = 0;
                break;
            } else {
                mu[v] = -mu[i];
            }
        }
    }
    // pow10
    vector<ll> pow10(maxA+1);
    pow10[0] = 1;
    for(int i = 1; i <= maxA; i++){
        pow10[i] = (pow10[i-1] * 10) % MOD;
    }
    // inv of (10^e -1)
    vector<ll> invDen(maxA+1);
    for(int i = 1; i <= maxA; i++){
        ll v = (pow10[i] - 1 + MOD) % MOD;
        invDen[i] = modexp(v, MOD-2);
    }
    // divisors
    vector<vector<int>> divs(maxA+1);
    for(int d = 1; d <= maxA; d++){
        for(int j = d; j <= maxA; j += d){
            divs[j].push_back(d);
        }
    }
    // compute Phi_d(10) mod M for d=1..maxA
    vector<ll> phi(maxA+1, 0);
    for(int d = 1; d <= maxA; d++){
        ll v = 1;
        for(int e: divs[d]){
            int k = d / e;
            if (mu[k] == 1) {
                ll t = (pow10[e] - 1 + MOD) % MOD;
                v = (v * t) % MOD;
            } else if (mu[k] == -1) {
                v = (v * invDen[e]) % MOD;
            }
        }
        phi[d] = v;
    }
    // main loop
    vector<char> seen(maxA+1, 0);
    ll ansPhi = 1;
    ll inv9 = modexp(9, MOD-2);
    for(int i = 0; i < N; i++){
        int x = A[i];
        for(int d: divs[x]){
            if (!seen[d]){
                seen[d] = 1;
                ansPhi = (ansPhi * phi[d]) % MOD;
            }
        }
        ll ans = (ansPhi * inv9) % MOD;
        cout << ans << "\n";
    }
    return 0;
}