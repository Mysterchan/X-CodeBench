#include <bits/stdc++.h>
using namespace std;
using pii = pair<int,int>;
struct DSU {
    int n;
    vector<int> p, r;
    DSU(int _n): n(_n), p(_n), r(_n,0) {
        iota(p.begin(), p.end(), 0);
    }
    int find(int x) {
        if (p[x]==x) return x;
        return p[x] = find(p[x]);
    }
    bool unite(int x, int y) {
        x = find(x); y = find(y);
        if (x==y) return false;
        if (r[x]<r[y]) swap(x,y);
        p[y] = x;
        if (r[x]==r[y]) r[x]++;
        return true;
    }
};
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int H, W;
    cin >> H >> W;
    int N = H * W;
    vector<int> F(N);
    for(int i=0;i<H;i++){
        for(int j=0;j<W;j++){
            int x; cin >> x;
            F[i*W + j] = x;
        }
    }
    // build edges
    vector<tuple<int,int,int>> edges;
    edges.reserve((H*(W-1) + (H-1)*W));
    for(int i=0;i<H;i++){
        for(int j=0;j<W;j++){
            int u = i*W + j;
            if(j+1 < W){
                int v = i*W + (j+1);
                int w = min(F[u], F[v]);
                edges.emplace_back(w, u, v);
            }
            if(i+1 < H){
                int v = (i+1)*W + j;
                int w = min(F[u], F[v]);
                edges.emplace_back(w, u, v);
            }
        }
    }
    sort(edges.begin(), edges.end(),
         [](auto &a, auto &b){
             return get<0>(a) > get<0>(b);
         });
    DSU dsu(N);
    vector<vector<pii>> g(N);
    g.reserve(N);
    int added = 0;
    for(auto &e : edges){
        int w,u,v;
        tie(w,u,v) = e;
        if(dsu.unite(u,v)){
            g[u].emplace_back(v, w);
            g[v].emplace_back(u, w);
            added++;
            if(added == N-1) break;
        }
    }
    // LCA prep
    const int LOG = 19;
    const int INF = 1000000007;
    vector< array<int, LOG> > parent(N);
    vector< array<int, LOG> > minEdge(N);
    vector<int> depth(N, -1);
    // BFS from node 0
    queue<int> q;
    depth[0] = 0;
    parent[0][0] = 0;
    minEdge[0][0] = INF;
    q.push(0);
    while(!q.empty()){
        int u = q.front(); q.pop();
        for(auto &pr : g[u]){
            int v = pr.first;
            int w = pr.second;
            if(depth[v] == -1){
                depth[v] = depth[u] + 1;
                parent[v][0] = u;
                minEdge[v][0] = w;
                q.push(v);
            }
        }
    }
    // For any unreachable (shouldn't happen), attach to root
    for(int i=0;i<N;i++){
        if(depth[i]==-1){
            depth[i]=0;
            parent[i][0]=i;
            minEdge[i][0]=INF;
        }
    }
    // Binary lifting
    for(int k=1; k<LOG; k++){
        for(int v=0; v<N; v++){
            int mid = parent[v][k-1];
            parent[v][k] = parent[mid][k-1];
            minEdge[v][k] = min(minEdge[v][k-1], minEdge[mid][k-1]);
        }
    }
    auto getMinEdgeOnPath = [&](int u, int v){
        if(u==v) return INF;
        int res = INF;
        if(depth[u] < depth[v]) swap(u,v);
        int diff = depth[u] - depth[v];
        for(int k=0; k<LOG; k++){
            if(diff & (1<<k)){
                res = min(res, minEdge[u][k]);
                u = parent[u][k];
            }
        }
        if(u == v) return res;
        for(int k=LOG-1; k>=0; k--){
            if(parent[u][k] != parent[v][k]){
                res = min(res, minEdge[u][k]);
                res = min(res, minEdge[v][k]);
                u = parent[u][k];
                v = parent[v][k];
            }
        }
        // now parent[0] is LCA
        res = min(res, minEdge[u][0]);
        res = min(res, minEdge[v][0]);
        return res;
    };
    int Q;
    cin >> Q;
    ostringstream out;
    for(int qi=0; qi<Q; qi++){
        int A,B,Y,Cp,D,Z;
        cin >> A >> B >> Y >> Cp >> D >> Z;
        int u = (A-1)*W + (B-1);
        int v = (Cp-1)*W + (D-1);
        int Cval = getMinEdgeOnPath(u, v);
        // if same cell, Cval = INF
        int mn = min(Y, Z);
        long long ans;
        if(Cval >= mn){
            ans = llabs((long long)Y - (long long)Z);
        } else {
            ans = (long long)Y + (long long)Z - 2LL * Cval;
        }
        out << ans << '\n';
    }
    cout << out.str();
    return 0;
}