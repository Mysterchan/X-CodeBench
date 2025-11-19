#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin>>n;
  vector<int> a(n);
  for(auto &i:a)cin>>a[i];
  for(int i=1;i<n-2;i++){
    if(a[i]*a[i]!=a[i-1]*a[i+1]){cout<<"No"<<endl;return 0;}
  }
  cout<<"Yes"<<endl;
}
