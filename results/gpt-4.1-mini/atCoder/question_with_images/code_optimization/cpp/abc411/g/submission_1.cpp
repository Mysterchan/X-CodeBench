#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int mod = 998244353;

struct mint {
    int x;
    mint(long long v = 0) {
        x = int((v % mod + mod) % mod);
    }
    mint& operator+=(const mint& a) {
        if ((x += a.x) >= mod) x -= mod;
        return *this;
    }
    mint& operator-=(const mint& a) {
        if ((x -= a.x) < 0) x += mod;
        return *this;
    }
    mint& operator*=(const mint& a) {
        x = (int)((long long)x * a.x % mod);
        return *this;
    }
    friend mint operator+(mint a, const mint& b) { return a += b; }
    friend mint operator-(mint a, const mint& b) { return a -= b; }
    friend mint operator*(mint a, const mint& b) { return a *= b; }
    mint pow(ll t) const {
        mint res = 1, cur = *this;
        while (t > 0) {
            if (t & 1) res *= cur;
            cur *= cur;
            t >>= 1;
        }
        return res;
    }
    mint inv() const { return pow(mod - 2); }
    mint& operator/=(const mint& a) { return (*this) *= a.inv(); }
    friend mint operator/(mint a, const mint& b) { return a /= b; }
    friend ostream& operator<<(ostream& os, const mint& m) {
        os << m.x;
        return os;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M; cin >> N >> M;
    vector<vector<int>> adj(N, vector<int>(N, 0));
    for (int i = 0; i < M; i++) {
        int u, v; cin >> u >> v; u--; v--;
        adj[u][v]++;
        adj[v][u]++;
    }

    // dp[u][v][mask]: number of paths starting at u, ending at v, visiting vertices in mask exactly once
    // mask includes u and v
    // We only store dp for masks where u and v are distinct and mask size >= 2
    // N <= 20, so dp size is about N*N*2^N ~ 20*20*1e6 = 400 million entries, too large for full storage
    // We optimize by storing dp as vector<vector<mint>> dp[v][mask], for fixed start u in outer loop

    // We'll implement the same DP but with memory optimization:
    // For each start vertex u:
    //   dp[v][mask]: number of paths from u to v visiting mask vertices
    //   mask always includes u and v
    // We'll build dp by increasing mask size

    // To speed up, we precompute for each vertex the adjacency list with counts
    vector<vector<pair<int,int>>> g(N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (adj[i][j] > 0) {
                g[i].emplace_back(j, adj[i][j]);
            }
        }
    }

    mint ans = 0;

    // We'll do DP for each start vertex u
    // dp[v][mask]: number of paths from u to v visiting mask vertices
    // mask includes u and v
    // We'll store dp as unordered_map<int,mint> or vector<mint> of size 2^N for each v
    // But 20*2^20 is 20 million per u, too big for memory and time
    // So we do a meet-in-the-middle approach:
    // The original code is O(N^2 * 2^N), which is borderline but can be optimized with bitset and careful loops

    // We'll implement the original DP but with bitset and careful iteration order

    // dp[u][v][mask] is large, so we store dp[v][mask] for fixed start u

    // We'll implement the DP as in the original code but with these optimizations:
    // - Use vector<mint> dp for each v
    // - For each mask, iterate over vertices in mask and outside mask efficiently
    // - Use __builtin_popcount and __builtin_ctz for fast bit operations

    // Precompute popcount for all masks
    int max_mask = 1 << N;

    // To reduce memory, we store dp as vector<vector<mint>> dp(N, vector<mint>(max_mask, 0));
    // But this is 20*1e6 = 20 million mint objects, which is large but possibly feasible with fast IO and no overhead

    // We'll try to store dp as vector<vector<mint>> dp(N, vector<mint>(max_mask));
    // Initialize dp[v][mask] = 0

    // Initialize dp for paths of length 2: from u to v with mask = (1<<u) + (1<<v)
    // We'll do for all u,v pairs

    // Then for increasing mask sizes, update dp

    // Finally, sum over all cycles

    // Implementation:

    vector<vector<mint>> dp(N, vector<mint>(max_mask, 0));

    // Initialize dp for paths of length 2
    for (int u = 0; u < N; u++) {
        for (auto& [v, c] : g[u]) {
            if (u == v) continue;
            int mask = (1 << u) | (1 << v);
            dp[v][mask] += mint(c);
        }
    }

    // For masks from size 3 to N
    for (int size = 3; size <= N; size++) {
        // Iterate over masks with popcount == size
        // To speed up, we iterate over masks with popcount == size
        // For each mask, for each v in mask, update dp[v][mask]
        // dp[v][mask] += sum over h in mask\{v} of dp[h][mask^(1<<v)] * adj[h][v]

        // We'll generate masks of size 'size' using std::next_permutation or bit tricks

        // Generate all masks of size 'size'
        // Use Gosper's hack for next combination

        int comb = (1 << size) - 1;
        while (comb < max_mask) {
            // For each v in comb
            // We'll iterate over bits set in comb
            // For each v, compute dp[v][comb]

            // For each v in comb:
            for (int v = 0; v < N; v++) {
                if (!(comb & (1 << v))) continue;
                int prev_mask = comb ^ (1 << v);
                mint val = 0;
                // For each h in prev_mask:
                // dp[v][comb] += dp[h][prev_mask] * adj[h][v]
                // Iterate over bits in prev_mask
                int sub = prev_mask;
                while (sub) {
                    int h = __builtin_ctz(sub);
                    sub &= sub - 1;
                    if (adj[h][v] == 0) continue;
                    val += dp[h][prev_mask] * mint(adj[h][v]);
                }
                dp[v][comb] += val;
            }

            // Gosper's hack to get next combination of size 'size'
            int x = comb & -comb;
            int y = comb + x;
            comb = ((comb & ~y) / x >> 1) | y;
        }
    }

    // Now count cycles
    // For each mask with size >= 2
    // For each pair (u,v) in mask, u < v
    // If size == 2:
    //   cycles += dp[v][mask] * (adj[v][u] - 1)
    // else:
    //   cycles += dp[v][mask] * adj[v][u]
    // Finally, divide cycles of length k by k

    vector<mint> memo(N + 1, 0);

    for (int size = 2; size <= N; size++) {
        int comb = (1 << size) - 1;
        while (comb < max_mask) {
            // Extract vertices in comb
            vector<int> verts;
            int tmp = comb;
            while (tmp) {
                int bit = __builtin_ctz(tmp);
                verts.push_back(bit);
                tmp &= tmp - 1;
            }
            // For each pair u < v
            for (int i = 0; i < (int)verts.size(); i++) {
                for (int j = i + 1; j < (int)verts.size(); j++) {
                    int u = verts[i], v = verts[j];
                    if (size == 2) {
                        // cycles += dp[v][comb] * (adj[v][u] - 1)
                        if (adj[v][u] > 1) {
                            memo[size] += dp[v][comb] * mint(adj[v][u] - 1);
                        }
                    } else {
                        if (adj[v][u] > 0) {
                            memo[size] += dp[v][comb] * mint(adj[v][u]);
                        }
                    }
                }
            }
            // Gosper's hack
            int x = comb & -comb;
            int y = comb + x;
            comb = ((comb & ~y) / x >> 1) | y;
        }
    }

    mint answer = 0;
    for (int k = 2; k <= N; k++) {
        answer += memo[k] / mint(k);
    }

    cout << answer << "\n";

    return 0;
}