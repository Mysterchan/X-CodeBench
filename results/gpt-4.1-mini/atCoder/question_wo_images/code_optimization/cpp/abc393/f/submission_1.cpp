#include <bits/stdc++.h>
using namespace std;

struct SegmentTree {
    int size;
    vector<int> tree;

    void init(int n) {
        size = 1;
        while (size < n) size <<= 1;
        tree.assign(2 * size, 0);
    }

    void update(int pos, int val) {
        pos += size;
        tree[pos] = max(tree[pos], val);
        for (pos /= 2; pos > 0; pos /= 2)
            tree[pos] = max(tree[2 * pos], tree[2 * pos + 1]);
    }

    int query(int l, int r) { // max in [l, r)
        int res = 0;
        l += size; r += size;
        while (l < r) {
            if (l & 1) res = max(res, tree[l++]);
            if (r & 1) res = max(res, tree[--r]);
            l >>= 1; r >>= 1;
        }
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];

    // Coordinate compress A
    vector<int> sortedA = A;
    sort(sortedA.begin(), sortedA.end());
    sortedA.erase(unique(sortedA.begin(), sortedA.end()), sortedA.end());

    auto getCompressed = [&](int x) {
        return (int)(lower_bound(sortedA.begin(), sortedA.end(), x) - sortedA.begin());
    };

    // Precompute dp[i] = length of LIS ending at i in A
    SegmentTree seg;
    seg.init((int)sortedA.size());
    vector<int> dp(N);
    for (int i = 0; i < N; i++) {
        int c = getCompressed(A[i]);
        int best = seg.query(0, c);
        dp[i] = best + 1;
        seg.update(c, dp[i]);
    }

    // Build segment tree over dp for range max queries
    struct SegMax {
        int size;
        vector<int> tree;
        void init(int n) {
            size = 1;
            while (size < n) size <<= 1;
            tree.assign(2 * size, 0);
        }
        void build(const vector<int>& v) {
            int n = (int)v.size();
            for (int i = 0; i < n; i++) tree[size + i] = v[i];
            for (int i = size - 1; i > 0; i--)
                tree[i] = max(tree[2 * i], tree[2 * i + 1]);
        }
        int query(int l, int r) { // max in [l, r)
            int res = 0;
            l += size; r += size;
            while (l < r) {
                if (l & 1) res = max(res, tree[l++]);
                if (r & 1) res = max(res, tree[--r]);
                l >>= 1; r >>= 1;
            }
            return res;
        }
    } segdp;

    segdp.init(N);
    segdp.build(dp);

    // For queries, we need to find max dp[i] for i < R and A[i] <= X
    // We'll process queries offline sorted by X
    struct Query {
        int idx, R, X;
    };
    vector<Query> queries(Q);
    for (int i = 0; i < Q; i++) {
        int R, X; cin >> R >> X;
        queries[i] = {i, R, X};
    }
    sort(queries.begin(), queries.end(), [](const Query& a, const Query& b) {
        return a.X < b.X;
    });

    // Sort elements by value
    vector<pair<int,int>> vals(N);
    for (int i = 0; i < N; i++) vals[i] = {A[i], i};
    sort(vals.begin(), vals.end());

    vector<int> ans(Q);
    int pos = 0;
    // We'll use a Fenwick tree (BIT) to maintain max dp[i] for indices i
    // but queries are on prefix [0, R-1], so Fenwick tree on indices
    // Fenwick tree for max:
    struct Fenw {
        int n;
        vector<int> bit;
        void init(int sz) {
            n = sz;
            bit.assign(n + 1, 0);
        }
        void update(int i, int v) {
            for (++i; i <= n; i += i & -i)
                bit[i] = max(bit[i], v);
        }
        int query(int i) {
            int res = 0;
            for (++i; i > 0; i -= i & -i)
                res = max(res, bit[i]);
            return res;
        }
    } fenw;

    fenw.init(N);

    for (auto& q : queries) {
        // Insert all elements with A[i] <= q.X into fenw
        while (pos < N && vals[pos].first <= q.X) {
            int idx = vals[pos].second;
            fenw.update(idx, dp[idx]);
            pos++;
        }
        // Query fenw for max dp[i] with i < R
        ans[q.idx] = fenw.query(q.R - 1);
    }

    for (int i = 0; i < Q; i++) cout << ans[i] << "\n";

    return 0;
}