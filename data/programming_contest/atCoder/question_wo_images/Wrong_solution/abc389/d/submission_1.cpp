#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n,i=1;
    cin >> n;
    long long ans=4*(n-1)+1,x=n;
    while(i++){
      if((2*i+1)*(2*i+1)+(2*1+1)*(2*1+1)>4*n*n){
        break;
      }
      while((2*i+1)*(2*i+1)+(2*x+1)*(2*x+1)>4*n*n && x>0){
        x--;
      }
      ans+=4*x;
    }
    cout << ans << endl;
}