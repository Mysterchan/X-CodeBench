#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long

bool twoSAT(vector<vector<int>> &adj, vector<vector<int>> &adj_rev, vector<bool> &assignment) {
    int n = adj.size();
    vector<int> order;
    vector<bool> used(n, false);

    function<void(int)> dfs1 = [&](int v) {
        used[v] = true;

        for(auto u : adj[v]) 
            if(!used[u])
                dfs1(u);

        order.push_back(v);
    };

    vector<int> comp(n, -1);

    function<void(int, int)> dfs2 = [&](int v, int color) {
        comp[v] = color;

        for(auto u : adj_rev[v]) 
            if(comp[u] == -1)
                dfs2(u, color);
    };

    for(int i = 0; i < n; ++i) 
        if(!used[i])
            dfs1(i);

    used.assign(n, false);

    for(int i = 0, j = 0; i < n; ++i) {
        int v = order[n - i - 1];
        if(comp[v] == -1)
            dfs2(v, j++);
    }

    assignment.assign(n / 2, false);
    for(int i = 0; i < n; i += 2) {
        if(comp[i] == comp[i + 1]) 
            return false; 
        assignment[i / 2] = comp[i] > comp[i + 1];
    }
    return true;
}

void solve() {
    int n, k; cin >> n >> k;

    vector<vector<int>> adj(2*n), adj_rev(2*n);

    auto add_or = [&](int a, bool nega, int b, bool negb) {
        a = (2*a) + nega;
        b = (2*b) + negb;
        adj[a^1].push_back(b);
        adj[b^1].push_back(a);
        adj_rev[b].push_back(a^1);
        adj_rev[a].push_back(b^1);
    };

    function<void(int, vector<vector<int>>&)> process = [&n, &add_or](int m, vector<vector<int>> &adj) {
        map<vector<int>, vector<int>> mp;

        for(int i = 0; i < n; ++i) {
            auto temp = adj[i];
            temp.push_back(i);
            sort(temp.begin(), temp.end());

            mp[temp].push_back(i);
        }

        for(auto [x, y] : mp) {
            for(int i = 0; i < y.size(); ++i) {
                for(int j = i + 1; j < y.size(); ++j) {
                    add_or(y[i], 1, y[j], 1);
                }
            }
        }

        mp.clear();

        for(int i = 0; i < n; ++i) {
            sort(adj[i].begin(), adj[i].end());
            mp[adj[i]].push_back(i);
        }

        for(auto [x, y] : mp) {
            for(int i = 0; i < y.size(); ++i) {
                for(int j = i + 1; j < y.size(); ++j) {
                    add_or(y[i], 0, y[j], 0);
                }
            }
        }
    };

    for(int i = 0; i < k; ++i) {
        int m; cin >> m;
        vector<vector<int>> adj(n);

        for(int j = 0; j < m; ++j) {
            int x, y; cin >> x >> y;
            x--; y--;
            adj[x].push_back(y);
            adj[y].push_back(x);
        }

        process(m, adj);
    }

    vector<bool> assignment(n, false);
    cout << ((twoSAT(adj, adj_rev, assignment)) ? "Yes" : "No");
}

int32_t main() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int _TC = 0; cin >> _TC;
    for(int _ct = 1; _ct <= _TC; ++_ct) {
        solve(); cout << endl;
    }
}