#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H, W;
    cin >> H >> W;
    vector<string> grid(H);
    for (int i = 0; i < H; i++) cin >> grid[i];

    // Directions for adjacency
    const int dr[] = {-1, 1, 0, 0};
    const int dc[] = {0, 0, -1, 1};

    // Count of black neighbors for each cell
    vector<vector<int>> black_neighbors(H, vector<int>(W, 0));

    // Initialize black_neighbors counts for white cells
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (grid[i][j] == '.') {
                int cnt = 0;
                for (int d = 0; d < 4; d++) {
                    int ni = i + dr[d], nj = j + dc[d];
                    if (ni >= 0 && ni < H && nj >= 0 && nj < W && grid[ni][nj] == '#') {
                        cnt++;
                    }
                }
                black_neighbors[i][j] = cnt;
            }
        }
    }

    // Queue for cells to be painted black
    queue<pair<int, int>> q;

    // Initially enqueue all white cells with exactly one black neighbor
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (grid[i][j] == '.' && black_neighbors[i][j] == 1) {
                q.emplace(i, j);
            }
        }
    }

    // BFS-like process to paint cells black until no more can be painted
    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        if (grid[r][c] == '#') continue; // Already painted

        grid[r][c] = '#';

        // Update neighbors' black_neighbors count
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d], nc = c + dc[d];
            if (nr >= 0 && nr < H && nc >= 0 && nc < W && grid[nr][nc] == '.') {
                black_neighbors[nr][nc]++;
                if (black_neighbors[nr][nc] == 1) {
                    q.emplace(nr, nc);
                }
            }
        }
    }

    // Count black cells
    int ans = 0;
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (grid[i][j] == '#') ans++;
        }
    }

    cout << ans << "\n";
    return 0;
}