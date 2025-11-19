#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using edge = pair<int, ll>;
using cur = pair<ll, int>;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N; cin >> N;
    vector<ll> W(N + 1);
    for (int i = 1; i <= N; i++) cin >> W[i];

    vector<int> L(N + 1), R(N + 1);
    for (int i = 1; i <= N; i++) cin >> L[i] >> R[i];

    // Build T: for each L[i], store (R[i], i)
    vector<vector<pair<int, int>>> T(2 * N + 2);
    for (int i = 1; i <= N; i++) {
        T[L[i]].emplace_back(R[i], i);
    }

    int Q; cin >> Q;
    vector<int> S(Q), U(Q);
    for (int i = 0; i < Q; i++) cin >> S[i] >> U[i];

    // Segment tree for min queries
    int size = 1;
    while (size < 2 * N + 1) size <<= 1;
    vector<ll> segtree(2 * size, LLONG_MAX);

    auto seg_update = [&](int pos, ll val) {
        pos += size - 1;
        if (segtree[pos] <= val) return; // no update needed
        segtree[pos] = val;
        while (pos > 1) {
            pos >>= 1;
            ll nv = min(segtree[pos << 1], segtree[(pos << 1) | 1]);
            if (segtree[pos] == nv) break;
            segtree[pos] = nv;
        }
    };

    auto seg_query = [&](int l, int r) -> ll {
        if (l > r) return LLONG_MAX;
        l += size - 1;
        r += size - 1;
        ll res = LLONG_MAX;
        while (l <= r) {
            if ((l & 1) == 1) res = min(res, segtree[l++]);
            if ((r & 1) == 0) res = min(res, segtree[r--]);
            l >>= 1; r >>= 1;
        }
        return res;
    };

    vector<ll> ans(Q, -1);
    // For queries that need complex processing
    vector<vector<ll>> cost(Q, vector<ll>(5, LLONG_MAX));
    vector<vector<pair<int, pair<int, int>>>> X(2 * N + 2);

    for (int i = 0; i < Q; i++) {
        int s = S[i], t = U[i];
        if (L[s] > L[t]) swap(s, t);
        S[i] = s; U[i] = t;
        if (L[t] > R[s]) {
            // Intervals disjoint, edge exists directly
            ans[i] = W[s] + W[t];
        } else {
            // Need to process complex case
            int l1 = L[s], r1 = R[s];
            int l2 = L[t], r2 = R[t];
            int minR = min(r1, r2);
            int maxR = max(r1, r2);

            // Add events for segment tree queries
            // The queries correspond to cost[i][0..4]
            // Using the same logic as original code but optimized

            // cost[i][0]: query [l1, l2]
            X[1].emplace_back(l1, make_pair(i, 0));
            X[l1].emplace_back(l2, make_pair(i, 1));
            X[l2].emplace_back(minR + 1, make_pair(i, 2));
            X[minR + 1].emplace_back(maxR + 1, make_pair(i, 3));
            X[maxR + 1].emplace_back(2 * N + 1, make_pair(i, 4));
        }
    }

    // Process from right to left
    for (int i = 2 * N; i >= 1; i--) {
        // Update segment tree with intervals starting at i
        for (auto &p : T[i]) {
            int r = p.first, id = p.second;
            seg_update(r, W[id]);
        }
        // Process queries at position i
        for (auto &q : X[i]) {
            int r = q.first;
            int idx = q.second.first;
            int t = q.second.second;
            cost[idx][t] = seg_query(i, r);
        }
    }

    // For queries that were not answered directly, run Dijkstra on small graph of 7 nodes
    // Graph nodes: 0..4 correspond to cost indices, 5 is start node, 6 is end node
    for (int i = 0; i < Q; i++) {
        if (ans[i] >= 0) continue; // already answered

        // Build graph
        vector<vector<edge>> G(7);
        // From node 5 (start) to 0,3,4 with cost cost[i][0], cost[i][3], cost[i][4]
        if (cost[i][0] != LLONG_MAX) G[5].emplace_back(0, cost[i][0]);
        if (cost[i][3] != LLONG_MAX) G[5].emplace_back(3, cost[i][3]);
        if (cost[i][4] != LLONG_MAX) G[5].emplace_back(4, cost[i][4]);

        // From 0,1,4 to 6 (end) with cost W[U[i]]
        G[0].emplace_back(6, W[U[i]]);
        G[1].emplace_back(6, W[U[i]]);
        G[4].emplace_back(6, W[U[i]]);

        // Edges between 0..4 (except self loops)
        for (int u = 0; u < 5; u++) {
            for (int v = 0; v < 5; v++) {
                if (u == v) continue;
                if (cost[i][v] != LLONG_MAX) {
                    G[u].emplace_back(v, cost[i][v]);
                }
            }
        }

        // Dijkstra on 7 nodes
        vector<ll> dist(7, LLONG_MAX);
        vector<bool> seen(7, false);
        priority_queue<cur, vector<cur>, greater<cur>> pq;
        dist[5] = W[S[i]];
        pq.emplace(dist[5], 5);

        while (!pq.empty()) {
            auto [cd, u] = pq.top(); pq.pop();
            if (seen[u]) continue;
            seen[u] = true;
            if (u == 6) break;
            for (auto &[nx, w] : G[u]) {
                if (seen[nx]) continue;
                ll nd = cd + w;
                if (nd < dist[nx]) {
                    dist[nx] = nd;
                    pq.emplace(nd, nx);
                }
            }
        }

        ans[i] = (dist[6] == LLONG_MAX) ? -1 : dist[6];
    }

    for (int i = 0; i < Q; i++) cout << ans[i] << '\n';

    return 0;
}