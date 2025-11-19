#include <bits/stdc++.h>
using namespace std;
#define int long long

struct State {
    int val;
    int i, j, k;
    bool operator<(const State& other) const {
        return val < other.val; // for max-heap, we invert comparison in priority_queue
    }
};

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, K;
    cin >> n >> K;
    vector<int> A(n), B(n), C(n);
    for (int i = 0; i < n; i++) cin >> A[i];
    for (int i = 0; i < n; i++) cin >> B[i];
    for (int i = 0; i < n; i++) cin >> C[i];

    sort(A.rbegin(), A.rend());
    sort(B.rbegin(), B.rend());
    sort(C.rbegin(), C.rend());

    // We want to find the K-th largest value of:
    // val = A[i]*B[j] + B[j]*C[k] + C[k]*A[i]
    // = A[i]*B[j] + B[j]*C[k] + C[k]*A[i]

    // Use a max-heap to generate top K values efficiently.
    // State: indices (i,j,k) and value val.
    // Start from (0,0,0)
    // Push neighbors (i+1,j,k), (i,j+1,k), (i,j,k+1) if not visited.

    auto get_val = [&](int i, int j, int k) -> int {
        return A[i]*B[j] + B[j]*C[k] + C[k]*A[i];
    };

    priority_queue<State> pq;
    set<tuple<int,int,int>> visited;

    pq.push({get_val(0,0,0), 0, 0, 0});
    visited.emplace(0,0,0);

    int ans = 0;
    for (int cnt = 0; cnt < K; cnt++) {
        State cur = pq.top();
        pq.pop();
        ans = cur.val;

        int i = cur.i, j = cur.j, k = cur.k;

        if (i + 1 < n) {
            auto nxt = make_tuple(i+1, j, k);
            if (visited.find(nxt) == visited.end()) {
                visited.insert(nxt);
                pq.push({get_val(i+1, j, k), i+1, j, k});
            }
        }
        if (j + 1 < n) {
            auto nxt = make_tuple(i, j+1, k);
            if (visited.find(nxt) == visited.end()) {
                visited.insert(nxt);
                pq.push({get_val(i, j+1, k), i, j+1, k});
            }
        }
        if (k + 1 < n) {
            auto nxt = make_tuple(i, j, k+1);
            if (visited.find(nxt) == visited.end()) {
                visited.insert(nxt);
                pq.push({get_val(i, j, k+1), i, j, k+1});
            }
        }
    }

    cout << ans << "\n";
    return 0;
}