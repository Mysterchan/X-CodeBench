#include<bits/stdc++.h>
using namespace std;
#define int long long
typedef pair<int,int> PII;
const int N=3e5+10;
int x[N];
vector<int>e[N];
set<int>s[N];
int p[N];
int U[N],V[N];
int find(int x){
    if(x!=p[x]) p[x]=find(p[x]);
    return p[x];
}

void solve(){
    int n,m;
    cin>>n>>m;
    for(int i=1;i<=n;i++) p[i]=i;
    for(int i=1;i<=m;i++){
        cin>>U[i]>>V[i];
        s[U[i]].insert(V[i]);
        s[V[i]].insert(U[i]);
    }
    int q;
    cin>>q;
    int ans=m;
    for(int i=1;i<=q;i++){
        int id;
        cin>>id;
        int u=find(U[id]);
        int v=find(V[id]);

        if(u==v){
            cout<<ans<<endl;
            continue;
        }
        if(s[u].size()>s[v].size()) swap(u,v);
        for(int it:s[u]){
            s[it].erase(u);
            m--;
            if(it!=v&&!s[v].count(it)){
                s[v].insert(it);
                s[it].insert(v);
                m++;
            }
        }
        s[u].clear();
        p[u]=v;
        cout<<m<<endl;
    }
}

signed main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    solve();
}
