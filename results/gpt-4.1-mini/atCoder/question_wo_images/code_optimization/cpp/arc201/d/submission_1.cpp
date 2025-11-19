#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    // The sum of N over all test cases is at most 3*10^5,
    // so we can safely allocate arrays once.
    static int A[300000], B[300000];

    while (T--) {
        int N; long long M;
        cin >> N >> M;
        for (int i = 0; i < N; i++) cin >> A[i];
        for (int i = 0; i < N; i++) cin >> B[i];

        // Sort A ascending
        sort(A, A + N);
        // Sort B ascending
        sort(B, B + N);

        // We want to minimize max((A_i + B_i) mod M)
        // by rearranging A arbitrarily.

        // Key insight:
        // For each B_i, to minimize (A_i + B_i) mod M,
        // we want A_i to be as close as possible to (M - B_i) mod M.
        // So for each B_i, find the smallest A_j >= (M - B_i) mod M.
        // If none, take the smallest A_j.

        // We'll use binary search on A to find the suitable element for each B_i.

        // To do this efficiently, we can:
        // - For each B_i, compute target = (M - B_i) % M
        // - Use lower_bound on A to find the first element >= target
        // - If found, assign that A element to B_i
        // - Else assign the smallest A element

        // To avoid modifying A array, we can use a multiset or a balanced structure.
        // But multiset insert/erase is O(log N), total O(N log N) which is acceptable.

        // However, since sum of N is large, we want to avoid overhead.
        // Instead, we can use a pointer approach:
        // We'll store A in a multiset or use a balanced tree structure.

        // But since we need to assign each A element exactly once,
        // and we want to do it efficiently, we can do the following:

        // Use a balanced tree structure: multiset<int> for A
        multiset<int> sa(A, A + N);

        long long ans = 0;
        for (int i = 0; i < N; i++) {
            long long target = (M - B[i]) % M;
            auto it = sa.lower_bound((int)target);
            if (it == sa.end()) it = sa.begin();
            long long val = *it;
            sa.erase(it);
            long long cur = (val + B[i]) % M;
            if (cur > ans) ans = cur;
        }

        cout << ans << "\n";
    }

    return 0;
}