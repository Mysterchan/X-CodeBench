#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
const ll inf = 0x3f3f3f3f3f3f3f3f;
#define rep(i, l, r) for (int i = l; i <= r; i++)
#define rep_(i, l, r) for (int i = l; i >= r; i--)
#define cy cout << "YES" << '\n'
#define cn cout << "NO" << '\n'
#define xx first
#define yy second
#define pb push_back
#define endl '\n'
const int N = 3e5 + 10;
int _ = 1;
struct SegmentTree
{
    int l, r;
    int dat;
} t[N * 4];
void build(int p, int l, int r)
{
    t[p].l = l, t[p].r = r;
    if (l == r)
    {
        t[p].dat = 1;
        return;
    }
    int mid = (l + r) >> 1;
    build(p * 2, l, mid);
    build(p * 2 + 1, mid + 1, r);
    t[p].dat = t[p * 2].dat + t[p * 2 + 1].dat;
}
void change(int p, int x, int v)
{
    if (t[p].l == t[p].r)
    {
        t[p].dat += v;
        return;
    }
    int mid = (t[p].l + t[p].r) >> 1;
    if (x <= mid)
        change(p * 2, x, v);
    else
        change(p * 2 + 1, x, v);
    t[p].dat = t[p * 2].dat + t[p * 2 + 1].dat;
}
int ask(int p, int l, int r)
{
    if (l <= t[p].l && r >= t[p].r)
        return t[p].dat;
    int mid = (t[p].l + t[p].r) >> 1;
    int val = 0;
    if (l <= mid)
        val += ask(p * 2, l, r);
    if (r > mid)
        val += ask(p * 2 + 1, l, r);
    return val;
}
vector<int> e[N];
int u[N], v[N], dfn[N], siz[N], tot;
void dfs(int x, int fa)
{
    siz[x] = 1;
    dfn[x] = ++tot;
    for (int ne : e[x])
    {
        if (ne != fa)
        {
            dfs(ne, x);
            siz[x] += siz[ne];
        }
    }
}
void xiaozong85()
{
    int n;
    cin >> n;
    rep(i, 1, n - 1)
    {
        cin >> u[i] >> v[i];
        e[u[i]].pb(v[i]);
        e[v[i]].pb(u[i]);
    }
    dfs(1, 0);
    build(1, 1, n);
    int sum = n;
    int q;
    cin >> q;
    while (q--)
    {
        int op;
        cin >> op;
        if (op == 1)
        {
            int x, w;
            cin >> x >> w;
            change(1, dfn[x], w);
            sum += w;
        }
        else
        {
            int y;
            cin >> y;
            y = v[y];
            int t1 = sum - ask(1, dfn[y], dfn[y] + siz[y] - 1);
            int t2 = ask(1, dfn[y], dfn[y] + siz[y] - 1);
            cout << abs(t1 - t2) << endl;
        }
    }
}
signed main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    while (_--)
    {
        xiaozong85();
    }
    return 0;
}