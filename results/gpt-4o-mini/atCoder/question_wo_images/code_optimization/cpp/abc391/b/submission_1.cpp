#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<string> s(n), t(m);
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
    }
    for (int i = 0; i < m; ++i) {
        cin >> t[i];
    }

    for (int i = 0; i <= n - m; ++i) {
        for (int j = 0; j <= n - m; ++j) {
            bool found = true;
            for (int a = 0; a < m && found; ++a) { // Only continue if found is true
                for (int b = 0; b < m; ++b) {
                    if (t[a][b] != s[i + a][j + b]) {
                        found = false;
                        break; // Break inner loop if mismatch found
                    }
                }
            }
            if (found) {
                cout << i + 1 << " " << j + 1 << endl;
                return 0;
            }
        }
    }

    return 0;
}