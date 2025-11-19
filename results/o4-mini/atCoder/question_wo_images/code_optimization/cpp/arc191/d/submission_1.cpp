#include <bits/stdc++.h>
using namespace std;
struct Edge {
    int to, rev, cap, cost;
};
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, S, T;
    cin >> N >> M >> S >> T;
    --S; --T;
    int V = 2 * N;
    vector<vector<Edge>> G(V);
    auto add_edge = [&](int fr, int to, int cap, int cost){
        G[fr].push_back({to, (int)G[to].size(), cap, cost});
        G[to].push_back({fr, (int)G[fr].size() - 1, 0, -cost});
    };

    // Split each vertex v into v_in = v, v_out = v+N
    // Capacity on v_in->v_out is 2 for S and T, 1 otherwise
    for(int v = 0; v < N; v++){
        int c = (v == S || v == T ? 2 : 1);
        add_edge(v, v + N, c, 0);
    }
    // For each undirected edge u-v, add directed arcs u_out->v_in and v_out->u_in with cost 1
    for(int i = 0; i < M; i++){
        int u, v;
        cin >> u >> v;
        --u; --v;
        add_edge(u + N, v, 1, 1);
        add_edge(v + N, u, 1, 1);
    }

    int s = S;        // source is S_in
    int t = T + N;    // sink is T_out
    const int INF = 1000000000;
    vector<int> h(V, 0), dist(V), prevv(V), preve(V);
    int flow = 0, cost = 0, maxf = 2;

    // Min-Cost Max-Flow (successive shortest augmenting path with potentials)
    while(flow < maxf){
        // Dijkstra to find shortest path wrt reduced costs
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
        fill(dist.begin(), dist.end(), INF);
        dist[s] = 0;
        pq.emplace(0, s);
        while(!pq.empty()){
            auto [d, v] = pq.top(); pq.pop();
            if(d > dist[v]) continue;
            for(int i = 0; i < (int)G[v].size(); i++){
                Edge &e = G[v][i];
                if(e.cap > 0){
                    int nd = dist[v] + e.cost + h[v] - h[e.to];
                    if(nd < dist[e.to]){
                        dist[e.to] = nd;
                        prevv[e.to] = v;
                        preve[e.to] = i;
                        pq.emplace(nd, e.to);
                    }
                }
            }
        }
        if(dist[t] == INF) break;
        // Update potentials
        for(int v = 0; v < V; v++){
            if(dist[v] < INF) h[v] += dist[v];
        }
        // Add as much flow as possible (here, 1 unit each time)
        int d = maxf - flow;
        int v = t;
        while(v != s){
            d = min(d, G[prevv[v]][preve[v]].cap);
            v = prevv[v];
        }
        flow += d;
        cost += d * h[t];
        v = t;
        while(v != s){
            Edge &e = G[prevv[v]][preve[v]];
            e.cap -= d;
            G[v][e.rev].cap += d;
            v = prevv[v];
        }
    }

    if(flow < 2) {
        cout << -1 << "\n";
    } else {
        cout << cost << "\n";
    }
    return 0;
}