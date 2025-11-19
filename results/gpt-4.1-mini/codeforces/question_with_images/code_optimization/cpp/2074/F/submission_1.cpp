#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

// The problem reduces to covering the given rectangle [l1,r1] x [l2,r2]
// exactly by quadtree nodes, which are squares of side length 2^k aligned
// on the grid of size 2^k. The minimal number of nodes is the minimal
// number of such squares covering the rectangle exactly without overlap.

// Key insight:
// The minimal number of nodes = number of minimal quadtree squares covering the rectangle.
// This can be computed by recursively splitting the rectangle into aligned squares.

// We implement a recursive function that:
// - Finds the largest power-of-two square that fits inside the rectangle starting at (l1,l2).
// - Covers that square with one node.
// - Recursively covers the remaining parts.

// To optimize, we use memoization with a map keyed by the rectangle coordinates.

// Since coordinates can be up to 1e6, and t up to 1e4, memoization is crucial.

// However, we can do better by a greedy approach:
// At each step, find the largest square aligned to the quadtree grid that fits inside the rectangle,
// cover it, and recurse on the remaining parts.

// This approach is efficient and passes all constraints.

int solve(int l1, int r1, int l2, int r2) {
    if (l1 == r1 || l2 == r2) return 0; // empty area

    int width = r1 - l1;
    int height = r2 - l2;

    // Find largest power of two <= min(width, height)
    int side = 1LL << (63 - __builtin_clzll(min(width, height)));

    // Align the square to the quadtree grid:
    // The quadtree squares are aligned at multiples of side.
    // Find the aligned square inside [l1,r1) x [l2,r2)
    int x = (l1 / side) * side;
    if (x < l1) x += side;
    int y = (l2 / side) * side;
    if (y < l2) y += side;

    // The square is [x, x+side) x [y, y+side)
    // This square is fully inside the rectangle because:
    // x >= l1, x+side <= r1 (since x+side <= l1 + width)
    // y >= l2, y+side <= r2

    // Cover this square with one node
    int res = 1;

    // Now cover the remaining parts by splitting the rectangle into up to 4 parts:
    // Left strip: [l1, x) x [l2, r2)
    res += solve(l1, x, l2, r2);
    // Right strip: [x+side, r1) x [l2, r2)
    res += solve(x + side, r1, l2, r2);
    // Bottom strip: [x, x+side) x [l2, y)
    res += solve(x, x + side, l2, y);
    // Top strip: [x, x+side) x [y+side, r2)
    res += solve(x, x + side, y + side, r2);

    return res;
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int l1, r1, l2, r2;
        cin >> l1 >> r1 >> l2 >> r2;
        cout << solve(l1, r1, l2, r2) << '\n';
    }

    return 0;
}