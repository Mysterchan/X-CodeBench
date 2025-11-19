#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using pll = pair<ll, ll>;

const ll INF = 1e18;
const ll OFFSET = 2e12;

struct Edge {
    int to, rev;
    ll cap, cost;
};

struct MinCostMaxFlow {
    int n;
    vector<vector<Edge>> G;
    vector<ll> dist, h, prevv, preve;

    MinCostMaxFlow(int n) : n(n), G(n), dist(n), h(n), prevv(n), preve(n) {}

    void add_edge(int from, int to, ll cap, ll cost) {
        G[from].push_back({to, (int)G[to].size(), cap, cost});
        G[to].push_back({from, (int)G[from].size() - 1, 0, -cost});
    }

    ll min_cost_flow(int s, int t) {
        ll res = 0;
        fill(h.begin(), h.end(), 0);
        while (true) {
            priority_queue<pll, vector<pll>, greater<pll>> pq;
            fill(dist.begin(), dist.end(), INF);
            dist[s] = 0;
            pq.push({0, s});
            while (!pq.empty()) {
                auto [d, v] = pq.top(); pq.pop();
                if (dist[v] < d) continue;
                for (int i = 0; i < (int)G[v].size(); i++) {
                    Edge &e = G[v][i];
                    if (e.cap > 0 && dist[e.to] > dist[v] + e.cost + h[v] - h[e.to]) {
                        dist[e.to] = dist[v] + e.cost + h[v] - h[e.to];
                        prevv[e.to] = v;
                        preve[e.to] = i;
                        pq.push({dist[e.to], e.to});
                    }
                }
            }
            if (dist[t] == INF) break;
            for (int v = 0; v < n; v++) h[v] += dist[v];
            ll d = INF;
            for (int v = t; v != s; v = prevv[v]) {
                d = min(d, G[prevv[v]][preve[v]].cap);
            }
            res += d * h[t];
            for (int v = t; v != s; v = prevv[v]) {
                Edge &e = G[prevv[v]][preve[v]];
                e.cap -= d;
                G[v][e.rev].cap += d;
            }
        }
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H, W; cin >> H >> W;
    vector<vector<ll>> A(H, vector<ll>(W));
    ll total_sum = 0;
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            cin >> A[i][j];
            total_sum += A[i][j];
        }
    }

    // Build bipartite graph: cells with (r+c) even on left, odd on right
    // Edges between adjacent cells with negative sum of values
    int N = H * W;
    int S = N, T = N + 1;
    MinCostMaxFlow mcmf(N + 2);

    auto id = [&](int r, int c) { return r * W + c; };

    // Add edges from S to even cells, odd cells to T
    for (int r = 0; r < H; r++) {
        for (int c = 0; c < W; c++) {
            int u = id(r, c);
            if ((r + c) % 2 == 0) {
                mcmf.add_edge(S, u, 1, 0);
            } else {
                mcmf.add_edge(u, T, 1, 0);
            }
        }
    }

    // Directions: right and down only (to avoid duplicates)
    const int dr[2] = {0, 1};
    const int dc[2] = {1, 0};

    for (int r = 0; r < H; r++) {
        for (int c = 0; c < W; c++) {
            if ((r + c) % 2 != 0) continue; // only from even cells
            int u = id(r, c);
            for (int dir = 0; dir < 2; dir++) {
                int nr = r + dr[dir], nc = c + dc[dir];
                if (nr < 0 || nr >= H || nc < 0 || nc >= W) continue;
                int v = id(nr, nc);
                ll sum_cells = A[r][c] + A[nr][nc];
                if (sum_cells < 0) {
                    // cost = sum_cells + OFFSET to keep cost positive
                    // We want to minimize total cost, so cost = sum_cells + OFFSET
                    // The OFFSET is large enough to keep costs positive
                    mcmf.add_edge(u, v, 1, sum_cells + OFFSET);
                }
            }
        }
    }

    ll flow_cost = mcmf.min_cost_flow(S, T);

    // The answer is total_sum - (flow_cost - OFFSET * flow)
    // But flow is number of matched edges = number of dominoes placed
    // flow_cost includes OFFSET * flow, so subtract OFFSET * flow to get sum of negative sums
    // We want to maximize total_sum - sum_of_covered_cells = total_sum - (sum_of_covered_cells)
    // sum_of_covered_cells = sum of values in covered cells = sum of negative sums of dominoes
    // flow_cost = sum of (sum_cells + OFFSET) = sum_of_covered_cells + OFFSET * flow
    // So total_sum - sum_of_covered_cells = total_sum - (flow_cost - OFFSET * flow) = total_sum - flow_cost + OFFSET * flow

    // To get flow (number of dominoes placed), count edges from S with capacity used
    // But easier: flow = number of edges used from S to even cells = number of dominoes placed
    // We can count flow by summing capacity used on edges from S

    ll flow = 0;
    for (auto &e : mcmf.G[S]) {
        flow += (1 - e.cap); // capacity was 1, so used = 1 - cap
    }

    ll answer = total_sum - (flow_cost - OFFSET * flow);
    cout << answer << "\n";

    return 0;
}