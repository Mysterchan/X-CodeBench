#include <iostream>
#include <cmath>

using namespace std;

int main() {
    long long R;
    cin >> R;

    long long R2 = (long long)2 * R;
    long long R2_sq = R2 * R2;

    long long answer = 0;

    // Iterate over x = 0, 2, 4, ..., up to 2*R
    for (long long x = 0; x <= R2; x += 2) {
        // Calculate max y such that (x+1)^2 + (y+1)^2 <= (2R)^2
        // We want to find max y (even) with (x+1)^2 + (y+1)^2 <= R2^2
        long long x1 = x + 1;
        long long val = R2_sq - x1 * x1;
        if (val < 0) break;

        // y+1 <= sqrt(val)
        long long y_max = (long long)floor(sqrt((double)val)) - 1;
        if (y_max < 0) continue;

        // y must be even, so find largest even <= y_max
        if (y_max % 2 != 0) y_max--;

        if (y_max < 0) continue;

        // Number of valid y's for this x is (y_max / 2) + 1 (including y=0)
        long long count_y = y_max / 2 + 1;

        if (x == 0) {
            // x=0 line counted once
            answer += count_y;
        } else {
            // other x lines counted twice (positive and negative x)
            answer += 2 * count_y;
        }
    }

    cout << answer << "\n";

    return 0;
}