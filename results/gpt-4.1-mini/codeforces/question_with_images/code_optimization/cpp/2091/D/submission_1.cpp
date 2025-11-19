#include <bits/stdc++.h>
using namespace std;

using ll = long long;

void solve() {
    ll n, m, k;
    cin >> n >> m >> k;

    // Minimum possible max bench length is at least ceil(k/n)
    ll a = (k + n - 1) / n;

    if (a >= m) {
        // If a >= m, the bench length can't be less than a
        cout << a << "\n";
        return;
    }

    // We want to find minimal bench length l (1 <= l <= a)
    // such that we can arrange k desks in n rows with max bench length l
    // and total spots per row m.

    // The number of benches per row = ceil(m / l)
    // Total benches = n * ceil(m / l)
    // Each bench can hold up to l desks, so total capacity = n * ceil(m / l) * l
    // But since benches are consecutive desks, the arrangement is more subtle.
    //
    // The problem reduces to:
    // For a given bench length l, can we seat k participants so that no bench length > l?
    //
    // The original code tries all i from 1 to m, but that's too slow.
    //
    // We can binary search on l in [1, a].

    ll left = 1, right = a, ans = a;

    while (left <= right) {
        ll mid = (left + right) / 2;

        // Number of benches per row = ceil(m / mid)
        ll benches_per_row = (m + mid - 1) / mid;

        // Total benches = n * benches_per_row
        // Max desks per bench = mid
        // Total capacity = n * benches_per_row * mid

        // But total capacity >= n * m (all seats), so no problem.

        // We want to check if we can seat k participants with max bench length mid.

        // The minimal number of benches needed to seat k participants with bench length mid:
        // benches_needed = ceil(k / mid)

        // If benches_needed <= total benches (n * benches_per_row), then mid is feasible.

        ll benches_needed = (k + mid - 1) / mid;
        ll total_benches = n * benches_per_row;

        if (benches_needed <= total_benches) {
            ans = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}