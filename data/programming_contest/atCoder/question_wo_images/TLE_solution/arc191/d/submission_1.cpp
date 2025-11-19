#include <bits/stdc++.h>
using namespace std;

static const int INF = 1e9;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M;
    if(!(cin >> N >> M)) return 0;
        int S, T; cin >> S >> T;
    vector<vector<int>> g(N+1);
    for(int i=0;i<M;i++){
        int u,v; cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }


    auto bfs = [&](int src){
        vector<int> d(N+1, INF);
        deque<int> dq;
        d[src] = 0;
        dq.push_back(src);
        while(!dq.empty()){
            int v = dq.front(); dq.pop_front();
            for(int to : g[v]){
                if(d[to] == INF){
                    d[to] = d[v] + 1;
                    dq.push_back(to);
                }
            }
        }
        return d;
    };

    vector<int> dS = bfs(S);
    vector<int> dT = bfs(T);
    if(dS[T] == INF){
        cout << -1 << '\n';
        return 0;
    }
    const long long baseLower = 2LL * dS[T];

    struct PairHash {
        size_t operator()(const uint64_t &x) const noexcept { return std::hash<uint64_t>()(x); }
    };
    auto keyOf = [&](int a, int b)->uint64_t{
        return (uint64_t)a << 32 | (uint64_t)b;
    };

    unordered_map<uint64_t,int,PairHash> dist;
    dist.reserve(1<<20);
    dist.max_load_factor(0.7f);

    array<deque<pair<int,int>>,3> bucket;
    auto push_state = [&](int a, int b, int nd, int cur_mod){
        uint64_t k = keyOf(a,b);
        auto it = dist.find(k);
        if(it==dist.end() || nd < it->second){
            dist[k] = nd;
            bucket[nd % 3].emplace_back(a,b);
        }
    };

    push_state(S, T, 0, 0);
    int curd = 0;
    int bi   = 0;
    auto pull_next = [&]()->optional<pair<int,int>>{
        int cnt = 0;
        while(bucket[bi].empty()){
            bi = (bi + 1) % 3;
            ++curd;
            if(++cnt > 3){
                return nullopt;
            }
        }
        auto p = bucket[bi].front();
        bucket[bi].pop_front();
        return p;
    };

    while(true){
        auto opt = pull_next();
        if(!opt.has_value()){
            cout << -1 << '\n';
            return 0;
        }
        int a = opt->first, b = opt->second;
        auto it = dist.find(keyOf(a,b));
        if(it==dist.end() || it->second != curd) continue;

        if(a==T && b==S){
            cout << (baseLower + curd) << '\n';
            return 0;
        }

        for(int an : g[a]){
            if(an == b) continue;
            int w = 1 + (dT[an] - dT[a]); // {0,1,2}
            int nd = curd + w;
            push_state(an, b, nd, bi);
        }
        for(int bn : g[b]){
            if(bn == a) continue;
            int w = 1 + (dS[bn] - dS[b]); // {0,1,2}
            int nd = curd + w;
            push_state(a, bn, nd, bi);
        }
    }
    return 0;
}
