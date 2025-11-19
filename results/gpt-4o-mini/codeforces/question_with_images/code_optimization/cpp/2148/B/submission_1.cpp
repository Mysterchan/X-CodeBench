#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T;
    cin >> T;
    while (T--) {
        int n, m, x, y;
        cin >> n >> m >> x >> y;
        
        vector<int> horizontal(n);
        vector<int> vertical(m);
        
        for (int i = 0; i < n; i++) {
            cin >> horizontal[i];
        }
        
        for (int i = 0; i < m; i++) {
            cin >> vertical[i];
        }
        
        int crossings = 0;
        
        // Check if we need to cross horizontal lasers
        if (horizontal[0] > 0) {
            crossings++; // Need to cross the first horizontal at least
        }
        
        for (int i = 1; i < n; i++) {
            if (horizontal[i] < y) {
                crossings++; // Cross each horizontal laser in the way
            }
        }
        
        // Check if we need to cross vertical lasers
        if (vertical[0] > 0) {
            crossings++; // Need to cross the first vertical at least
        }
        
        for (int i = 1; i < m; i++) {
            if (vertical[i] < x) {
                crossings++; // Cross each vertical laser in the way
            }
        }
        
        cout << crossings << '\n';
    }
    
    return 0;
}