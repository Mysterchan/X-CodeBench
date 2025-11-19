#include <bits/stdc++.h>
using namespace std;
#define int long long
typedef pair<char,int> PII;
const int N=5e6+10;

vector<int>e[N];
int n,m;
int a[N];
struct node{
    int u,d;
    bool operator <(const node & x) const{
        return d<x.d;
    }
};
int dist[N];
int w[N];
void bfs(){
    for(int i=1;i<=n;i++) dist[i]=1e18;
    for(int i=1;i<=n;i++) w[i]=1e18;
    priority_queue<node>q;
    dist[1]=0;
    w[1]=a[1];
    q.push({0,1});
    while(!q.empty()){
        auto [d,u]=q.top();
        q.pop();
        for(int v:e[u]){
            if(dist[v]>dist[u]+w[u]){
                dist[v]=dist[u]+w[u];
                q.push({dist[v],v});
            }
            if(w[v]>w[u]+a[v]) w[v]=w[u]+a[v];
        }
    }
}
void solve() {
     
    cin>>n>>m;
    for(int i=1;i<=n;i++) cin>>a[i];
    for(int i=1;i<=m;i++){
        int u,v;
        cin>>u>>v;
        e[u].push_back(v);
        e[v].push_back(u);
    }
    bfs();
    for(int i=1;i<=n;i++) cout<<dist[i]<<endl;
}

signed main() {
    srand(time(0));
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T=1;
    while(T--){
        solve();
    }
}

