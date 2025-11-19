#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];

    // We want to compute sum over all subarrays f(L,R),
    // where f(L,R) = number of connected components in the set of distinct values in A[L..R].
    //
    // The original code is O(N^3) roughly, too slow.
    //
    // Key insight:
    // f(L,R) = number of connected components in the set of distinct values in A[L..R].
    // Connected components are formed by consecutive integers present in the subarray.
    //
    // We can rewrite f(L,R) = 1 + number_of_gaps,
    // where a gap is a pair of consecutive integers (x, x+1) such that x and x+1 are both in A[L..R].
    //
    // Actually, number_of_components = number_of_present_intervals,
    // which equals 1 + number_of_gaps (where gap means a missing integer between present integers).
    //
    // But the original code counts components by scanning from min_val to max_val.
    //
    // Another way:
    // number_of_components = number_of_present_intervals
    // = number_of_present_values - number_of_adjacent_pairs_present
    //
    // Because each adjacency reduces components by 1.
    //
    // So:
    // f(L,R) = number_of_distinct_values_in_subarray - number_of_adjacent_pairs_in_subarray
    //
    // where adjacent pairs are pairs (x, x+1) both present in subarray.
    //
    // So sum f(L,R) = sum over all subarrays of (distinct_count - adjacent_pairs_count)
    // = sum distinct_count over all subarrays - sum adjacent_pairs_count over all subarrays
    //
    // We can compute:
    // 1) sum of distinct counts over all subarrays
    // 2) sum of adjacent pairs counts over all subarrays
    //
    // Then subtract.
    //
    // Computing sum of distinct counts over all subarrays:
    // Standard approach: two pointers + frequency array.
    //
    // Computing sum of adjacent pairs counts over all subarrays:
    // For each adjacent pair (x, x+1), count in how many subarrays both x and x+1 appear.
    //
    // So we need to:
    // - For each value v, store positions of v in A.
    // - For each adjacent pair (v, v+1), merge their positions and count subarrays containing both.
    //
    // Then sum over all adjacent pairs.
    //
    // Finally answer = sum_distinct - sum_adjacent_pairs.

    // Step 1: sum of distinct counts over all subarrays
    vector<int> freq(N + 2, 0);
    long long sum_distinct = 0;
    int distinct = 0;
    int r = 0;
    for (int l = 0; l < N; l++) {
        while (r < N && (freq[A[r]] == 0 || true)) {
            freq[A[r]]++;
            if (freq[A[r]] == 1) distinct++;
            r++;
        }
        sum_distinct += distinct;
        freq[A[l]]--;
        if (freq[A[l]] == 0) distinct--;
    }

    // Step 2: sum of adjacent pairs counts over all subarrays
    // For each value v, store sorted positions of v
    vector<vector<int>> pos(N + 2);
    for (int i = 0; i < N; i++) {
        pos[A[i]].push_back(i);
    }

    // Function to count number of subarrays containing both values in two sorted arrays
    // We use two pointers to count number of subarrays containing both values.
    // For each pair of positions (p in pos[v], q in pos[v+1]), subarrays containing both must cover [min(p,q), max(p,q)].
    // The number of subarrays containing both is:
    // (min(p,q) + 1) * (N - max(p,q))
    //
    // We sum over all pairs (p,q).
    //
    // To do this efficiently, we use two pointers and prefix sums.

    long long sum_adjacent_pairs = 0;

    for (int v = 1; v < N + 1; v++) {
        if (pos[v].empty() || pos[v + 1].empty()) continue;

        const auto &P = pos[v];
        const auto &Q = pos[v + 1];
        int m = (int)P.size();
        int n = (int)Q.size();

        // Precompute prefix sums for Q:
        // prefix_q[i] = sum of Q[0..i-1]
        vector<long long> prefix_q(n + 1, 0);
        for (int i = 0; i < n; i++) prefix_q[i + 1] = prefix_q[i] + Q[i];

        // For each p in P, find how many q in Q are <= p
        // For q <= p:
        // subarrays count contribution = (q+1)*(N - p)
        // For q > p:
        // subarrays count contribution = (p+1)*(N - q)

        int idx = 0;
        for (int i = 0; i < m; i++) {
            int p = P[i];
            // Find number of q in Q with q <= p
            // upper_bound returns first q > p
            int ub = (int)(std::upper_bound(Q.begin(), Q.end(), p) - Q.begin());

            // q <= p: indices [0, ub-1]
            // q > p: indices [ub, n-1]

            // sum over q <= p: sum (q+1)*(N - p)
            // = (N - p) * sum_{q <= p} (q+1)
            long long sum_q_le_p = 0;
            if (ub > 0) {
                // sum of q+1 for q in Q[0..ub-1]
                // sum_q = prefix_q[ub] + ub (since q+1 = q + 1)
                // Actually prefix_q stores sum of q, so sum of q+1 = prefix_q[ub] + ub
                sum_q_le_p = (long long)(N - p) * (prefix_q[ub] + ub);
            }

            // sum over q > p: sum (p+1)*(N - q)
            // = (p+1) * sum_{q > p} (N - q)
            // = (p+1) * ( (n - ub)*N - sum_{q > p} q )
            long long sum_q_gt_p = 0;
            if (ub < n) {
                long long sum_q_gt = prefix_q[n] - prefix_q[ub];
                sum_q_gt_p = (long long)(p + 1) * ((long long)(n - ub) * N - sum_q_gt);
            }

            sum_adjacent_pairs += sum_q_le_p + sum_q_gt_p;
        }
    }

    // Final answer
    // f(L,R) = distinct_count - adjacent_pairs_count
    // sum f(L,R) = sum_distinct - sum_adjacent_pairs
    cout << sum_distinct - sum_adjacent_pairs << "\n";

    return 0;
}