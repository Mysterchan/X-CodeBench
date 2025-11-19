#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int l, r, d, u;
        cin >> l >> r >> d >> u;
        // The points are (-l,0), (r,0), (0,-d), (0,u)
        // For these points to form a square:
        // The distance between L and R = l + r
        // The distance between D and U = d + u
        // Both must be equal for a square (side length)
        // Also, since points are on axes, the shape is a square iff l+r == d+u
        cout << (l + r == d + u ? "Yes\n" : "No\n");
    }
    return 0;
}