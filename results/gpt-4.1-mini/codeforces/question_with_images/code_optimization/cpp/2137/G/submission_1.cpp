#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t; cin >> t;
    while (t--) {
        int n, m, q; cin >> n >> m >> q;
        vector<vector<int>> adj(n + 1), revAdj(n + 1);
        vector<int> out_degree(n + 1, 0);

        for (int i = 0; i < m; i++) {
            int u, v; cin >> u >> v;
            adj[u].push_back(v);
            revAdj[v].push_back(u);
            out_degree[u]++;
        }

        // Colors: false = blue, true = red
        vector<bool> red(n + 1, false);

        // Topological sort
        vector<int> in_degree(n + 1, 0);
        for (int u = 1; u <= n; u++) {
            for (int v : adj[u]) in_degree[v]++;
        }
        queue<int> q_topo;
        for (int i = 1; i <= n; i++) {
            if (in_degree[i] == 0) q_topo.push(i);
        }
        vector<int> topo;
        topo.reserve(n);
        while (!q_topo.empty()) {
            int u = q_topo.front(); q_topo.pop();
            topo.push_back(u);
            for (int v : adj[u]) {
                if (--in_degree[v] == 0) q_topo.push(v);
            }
        }

        // cryWin0[u]: Cry to move, can Cry force a win from u?
        // cryWin1[u]: River to move, can Cry force a win from u?
        vector<bool> cryWin0(n + 1, false), cryWin1(n + 1, false);

        // Precompute cryWin arrays in reverse topo order
        for (int i = (int)topo.size() - 1; i >= 0; i--) {
            int u = topo[i];
            if (red[u]) {
                cryWin0[u] = false;
                cryWin1[u] = false;
            } else if (out_degree[u] == 0) {
                cryWin0[u] = true;
                cryWin1[u] = true;
            } else {
                bool canCryWin0 = false;
                bool canCryWin1 = true;
                for (int v : adj[u]) {
                    canCryWin0 |= cryWin1[v];
                    if (!cryWin0[v]) canCryWin1 = false;
                }
                cryWin0[u] = canCryWin0;
                cryWin1[u] = canCryWin1;
            }
        }

        // To efficiently update after coloring a node red:
        // We'll maintain counts of children that satisfy cryWin1 and cryWin0
        // to avoid recomputing from scratch each time.

        // For each node:
        // count_cryWin1_children[u] = number of children v with cryWin1[v] == true
        // count_cryWin0_children[u] = number of children v with cryWin0[v] == true
        vector<int> count_cryWin1_children(n + 1, 0);
        vector<int> count_cryWin0_children(n + 1, 0);

        for (int u = 1; u <= n; u++) {
            int c1 = 0, c0 = 0;
            for (int v : adj[u]) {
                if (cryWin1[v]) c1++;
                if (cryWin0[v]) c0++;
            }
            count_cryWin1_children[u] = c1;
            count_cryWin0_children[u] = c0;
        }

        while (q--) {
            int x, u; cin >> x >> u;
            if (x == 1) {
                // Update color to red if not already red
                if (red[u]) continue;
                red[u] = true;

                // Update cryWin0[u], cryWin1[u]
                bool oldWin0 = cryWin0[u];
                bool oldWin1 = cryWin1[u];
                cryWin0[u] = false;
                cryWin1[u] = false;

                if (oldWin0 == false && oldWin1 == false) continue;

                // BFS-like update on ancestors
                queue<int> updateQueue;
                for (int p : revAdj[u]) updateQueue.push(p);

                while (!updateQueue.empty()) {
                    int cur = updateQueue.front();
                    updateQueue.pop();

                    if (red[cur]) {
                        if (cryWin0[cur] || cryWin1[cur]) {
                            cryWin0[cur] = false;
                            cryWin1[cur] = false;
                            for (int p : revAdj[cur]) updateQueue.push(p);
                        }
                        continue;
                    }

                    // Update counts for cur based on changed child u
                    // We must recalc counts for cur because child's cryWin changed

                    // Instead of full recompute, we can update counts incrementally:
                    // But since multiple children can change, and we don't track which child changed,
                    // safer to recompute counts for cur.

                    int c1 = 0, c0 = 0;
                    for (int v : adj[cur]) {
                        if (cryWin1[v]) c1++;
                        if (cryWin0[v]) c0++;
                    }

                    bool newWin0 = (c1 > 0);
                    bool newWin1 = (c0 == (int)adj[cur].size());

                    if (newWin0 != cryWin0[cur] || newWin1 != cryWin1[cur]) {
                        cryWin0[cur] = newWin0;
                        cryWin1[cur] = newWin1;
                        for (int p : revAdj[cur]) updateQueue.push(p);
                    }
                }
            } else {
                cout << (cryWin0[u] ? "YES\n" : "NO\n");
            }
        }
    }

    return 0;
}