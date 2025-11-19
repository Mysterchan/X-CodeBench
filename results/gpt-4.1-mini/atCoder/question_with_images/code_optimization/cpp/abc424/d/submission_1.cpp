#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while (T--) {
        int H, W; cin >> H >> W;
        vector<string> grid(H);
        for (int i = 0; i < H; i++) cin >> grid[i];

        int repaint = 0;
        // For each 2x2 block, if all black, repaint one cell (choose top-left)
        for (int i = 0; i + 1 < H; i++) {
            for (int j = 0; j + 1 < W; j++) {
                if (grid[i][j] == '#' && grid[i][j + 1] == '#' &&
                    grid[i + 1][j] == '#' && grid[i + 1][j + 1] == '#') {
                    // Repaint top-left cell to white
                    grid[i][j] = '.';
                    repaint++;
                }
            }
        }

        cout << repaint << "\n";
    }

    return 0;
}