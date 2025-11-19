#include <bits/stdc++.h>
using namespace std;
#define V vector
#define LL long long
 
enum Color {
    RED,
    BLUE
};
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
 
    int t;
    cin >> t;
    while(t--){
        int n, m, q;
        cin >> n >> m >> q;
        V<V<int>> adj(n+1);
        V<V<int>> revAdj(n+1);
        V<int> out_degree(n+1, 0);
        
        for(int i=0; i<m; i++){
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            revAdj[v].push_back(u);
            out_degree[u]++;
        }
        
        V<Color> colors(n+1);
        for(int i=1; i<=n; i++){
            colors[i] = BLUE;
        }
        
        V<int> in_degree(n+1, 0);
        for(int i=1; i<=n; i++){
            for(int v : adj[i]){
                in_degree[v]++;
            }
        }
        
        queue<int> q_topo;
        for(int i=1; i<=n; i++){
            if(in_degree[i] == 0){
                q_topo.push(i);
            }
        }
        
        V<int> topo;
        while(!q_topo.empty()){
            int u = q_topo.front();
            q_topo.pop();
            topo.push_back(u);
            for(int v : adj[u]){
                in_degree[v]--;
                if(in_degree[v] == 0){
                    q_topo.push(v);
                }
            }
        }
        
        V<bool> cryWin0(n+1, false);
        V<bool> cryWin1(n+1, false);
        
        for(int i = topo.size()-1; i >= 0; i--){
            int u = topo[i];
            
            if(colors[u] == RED){
                cryWin0[u] = false;
                cryWin1[u] = false;
            }
            else if(out_degree[u] == 0){
                cryWin0[u] = true;
                cryWin1[u] = true;
            }
            else{
                cryWin0[u] = false;
                for(int v : adj[u]){
                    cryWin0[u] = cryWin0[u] || cryWin1[v];
                }
                
                cryWin1[u] = true;
                for(int v : adj[u]){
                    cryWin1[u] = cryWin1[u] && cryWin0[v];
                }
            }
        }
 
        for(int i=0; i<q; i++){
            int x, u;
            cin >> x >> u;
            
            if(x == 1){
                if(colors[u] == RED) continue;
                colors[u] = RED;
                
                bool oldWin0 = cryWin0[u];
                bool oldWin1 = cryWin1[u];
                
                cryWin0[u] = false;
                cryWin1[u] = false;
                
                if(oldWin0 == false && oldWin1 == false) continue;
                
                queue<int> updateQueue;
                for(int parent : revAdj[u]){
                    updateQueue.push(parent);
                }
                
                while(!updateQueue.empty()){
                    int current = updateQueue.front();
                    updateQueue.pop();
                    
                    if(colors[current] == RED){
                        cryWin0[current] = false;
                        cryWin1[current] = false;
                        continue;
                    }
                    
                    bool newWin0 = false;
                    bool newWin1 = true;
                    
                    for(int child : adj[current]){
                        newWin0 = newWin0 || cryWin1[child];
                        newWin1 = newWin1 && cryWin0[child];
                    }
                    
                    if(newWin0 != cryWin0[current] || newWin1 != cryWin1[current]){
                        cryWin0[current] = newWin0;
                        cryWin1[current] = newWin1;
                        
                        for(int parent : revAdj[current]){
                            updateQueue.push(parent);
                        }
                    }
                }
            }
            else{
                if(cryWin0[u]){
                    cout << "YES" << '\n';
                }
                else{
                    cout << "NO" << '\n';
                }
            }
        }
    }
    
    return 0;
}