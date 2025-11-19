#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, x;
    cin >> n >> x;
    string s;
    cin >> s;

    // Adjust 'x' to be 0-indexed
    x--;

    // Left: Count walls until a wall or boundary
    int left = 0;
    for (int i = x - 1; i >= 0; --i) {
        if (s[i] == '#') break;
        left++;
    }

    // Right: Count walls until a wall or boundary
    int right = 0;
    for (int i = x + 1; i < n; ++i) {
        if (s[i] == '#') break;
        right++;
    }

    // The minimum days required to escape is the minimum walls in either direction + 1
    cout << min(left, right) + 1 << endl;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int T;
    cin >> T;
    while (T--) {
        solve();
    }
    
    return 0;
}