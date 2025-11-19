#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; cin >> n;
    vector<string> S(n), T(n);
    for (int i = 0; i < n; i++) cin >> S[i];
    for (int i = 0; i < n; i++) cin >> T[i];

    // Precompute all 4 rotations of S
    // rot[0] = original S
    // rot[1] = S rotated 90 degrees clockwise
    // rot[2] = S rotated 180 degrees
    // rot[3] = S rotated 270 degrees
    vector<vector<string>> rot(4, vector<string>(n));
    rot[0] = S;

    for (int k = 1; k < 4; k++) {
        vector<string> &prev = rot[k - 1];
        vector<string> cur(n, string(n, '.'));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cur[j][n - 1 - i] = prev[i][j];
            }
        }
        rot[k] = move(cur);
    }

    int ans = INT_MAX;
    // For each rotation, count how many cells differ from T
    // The minimal number of operations = number of rotations + number of differing cells
    for (int k = 0; k < 4; k++) {
        int diff = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (rot[k][i][j] != T[i][j]) diff++;
            }
        }
        ans = min(ans, k + diff);
    }

    cout << ans << "\n";
    return 0;
}