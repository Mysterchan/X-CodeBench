#include<bits/stdc++.h>
using namespace std;
#define int long long

void slove(){
    int n, m;
    cin >> n >> m;
    
    if(m == 1){
        cout << 1 << endl;
        return;
    }
    
    int ans = m + ((m - 1) * (n - 1) + 1) / 2;
    cout << ans << endl;
}

signed main(){
    int T;
    cin >> T;
    while(T--) slove();
    return 0;
}