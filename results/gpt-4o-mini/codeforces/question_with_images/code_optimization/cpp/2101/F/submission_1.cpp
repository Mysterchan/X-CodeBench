#include <bits/stdc++.h>
using namespace std;
const int N = 3005;
const int MOD = 998244353;

int n, ec;
vector<int> tree[N];
long long power2[N], power3[N];

void dfs(int u, int parent, vector<int>& depth, int d) {
    depth[u] = d;
    for (int v : tree[u]) {
        if (v != parent) {
            dfs(v, u, depth, d + 1);
        }
    }
}

long long computeCoolness(int k, vector<int>& depth) {
    long long coolness = 0;
    for (int u = 1; u <= n; u++) {
        for (int v = 1; v <= n; v++) {
            if (depth[u] >= k && depth[v] >= k) {
                coolness += (depth[u] + depth[v] - 2 * k);
                coolness %= MOD;
            }
        }
    }
    return coolness;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    power2[0] = power3[0] = 1;
    for (int i = 1; i < N; i++) {
        power2[i] = power2[i - 1] * 2 % MOD;
        power3[i] = power3[i - 1] * 3 % MOD;
    }

    int T; 
    cin >> T;
    while (T--) {
        cin >> n;
        ec = 0;
        for (int i = 1; i <= n; i++) {
            tree[i].clear();
        }
        for (int i = 1; i < n; i++) {
            int u, v;
            cin >> u >> v;
            tree[u].push_back(v);
            tree[v].push_back(u);
        }

        long long totalCoolness = 0;
        for (int k = 1; k < n; k++) {
            vector<int> depth(n + 1, 0);
            dfs(1, -1, depth, 0);
            totalCoolness = (totalCoolness + computeCoolness(k, depth)) % MOD;
        }

        long long totalColorings = (1LL * (n - 1) * power3[n]) % MOD;
        long long answer = (totalColorings - totalCoolness + MOD) % MOD;

        cout << answer << "\n";
    }
    return 0;
}