#include<bits/stdc++.h>
using namespace std;
int main(){
  int Q; cin>>Q; long long nuke=0LL; vector<long long>h(2*Q+1,0);
  int cnt1=0;  int cnt2=0;
  for(int i=1; i<=Q; i++){
    int t; cin>>t;
    if(t==1){
      cnt1++;
      long long l; cin>>l;
      h.at(cnt1)=h.at(cnt1-1)+l;
    }
    if(t==2){
      cnt2++;
      nuke=h[cnt2];
      
    }
    if(t==3){
      int k; cin>>k;
      cout<<h.at(k-1+cnt2)-nuke<<endl;
    }
  }
}
