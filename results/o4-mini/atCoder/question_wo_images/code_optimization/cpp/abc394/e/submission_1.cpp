#include <bits/stdc++.h>
using namespace std;
using pii = pair<int,int>;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    cin >> N;
    vector<string> A(N);
    for(int i = 0; i < N; i++) cin >> A[i];
    const int INF = 1000000000;
    int N2 = N * N;
    int T = N2;
    // Build out_all, out by letter, and in by letter
    vector<vector<int>> out_all(N);
    static vector<int> out_c[100][26], in_c[100][26];
    for(int u = 0; u < N; u++){
        for(int v = 0; v < N; v++){
            char ch = A[u][v];
            if(ch != '-'){
                int c = ch - 'a';
                out_c[u][c].push_back(v);
                in_c[v][c].push_back(u);
                out_all[u].push_back(v);
            }
        }
    }
    // Dijkstra on reversed graph from T
    int V = N2 + 1;
    vector<int> dist(V, INF);
    dist[T] = 0;
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    pq.push({0, T});
    while(!pq.empty()){
        auto [d, u] = pq.top();
        pq.pop();
        if(d != dist[u]) continue;
        if(u == T){
            // reversed edges from T: to (u,u) weight 0, to (u,v) weight 1
            for(int uu = 0; uu < N; uu++){
                int idd = uu * N + uu;
                if(dist[idd] > d){
                    dist[idd] = d;
                    pq.push({d, idd});
                }
            }
            for(int uu = 0; uu < N; uu++){
                int base = uu * N;
                for(int v : out_all[uu]){
                    int idd = base + v;
                    if(dist[idd] > d + 1){
                        dist[idd] = d + 1;
                        pq.push({d + 1, idd});
                    }
                }
            }
        } else {
            int u2 = u / N;
            int v2 = u % N;
            // reversed transitions: for each c, for each u1 in in_c[u2][c], v1 in out_c[v2][c]
            for(int c = 0; c < 26; c++){
                auto &inu = in_c[u2][c];
                auto &outv = out_c[v2][c];
                if(inu.empty() || outv.empty()) continue;
                for(int u1 : inu){
                    int base = u1 * N;
                    for(int v1 : outv){
                        int id2 = base + v1;
                        int nd = d + 2;
                        if(dist[id2] > nd){
                            dist[id2] = nd;
                            pq.push({nd, id2});
                        }
                    }
                }
            }
        }
    }
    // Output answers
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            int d = dist[i * N + j];
            if(d >= INF) d = -1;
            cout << d << (j+1<N ? ' ' : '\n');
        }
    }
    return 0;
}