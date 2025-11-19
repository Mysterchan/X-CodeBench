#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int N = 200001;
int n, q, a[N];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> q;
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    while (q--) {
        int l, r;
        cin >> l >> r;

        ll total = 0;
        int max_count = 0;
        for (int i = l; i <= r; ++i) {
            total += a[i];
            max_count = max(max_count, a[i]);
        }

        // The maximum number of operations we can perform
        // should not exceed half the total available "1s" we can create from all segments
        // and can't exceed the operation limit based on max_count
        ll ans = min(total / 2, (ll)max_count);
        cout << ans << "\n";
    }
}
