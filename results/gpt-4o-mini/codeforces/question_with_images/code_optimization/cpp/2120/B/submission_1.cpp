#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, s;
        cin >> n >> s;
        int p = 0;
        for (int i = 0; i < n; i++) {
            int dx, dy, x, y;
            cin >> dx >> dy >> x >> y;

            if (dx == 1) {
                // moving right
                x = s - x;
            }
            if (dy == 1) {
                // moving up
                y = s - y;
            }

            // Check if the ball eventually goes into a pocket
            if (dx == 1 && dy == 1 && x == y) {
                p++;
            } else if (dx == 1 && dy == -1 && x + y == s) {
                p++;
            } else if (dx == -1 && dy == 1 && x + y == s) {
                p++;
            } else if (dx == -1 && dy == -1 && x == y) {
                p++;
            }
        }
        cout << p << endl;
    }
    return 0;
}