#include <bits/stdc++.h>
using namespace std;

const int N = 2e5 + 5;
int n, k, p[N], deg[N], h[N], cnt[N];
vector<int> adj[N];

void solve() {
    cin >> n >> k;
    for (int i = 1; i <= n; ++i) {
        deg[i] = 0;
        cnt[i] = 0;
        h[i] = 0;
        adj[i].clear();
    }
    for (int i = 2; i <= n; ++i) {
        cin >> p[i];
        deg[p[i]]++;
        adj[p[i]].push_back(i);
    }

    // Compute heights and count nodes at each height
    cnt[0] = 1; // root height 0
    h[1] = 0;
    int mnh = n;
    for (int i = 2; i <= n; ++i) {
        h[i] = h[p[i]] + 1;
        cnt[h[i]]++;
        if (deg[i] == 0) mnh = min(mnh, h[i]);
    }

    // We want to find the maximum length L (<= mnh+1) such that
    // we can assign labels with exactly k zeros and n-k ones,
    // and the longest common subsequence of all leaf names is at least L.

    // The longest common subsequence of all leaf names corresponds to
    // a subsequence of labels on the path from root to leaves.
    // Since all leaves share the prefix up to the minimal leaf height,
    // the maximum length is at most mnh+1.

    // We try to assign zeros and ones to levels 0..mnh to maximize L.
    // For each prefix length i, sum of cnt[0..i-1] nodes must be assigned labels.
    // We want to check if there exists a distribution of zeros and ones
    // on these levels so that total zeros = k and total ones = n-k,
    // and the subsequence of length i is common to all leaves.

    // The problem reduces to subset sum on cnt array for levels 0..mnh.

    // Use bitset for subset sum on cnt[0..mnh]
    static bitset<N> dp;
    dp.reset();
    dp[0] = 1;
    int total = n;
    for (int i = 0; i <= mnh; ++i) {
        dp |= (dp << cnt[i]);
    }

    // For each possible length i (1 to mnh+1),
    // check if there exists x zeros assigned in prefix such that:
    // x in [max(0, k - (n - sum(cnt[0..i-1]))), min(k, sum(cnt[0..i-1]))]
    // and dp[x] == 1 (means sum cnt[i] subset sum to x zeros)
    // If yes, answer = i

    int ans = 0;
    int prefix_sum = 0;
    for (int i = 0; i <= mnh; ++i) {
        prefix_sum += cnt[i];
        int rem = n - prefix_sum;
        int low = max(0, k - rem);
        int high = min(k, prefix_sum);
        // Check if dp has any bit set in [low, high]
        // dp is a bitset where dp[x] = 1 means sum x is achievable
        // We can check dp[low..high] by dp >> low and check if any bit set in first (high - low + 1) bits
        if (low <= high) {
            // Create mask for bits low..high
            // dp >> low shifts dp so bit 0 corresponds to low
            // We check if any bit in [0..high-low] is set
            // Use dp >> low and check if (dp >> low).any() in that range
            // To limit to range, we can mask with ((1ULL << (high - low + 1)) - 1)
            // But bitset doesn't support 64-bit masks directly, so we check by iterating or using test()
            // Since high-low+1 can be large, we do a quick check:
            // We'll check dp.test(x) for x in [low..high]
            // To optimize, we can check dp._Find_first() and dp._Find_next()
            // But since constraints are large, we do a binary search on dp bits.

            // We'll do a binary search for first set bit in [low..high]
            int left = low, right = high;
            bool found = false;
            while (left <= right) {
                int mid = (left + right) / 2;
                if (dp.test(mid)) {
                    found = true;
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            if (found) ans = i + 1;
            else break;
        } else {
            // no valid x
            break;
        }
    }

    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) solve();

    return 0;
}