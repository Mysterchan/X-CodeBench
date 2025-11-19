#include <iostream>
using namespace std;
using ll = long long;

void solve() {
    ll w, h, a, b;
    cin >> w >> h >> a >> b;

    ll xa, ya, xb, yb;
    cin >> xa >> ya >> xb >> yb;

    // Check if the two placed sheets align in a way that allows tiling
    // without rotation and without overlap, covering the entire roof.

    // Condition 1: vertical alignment
    // If x-coordinates differ by multiple of a, and either same x or y differ by multiple of b
    bool ver = false;
    if ((abs(xa - xb) % a) == 0) {
        if (xa == xb) {
            if ((abs(ya - yb) % b) == 0)
                ver = true;
        } else {
            ver = true;
        }
    }

    // Condition 2: horizontal alignment
    // If y-coordinates differ by multiple of b, and either same y or x differ by multiple of a
    bool hor = false;
    if ((abs(ya - yb) % b) == 0) {
        if (ya == yb) {
            if ((abs(xa - xb) % a) == 0)
                hor = true;
        } else {
            hor = true;
        }
    }

    cout << (hor || ver ? "Yes\n" : "No\n");
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) solve();

    return 0;
}