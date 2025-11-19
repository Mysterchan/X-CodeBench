#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const int N = 200000 + 10;

int n, q;
ll a[N];
ll prefix_sum[N];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> q;
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        prefix_sum[i] = prefix_sum[i - 1] + a[i];
    }

    while (q--) {
        int l, r;
        cin >> l >> r;
        ll total = prefix_sum[r] - prefix_sum[l - 1];
        // The maximum number of operations is floor(total / 2)
        cout << total / 2 << "\n";
    }

    return 0;
}