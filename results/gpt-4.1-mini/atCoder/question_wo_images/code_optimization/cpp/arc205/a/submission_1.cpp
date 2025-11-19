#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;
    vector<string> s(n + 2, string(n + 2, '#')); // padding with black cells

    for (int i = 1; i <= n; i++) {
        cin >> s[i];
        s[i] = "#" + s[i] + "#"; // pad each row with black cells on both sides
    }

    // Precompute a 2D prefix sum for 2x2 white squares
    // A 2x2 white square at (r,c) means cells (r,c),(r,c+1),(r+1,c),(r+1,c+1) are all '.'
    vector<vector<int>> prefix(n + 1, vector<int>(n + 1, 0));
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < n; j++) {
            int val = (s[i][j] == '.' && s[i][j + 1] == '.' && s[i + 1][j] == '.' && s[i + 1][j + 1] == '.') ? 1 : 0;
            prefix[i][j] = val + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1];
        }
    }

    while (q--) {
        int u, d, l, r;
        cin >> u >> d >> l >> r;
        // We want to count how many 2x2 white squares are fully inside the subgrid [u,d] x [l,r].
        // The top-left corner of such squares must be in rows [u, d-1] and columns [l, r-1].
        if (d - 1 < u || r - 1 < l) {
            cout << 0 << "\n";
            continue;
        }
        int res = prefix[d - 1][r - 1] - prefix[u - 1][r - 1] - prefix[d - 1][l - 1] + prefix[u - 1][l - 1];
        cout << res << "\n";
    }

    return 0;
}