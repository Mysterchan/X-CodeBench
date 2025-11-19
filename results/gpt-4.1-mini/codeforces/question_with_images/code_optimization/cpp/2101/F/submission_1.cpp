#include <bits/stdc++.h>
using namespace std;
const int N = 3005;
const int MOD = 998244353;

int n;
vector<int> g[N];
int dist[N][N];
int pw2[N], pw3[N];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    pw2[0] = pw3[0] = 1;
    for (int i = 1; i < N; i++) {
        pw2[i] = (pw2[i - 1] * 2LL) % MOD;
        pw3[i] = (pw3[i - 1] * 3LL) % MOD;
    }

    int T; cin >> T;
    while (T--) {
        cin >> n;
        for (int i = 1; i <= n; i++) g[i].clear();

        for (int i = 1, u, v; i < n; i++) {
            cin >> u >> v;
            g[u].push_back(v);
            g[v].push_back(u);
        }

        // BFS from each node to get all pair distances
        for (int i = 1; i <= n; i++) {
            fill(dist[i] + 1, dist[i] + n + 1, -1);
            dist[i][i] = 0;
            queue<int> q;
            q.push(i);
            while (!q.empty()) {
                int u = q.front(); q.pop();
                for (int w : g[u]) {
                    if (dist[i][w] == -1) {
                        dist[i][w] = dist[i][u] + 1;
                        q.push(w);
                    }
                }
            }
        }

        // Count number of pairs at each distance
        // max distance in tree <= n-1
        vector<long long> countPairs(n, 0);
        for (int u = 1; u <= n; u++) {
            for (int v = u + 1; v <= n; v++) {
                int d = dist[u][v];
                countPairs[d]++;
            }
        }

        // Precompute powers for efficiency
        // sum of coolness = sum_{k=1}^{maxDist} k * (number_of_colorings_with_max_distance_k)
        // Using formula derived from problem editorial:
        // total = (n-1)*3^n - sum_{k=1}^{n-1} [number_of_colorings_with_max_distance_less_than_k]
        // The original code uses inclusion-exclusion with bitsets, but we can optimize by:
        // For each distance k, number_of_colorings_with_max_distance_less_than_k = sum over subsets
        // The problem editorial shows the formula:
        // sum of coolness = (n-1)*3^n - sum_{k=1}^{n-1} f(k)
        // where f(k) = sum over subsets S of vertices with no pair at distance >= k of 2^{|S|}

        // We can rewrite f(k) as:
        // f(k) = sum_{S subset of V, no pair at distance >= k} 2^{|S|}
        // This is equivalent to counting independent sets in a graph where edges connect pairs at distance >= k,
        // with weight 2^{|S|}.

        // The original code uses bitsets and DP to compute f(k).
        // We will optimize by using a DP over vertices with bitsets, but with a more cache-friendly approach.

        // To optimize, we precompute for each vertex u a bitset ban[u] of vertices v where dist[u][v] >= k.
        // Then we do DP over subsets using bitsets.

        // We'll implement a bitset-based DP similar to original but more cache-friendly and without unordered_map.

        // Since n <= 3000, we can use std::bitset for ban arrays.

        // We'll implement the DP as follows:
        // dp is a bitset representing subsets of vertices allowed so far.
        // For each vertex u, we update dp by:
        // dp_new = dp + dp & (~ban[u])
        // where dp & (~ban[u]) means subsets that do not contain any vertex at distance >= k from u.

        // But this is complicated to implement directly with bitsets of subsets (2^n is too large).
        // So we revert to the original approach but optimize the bitset operations and hashing.

        // Instead, we use the formula from the editorial:
        // sum of coolness = sum_{u,v} dist(u,v) * number_of_colorings_where_u is red and v is blue
        // number_of_colorings_where_u is red and v is blue = 3^{n-2} (since colors of other vertices are free)
        // So sum = 3^{n-2} * sum_{u,v} dist(u,v) if u != v
        // But problem states max distance between red and blue vertices, so max over pairs, not sum.

        // So this direct formula doesn't work.

        // We will optimize the original approach by:
        // 1) Precompute all distances with BFS (already done)
        // 2) For each k from 1 to n-1:
        //    - For each vertex u, build a bitset ban[u] where ban[u][v] = 1 if dist[u][v] >= k
        //    - Then do DP over vertices:
        //      dp is a map from bitset to count
        //      For each vertex u:
        //        For each subset s in dp:
        //          dp_new[s] += dp[s]
        //          dp_new[s & ~ban[u]] += dp[s]
        //    - sum f(k) = sum over dp subsets s of dp[s] * 2^{popcount(s)}
        // 3) sumF = sum f(k)
        // 4) answer = (n-1)*3^n - sumF

        // We will implement the bitset as vector<uint64_t> and use a custom hash with __builtin_popcountll.

        // To optimize:
        // - Use static arrays to avoid reallocation
        // - Use reserve for unordered_map
        // - Use fast IO
        // - Use inline functions

        // Implementing optimized bitset and DP:

        using ull = unsigned long long;
        int M = (n + 63) / 64;

        struct BS {
            ull a[48]; // 3000/64 ~ 47
            BS() { memset(a, 0, sizeof(a)); }
            void set_all() {
                int full = n / 64;
                for (int i = 0; i < full; i++) a[i] = ~0ULL;
                int rem = n % 64;
                if (rem) a[full] = (1ULL << rem) - 1;
            }
            void reset() {
                for (int i = 0; i < M; i++) a[i] = 0;
            }
            void set1(int i) {
                a[i >> 6] |= 1ULL << (i & 63);
            }
            BS operator&(const BS &b) const {
                BS r;
                for (int i = 0; i < M; i++) r.a[i] = a[i] & b.a[i];
                return r;
            }
            BS operator~() const {
                BS r;
                for (int i = 0; i < M; i++) r.a[i] = ~a[i];
                int rem = n % 64;
                if (rem) r.a[M - 1] &= (1ULL << rem) - 1;
                return r;
            }
            bool operator==(const BS &b) const {
                for (int i = 0; i < M; i++) if (a[i] != b.a[i]) return false;
                return true;
            }
        };

        struct MyHash {
            size_t operator()(const BS &b) const {
                size_t h = 0;
                for (int i = 0; i < M; i++) {
                    h ^= b.a[i] + 0x9e3779b97f4a7c15ULL + (h << 6) + (h >> 2);
                }
                return h;
            }
        };

        static BS ban[N];

        long long sumF = 0;
        for (int k = 1; k < n; k++) {
            for (int u = 1; u <= n; u++) {
                ban[u].reset();
                ban[u].set1(u - 1);
                for (int v = 1; v <= n; v++) {
                    if (dist[u][v] >= k) ban[u].set1(v - 1);
                }
            }

            unordered_map<BS, int, MyHash> mp, mp2;
            mp.reserve(1 << 12);
            BS all1; all1.set_all();
            mp[all1] = 1;

            for (int u = 1; u <= n; u++) {
                mp2.clear();
                for (auto &it : mp) {
                    const BS &s = it.first;
                    int c = it.second;
                    // Not choose u
                    int &r1 = mp2[s];
                    r1 = (r1 + c) % MOD;
                    // Choose u
                    BS s2 = s & (~ban[u]);
                    int &r2 = mp2[s2];
                    r2 = (r2 + c) % MOD;
                }
                mp.swap(mp2);
            }

            long long fk = 0;
            for (auto &it : mp) {
                int c = it.second;
                const BS &bs = it.first;
                int cnt = 0;
                for (int i = 0; i < M; i++) cnt += __builtin_popcountll(bs.a[i]);
                fk = (fk + 1LL * c * pw2[cnt]) % MOD;
            }
            sumF = (sumF + fk) % MOD;
        }

        long long ans = ((1LL * (n - 1) * pw3[n]) % MOD - sumF) % MOD;
        if (ans < 0) ans += MOD;
        cout << ans << "\n";
    }

    return 0;
}