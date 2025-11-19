#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll MOD = 998244353;

// fast exponentiation mod
ll modexp(ll a, ll e) {
    ll r = 1;
    a %= MOD;
    while (e > 0) {
        if (e & 1) r = (r * a) % MOD;
        a = (a * a) % MOD;
        e >>= 1;
    }
    return r;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H, W;
    cin >> H >> W;
    // If either dimension is even, no tour is possible
    if ((H % 2 == 0) || (W % 2 == 0)) {
        cout << 0 << "\n";
        return 0;
    }

    // Precompute factorials and inverse factorials up to H
    vector<ll> fac(H+1), invf(H+1);
    fac[0] = 1;
    for(int i = 1; i <= H; i++){
        fac[i] = fac[i-1] * i % MOD;
    }
    invf[H] = modexp(fac[H], MOD - 2);
    for(int i = H; i > 0; i--){
        invf[i-1] = invf[i] * i % MOD;
    }

    auto comb = [&](int n, int k)->ll {
        if (k < 0 || k > n) return 0;
        return fac[n] * (invf[k] * invf[n-k] % MOD) % MOD;
    };

    ll ans = 0;
    // Sum over odd i: gcd(i, W) == 1, add C(H, (i+H)/2)
    for(int i = 1; i <= H; i += 2) {
        if (std::gcd(i, W) == 1) {
            int r = (i + H) / 2;
            ans = (ans + comb(H, r)) % MOD;
        }
    }
    // Multiply by 2 as per problem statement
    ans = ans * 2 % MOD;

    cout << ans << "\n";
    return 0;
}