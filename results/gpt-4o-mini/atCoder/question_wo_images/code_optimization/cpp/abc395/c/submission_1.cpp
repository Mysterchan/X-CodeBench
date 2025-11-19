#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    unordered_map<int, int> lastIndex;
    int minLength = N + 1;

    for (int i = 0; i < N; i++) {
        if (lastIndex.find(A[i]) != lastIndex.end()) {
            // The length of the subarray is the current index minus the last index of the repeated value plus one.
            minLength = min(minLength, i - lastIndex[A[i]] + 1);
        }
        lastIndex[A[i]] = i; // update the last index of the current value
    }

    if (minLength == N + 1) {
        cout << -1; // No repeated subarray found
    } else {
        cout << minLength; // Output the length of the shortest subarray
    }

    return 0;
}
