#include <bits/stdc++.h>
using namespace std;

struct DSU {
    vector<int> p, r;
    DSU(int n): p(n), r(n,1) { iota(p.begin(), p.end(), 0); }
    int find(int x){ return p[x]==x? x : p[x]=find(p[x]); }
    bool unite(int a,int b){
        a = find(a); b = find(b);
        if(a==b) return false;
        if(r[a]<r[b]) swap(a,b);
        p[b]=a; r[a]+=r[b];
        return true;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H,W;
    cin >> H >> W;
    int N = H*W;
    vector<int> height(N);
    for(int i=0;i<N;i++){
        cin >> height[i];
    }

    // build all edges with weight = min(height[u],height[v])
    vector<array<int,3>> edges;
    edges.reserve(2*N);
    auto idx = [&](int i,int j){ return i*W + j; };
    for(int i=0;i<H;i++){
        for(int j=0;j<W;j++){
            int u = idx(i,j);
            if(i+1<H){
                int v = idx(i+1,j);
                int w = min(height[u], height[v]);
                edges.push_back({w, u, v});
            }
            if(j+1<W){
                int v = idx(i,j+1);
                int w = min(height[u], height[v]);
                edges.push_back({w, u, v});
            }
        }
    }
    // sort descending by weight
    sort(edges.begin(), edges.end(),
         [](auto &a, auto &b){ return a[0] > b[0]; });

    // Kruskal to build maximum spanning tree
    DSU dsu(N);
    vector<vector<pair<int,int>>> adj(N);
    for(auto &e: edges){
        int w=e[0], u=e[1], v=e[2];
        if(dsu.unite(u,v)){
            adj[u].push_back({v,w});
            adj[v].push_back({u,w});
        }
    }

    // Prepare LCA structures
    int LOG = 18;           // since 2^18 = 262144 > N=250k
    const int INF = 1000000007;
    vector<int> depth(N,0);
    static int parent[19][250000];
    static int minE[19][250000];

    // DFS from node 0
    {
        vector<int> stk;
        stk.reserve(N);
        stk.push_back(0);
        parent[0][0] = 0;
        minE[0][0] = INF;
        depth[0] = 0;
        vector<char> seen(N,0);
        seen[0] = 1;
        while(!stk.empty()){
            int u = stk.back(); stk.pop_back();
            for(auto &pr: adj[u]){
                int v = pr.first, w=pr.second;
                if(!seen[v]){
                    seen[v]=1;
                    depth[v]=depth[u]+1;
                    parent[0][v]=u;
                    minE[0][v]=w;
                    stk.push_back(v);
                }
            }
        }
    }

    // Build up the 2^k ancestors and min‐edge to ancestor
    for(int k=1;k<LOG;k++){
        for(int v=0;v<N;v++){
            int mid = parent[k-1][v];
            parent[k][v] = parent[k-1][ mid ];
            minE[k][v] = min(minE[k-1][v], minE[k-1][ mid ]);
        }
    }

    // LCA‐based routine to find min edge on path u<->v
    auto getMinEdge = [&](int u,int v){
        int res = INF;
        if(depth[u]<depth[v]) swap(u,v);
        int diff = depth[u]-depth[v];
        for(int k=0;k<LOG;k++){
            if(diff & (1<<k)){
                res = min(res, minE[k][u]);
                u = parent[k][u];
            }
        }
        if(u==v) return res;
        for(int k=LOG-1;k>=0;k--){
            if(parent[k][u]!=parent[k][v]){
                res = min(res, minE[k][u]);
                res = min(res, minE[k][v]);
                u = parent[k][u];
                v = parent[k][v];
            }
        }
        // last step to LCA
        res = min(res, minE[0][u]);
        res = min(res, minE[0][v]);
        return res;
    };

    // Answer queries
    int Q; cin >> Q;
    while(Q--){
        int a,b,y,c,d,z;
        cin >> a >> b >> y >> c >> d >> z;
        --a; --b; --c; --d;
        int u = idx(a,b), v = idx(c,d);
        if(u==v){
            // same building
            cout << abs(y-z) << "\n";
            continue;
        }
        int M = getMinEdge(u,v);
        int lo = min(y,z);
        if(M >= lo){
            // can walk at level lo or higher for free
            cout << abs(y-z) << "\n";
        } else {
            // must descend to M from both ends
            cout << (y - M) + (z - M) << "\n";
        }
    }
    return 0;
}