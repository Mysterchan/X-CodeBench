#include <bits/stdc++.h>
using namespace std;

// Disjoint‐set (Union‐Find) with path‐compression and union by rank
struct DSU {
    vector<int> p, r;
    DSU(int n): p(n,-1), r(n,0) {
        for(int i=0;i<n;i++) p[i]=i;
    }
    int findp(int x) {
        return p[x]==x ? x : (p[x]=findp(p[x]));
    }
    void unite(int a,int b) {
        a = findp(a);
        b = findp(b);
        if(a==b) return;
        if(r[a]<r[b]) swap(a,b);
        p[b]=a;
        if(r[a]==r[b]) r[a]++;
    }
};

// Edge in the grid graph
struct Edge {
    int u,v;
    int w;
    bool operator<(Edge const& o) const {
        return w>o.w;  // sort descending by w
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H,W;
    cin>>H>>W;
    int N = H*W;
    vector<int> F(N);
    for(int r=0;r<H;r++){
        for(int c=0;c<W;c++){
            cin>>F[r*W+c];
        }
    }

    // Build all adjacency‐edges with weight = min(F[u],F[v])
    vector<Edge> edges;
    edges.reserve(2*N);
    auto addEdge = [&](int r1,int c1,int r2,int c2){
        int u = r1*W + c1;
        int v = r2*W + c2;
        edges.push_back({u,v, min(F[u],F[v])});
    };
    for(int r=0;r<H;r++){
        for(int c=0;c<W;c++){
            if(r+1<H) addEdge(r,c,r+1,c);
            if(c+1<W) addEdge(r,c,r,c+1);
        }
    }
    sort(edges.begin(), edges.end());

    int Q;
    cin>>Q;
    vector<int> A(Q), B(Q), Y(Q), C(Q), D(Q), Z(Q), lim(Q), diff(Q);
    for(int i=0;i<Q;i++){
        cin>>A[i]>>B[i]>>Y[i]>>C[i]>>D[i]>>Z[i];
        --A[i]; --B[i];
        --C[i]; --D[i];
        int s = A[i]*W + B[i];
        int t = C[i]*W + D[i];
        A[i] = s;
        C[i] = t;
        lim[i] = min(Y[i], Z[i]);
        diff[i] = abs(Y[i] - Z[i]);
    }

    // Parallel binary‐search on M for each query in [0..lim[i]]
    vector<int> low(Q,0), high(Q);
    for(int i=0;i<Q;i++) high[i] = lim[i];

    vector<pair<int,int>> queries; 
    queries.reserve(Q);

    // Repeat until all low==high
    bool changed = true;
    while(changed){
        changed = false;
        queries.clear();

        // Gather only those queries that still have low<high
        for(int i=0;i<Q;i++){
            if(low[i]<high[i]){
                int m = (low[i] + high[i] + 1)/2;
                queries.emplace_back(m,i);
                changed = true;
            }
        }
        if(!changed) break;

        // Sort queries by descending m
        sort(queries.begin(), queries.end(),
             [&](auto &a, auto &b){ return a.first>b.first; });

        // Reset DSU, sweep edges
        DSU dsu(N);
        int epos=0;

        // Process each query in descending order of mid
        for(auto &qr: queries){
            int mid = qr.first;
            int qi  = qr.second;
            // add all edges with weight >= mid
            while(epos < (int)edges.size() && edges[epos].w >= mid){
                dsu.unite(edges[epos].u, edges[epos].v);
                ++epos;
            }
            // check connectivity
            if(dsu.findp(A[qi]) == dsu.findp(C[qi])){
                low[qi] = mid;    // possible
            } else {
                high[qi] = mid-1; // too large
            }
        }
    }

    // Output final answers
    // If M >= lim => cost = diff
    // else cost = diff + 2*(lim - M)
    for(int i=0;i<Q;i++){
        int M = low[i];
        if(M >= lim[i]){
            cout<< diff[i] << "\n";
        } else {
            cout<< (diff[i] + 2*(lim[i] - M)) << "\n";
        }
    }
    return 0;
}