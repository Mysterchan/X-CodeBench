#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        
        if (a[0] != 2 || a[n-1] != 0) {
            cout << "0\n";
            continue;
        }
        
        int ans = 1;
        for (int i = 0; i < n; i++) {
            if (a[i] > 2) {
                ans = 0;
                break;
            }
            if (i > 0 && a[i] == 2 && a[i-1] == 0) {
                ans = 0;
                break;
            }
            if (i > 0 && a[i] == 1 && a[i-1] == 0) {
                int j = i;
                while (j < n && a[j] == 1) j++;
                int len = j - i;
                if (len % 2 == 1) {
                    ans = 0;
                    break;
                }
                if (len >= 2) {
                    int ways = 1;
                    for (int k = 0; k < len/2 - 1; k++) {
                        ways = (ways * 2) % MOD;
                    }
                    ans = (ans * ways) % MOD;
                }
                i = j - 1;
            }
        }
        
        cout << ans << "\n";
    }
    
    return 0;
}

