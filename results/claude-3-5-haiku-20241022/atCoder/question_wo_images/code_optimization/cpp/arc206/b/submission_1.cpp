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
        if(v[i].empty())continue;
        vector<int>dp;
        dp.reserve(v[i].size());
        for(int j:v[i]){
            auto it=lower_bound(dp.begin(),dp.end(),j);
            if(it==dp.end()){
                dp.push_back(j);
            }else{
                *it=j;
            }
        }
        ans+=(ll)(((int)v[i].size())-((int)dp.size()))*(i+1);
    }
    cout<<ans<<'\n';
}