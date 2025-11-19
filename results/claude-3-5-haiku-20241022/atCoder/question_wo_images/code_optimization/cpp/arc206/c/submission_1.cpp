#include <bits/stdc++.h>
#define int long long
using namespace std;

const int MOD = 998244353;
int a[200010];

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    
    int l = 0, r = n;
    int bad_count = 0;
    
    for(int i = 1; i <= n; i++){
        cin >> a[i];
        if(a[i] == i + 1) l = max(l, i + 1);
        else if(a[i] == i - 1) r = min(r, i - 1);
        else if(a[i] != -1) bad_count++;
    }
    
    if(bad_count == 1 || l > r){
        cout << 0;
        return 0;
    }
    
    if(bad_count > 1){
        cout << 0;
        return 0;
    }
    
    int result = 0;
    for(int i = l; i <= r; i++){
        if(a[i] == -1){
            if(a[i-1] == -1){
                result = (result + n - 1) % MOD;
            } else {
                result = (result + n) % MOD;
            }
        }
    }
    
    cout << result;
    return 0;
}