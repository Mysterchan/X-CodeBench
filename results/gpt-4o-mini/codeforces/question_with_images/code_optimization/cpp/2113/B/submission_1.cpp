#include <iostream>
using namespace std;
using ll = long long;

void solve() {
    ll w, h, a, b;
    cin >> w >> h >> a >> b;

    ll xa, ya, xb, yb;
    cin >> xa >> ya >> xb >> yb;

    // Calculate the effective covered width and height
    ll covered_width = max(xa + a, xb + a) - min(xa, xb);
    ll covered_height = max(ya + b, yb + b) - min(ya, yb);

    // Check if the roof can be completely tiled
    if ((covered_width <= w && covered_height <= h) && 
        (covered_width % a == 0) && 
        (covered_height % b == 0)) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }
}

signed main() {
    ll t;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}