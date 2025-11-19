#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MAXN=1e6+5;
ll tests, n, m, tmp, flag;
char ch;
vector<pair<ll, ll>> v1, v2;
int main(){
  ios::sync_with_stdio(0);
  cin.tie(NULL);
  cout.tie(NULL);
  cin>>tests;
  while(tests--){
    cin>>n;
    m=n&(-n);
    n/=m;
    swap(n,m);
    bitset<MAXN> b1[n], b2[n];
    for(ll i=0; i<n; i++){
      for(ll j=0; j<m; j++){
        cin>>ch;
        b1[i][j]=ch-'0';
      }
    }
    for(ll i=0; i<n; i++){
      for(ll j=0; j<m; j++){
        cin>>ch;
        b2[i][j]=ch-'0';
      }
    }
    v1.clear();
    for(ll i=0; i<n; i++){
      for(ll j=0; j<v1.size(); j++){
        if(b1[i][v1[j].first]){
          b1[i]^=b1[v1[j].second];
        }
      }
      if(b1[i].any()){
        tmp=b1[i]._Find_next(-1);
        v1.insert(lower_bound(v1.begin(),v1.end(),make_pair(tmp,i)),make_pair(tmp,i));
      }
    }
    for(ll i=0; i<n; i++){
      for(ll j=0; j<v1.size(); j++){
        if(b1[i][v1[j].first]&&i!=v1[j].second){
          b1[i]^=b1[v1[j].second];
        }
      }
    }
    v2.clear();
    for(ll i=0; i<n; i++){
      for(ll j=0; j<v2.size(); j++){
        if(b2[i][v2[j].first]){
          b2[i]^=b2[v2[j].second];
        }
      }
      if(b2[i].any()){
        tmp=b2[i]._Find_next(-1);
        v2.insert(lower_bound(v2.begin(),v2.end(),make_pair(tmp,i)),make_pair(tmp,i));
      }
    }
    for(ll i=0; i<n; i++){
      for(ll j=0; j<v2.size(); j++){
        if(b2[i][v2[j].first]&&i!=v2[j].second){
          b2[i]^=b2[v2[j].second];
        }
      }
    }
    flag=0;
    if(v1.size()==v2.size()){
      flag=1;
      for(ll i=0; i<v1.size(); i++){
        if(v1[i].first!=v2[i].first||(b1[v1[i].second]!=b2[v2[i].second])){
          flag=0;
        }
      }
    }
    cout<<(flag?"YES":"NO")<<"\n";
  }
  return 0;
}