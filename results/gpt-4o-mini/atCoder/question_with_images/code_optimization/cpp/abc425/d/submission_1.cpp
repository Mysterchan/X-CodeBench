#include<bits/stdc++.h>
using namespace std;

int main() {
    int H, W;
    cin >> H >> W;
    vector<vector<char>> grid(H, vector<char>(W));
    queue<pair<int, int>> q;
    
    // Read grid and initialize the queue with initial black cells
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            cin >> grid[i][j];
            if (grid[i][j] == '#') {
                q.push({i, j});
            }
        }
    }

    // Directions for neighbor cells (up, down, left, right)
    vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    while (!q.empty()) {
        int count_new_black = 0; // Count of new black cells to be painted
        vector<pair<int, int>> to_paint; // Cells to paint in this iteration
        
        // Process current batch of black cells
        int size = q.size();
        for (int i = 0; i < size; ++i) {
            auto [x, y] = q.front();
            q.pop();
            
            for (auto [dx, dy] : directions) {
                int nx = x + dx, ny = y + dy;
                if (nx >= 0 && nx < H && ny >= 0 && ny < W && grid[nx][ny] == '.') {
                    // Check if this white cell is to be painted
                    int black_neighbors = 0;

                    for (auto [ddx, ddy] : directions) {
                        int nnx = nx + ddx, nny = ny + ddy;
                        if (nnx >= 0 && nnx < H && nny >= 0 && nny < W && grid[nnx][nny] == '#') {
                            black_neighbors++;
                        }
                    }

                    if (black_neighbors == 1) {
                        to_paint.push_back({nx, ny});
                    }
                }
            }
        }

        // Paint the collected cells black
        for (auto [a, b] : to_paint) {
            grid[a][b] = '#';
            q.push({a, b});
            count_new_black++;
        }

        // If no new cells to paint, we break out
        if (count_new_black == 0) {
            break;
        }
    }

    // Count the total number of black cells
    int total_black_cells = 0;
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            if (grid[i][j] == '#') {
                total_black_cells++;
            }
        }
    }

    cout << total_black_cells << endl;
    return 0;
}