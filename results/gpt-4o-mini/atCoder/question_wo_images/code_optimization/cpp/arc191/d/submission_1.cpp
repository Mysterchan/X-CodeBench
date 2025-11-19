#include <bits/stdc++.h>
using namespace std;

static const int INF = 1e9;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N, M, S, T;
    cin >> N >> M >> S >> T;

    vector<vector<int>> graph(N + 1);
    for(int i = 0; i < M; i++){
        int u, v; 
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    // BFS to calculate distances from S and T
    auto bfs = [&](int start) {
        vector<int> distance(N + 1, INF);
        queue<int> q;
        distance[start] = 0;
        q.push(start);

        while (!q.empty()) {
            int node = q.front(); 
            q.pop();
            for (int neighbor : graph[node]) {
                if (distance[neighbor] == INF) {
                    distance[neighbor] = distance[node] + 1;
                    q.push(neighbor);
                }
            }
        }
        return distance;
    };

    vector<int> dS = bfs(S);
    vector<int> dT = bfs(T);
    
    if (dS[T] == INF) {
        cout << -1 << '\n';
        return 0;
    }

    int totalMoves = 2 * dS[T]; 
    int minOperations = INF;

    // Iterate through all nodes to check reachability while avoiding overlap
    for (int i = 1; i <= N; ++i) {
        if (i != S && i != T) {
            int movesFromA = dS[i] + 1 + dT[i]; // Move A to i and then B to T
            int movesFromB = dT[i] + 1 + dS[i]; // Move B to i and then A to S
            minOperations = min(minOperations, min(movesFromA, movesFromB));
        }
    }

    cout << (minOperations == INF ? -1 : totalMoves + minOperations) << '\n';
    
    return 0;
}
