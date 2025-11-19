#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T;
    cin >> T;
    
    while (T--) {
        int n;
        cin >> n;
        
        vector<int> a(n), b(n);
        int sum_a = 0, sum_b = 0;
        
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            sum_a += a[i];
        }
        
        for (int i = 0; i < n; i++) {
            cin >> b[i];
            sum_b += b[i];
        }
        
        // If counts don't match, impossible
        if (sum_a != sum_b) {
            cout << "No\n";
            continue;
        }
        
        // If already equal
        if (a == b) {
            cout << "Yes\n";
            continue;
        }
        
        // Edge cases
        if (sum_a == 0 || sum_a == n) {
            // All 0s or all 1s - must be equal already
            cout << "No\n";
            continue;
        }
        
        if (sum_a == 1 || sum_a == n - 1) {
            // Only one 1 or one 0 - very limited transformations
            // Check if they're equal
            cout << (a == b ? "Yes" : "No") << "\n";
            continue;
        }
        
        // For most cases with at least 2 ones and 2 zeros,
        // the operation is powerful enough to reach any configuration
        // with the same count of 1s and 0s
        cout << "Yes\n";
    }
    
    return 0;
}