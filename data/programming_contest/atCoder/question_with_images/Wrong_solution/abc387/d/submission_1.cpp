#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <climits>
using namespace std;

const int INF = INT_MAX;
const int dx[4] = {0, 0, 1, -1};
const int dy[4] = {1, -1, 0, 0};

int main() {
    int H, W;
    cin >> H >> W;
    
    vector<string> grid(H);
    for (int i = 0; i < H; ++i) {
        cin >> grid[i];
    }
    
    int sh = -1, sw = -1, gh = -1, gw = -1;
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            if (grid[i][j] == 'S') {
                sh = i; sw = j;
            } else if (grid[i][j] == 'G') {
                gh = i; gw = j;
            }
        }
    }
    
    vector<vector<vector<int>>> dist(H, vector<vector<int>>(W, vector<int>(2, INF)));
    queue<tuple<int, int, int>> q;
    
    dist[sh][sw][0] = 0;
    dist[sh][sw][1] = 0;
    q.emplace(sh, sw, 0);
    q.emplace(sh, sw, 1);
    
    while (!q.empty()) {
        auto [h, w, last] = q.front();
        q.pop();
        
        int start = (last == 0) ? 2 : 0;
        int end = (last == 0) ? 4 : 2;
        
        for (int i = start; i < end; ++i) {
            int nh = h + dx[i];
            int nw = w + dy[i];
            
            if (nh < 0 || nh >= H || nw < 0 || nw >= W) continue;
            if (grid[nh][nw] == '#') continue;
            
            int nlast = (i < 2) ? 1 : 0;
            if (dist[nh][nw][nlast] > dist[h][w][last] + 1) {
                dist[nh][nw][nlast] = dist[h][w][last] + 1;
                q.emplace(nh, nw, nlast);
            }
        }
    }
    
    int ans = min(dist[gh][gw][0], dist[gh][gw][1]);
    cout << (ans == INF ? -1 : ans) << endl;
    
    return 0;
}