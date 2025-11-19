#include <bits/stdc++.h>
using namespace std;



const int maximum=INT_MAX;
const int minimum=INT_MIN;
typedef long long ll;
typedef unsigned long long int ull;
const int MOD=1e9+7;


void solve(){
    
    int n,m,k;
    cin>>n>>m>>k;
    
    int a= ceil((k*1.0)/n);
    if(a>=m)cout<<a<<"\n";
    else{
        for(int i=1;i<=m;i++){
            int x= ceil((a*1.0)/i);
            int y=a%i;
            int t=0;
            if(y==0){
                t=x*i+x-1;
            }
            else t=(x-1)*i+y+x-1;
            if(t<=m){
                cout<<i<<"\n";
                return;
            }
        }
    }
        return;
}

int main() {
    ll t;
    cin>>t;
    while(t--){
        solve();
    }
	return 0;
 }