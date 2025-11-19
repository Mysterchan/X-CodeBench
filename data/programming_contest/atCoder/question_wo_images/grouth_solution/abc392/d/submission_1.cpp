#include<bits/stdc++.h>
using namespace std;
#define int long long
void solve(){
    int n;
    cin>>n;
    vector<vector<int>> cnt(2e5+5, vector<int>(n+1));
    vector<int> k(n+1);
    double ans = 0;
    for(int i = 1; i <= n; i++){
        cin>>k[i];
        set<int> s;
        for(int j = 1; j <= k[i]; j++){
            int x;
            cin>>x;
            s.insert(x);
            cnt[x][i]++;
        }
        
        for(int j = 1; j < i; j++){
            double mx = 0;
            for(auto x:s){
                mx += 1.0*cnt[x][i]*cnt[x][j]/(k[i]*k[j]);
            }
            ans = max(ans, mx);
        }
        
    }
    cout<<fixed<<setprecision(15)<<ans<<endl;
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