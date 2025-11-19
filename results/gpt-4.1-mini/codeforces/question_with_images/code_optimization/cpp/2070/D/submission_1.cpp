#include <bits/stdc++.h>
using namespace std;

const int mod = 998244353;
const int maxn = 3e5 + 10;

int t, n;
int p[maxn];
int depth[maxn];
int cnt[maxn];
int childrenCount[maxn];
vector<int> adj[maxn];

void solve() {
    cin >> n;
    for (int i = 1; i <= n; i++) {
        adj[i].clear();
        cnt[i] = 0;
        childrenCount[i] = 0;
        depth[i] = 0;
    }

    for (int i = 2; i <= n; i++) {
        cin >> p[i];
        adj[p[i]].push_back(i);
    }

    // BFS to compute depths and count nodes per depth
    queue<int> q;
    q.push(1);
    depth[1] = 1;
    cnt[1] = 1;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adj[u]) {
            depth[v] = depth[u] + 1;
            cnt[depth[v]]++;
            q.push(v);
        }
    }

    // Count children for each node
    for (int i = 1; i <= n; i++) {
        childrenCount[i] = (int)adj[i].size();
    }

    // Calculate answer
    // ans = n + sum over all nodes x of cnt[depth[x]+1] - sum over all nodes x of childrenCount[x]
    // Because sum of childrenCount = n-1, so:
    // ans = n + sum cnt[depth[x]+1] - (n-1) = 1 + sum cnt[depth[x]+1]
    // We'll compute sum cnt[depth[x]+1] efficiently.

    long long ans = n; // initial sequences: single nodes (each node alone)
    for (int i = 1; i <= n; i++) {
        int d = depth[i] + 1;
        if (d <= n) {
            ans += cnt[d];
        }
    }
    ans -= (n - 1);
    ans %= mod;
    if (ans < 0) ans += mod;

    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> t;
    while (t--) solve();

    return 0;
}