#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <unordered_map>

using namespace std;

constexpr int MOD = 998244353;

struct mint {
    int val;
    mint(long long v = 0) {
        val = int((v % MOD + MOD) % MOD);
    }
    mint& operator+=(const mint& other) {
        val += other.val;
        if (val >= MOD) val -= MOD;
        return *this;
    }
    mint& operator*=(const mint& other) {
        val = int((long long)val * other.val % MOD);
        return *this;
    }
    friend mint operator+(mint a, const mint& b) { return a += b; }
    friend mint operator*(mint a, const mint& b) { return a *= b; }
    bool operator==(const mint& other) const { return val == other.val; }
};

// Custom hash for pair<vector<int>, int> to use in unordered_map
struct StateHash {
    size_t operator()(const pair<vector<int>, int>& p) const {
        size_t seed = p.second;
        for (int x : p.first) {
            seed = seed * 31 + x;
        }
        return seed;
    }
};

int N;
vector<vector<int>> A;

// Memoization with unordered_map and custom hash for speed
unordered_map<pair<vector<int>, int>, mint, StateHash> memo;

mint count_trees(const vector<int>& S, int R) {
    if (S.size() == 1) return mint(1);

    // S is always sorted before calling this function
    pair<vector<int>, int> state = {S, R};
    auto it = memo.find(state);
    if (it != memo.end()) return it->second;

    // Check if R is connected to all nodes in S
    for (int v : S) {
        if (A[R - 1][v - 1] == 0) return memo[state] = mint(0);
    }

    // Build subgraph excluding R
    vector<int> S_minus_R;
    S_minus_R.reserve(S.size() - 1);
    unordered_map<int, int> val_to_idx;
    for (int v : S) {
        if (v != R) {
            val_to_idx[v] = (int)S_minus_R.size();
            S_minus_R.push_back(v);
        }
    }
    if (S_minus_R.empty()) return memo[state] = mint(1);

    int sz = (int)S_minus_R.size();
    vector<vector<int>> adj(sz);
    for (int i = 0; i < sz; ++i) {
        int vi = S_minus_R[i] - 1;
        for (int j = i + 1; j < sz; ++j) {
            int vj = S_minus_R[j] - 1;
            if (A[vi][vj] == 1) {
                adj[i].push_back(j);
                adj[j].push_back(i);
            }
        }
    }

    // Find connected components in subgraph
    vector<bool> visited(sz, false);
    vector<vector<int>> components;
    for (int i = 0; i < sz; ++i) {
        if (!visited[i]) {
            vector<int> comp;
            vector<int> stack = {i};
            visited[i] = true;
            for (int idx = 0; idx < (int)stack.size(); ++idx) {
                int u = stack[idx];
                comp.push_back(S_minus_R[u]);
                for (int w : adj[u]) {
                    if (!visited[w]) {
                        visited[w] = true;
                        stack.push_back(w);
                    }
                }
            }
            components.push_back(move(comp));
        }
    }

    // Check no edges between different components
    // Optimization: For each component, build a bitset of nodes for O(1) checks
    // But since sum N^2 is small, nested loops are acceptable here.
    for (size_t i = 0; i < components.size(); ++i) {
        for (size_t j = i + 1; j < components.size(); ++j) {
            const auto& c1 = components[i];
            const auto& c2 = components[j];
            for (int x : c1) {
                int xi = x - 1;
                for (int y : c2) {
                    if (A[xi][y - 1] == 1) return memo[state] = mint(0);
                }
            }
        }
    }

    mint total(1);
    // For each component, find potential roots Kp (nodes connected to all others in component)
    for (const auto& comp : components) {
        vector<int> Kp;
        for (int v : comp) {
            bool ok = true;
            int vi = v - 1;
            for (int u : comp) {
                if (A[vi][u - 1] == 0) {
                    ok = false;
                    break;
                }
            }
            if (ok) Kp.push_back(v);
        }
        if (Kp.empty()) return memo[state] = mint(0);

        mint comp_sum(0);
        // Sort comp once for recursive calls to keep memo keys consistent
        vector<int> comp_sorted = comp;
        sort(comp_sorted.begin(), comp_sorted.end());
        for (int root : Kp) {
            comp_sum += count_trees(comp_sorted, root);
        }
        if (comp_sum.val == 0) return memo[state] = mint(0);
        total *= comp_sum;
    }

    return memo[state] = total;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while (T--) {
        cin >> N;
        A.assign(N, vector<int>(N));
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                cin >> A[i][j];

        // Quick checks for invalid input
        bool possible = true;
        for (int i = 0; i < N && possible; ++i) {
            if (A[i][i] == 0) possible = false;
        }
        for (int i = 0; i < N && possible; ++i) {
            for (int j = i + 1; j < N; ++j) {
                if (A[i][j] != A[j][i]) {
                    possible = false;
                    break;
                }
            }
        }
        for (int j = 0; j < N && possible; ++j) {
            if (A[0][j] == 0) possible = false;
        }
        if (!possible) {
            cout << 0 << "\n";
            continue;
        }

        vector<int> initial_S(N);
        iota(initial_S.begin(), initial_S.end(), 1);
        // Sort initial_S once for consistent memo keys
        sort(initial_S.begin(), initial_S.end());

        memo.clear();
        mint ans = count_trees(initial_S, 1);
        cout << ans.val << "\n";
    }
    return 0;
}