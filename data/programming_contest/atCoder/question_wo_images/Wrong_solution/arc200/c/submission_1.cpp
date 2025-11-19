#include <bits/stdc++.h>
using namespace std;

#define FAST ios_base::sync_with_stdio(false);cin.tie(NULL);
using ll = long long;

const int INF = 1'000'000'000;
const int MX = 500;
bool g[MX][MX], taken[MX];
int din[MX], dis[MX][MX];

void init(int n) {
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      g[i][j] = 0;
      dis[i][j] = INF;
    }
    din[i] = 0;
    taken[i] = 0;
    dis[i][i] = 0;
  }
}

int main() {
  FAST;
  
  int tc = 1, ti;
  cin >> tc;

  for (ti = 1; ti <= tc; ++ti) {
    int n;
    cin >> n;
    init(n);

    vector<int> L(n), R(n);
    for (int i = 0; i < n; ++i) {
      int l, r; cin >> l >> r; --l; --r;
      L[i] = l;
      R[i] = r;
    }

    for (int u = 0; u < n; ++u) for (int v = 0; v < n; ++v) {
      if ((L[v] < L[u]) && (R[u] < R[v])) {
        g[u][v] = 1;
        dis[u][v] = 1;
        din[v] += 1;
      }
    }

    for (int k = 0; k < n; ++k) {
      for (int u = 0; u < n; ++u) for (int v = 0; v < n; ++v) {
        dis[u][v] = min(dis[u][v], dis[u][k] + dis[k][v]);
      }
    }

    auto mark_taken = [&](int u) -> void {
      for (int v = 0; v < n; ++v) if (g[u][v]) {
        g[u][v] = 0;
        din[v] -= 1;
      }
      taken[u] = 1;
    };

    vector<int> ans(n, -1);
    int mn_id = 0;
    for (int x = 0; x < n; ++x) {
      while (taken[mn_id]) mn_id += 1;

      int take = -1;

      if (din[mn_id] == 0) {
        take = mn_id;
      } else {
        int take_dis = INF;
        for (int u = 0; u < n; ++u) if (u != mn_id) {
          if (!taken[u] && (din[u] == 0) && (dis[u][mn_id] != INF)) {
            if (dis[u][mn_id] < take_dis) {
              take_dis = dis[u][mn_id];
              take = u;
            } else if (dis[u][mn_id] == take_dis) {
              take = min(take, u);
            }
          }
        }
      }

      assert(take != -1);
      ans[take] = x;
      mark_taken(take);
    }

    for (int i = 0; i < n; ++i) cout << ans[i]+1 << " ";
    cout << "\n";
  }

  return 0;
}
