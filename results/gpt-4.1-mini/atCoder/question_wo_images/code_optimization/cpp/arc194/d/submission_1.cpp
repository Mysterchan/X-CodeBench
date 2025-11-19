#include <bits/stdc++.h>
using namespace std;

const int mod = 998244353;

int n;
string s;

vector<long long> fact, inv_fact;

long long modexp(long long base, long long exp) {
    long long res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) res = res * base % mod;
        base = base * base % mod;
        exp >>= 1;
    }
    return res;
}

long long inv(long long x) {
    return modexp(x, mod - 2);
}

void precompute_factorials(int max_n) {
    fact.assign(max_n + 1, 1);
    inv_fact.assign(max_n + 1, 1);
    for (int i = 1; i <= max_n; i++) fact[i] = fact[i - 1] * i % mod;
    inv_fact[max_n] = inv(fact[max_n]);
    for (int i = max_n - 1; i >= 0; i--) inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod;
}

// Instead of reconstructing strings and sorting, we use a canonical form based on subtree hashes.
// This avoids expensive string operations and speeds up the solution drastically.

struct Hasher {
    static const uint64_t base = 131;
    static const uint64_t mod64 = (1ULL << 61) - 1;

    static uint64_t modmul(uint64_t a, uint64_t b) {
        __uint128_t res = (__uint128_t)a * b;
        res = (res >> 61) + (res & mod64);
        if (res >= mod64) res -= mod64;
        return (uint64_t)res;
    }

    static uint64_t combine(uint64_t a, uint64_t b) {
        return modmul(a, base) + b < mod64 ? modmul(a, base) + b : modmul(a, base) + b - mod64;
    }
};

vector<vector<int>> adj;
vector<uint64_t> hash_val;

// Compute hash of subtree rooted at u
// Hash = hash of '(' + sorted hashes of children + hash of ')'
// This corresponds to the canonical form of the subtree.
uint64_t dfs_hash(int u) {
    vector<uint64_t> child_hashes;
    for (int v : adj[u]) {
        child_hashes.push_back(dfs_hash(v));
    }
    sort(child_hashes.begin(), child_hashes.end());

    uint64_t h = '('; // use ASCII code of '(' as starting hash
    for (auto &ch : child_hashes) {
        h = Hasher::combine(h, ch);
    }
    h = Hasher::combine(h, ')'); // append ')'
    return h;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> s;

    precompute_factorials(n);

    // Build tree from parentheses
    // Each '(' is a node, edges to immediate children
    adj.assign(n + 1, vector<int>());
    vector<int> st;
    st.reserve(n);
    int node_id = 0; // root = 0 (virtual root)
    for (int i = 0; i < n; i++) {
        if (s[i] == '(') {
            int cur = i + 1; // use 1-based indexing for nodes
            if (st.empty()) {
                adj[0].push_back(cur);
            } else {
                adj[st.back()].push_back(cur);
            }
            st.push_back(cur);
        } else {
            st.pop_back();
        }
    }

    // For each node, count how many children with each hash
    // The answer is product over all nodes of multinomial coefficients of their children hashes

    // We'll do a post-order traversal to compute hashes and multinomial counts

    // Store hash for each node
    hash_val.assign(n + 1, 0);

    // Post-order traversal to compute hashes and multinomial coefficients
    // We'll do iterative DFS to avoid recursion overhead

    vector<int> order;
    vector<int> stack = {0};
    vector<bool> visited(n + 1, false);
    while (!stack.empty()) {
        int u = stack.back();
        if (!visited[u]) {
            visited[u] = true;
            for (int v : adj[u]) stack.push_back(v);
        } else {
            stack.pop_back();
            order.push_back(u);
        }
    }

    long long ans = 1;

    for (int u : order) {
        if (u == 0) {
            // virtual root, no hash needed
            continue;
        }
        vector<uint64_t> child_hashes;
        for (int v : adj[u]) {
            child_hashes.push_back(hash_val[v]);
        }
        sort(child_hashes.begin(), child_hashes.end());

        // Compute hash for u
        uint64_t h = '(';
        for (auto &ch : child_hashes) {
            h = Hasher::combine(h, ch);
        }
        h = Hasher::combine(h, ')');
        hash_val[u] = h;

        // Count frequencies of child hashes
        // Compute multinomial coefficient for children
        int sz = (int)child_hashes.size();
        if (sz > 0) {
            long long ways = fact[sz];
            int count = 1;
            for (int i = 1; i <= sz; i++) {
                if (i == sz || child_hashes[i] != child_hashes[i - 1]) {
                    ways = ways * inv_fact[count] % mod;
                    count = 1;
                } else {
                    count++;
                }
            }
            ans = ans * ways % mod;
        }
    }

    cout << ans << "\n";

    return 0;
}