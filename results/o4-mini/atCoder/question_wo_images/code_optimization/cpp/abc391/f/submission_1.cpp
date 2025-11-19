#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct Node {
    ll val;
    int i, j, k;
};

struct Cmp {
    bool operator()(const Node &a, const Node &b) const {
        return a.val < b.val; // max-heap
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    ll K;
    cin >> n >> K;

    vector<ll> A(n+1), B(n+1), C(n+1);
    for (int i = 1; i <= n; i++) {
        cin >> A[i];
    }
    for (int i = 1; i <= n; i++) {
        cin >> B[i];
    }
    for (int i = 1; i <= n; i++) {
        cin >> C[i];
    }
    sort(A.begin()+1, A.end(), greater<ll>());
    sort(B.begin()+1, B.end(), greater<ll>());
    sort(C.begin()+1, C.end(), greater<ll>());

    priority_queue<Node, vector<Node>, Cmp> pq;
    // use 20 bits per index: i<<40 | j<<20 | k
    unordered_set<uint64_t> seen;
    seen.reserve(K * 3 + 10);

    auto push = [&](int i, int j, int k) {
        if (i > n || j > n || k > n) return;
        uint64_t key = ( (uint64_t)i << 40 ) | ( (uint64_t)j << 20 ) | (uint64_t)k;
        if (seen.insert(key).second) {
            ll v = A[i]*B[j] + B[j]*C[k] + C[k]*A[i];
            pq.push({v, i, j, k});
        }
    };

    // initial
    push(1, 1, 1);

    ll answer = 0;
    for (ll cnt = 0; cnt < K; cnt++) {
        Node cur = pq.top();
        pq.pop();
        answer = cur.val;
        // generate neighbors
        push(cur.i + 1, cur.j, cur.k);
        push(cur.i, cur.j + 1, cur.k);
        push(cur.i, cur.j, cur.k + 1);
    }

    cout << answer << "\n";
    return 0;
}