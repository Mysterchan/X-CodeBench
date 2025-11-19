#include <iostream>
using namespace std;

#define int long long

void solve() {
    int n, m;
    cin >> n >> m;

    // Calculate the maximum players with perfect record directly
    if (m == 1) {
        cout << 1 << endl;  // Only one player on each team can win
    } else {
        cout << (n - 1) * m << endl;  // Each team can have (n-1) players winning, hence (n-1) * m
    }
}

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int T;
    cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}
