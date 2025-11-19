#include <bits/stdc++.h>
using namespace std;
using ll=long long;
ll INF=1e9;
int main(){
    ll t;
    cin>>t;
    while(t--){
    ll n;
    cin>>n;
    ll maxi=0;
    vector <vector <ll>> v;
    for(ll i=0;i<n;i++){
        ll si;
        cin>>si;
        vector <ll> gr(si+1);
        gr[0]=si;
        for(ll j=1;j<=si;j++){
            cin>>gr[j];
        }
        v.push_back(gr);
        maxi=max(maxi,si+1);
    }
    vector <ll> bo(maxi);
    vector <ll> ind(maxi);
    for(ll j=1;j<maxi;j++){
        ll mini=1e9;
        set <ll> s;
        for(ll i=0;i<n;i++){
           if(v[i][0]<j) continue;
           if(v[i][j]<mini){
                mini=v[i][j];
                ind[j]=i;
           }
           if(v[i][j]!=INF) s.insert(v[i][j]); 
        }
        if(s.size()==1) bo[j]=*(s.begin());
        int ct=0;
        for(ll i=0;i<n;i++){
           if(v[i][0]<j) continue;
           if(v[i][j]==mini) ct++;
        }
        if(ct>1) bo[j]=*(s.begin());
    }
    vector <ll> ans;
    for(ll j=1;j<maxi;j++){
          if(bo[j]!=0){
             ans.push_back(bo[j]);
             continue;
          }
          ll i1=ind[j];
          ll si=v[i1][0];
          for(ll j1=j;j1<=si;j1++){
            ans.push_back(v[i1][j1]);
          }
          j=si;
    }
    for(auto ele : ans){
        cout<<ele<<" ";
    }
    cout<<endl;

}
}
