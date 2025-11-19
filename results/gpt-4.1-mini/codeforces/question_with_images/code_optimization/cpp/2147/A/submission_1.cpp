#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        long long x, y;
        cin >> x >> y;

        // If y > x, we can reach in 2 steps: step1 = x (x-axis), step2 = y (y-axis)
        if (y > x) {
            cout << 2 << "\n";
            continue;
        }

        // Check if 3 steps are possible:
        // Steps: a (x), b (y), c (x)
        // Conditions:
        // a + c = x
        // b = y
        // a < b < c
        // => a < y < c
        // => a + c = x and a < y < c
        // So, a < y < x - a
        // => a < y and y < x - a
        // => a < y and a < x - y
        // So a < min(y, x - y)
        // Also a > 0 and c = x - a > y

        // So if min(y, x - y) > 0, then there exists an integer a in (0, min(y, x - y))
        // We just need to check if min(y, x - y) > 0 and y < x

        if (y < x && min(y, x - y) > 0) {
            cout << 3 << "\n";
        } else {
            cout << -1 << "\n";
        }
    }

    return 0;
}