#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> A(n), B(n);
    int countNegA = 0, countNegB = 0, totalA = 0, totalB = 0;

    for (int i = 0; i < n; i++) {
        cin >> A[i];
        if (A[i] == -1) countNegA++;
        else totalA += A[i];
    }

    for (int i = 0; i < n; i++) {
        cin >> B[i];
        if (B[i] == -1) countNegB++;
        else totalB += B[i];
    }

    int requiredPairs = n - countNegA - countNegB; // Number of pairs we can form without -1

    // If we have enough -1s to replace and match the pairs
    if (countNegA + countNegB >= n) {
        cout << "Yes" << endl;
        return 0;
    }

    // Calculate the necessary constant to equalize the sums
    int totalRequired = totalA + totalB + countNegA + countNegB;

    // We check if the remaining values can form a valid equal sum S
    // which would be totalRequired / n, if totalRequired % n == 0
    if (totalRequired % n == 0) {
        int S = totalRequired / n;
        // If S is less than the maximum possible value that can be formed
        // with the current values and negated values, it’s possible
        int canForm = 0;
        for (int i = 0; i < n; i++) {
            if (A[i] != -1) canForm += A[i];
            if (B[i] != -1) canForm += B[i];
        }
        if (canForm + (countNegA + countNegB) >= S * n) {
            cout << "Yes" << endl;
            return 0;
        }
    }

    cout << "No" << endl;
    return 0;
}
