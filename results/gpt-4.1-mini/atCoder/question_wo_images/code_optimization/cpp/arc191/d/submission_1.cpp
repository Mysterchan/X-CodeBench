#include <bits/stdc++.h>
using namespace std;

static const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, S, T;
    cin >> N >> M >> S >> T;

    vector<vector<int>> g(N + 1);
    for (int i = 0; i < M; i++) {
        int u, v; cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    auto bfs = [&](int src) {
        vector<int> d(N + 1, INF);
        queue<int> q;
        d[src] = 0;
        q.push(src);
        while (!q.empty()) {
            int v = q.front(); q.pop();
            for (int to : g[v]) {
                if (d[to] == INF) {
                    d[to] = d[v] + 1;
                    q.push(to);
                }
            }
        }
        return d;
    };

    vector<int> dS = bfs(S);
    vector<int> dT = bfs(T);

    if (dS[T] == INF) {
        cout << -1 << '\n';
        return 0;
    }

    // The minimal base cost is 2 * dS[T]
    const long long baseLower = 2LL * dS[T];

    // Use a vector for visited states instead of unordered_map for speed
    // State: (a, b) positions of pieces A and B
    // We encode state as a single integer: a * (N+1) + b
    // N can be up to 2e5, so max states ~4e10, too large for full visited array
    // So we use a hash map but with a faster custom hash and reserve large capacity

    struct PairHash {
        size_t operator()(const uint64_t &x) const noexcept {
            // Splitmix64 hash for better distribution
            uint64_t z = x + 0x9e3779b97f4a7c15;
            z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9;
            z = (z ^ (z >> 27)) * 0x94d049bb133111eb;
            return z ^ (z >> 31);
        }
    };

    auto keyOf = [&](int a, int b) -> uint64_t {
        return (uint64_t)a << 32 | (uint64_t)b;
    };

    // Use a deque for 0-1-2 BFS with 3 buckets
    array<deque<pair<int,int>>,3> bucket;
    // dist map: key -> minimal cost from start state (S,T)
    // reserve large capacity to reduce rehashing
    unordered_map<uint64_t,int,PairHash> dist;
    dist.reserve(1 << 20);
    dist.max_load_factor(0.7f);

    auto push_state = [&](int a, int b, int nd) {
        uint64_t k = keyOf(a,b);
        auto it = dist.find(k);
        if (it == dist.end() || nd < it->second) {
            dist[k] = nd;
            bucket[nd % 3].emplace_back(a,b);
        }
    };

    push_state(S, T, 0);

    int curd = 0;
    int bi = 0;

    auto pull_next = [&]() -> pair<int,int> {
        for (int tries = 0; tries < 3; tries++) {
            if (!bucket[bi].empty()) {
                auto p = bucket[bi].front();
                bucket[bi].pop_front();
                return p;
            }
            bi = (bi + 1) % 3;
            curd++;
        }
        return {-1,-1};
    };

    while (true) {
        auto [a,b] = pull_next();
        if (a == -1) {
            cout << -1 << '\n';
            return 0;
        }
        auto it = dist.find(keyOf(a,b));
        if (it == dist.end() || it->second != curd) continue;

        if (a == T && b == S) {
            cout << (baseLower + curd) << '\n';
            return 0;
        }

        // Move piece A
        for (int an : g[a]) {
            if (an == b) continue;
            // w = 1 + (dT[an] - dT[a]) in {0,1,2}
            int w = 1 + (dT[an] - dT[a]);
            int nd = curd + w;
            push_state(an, b, nd);
        }
        // Move piece B
        for (int bn : g[b]) {
            if (bn == a) continue;
            // w = 1 + (dS[bn] - dS[b]) in {0,1,2}
            int w = 1 + (dS[bn] - dS[b]);
            int nd = curd + w;
            push_state(a, bn, nd);
        }
    }

    return 0;
}