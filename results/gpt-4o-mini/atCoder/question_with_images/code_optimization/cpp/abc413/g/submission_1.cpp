#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int h, w, k;
    cin >> h >> w >> k;
    
    vector<vector<bool>> g(h + 1, vector<bool>(w + 1, false));
    
    for (int i = 0; i < k; i++) {
        int x, y;
        cin >> x >> y;
        g[x][y] = true;
    }

    if (g[1][1] || g[h][w]) {
        cout << "No\n";
        return 0;
    }
    
    queue<pair<int, int>> q;
    q.push({1, 1});
    g[1][1] = true;

    const vector<int> dx = {0, 0, -1, 1};
    const vector<int> dy = {-1, 1, 0, 0};

    while (!q.empty()) {
        int x = q.front().first, y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; ++i) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 1 && nx <= h && ny >= 1 && ny <= w && !g[nx][ny]) {
                g[nx][ny] = true;
                q.push({nx, ny});
            }
        }
    }

    cout << (g[h][w] ? "Yes\n" : "No\n");
}