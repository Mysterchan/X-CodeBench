#include<bits/stdc++.h>
using namespace std;

#define ll long long

vector<int> graf[21];
bitset<20> vis;

void build_graf(int n, int m){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            int v = i * m + j;
            if(i) graf[v].push_back(v - m);
            if(j) graf[v].push_back(v - 1);
            if(i + 1 < n) graf[v].push_back(v + m);
            if(j + 1 < m) graf[v].push_back(v + 1);
        }
    }
}

int dfs(int v, int mask){
    int ile = 1;
    vis[v] = 1;

    for(int u : graf[v]){
        if(!vis[u] && ((1 << u) & mask)) ile += dfs(u, mask);
    }

    return ile;
}

ll count_ans(int mask, vector<vector<ll>> &grid){
    int n = grid.size(), m = grid[0].size();
    int l = n * m;

    vector<int> ile(l);
    deque<int> q;

    for(int v = 0; v < l; v++){
        if(!((1 << v) & mask)) continue;
        for(auto u : graf[v]){
            if(!((1 << u) & mask)) continue;
            ile[v]++;
        }
        if(ile[v] == 0) return 0;
        if(ile[v] == 1) q.push_front(v);
        else q.push_back(v);
    }
    vis &= 0;

    for(int v : q){
        if(vis[v]) continue;
        int x = dfs(v, mask);
        if(x % 2) return 0;
    }

    ll ans = 0;

    for(int v = 0; v < l; v++){
        if((1 << v) & mask) continue;
        ans ^= grid[v / m][v % m];
    }
    return ans;
}

int main(){
    int n, m;
    cin >> n >> m;

    build_graf(n, m);

    vector<vector<ll>> grid(n, vector<ll>(m));

    for(auto &v : grid){
        for(ll &x : v) cin >> x;
    }


    int l = n * m;
    ll ans = 0;
    for(int mask = 0; mask < (1 << l); mask++){
        ans = max(ans, count_ans(mask, grid));
    }

    cout << ans << '\n';
}