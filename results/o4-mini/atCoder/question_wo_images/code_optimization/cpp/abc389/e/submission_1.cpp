#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    ll N;
    ll M;
    cin >> N >> M;
    vector<ll> P(N);
    for(ll i = 0; i < N; i++){
        cin >> P[i];
    }
    // Function to compute total cost of taking all marginal costs <= T
    auto calcC = [&](ll T)->__int128 {
        __int128 sum = 0;
        for(ll i = 0; i < N; i++){
            ll p = P[i];
            if (p > T) continue;
            // q = floor(T / p)
            ll q = T / p;
            // number of units k = floor((q + 1) / 2)
            ll k = (q + 1) >> 1;
            if(k <= 0) continue;
            // add cost = p * k^2, but cap if exceeds M
            __int128 cost = (__int128)p * k * k;
            sum += cost;
            if(sum > M) return sum;
        }
        return sum;
    };

    // Binary search on marginal cost threshold T
    ll l = 0;
    ll r = 2 * M + 1; // r guaranteed so that calcC(r) > M
    while(r - l > 1){
        ll mid = l + ((r - l) >> 1);
        if(calcC(mid) <= M){
            l = mid;
        } else {
            r = mid;
        }
    }
    ll T1 = r; // first T where cost > M

    // Compute K1 and C1 for all marginals < T1
    __int128 C1 = 0;
    ll K1 = 0;
    for(ll i = 0; i < N; i++){
        ll p = P[i];
        if(p > T1 - 1) continue;
        ll q = (T1 - 1) / p;
        ll k = (q + 1) >> 1;
        if(k <= 0) continue;
        K1 += k;
        C1 += (__int128)p * k * k;
        // C1 should not exceed M here by construction
    }
    ll budget = M - (ll)C1;
    // Count how many marginals exactly equal to T1
    ll cnt_eq = 0;
    for(ll i = 0; i < N; i++){
        ll p = P[i];
        if(p == 0) continue;
        if(T1 % p != 0) continue;
        ll t = T1 / p;
        // marginal = (2*j-1)*p == T1 => t = 2*j-1 => t odd
        if((t & 1LL) == 1){
            // j = (t+1)/2 >=1 always
            cnt_eq++;
        }
    }
    ll add = 0;
    if(budget > 0 && T1 > 0){
        add = budget / T1;
        if(add > cnt_eq) add = cnt_eq;
    }
    ll ans = K1 + add;
    cout << ans << "\n";
    return 0;
}