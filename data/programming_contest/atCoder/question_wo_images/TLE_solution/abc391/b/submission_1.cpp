#include <bits/stdc++.h>
using namespace std;


int main() {
    int n, m;
    cin >> n >> m;

    vector<string> s(n), t(m);
    for (auto& x : s) {
        cin >> x;
    }
    for (auto& x : t) {
        cin >> x;
    }

    for (int i = 0; i <= n-m; ++i) {
        for (int j = 0; j <= n-m; ++j) {
            bool result = true;
            for (int a = 0; a < m; ++a) {
                for (int b = 0; j < m; ++b) {
                    if (t[a][b] != s[i+a][j+b]) {
                        result = false;
                    }
                }
            }
            if (result) {
                cout << i+1 << " " << j+1 << endl;
                return 0;
            }
        }
    }

    return 0;
}
