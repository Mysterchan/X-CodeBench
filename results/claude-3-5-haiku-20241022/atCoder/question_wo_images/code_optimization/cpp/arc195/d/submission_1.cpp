#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; 
    cin >> n;
    vector<int> a(n);
    for(int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    vector<int> dp(n + 1, 0);
    
    for(int i = 0; i < n; i++) {
        dp[i + 1] = max(dp[i + 1], dp[i] + 1);
        
        vector<int> b(a.begin() + i, a.end());
        int m = b.size();
        
        for(int len = 1; len <= m; len++) {
            bool can_make_equal = true;
            int swaps = 0;
            vector<int> temp = b;
            
            for(int j = 1; j < len; j++) {
                if(temp[j] != temp[0]) {
                    int pos = -1;
                    for(int k = j + 1; k < len; k++) {
                        if(temp[k] == temp[0]) {
                            pos = k;
                            break;
                        }
                    }
                    if(pos == -1) {
                        can_make_equal = false;
                        break;
                    }
                    while(pos > j) {
                        swap(temp[pos], temp[pos - 1]);
                        pos--;
                        swaps++;
                    }
                }
            }
            
            if(can_make_equal) {
                int new_pos = i + len;
                dp[new_pos] = max(dp[new_pos], dp[i] + swaps + 1);
            }
        }
    }
    
    cout << dp[n] << '\n';
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int TC;
    cin >> TC;
    while(TC--){
        solve();
    }
    return 0;
}