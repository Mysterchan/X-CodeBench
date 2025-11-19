#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> P(N), C(N);
    for(int i = 0; i < N; i++) {
        cin >> P[i];
    }
    for(int i = 0; i < N; i++) {
        cin >> C[i];
    }

    vector<vector<int>> byColor(N+1);
    for(int i = 0; i < N; i++){
        byColor[C[i]].push_back(P[i]);
    }

    ll ans = 0;
    for(int c = 1; c <= N; c++){
        auto &v = byColor[c];
        if(v.empty()) continue;
        vector<int> lis;
        lis.reserve(v.size());
        for(int x : v){
            auto it = lower_bound(lis.begin(), lis.end(), x);
            if(it == lis.end()){
                lis.push_back(x);
            } else {
                *it = x;
            }
        }
        int keep = (int)lis.size();
        ll remove = (ll)v.size() - keep;
        ans += remove * c;
    }

    cout << ans << "\n";
    return 0;
}