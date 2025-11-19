#include<bits/stdc++.h>
using namespace std;
int n;
int a[1000040];
int b[1100004];
bool ok;
signed main(){
    cin>>n;
    for(int i=0;i<n;i++){
      cin>>a[i];
      if(a[i]==1) ok=1;
    }
    int m=n%4;
    if(!m){
      cout<<"yes\n";
      return 0;
    }
    if(m==1||m==3){
      if(ok) cout<<"Yes\n";
      else cout<<"No\n";
      return 0;
    }
    if(m==2){
      for(int i=0;i<n;i++){
        if(a[i]&&b[(i&1)^1]) {
          cout<<"yEs\n";
          return 0;
        } else if(a[i]) b[(i&1)]=1;
      }
      
      cout<<"no\n";
    } 
}