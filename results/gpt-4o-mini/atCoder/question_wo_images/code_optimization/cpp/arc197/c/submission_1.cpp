#include <bits/stdc++.h>
using namespace std;

const int MAX = 3000000;
bitset<MAX + 1> removed;  // To track removed multiples
vector<int> result;        // To collect results to output
vector<int> S;            // To maintain the list of remaining elements

void initialize() {
    for (int i = 1; i <= MAX; ++i) {
        if (!removed[i]) {
            S.push_back(i);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int q;
    cin >> q;
    initialize();  // Initialize the remaining elements in S

    while (q--) {
        int a, b;
        cin >> a >> b;
        
        // Mark multiples of a as removed
        for (int multiple = a; multiple <= MAX; multiple += a) {
            removed[multiple] = true;
        }
        
        // Find and print the b-th smallest remaining element
        int count = 0;
        for (int i = 1; i <= MAX; ++i) {
            if (!removed[i]) {
                count++;
                if (count == b) {
                    result.push_back(i);
                    break;
                }
            }
        }
    }

    // Output all results
    for (int res : result) {
        cout << res << '\n';
    }

    return 0;
}
