#include<bits/stdc++.h>
using namespace std;
#define int long long
#define INF 1e18 + 7
#define MMi -1e18+7
#define endl '\n'
const int N1 = 1e6 + 10;
#define owo 0
#define fushen ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
int mod = 1e9 + 7;
#define ll __int128
const int N = 3e5 + 10;
int n, m;
int js = -1;
int head[N1];
struct node
{
    int to, nxt;
}g[N1 * 2];
void add(int x, int y)
{
    g[++js].to = y;
    g[js].nxt = head[x];
    head[x] = js;
}
int ans1 = 0;
int cf[N];
void dfs2(int x, int fa)
{
    ans1 += cf[x];
    for (int i = head[x]; i != -1; i = g[i].nxt)
    {
        int v = g[i].to;
        if (v != fa)
        {
            dfs2(v, x);
        }
    }
    return;
}
vector<pair<int, int>> vv;
void hh()
{
    memset(head, -1, sizeof(head));
    cin >> n;
    cf[1] = 1;
    for (int i = 1; i < n; i++)
    {
        cf[i + 1] = 1;
        int u, v;
        cin >> u >> v;
        add(u, v);
        add(v, u);
        vv.push_back({ u,v });
    }
    cin >> m;
    for (int i = 1; i <= m; i++)
    {
        int op;
        cin >> op;
        if (op == 1)
        {
            int x, w;
            cin >> x >> w;
            cf[x] += w;
        }
        else
        {
            int y;
            cin >> y;
            y -= 1;
            int x1 = vv[y].first;
            int x2 = vv[y].second;
            dfs2(x1, x2);
            int ans2 = ans1;
            ans1 = 0;
            dfs2(x2, x1);
            cout << abs(ans1 - ans2) << endl;
            ans1 = 0;
        }
    }
}
signed main()
{
    fushen
        int T = 1;
    while (T--)
    {
        hh();
    }
    return owo;
}