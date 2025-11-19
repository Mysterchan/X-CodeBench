#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    // sum of N over all test cases <= 2*10^5
    while (T--) {
        int n; cin >> n;
        vector<int> A(n), B(n);
        int sumA = 0, sumB = 0;
        for (int i = 0; i < n; i++) {
            cin >> A[i];
            sumA += A[i];
        }
        for (int i = 0; i < n; i++) {
            cin >> B[i];
            sumB += B[i];
        }

        // If total number of 1s differ, impossible
        if (sumA != sumB) {
            cout << "No\n";
            continue;
        }

        // If sequences are already equal
        if (A == B) {
            cout << "Yes\n";
            continue;
        }

        // If all zeros or all ones, no rearrangement possible
        if (sumA == 0 || sumA == n) {
            // Since A != B and no 1s or all 1s, no way to rearrange
            cout << "No\n";
            continue;
        }

        // Otherwise, answer is Yes
        cout << "Yes\n";
    }

    return 0;
}