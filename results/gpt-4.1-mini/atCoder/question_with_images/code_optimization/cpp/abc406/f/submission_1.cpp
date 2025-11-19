#include <bits/stdc++.h>
using namespace std;
#define int long long
const int N = 3e5 + 10;

int n, Q;
vector<int> adj[N];
int parent[N], depth[N];
int in[N], out[N], timer;
int weight[N];
int fenw[N];

// Fenwick tree (BIT) for point updates and prefix sums
void fenw_update(int i, int v) {
    while (i <= n) {
        fenw[i] += v;
        i += i & (-i);
    }
}

int fenw_sum(int i) {
    int s = 0;
    while (i > 0) {
        s += fenw[i];
        i -= i & (-i);
    }
    return s;
}

// DFS to assign parent, depth, and Euler tour indices
void dfs(int u, int p, int d) {
    parent[u] = p;
    depth[u] = d;
    in[u] = ++timer;
    for (auto &v : adj[u]) {
        if (v != p) {
            dfs(v, u, d + 1);
        }
    }
    out[u] = timer;
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    for (int i = 1; i < n; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // Initialize weights to 1
    for (int i = 1; i <= n; i++) weight[i] = 1;

    // Root the tree at 1
    timer = 0;
    dfs(1, 0, 0);

    // Initialize Fenwick tree with initial weights
    for (int i = 1; i <= n; i++) {
        fenw_update(in[i], weight[i]);
    }

    cin >> Q;
    vector<pair<int,int>> edges(n); // store edges for queries of type 2
    // We need to store edges in input order to answer queries
    // We'll read edges again to store them
    // But we already read edges, so let's store them during input
    // So we need to re-read edges or store them before dfs
    // Let's store edges before dfs

    // Since we need edges in order, let's store them before dfs
    // So we redo input reading with edges stored

    // To fix this, let's do the following:
    // We'll store edges in a vector before dfs, then do dfs

    // So let's restart main logic with edges stored first

    // Re-implement with edges stored first:

    // --- Restart code ---

    // We'll do this outside main for clarity

    return 0;
}

// Optimized code with edges stored before dfs:

#include <bits/stdc++.h>
using namespace std;
#define int long long
const int N = 3e5 + 10;

int n, Q;
vector<int> adj[N];
int parent[N], depth[N];
int in[N], out[N], timer;
int weight[N];
int fenw[N];

void fenw_update(int i, int v) {
    while (i <= n) {
        fenw[i] += v;
        i += i & (-i);
    }
}

int fenw_sum(int i) {
    int s = 0;
    while (i > 0) {
        s += fenw[i];
        i -= i & (-i);
    }
    return s;
}

void dfs(int u, int p, int d) {
    parent[u] = p;
    depth[u] = d;
    in[u] = ++timer;
    for (auto &v : adj[u]) {
        if (v != p) {
            dfs(v, u, d + 1);
        }
    }
    out[u] = timer;
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    vector<pair<int,int>> edges(n); // 1-based indexing for edges, edges[1..n-1]
    for (int i = 1; i < n; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        edges[i] = {u, v};
    }

    // Initialize weights to 1
    for (int i = 1; i <= n; i++) weight[i] = 1;

    timer = 0;
    dfs(1, 0, 0);

    for (int i = 1; i <= n; i++) {
        fenw_update(in[i], weight[i]);
    }

    cin >> Q;
    int total_weight = n; // sum of all weights initially

    for (int _ = 0; _ < Q; _++) {
        int op; cin >> op;
        if (op == 1) {
            int x, w; cin >> x >> w;
            weight[x] += w;
            fenw_update(in[x], w);
            total_weight += w;
        } else {
            int y; cin >> y;
            // edge y connects edges[y].first and edges[y].second
            int u = edges[y].first;
            int v = edges[y].second;

            // Determine which is parent and which is child
            // The one with greater depth is child
            int child = (depth[u] > depth[v]) ? u : v;

            // sum of subtree rooted at child
            int subtree_sum = fenw_sum(out[child]) - fenw_sum(in[child] - 1);
            int diff = abs(total_weight - 2 * subtree_sum);
            cout << diff << "\n";
        }
    }

    return 0;
}