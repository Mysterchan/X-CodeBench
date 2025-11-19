#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false), cin.tie(0);
    
    int n;
    cin >> n;
    vector<int> a(n);
    
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int pairs = 0;
    int j = 0; // Pointer for larger mochi
    for (int i = 0; i < n; i++) {
        // Move j to find a suitable mochi that can be paired with i
        while (j < n && a[j] < 2 * a[i]) {
            j++;
        }
        // If j is within bounds and is greater than i, we have found a pair
        if (j < n && j > i) {
            pairs++;
            j++; // Move j forward to not reuse the same mochi
        }
    }

    cout << pairs << endl;
    return 0;
}