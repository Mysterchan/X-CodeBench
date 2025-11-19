#include <bits/stdc++.h>
using namespace std;

int n, m, x, y;
bool end_flag;
vector<vector<int>> graph;
vector<int> path;

void dfs(int v){
    
    path.push_back(v);
    if(v==y){
        if(!end_flag){
            for(int ans_v: path) cout << ans_v+1 << " ";
            cout << endl;
            end_flag = true;
        }
    }
    for(int nv: graph.at(v)){
        bool ok = true;
        for(int target: path){
            if(target==nv) ok = false;
        }
        if(ok) dfs(nv);
    }
    path.pop_back();

}

int main(){

    int t;
    cin >> t;
    while(t--){

        cin >> n >> m >> x >> y;
        x--, y--;
        graph.clear();
        graph.resize(n);
        path.clear();
        end_flag = false;
        for(int i=0; i<m; i++){
            int u, v;
            cin >> u >> v;
            u--, v--;
            graph.at(u).push_back(v);
            graph.at(v).push_back(u);
        }

        for(int i=0; i<n; i++) sort(graph.at(i).begin(), graph.at(i).end());
        dfs(x);
    }

}