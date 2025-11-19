#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int H, W;
    cin >> H >> W;
    
    vector<vector<int>> F(H, vector<int>(W));
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            cin >> F[i][j];
        }
    }

    int Q;
    cin >> Q;
    
    while (Q--) {
        int A, B, Y, C, D, Z;
        cin >> A >> B >> Y >> C >> D >> Z;
        A--; B--; C--; D--; // Make zero-indexed

        int stairs = abs(Y - Z); // Direct stairs usage without walkways
        // Check if we can use walkways to potentially reduce stairs usage
        if (A == C && B == D) {
            // Same building
            cout << stairs << "\n";
            continue;
        }

        queue<pair<int, int>> q;
        vector<vector<bool>> visited(H, vector<bool>(W, false));

        q.push({A, B});
        visited[A][B] = true;

        while (!q.empty()) {
            auto [x, y] = q.front();
            q.pop();
            int currentFloors = F[x][y];
            
            // Check adjacent moves
            for (int dx = -1; dx <= 1; dx++) {
                for (int dy = -1; dy <= 1; dy++) {
                    if (abs(dx) == abs(dy)) continue; // Only cardinal directions
                    int nx = x + dx, ny = y + dy;

                    if (nx >= 0 && nx < H && ny >= 0 && ny < W && !visited[nx][ny]) {
                        visited[nx][ny] = true;
                        // Calculate the new stairs needed for this adjacent building:
                        int requiredStairs = abs(Z - min(currentFloors, F[nx][ny]));
                        stairs = min(stairs, requiredStairs);
                        q.push({nx, ny});
                    }
                }
            }
        }

        cout << stairs << "\n";
    }

    return 0;
}
