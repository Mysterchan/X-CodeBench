#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> a(n), b(m);
    
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < m; i++) {
        cin >> b[i];
    }

    // Map to store indices of each value in A
    unordered_map<int, vector<int>> index_map;
    for (int i = 0; i < n; i++) {
        index_map[a[i]].push_back(i);
    }

    int prev_index = -1;
    int count = 0;

    // Check for two distinct subsequence matching
    for (int j = 0; j < m; j++) {
        if (index_map.find(b[j]) == index_map.end()) {
            // No occurrence of B[j] in A
            cout << "No" << endl;
            return 0;
        }

        // Find the next position of b[j] after prev_index
        auto& indices = index_map[b[j]];
        
        // Use lower_bound to find the first index greater than prev_index
        auto it = lower_bound(indices.begin(), indices.end(), prev_index + 1);
        
        if (it != indices.end()) {
            prev_index = *it; // Move to the next position in the match
        } else {
            // Reset and check again to count the occurrences
            count++;
            prev_index = indices[0];
            it = lower_bound(indices.begin(), indices.end(), prev_index + 1);
            if (it != indices.end()) {
                prev_index = *it;
            } else {
                cout << "No" << endl;
                return 0;
            }
        }

        // If we've found more than 1 subsequence, we can conclude early
        if (count > 1) {
            cout << "Yes" << endl;
            return 0;
        }
    }

    // After processing all elements in B, check count
    cout << (count >= 1 ? "No" : "Yes") << endl;
}
