#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

vector<int> adj[200005];
long long dp[200005];
long long ans = -1;


void dfs1(int u, int p) {

    vector<long long> child_dps;
    for (int v : adj[u]) {
        if (v == p) continue;
        dfs1(v, u);
        child_dps.push_back(dp[v]);
    }
    sort(child_dps.rbegin(), child_dps.rend());

    dp[u] = 1;
    if (child_dps.size() >= 3) {
        dp[u] += child_dps[0] + child_dps[1] + child_dps[2];
    }
}


void dfs2(int u, int p, long long up_val) {

    vector<long long> all_branches;
    if (p != 0) {
        all_branches.push_back(up_val);
    }
    for (int v : adj[u]) {
        if (v == p) continue;
        all_branches.push_back(dp[v]);
    }
    sort(all_branches.rbegin(), all_branches.rend());

    if (all_branches.size() >= 4) {
        long long current_size = 1;
        for (int i = 0; i < 4; ++i) {
            current_size += all_branches[i];
        }
        ans = max(ans, current_size);
    }

    for (int v : adj[u]) {
        if (v == p) continue;

        vector<long long> available_for_up;
        if (p != 0) {
            available_for_up.push_back(up_val);
        }
        for (int ov : adj[u]) {
            if (ov == p || ov == v) continue;
            available_for_up.push_back(dp[ov]);
        }
        sort(available_for_up.rbegin(), available_for_up.rend());

        long long new_up_val = 1;
        if (available_for_up.size() >= 3) {
            new_up_val += available_for_up[0] + available_for_up[1] + available_for_up[2];
        }
        
        dfs2(v, u, new_up_val);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs1(1, 0);

    dfs2(1, 0, 1); 

    cout << ans << endl;

    return 0;
}