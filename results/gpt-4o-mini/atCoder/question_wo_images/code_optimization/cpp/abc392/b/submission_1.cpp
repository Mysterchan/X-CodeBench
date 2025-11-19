#include<bits/stdc++.h>

using namespace std;

int main(){
    int n, m;
    cin >> n >> m;
    vector<bool> present(n + 1, false);
    for (int i = 0; i < m; ++i) {
        int x;
        cin >> x;
        present[x] = true; // Mark each number in A as present
    }
    
    vector<int> missing;
    for (int i = 1; i <= n; ++i) {
        if (!present[i]) {
            missing.push_back(i); // Collect all missing numbers
        }
    }

    cout << missing.size() << endl; // Output the count of missing numbers
    if (!missing.empty()) {
        for (int num : missing) {
            cout << num << " "; // Output all missing numbers
        }
        cout << endl;
    }
    return 0;
}