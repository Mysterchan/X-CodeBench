#include<bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, m;
    cin >> n >> m;
    
    set<pair<int,int>> unique_edges;
    int self_loops = 0;
    
    for(int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        
        if(u == v) {
            self_loops++;
        } else {
            if(u > v) swap(u, v);
            unique_edges.insert({u, v});
        }
    }
    
    int duplicates = m - self_loops - unique_edges.size();
    cout << self_loops + duplicates << endl;
    
    return 0;
}