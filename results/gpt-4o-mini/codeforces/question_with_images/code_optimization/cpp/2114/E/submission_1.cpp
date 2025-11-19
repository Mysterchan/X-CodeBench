#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200005;

vector<int> tree[MAXN];
long long a[MAXN];
long long threat[MAXN];

void dfs(int node, int par, long long current_sum, int sign) {
    current_sum += sign * a[node];
    threat[node] = max(threat[node], current_sum);
    
    for (int child : tree[node]) {
        if (child != par) {
            dfs(child, node, current_sum, -sign);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        for (int i = 1; i <= n; ++i) {
            cin >> a[i];
            tree[i].clear();
            threat[i] = LLONG_MIN; // Initialize threat to minimum
        }

        for (int i = 1; i < n; ++i) {
            int u, v;
            cin >> u >> v;
            tree[u].push_back(v);
            tree[v].push_back(u);
        }

        // Start DFS from the root (node 1)
        dfs(1, -1, 0, 1);

        for (int i = 1; i <= n; ++i) {
            cout << threat[i] << " ";
        }
        cout << '\n';
    }

    return 0;
}