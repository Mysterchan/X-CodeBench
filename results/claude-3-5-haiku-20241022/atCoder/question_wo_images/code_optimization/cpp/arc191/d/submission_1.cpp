#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M, S, T;
    cin >> N >> M >> S >> T;
    
    vector<vector<int>> g(N+1);
    for(int i=0;i<M;i++){
        int u,v; cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    auto bfs = [&](int src){
        vector<int> d(N+1, -1);
        queue<int> q;
        d[src] = 0;
        q.push(src);
        while(!q.empty()){
            int v = q.front(); q.pop();
            for(int to : g[v]){
                if(d[to] == -1){
                    d[to] = d[v] + 1;
                    q.push(to);
                }
            }
        }
        return d;
    };

    vector<int> dS = bfs(S);
    vector<int> dT = bfs(T);
    
    if(dS[T] == -1){
        cout << -1 << '\n';
        return 0;
    }

    const int base = 2 * dS[T];
    vector<vector<int>> dist(N+1, vector<int>(N+1, -1));
    
    vector<vector<pair<int,int>>> bucket(3);
    bucket[0].push_back({S, T});
    dist[S][T] = 0;
    
    int curd = 0;
    
    for(int bi = 0; ; bi = (bi + 1) % 3, ++curd){
        if(bucket[bi].empty()){
            if(bucket[(bi+1)%3].empty() && bucket[(bi+2)%3].empty()){
                cout << -1 << '\n';
                return 0;
            }
            continue;
        }
        
        vector<pair<int,int>> current;
        swap(current, bucket[bi]);
        
        for(auto [a, b] : current){
            if(dist[a][b] != curd) continue;
            
            if(a == T && b == S){
                cout << base + curd << '\n';
                return 0;
            }
            
            for(int an : g[a]){
                if(an == b) continue;
                int w = 1 + (dT[an] - dT[a]);
                int nd = curd + w;
                int nbi = nd % 3;
                if(dist[an][b] == -1 || dist[an][b] > nd){
                    dist[an][b] = nd;
                    bucket[nbi].push_back({an, b});
                }
            }
            
            for(int bn : g[b]){
                if(bn == a) continue;
                int w = 1 + (dS[bn] - dS[b]);
                int nd = curd + w;
                int nbi = nd % 3;
                if(dist[a][bn] == -1 || dist[a][bn] > nd){
                    dist[a][bn] = nd;
                    bucket[nbi].push_back({a, bn});
                }
            }
        }
    }
    
    return 0;
}