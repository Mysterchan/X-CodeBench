#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const int LM = 22;
ll n,m,arr[LM*2],ret=0;
bool visited[LM*2];
void dfs(int idx){
    if(idx>n*m){
        ll d=0;
        for(int i = 1; i<=n*m;i++){
            if(!visited[i])d^=arr[i];
        }
        ret=max(ret,d);
        return;
    }
    dfs(idx+1);
    if(visited[idx])return;
    if(idx+m<=n*m){
        if(!visited[idx+m]){
            visited[idx]=true;
            visited[idx+m]=true;
            dfs(idx+1);
            visited[idx]=false;
            visited[idx+m]=false;
        }
    }
    if(idx%m){
        if(!visited[idx+1]){
            visited[idx]=true;
            visited[idx+1]=true;
            dfs(idx+1);
            visited[idx]=false;
            visited[idx+1]=false;
        }
    }
}
signed main(){
    ios::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    cin >> n >> m;
    for(int i = 1; i <= m*n; i++){
        cin>>arr[i];
    }
    dfs(1);
    cout<<ret;
}
