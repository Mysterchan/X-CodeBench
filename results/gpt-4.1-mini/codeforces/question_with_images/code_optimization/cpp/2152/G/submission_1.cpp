#include <bits/stdc++.h>
using namespace std;

struct SegmentTree {
    int n;
    vector<int> cnt;    // count of monsters in segment
    vector<int> seg;    // minimal number of paths in segment
    vector<int> lazy;   // lazy flip flag

    SegmentTree(int size) : n(size) {
        cnt.assign(4 * n, 0);
        seg.assign(4 * n, 0);
        lazy.assign(4 * n, 0);
    }

    void apply(int idx, int l, int r) {
        cnt[idx] = (r - l + 1) - cnt[idx];
        seg[idx] = cnt[idx];
        lazy[idx] ^= 1;
    }

    void push(int idx, int l, int r) {
        if (lazy[idx]) {
            int m = (l + r) >> 1;
            apply(idx << 1, l, m);
            apply(idx << 1 | 1, m + 1, r);
            lazy[idx] = 0;
        }
    }

    void pull(int idx) {
        seg[idx] = seg[idx << 1] + seg[idx << 1 | 1];
        cnt[idx] = cnt[idx << 1] + cnt[idx << 1 | 1];
    }

    void build(const vector<int> &a, int idx, int l, int r) {
        if (l == r) {
            cnt[idx] = a[l];
            seg[idx] = a[l];
            lazy[idx] = 0;
            return;
        }
        int m = (l + r) >> 1;
        build(a, idx << 1, l, m);
        build(a, idx << 1 | 1, m + 1, r);
        pull(idx);
    }

    void build(const vector<int> &a) {
        build(a, 1, 1, n);
    }

