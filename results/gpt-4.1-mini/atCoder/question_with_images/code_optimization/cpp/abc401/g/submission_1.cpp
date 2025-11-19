#pragma GCC optimize("Ofast")
#pragma GCC target("avx,avx2,fma")
#include <bits/stdc++.h>
using namespace std;

using ld = long double;
using pi = pair<int, int>;

int N;
vector<vector<pair<int, ld>>> G;
vector<bool> vis;
vector<int> mt;

bool try_kuhn(ld C, int v) {
    if (vis[v]) return false;
    vis[v] = true;
    for (auto &[c, w] : G[v]) {
        if (w <= C) {
            if (mt[c] == -1 || try_kuhn(C, mt[c])) {
                mt[c] = v;
                return true;
            }
        }
    }
    return false;
}

bool can(ld C) {
    mt.assign(N, -1);
    for (int v = 0; v < N; v++) {
        vis.assign(N, false);
        if (!try_kuhn(C, v)) return false;
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    vector<pair<ld, ld>> people(N), buttons(N);
    for (auto &[x, y] : people) cin >> x >> y;
    for (auto &[x, y] : buttons) cin >> x >> y;

    G.assign(N, vector<pair<int, ld>>(N));
    ld max_dist = 0;
    for (int i = 0; i < N; i++) {
        auto &[x, y] = people[i];
        for (int j = 0; j < N; j++) {
            auto &[bx, by] = buttons[j];
            ld d = hypotl(bx - x, by - y);
            G[i][j] = {j, d};
            if (d > max_dist) max_dist = d;
        }
    }

    ld lo = 0, hi = max_dist;
    for (int iter = 0; iter < 60; iter++) {
        ld mid = (lo + hi) * 0.5L;
        if (can(mid)) hi = mid;
        else lo = mid;
    }

    cout << fixed << setprecision(9) << hi << "\n";
}