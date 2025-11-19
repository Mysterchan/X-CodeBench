#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;

        vector<int> A(n), B(n);
        int countA = 0, countB = 0;

        // Read A and B, while counting the number of 1s.
        for (int i = 0; i < n; ++i) {
            cin >> A[i];
            countA += A[i];
        }
        
        for (int i = 0; i < n; ++i) {
            cin >> B[i];
            countB += B[i];
        }

        // Check if the counts of 1s in both arrays are the same.
        if (countA != countB) {
            cout << "No\n";
            continue;
        }

        // If A and B have the same count of 1s, we can rearrange A to match B.
        cout << "Yes\n";
    }

    return 0;
}
