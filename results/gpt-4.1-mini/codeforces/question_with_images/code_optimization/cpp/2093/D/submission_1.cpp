#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        int q; cin >> q;
        ll size = 1LL << n; // 2^n
        ll total = size * size; // 2^(2n)

        // We implement two functions:
        // getNumber(x, y, n, start) returns the number at cell (x,y)
        // getPos(d, n, start) returns the (x,y) position of number d

        // The filling order of quadrants is:
        // 1) top-left (TL)
        // 2) bottom-right (BR)
        // 3) bottom-left (BL)
        // 4) top-right (TR)

        // Each quadrant is size/2 x size/2, and contains quarter of the numbers.

        // Base case: n=1 (2x2)
        // The 2x2 matrix is:
        // (1,1) = 1
        // (2,2) = 2
        // (2,1) = 3
        // (1,2) = 4

        // We'll implement recursive functions without extra memory.

        function<ll(int,int,int,ll)> getNumber = [&](int x, int y, int level, ll start) -> ll {
            if (level == 1) {
                // 2x2 base case
                // positions:
                // (1,1) -> 1
                // (2,2) -> 2
                // (2,1) -> 3
                // (1,2) -> 4
                if (x == 1 && y == 1) return start + 0;
                if (x == 2 && y == 2) return start + 1;
                if (x == 2 && y == 1) return start + 2;
                if (x == 1 && y == 2) return start + 3;
                // Should never reach here
                return -1;
            }
            ll half = 1LL << (level - 1);
            ll quarter = half * half;
            if (x <= half && y <= half) {
                // top-left
                return getNumber(x, y, level - 1, start);
            } else if (x > half && y > half) {
                // bottom-right
                return getNumber(x - half, y - half, level - 1, start + quarter);
            } else if (x > half && y <= half) {
                // bottom-left
                return getNumber(x - half, y, level - 1, start + 2 * quarter);
            } else {
                // top-right
                return getNumber(x, y - half, level - 1, start + 3 * quarter);
            }
        };

        function<pair<int,int>(ll,int,ll)> getPos = [&](ll d, int level, ll start) -> pair<int,int> {
            if (level == 1) {
                // base case 2x2
                // numbers:
                // start+0 -> (1,1)
                // start+1 -> (2,2)
                // start+2 -> (2,1)
                // start+3 -> (1,2)
                ll offset = d - start;
                if (offset == 0) return {1,1};
                if (offset == 1) return {2,2};
                if (offset == 2) return {2,1};
                if (offset == 3) return {1,2};
                // Should never reach here
                return {-1,-1};
            }
            ll half = 1LL << (level - 1);
            ll quarter = half * half;
            if (d < start + quarter) {
                // top-left
                return getPos(d, level - 1, start);
            } else if (d < start + 2 * quarter) {
                // bottom-right
                auto p = getPos(d, level - 1, start + quarter);
                return {p.first + (int)half, p.second + (int)half};
            } else if (d < start + 3 * quarter) {
                // bottom-left
                auto p = getPos(d, level - 1, start + 2 * quarter);
                return {p.first + (int)half, p.second};
            } else {
                // top-right
                auto p = getPos(d, level - 1, start + 3 * quarter);
                return {p.first, p.second + (int)half};
            }
        };

        while (q--) {
            string s; cin >> s;
            if (s == "->") {
                int x,y; cin >> x >> y;
                cout << getNumber(x,y,n,1) << "\n";
            } else {
                ll d; cin >> d;
                auto p = getPos(d,n,1);
                cout << p.first << " " << p.second << "\n";
            }
        }
    }

    return 0;
}