#include<bits/stdc++.h>
using namespace std;
#define endl "\n"
typedef long long ll;
typedef pair<ll, ll> pll;
ll n;
vector<string> ve;
string s;
ll dfs(ll cur, ll pt){
    if(cur==(n+1)){
        return 1;
    }
    char target;
    if(ve[cur][pt]=='0'){
        target='1';
    }else{
        target='0';
    }
    ll sum0, sum1;
    ll i=pt*3;
    sum0=(ve[cur+1][i]=='0')+(ve[cur+1][i+1]=='0')+(ve[cur+1][i+2]=='0');
    sum1=(ve[cur+1][i]=='1')+(ve[cur+1][i+1]=='1')+(ve[cur+1][i+2]=='1');
    ll ans=LONG_LONG_MAX;
    if(target=='1'){
        if(sum1<sum0){
            if(sum0==3){
                for(ll j=pt*3;j<pt*3+2;j++){
                    for(ll k=j+1;k<=pt*3+2;k++){
                        ans=min(ans, dfs(cur+1, j)+dfs(cur+1, k));
                    }
                }
            }else{
                for(ll j=pt*3;j<=pt*3+2;j++){
                    if(ve[cur+1][j]=='0'){
                        ans=min(ans, dfs(cur+1, j));
                    }
                }
            }
        }
    }else{
        if(sum1>sum0){
            if(sum1==3){
                for(ll j=pt*3;j<pt*3+2;j++){
                    for(ll k=j+1;k<=pt*3+2;k++){
                        ans=min(ans, dfs(cur+1, j)+dfs(cur+1, k));
                    }
                }
            }else{
                for(ll j=pt*3;j<=pt*3+2;j++){
                    if(ve[cur+1][j]=='1'){
                        ans=min(ans, dfs(cur+1, j));
                    }
                }
            }
        }
    }
    if(ans==LONG_LONG_MAX){
        return 0;
    }else{
        return ans;
    }
}
void solved(){
    cin>>n;
    cin>>s;
    ve.resize(n+2);
    ve[n+1]=s;
    ll sum0, sum1;
    for(ll i=n+1;i>=2;i--){
        for(ll j=0;j<ve[i].size()-2;j+=3){
            sum0=(ve[i][j]=='0')+(ve[i][j+1]=='0')+(ve[i][j+2]=='0');
            sum1=(ve[i][j]=='1')+(ve[i][j+1]=='1')+(ve[i][j+2]=='1');
            ve[i-1].push_back(sum0>sum1?'0':'1');
        }
    }
    ll ans=dfs(1, 0);
    cout<<ans;
}
signed main(){
	ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    ll T;
    T=1;
    while(T--){
        solved();
    }
    return 0;
}

