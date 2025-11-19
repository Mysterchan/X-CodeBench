#include<bits/stdc++.h>
using namespace std;
#define int long long

signed main(){
    ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);
    int n, K;
    cin >> n >> K;
    
    vector<int> a(n), b(n), c(n);
    for(int i = 0; i < n; i++) cin >> a[i];
    for(int i = 0; i < n; i++) cin >> b[i];
    for(int i = 0; i < n; i++) cin >> c[i];
    
    sort(a.begin(), a.end(), greater<int>());
    sort(b.begin(), b.end(), greater<int>());
    sort(c.begin(), c.end(), greater<int>());
    
    auto calc = [&](int i, int j, int k) -> int {
        return a[i]*b[j] + b[j]*c[k] + c[k]*a[i];
    };
    
    priority_queue<pair<int, tuple<int,int,int>>> pq;
    set<tuple<int,int,int>> visited;
    
    pq.push({calc(0,0,0), {0,0,0}});
    visited.insert({0,0,0});
    
    int count = 0;
    int answer = 0;
    
    while(!pq.empty() && count < K) {
        auto [val, idx] = pq.top();
        pq.pop();
        auto [i, j, k] = idx;
        
        count++;
        answer = val;
        
        if(count == K) break;
        
        // Generate next candidates
        vector<tuple<int,int,int>> next_states = {
            {i+1, j, k},
            {i, j+1, k},
            {i, j, k+1}
        };
        
        for(auto [ni, nj, nk] : next_states) {
            if(ni < n && nj < n && nk < n && visited.find({ni,nj,nk}) == visited.end()) {
                visited.insert({ni,nj,nk});
                pq.push({calc(ni,nj,nk), {ni,nj,nk}});
            }
        }
    }
    
    cout << answer << endl;
    return 0;
}