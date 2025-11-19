#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<string> grid(N, string(N, '.'));

    // For i = 1 to N:
    // j = N+1 - i
    // if i <= j, fill square (i,i) to (j,j) with black if i odd, white if even
    // Overwrite previous colors

    for (int i = 1; i <= N; i++) {
        int j = N + 1 - i;
        if (i > j) break;
        char c = (i % 2 == 1) ? '#' : '.';
        for (int r = i - 1; r <= j - 1; r++) {
            for (int cidx = i - 1; cidx <= j - 1; cidx++) {
                grid[r][cidx] = c;
            }
        }
    }

    for (auto &row : grid) cout << row << "\n";

    return 0;
}