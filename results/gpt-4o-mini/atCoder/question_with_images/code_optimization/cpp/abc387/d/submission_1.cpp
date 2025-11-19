#include <iostream>
#include <queue>
#include <vector>
#include <string>
using namespace std;

const int maxn = 1005;
const int inf = 0x3f3f3f3f;

struct node {
    int x, y, step;
    bool isVertical;
};

char grid[maxn][maxn];
int H, W;

const int dx[4] = {1, -1, 0, 0};
const int dy[4] = {0, 0, 1, -1};

bool isValid(int x, int y) {
    return x >= 1 && x <= H && y >= 1 && y <= W && grid[x][y] != '#';
}

int main() {
    queue<node> q;
    cin >> H >> W;

    int startX, startY, goalX, goalY;

    for (int i = 1; i <= H; ++i) {
        string S;
        cin >> S;
        for (int j = 1; j <= W; ++j) {
            grid[i][j] = S[j - 1];
            if (S[j - 1] == 'S') {
                startX = i;
                startY = j;
            } else if (S[j - 1] == 'G') {
                goalX = i;
                goalY = j;
            }
        }
    }

    // Initialize the queue with both possible starting moves
    q.push({startX, startY, 0, false}); // horizontal move
    q.push({startX, startY, 0, true});  // vertical move

    bool visited[maxn][maxn][2] = {{{false}}};

    while (!q.empty()) {
        node current = q.front();
        q.pop();

        if (visited[current.x][current.y][current.isVertical]) continue;
        visited[current.x][current.y][current.isVertical] = true;

        if (current.x == goalX && current.y == goalY) {
            cout << current.step << '\n';
            return 0;
        }

        // Calculate the next possible moves
        for (int i = 0; i < 4; ++i) {
            int newX = current.x + dx[i];
            int newY = current.y + dy[i];

            if (isValid(newX, newY)) {
                if (current.isVertical && (newX != current.x)) {
                    // Switch to horizontal
                    q.push({newX, newY, current.step + 1, false}); 
                } else if (!current.isVertical && (newY != current.y)) {
                    // Switch to vertical
                    q.push({newX, newY, current.step + 1, true}); 
                }
            }
        }
    }

    cout << -1 << '\n';
}