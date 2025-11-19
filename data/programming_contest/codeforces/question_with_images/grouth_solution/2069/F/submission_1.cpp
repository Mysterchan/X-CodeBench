#include <bits/stdc++.h>
using namespace std;


const int N = 4e5+5;
int l[N], r[N], fa[N], sz[N];
int comps;

vector<pair<int, int>> edges[4*N];

void add(int t, int tl, int tr, int l, int r, int u, int v) {
  if (l > tr || r < tl) return;
  if (l <= tl && tr <= r) {
    edges[t].emplace_back(u, v);
    return;
  }
  int tm = (tl+tr)/2;
  add(2*t, tl, tm, l, r, u, v);
  add(2*t+1, tm+1, tr, l, r, u, v);
}

int root(int x) {
  while (x != fa[x]) x = fa[x];
  return x;
}

vector<int> ops;

void solve(int t, int tl, int tr, vector<int>& res) {
  int cnt = 0;
  for (auto [u, v]: edges[t]) {
    u = root(u);
    v = root(v);
    if (u == v) continue;
    if (sz[u] < sz[v]) swap(u, v);
    sz[u] += sz[v];
    fa[v] = u;
    cnt++;
    comps--;
    ops.emplace_back(v);
  }
  if (tl < tr) {
    int tm = (tl+tr)/2;
    solve(2*t, tl, tm, res);
    solve(2*t+1, tm+1, tr, res);
  }
  if (tl == tr) {
    res.push_back(comps);
  }
  while (cnt--) {
    int v = ops.back();
    ops.pop_back();
    int u = fa[v];
    fa[v] = v;
    sz[u] -= sz[v];
    comps++;
  }
}
int main () {
  ios_base::sync_with_stdio(0); cin.tie(0);
  int n, q;
  cin >> n >> q;
  comps = n;
  iota(fa, fa+N, 0);
  fill(sz, sz+N, 1);

  vector<tuple<char, int, int>> queries(q);
  for (auto& [c, u, v]: queries) {
    cin >> c >> u >> v;
    u--, v--;
    if (u > v) swap(u, v);
  }

  map<pair<int, int>, int> mp;
  for (int i = 0; i < q; i++) {
    auto [c, u, v] = queries[i];
    if (c == 'A') {
      if (mp.count({u, v})) {
        add(1, 0, q-1, mp[{u, v}], i-1, u, v);
        mp.erase({u, v});
      }
      else {
        mp[{u, v}] = i;
      }
    }
  }
  for (auto [e, v]: mp) {
    add(1, 0, q-1, v, q-1, e.first, e.second);
  }

  vector<int> resa;
  solve(1, 0, q-1, resa);

  mp.clear();
  set<pair<int, int>> E[2];
  for (int i = 0; i < q; i++) {
    auto [c, u, v] = queries[i];
    int z = c == 'B';
    if (E[z].count({u, v})) {
      E[z].erase({u, v});
      if (!E[z^1].count({u, v})) {
        assert(mp.count({u, v}));
        add(1, 0, q-1, mp[{u, v}], i-1, u, v);
        mp.erase({u, v});
      }
    }
    else {
      E[z].emplace(u, v);
      if (!E[z^1].count({u, v})) {
        assert(!mp.count({u, v}));
        mp[{u, v}] = i;
      }
    }
  }
  for (auto [e, v]: mp) {
    add(1, 0, q-1, v, q-1, e.first, e.second);
  }

  vector<int> resab;
  solve(1, 0, q-1, resab);
  assert((int)resa.size() == q && (int)resab.size() == q);
  for (int i = 0; i < q; i++) {
    cout << resa[i] - resab[i] << '\n';
  }
}
