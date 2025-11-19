#include <bits/stdc++.h>
using namespace std;

void solve() {
    long long n, x, y, vx, vy; 
    cin >> n >> x >> y >> vx >> vy;

    // Check if the airplane is moving towards the vertex
    bool canEscape = false;
    int hits = 0;

    // Check if it can escape directly to (0, 0)
    if (vx > 0 && vy > 0) {
        // Check if moving towards (0, 0)
        if (x + vx * (n - x) / vx > n) canEscape = true;
        if (y + vy * (n - y) / vy > n) canEscape = true;
    }
    // Check if it can escape directly to (0, n)
    if (vx < 0 && vy > 0) {
        // Change the motion direction for the boundary check
        hits++;
        vx = -vx; vy = -vy; // Reflect velocity
    }
    // Check if it can escape directly to (n, 0)
    if (vx > 0 && vy < 0) {
        hits++;
        vx = -vx; vy = -vy; // Reflect velocity
    }

    // Ensure it can hit the borders before checking escape
    if (vx == 0 && vy == 0) {
        cout << -1 << '\n';
        return;
    }

    long long stepsX = (n - x) / vx;
    long long stepsY = (n - y) / vy;

    // Check conditions for hitting the edges
    if (stepsX < stepsY) {
        hits += stepsX;
        y += vy * stepsX;
        if (y == 0) canEscape = true;
        if (y < 0 || y > n) canEscape = false;
    } else {
        hits += stepsY;
        x += vx * stepsY;
        if (x == 0) canEscape = true;
        if (x < 0 || x > n) canEscape = false;
    }

    cout << (canEscape ? hits : -1) << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T; 
    cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}