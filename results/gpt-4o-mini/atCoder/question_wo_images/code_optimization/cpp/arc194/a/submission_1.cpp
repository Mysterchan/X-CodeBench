#include <bits/stdc++.h>
using namespace std;
using ll = long long;

void solve() {
    int n;
    cin >> n;
    vector<ll> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    
    ll max_sum = 0; // This will hold the maximum possible sum
    ll current_sum = 0; // This will hold the sum if we choose to append elements to S

    for (int i = 0; i < n; ++i) {
        if (a[i] > 0) {
            current_sum += a[i]; // Only add positive numbers
        } else if (current_sum + a[i] > 0) {
            current_sum += a[i]; // Only add negative numbers if it doesn't drop sum below zero
        }
        max_sum = max(max_sum, current_sum); // Keep track of maximum sum
    }

    cout << max_sum << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}
