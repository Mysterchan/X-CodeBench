#include <bits/stdc++.h>

using namespace std;

#define int long long
const int INF = 0x3F3F3F3F;
using ii = pair<int, int>;
using ll = long long;
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()

const bool DEBUG = true;



struct MinCostMaxFlow {
    const int INF = 1e18;
    vector<vector<int>> adj, cap, cost;
    vector<int> p, d;
    int n, s, t;

    MinCostMaxFlow(int n, int s, int t) : n(n), s(s), t(t) {
        adj.resize(n);
        cap.assign(n, vector<int>(n, 0));
        cost.assign(n, vector<int>(n, INF));
    }

    void addEdge(int u, int v, int ecap, int ecost) {
        adj[u].push_back(v);
        adj[v].push_back(u);
        cap[u][v] += ecap;
        cost[u][v] = min(cost[u][v], ecost);
        cost[v][u] = min(cost[v][u], -ecost);
    }

    bool spfa() {
        int n = adj.size();
        d.assign(n, INF);
        vector<bool> inqueue(n, false);
        queue<int> q;
        p.assign(n, -1);

        d[s] = 0;
        q.push(s);
        inqueue[s] = true;
        while (!q.empty()) {
            int v = q.front(); q.pop();
            inqueue[v] = false;

            for (int to : adj[v]) {
                int len = cost[v][to];
                if (d[v] != INF && d[v] + len < d[to] && cap[v][to] > 0) {
                    d[to] = d[v] + len;
                    p[to] = v;
                    if (!inqueue[to]) {
                        q.push(to);
                        inqueue[to] = true;
                    }
                }
            }
        }

        return d[t] != INF;
    }

    int maxflow() {
        int ans = 0;
        int maxflow = 0, cost = 0;
        while (spfa()) {
            int increment = INF;
            for (int u = t; p[u] >= 0; u = p[u])
                increment = min(increment, cap[p[u]][u]);

            for (int u = t; p[u] >= 0; u = p[u]) {
                cap[p[u]][u] -= increment;
                cap[u][p[u]] += increment;              
            }
            cost += increment * d[t];
            maxflow += increment;
            ans = min(ans, cost);
        }
        return ans;
    }
};

vector<ii> cor = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

signed main() {
    cin.tie(0)->sync_with_stdio(0);

    int h, w;
    cin >> h >> w;
    vector<vector<int>> grid(h, vector<int>(w));
    int gridsum = 0;
    for (vector<int> &v : grid)
        for (int &i : v)
            cin >> i, gridsum += i;

    const int SIZE = h*w+2;
    const int SOURCE = h*w;
    const int SINK = h*w+1;
    MinCostMaxFlow mf(SIZE, SOURCE, SINK);

    auto getId = [&](int i, int j) { return i*w+j; };

    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if ((i+j)%2 == 1) mf.addEdge(getId(i, j), SINK, 1, 0);
            else {
                mf.addEdge(SOURCE, getId(i, j), 1, 0);
                for (auto [x, y] : cor) {
                    int ii = x+i;
                    int jj = y+j;
                    if (ii >= 0 && ii < h && jj >= 0 && jj < w) {
                        int val = (grid[i][j] + grid[ii][jj]);
                        if (val < 0)
                            mf.addEdge(getId(i, j), getId(ii, jj), 1, val);
                    }
                }
            }
        }
    }

    cout << gridsum - mf.maxflow() << '\n';
    
    return 0;
}