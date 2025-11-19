#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        ll px, py, qx, qy; cin >> px >> py >> qx >> qy;
        vector<int> a(n);
        ll sum = 0;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            sum += a[i];
        }

        ll dist_sq = (px - qx) * (px - qx) + (py - qy) * (py - qy);

        // The minimal possible distance after all moves is:
        // max(0, sum - 2 * max(a_i))
        // Because we can arrange moves to cancel out the largest move partially or fully.
        int max_a = *max_element(a.begin(), a.end());
        ll min_dist = sum - 2LL * max_a;
        if (min_dist < 0) min_dist = 0;

        // Check if dist_sq is between min_dist^2 and sum^2
        // Use 64-bit multiplication carefully
        ll min_dist_sq = min_dist * min_dist;
        ll max_dist_sq = sum * sum;

        if (min_dist_sq <= dist_sq && dist_sq <= max_dist_sq) {
            cout << "Yes\n";
        } else {
            cout << "No\n";
        }
    }
}