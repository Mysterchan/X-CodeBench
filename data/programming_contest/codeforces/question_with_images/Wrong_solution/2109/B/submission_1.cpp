#include<bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin>>t;
    while(t--){
          long long int n,m,x,y;
          cin>>n>>m>>x>>y;
             int ans=0;
          while(n>1 || m>1){
            long long l=0;
            long long r=0;
            long long u=0;
            long long d=0;
    
            if(y>=1){
                l=n*(y-1);
            }
            if(y<=m){
                r=n*(m-y);
            }
            if(x>=1){
                u=m*(x-1);
            }
            if(x<=n){
                d=m*(n-x);
            }
            long long maxe = max({l, r, u, d});

        if(maxe == l){
            m = m+1 - y;
            } 
        else if(maxe == r){
            m = y;
             } 
         else if(maxe == u){
             n = n+1- x ;
              } 
           else{
               n = x;
                }


            x=(n+1)/2;
            y=(m+1)/2;
            ans++;
             
          }
          cout<<ans<<endl;
    }
}