#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll prime = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    ll t;
    cin >> t;
    while (t--) {
        ll h, w;
        cin >> h >> w;
        vector<string> a(h);
        for (auto &row : a) cin >> row;

        vector<bool> rowVisited(h, false), colVisited(w, false);
        vector<vector<int>> arr(h, vector<int>(w, 0));
        ll ans = 1;
        bool valid = true;

        for (int i = 0; i < h; ++i) {
            if (rowVisited[i]) continue;
            rowVisited[i] = true;
            stack<pair<ll, ll>> rows, cols;
            
            // Search for 'B' in the current row
            for (int j = 0; j < w; ++j) {
                if (a[i][j] == 'B') {
                    rows.emplace(i, j);
                    cols.emplace(i, j);
                    colVisited[j] = true;
                    arr[i][j] = 1; // Initial mark
                    break;
                }
            }

            ans = (ans * 2) % prime;
            if (rows.empty()) {
                if (w % 2 == 1) {
                    valid = false;
                    break;
                }
                continue;
            }

            while (!rows.empty() || !cols.empty()) {
                if (!valid) break;

                if (!rows.empty()) {
                    auto [curRow, lastCol] = rows.top();
                    rows.pop();
                    for (int j = 1; j <= w; ++j) {
                        int nextCol = (lastCol + j) % w;
                        if (a[curRow][nextCol] == 'B') {
                            int nextValue = (j % 2 == 1) ? arr[curRow][lastCol] : 3 - arr[curRow][lastCol];

                            if (arr[curRow][nextCol] != 0 && arr[curRow][nextCol] != nextValue) {
                                valid = false;
                                break;
                            }
                            if (arr[curRow][nextCol] == 0) {
                                arr[curRow][nextCol] = nextValue;
                                cols.emplace(curRow, nextCol);
                                colVisited[nextCol] = true;
                            }
                            lastCol = nextCol;
                        }
                    }
                    continue;
                }

                auto [curColRow, curCol] = cols.top();
                cols.pop();
                for (int j = 1; j <= h; ++j) {
                    int nextRow = (curColRow + j) % h;
                    if (a[nextRow][curCol] == 'B') {
                        int nextValue = (j % 2 == 1) ? arr[curColRow][curCol] : 3 - arr[curColRow][curCol];

                        if (arr[nextRow][curCol] != 0 && arr[nextRow][curCol] != nextValue) {
                            valid = false;
                            break;
                        }
                        if (arr[nextRow][curCol] == 0) {
                            arr[nextRow][curCol] = nextValue;
                            rows.emplace(nextRow, curCol);
                            rowVisited[nextRow] = true;
                        }
                    }
                }
            }
            if (!valid) break;
        }

        for (int j = 0; j < w; ++j) {
            bool colEmpty = true;
            for (int i = 0; i < h; ++i) {
                if (a[i][j] == 'B') {
                    colEmpty = false;
                    break;
                }
            }
            if (colEmpty) {
                if (h % 2 == 1) {
                    valid = false;
                    break;
                }
                ans = (ans * 2) % prime;
            }
        }

        cout << (valid ? ans : 0) << '\n';
    }

    return 0;
}