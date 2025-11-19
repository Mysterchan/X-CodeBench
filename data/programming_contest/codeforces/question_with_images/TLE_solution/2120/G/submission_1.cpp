#include <bits/stdc++.h>
using namespace std;

struct Graph {
    int n;
    vector<vector<int>> adj;
    
    Graph(int vertices) : n(vertices), adj(vertices) {}
    
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    
    bool isConnected() {
        if (n == 0) return true;
        
        vector<bool> visited(n, false);
        queue<int> q;
        int start = -1;
        for (int i = 0; i < n; i++) {
            if (!adj[i].empty()) {
                start = i;
                break;
            }
        }
        
        if (start == -1) return n <= 1; 
        
        q.push(start);
        visited[start] = true;
        int visitedCount = 1;
        
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            
            for (int neighbor : adj[curr]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                    visitedCount++;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            if (!adj[i].empty() && !visited[i]) {
                return false;
            }
        }
        
        return true;
    }
    
    bool hasEulerTrail() {
        if (!isConnected()) return false;
        
        int oddDegreeCount = 0;
        for (int i = 0; i < n; i++) {
            if (adj[i].size() % 2 == 1) {
                oddDegreeCount++;
            }
        }
        
        return oddDegreeCount <= 2;
    }
};

Graph computeLineGraph(const Graph& g) {
    vector<pair<int, int>> edges;
    map<pair<int, int>, int> edgeToVertex;
    
    for (int u = 0; u < g.n; u++) {
        for (int v : g.adj[u]) {
            if (u < v) { 
                edges.push_back({u, v});
                edgeToVertex[{u, v}] = edges.size() - 1;
            }
        }
    }
    
    Graph lineGraph(edges.size());
    for (int i = 0; i < edges.size(); i++) {
        for (int j = i + 1; j < edges.size(); j++) {
            pair<int, int> edge1 = edges[i];
            pair<int, int> edge2 = edges[j];
            if (edge1.first == edge2.first || edge1.first == edge2.second ||
                edge1.second == edge2.first || edge1.second == edge2.second) {
                lineGraph.addEdge(i, j);
            }
        }
    }
    
    return lineGraph;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    
    while (t--) {
        int n, m, k;
        cin >> n >> m >> k;
        
        Graph g(n);
        
        for (int i = 0; i < m; i++) {
            int u, v;
            cin >> u >> v;
            u--; v--; 
            g.addEdge(u, v);
        }
        
        Graph current = g;
        for (int i = 0; i < k; i++) {
            current = computeLineGraph(current);
            if (current.n == 0) break; 
        }
        
        if (current.hasEulerTrail()) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
    
    return 0;
} 