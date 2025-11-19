#include <bits/stdc++.h>
#include <experimental/random>
#include <ext/pb_ds/assoc_container.hpp>
using namespace std;
using namespace __gnu_pbds;

using ll = long long;
using ld = long double;
using ordered_set = tree<ll, null_type, less<ll>, rb_tree_tag, tree_order_statistics_node_update>;
using str = string;
const ll INF = 1e18, MOD = 1e9 + 7;
#define int long long

void solve();

signed main() {
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    ll q = 1;
    cin >> q;
    while (q--) {
        solve();
    }
}

vector<vector<int>> g;
vector<vector<int>> g1;

void solve() {
    int n, m, q;
    cin >> n >> m >> q;
    g.clear();
    g1.clear();
    g1.resize(n);
    g.resize(n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        g[u].push_back(v);
        g1[v].push_back(u);
    }
    vector<pair<int, int>> que(q);
    vector<vector<int>> ans(n, vector<int>(2));
    vector<int> cnt(n);
    for (int i = 0; i < n; ++i) {
        cnt[i] = g[i].size();
    }
    for (int i = 0; i < q; ++i) {
        cin >> que[i].first >> que[i].second;
        que[i].second--;
        if (que[i].first == 2) {
            cout << (ans[que[i].second][0] == 0 ? "YES" : "NO") << "\n";
        } else {
            if (ans[que[i].second][0] == 1) {
                continue;
            } else {
                deque<pair<int, int>> del;
                del.push_back({que[i].second, 0});
                ans[que[i].second][0] = 1;
                while (del.size() > 0) {
                    auto [v, c] = del.front();
                    del.pop_front();
                    for (auto to: g1[v]) {
                        if (c == 0) {
                            if (ans[to][1 - c] == 0) {
                                ans[to][1 - c] = 1;
                                del.push_back({to, 1 - c});
                            }
                        } else {
                            cnt[to]--;
                            if (cnt[to] == 0 && ans[to][0] == 0) {
                                ans[to][0] = 1;
                                del.push_back({to, 0});
                            }
                        }
                    }
                }
            }
            if (ans[que[i].second][1] == 1) {
                continue;
            } else {
                deque<pair<int, int>> del;
                del.push_back({que[i].second, 1});
                ans[que[i].second][1] = 1;
                while (del.size() > 0) {
                    auto [v, c] = del.front();
                    del.pop_front();
                    for (auto to: g1[v]) {
                        if (c == 0) {
                            if (ans[to][1 - c] == 0) {
                                ans[to][1 - c] = 1;
                                del.push_back({to, 1 - c});
                            }
                        } else {
                            cnt[to]--;
                            if (cnt[to] == 0 && ans[to][0] == 0) {
                                ans[to][0] = 1;
                                del.push_back({to, 0});
                            }
                        }
                    }
                }
            }
        }
    }
}