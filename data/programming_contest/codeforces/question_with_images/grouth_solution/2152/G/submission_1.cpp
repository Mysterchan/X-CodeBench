#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using V = vector<ll>;

struct S {
    ll l1, lc, r1, rc;
};
S e() { return {LLONG_MAX, 0, LLONG_MIN, 0}; }
S op(S l, S r) {
    S res;
    res.l1 = min(l.l1, r.l1);
    res.lc = (l.l1 == res.l1 ? l.lc : 0) + (r.l1 == res.l1 ? r.lc : 0);
    res.r1 = min(l.r1, r.r1);
    res.rc = (l.r1 == res.r1 ? l.rc : 0) + (r.r1 == res.r1 ? r.rc : 0);
    return res;
}
struct F {
    ll a, b;
};
S mapping(F f, S x) {
    if (!f.a && !f.b) return x;
    if (f.a) {
        swap(x.l1, x.r1);
        swap(x.lc, x.rc);
    }
    x.l1 += f.b;
    x.r1 -= f.b;
    return x;
}
F composition(F f, F x) {
    if (f.a) {
        x.a ^= 1;
        x.b = -x.b;
    }
    x.b += f.b;
    return x;
}
F id() { return {0, 0}; }

namespace nachia {

struct Graph {
    struct Edge {
        int from, to;
    };
    int n;
    vector<Edge> edges;
    Graph(int n, const vector<pair<int, int>>& edges) : n(n) {
        for (auto [u, v] : edges) this->edges.push_back({u, v});
    }
};

struct HeavyLightDecomposition {
    int n;
    vector<int> parent, depth, heavyRoot, rangeL, rangeR, index;
    HeavyLightDecomposition(const Graph& tree, int root = 0) {
        n = tree.n;
        parent.assign(n, -1);
        depth.assign(n, 0);
        heavyRoot.assign(n, 0);
        rangeL.assign(n, 0);
        rangeR.assign(n, 0);
        index.assign(n, 0);

        vector<int> size(n, 1);
        vector<int> order;
        function<void(int)> dfs = [&](int v) {
            order.push_back(v);
            for (auto e : tree.edges) {
                int u = e.to;
                if (u == parent[v]) continue;
                parent[u] = v;
                depth[u] = depth[v] + 1;
                dfs(u);
                size[v] += size[u];
                if (size[u] > size[heavyRoot[v]]) heavyRoot[v] = u;
            }
        };
        dfs(root);

        int t = 0;
        for (int v : order) {
            if (v == root || heavyRoot[parent[v]] != v) {
                for (int u = v; u != -1; u = heavyRoot[u]) {
                    rangeL[u] = t++;
                    index[u] = v;
                }
            }
        }
        for (int v = 0; v < n; ++v) rangeR[v] = rangeL[v] + size[v];
    }

    pair<int, int> subtree(int v) const { return {rangeL[v], rangeR[v]}; }
    int parentOf(int v) const { return parent[v]; }
};

} 

void testcase() {
    ll n;
    cin >> n;
    V a(n);
    for (ll& x : a) cin >> x;

    vector<pair<int, int>> edges(n - 1);
    for (auto& [u, v] : edges) {
        cin >> u >> v;
        --u, --v;
    }

    auto tree = nachia::Graph(n, edges);
    auto hld = nachia::HeavyLightDecomposition(tree);

    V<S> init(n);
    for (int i = 0; i < n; ++i) {
        init[i] = {a[i], 1, -a[i], 1};
    }

    nachia::LazySegtree<S, F, op, composition, mapping> seg(init, e(), id());

    auto query = [&]() {
        auto res = seg.allProd();
        cout << (res.l1 == 0 ? res.lc : 0) << "\n";
    };

    query();

    ll q;
    cin >> q;
    while (q--) {
        ll v;
        cin >> v;
        --v;
        auto [l, r] = hld.subtree(v);
        seg.apply(l, r, {1, 0});
        query();
    }
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    ll t;
    cin >> t;
    while (t--) testcase();
    return 0;
}