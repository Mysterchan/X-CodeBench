#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <climits>

using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    if (!(cin >> T)) return 0;
    while (T--) {
        int n; cin >> n;
        vector<int> a(n + 1);
        for (int i = 1; i <= n; i++) cin >> a[i];
        vector<vector<int>> g(n + 1);
        for (int i = 0; i < n - 1; i++) {
            int u, v; cin >> u >> v;
            g[u].push_back(v);
            g[v].push_back(u);
        }

        vector<int> tin(n + 1), tout(n + 1), ord(n + 1);
        ord[0] = 0;
        int timer = 0;
        vector<int> parent(n + 1, 0), it_index(n + 1, 0);
        vector<int> st; st.reserve(n * 2);
        st.push_back(1);
        parent[1] = 0;
        while (!st.empty()) {
            int u = st.back();
            if (it_index[u] == 0) {
                timer++;
                tin[u] = timer;
                ord[timer] = u;
            }
            if (it_index[u] < (int)g[u].size()) {
                int v = g[u][it_index[u]++];
                if (v == parent[u]) continue;
                parent[v] = u;
                st.push_back(v);
            } else {
                tout[u] = timer;
                st.pop_back();
            }
        }

        vector<int> bit(n + 1);
        for (int pos = 1; pos <= n; ++pos)
            bit[pos] = a[ord[pos]];

        map<int, pair<int, int>> intervals;
        {
            int l = 1;
            for (int pos = 2; pos <= n; ++pos) {
                if (bit[pos] != bit[pos - 1]) {
                    intervals[l] = {pos - 1, bit[l]};
                    l = pos;
                }
            }
            intervals[l] = {n, bit[l]};
            for (auto &kv : intervals) {
                int left = kv.first;
                kv.second.second = bit[left];
            }
        }

        set<int> ones;
        for (int pos = 1; pos <= n; ++pos)
            if (bit[pos] == 1) ones.insert(pos);

        auto succ_in_ones = [&](int p) -> int {
            auto it = ones.upper_bound(p);
            return (it == ones.end()) ? INT_MAX : *it;
        };
        auto prev_in_ones = [&](int p) -> int {
            auto it = ones.lower_bound(p);
            if (it == ones.begin()) return -1;
            --it;
            return *it;
        };

        long long ans = 0;
        for (int p : ones) {
            int u = ord[p];
            if (succ_in_ones(p) > tout[u]) ans++;
        }

        auto remove_one_pos = [&](int p) {
            int u = ord[p], s = succ_in_ones(p);
            if (s > tout[u]) ans--;
            int pr = prev_in_ones(p);
            if (pr != -1) {
                int upr = ord[pr];
                int spr_before = p;
                bool wasCount = (spr_before > tout[upr]);
                bool nowCount = (s > tout[upr]);
                if (wasCount && !nowCount) ans--;
                else if (!wasCount && nowCount) ans++;
            }
            ones.erase(p);
        };

        auto insert_one_pos = [&](int p) {
            auto it_succ = ones.upper_bound(p);
            int s = (it_succ == ones.end() ? INT_MAX : *it_succ);
            int pr = -1;
            if (it_succ != ones.begin()) {
                auto it_prev = it_succ;
                --it_prev;
                pr = *it_prev;
            }
            if (pr != -1) {
                int upr = ord[pr];
                bool beforeCount = (s > tout[upr]);
                bool afterCount = (p > tout[upr]);
                if (beforeCount && !afterCount) ans--;
                else if (!beforeCount && afterCount) ans++;
            }
            ones.insert(p);
            int u = ord[p];
            if (succ_in_ones(p) > tout[u]) ans++;
        };

        auto split_at = [&](int pos) {
            auto it = intervals.upper_bound(pos);
            if (it == intervals.begin()) return;
            --it;
            int L = it->first, R = it->second.first, val = it->second.second;
            if (L == pos || pos > R) return;
            it->second.first = pos - 1;
            intervals[pos] = {R, val};
        };

        auto flip_range = [&](int L, int R) {
            if (L > R) return;
            split_at(L);
            split_at(R + 1);
            auto it = intervals.lower_bound(L);
            vector<pair<int, pair<int, int>>> toProcess;
            while (it != intervals.end() && it->first <= R) {
                toProcess.push_back(*it);
                ++it;
            }
            for (auto &iv : toProcess) intervals.erase(iv.first);
            for (auto &iv : toProcess) {
                int l = iv.first, r = iv.second.first, v = iv.second.second;
                int newv = 1 - v;
                if (v == 1 && newv == 0) {
                    auto itpos = ones.lower_bound(l);
                    vector<int> toErase;
                    while (itpos != ones.end() && *itpos <= r) {
                        toErase.push_back(*itpos);
                        ++itpos;
                    }
                    for (int p : toErase) remove_one_pos(p);
                    intervals[l] = {r, 0};
                } else if (v == 0 && newv == 1) {
                    for (int p = l; p <= r; ++p) insert_one_pos(p);
                    intervals[l] = {r, 1};
                } else {
                    intervals[l] = {r, v};
                }
            }

            vector<int> lefts;
            for (auto &kv : intervals) lefts.push_back(kv.first);
            for (size_t i = 0; i + 1 < lefts.size(); ++i) {
                int L1 = lefts[i], L2 = lefts[i + 1];
                auto it1 = intervals.find(L1), it2 = intervals.find(L2);
                if (it1 == intervals.end() || it2 == intervals.end()) continue;
                int R1 = it1->second.first, V1 = it1->second.second;
                int R2 = it2->second.first, V2 = it2->second.second;
                if (R1 + 1 == L2 && V1 == V2) {
                    it1->second.first = R2;
                    intervals.erase(it2);
                    lefts.clear();
                    for (auto &kv : intervals) lefts.push_back(kv.first);
                    i = -1;
                }
            }
        };

        cout << ans << '\n';
        int q; cin >> q;
        while (q--) {
            int v; cin >> v;
            flip_range(tin[v], tout[v]);
            cout << ans << '\n';
        }
    }
    return 0;
}
