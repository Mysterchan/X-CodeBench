#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        
        vector<int> a(n + 1);
        for (int i = 1; i <= n; i++) cin >> a[i];
        
        vector<vector<int>> g(n + 1);
        for (int i = 0; i < n - 1; i++) {
            int u, v; cin >> u >> v;
            g[u].push_back(v);
            g[v].push_back(u);
        }

        vector<int> tin(n + 1), tout(n + 1), subtree_size(n + 1);
        vector<int> stack;
        stack.reserve(n);
        stack.push_back(1);
        
        vector<int> parent(n + 1);
        vector<bool> visited(n + 1, false);
        int timer = 0;

        while (!stack.empty()) {
            int u = stack.back();
            stack.pop_back();
            if (visited[u]) continue;

            visited[u] = true; 
            timer++;
            tin[u] = timer; 

            for (int v : g[u]) {
                if (!visited[v]) {
                    parent[v] = u;
                    stack.push_back(v);
                }
            }
            tout[u] = timer; 
        }

        set<int> monsters;
        for (int i = 1; i <= n; i++) {
            if (a[i] == 1) monsters.insert(tin[i]);
        }
        
        auto add_monster = [&](int idx) {
            monsters.insert(idx);
        };

        auto remove_monster = [&](int idx) {
            monsters.erase(idx);
        };

        auto count_paths = [&]() {
            int count = 0;
            for (int m : monsters) {
                if (monsters.upper_bound(m) == monsters.end() || tout[parent[m]] < m) {
                    count++;
                }
            }
            return count;
        };

        cout << count_paths() << '\n';

        int q;
        cin >> q;
        while (q--) {
            int v;
            cin >> v;
            int start = tin[v], end = tout[v];
            for (int i = start; i <= end; i++) { // Invert all monsters in the subtree
                if (monsters.find(i) != monsters.end()) {
                    remove_monster(i);
                } else {
                    add_monster(i);
                }
            }
            cout << count_paths() << '\n';
        }
    }
    return 0;
}