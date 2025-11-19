#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> P(N), C(N);
    for(int i = 0; i < N; i++) cin >> P[i];
    for(int i = 0; i < N; i++) cin >> C[i];

    vector<vector<int>> groups(N + 1);
    for(int i = 0; i < N; i++){
        groups[C[i]].push_back(P[i]);
    }

    long long totalCost = 0;
    for(int color = 1; color <= N; color++){
        auto &seq = groups[color];
        int sz = seq.size();
        if(sz <= 1) continue;
        vector<int> lis;
        lis.reserve(sz);
        for(int x : seq){
            auto it = lower_bound(lis.begin(), lis.end(), x);
            if(it == lis.end()) lis.push_back(x);
            else *it = x;
        }
        totalCost += 1LL * (sz - (int)lis.size()) * color;
    }

    cout << totalCost << "\n";
    return 0;
}