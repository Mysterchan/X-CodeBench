#include <bits/stdc++.h>
#define ls (p << 1)
#define rs (p << 1 | 1)
#define mid (l + r >> 1)
using namespace std;
const int N = 5e5 + 5;
int T, n, a[N], u, v, in[N], ou[N], idx, reu[N], q;
vector<int> G[N];
inline void dfs(int x, int ff = 0) {
    reu[in[x] = ++idx] = x;
    for(int y : G[x]) if(y ^ ff) {
        dfs(y, x);
    }
    reu[ou[x] = ++idx] = -x;
}
struct info {
    int L, R, ans;
    info() {
        L = R = ans = 0;
    }
    info(int op) {
        L = R = op, ans = 0;
    }
    info(int _L, int _R, int _ans) {
        L = _L, R = _R, ans = _ans;
    }
}tr[N << 2][2];
int tag[N << 2];
inline info operator + (info x, info y) {
    if(!x.L) return y;
    if(!y.L) return x;
    return info(x.L, y.R, x.ans + (x.R == 1 && y.L == -1 ? 1 : 0) + y.ans);
}
inline void updtag(int p) {
    tag[p] ^= 1, swap(tr[p][0], tr[p][1]);
}
inline void push_down(int p) {
    if(tag[p]) {
        updtag(ls), updtag(rs), tag[p] = 0;
    }
}
inline void push_up(int p) {
    tr[p][0] = tr[ls][0] + tr[rs][0], tr[p][1] = tr[ls][1] + tr[rs][1];
}
inline void build(int p, int l, int r) {
    if(l == r) {
        tr[p][0] = tr[p][1] = info();
        if(reu[l] > 0) tr[p][a[reu[l]]] = info(1);
        else tr[p][a[-reu[l]]] = info(-1);
        return ;
    }
    build(ls, l, mid), build(rs, mid + 1, r);
    push_up(p);
}
inline void modify(int p, int l, int r, int x, int y) {
    if(x <= l && r <= y) {updtag(p);return ;}
    push_down(p);
    if(mid >= x) modify(ls, l, mid, x, y);
    if(mid < y) modify(rs, mid + 1, r, x, y);
    push_up(p);
}
inline void solve() {
    scanf("%d", &n);
    for(int i = 1; i <= n; i++) scanf("%d", &a[i]);
    for(int i = 1; i < n; i++) {
        scanf("%d%d", &u, &v);
        G[u].emplace_back(v), G[v].emplace_back(u);
    }
    dfs(1);
    auto getans = [&] {
        printf("%d\n", tr[1][1].ans);
    };
    build(1, 1, idx);
    getans();
    scanf("%d", &q);
    while(q--) {
        scanf("%d", &u);
        modify(1, 1, idx, in[u], ou[u]);
        getans();
    }
}
inline void clr() {
    for(int i = 1; i <= n; i++) G[i].clear();
    idx = 0;
}
int main() {
    scanf("%d", &T);
    while(T--) {
        solve(), clr();
    }
    return 0;
}