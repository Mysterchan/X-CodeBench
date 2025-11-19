#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve() {
    ll n, m, k;
    cin >> n >> m >> k;

    // Calculate the minimum possible length of the longest bench
    ll low = 1, high = m, best = m;

    while (low <= high) {
        ll mid = low + (high - low) / 2;
        // Calculate the total desks that can be fit with longest bench of length mid
        ll total = 0;

        if (mid > 0) {
            total = (mid * (mid + 1)) / 2; // Total desks in one row if max bench length is mid
            total *= n; // Total desks in n rows
        }

        if (total >= k) {
            best = mid; // It is possible to arrange in this configuration
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << best << "\n";
}

int main() {
    ll t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}