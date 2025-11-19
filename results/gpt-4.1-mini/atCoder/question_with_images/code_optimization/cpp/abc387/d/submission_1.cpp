#include <iostream>
#include <queue>
#include <string>
using namespace std;

const int maxn = 1005;
const int hori = 0;
const int ver = 1;

int H, W;
char grid[maxn][maxn];
bool vis[maxn][maxn][2];

// Directions: vertical moves (up/down), horizontal moves (left/right)
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

struct State {
    int x, y, lastDir, steps;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> H >> W;
    int sx = 0, sy = 0;
    for (int i = 1; i <= H; ++i) {
        string row; cin >> row;
        for (int j = 1; j <= W; ++j) {
            grid[i][j] = row[j - 1];
            if (grid[i][j] == 'S') {
                sx = i; sy = j;
            }
        }
    }

    queue<State> q;
    // Start with both possible directions (horizontal or vertical)
    q.push({sx, sy, hori, 0});
    q.push({sx, sy, ver, 0});
    vis[sx][sy][hori] = true;
    vis[sx][sy][ver] = true;

    while (!q.empty()) {
        State cur = q.front(); q.pop();
        if (grid[cur.x][cur.y] == 'G') {
            cout << cur.steps << "\n";
            return 0;
        }

        // Next moves must alternate direction:
        // if last move was horizontal, next must be vertical, and vice versa
        int nextDir = (cur.lastDir == hori) ? ver : hori;

        // For vertical moves: dx = ±1, dy = 0
        // For horizontal moves: dx = 0, dy = ±1
        if (nextDir == ver) {
            for (int d = 0; d < 2; ++d) {
                int nx = cur.x + dx[d];
                int ny = cur.y + dy[d];
                if (nx >= 1 && nx <= H && ny >= 1 && ny <= W &&
                    !vis[nx][ny][nextDir] && grid[nx][ny] != '#') {
                    vis[nx][ny][nextDir] = true;
                    q.push({nx, ny, nextDir, cur.steps + 1});
                }
            }
        } else { // nextDir == hori
            for (int d = 2; d < 4; ++d) {
                int nx = cur.x + dx[d];
                int ny = cur.y + dy[d];
                if (nx >= 1 && nx <= H && ny >= 1 && ny <= W &&
                    !vis[nx][ny][nextDir] && grid[nx][ny] != '#') {
                    vis[nx][ny][nextDir] = true;
                    q.push({nx, ny, nextDir, cur.steps + 1});
                }
            }
        }
    }

    cout << -1 << "\n";
    return 0;
}