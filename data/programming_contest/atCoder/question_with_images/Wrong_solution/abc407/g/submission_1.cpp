#include<bits/stdc++.h>
using namespace std ; 
#define pii pair<ll,ll> 
#define pb push_back
#define ll long long 
#define ff first 
#define ss second 
#define vi vector<int> 


const int maxn = 2e3+5 ; 

const ll INF = 1e16 ;
template <class T = ll>
class MCMF {
public:
    struct Edge {
        Edge(int a, T b, T c) : to(a), cap(b), cost(c) {}
        int to;
        T cap, cost;
    };

    MCMF(int size) {
        n = size;
        edges.resize(n);
        pot.assign(n, 0);
        dist.resize(n);
        visit.assign(n, false);
    }

    std::pair<T, T> mcmf(int src, int sink) {
        std::pair<T, T> ans(0LL, 0LL);
        if(!SPFA(src, sink)) return ans;
        fixPot();
        while(SPFA(src, sink)) {
            auto flow = augment(src, sink);
            ans.first += flow.first;
            ans.second += flow.first * flow.second;
            fixPot();
        }
        return ans;
    }

    void add_edge(int from, int to, T cap, T cost) {
        edges[from].push_back(list.size());
        list.push_back(Edge(to, cap, cost));
        edges[to].push_back(list.size());
        list.push_back(Edge(from, 0, -cost));
    }
private:
    int n;
    std::vector<std::vector<int>> edges;
    std::vector<Edge> list;
    std::vector<int> from;
    std::vector<T> dist, pot;
    std::vector<bool> visit;

    

    std::pair<T, T> augment(int src, int sink) {
        std::pair<T, T> flow = {list[from[sink]].cap, 0};
        for(int v = sink; v != src; v = list[from[v]^1].to) {
            flow.first = std::min(flow.first, list[from[v]].cap);
            flow.second += list[from[v]].cost;
        }
        for(int v = sink; v != src; v = list[from[v]^1].to) {
            list[from[v]].cap -= flow.first;
            list[from[v]^1].cap += flow.first;
        }
        return flow;
    }

    std::queue<int> q;
    bool SPFA(int src, int sink) {
        T INF = std::numeric_limits<T>::max();
        dist.assign(n, INF);
        from.assign(n, -1);
        q.push(src);
        dist[src] = 0;
        while(!q.empty()) {
            int on = q.front();
            q.pop();
            visit[on] = false;
            for(auto e : edges[on]) {
                auto ed = list[e];
                if(ed.cap == 0) continue;
                T toDist = dist[on] + ed.cost + pot[on] - pot[ed.to];
                if(toDist < dist[ed.to]) {
                    dist[ed.to] = toDist;
                    from[ed.to] = e;
                    if(!visit[ed.to]) {
                        visit[ed.to] = true;
                        q.push(ed.to);
                    }
                }
            }
        }
        return dist[sink] < INF;
    }

    void fixPot() {
        T INF = std::numeric_limits<T>::max();
        for(int i = 0; i < n; i++) {
            if(dist[i] < INF) pot[i] += dist[i];
        }
    }
};

int n, m, ct ;
int mp[maxn][maxn] ;  
ll v[maxn][maxn] ;
int dx[] = {0, 0, 1, -1} ; 
int dy[] = {1, -1, 0, 0} ; 

bool valid(int i, int j){ return i > 0 && j > 0 && i <= n && j <= m ; }

void solve(){

    cin >> n >> m ; 
    
    ll ans = 0 ; 

    for(int i = 1 ; i <= n ; i++){
        for(int j = 1 ; j <= m ; j++) {
            cin >> v[i][j] ; 
            mp[i][j] = ++ct ; 
            ans += v[i][j] ; 
        }
    }

    MCMF dinic(ct+2) ; 

    int S = 0, T = ct + 1 ; 
    
    for(int i = 1 ; i <= n ; i++){
        for(int j = 1 ; j <= m ; j++){
            if((i+j)%2==0) dinic.add_edge(S, mp[i][j], 1, 0);
            else dinic.add_edge(mp[i][j], T, 1, 0);
        }
    }

    for(int i = 1 ; i <= n ; i++){
        for(int j = 1 ; j <= m ; j++){
            if((i+j)&1) continue ; 
            for(int k = 1 ; k <= n ; k++){
                for(int l = 1 ; l <= m ; l++){
                    if((k+l)%2 == 0) continue ; 
                    int u = mp[i][j], V = mp[k][l] ; 
                    ll add = 0 ; 
                    if(abs(i-k) + abs(j-l) == 1) add = max(0LL, v[k][l] + v[i][j]) ;
                    dinic.add_edge(u, V, 1, add) ; 
                }
            }
        }
    }

    auto uso = dinic.mcmf(0, ct+1) ;

    cout << ans - (uso.ss) << "\n" ; 

}

int32_t main(){

    ios_base::sync_with_stdio(false) ; cin.tie(NULL) ; 

    int t ; t = 1 ; 

    while(t--) solve(); 

}