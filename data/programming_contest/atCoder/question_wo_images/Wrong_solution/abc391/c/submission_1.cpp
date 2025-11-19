#include<bits/stdc++.h>
using namespace std;
const int mxn=1e6+10;
int n,q,p,h,op;
int don[mxn],ge[mxn];
int ans;
void op2();
signed main(){
    cin>>n>>q;
    for(int i=1;i<=n;++i){ don[i]=1;ge[i]=i;}
    while(q--){
        cin>>op;
        if(op==1){
            cin>>p>>h;
            don[h]++;
            don[ge[p]]--;
            if(don[h]==2) ans++;
            if(don[ge[p]]==1) ans--;
        }
        else cout<<ans<<endl;
    }
    return 0;
}