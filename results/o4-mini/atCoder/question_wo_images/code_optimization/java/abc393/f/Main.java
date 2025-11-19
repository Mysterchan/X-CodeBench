#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n;
    vector<int> bit;
    Fenwick(int _n): n(_n), bit(n, 0) {}
    // set position idx to max(current, val)
    void update(int idx, int val) {
        for (int i = idx; i < n; i = i | (i + 1)) {
            if (bit[i] < val) bit[i] = val;
        }
    }
    // query max on [0..idx]
    int query(int idx) {
        int res = 0;
        for (int i = idx; i >= 0; i = (i & (i + 1)) - 1) {
            if (bit[i] > res) res = bit[i];
        }
        return res;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, Q;
    cin >> N >> Q;
    vector<long long> A(N);
    for(int i = 0; i < N; i++){
        cin >> A[i];
    }
    vector<pair<int, long long>> inputQ(Q);
    for(int i = 0; i < Q; i++){
        int r;
        long long x;
        cin >> r >> x;
        r--; // to 0-based
        inputQ[i] = {r, x};
    }

    // coordinate compress A and all X values
    vector<long long> xs;
    xs.reserve(N + Q);
    for(auto &v : A) xs.push_back(v);
    for(int i = 0; i < Q; i++) xs.push_back(inputQ[i].second);
    sort(xs.begin(), xs.end());
    xs.erase(unique(xs.begin(), xs.end()), xs.end());

    int M = xs.size();
    // compress A
    vector<int> a(N);
    for(int i = 0; i < N; i++){
        a[i] = int(lower_bound(xs.begin(), xs.end(), A[i]) - xs.begin());
    }
    // prepare queries by prefix
    vector<vector<pair<int,int>>> queries_by_r(N);
    for(int i = 0; i < Q; i++){
        int r = inputQ[i].first;
        long long xval = inputQ[i].second;
        int xc = int(lower_bound(xs.begin(), xs.end(), xval) - xs.begin());
        queries_by_r[r].emplace_back(xc, i);
    }

    vector<int> ans(Q);
    Fenwick fw(M);

    for(int i = 0; i < N; i++){
        int ai = a[i];
        int best = 1;
        if (ai > 0) best = fw.query(ai - 1) + 1;
        // update dp for value ai
        fw.update(ai, best);
        // answer queries ending at i
        for(auto &pr : queries_by_r[i]){
            int xc = pr.first, qi = pr.second;
            ans[qi] = fw.query(xc);
        }
    }

    // output answers
    for(int i = 0; i < Q; i++){
        cout << ans[i] << "\n";
    }
    return 0;
}