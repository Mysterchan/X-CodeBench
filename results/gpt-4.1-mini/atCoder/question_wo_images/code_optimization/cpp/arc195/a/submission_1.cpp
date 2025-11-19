#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<int> a(n);
    for (int &x : a) cin >> x;
    vector<int> b(m);
    for (int &x : b) cin >> x;

    // Forward pass: for each position in B, find earliest position in A matching B[i]
    vector<int> forward(m);
    int pos = 0;
    for (int i = 0; i < m; i++) {
        while (pos < n && a[pos] != b[i]) pos++;
        if (pos == n) {
            // No subsequence matches B at all
            cout << "No\n";
            return 0;
        }
        forward[i] = pos++;
    }

    // Backward pass: for each position in B, find latest position in A matching B[i]
    vector<int> backward(m);
    pos = n - 1;
    for (int i = m - 1; i >= 0; i--) {
        while (pos >= 0 && a[pos] != b[i]) pos--;
        if (pos < 0) {
            // No subsequence matches B at all
            cout << "No\n";
            return 0;
        }
        backward[i] = pos--;
    }

    // If there are at least two distinct subsequences, there must be some position i
    // where forward[i] < backward[i], meaning we can pick different positions for B[i]
    for (int i = 0; i < m; i++) {
        if (forward[i] < backward[i]) {
            cout << "Yes\n";
            return 0;
        }
    }

    // If no such position found, only one subsequence matches B
    cout << "No\n";
    return 0;
}