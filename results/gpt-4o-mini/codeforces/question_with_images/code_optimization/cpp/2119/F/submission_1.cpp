#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class Solution {
private:
    vector<vector<int>> adj;
    vector<int> weights;
    vector<int> reachableDepth;
    vector<int> lifeAtDepth;
    
public:
    void solve() {
        int T;
        cin >> T;
        
        while (T--) {
            int n, st;
            cin >> n >> st;

            weights.resize(n + 1);
            for (int i = 1; i <= n; i++) {
                cin >> weights[i];
            }

            adj.assign(n + 1, vector<int>());
            for (int i = 0; i < n - 1; i++) {
                int u, v;
                cin >> u >> v;
                adj[u].push_back(v);
                adj[v].push_back(u);
            }

            reachableDepth.assign(n + 1, 0);
            lifeAtDepth.assign(n + 1, 0);
            calculateDepth(st, 0, 0);

            int result = 0;
            int currentLife = 1 + weights[st];
            if (currentLife > 0) {
                result = simulateMovement(st, 0, currentLife, 1);
            }
            cout << result << "\n";
        }
    }

private:
    void calculateDepth(int node, int parent, int depth) {
        reachableDepth[node] = depth;
        for (int neighbor : adj[node]) {
            if (neighbor != parent) {
                calculateDepth(neighbor, node, depth + 1);
            }
        }
    }

    int simulateMovement(int node, int time, int life, int moves) {
        life += weights[node];
        if (life <= 0 || reachableDepth[node] <= time) {
            return moves - 1;
        }
        int maxMoves = moves;
        
        for (int neighbor : adj[node]) {
            if (reachableDepth[neighbor] > time) {
                maxMoves = max(maxMoves, simulateMovement(neighbor, time + 1, life, moves + 1));
            }
        }
        
        return maxMoves;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    Solution solution;
    solution.solve();

    return 0;
}