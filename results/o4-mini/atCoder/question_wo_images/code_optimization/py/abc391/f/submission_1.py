#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ull = unsigned long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    ll K;
    cin >> N >> K;
    vector<ll> A(N), B(N), C(N);
    for(int i = 0; i < N; i++) cin >> A[i];
    for(int i = 0; i < N; i++) cin >> B[i];
    for(int i = 0; i < N; i++) cin >> C[i];
    sort(A.begin(), A.end(), greater<ll>());
    sort(B.begin(), B.end(), greater<ll>());
    sort(C.begin(), C.end(), greater<ll>());

    // max-heap of (value, i, j, k)
    struct Node {
        ll val;
        int i, j, k;
    };
    struct Cmp {
        bool operator()(Node const &a, Node const &b) const {
            return a.val < b.val;
        }
    };
    priority_queue<Node, vector<Node>, Cmp> pq;

    // pack i,j,k into one 64-bit key: 20 bits per index
    auto pack = [&](int i, int j, int k)->ull {
        return ( (ull)i << 40 ) | ( (ull)j << 20 ) | (ull)k;
    };

    // visited set
    unordered_set<ull> vis;
    vis.reserve(K * 3 + 10);

    // initial
    ll initVal = A[0]*B[0] + B[0]*C[0] + C[0]*A[0];
    pq.push({initVal, 0, 0, 0});
    vis.insert(pack(0,0,0));

    ll answer = 0;
    for(ll cnt = 1; cnt <= K; ++cnt){
        Node cur = pq.top(); pq.pop();
        if(cnt == K){
            answer = cur.val;
            break;
        }
        int i = cur.i, j = cur.j, k = cur.k;
        // neighbor i+1, j, k
        if(i + 1 < N){
            ull key = pack(i+1, j, k);
            if(vis.insert(key).second){
                ll v = A[i+1]*B[j] + B[j]*C[k] + C[k]*A[i+1];
                pq.push({v, i+1, j, k});
            }
        }
        // neighbor i, j+1, k
        if(j + 1 < N){
            ull key = pack(i, j+1, k);
            if(vis.insert(key).second){
                ll v = A[i]*B[j+1] + B[j+1]*C[k] + C[k]*A[i];
                pq.push({v, i, j+1, k});
            }
        }
        // neighbor i, j, k+1
        if(k + 1 < N){
            ull key = pack(i, j, k+1);
            if(vis.insert(key).second){
                ll v = A[i]*B[j] + B[j]*C[k+1] + C[k+1]*A[i];
                pq.push({v, i, j, k+1});
            }
        }
    }

    cout << answer << "\n";
    return 0;
}