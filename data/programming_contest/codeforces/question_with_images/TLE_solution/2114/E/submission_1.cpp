#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200005;

vector<int> tree[MAXN];
int parent[MAXN];
long long a[MAXN];
long long threat[MAXN];

void build_parent(int node, int par) {
    parent[node] = par;
    for (int child : tree[node]) {
        if (child != par) {
            build_parent(child, node);
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
        }

        for (int i = 1; i < n; ++i) {
            int u, v;
            cin >> u >> v;
            tree[u].push_back(v);
            tree[v].push_back(u);
        }

        build_parent(1, 0); // root is 1

        for (int v = 1; v <= n; ++v) {
            long long sum = 0;
            long long max_sum = LLONG_MIN;
            int curr = v;
            int sign = 1;
            while (curr != 0) {
                sum += sign * a[curr];
                max_sum = max(max_sum, sum);
                sign *= -1;
                curr = parent[curr];
            }
            threat[v] = max_sum;
        }

        for (int i = 1; i <= n; ++i) {
            cout << threat[i] << " ";
        }
        cout << '\n';
    }

    return 0;
}
