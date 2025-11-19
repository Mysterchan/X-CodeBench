#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct State {
    int f, g, a, b;
    bool operator<(State const &o) const {
        if (f != o.f) return f > o.f;
        return g > o.g;
    }
};
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    int S, T;
    cin >> N >> M >> S >> T;
    --S; --T;
    vector<vector<int>> adj(N);
    for(int i = 0; i < M; i++){
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // BFS from T
    vector<int> distT(N, -1), distS(N, -1);
    {
        deque<int> dq;
        distT[T] = 0;
        dq.push_back(T);
        while(!dq.empty()){
            int u = dq.front(); dq.pop_front();
            for(int v: adj[u]){
                if(distT[v] == -1){
                    distT[v] = distT[u] + 1;
                    dq.push_back(v);
                }
            }
        }
    }
    // BFS from S
    {
        deque<int> dq;
        distS[S] = 0;
        dq.push_back(S);
        while(!dq.empty()){
            int u = dq.front(); dq.pop_front();
            for(int v: adj[u]){
                if(distS[v] == -1){
                    distS[v] = distS[u] + 1;
                    dq.push_back(v);
                }
            }
        }
    }

    // A* on product graph
    // key: (a,b) -> g
    unordered_map<ll,int> best;
    best.reserve(1<<20);
    priority_queue<State> pq;
    int h0 = max(distT[S], distS[T]);
    pq.push({h0, 0, S, T});
    best[((ll)S<<32) | (unsigned int)T] = 0;

    while(!pq.empty()){
        State st = pq.top(); pq.pop();
        int f = st.f, g = st.g, a = st.a, b = st.b;
        ll key = ((ll)a<<32) | (unsigned int)b;
        auto it = best.find(key);
        if(it == best.end() || it->second < g) continue;
        if(a == T && b == S){
            cout << g << "\n";
            return 0;
        }
        // Move A
        for(int na: adj[a]){
            if(na == b) continue;
            ll nk = ((ll)na<<32) | (unsigned int)b;
            int ng = g + 1;
            auto it2 = best.find(nk);
            if(it2 == best.end() || ng < it2->second){
                best[nk] = ng;
                int h = max(distT[na], distS[b]);
                pq.push({ng + h, ng, na, b});
            }
        }
        // Move B
        for(int nb: adj[b]){
            if(a == nb) continue;
            ll nk = ((ll)a<<32) | (unsigned int)nb;
            int ng = g + 1;
            auto it2 = best.find(nk);
            if(it2 == best.end() || ng < it2->second){
                best[nk] = ng;
                int h = max(distT[a], distS[nb]);
                pq.push({ng + h, ng, a, nb});
            }
        }
    }

    cout << "-1\n";
    return 0;
}