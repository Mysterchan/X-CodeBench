#include<bits/stdc++.h>
using namespace std;
#define int long long

void solve(){
    int n;
    cin>>n;
    vector<int> p(n+1);
    for(int i = 1; i <= n; i++) {
        cin>>p[i];
    }
    
    deque<int> a;
    for(int i = n; i >= 1; i--) {
        // When going backwards, inserting at position p[i] means
        // we need to insert at position (i - p[i]) from the end
        int pos = i - p[i];
        a.insert(a.begin() + pos, i);
    }
    
    for(int i = 0; i < a.size(); i++) {
        if(i > 0) cout << ' ';
        cout << a[i];
    }
    cout << '\n';
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