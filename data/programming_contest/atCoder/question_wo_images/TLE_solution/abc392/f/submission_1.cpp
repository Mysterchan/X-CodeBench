#include<bits/stdc++.h>
using namespace std;
#define int long long
void solve(){
    int n;
    cin>>n;
    vector<int> a;
    a.push_back(0);
    for(int i = 1; i <= n; i++) {
        int pos;
        cin>>pos;
        a.insert(a.begin()+pos, i);
    }
    for(int i = 1; i < a.size(); i++) cout<<a[i]<<' ';
}
signed main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
    int T = 1;
    while(T--){
        solve();
    }
    return 0;
}