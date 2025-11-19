#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<ll,ll> pll;
typedef pair<int,int> pii;
typedef pair<int,string> pis;
typedef pair<pii,int> ppiii;
typedef array<int, 27> a27;

#define lc id<<1
#define rc id<<1|1
#define mid (l+r)/2
#define F first
#define S second
#define pb push_back

const ll N= 5e3+5,M = 1e6,B=1e6+7, inf = 1e18,mod = 998244353;

vector<int> adj[N];
int d[N], p[N],L[N],R[N], lst;
set<int> s[N];
void dfs(int v, int i){
    s[i].insert(v);
    for(int u:adj[v]){
        dfs(u,i);
    }
}
int f(int v, int st){

    for(int u : adj[v]){
        dfs(u,v);
    }
    while(s[v].size()){
        int x = *s[v].begin();
        s[v].erase(s[v].begin());
        if(p[x])
            continue;
        st= f(x,st);
    }
    p[v]= st;
    return ++st;
}
int main(){
    ios::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        d[0] = p[0] = 0;
        adj[0].clear();
        s[0].clear();
        for(int i = 1; i<=n; i++){
            cin >> L[i] >> R[i];
            d[i]=0;
            p[i]=0;
            adj[i].clear();
            s[i].clear();

        }
        lst = 0;
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                if(L[j] > L[i] and R[i] > R[j]){
                    adj[i].pb(j);
                    d[j]++;
                }
            }
        }
        for(int i = 1; i<=n; i++){
            if(!d[i])
                adj[0].pb(i);
        }
        f(0,1);
        for(int i=1; i<=n; i++)
            cout << p[i]<< " ";
        cout << endl;
    }
    return 0;
}
