#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
private:
    vector<vector<int>> adj;
    vector<int> weights;
    vector<int> distFromRoot;
    int n, st;
    unordered_map<string, int> memo;
    
public:
    void solve() {
        int T;
        cin >> T;
        
        while (T--) {
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
            
            distFromRoot.assign(n + 1, -1);
            bfsDistance();
            
            memo.clear();
            int result = dfs(st, 0, 1);
            cout << result << "\n";
        }
    }
    
private:
    void bfsDistance() {
        queue<int> q;
        q.push(1);
        distFromRoot[1] = 0;
        
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            
            for (int next : adj[curr]) {
                if (distFromRoot[next] == -1) {
                    distFromRoot[next] = distFromRoot[curr] + 1;
                    q.push(next);
                }
            }
        }
    }
    
    int dfs(int vertex, int time, int life) {
        life += weights[vertex];
        
        if (life == 0 || distFromRoot[vertex] <= time) {
            return 0;
        }
        
        string key = to_string(vertex) + "," + to_string(time) + "," + to_string(life);
        if (memo.find(key) != memo.end()) {
            return memo[key];
        }
        
        int maxMoves = 0;
        
        for (int nextVertex : adj[vertex]) {
            int moves = 1 + dfs(nextVertex, time + 1, life);
            maxMoves = max(maxMoves, moves);
        }
        
        memo[key] = maxMoves;
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