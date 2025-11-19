#include <bits/stdc++.h>
using namespace std;
#define int long long
#define fastIO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

signed main() {
    fastIO
    int t;
    cin >> t;
    while (t--) {
        int l, r, d, u;
        cin >> l >> r >> d >> u;
        // Check if the lengths between opposite points are equal
        if (l == r && d == u || l == d && r == u) {
            cout << "Yes\n";
        } else {
            cout << "No\n";
        }
    }
    return 0;
}