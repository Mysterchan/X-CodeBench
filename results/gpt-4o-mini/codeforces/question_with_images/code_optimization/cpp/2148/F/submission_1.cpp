#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<vector<int>> arrays(n);
        int maxSize = 0;
        
        for (int i = 0; i < n; i++) {
            int k;
            cin >> k;
            arrays[i].resize(k);
            for (int j = 0; j < k; j++) {
                cin >> arrays[i][j];
            }
            maxSize = max(maxSize, k);
        }
        
        vector<int> result;
        vector<int> nextIndex(n, 0);
        vector<int> columns;

        // Create a column list where each index corresponds to arrays that can contribute
        for (int j = 0; j < maxSize; j++) {
            vector<int> candidates;
            
            for (int i = 0; i < n; i++) {
                if (nextIndex[i] < arrays[i].size()) {
                    candidates.push_back(arrays[i][nextIndex[i]]);
                }
            }
            
            // If there are candidates, find the minimum and fill result
            if (!candidates.empty()) {
                int minValue = *min_element(candidates.begin(), candidates.end());
                result.push_back(minValue);
                
                // Update the array indices
                for (int i = 0; i < n; i++) {
                    if (nextIndex[i] < arrays[i].size() && arrays[i][nextIndex[i]] == minValue) {
                        nextIndex[i]++;
                    }
                }
            }
        }
        
        // Output the result
        for (int ele : result) {
            cout << ele << " ";
        }
        cout << "\n";
    }
}