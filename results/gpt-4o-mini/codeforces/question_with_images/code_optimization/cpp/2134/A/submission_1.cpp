#include<bits/stdc++.h>
using namespace std;

signed main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    ll T;
    cin >> T;
    while(T--){
        ll n, a, b;
        
        cin >> n >> a >> b;
        
        // The conditions to check
        if (n < a + b) {
            cout << "NO" << endl;
            continue;
        }
        
        if ((n - a) % 2 == (n - b) % 2) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}