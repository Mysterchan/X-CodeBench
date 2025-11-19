#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int n, k; cin >> n >> k;
        vector<vector<bool>> graphs(k, vector<bool>(n * n, false));

        for (int i = 0; i < k; i++) {
            int m; cin >> m;
            for (int j = 0; j < m; j++) {
                int u, v; cin >> u >> v; u--; v--;
                graphs[i][u * n + v] = true;
                graphs[i][v * n + u] = true;
            }
        }

        // For each vertex, track if it is in a non-singleton independent set or clique in any graph
        // We only need to know if vertex v is in a clique or independent set of size > 1 in any graph
        // The condition is: if vertex v is in a large independent set in some graph Gi,
        // then it cannot be in a large clique in any other graph Gj (j != i).

        // To check this, we need to find the partition of vertices in each graph into the minimal number of
        // cliques or independent sets that form the superb graph.

        // The problem reduces to checking if there exists a labeling of each vertex v with a type:
        // 0 = singleton (both clique and independent set)
        // 1 = in a large independent set in some graph Gi
        // 2 = in a large clique in some graph Gi
        // such that no vertex is assigned 1 in one graph and 2 in another.

        // We can find the minimal partition of vertices into cliques or independent sets by checking
        // connected components in the complement or original graph.

        // For each graph Gi:
        // - The superb graph corresponds to the partition of vertices into maximal cliques or independent sets.
        // - Since the problem states that vertices of Gi correspond to either independent sets or cliques in Hi,
        //   and the superb graph has minimum vertices, the partition is unique and corresponds to connected components
        //   in Gi or its complement.

        // So for each graph Gi:
        // - If Gi is a perfect graph (which is guaranteed by the problem context),
        //   the minimal partition into cliques or independent sets corresponds to connected components in Gi or complement.

        // We try both partitions:
        // - Partition by connected components in Gi (cliques)
        // - Partition by connected components in complement of Gi (independent sets)
        // and pick the one with minimal number of parts.

        // For each vertex, record if it belongs to a clique of size > 1 or independent set of size > 1 in Gi.

        // Finally, check the condition:
        // For each vertex v, if it is in a large independent set in some Gi,
        // then it must not be in a large clique in any other Gj (j != i).

        // Implementation:

        vector<int> type(n, 0); // 0 = unknown, 1 = indep set >1, 2 = clique >1

        for (int i = 0; i < k; i++) {
            // Build adjacency for Gi
            vector<vector<int>> adj(n);
            for (int u = 0; u < n; u++) {
                for (int v = u + 1; v < n; v++) {
                    if (graphs[i][u * n + v]) {
                        adj[u].push_back(v);
                        adj[v].push_back(u);
                    }
                }
            }

            // Build complement adjacency
            vector<vector<int>> comp_adj(n);
            for (int u = 0; u < n; u++) {
                vector<bool> connected(n, false);
                for (int w : adj[u]) connected[w] = true;
                connected[u] = true;
                for (int v = 0; v < n; v++) {
                    if (!connected[v]) {
                        comp_adj[u].push_back(v);
                    }
                }
            }

            // Find connected components in adj (cliques)
            vector<int> comp_clique(n, -1);
            int ccount_clique = 0;
            {
                vector<bool> vis(n, false);
                for (int v = 0; v < n; v++) {
                    if (!vis[v]) {
                        ccount_clique++;
                        queue<int> q; q.push(v); vis[v] = true; comp_clique[v] = ccount_clique;
                        while (!q.empty()) {
                            int cur = q.front(); q.pop();
                            for (int nxt : adj[cur]) {
                                if (!vis[nxt]) {
                                    vis[nxt] = true;
                                    comp_clique[nxt] = ccount_clique;
                                    q.push(nxt);
                                }
                            }
                        }
                    }
                }
            }

            // Find connected components in comp_adj (independent sets)
            vector<int> comp_indep(n, -1);
            int ccount_indep = 0;
            {
                vector<bool> vis(n, false);
                for (int v = 0; v < n; v++) {
                    if (!vis[v]) {
                        ccount_indep++;
                        queue<int> q; q.push(v); vis[v] = true; comp_indep[v] = ccount_indep;
                        while (!q.empty()) {
                            int cur = q.front(); q.pop();
                            for (int nxt : comp_adj[cur]) {
                                if (!vis[nxt]) {
                                    vis[nxt] = true;
                                    comp_indep[nxt] = ccount_indep;
                                    q.push(nxt);
                                }
                            }
                        }
                    }
                }
            }

            // Choose partition with minimal parts
            // If tie, choose independent set partition (arbitrary)
            bool use_indep = (ccount_indep <= ccount_clique);

            if (use_indep) {
                // Mark vertices in independent sets of size > 1
                vector<int> size_indep(ccount_indep + 1, 0);
                for (int v = 0; v < n; v++) size_indep[comp_indep[v]]++;
                for (int v = 0; v < n; v++) {
                    if (size_indep[comp_indep[v]] > 1) {
                        // vertex v is in a large independent set in graph i
                        if (type[v] == 2) {
                            // conflict: previously assigned clique >1 in another graph
                            cout << "No\n";
                            goto next_testcase;
                        }
                        type[v] = 1;
                    }
                }
            } else {
                // Mark vertices in cliques of size > 1
                vector<int> size_clique(ccount_clique + 1, 0);
                for (int v = 0; v < n; v++) size_clique[comp_clique[v]]++;
                for (int v = 0; v < n; v++) {
                    if (size_clique[comp_clique[v]] > 1) {
                        // vertex v is in a large clique in graph i
                        if (type[v] == 1) {
                            // conflict: previously assigned independent set >1 in another graph
                            cout << "No\n";
                            goto next_testcase;
                        }
                        type[v] = 2;
                    }
                }
            }
        }

        cout << "Yes\n";
    next_testcase:;
    }

    return 0;
}