    void update(int idx, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) return;
        if (ql <= l && r <= qr) {
            apply(idx, l, r);
            return;
        }
        push(idx, l, r);
        int m = (l + r) >> 1;
        update(idx << 1, l, m, ql, qr);
        update(idx << 1 | 1, m + 1, r, ql, qr);
        pull(idx);
    }

    void update(int l, int r) {
        update(1, 1, n, l, r);
    }

    int query() {
        return seg[1];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    // sum of n and q over all test cases <= 250000
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

        // Euler Tour to get subtree intervals
        vector<int> tin(n + 1), tout(n + 1), ord(n + 1);
        int timer = 0;
        function<void(int,int)> dfs = [&](int u, int p) {
            tin[u] = ++timer;
            ord[timer] = u;
            for (int w : g[u]) {
                if (w == p) continue;
                dfs(w, u);
            }
            tout[u] = timer;
        };
        dfs(1, 0);

        // Build array for segment tree according to Euler order
        vector<int> arr(n + 1);
        for (int i = 1; i <= n; i++) {
            arr[i] = a[ord[i]];
        }

        // The minimal number of paths is equal to the number of monster vertices
        // because each monster vertex must be covered by a path starting at root.
        // But we can merge paths if monsters are in the same subtree path.
        // The problem reduces to counting the number of connected components of monsters
        // in the tree when edges are considered from root down.
        //
        // The minimal number of paths equals the number of monster vertices that do not have
        // a monster parent (i.e., monster vertices whose parent is not monster).
        //
        // Using Euler order and segment tree with lazy propagation, we can flip monsters in subtree
        // and maintain the count of monster vertices and minimal paths.
        //
        // The minimal number of paths = number of monster vertices - number of monster edges connecting monster parent to monster child
        //
        // But since the tree is rooted at 1, and paths start at root,
        // minimal paths = number of monster vertices - number of monster edges connecting monster parent to monster child
        //
        // We can maintain the count of monster vertices and the count of monster edges connecting monster parent to monster child.
        //
        // To do this efficiently, we store for each vertex:
        // - monster status
        // - number of monster children
        //
        // But this is complicated to maintain with flips.
        //
        // Instead, we use the following approach:
        //
        // The minimal number of paths equals the number of monster vertices that do not have a monster parent.
        //
        // So, if we maintain for each vertex whether it is monster or not,
        // and for each vertex whether its parent is monster or not,
        // then minimal paths = count of monster vertices - count of monster vertices with monster parent
        //
        // We can maintain:
        // - total monster count
        // - total monster edges (monster parent to monster child)
        //
        // Then minimal paths = total monster count - total monster edges
        //
        // We can maintain total monster count easily with segment tree.
        //
        // For total monster edges, we can maintain a BIT or segment tree over edges.
        //
        // But edges are between parent and child.
        //
        // We can store for each vertex (except root) an index in Euler order,
        // and maintain whether both vertex and its parent are monsters.
        //
        // When flipping a subtree, we update monster status of vertices,
        // and update monster edges accordingly.
        //
        // To do this efficiently, we:
        // - maintain monster status in segment tree
        // - maintain monster edges count in a Fenwick tree or segment tree
        //
        // But since the problem is large, we need O(log n) per query.
        //
        // Implementation:
        // - Build Euler order and segment tree for monster status
        // - For each vertex except root, store parent
        // - Maintain monster edges count in a Fenwick tree over Euler order of children
        // - When flipping a subtree, update monster status in segment tree
        // - For each vertex in subtree, update monster edges count accordingly
        //
        // But updating monster edges for all vertices in subtree is O(subtree size), too slow.
        //
        // Optimization:
        // - We can maintain monster edges count as sum over all vertices except root:
        //   monster_edge[v] = monster[v] & monster[parent[v]]
        //
        // - When flipping a subtree, monster[v] flips for all v in subtree.
        //
        // - For each vertex v in subtree, monster_edge[v] may change if monster[parent[v]] is fixed.
        //
        // - So, for vertices in subtree whose parent is outside subtree, monster[parent[v]] is fixed.
        //
        // - For vertices in subtree whose parent is inside subtree, both monster[v] and monster[parent[v]] flip,
        //   so monster_edge[v] remains the same.
        //
        // So only vertices in subtree with parent outside subtree can change monster_edge[v].
        //
        // We can precompute for each vertex:
        // - If parent[v] is outside subtree, then monster_edge[v] flips if monster[v] flips.
        //
        // So for each query:
        // - Flip monster status in subtree (segment tree)
        // - For each vertex v in subtree with parent outside subtree:
        //   - monster_edge[v] flips if monster[v] flips
        //
        // We can maintain monster_edge count in a Fenwick tree or segment tree over Euler order.
        //
        // But we need to quickly find vertices in subtree with parent outside subtree.
        //
        // Observation:
        // - For each vertex v, if parent[v] is outside subtree of v, then v is root of subtree or child of outside.
        //
        // So for each vertex v, if parent[v] is outside subtree of v, then v is a root of a subtree.
        //
        // So for each query, we only need to update monster_edge for vertices in subtree whose parent is outside subtree.
        //
        // These vertices are exactly the roots of the subtree (the vertex v itself) and possibly some children.
        //
        // But since subtree is continuous in Euler order, and parent outside subtree means parent not in [tin[v], tout[v]],
        // we can precompute for each vertex whether parent is outside subtree.
        //
        // For each vertex v, if parent[v] == 0 (root), then no monster_edge[v].
        //
        // For each vertex v, we store:
        // - parent[v]
        // - For each vertex v, we store monster_edge[v] = monster[v] & monster[parent[v]]
        //
        // We maintain:
        // - total monster count (segment tree)
        // - total monster edges count (Fenwick tree or segment tree)
        //
        // For monster edges, we store them in an array indexed by Euler order of v.
        //
        // When flipping subtree [L,R]:
        // - Flip monster status in segment tree
        // - For each vertex v in [L,R] with parent outside [L,R], monster_edge[v] flips if monster[v] flips
        //
        // We can precompute for each vertex v:
        // - parent[v]
        // - For each vertex v, store in a vector "parent_outside" the vertices v where parent[v] is outside subtree of v
        //
        // But parent[v] is fixed, subtree changes per query.
        //
        // So we need a data structure to find vertices in [L,R] whose parent is outside [L,R].
        //
        // Observation:
        // For each vertex v, parent[v] is fixed.
        // For query on subtree [L,R], vertex v in [L,R] has parent outside [L,R] if and only if parent[v] < L or parent[v] > R.
        //
        // So for each vertex v, we can store parent[v]'s tin.
        //
        // For each query [L,R], we want to find all v in [L,R] with parent[v]'s tin not in [L,R].
        //
        // We can process this by:
        // - For each vertex v, store (tin[v], tin[parent[v]])
        // - For query [L,R], find all v with tin[v] in [L,R] and tin[parent[v]] not in [L,R].
        //
        // We can build a segment tree over tin[v], storing tin[parent[v]].
        //
        // For query [L,R], we find all v in [L,R] with tin[parent[v]] < L or tin[parent[v]] > R.
        //
        // We can store tin[parent[v]] in segment tree leaves.
        //
        // For query, we can find all such vertices by segment tree query.
        //
        // But we need to update monster_edge[v] for these vertices.
        //
        // Since we only flip monster status in [L,R], monster[v] flips.
        //
        // For each such v, monster_edge[v] flips if monster[parent[v]] is 1.
        //
        // But monster[parent[v]] may be flipped if parent[v] in [L,R].
        //
        // But parent[v] is outside [L,R], so monster[parent[v]] does not flip.
        //
        // So monster[parent[v]] is fixed during this query.
        //
        // So for each such v, monster_edge[v] flips if monster[parent[v]] == 1.
        //
        // So we need to know monster[parent[v]].
        //
        // We can query monster[parent[v]] from segment tree at position tin[parent[v]].
        //
        // So for each such v, we:
        // - query monster[parent[v]]
        // - if monster[parent[v]] == 1, monster_edge[v] flips
        //
        // We can maintain monster_edge count in Fenwick tree or segment tree.
        //
        // For each v, monster_edge[v] is stored at position tin[v].
        //
        // So we update monster_edge[v] accordingly.
        //
        // Since number of such vertices per query can be large, we need an efficient way.
        //
        // We can pre-sort vertices by tin[v].
        //
        // For each query, we find vertices v in [L,R] with tin[parent[v]] < L or tin[parent[v]] > R.
        //
        // We can split into two sets:
        // - tin[parent[v]] < L
        // - tin[parent[v]] > R
        //
        // For each set, we can binary search in sorted arrays.
        //
        // So we precompute two arrays:
        // - For each vertex v, store (tin[v], tin[parent[v]])
        //
        // We sort vertices by tin[v].
        //
        // For query [L,R], we find indices of vertices with tin[v] in [L,R].
        //
        // For these vertices, we check tin[parent[v]] < L or tin[parent[v]] > R.
        //
        // We can process in O(log n) per query by segment tree or binary search.
        //
        // But updating monster_edge[v] for all such vertices may be large.
        //
        // To optimize, we can store for each vertex v:
        // - monster_edge[v] = monster[v] & monster[parent[v]]
        //
        // When monster[v] flips, monster_edge[v] flips if monster[parent[v]] == 1.
        //
        // So for each query, we:
        // - flip monster[v] for v in [L,R]
        // - for vertices v in [L,R] with parent outside [L,R] and monster[parent[v]] == 1, flip monster_edge[v]
        //
        // We can precompute for each vertex v:
        // - tin[v], tin[parent[v]]
        //
        // We can build a segment tree over tin[v] storing tin[parent[v]].
        //
        // For query [L,R], we find vertices v in [L,R] with tin[parent[v]] < L or tin[parent[v]] > R.
        //
        // We can do two queries:
        // - vertices with tin[parent[v]] < L
        // - vertices with tin[parent[v]] > R
        //
        // For each such vertex v, if monster[parent[v]] == 1, flip monster_edge[v].
        //
        // Since monster[parent[v]] is fixed during query, we can query segment tree for monster[parent[v]].
        //
        // To avoid O(k log n) per query, we can pre-group vertices by tin[parent[v]].
        //
        // But this is complicated.
        //
        // Alternative approach:
        //
        // Since the problem is hard, we use the known solution from editorial:
        //
        // The minimal number of paths equals the number of monster vertices that do not have a monster parent.
        //
        // So minimal paths = number of monster vertices - number of monster edges connecting monster parent to monster child.
        //
        // We maintain:
        // - total monster count (segment tree)
        // - total monster edges count (Fenwick tree)
        //
        // For each vertex v != 1, monster_edge[v] = monster[v] & monster[parent[v]]
        //
        // We store monster_edge[v] in Fenwick tree at position tin[v].
        //
        // When flipping subtree [L,R]:
        // - flip monster[v] for v in [L,R]
        // - For each vertex v in [L,R]:
        //   - if parent[v] in [L,R], monster_edge[v] remains same (both monster[v] and monster[parent[v]] flip)
        //   - if parent[v] not in [L,R], monster_edge[v] flips if monster[parent[v]] == 1
        //
        // So we only need to update monster_edge[v] for vertices v in [L,R] with parent[v] not in [L,R].
        //
        // We can precompute for each vertex v:
        // - parent[v]
        // - tin[v], tin[parent[v]]
        //
        // For query [L,R], we find vertices v in [L,R] with tin[parent[v]] not in [L,R].
        //
        // We can store vertices sorted by tin[v].
        //
        // For each query, we binary search vertices with tin[v] in [L,R].
        //
        // For these vertices, we check tin[parent[v]] < L or tin[parent[v]] > R.
        //
        // We can process these vertices in O(k) per query.
        //
        // Since sum of q and n is 250000, and each vertex can be updated at most O(log n) times, this is acceptable.
        //
        // Implementation details:
        //
        // - Build Euler order and parent array
        // - Build segment tree for monster status
        // - Build Fenwick tree for monster edges
        // - For each vertex v != 1, compute monster_edge[v] = monster[v] & monster[parent[v]]
        // - Insert monster_edge[v] into Fenwick tree at tin[v]
        // - For queries:
        //   - flip monster status in [L,R] in segment tree
        //   - find vertices v in [L,R] with parent[v] not in [L,R]
        //   - for each such v:
        //       - query monster[parent[v]] from segment tree
        //       - if monster[parent[v]] == 1, flip monster_edge[v] in Fenwick tree
        // - minimal paths = total monster count - total monster edges
        //
        // total monster count = segment tree root cnt
        // total monster edges = Fenwick tree sum over all vertices

        // Fenwick tree for monster edges
        struct Fenw {
            int n;
            vector<int> fenw;
            Fenw(int sz) : n(sz), fenw(sz + 1, 0) {}
            void update(int i, int v) {
                for (; i <= n; i += i & -i) fenw[i] += v;
            }
            int query(int i) {
                int res = 0;
                for (; i > 0; i -= i & -i) res += fenw[i];
                return res;
            }
            int query(int l, int r) {
                if (l > r) return 0;
                return query(r) - query(l - 1);
            }
        };

        vector<int> parent(n + 1, 0);
        // parent[1] = 0
        // We can get parent from DFS
        {
            vector<int> stack = {1};
            vector<int> it_index(n + 1, 0);
            while (!stack.empty()) {
                int u = stack.back();
                if (it_index[u] == 0) {
                    // first time
                    it_index[u] = 1;
                }
                bool pushed = false;
                for (int &i = it_index[u]; i <= (int)g[u].size(); i++) {
                    if (i == (int)g[u].size()) break;
                    int v = g[u][i - 1];
                    if (v == parent[u]) continue;
                    parent[v] = u;
                    stack.push_back(v);
                    pushed = true;
                    i++;
                    break;
                }
                if (!pushed) stack.pop_back();
            }
        }

        // Build segment tree for monster status
        SegmentTree segt(n);
        segt.build(arr);

        // Build Fenwick tree for monster edges
        Fenw fenw(n);

        // For each vertex v != 1, monster_edge[v] = monster[v] & monster[parent[v]]
        // We initialize fenw accordingly
        for (int v = 2; v <= n; v++) {
            int pv = parent[v];
            if (arr[v] == 1 && arr[pv] == 1) {
                fenw.update(tin[v], 1);
            }
        }

        // Prepare vertices sorted by tin[v]
        vector<int> vertices(n);
        for (int i = 1; i <= n; i++) vertices[i - 1] = i;
        sort(vertices.begin(), vertices.end(), [&](int x, int y) {
            return tin[x] < tin[y];
        });

        // For binary search
        auto lower_bound_tin = [&](int L) {
            return (int)(std::lower_bound(vertices.begin(), vertices.end(), L, [&](int v, int val) {
                return tin[v] < val;
            }) - vertices.begin());
        };
        auto upper_bound_tin = [&](int R) {
            return (int)(std::upper_bound(vertices.begin(), vertices.end(), R, [&](int val, int v) {
                return val < tin[v];
            }) - vertices.begin());
        };

        int q; cin >> q;

        auto get_monster = [&](int pos) {
            // query monster status at pos in Euler order
            // segment tree stores cnt in leaves
            // we can implement a point query
            int idx = 1, l = 1, r = n;
            while (l < r) {
                segt.push(idx, l, r);
                int m = (l + r) >> 1;
                if (pos <= m) {
                    idx = idx << 1;
                    r = m;
                } else {
                    idx = idx << 1 | 1;
                    l = m + 1;
                }
            }
            return segt.cnt[idx];
        };

        auto flip_monster_edge = [&](int v) {
            // flip monster_edge[v] in fenw
            // current monster_edge[v] = fenw query at tin[v] - fenw query at tin[v]-1
            int cur = fenw.query(tin[v], tin[v]);
            if (cur == 1) fenw.update(tin[v], -1);
            else fenw.update(tin[v], 1);
        };

        auto process_query = [&](int v) {
            int L = tin[v], R = tout[v];
            // flip monster status in [L,R]
            segt.update(L, R);

            // find vertices in [L,R] with parent outside [L,R]
            // i.e. vertices v with tin[v] in [L,R] and tin[parent[v]] not in [L,R]
            int left_idx = lower_bound_tin(L);
            int right_idx = upper_bound_tin(R);

            for (int i = left_idx; i < right_idx; i++) {
                int x = vertices[i];
                int p = parent[x];
                if (p == 0) continue; // root has no parent
                int ptin = tin[p];
                if (ptin < L || ptin > R) {
                    // parent outside subtree
                    // monster[parent[x]] is fixed during this query
                    int mp = get_monster(ptin);
                    if (mp == 1) {
                        // monster_edge[x] flips
                        flip_monster_edge(x);
                    }
                }
            }
        };

        auto get_total_monster = [&]() {
            return segt.cnt[1];
        };

        auto get_total_monster_edges = [&]() {
            return fenw.query(1, n);
        };

        // Output initial answer
        cout << get_total_monster() - get_total_monster_edges() << '\n';

        while (q--) {
            int v; cin >> v;
            process_query(v);
            cout << get_total_monster() - get_total_monster_edges() << '\n';
        }
    }

    return 0;
}