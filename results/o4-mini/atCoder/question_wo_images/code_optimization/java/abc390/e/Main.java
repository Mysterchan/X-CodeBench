#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, X;
    cin >> N >> X;
    vector<pair<int,int>> items[3];
    for(int i = 0; i < N; i++){
        int v, a, c;
        cin >> v >> a >> c;
        items[v-1].emplace_back(a, c);
    }

    const int NEG_INF = -1000000000;
    static int dp[3][5001];
    for(int g = 0; g < 3; g++){
        for(int j = 0; j <= X; j++) dp[g][j] = NEG_INF;
        dp[g][0] = 0;
        for(auto &it: items[g]){
            int a = it.first, c = it.second;
            for(int j = X; j >= c; j--){
                dp[g][j] = max(dp[g][j], dp[g][j-c] + a);
            }
        }
    }

    int high = INT_MAX;
    for(int g = 0; g < 3; g++){
        long long sumA = 0;
        for(auto &it: items[g]) sumA += it.first;
        high = min(high, (int)sumA);
    }
    if(high < 0) high = 0;

    int low = 0;
    while(low < high){
        int mid = low + (high - low + 1) / 2;
        long long totalCal = 0;
        bool ok = true;
        for(int g = 0; g < 3; g++){
            int minCal = X + 1;
            for(int j = 0; j <= X; j++){
                if(dp[g][j] >= mid){
                    minCal = j;
                    break;
                }
            }
            if(minCal > X){
                ok = false;
                break;
            }
            totalCal += minCal;
            if(totalCal > X){
                ok = false;
                break;
            }
        }
        if(ok) low = mid;
        else high = mid - 1;
    }

    cout << low << "\n";
    return 0;
}