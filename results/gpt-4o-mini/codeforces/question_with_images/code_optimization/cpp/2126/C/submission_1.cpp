#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, k;
        cin >> n >> k;
        k--;  // Convert to zero-based index
        
        vector<long long> h(n);
        for (int i = 0; i < n; i++) {
            cin >> h[i];
        }
        
        long long max_height = *max_element(h.begin(), h.end());
        
        // If the current tower already has the maximum height
        if (h[k] == max_height) {
            cout << "YES\n";
            continue;
        }
        
        // Check if we can reach a tower with max height
        // Both left and right movements are possible until we can't move anymore
        long long time_limit = h[k];

        // Try to traverse to the left
        for (int i = k; i >= 0; i--) {
            if (h[i] >= time_limit) {
                time_limit++; // Increase time limit as we can stand here until we teleport.
            } else {
                break;
            }
            if (h[i] == max_height) {
                cout << "YES\n";
                goto next_case;
            }
        }

        // Try to traverse to the right
        for (int i = k; i < n; i++) {
            if (h[i] >= time_limit) {
                time_limit++; // Increase time limit as we can stand here until we teleport.
            } else {
                break;
            }
            if (h[i] == max_height) {
                cout << "YES\n";
                goto next_case;
            }
        }

        cout << "NO\n";

        next_case:; // Label to continue with next test case
    }

    return 0;
}