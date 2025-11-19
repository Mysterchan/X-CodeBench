#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int MOD = 998244353;
const int maxsize = 3e5 + 10;

vector<int> tree[maxsize];
int cnt[maxsize], depth[maxsize];

void dfs_count(int node, int parent) {
    cnt[depth[node]]++;
    for (int child : tree[node]) {
        if (child != parent) {
            depth[child] = depth[node] + 1;
            dfs_count(child, node);
        }
    }
}

ll calculate_sequences(int node, int parent) {
    ll ans = 1; // Count the sequence that includes just the current node
    for (int child : tree[node]) {
        if (child != parent) {
            ans = (ans * (cnt[depth[child] + 1])) % MOD; // Multiply by the number of valid sequences from depth of child
            ans--; // Subtract the case where we only count the child (invalid move)
        }
    }
    return ans; // Return valid sequences including this node
}

void solve() {
    int n;
    cin >> n;
    
    // Clear previous test case data
    for (int i = 1; i <= n; ++i) {
        tree[i].clear();
        cnt[i] = 0;
        depth[i] = 0;
    }

    for (int i = 2; i <= n; ++i) {
        int parent;
        cin >> parent;
        tree[parent].push_back(i);
        tree[i].push_back(parent);
    }

    depth[1] = 0; // Starting from root
    dfs_count(1, -1);
    
    ll ans = calculate_sequences(1, -1);
    
    cout << ans << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) solve();
}