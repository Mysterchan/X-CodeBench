#include <bits/stdc++.h>

#pragma GCC optimize("Ofast")
using namespace std;
#define int long long

void solve()
{
    int n, m;
    cin >> n >> m;
    vector<string> arr(n);
    for(auto &i: arr) cin >> i;
    vector<vector<vector<int>>> dis(n, vector<vector<int>> (m, vector<int> (2, 1e18)));
    
    auto check = [&](int x, int y)
    {
        if(x >= 0 && x < n && y >= 0 && y < m && arr[x][y] != '#') return 1;
        else return 0;
    };

    vector<pair<int, int>> ok0 = {{1, 0}, {-1, 0}};
    vector<pair<int, int>> ok1 = {{0, -1}, {0, 1}};

    int sx = -1, sy = -1, ex = -1, ey = -1;
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < m; j++)
        {
            if(arr[i][j] == 'S')
            {
                sx = i;
                sy = j;
            }
            else if(arr[i][j] == 'G')
            {
                ex = i;
                ey = j;
            }
        }
    }

    queue<tuple<int, int, int>> qu;
    qu.push({sx, sy, 0});
    qu.push({sx, sy, 1});
    dis[sx][sy][0] = 0;
    dis[sx][sy][1] = 0;

    while(!qu.empty())
    {
        auto [x, y, s] = qu.front();
        qu.pop();

        vector<pair<int, int>> ok = s ? ok0 : ok1;
        for(auto [dx, dy]: ok)
        {
            int nx = x + dx, ny = y + dy, ns = 1 - s;

            if(check(nx, ny) && dis[nx][ny][ns] > 1 + dis[x][y][s])
            {
                dis[nx][ny][ns] = 1 + dis[x][y][s];
                qu.push({nx, ny, ns});
            }
        }
    }

    int ans = min(dis[ex][ey][0], dis[ex][ey][1]);
    if(ans == 1e18) cout << -1 << '\n';
    else cout << ans << '\n';
    return;
}

int32_t main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t = 1;

    while(t--)
    {
        solve();
    }

    return 0;
}