#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int l1, b1, l2, b2, l3, b3;
        cin >> l1 >> b1 >> l2 >> b2 >> l3 >> b3;

        // Since l3 ≤ l2 ≤ l1 and b3 ≤ b2 ≤ b1, we only need to check a few configurations.

        // The side of the square must be equal to the largest length or breadth
        // Check if total area matches a perfect square side^2
        int side = l1;
        bool can_form = false;

        // Check if sum of areas equals side^2
        int total_area = l1 * b1 + l2 * b2 + l3 * b3;
        if (total_area == side * side) {
            // Try to fit rectangles in these patterns:

            // Pattern 1: All three stacked vertically (heights sum to side, widths equal side)
            if (b1 == side && b2 == side && b3 == side && (l1 + l2 + l3) == side)
                can_form = true;

            // Pattern 2: Largest rectangle on top, two smaller rectangles side by side below
            // Check if l1 == side and b1 + max(b2,b3) == side and l2 + l3 == side and b2 == b3
            if (!can_form) {
                if (l1 == side && b1 <= side) {
                    int rem_height = side - b1;
                    if (rem_height > 0) {
                        // Check if l2 + l3 == side and b2 == b3 == rem_height
                        if ((l2 + l3) == side && b2 == b3 && b2 == rem_height)
                            can_form = true;
                    }
                }
            }

            // Pattern 3: Largest rectangle on left, two smaller rectangles stacked vertically on right
            // Check if b1 == side and l1 + max(l2,l3) == side and b2 + b3 == side and l2 == l3
            if (!can_form) {
                if (b1 == side && l1 <= side) {
                    int rem_width = side - l1;
                    if (rem_width > 0) {
                        // Check if b2 + b3 == side and l2 == l3 == rem_width
                        if ((b2 + b3) == side && l2 == l3 && l2 == rem_width)
                            can_form = true;
                    }
                }
            }
        }

        cout << (can_form ? "YES\n" : "NO\n");
    }

    return 0;
}