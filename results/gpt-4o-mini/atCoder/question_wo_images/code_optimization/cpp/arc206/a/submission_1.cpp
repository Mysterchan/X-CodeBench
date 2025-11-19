#include <bits/stdc++.h>
using namespace std;

int countDifferentSequences(const vector<int>& A) {
    int n = A.size();
    if (n == 0) return 0;

    set<int> unique_values(A.begin(), A.end());
    int different_sequences = 0;
    
    for (int i = 0; i < n; ++i) {
        for (int j = i; j < n; ++j) {
            if (A[i] != A[j]) {
                different_sequences++;
            }
        }
        different_sequences++;  // counting the case where all values from A[i] to A[j] are the same
    }
    
    // The number of unique sequences resulted by performing the operation
    return different_sequences + unique_values.size(); // counting unique values as distinct sequences
}

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    cout << countDifferentSequences(a);
    return 0;
}
