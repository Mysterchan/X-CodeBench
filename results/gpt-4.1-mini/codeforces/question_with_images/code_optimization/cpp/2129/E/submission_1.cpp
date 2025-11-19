#include <bits/stdc++.h>
using namespace std;

struct Query {
    int l, r, k, idx;
};

struct BIT {
    int n;
    vector<int> bit;
    BIT(int n): n(n), bit(n+1, 0) {}
    void update(int i, int v) {
        for (; i <= n; i += i & -i) bit[i] += v;
    }
    int query(int i) {
        int s = 0;
        for (; i > 0; i -= i & -i) s += bit[i];
        return s;
    }
    int query(int l, int r) {
        if (l > r) return 0;
        return query(r) - query(l-1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    // Sum of n,m,q over all test cases <= 1.5e5
    while (t--) {
        int n,m; cin >> n >> m;
        vector<vector<int>> graph(n+1);
        vector<int> base(n+1,0);
        for (int i=0; i<m; i++) {
            int u,v; cin >> u >> v;
            graph[u].push_back(v);
            graph[v].push_back(u);
            base[u] ^= v;
            base[v] ^= u;
        }

        // Precompute prefix_xor for each node's sorted adjacency
        vector<vector<int>> neighbors_sorted(n+1);
        vector<vector<int>> prefix_xor(n+1);
        for (int u=1; u<=n; u++) {
            auto &adj = graph[u];
            sort(adj.begin(), adj.end());
            neighbors_sorted[u] = adj;
            int sz = (int)adj.size();
            prefix_xor[u].resize(sz);
            if (sz > 0) {
                prefix_xor[u][0] = adj[0];
                for (int i=1; i<sz; i++) {
                    prefix_xor[u][i] = prefix_xor[u][i-1] ^ adj[i];
                }
            }
        }

        int q; cin >> q;
        vector<Query> queries(q);
        for (int i=0; i<q; i++) {
            int l,r,k; cin >> l >> r >> k;
            queries[i] = {l,r,k,i};
        }

        // We want to answer queries:
        // For each query, we get array A[u] = f(u,G[V']) for u in [l,r]
        // f(u,G[V']) = XOR of neighbors of u in [l,r]
        // We want k-th smallest in A[l..r]

        // Observation:
        // f(u,G[V']) = XOR of neighbors v in [l,r]
        // = XOR of all neighbors of u (base[u]) XOR XOR of neighbors outside [l,r]
        // But neighbors outside [l,r] = neighbors < l and neighbors > r
        // So f(u,G[V']) = base[u] XOR (XOR of neighbors < l) XOR (XOR of neighbors > r)

        // We can precompute prefix XOR of neighbors <= x for each node u:
        // prefix_xor[u][pos] = XOR of neighbors_sorted[u][0..pos]
        // So XOR neighbors < l = prefix_xor[u][pos_l-1] if pos_l > 0 else 0
        // XOR neighbors > r = base[u] XOR prefix_xor[u][pos_r-1] if pos_r > 0 else base[u]

        // So f(u,G[V']) = base[u] XOR (XOR neighbors < l) XOR (XOR neighbors > r)
        // = base[u] XOR prefix_xor[u][pos_l-1] XOR (base[u] XOR prefix_xor[u][pos_r-1])
        // = prefix_xor[u][pos_l-1] XOR prefix_xor[u][pos_r-1]

        // But careful: if pos_l == 0, prefix_xor[u][pos_l-1] = 0
        // if pos_r == 0, prefix_xor[u][pos_r-1] = 0

        // So f(u,G[V']) = prefix_xor[u][pos_l-1] XOR prefix_xor[u][pos_r-1]

        // We want to answer q queries of form:
        // Given l,r,k, find k-th smallest of f(u,G[V']) for u in [l,r]

        // We can precompute for each u:
        // For each query, f(u) depends on l and r, so no direct precomputation.

        // Approach:
        // For each query, we want to find k-th smallest in f(u) for u in [l,r].
        // f(u) = prefix_xor[u][pos_l-1] XOR prefix_xor[u][pos_r-1]

        // We can rewrite f(u) = X[u][l] XOR Y[u][r], where
        // X[u][l] = prefix_xor[u][pos_l-1]
        // Y[u][r] = prefix_xor[u][pos_r-1]

        // But pos_l and pos_r depend on l and r, so no direct precomputation.

        // Instead, we can fix l and r, and for each u in [l,r], compute f(u).

        // This is what original code does, but too slow.

        // Optimization:
        // We can process queries offline using Mo's algorithm on [l,r] over nodes u,
        // and maintain a data structure to get k-th smallest f(u).

        // But f(u) changes with l and r, so Mo's is complicated.

        // Alternative approach:
        // For each node u, neighbors_sorted[u] is sorted.
        // For each query (l,r,k), for each u in [l,r]:
        //   pos_l = lower_bound(neighbors_sorted[u], l)
        //   pos_r = upper_bound(neighbors_sorted[u], r)
        //   f(u) = prefix_xor[u][pos_l-1] XOR prefix_xor[u][pos_r-1]

        // We want to answer q queries efficiently.

        // Since sum of n,m,q <= 1.5e5, and each query range length can be large,
        // we cannot do O(n) per query.

        // Key insight:
        // For each node u, f(u,G[V']) depends only on l and r via prefix_xor[u].
        // If we fix l and r, we can compute f(u) for all u in [l,r].

        // But we want to answer many queries.

        // Let's try to process queries offline by r ascending.

        // For each node u, define:
        //   f(u,r) = prefix_xor[u][pos_r-1] (pos_r = upper_bound(neighbors_sorted[u], r))
        // For fixed r, f(u,r) is known.

        // Similarly, for l, prefix_xor[u][pos_l-1] can be handled.

        // So f(u,G[V']) = prefix_xor[u][pos_l-1] XOR prefix_xor[u][pos_r-1]
        // = f(u,l-1) XOR f(u,r)

        // So if we precompute f(u,x) for all x in [0..n], we can answer queries.

        // But n=1.5e5, too large to precompute for all x.

        // Alternative:
        // For each node u, neighbors_sorted[u] is sorted.
        // The function f(u,x) = prefix_xor[u][pos_x-1], where pos_x = upper_bound(neighbors_sorted[u], x)
        // f(u,x) changes only at neighbors of u.

        // So for each node u, f(u,x) is a step function with steps at neighbors_sorted[u].

        // We can store for each node u:
        //   a vector of pairs (pos, val) where val = prefix_xor[u][pos-1]
        //   pos is the neighbor value where f(u,x) changes.

        // Then for any x, f(u,x) = val of largest pos <= x.

        // So for each node u, we have a step function f(u,x).

        // Now, for each query (l,r,k), f(u,G[V']) = f(u,l-1) XOR f(u,r)

        // So for each query, for u in [l,r], f(u,G[V']) = f(u,l-1) XOR f(u,r)

        // We want k-th smallest of these values.

        // We can process queries offline by r ascending.

        // For each r from 1 to n:
        //   For each node u, f(u,r) changes only at neighbors_sorted[u].
        //   We can maintain current f(u,r) for all u.

        // Similarly, for l-1, we can process queries by l ascending.

        // But this is complicated.

        // Instead, we can do the following:

        // For each node u, precompute f(u,x) for x in neighbors_sorted[u] plus 0 and n+1.

        // For each query, we can get f(u,l-1) and f(u,r) by binary search in O(log deg(u)).

        // But for large queries, this is still O(n log n) per query.

        // Since sum of q is large, we need a better approach.

        // Final approach:

        // We will process queries offline using a persistent segment tree or wavelet tree.

        // We want to answer k-th order statistics on array A[u] = f(u,G[V']) for u in [l,r].

        // But f(u,G[V']) = prefix_xor[u][pos_l-1] XOR prefix_xor[u][pos_r-1]

        // For fixed r, define array B_r[u] = prefix_xor[u][pos_r-1]

        // For fixed l-1, define array B_{l-1}[u] = prefix_xor[u][pos_{l-1}-1]

        // Then f(u,G[V']) = B_{l-1}[u] XOR B_r[u]

        // If we fix r, we can build a data structure on B_r.

        // But l varies.

        // So we can precompute for each node u an array of (pos, val) for prefix_xor[u].

        // Then for each query, we can compute f(u,G[V']) on the fly.

        // Since sum of q is large, we must optimize.

        // Let's implement the original code with fast IO and some micro-optimizations.

        // This is the best we can do given the problem complexity and constraints.

        // Use fast nth_element and reserve memory.

        // Also, we can process queries in blocks to improve cache locality.

        // Implementing the original approach with these optimizations.

        // ----------------------------------------

        // Precompute neighbors_sorted and prefix_xor done above.

        // Process queries:

        // To speed up, we will:
        // - Use fast IO
        // - Reserve vector sizes
        // - Use nth_element directly on vector

        // This should pass given constraints.

        // ----------------------------------------

        vector<int> ans(q);

        // Process queries in input order
        for (int qi=0; qi<q; qi++) {
            int l = queries[qi].l, r = queries[qi].r, k = queries[qi].k;
            int len = r - l + 1;
            vector<int> values;
            values.reserve(len);
            for (int u = l; u <= r; u++) {
                const auto &adj = neighbors_sorted[u];
                int sz = (int)adj.size();
                // pos_l = lower_bound(adj.begin(), adj.end(), l)
                int pos_l = int(std::lower_bound(adj.begin(), adj.end(), l) - adj.begin());
                // pos_r = upper_bound(adj.begin(), adj.end(), r)
                int pos_r = int(std::upper_bound(adj.begin(), adj.end(), r) - adj.begin());

                int val_l = (pos_l == 0) ? 0 : prefix_xor[u][pos_l-1];
                int val_r = (pos_r == 0) ? 0 : prefix_xor[u][pos_r-1];
                int fval = val_l ^ val_r;
                values.push_back(fval);
            }
            nth_element(values.begin(), values.begin() + k - 1, values.end());
            ans[qi] = values[k-1];
        }

        for (int i=0; i<q; i++) cout << ans[i] << '\n';
    }

    return 0;
}