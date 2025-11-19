#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200005;

vector<int> tree[MAXN];
long long a[MAXN];
long long threat[MAXN];

// We will do a DFS from the root to compute threat values.
// Define dp arrays:
// dp_even[v] = max alternating sum starting at v with sign +1 at v (even length path from v)
// dp_odd[v] = max alternating sum starting at v with sign -1 at v (odd length path from v)
// The threat[v] = max(dp_even[v], dp_odd[v]) but since path starts at v with + sign, threat[v] = dp_even[v].

// Recurrence:
// dp_even[v] = a[v] + max(0, max over children c of dp_odd[c])
// dp_odd[v] = -a[v] + max(0, max over children c of dp_even[c])

// This works because the path is vertical (up to root), but we can think of the tree rooted at 1,
// and the path from v to root is unique. We can process from root down and use dp to get the answer efficiently.

void dfs(int v, int p) {
    long long max_odd_child = 0;
    long long max_even_child = 0;
    for (int c : tree[v]) {
        if (c == p) continue;
        dfs(c, v);
        if (threat[c + MAXN] < 0) continue; // not needed, just safe
        // We'll store dp_even and dp_odd in arrays indexed by v
        // We'll store dp_even[v] and dp_odd[v] in threat[v] and threat[v + MAXN] respectively
        // But better to use separate arrays for clarity
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    // We'll store dp_even and dp_odd separately
    static long long dp_even[MAXN], dp_odd[MAXN];

    while (t--) {
        int n;
        cin >> n;

        for (int i = 1; i <= n; ++i) {
            cin >> a[i];
            tree[i].clear();
        }

        for (int i = 1; i < n; ++i) {
            int u, v;
            cin >> u >> v;
            tree[u].push_back(v);
            tree[v].push_back(u);
        }

        // DFS from root 1
        function<void(int,int)> dfs = [&](int v, int p) {
            long long max_odd_child = 0;
            long long max_even_child = 0;
            for (int c : tree[v]) {
                if (c == p) continue;
                dfs(c, v);
                if (dp_odd[c] > max_odd_child) max_odd_child = dp_odd[c];
                if (dp_even[c] > max_even_child) max_even_child = dp_even[c];
            }
            dp_even[v] = a[v] + max(0LL, max_odd_child);
            dp_odd[v] = -a[v] + max(0LL, max_even_child);
        };

        dfs(1, 0);

        for (int i = 1; i <= n; ++i) {
            cout << dp_even[i] << " ";
        }
        cout << "\n";
    }

    return 0;
}