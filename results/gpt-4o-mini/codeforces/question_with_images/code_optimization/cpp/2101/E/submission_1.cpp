#include <bits/stdc++.h>
using namespace std;

const int MX = 70005;
char s[MX];
vector<int> g[MX];
int depth[MX], vis[MX], res[MX];

void dfs(int node, int d) {
    depth[node] = d;
    vis[node] = 1;
    for (int neighbor : g[node]) {
        if (!vis[neighbor])
            dfs(neighbor, d + 1);
    }
}

// Main function to calculate the nice paths
void calculateNicePaths(int n) {
    for (int i = 1; i <= n; i++) {
        if (s[i] == '1') {
            vector<int> weights;
            for (int neighbor : g[i]) {
                if (s[neighbor] == '1') {
                    weights.push_back(depth[neighbor] - depth[i]);
                }
            }
            sort(weights.begin(), weights.end());
            int count = 0, last = 0; 
            for (int weight : weights) {
                if (count == 0 || weight >= 2 * last) {
                    count++;
                    last = weight;
                }
            }
            res[i] = count + 1; // +1 for the starting node
        } else {
            res[i] = -1;
        }
    }
}

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n;
        scanf("%d", &n);
        scanf("%s", s + 1);
        
        for (int i = 1; i <= n; i++)
            g[i].clear();

        for (int i = 1; i < n; i++) {
            int u, v;
            scanf("%d%d", &u, &v);
            g[u].emplace_back(v);
            g[v].emplace_back(u);
        }

        memset(vis, 0, sizeof(vis));
        memset(depth, 0, sizeof(depth));
        dfs(1, 0); // Start DFS from node 1
        calculateNicePaths(n);

        for (int i = 1; i <= n; i++) {
            printf("%d ", res[i]);
        }
        printf("\n");
    }
    return 0;
}