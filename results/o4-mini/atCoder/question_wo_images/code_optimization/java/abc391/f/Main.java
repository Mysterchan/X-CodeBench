#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct Node {
    ll cost;
    int i, j, k;
};
struct Cmp {
    bool operator()(Node const &a, Node const &b) const {
        return a.cost < b.cost;
    }
};
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long K;
    cin >> N >> K;
    vector<ll> A(N), B(N), C(N);
    for(int i = 0; i < N; i++) cin >> A[i];
    for(int i = 0; i < N; i++) cin >> B[i];
    for(int i = 0; i < N; i++) cin >> C[i];

    sort(A.begin(), A.end());
    sort(B.begin(), B.end());
    sort(C.begin(), C.end());

    auto encode = [&](int i, int j, int k)->uint64_t {
        // use 18 bits per index, since N <= 2e5 < 2^18
        return (uint64_t(i) << 36) | (uint64_t(j) << 18) | uint64_t(k);
    };

    priority_queue<Node, vector<Node>, Cmp> pq;
    unordered_set<uint64_t> vis;
    vis.reserve(K * 3);
    int i0 = N-1, j0 = N-1, k0 = N-1;
    ll initCost = A[i0]*B[j0] + B[j0]*C[k0] + C[k0]*A[i0];
    pq.push({initCost, i0, j0, k0});
    vis.insert(encode(i0,j0,k0));

    ll answer = 0;
    for(long long cnt = 1; cnt <= K; cnt++){
        Node cur = pq.top(); pq.pop();
        answer = cur.cost;
        int i = cur.i, j = cur.j, k = cur.k;
        // neighbor (i-1, j, k)
        if(i > 0){
            uint64_t h = encode(i-1, j, k);
            if(vis.insert(h).second) {
                ll cost = A[i-1]*B[j] + B[j]*C[k] + C[k]*A[i-1];
                pq.push({cost, i-1, j, k});
            }
        }
        // neighbor (i, j-1, k)
        if(j > 0){
            uint64_t h = encode(i, j-1, k);
            if(vis.insert(h).second) {
                ll cost = A[i]*B[j-1] + B[j-1]*C[k] + C[k]*A[i];
                pq.push({cost, i, j-1, k});
            }
        }
        // neighbor (i, j, k-1)
        if(k > 0){
            uint64_t h = encode(i, j, k-1);
            if(vis.insert(h).second) {
                ll cost = A[i]*B[j] + B[j]*C[k-1] + C[k-1]*A[i];
                pq.push({cost, i, j, k-1});
            }
        }
    }

    cout << answer << "\n";
    return 0;
}