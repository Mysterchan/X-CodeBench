#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        ll x, y;
        cin >> x >> y;
        ll ans = -1;

        if (y > x) {
            ans = 2;
        } else {
            // Check if we can achieve (x, y) in 3 moves
            // Let the first move be a, second be b, third be c
            // a + c = x, b = y
            // conditions: a < b < c
            // It implies: a = y - 1, c = x - (y - 1)
            // Therefore, a = y - 1 should be less than b, and c = x - a > a
            
            ll a = y - 1;
            ll c = x - a;
            if (a >= 1 && a < b && b < c) {
                ans = 3;
            } else if (y >= 1 && y < x) {
                ans = 2; // Cover the case where we can go to (x, y) directly
            }
        }
        
        cout << ans << "\n";
    }

    return 0;
}