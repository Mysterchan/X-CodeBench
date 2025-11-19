#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int MOD = 998244353;
const int N = 5000;
int fac[N + 1], inv[N + 1];

int mul(int a, int b) {
    return 1LL * a * b % MOD;
}

int power(int a, int b) {
    int res = 1;
    while (b) {
        if (b & 1) {
            res = mul(res, a);
        }
        a = mul(a, a);
        b >>= 1;
    }
    return res;
}

int C(int n, int m) {
    if (n < m || m < 0) return 0;
    return mul(fac[n], mul(inv[m], inv[n - m]));
}

void preprocess(int max_n) {
    fac[0] = inv[0] = 1;
    for (int i = 1; i <= max_n; i++) {
        fac[i] = mul(fac[i - 1], i);
    }
    inv[max_n] = power(fac[max_n], MOD - 2);
    for (int i = max_n - 1; i > 0; i--) {
        inv[i] = mul(inv[i + 1], i + 1);
    }
}

struct TreeNode {
    int size = 0;
    int count[2] = {0, 0}; // Counts for colors
    vector<int> chips; // Chips colors for this node
    vector<int> children;
};

TreeNode nodes[N + 1];

void DFS(int u) {
    for (int v : nodes[u].children) {
        DFS(v);
        nodes[u].size += nodes[v].size;
        nodes[u].count[0] += nodes[v].count[0];
        nodes[u].count[1] += nodes[v].count[1];
        nodes[u].chips.insert(nodes[u].chips.end(), nodes[v].chips.begin(), nodes[v].chips.end());
    }
    nodes[u].size += nodes[u].chips.size();
}

int calculateAnswer(int m) {
    int result = 0;
    for (int i = 0; i <= m; i++) {
        result = (result + C(m, i)) % MOD;
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    preprocess(N);
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        for (int i = 0; i <= n; i++) {
            nodes[i].size = 0;
            nodes[i].count[0] = 0;
            nodes[i].count[1] = 0;
            nodes[i].chips.clear();
            nodes[i].children.clear();
        }

        vector<int> parent(n + 1), color(m + 1), limit(m + 1);
        for (int i = 1; i <= n; i++) {
            cin >> parent[i];
            nodes[parent[i]].children.push_back(i);
        }
        for (int i = 1; i <= m; i++) {
            cin >> color[i];
        }
        for (int i = 1; i <= m; i++) {
            cin >> limit[i];
            nodes[limit[i]].chips.push_back(color[i]);
            nodes[limit[i]].count[color[i]]++;
        }

        DFS(1); // Start DFS from the root node
        int answer = calculateAnswer(m);
        cout << answer << '\n';
    }
    return 0;
}