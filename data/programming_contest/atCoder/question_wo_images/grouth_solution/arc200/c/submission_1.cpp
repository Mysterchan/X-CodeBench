#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int n; cin >> n;
    vector <int> l(n + 1),r(n + 1),in(n + 1),ans(n + 1);
    vector <vector <int> > G(n + 1);
    int dfn = 0;
    for(int i = 1;i <= n;i ++){
        cin >> l[i] >> r[i];
    }
    for(int i = 1;i <= n;i ++){
        for(int j = 1;j <= n;j ++){
            if(i == j) continue;
            if(l[i] <= l[j] && r[j] <= r[i]){
                G[i].push_back(j); in[j] ++;
            }
        }
    }
    priority_queue <int> q;
    for(int i = 1;i <= n;i ++) if(!in[i]) q.push(i);
    while(!q.empty()){
        int u = q.top(); q.pop();
        ans[u] = n - (++ dfn) + 1;
        for(int v : G[u]){
            in[v] --;
            if(in[v] == 0) q.push(v);
        }
    }
    for(int i = 1;i <= n;i ++) cout << ans[i] << " \n"[i == n];
}

int main(){
    ios::sync_with_stdio(false);
    int TC; cin >> TC;
    while(TC --)
        solve();
    return 0;
}