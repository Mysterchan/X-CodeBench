#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while(T--){
        int N; cin >> N;
        vector<int> L(N+1), R(N+1);
        for(int i=1; i<=N; i++) cin >> L[i] >> R[i];

        // Build adjacency list for the containment DAG:
        // i -> j if interval j is strictly inside interval i
        vector<vector<int>> adj(N+1);
        vector<int> indeg(N+1,0);

        // Since all L_i and R_i are distinct, we can sort intervals by L ascending
        // and then by R descending to optimize the containment check.
        // But N=500 is small enough for O(N^2) with pruning.

        // To speed up, we can sort intervals by L ascending, and for each i,
        // only check j with L[j] > L[i] and R[j] < R[i].
        // We'll store indices sorted by L ascending.
        vector<int> order(N);
        iota(order.begin(), order.end(), 1);
        sort(order.begin(), order.end(), [&](int a,int b){
            return L[a]<L[b];
        });

        // For each i in order, check j with L[j]>L[i]
        // Since order is sorted by L ascending, for i-th in order,
        // j > i in order have L[j]>=L[i].
        // We'll do a nested loop but break early when L[j] > L[i] no longer holds.

        for(int i=0; i<N; i++){
            int u = order[i];
            for(int j=i+1; j<N; j++){
                int v = order[j];
                if(L[v] > L[u] && R[u] > R[v]){
                    adj[u].push_back(v);
                    indeg[v]++;
                }
            }
        }

        // Add a dummy node 0 with edges to all nodes with indeg=0
        // to perform a lex smallest topological sort starting from 0.
        // We'll do a topological sort with a min-heap to get lex smallest order.

        // Create a min-heap of nodes with indeg=0
        priority_queue<int, vector<int>, greater<int>> pq;
        for(int i=1; i<=N; i++){
            if(indeg[i]==0) pq.push(i);
        }

        vector<int> P(N+1,0);
        int seat = 1;
        while(!pq.empty()){
            int u = pq.top(); pq.pop();
            P[u] = seat++;
            for(int v : adj[u]){
                indeg[v]--;
                if(indeg[v]==0) pq.push(v);
            }
        }

        for(int i=1; i<=N; i++){
            cout << P[i] << (i==N?'\n':' ');
        }
    }
    return 0;
}