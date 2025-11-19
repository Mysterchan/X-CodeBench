#include<bits/stdc++.h>
using namespace std;
#define int long long
void solve(){
    int a,b,c;
    cin>>a>>b>>c;
    if(a*b==c || a*c==b || b*c==a) cout<<"Yes"<<endl;
    else cout<<"No"<<endl;
}
signed main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
    int T = 1;
    // cin>>T;
    while(T--){
        solve();
    }
    return 0;
}