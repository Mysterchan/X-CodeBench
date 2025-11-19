#include <iostream>
#include <algorithm>
using namespace std;

int fi[11];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Precompute Fibonacci cubes sides
    fi[1] = 1;
    fi[2] = 2;
    for (int i = 3; i <= 10; ++i) {
        fi[i] = fi[i - 1] + fi[i - 2];
    }

    int t; cin >> t;
    while (t--) {
        int n, m; cin >> n >> m;

        // Calculate total height needed (sum of all cubes' sides)
        int total_height = 0;
        for (int i = 1; i <= n; ++i) {
            total_height += fi[i];
        }

        // The largest cube side (base cube) must fit in the base area
        int base_side = fi[n];

        // For each box, check if cubes fit:
        // Conditions:
        // 1) The base of the box must be able to hold the largest cube (side fi[n]) in some orientation
        //    i.e. max(fi[n], fi[n]) <= max(w, l) and min(fi[n], fi[n]) <= min(w, l)
        //    Since cubes are squares, just check if min(w,l) >= fi[n]
        // 2) The height of the box must be at least total_height (stacked cubes)
        //
        // Because cubes must be stacked largest to smallest, and placed aligned,
        // the base must fit the largest cube, and height must fit sum of all cubes.

        for (int i = 0; i < m; ++i) {
            int w, l, h; cin >> w >> l >> h;
            int base_min = min(w, l);
            int base_max = max(w, l);

            // Check base fits largest cube
            bool base_fits = (base_min >= base_side);

            // Check height fits total height
            bool height_fits = (h >= total_height);

            cout << (base_fits && height_fits ? '1' : '0');
        }
        cout << '\n';
    }

    return 0;
}