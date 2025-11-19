#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    
    while (t--) {
        int n, m, k;
        cin >> n >> m >> k;
        vector<int> cnt(m + 1, 0);
        
        for (int i = 0; i < k; ++i) {
            int x, y;
            cin >> x >> y;
            if (y >= 1 && y <= m) ++cnt[y];
        }
        
        bool flag = false;
        
        if (n == 1) {
            if (m >= 2 && (cnt[2] % 2 == 1)) flag = true;
        } else {
            for (int y = 2; y <= m; ++y) {
                if (cnt[y] % 2 == 1) {
                    flag = true;
                    break;
                }
            }
        }
        
        cout << (flag ? "Mimo\n" : "Yuyu\n");
    }
    
    return 0;
}