#include <bits/stdc++.h>
using namespace std;

const int MX = 200000;

int n, m;
vector<int> G[MX + 1];
int dist0[MX + 1], distn[MX + 1];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    for (int i = 1; i <= n; i++) G[i].clear();
    for (int i = 0; i < m; i++) {
        int u,v; cin >> u >> v;
        G[u].push_back(v);
        G[v].push_back(u);
    }

    // BFS from n to get distn[]
    {
        fill(distn + 1, distn + n + 1, -1);
        queue<int> q;
        distn[n] = 0;
        q.push(n);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int w : G[u]) {
                if (distn[w] == -1) {
                    distn[w] = distn[u] + 1;
                    q.push(w);
                }
            }
        }
    }

    // BFS from 1 to get dist0[]
    {
        fill(dist0 + 1, dist0 + n + 1, -1);
        queue<int> q;
        dist0[1] = 0;
        q.push(1);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int w : G[u]) {
                if (dist0[w] == -1) {
                    dist0[w] = dist0[u] + 1;
                    q.push(w);
                }
            }
        }
    }

    if (dist0[n] == -1) {
        cout << -1 << "\n";
        return 0;
    }

    int shortest = dist0[n];

    // Count number of shortest paths edges from each node
    // For each node u, count how many neighbors v satisfy dist0[v] == dist0[u] + 1 and distn[v] == distn[u] - 1
    // These edges are on shortest paths from 1 to n
    vector<int> sp_count(n+1,0);
    for (int u = 1; u <= n; u++) {
        for (int v : G[u]) {
            if (dist0[v] == dist0[u] + 1 && distn[v] == distn[u] - 1) {
                sp_count[u]++;
            }
        }
    }

    // The police wants to block an edge on the supporters' shortest path to maximize supporters' travel length.
    // The supporters know police will block optimally and will try to minimize travel length.
    // The police can block exactly one edge not currently being traversed.
    // The supporters can reroute after the block.

    // The key insight:
    // The supporters will try to avoid edges that are unique on shortest paths.
    // The police will try to block an edge that is unique on shortest paths (i.e., sp_count[u] == 1),
    // so that supporters must detour.

    // Find the minimal length after police blocks optimally:
    // For each node u on shortest path (dist0[u] + distn[u] == shortest),
    // if sp_count[u] == 1, then blocking that unique edge forces supporters to detour.
    // The detour cost is at least shortest + 2 (go back and around).

    // If no such unique edge exists, supporters can always avoid the block and keep shortest path length.

    // So answer is:
    // -1 if no path exists (already checked)
    // shortest + 2 if there exists a node u on shortest path with sp_count[u] == 1
    // else shortest

    bool unique_edge_exists = false;
    for (int u = 1; u <= n; u++) {
        if (dist0[u] == -1 || distn[u] == -1) continue;
        if (dist0[u] + distn[u] == shortest && sp_count[u] == 1) {
            unique_edge_exists = true;
            break;
        }
    }

    if (unique_edge_exists) cout << shortest + 2 << "\n";
    else cout << shortest << "\n";

    return 0;
}