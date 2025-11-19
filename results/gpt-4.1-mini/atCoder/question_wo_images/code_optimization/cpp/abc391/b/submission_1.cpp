#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<string> s(n), t(m);
    for (auto& x : s) cin >> x;
    for (auto& x : t) cin >> x;

    // Precompute hash for each row of S and T to speed up comparison
    // Since N and M are small (<=50), a direct comparison with early break is efficient enough.

    for (int i = 0; i <= n - m; ++i) {
        for (int j = 0; j <= n - m; ++j) {
            bool match = true;
            for (int a = 0; a < m && match; ++a) {
                // Compare substring of s[i+a] from j to j+m-1 with t[a]
                if (s[i + a].compare(j, m, t[a]) != 0) {
                    match = false;
                }
            }
            if (match) {
                cout << i + 1 << " " << j + 1 << "\n";
                return 0;
            }
        }
    }

    return 0;
}