#include<bits/stdc++.h>
using namespace std;
#define int long long
void solve(){
    int m,n;
    cin>>n>>m;
    set<int> s;
    for(int i = 1; i <= n; i++) s.insert(i);
    for(int i = 1; i <= m; i++){
        int x;
        cin>>x;
        s.erase(x);
    }
    cout<<s.size()<<endl;
    for(auto x:s) cout<<x<<' ';
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