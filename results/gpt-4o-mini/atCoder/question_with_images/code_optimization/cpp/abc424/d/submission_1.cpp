#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int T;
    cin >> T;
    
    while (T--) {
        int H, W;
        cin >> H >> W;
        vector<string> grid(H);
        for (int i = 0; i < H; i++)
            cin >> grid[i];

        int repaintCount = 0;

        for (int i = 0; i < H - 1; i++) {
            for (int j = 0; j < W - 1; j++) {
                if (grid[i][j] == '#' && grid[i + 1][j] == '#' && 
                    grid[i][j + 1] == '#' && grid[i + 1][j + 1] == '#') {

                    // We have a 2x2 block of '#'
                    repaintCount += 1; // At least one needs to be changed
                    grid[i + 1][j + 1] = '.'; // Change one cell to avoid 2x2 block
                }
            }
        }

        cout << repaintCount << "\n";
    }
    
    return 0;
}