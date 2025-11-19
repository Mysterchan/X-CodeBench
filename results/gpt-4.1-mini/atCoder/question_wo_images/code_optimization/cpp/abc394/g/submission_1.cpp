#include <bits/stdc++.h>
using namespace std;

struct DSU {
    vector<int> f, sz;
    stack<pair<int, int>> sk;
    DSU(int n) : f(n), sz(n, 1) {
        iota(f.begin(), f.end(), 0);
    }
    int find(int u) {
        while (f[u] != u) u = f[u];
        return u;
    }
    void merge(int u, int v) {
        u = find(u);
        v = find(v);
        if (u == v) return;
        if (sz[u] < sz[v]) swap(u, v);
        sk.emplace(u, v);
        f[v] = u;
        sz[u] += sz[v];
    }
    void back(int n) {
        while ((int)sk.size() > n) {
            auto [u, v] = sk.top(); sk.pop();
            f[v] = v;
            sz[u] -= sz[v];
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H, W; cin >> H >> W;
    vector<vector<int>> F(H + 1, vector<int>(W + 1));
    int maxF = 0;
    for (int i = 1; i <= H; i++) {
        for (int j = 1; j <= W; j++) {
            cin >> F[i][j];
            if (F[i][j] > maxF) maxF = F[i][j];
        }
    }

    int Q; cin >> Q;
    struct Query {
        int A, B, Y, C, D, Z, id;
    };
    vector<Query> queries(Q);
    for (int i = 0; i < Q; i++) {
        int A, B, Y, C, D, Z;
        cin >> A >> B >> Y >> C >> D >> Z;
        queries[i] = {A, B, Y, C, D, Z, i};
    }

    // DSU on grid cells
    auto get = [&](int x, int y) { return (x - 1) * W + (y - 1); };
    DSU dsu(H * W);

    // Directions for adjacency
    constexpr int dx[4] = {0, 0, 1, -1};
    constexpr int dy[4] = {1, -1, 0, 0};

    vector<int> ans(Q);

    // Divide and conquer on answer (stairs usage)
    function<void(int,int,vector<Query>&)> solve = [&](int l, int r, vector<Query> &qs) {
        if (qs.empty()) return;
        if (l == r) {
            // If l is fixed stairs usage, answer is abs(Y - Z) if l > max(Y,Z)
            for (auto &q : qs) {
                int maxYZ = max(q.Y, q.Z);
                if (l > maxYZ) {
                    ans[q.id] = abs(q.Y - q.Z);
                } else {
                    ans[q.id] = abs(q.Y - l) + abs(q.Z - l);
                }
            }
            return;
        }
        int mid = (l + r) >> 1;

        // Save DSU state
        int sz = (int)dsu.sk.size();

        // Merge all buildings with floors > mid
        for (int i = 1; i <= H; i++) {
            for (int j = 1; j <= W; j++) {
                if (F[i][j] <= mid) continue;
                for (int d = 0; d < 4; d++) {
                    int ni = i + dx[d], nj = j + dy[d];
                    if (ni < 1 || ni > H || nj < 1 || nj > W) continue;
                    if (F[ni][nj] <= mid) continue;
                    dsu.merge(get(i, j), get(ni, nj));
                }
            }
        }

        vector<Query> leftQ, rightQ;
        for (auto &q : qs) {
            int u = dsu.find(get(q.A, q.B));
            int v = dsu.find(get(q.C, q.D));
            if (u == v) {
                rightQ.push_back(q);
            } else {
                leftQ.push_back(q);
            }
        }

        dsu.back(sz);

        if (!leftQ.empty()) solve(l, mid, leftQ);
        if (!rightQ.empty()) solve(mid + 1, r, rightQ);
    };

    solve(0, maxF, queries);

    for (int i = 0; i < Q; i++) {
        cout << ans[i] << "\n";
    }

    return 0;
}