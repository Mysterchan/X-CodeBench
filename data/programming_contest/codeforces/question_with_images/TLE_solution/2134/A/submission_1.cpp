#include<bits/stdc++.h>
using namespace std;
typedef long long ll;


signed main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    ll T;
    cin>>T;
    while(T--){
        ll n,a,b;
        cin>>n>>a>>b;
        for(size_t y=1;y<=n-b+1;y++){
            if((double)y==(double)(n-b+2)/2) {
                if(y<=(n-a+1)&&(y+b-1)>(y+a-1)){
                    cout<<"YES"<<endl;
                    goto end;
                }
                else for(size_t x=1;x<=n-a+1;x++){
                    if((double)x==(double)(n-a+2)/2) {
                        cout<<"YES"<<endl;
                        goto end;
                    }
                }
                break;
            }
        }
        cout<<"NO"<<endl;
        end:;
    }
}