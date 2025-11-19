#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, X;
    cin >> N >> X;
    vector<pair<int,int>> items1, items2, items3;
    for(int i = 0; i < N; i++){
        int V, C; ll A;
        cin >> V >> A >> C;
        if(V == 1) items1.emplace_back(C, (int)A);
        else if(V == 2) items2.emplace_back(C, (int)A);
        else items3.emplace_back(C, (int)A);
    }

    auto solve_dp = [&](const vector<pair<int,int>>& items){
        vector<int> dp(X+1, 0);
        for(auto &it: items){
            int cost = it.first;
            int val = it.second;
            for(int c = X; c >= cost; c--){
                int nv = dp[c-cost] + val;
                if(nv > dp[c]) dp[c] = nv;
            }
        }
        return dp;
    };

    vector<int> dp1 = solve_dp(items1);
    vector<int> dp2 = solve_dp(items2);
    vector<int> dp3 = solve_dp(items3);

    int max1 = dp1[X], max2 = dp2[X], max3 = dp3[X];
    int hi = min({max1, max2, max3});
    int lo = 0, ans = 0;

    auto can = [&](int t){
        ll sumc = 0;
        // for each dp array find minimal c s.t. dp[c] >= t
        auto f = [&](const vector<int>& dp)->int{
            auto it = lower_bound(dp.begin(), dp.end(), t);
            if(it == dp.end()) return X+1;
            return int(it - dp.begin());
        };
        int c1 = f(dp1);
        if(c1 > X) return false;
        sumc += c1;
        if(sumc > X) return false;
        int c2 = f(dp2);
        if(c2 > X) return false;
        sumc += c2;
        if(sumc > X) return false;
        int c3 = f(dp3);
        if(c3 > X) return false;
        sumc += c3;
        return sumc <= X;
    };

    while(lo <= hi){
        int mid = lo + (hi - lo) / 2;
        if(can(mid)){
            ans = mid;
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}