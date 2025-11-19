#include <iostream>
#include <thread>
#include <chrono>
#include <ctime>
#include <iomanip> // For std::put_time
#include <string>
#include <stack>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <numeric>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <set>
using ll = long long;
using pii = std::pair<int, int>;
using mii = std::map<int, int>;
const int maxn = 1e3 + 5;
const int inf = 0x3f3f3f3f;
using namespace std;
struct node
{
    int x;
    int y;
    int lastMoveDir;
    int step;
};

char m[maxn][maxn];
int H, W;

const int hori = 0;
const int ver = 1;
int dir[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
bool vis[maxn][maxn][2];
bool check(int x, int y, int dir)
{
    if(x<1 || x > H || y < 1 || y > W)
    {
        return false;
    }
    if(vis[x][y][dir])
    {
        return false;
    }
    if(m[x][y] == '#')
    {
        return false;
    }

    return true;

}

int main() {
    queue<node> q;
    std::cin >> H >> W;
    for (int i = 1; i <= H; ++i)
    {
        std::string S;
        std::cin >> S;
        for (int j = 1; j <= W; ++j)
        {
            m[i][j] = S[j-1];
            if(S[j-1] == 'S')
            {
                q.push({i, j, 0, 0});
                q.push({i, j, 1, 0});
            }
        }
    }
    while(!q.empty())
    {
        auto tmp = q.front();
        q.pop();
        vis[tmp.x][tmp.y][tmp.lastMoveDir] = 1;
        if(m[tmp.x][tmp.y] == 'G')
        {
            std::cout << tmp.step << '\n';
            return 0;
        }

        for(int i = 0; i < 4; ++i)
        {
            int newx = tmp.x + dir[i][0];
            int newy = tmp.y + dir[i][1];
            if(check(newx, newy, newx != tmp.x) && ((tmp.x != newx) && tmp.lastMoveDir==hori))
            {
                q.push({newx, newy, ver, tmp.step+1});
            }
            if(check(newx, newy, newx != tmp.x) && ((tmp.x == newx) && tmp.lastMoveDir==ver))
            {
                q.push({newx, newy, hori, tmp.step+1});
            }
        }
    }
    std::cout << -1 << '\n';

}




