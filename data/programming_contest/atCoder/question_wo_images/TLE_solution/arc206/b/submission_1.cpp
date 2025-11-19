#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    int n;
    cin>>n;
    vector<int>p(n);
    vector<vector<int>>v(n);
    for(int i=0;i<n;i++)cin>>p[i];
    for(int i=0;i<n;i++){
        int c;
        cin>>c;
        v[c-1].push_back(p[i]);
    }
    ll ans=0;
    for(int i=0;i<n;i++){
        vector<int>dp(n,1e9);
        int mx=0;
        for(int j:v[i]){
            int it=lower_bound(dp.begin(),dp.end(),j)-dp.begin();
            dp[it]=j;
            mx=max(mx,it+1);
        }
        ans+=(ll)(((int)v[i].size())-mx)*(i+1);
    }
    cout<<ans<<'\n';
}