#include <bits/stdc++.h>
using namespace std;
#define close ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define int long long 
#define endl '\n'
#define inf 0x3f3f3f3f3f3f3f3f
#define MAXN 100
const int MOD = 998244353; 
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};
int n,m;
void solve(){ 
    int n; cin >> n;
    vector<int> a(n),b(n);
    int s1 = 0,s2 = 0;
    for(int i = 0; i < n; i++){
        cin >> a[i];
        s1 += a[i];
    }
    for(int i = 0; i < n; i++){
        cin >> b[i];
        s2 += b[i];
    }
    if(s1 != s2){
        cout << "No" << endl;
        return;
    }
    if(s1 == 1){
        if(a[0] == 1 && b[0] == 1) cout << "Yes" << endl;
        else if(a[n-1] == 1 && b[n-1] == 1) cout << "Yes" << endl;
        else if(a[0] == 0 && b[n-1] == 0 && a[n-1] == 0 && b[0] == 0) cout << "Yes" << endl;
        else cout << "No" << endl;
        return;
    }
    cout << "Yes" << endl;
    
}
signed main(){
    close
    int T = 1;cin >> T;
    while(T--){
        solve();
    }
    
    return 0;
}