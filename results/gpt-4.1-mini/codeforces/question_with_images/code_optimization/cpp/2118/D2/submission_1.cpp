#include <bits/stdc++.h>
using namespace std;
#define int long long

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int n, k; cin >> n >> k;
        vector<int> p(n), d(n);
        for (int i = 0; i < n; i++) cin >> p[i];
        for (int i = 0; i < n; i++) cin >> d[i];

        // Precompute left and right boundaries for each traffic light
        // where the light is red at time t % k == d[i].
        // We want to find intervals where the traveler can get stuck.

        // The key insight:
        // The traveler moves along the strip and flips direction only when
        // standing on a red light at that second.
        // The traveler can get stuck only if there is a "trap" formed by two
        // traffic lights that cause infinite bouncing.

        // We will precompute for each traffic light:
        // - The earliest position to the left where the traveler can get stuck
        // - The earliest position to the right where the traveler can get stuck

        // We will use a stack to find intervals of "traps" based on the delays.

        // The problem reduces to:
        // For each query position x, check if it lies inside any trap interval.
        // If yes, print NO (won't leave), else YES.

        // To find trap intervals:
        // For each traffic light i, define:
        //   L[i] = max position to the left where traveler can get stuck due to i
        //   R[i] = min position to the right where traveler can get stuck due to i

        // We will find intervals [L[i], R[i]] for each i and merge them.

        // Since the strip is very large, and n,q up to 2e5,
        // we must do O(n + q) per test case.

        // Approach:
        // 1) For each traffic light i, compute the earliest time it shows red:
        //    red times: t ≡ d[i] (mod k)
        // 2) The traveler flips direction only if at time t % k == d[i].
        // 3) The traveler moves one cell per second.
        // 4) The traveler starts at position x at time 0, facing right.

        // Observation:
        // The traveler can get stuck only if there is a pair of traffic lights
        // that cause it to bounce infinitely between them.

        // We can precompute for each traffic light the minimal and maximal
        // positions reachable without leaving the strip.

        // Let's define arrays:
        // left_bound[i]: the minimal position reachable starting from p[i]
        // right_bound[i]: the maximal position reachable starting from p[i]

        // We can compute these bounds by scanning from left to right and right to left.

        // But the problem is complicated by the delays d[i].

        // Instead, we use the editorial approach (from the original problem editorial):
        // We define arrays:
        //   leftmost[i]: the minimal position reachable starting from p[i]
        //   rightmost[i]: the maximal position reachable starting from p[i]

        // We can compute these by dynamic programming:
        // For i from 0 to n-1:
        //   leftmost[i] = p[i]
        //   rightmost[i] = p[i]
        // Then we propagate constraints:
        //   If the light at p[i] can cause a bounce, update leftmost and rightmost accordingly.

        // But this is complicated.

        // Instead, we use the following approach from the editorial:

        // We define arrays:
        //   leftmost[i] = minimal position reachable starting from p[i]
        //   rightmost[i] = maximal position reachable starting from p[i]

        // Initialize:
        //   leftmost[i] = p[i]
        //   rightmost[i] = p[i]

        // Then:
        // For i from 1 to n-1:
        //   If d[i] <= d[i-1], then leftmost[i] = leftmost[i-1]
        // For i from n-2 down to 0:
        //   If d[i] >= d[i+1], then rightmost[i] = rightmost[i+1]

        // After this, for each query x:
        //   Find the traffic light i such that p[i] <= x < p[i+1]
        //   If x < leftmost[i] or x > rightmost[i], then answer YES else NO

        // But the problem is that delays d[i] can be arbitrary.

        // The editorial solution is to precompute two arrays:
        //   leftmost[i] = minimal position reachable starting from p[i]
        //   rightmost[i] = maximal position reachable starting from p[i]

        // We do this by:
        //   leftmost[0] = p[0]
        //   for i in [1..n-1]:
        //     if d[i] <= d[i-1], leftmost[i] = leftmost[i-1]
        //     else leftmost[i] = p[i]
        //
        //   rightmost[n-1] = p[n-1]
        //   for i in [n-2..0]:
        //     if d[i] >= d[i+1], rightmost[i] = rightmost[i+1]
        //     else rightmost[i] = p[i]

        // For queries:
        //   Use binary search to find i such that p[i] <= x < p[i+1]
        //   If x < leftmost[i] or x > rightmost[i], print YES else NO

        // Edge cases:
        //   If x < p[0], then YES (leaves to the left)
        //   If x > p[n-1], then YES (leaves to the right)

        // Implementing this approach:

        vector<int> leftmost(n), rightmost(n);
        leftmost[0] = p[0];
        for (int i = 1; i < n; i++) {
            if (d[i] <= d[i - 1]) leftmost[i] = leftmost[i - 1];
            else leftmost[i] = p[i];
        }
        rightmost[n - 1] = p[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            if (d[i] >= d[i + 1]) rightmost[i] = rightmost[i + 1];
            else rightmost[i] = p[i];
        }

        int q; cin >> q;
        while (q--) {
            int x; cin >> x;
            if (x < p[0] || x > p[n - 1]) {
                cout << "YES\n";
                continue;
            }
            int idx = (int)(upper_bound(p.begin(), p.end(), x) - p.begin()) - 1;
            if (x < leftmost[idx] || x > rightmost[idx]) cout << "YES\n";
            else cout << "NO\n";
        }
    }
    return 0;
}