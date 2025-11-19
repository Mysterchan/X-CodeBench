#include <bits/stdc++.h>
using namespace std;

void solve() {
    long long n, m, a, b;
    cin >> n >> m >> a >> b;
    
    // Find the minimum distance to the edges of the grid
    long long h = min(a - 1, n - a); // rows above and below
    long long w = min(b - 1, m - b); // columns left and right
    
    // The number of turns to end the game
    long long ans = max(h, w) + 1; // adding 1 for the last turn to reach 1x1
    cout << ans << '\n';
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t;
    cin >> t; // Read number of test cases
    while (t--) {
        solve();
    }
    return 0;
}