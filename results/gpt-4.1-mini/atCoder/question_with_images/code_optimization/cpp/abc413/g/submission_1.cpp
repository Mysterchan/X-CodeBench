#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H, W, K;
    cin >> H >> W >> K;

    // Store obstacles in a hash set for O(1) lookup
    unordered_set<long long> obstacles;
    auto encode = [&](int r, int c) -> long long {
        return (long long)r * (W + 1) + c;
    };

    for (int i = 0; i < K; i++) {
        int r, c;
        cin >> r >> c;
        obstacles.insert(encode(r, c));
    }

    // If start or goal is blocked (should not happen per constraints), no path
    // But constraints guarantee (1,1) and (H,W) are not obstacles.

    // BFS using a queue and visited set
    unordered_set<long long> visited;
    queue<pair<int,int>> q;
    q.emplace(1,1);
    visited.insert(encode(1,1));

    const int dr[4] = {-1, 1, 0, 0};
    const int dc[4] = {0, 0, -1, 1};

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        if (r == H && c == W) {
            cout << "Yes\n";
            return 0;
        }

        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr < 1 || nr > H || nc < 1 || nc > W) continue;
            long long code = encode(nr, nc);
            if (obstacles.count(code) || visited.count(code)) continue;
            visited.insert(code);
            q.emplace(nr, nc);
        }
    }

    cout << "No\n";
    return 0;
}