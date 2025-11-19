#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0); // Faster I/O
    cin.tie(0);

    int t;
    cin >> t;
    while (t--) {
        long long x, y, z;
        cin >> x >> y >> z;

        // Conditions
        if (x < z || (y > 0 && (y < (z - 1) || y < (x + (y > 0 ? 1 : 0) - z)))) || (x == 0 && z > 0) || (y == 0 && z > 0)) {
            cout << "No\n";
        } else {
            cout << "Yes\n";
        }
    }
    return 0;
}
