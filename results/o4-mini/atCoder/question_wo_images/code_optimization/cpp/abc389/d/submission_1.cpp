#include <iostream>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll R;
    cin >> R;

    // We count integer centers (i, j) of unit squares whose farthest corner
    // lies inside the circle of radius R centered at (0,0).
    // A = 2*i + 1, B = 2*j + 1 must satisfy A^2 + B^2 <= (2R)^2.
    ll R2 = R << 1;
    ll RR4 = R2 * R2;

    // Initial max odd B for i = 0 is floor(sqrt(RR4 - 1)) = (2R - 1)
    ll Bmax = R2 - 1;  // always odd when R >= 1

    ll ans = 0;
    // i ranges from 0 to floor(R - 0.5) = R - 1 for integer R >= 1
    for (ll i = 0; i <= R - 1; ++i) {
        ll A = 2 * i + 1;
        // Decrease Bmax until A^2 + Bmax^2 <= RR4
        while (Bmax > 0 && A * A + Bmax * Bmax > RR4) {
            Bmax -= 2;
        }
        if (Bmax <= 0) {
            // No more valid j for this i or larger i
            break;
        }
        // j_max = (Bmax - 1) / 2
        ll t = (Bmax - 1) >> 1;
        if (i == 0) {
            // i == 0, j = 0 counted once, j >= 1 counted twice (±j)
            ans += 1 + 2 * t;
        } else {
            // i >= 1, j == 0 counted twice (±i), j >= 1 counted four times
            ans += 2 + 4 * t;
        }
    }

    cout << ans << "\n";
    return 0;
}