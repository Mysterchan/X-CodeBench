#include <bits/stdc++.h>
using namespace std;
#define int long long
const int N = 1e6 + 10, mod = 1e9 + 7, inf = 0x3f3f3f3f3f3f3f3f;
int dx[4] = { 1,0,-1,0 };
int dy[4] = { 0,-1,0,1 };
struct node {
    int x, y, t, r, d;
};
struct pair_hash {
    size_t operator()(const pair<int, int>& p) const {
        return hash<int>()(p.first) ^ (hash<int>()(p.second) << 1);
    }
};
queue<node>pq;
unordered_map<pair<int, int>, int,pair_hash>vis;
int cnt;
void solve()
{

    int h, w;string s;cin >> h >> w >> s;int ans = 0;cnt++;
    s = " " + s;
    pq.push({ 1,1,1,count(s.begin(),s.end(),'R'),count(s.begin(),s.end(),'D') });
    vis[make_pair(1, 1)] = cnt;
    while (!pq.empty()) {
        auto [x, y, t, r, d] = pq.front();pq.pop();
        if (t > h + w - 1)continue;
        ans++;
        if (s[t] == 'D' && x + 1 <= h && vis[make_pair(x + 1, y)] != cnt) {
            pq.push({ x + 1, y, t + 1, r, d });vis[make_pair(x + 1, y)] = cnt;
        } else if (s[t] == 'R' && y + 1 <= w && vis[make_pair(x, y + 1)] != cnt) {
            pq.push({ x, y + 1, t + 1, r, d });vis[make_pair(x, y + 1)] = cnt;
        } else if (s[t] == '?') {
            if (x + 1 <= h && d + 1 <= h - 1 && vis[make_pair(x + 1, y)] != cnt) {
                pq.push({ x + 1, y, t + 1, r, d + 1 });vis[make_pair(x + 1, y)] = cnt;
            }
            if (y + 1 <= w && r + 1 <= w - 1 && vis[make_pair(x, y + 1)] != cnt) {
                pq.push({ x, y + 1, t + 1, r + 1, d });vis[make_pair(x, y + 1)] = cnt;
            }
        }
    }
    cout << ans << endl;
    return;
}

signed main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T = 1;
    cin >> T;
    for (int i = 1;i <= T;i++) {
        solve();
    }
}