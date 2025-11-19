#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> S(N);
    int max_val = 0;
    for (int i = 0; i < N; i++) {
        cin >> S[i];
        if (S[i] > max_val) max_val = S[i];
    }

    // Use a boolean vector to mark presence of elements for O(1) lookup
    vector<bool> present(max_val + 1, false);
    for (int x : S) present[x] = true;

    // Sort the array for ordered traversal
    sort(S.begin(), S.end());

    long long count = 0;
    // For each pair (A, B), check if C = 2*B - A exists
    // Since S is sorted, we can break early if C > max_val
    for (int i = 0; i < N; i++) {
        int A = S[i];
        for (int j = i + 1; j < N; j++) {
            int B = S[j];
            int C = 2 * B - A;
            if (C > max_val) break; // no need to check further
            if (present[C]) count++;
        }
    }

    cout << count << "\n";
    return 0;
}