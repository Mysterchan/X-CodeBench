#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n, m, k;
        cin >> n >> m >> k;
        vector<string> grid(n);
        for (int i = 0; i < n; i++) {
            cin >> grid[i];
        }

        if (k == 0) {
            cout << 0 << '\n';
            continue;
        }

        vector<vector<bool>> empty(n, vector<bool>(m, false));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '.') {
                    empty[i][j] = true;
                }
            }
        }

        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 'g') {
                    bool found = false;
                    if (i - k >= 0) {
                        for (int b = j - k; b <= j + k; b++) {
                            if (b >= 0 && b < m && empty[i - k][b]) {
                                found = true;
                                break;
                            }
                        }
                    }
                    if (found) {
                        count++;
                        continue;
                    }
                    if (i + k < n) {
                        for (int b = j - k; b <= j + k; b++) {
                            if (b >= 0 && b < m && empty[i + k][b]) {
                                found = true;
                                break;
                            }
                        }
                    }
                    if (found) {
                        count++;
                        continue;
                    }
                    if (j - k >= 0) {
                        for (int a = i - k + 1; a <= i + k - 1; a++) {
                            if (a >= 0 && a < n && empty[a][j - k]) {
                                found = true;
                                break;
                            }
                        }
                    }
                    if (found) {
                        count++;
                        continue;
                    }
                    if (j + k < m) {
                        for (int a = i - k + 1; a <= i + k - 1; a++) {
                            if (a >= 0 && a < n && empty[a][j + k]) {
                                found = true;
                                break;
                            }
                        }
                    }
                    if (found) {
                        count++;
                    }
                }
            }
        }
        cout << count << '\n';
    }
    return 0;
}