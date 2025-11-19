#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int n, s; cin >> n >> s;
        int p = 0;
        for (int i = 0; i < n; i++) {
            int d1, d2, x, y;
            cin >> d1 >> d2 >> x >> y;

            // Check if the ball is moving towards a corner pocket
            // The ball moves at 45 degrees, so it will reach a corner if:
            // (x, y) lies on the line from corner in the direction of (d1, d2)
            // The corners are (0,0), (0,s), (s,0), (s,s)
            // The ball will be potted if it can reach one of these corners by moving along the direction (d1, d2)
            // The ball bounces elastically, so the effective position after reflections can be found by "unfolding" the table.
            // But since the ball moves at 45 degrees, the sum or difference of coordinates remains constant modulo 2*s.

            // The key insight:
            // The ball will be potted if and only if the ball's position lies on the diagonal line that leads to a corner in the given direction.
            // The corners are at (0,0), (0,s), (s,0), (s,s).
            // The ball moves diagonally, so the ball's path is along lines x + y = c or x - y = c.
            // The ball will be potted if the ball's position satisfies:
            // If d1 == d2, then x + y == s or x + y == 0 (but 0 is impossible since 0 < x,y < s)
            // If d1 != d2, then x - y == 0 or x - y == s or -s (depending on direction)
            // But since the ball is inside the table, the only possible pockets reachable are those where the ball's path hits a corner.

            // More simply:
            // The ball will be potted if (d1 == d2 and x + y == s) or (d1 != d2 and x == y)

            if ((d1 == d2 && x + y == s) || (d1 != d2 && x == y)) {
                p++;
            }
        }
        cout << p << "\n";
    }
    return 0;
}