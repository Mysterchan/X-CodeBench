#include <bits/stdc++.h>

using namespace std;

int L[505], R[505], p[505];
vector<int> adj[505];
int d[505];

int dfs(int v, int st, int n) {
    vector<int> children;
    for(int u : adj[v]) {
        children.push_back(u);
    }
    
    sort(children.begin(), children.end(), [](int a, int b) {
        return L[a] < L[b];
    });
    
    for(int u : children) {
        st = dfs(u, st, n);
    }
    
    if(v != 0) {
        p[v] = st++;
    }
    
    return st;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int t;
    cin >> t;
    
    while(t--){
        int n;
        cin >> n;
        
        for(int i = 0; i <= n; i++){
            adj[i].clear();
            d[i] = 0;
            p[i] = 0;
        }
        
        for(int i = 1; i <= n; i++){
            cin >> L[i] >> R[i];
        }
        
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                if(L[j] > L[i] && R[i] > R[j]){
                    adj[i].push_back(j);
                    d[j]++;
                }
            }
        }
        
        for(int i = 1; i <= n; i++){
            if(d[i] == 0){
                adj[0].push_back(i);
            }
        }
        
        dfs(0, 1, n);
        
        for(int i = 1; i <= n; i++){
            cout << p[i];
            if(i < n) cout << " ";
        }
        cout << "\n";
    }
    
    return 0;
}