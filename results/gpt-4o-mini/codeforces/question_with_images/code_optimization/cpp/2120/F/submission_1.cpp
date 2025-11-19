#include <bits/stdc++.h>
using namespace std;

#define MAX_N 301

bool is_clique(const vector<vector<bool>>& graph, const vector<int>& vertices) {
    for (size_t i = 0; i < vertices.size(); ++i) {
        for (size_t j = i + 1; j < vertices.size(); ++j) {
            if (!graph[vertices[i]][vertices[j]]) {
                return false; // Not a clique
            }
        }
    }
    return true; // All pairs are connected
}

bool is_independent(const vector<vector<bool>>& graph, const vector<int>& vertices) {
    for (size_t i = 0; i < vertices.size(); ++i) {
        for (size_t j = i + 1; j < vertices.size(); ++j) {
            if (graph[vertices[i]][vertices[j]]) {
                return false; // Not independent
            }
        }
    }
    return true; // All pairs are disconnected
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;

        vector<vector<bool>> graph(n + 1, vector<bool>(n + 1, false));
        vector<int> component_size(k, 0);

        for (int i = 0; i < k; ++i) {
            int m;
            cin >> m;
            vector<int> vertices;

            for (int j = 0; j < m; ++j) {
                int u, v;
                cin >> u >> v;
                graph[u][v] = graph[v][u] = true;
                
                // Track vertices for independent set or clique checks
                vertices.push_back(u);
                vertices.push_back(v);
            }
            
            set<int> vertex_set(vertices.begin(), vertices.end());
            component_size[i] = vertex_set.size();

            if (m == 0) continue;

            // Check for cliques or independent sets
            bool valid = true;
            for (int u : vertex_set) {
                vector<int> neighbor;
                for (int v : vertex_set) {
                    if (u != v && graph[u][v]) {
                        neighbor.push_back(v);
                    }
                }

                if (neighbor.size() > 1 && is_clique(graph, neighbor)) {
                    valid = false; // Found a clique of size >1
                    break;
                }

                if (neighbor.size() == 1 && is_independent(graph, {u})) {
                    valid = false; // Found an independent set of size == 1
                    break;
                }
            }

            if (!valid) {
                cout << "No\n";
                goto end_of_case;
            }
        }
        
        cout << "Yes\n";
        end_of_case: ;
    }
    return 0;
}