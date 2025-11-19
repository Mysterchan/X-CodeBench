#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        vector<int> A(N);
        for (int i = 0; i < N; ++i) {
            cin >> A[i];
        }

        sort(A.begin(), A.end());
        ll insertions = 0;
        int expected = 0;  // Initialize expected value to 0

        for (int i = 0; i < N; ++i) {
            if (A[i] > expected) {
                insertions += (A[i] - expected);  // Count how many we need to insert to reach A[i]
            }
            expected = max(expected, A[i]) + 1;  // Update expected to the next number after A[i]
        }

        cout << insertions << '\n';
    }

    return 0;
}
