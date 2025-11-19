#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while (T--) {
        int n; cin >> n;
        vector<int> a(n);
        for (auto &x : a) cin >> x;

        // Sort ascending
        sort(a.begin(), a.end());

        // Compute prefix sums
        vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + a[i];

        int ans = 0;

        // For each starting index i, binary search max j > i
        // such that average of a[i..j-1] < a[j]
        // i.e. (prefix[j] - prefix[i]) / (j - i) < a[j]
        // => (prefix[j] - prefix[i]) < a[j] * (j - i)
        for (int i = 0; i < n; i++) {
            int low = i + 1, high = n;
            int res = i;
            while (low < high) {
                int mid = (low + high) / 2;
                long long sum_sub = prefix[mid] - prefix[i];
                int len = mid - i;
                if (sum_sub < (long long)a[mid] * len) {
                    res = mid;
                    low = mid + 1;
                } else {
                    high = mid;
                }
            }
            // Score = number of elements > average = (res - i)
            // Update answer
            ans = max(ans, res - i);
        }

        cout << ans << "\n";
    }
}