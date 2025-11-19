#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    int sum = 0; // to count number of 1's
    bool canMakeGood = false;

    for (int i = 0; i < n; i++) {
        cin >> a[i];
        if (a[i]) sum++;
    }

    // If we have no zeros, the answer is yes.
    if (sum == n) {
        cout << "Yes" << endl;
        return 0;
    }

    // Check for adjacent pairs of 1's
    for (int i = 0; i < n; i++) {
        if (a[i] == 1) {
            if (a[(i + 1) % n] == 1 || a[(i + 2) % n] == 1) {
                canMakeGood = true;
                break;
            }
        }
    }

    // Determine if a good string can be formed based on pattern
    if (n % 4 == 0 || (sum > 0 && (n % 4 == 1 || n % 4 == 3)) || (canMakeGood && n % 4 == 2)) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

    return 0;
}
