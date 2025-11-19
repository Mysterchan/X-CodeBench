#include <bits/stdc++.h>
using namespace std;
#define int long long

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N; cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];

    // If N is even:
    // The maximum total score is sum of first N/2 largest elements minus sum of N/2 smallest elements.
    // This corresponds to pairing largest with smallest to maximize absolute differences.
    if (N % 2 == 0) {
        sort(A.rbegin(), A.rend());
        int M = N / 2;
        int64_t ans = 0;
        for (int i = 0; i < M; i++) ans += A[i];
        for (int i = N - M; i < N; i++) ans -= A[i];
        cout << ans << "\n";
        return 0;
    }

    // If N is odd:
    // We must remove one element first (which will remain unpaired).
    // Try removing each element and compute the max score for the remaining even-length sequence.
    // To optimize, we pre-sort the array and try removing each element in sorted order.
    // But this is O(N^2) if done naively.
    // Instead, we use a prefix and suffix sums approach.

    // Sort the array
    sort(A.begin(), A.end());

    // Precompute prefix sums
    vector<int64_t> prefix(N + 1, 0);
    for (int i = 0; i < N; i++) prefix[i + 1] = prefix[i] + A[i];

    // For even length sequences, max score = sum of top half - sum of bottom half
    // For odd length, after removing one element, length = N-1 (even)
    // We try removing each element and compute:
    // sum of largest (N-1)/2 elements - sum of smallest (N-1)/2 elements in the remaining array

    int M = (N - 1) / 2;
    int64_t ans = 0;

    // To efficiently compute sums after removing A[i], we consider two parts:
    // The array without A[i] is A[0..i-1] + A[i+1..N-1]
    // We want to pick M largest and M smallest from this array.

    // Since the array is sorted, the smallest elements are from the start,
    // largest elements are from the end.

    // We try all i, and for each:
    // - The smallest M elements come from the first M elements of the array excluding A[i].
    // - The largest M elements come from the last M elements of the array excluding A[i].

    // But removing A[i] shifts indices, so we handle carefully.

    // We'll try two cases for each i:
    // Case 1: The removed element is in the smallest M elements
    // Case 2: The removed element is in the largest M elements
    // Case 3: The removed element is in the middle (not in smallest or largest M elements)

    // For each i:
    // smallest M elements after removal:
    // if i < M: smallest M elements = A[0..M] excluding A[i] (so M elements)
    // else: smallest M elements = A[0..M-1]

    // largest M elements after removal:
    // if i >= N - M: largest M elements = A[N-M-1..N-1] excluding A[i]
    // else: largest M elements = A[N-M..N-1]

    // We'll compute sums accordingly.

    for (int i = 0; i < N; i++) {
        // sum_smallest: sum of smallest M elements after removing A[i]
        int64_t sum_smallest = 0;
        if (i < M) {
            // smallest M elements are A[0..M], remove A[i]
            // sum of A[0..M] - A[i]
            sum_smallest = prefix[M + 1] - A[i];
        } else {
            // smallest M elements are A[0..M-1]
            sum_smallest = prefix[M];
        }

        // sum_largest: sum of largest M elements after removing A[i]
        if (i >= N - M) {
            // largest M elements are A[N-M-1..N-1], remove A[i]
            // sum of A[N-M-1..N-1] - A[i]
            sum_largest = prefix[N] - prefix[N - M - 1] - A[i];
        } else {
            // largest M elements are A[N-M..N-1]
            sum_largest = prefix[N] - prefix[N - M];
        }

        int64_t cur = sum_largest - sum_smallest;
        if (cur > ans) ans = cur;
    }

    cout << ans << "\n";
    return 0;
}