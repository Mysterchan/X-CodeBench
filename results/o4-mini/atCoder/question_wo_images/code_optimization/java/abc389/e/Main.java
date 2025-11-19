#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    ll M;
    cin >> N >> M;
    vector<ll> P(N);
    ll minP = LLONG_MAX;
    for(int i = 0; i < N; i++){
        cin >> P[i];
        if(P[i] < minP) minP = P[i];
    }

    ll l = 0, r = 4000000000000000000LL;
    auto can = [&](ll T)->bool{
        __int128 cost = 0;
        for(int i = 0; i < N; i++){
            if (T < P[i]) continue;
            ll k = (T / P[i] + 1) / 2;
            // cost += P[i] * k * k
            __int128 t = (__int128)P[i] * k * k;
            cost += t;
            if(cost > M) return false;
        }
        return cost <= M;
    };

    while(l < r){
        ll mid = (l + r + 1) >> 1;
        if(can(mid)) l = mid;
        else r = mid - 1;
    }

    // compute base units and cost
    __int128 used = 0;
    ll totalUnits = 0;
    vector<unsigned long long> nextCost;
    nextCost.reserve(N);
    for(int i = 0; i < N; i++){
        ll k = 0;
        if(l >= P[i]) k = (l / P[i] + 1) / 2;
        totalUnits += k;
        used += (__int128)P[i] * k * k;
        // next marginal cost
        unsigned long long c = (unsigned long long)(2ULL * k + 1ULL) * (unsigned long long)P[i];
        nextCost.push_back(c);
    }
    ll rem = M - (ll)used;

    sort(nextCost.begin(), nextCost.end());
    for(auto c : nextCost){
        if(rem >= (ll)c){
            rem -= (ll)c;
            totalUnits++;
        } else break;
    }

    cout << totalUnits << "\n";
    return 0;
}