#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, X;
    cin >> N >> X;
    vector<pair<int,int>> items[4];
    for(int i = 0; i < N; i++){
        int V, A, C;
        cin >> V >> A >> C;
        items[V].emplace_back(A, C);
    }

    // dp[v][cal] = max vitamin units of type v with exactly cal calories (then take prefix max)
    vector<vector<ll>> dp(4, vector<ll>(X+1, LLONG_MIN));
    for(int v = 1; v <= 3; v++){
        dp[v][0] = 0;
        for(auto &it : items[v]){
            int a = it.first;
            int c = it.second;
            for(int cal = X; cal >= c; cal--){
                if(dp[v][cal - c] != LLONG_MIN){
                    dp[v][cal] = max(dp[v][cal], dp[v][cal - c] + a);
                }
            }
        }
        // prefix max so dp[v] is non-decreasing in cal
        for(int cal = 1; cal <= X; cal++){
            dp[v][cal] = max(dp[v][cal], dp[v][cal - 1]);
        }
    }

    // maximum possible k is limited by the minimal of dp[v][X]
    ll max1 = dp[1][X], max2 = dp[2][X], max3 = dp[3][X];
    ll high = min({max1, max2, max3}) + 1;
    ll low = 0; // feasible
    // binary search largest k such that sum minimal calories to achieve k <= X
    while(low + 1 < high){
        ll mid = (low + high) / 2;
        // find minimal cal_1 such that dp[1][cal_1] >= mid
        bool ok = true;
        ll sumc = 0;
        for(int v = 1; v <= 3; v++){
            auto it = lower_bound(dp[v].begin(), dp[v].end(), mid);
            if(it == dp[v].end()){
                ok = false;
                break;
            }
            sumc += (it - dp[v].begin());
            if(sumc > X){
                ok = false;
                break;
            }
        }
        if(ok) low = mid;
        else    high = mid;
    }

    cout << low << "\n";
    return 0;
}