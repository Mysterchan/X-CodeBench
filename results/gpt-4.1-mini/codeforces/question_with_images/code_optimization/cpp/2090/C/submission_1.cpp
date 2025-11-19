#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int q; cin >> q;
    while (q--) {
        int n; cin >> n;
        int t0 = 0, t1 = 0;
        for (int i = 0; i < n; i++) {
            int ti; cin >> ti;
            if (ti == 0) {
                // For t_i=0 guests, assign seats in the "0" pattern:
                // Coordinates: (1 + 3*t0, 1 + 3*t0)
                int x = 1 + 3 * t0;
                int y = 1 + 3 * t0;
                cout << x << ' ' << y << '\n';
                t0++;
            } else {
                // For t_i=1 guests, assign seats in the "1" pattern:
                // Coordinates: (1 + 3*t1, 2)
                int x = 1 + 3 * t1;
                int y = 2;
                cout << x << ' ' << y << '\n';
                t1++;
            }
        }
    }
    return 0;
}