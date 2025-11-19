#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vll = vector<ll>;

void solve() {
    ll n;
    cin >> n;
    vll V(n);
    for (int i = 0; i < n; i++) cin >> V[i];

    vector<vll> adj(n);
    vll ans(n), rans(n);

    for (int i = 1; i < n; i++) {
        ll a, b;
        cin >> a >> b;
        a--, b--;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    stack<pair<ll, ll>> dfds;
    dfds.push({0, 0});

    while (!dfds.empty()) {
        auto [node, parent] = dfds.top();
        dfds.pop();

        if (ans[node] != 0) continue;

        if (node == 0) {
            ans[node] = V[node];
            rans[node] = 0;
        } else {
            ans[node] = V[node] - min(0LL, rans[parent]);
            rans[node] = V[node] - ans[parent];
        }

        for (ll neighbor : adj[node]) {
            dfds.push({neighbor, node});
        }
    }

    for (ll val : ans) cout << val << " ";
    cout << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}