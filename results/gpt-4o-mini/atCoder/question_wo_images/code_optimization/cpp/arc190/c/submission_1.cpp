#include <bits/stdc++.h>
using namespace std;

const int mod = 998244353;

int main() {
    int H, W;
    cin >> H >> W;
    vector<vector<long long>> A(H + 1, vector<long long>(W + 1));
    for (int i = 1; i <= H; ++i) {
        for (int j = 1; j <= W; ++j) {
            cin >> A[i][j];
        }
    }

    int Q, sh, sw;
    cin >> Q >> sh >> sw;

    vector<long long> f(W + 1), g(W + 1); // f and g arrays for path sums.

    // Initial path product calculation.
    f[1] = A[1][1];
    for (int j = 2; j <= W; ++j) {
        f[j] = f[j - 1] * A[1][j] % mod;
    }

    long long result = 0;
    g[W] = A[H][W]; // g array for inverse path calculation.
    for (int j = W - 1; j >= 1; --j) {
        g[j] = g[j + 1] * A[H][j] % mod;
    }

    auto query = [&]() {
        long long res = 0;
        for (int j = 1; j <= W; ++j) {
            res = (res + f[j] * g[j]) % mod;
        }
        return res;
    };

    cout << query() << endl;

    // Process each operation.
    while (Q--) {
        char dir;
        long long value;
        cin >> dir >> value;

        // Update position based on direction.
        if (dir == 'L') {
            sw--;
        } else if (dir == 'R') {
            sw++;
        } else if (dir == 'U') {
            sh--;
        } else {
            sh++;
        }

        // Update the grid.
        A[sh][sw] = value;

        // Recalculate f and g from the position.
        f[1] = A[1][1];
        for (int j = 2; j <= W; ++j) {
            f[j] = f[j - 1] * A[1][j] % mod;
        }

        g[W] = A[H][W];
        for (int j = W - 1; j >= 1; --j) {
            g[j] = g[j + 1] * A[H][j] % mod;
        }

        cout << query() << endl;
    }

    return 0;
}
