#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    vector<pair<int,int>> segs(M);
    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        if (a > b) swap(a, b);
        segs[i] = {a, b};
    }

    // Sort segments by their start point (A_i)
    sort(segs.begin(), segs.end());

    // Extract arrays for binary search
    vector<int> A(M), B(M);
    for (int i = 0; i < M; i++) {
        A[i] = segs[i].first;
        B[i] = segs[i].second;
    }

    int Q; cin >> Q;
    while (Q--) {
        int c, d;
        cin >> c >> d;
        if (c > d) swap(c, d);

        // We want to count segments (a,b) with a < c < b < d OR c < a < d < b
        // Since segments are sorted by a, we can binary search to find candidates.

        // Count segments with a < c and b < d and c < b
        // Condition (a < c < b < d) means:
        // a < c, b < d, and b > c
        // So b in (c, d)

        // Find segments with a < c
        int idx = lower_bound(A.begin(), A.end(), c) - A.begin();

        // Among these segments [0, idx-1], count how many have b in (c, d)
        // b > c and b < d
        int cnt1 = 0;
        if (idx > 0) {
            // B[0..idx-1] is not sorted, so we sort B once for all segments
            // But B is not sorted by default, so we need a data structure for fast queries.

            // To optimize, we pre-sort B by A, but B is not sorted.
            // So we build a Fenwick tree or segment tree on B after sorting segments by A.

            // Since M <= 2e5, we can build a Fenwick tree on B values.

            // We'll do this outside the query loop.
        }

        // Similarly, condition (c < a < d < b):
        // a in (c, d), b > d

        // We'll handle both conditions using Fenwicks.

        // So we need to preprocess:

        // Let's implement Fenwicks for B values.

        // Since points are up to 2N (max 2*10^6), we can compress B values.

        // Let's do all preprocessing before queries.

        // So break here and implement preprocessing.

        // (We will move the query loop after preprocessing)
    }

    // --- Preprocessing ---

    // Compress B values
    vector<int> allB(M);
    for (int i = 0; i < M; i++) allB[i] = B[i];
    sort(allB.begin(), allB.end());
    allB.erase(unique(allB.begin(), allB.end()), allB.end());

    auto getBidx = [&](int x) {
        return int(lower_bound(allB.begin(), allB.end(), x) - allB.begin()) + 1;
    };

    // Fenwick tree for counting B values
    struct Fenw {
        int n;
        vector<int> bit;
        Fenw(int n): n(n), bit(n+1,0) {}
        void add(int i, int v) {
            while (i <= n) {
                bit[i] += v;
                i += i & (-i);
            }
        }
        int sum(int i) {
            int s = 0;
            while (i > 0) {
                s += bit[i];
                i -= i & (-i);
            }
            return s;
        }
        int range_sum(int l, int r) {
            if (r < l) return 0;
            return sum(r) - sum(l-1);
        }
    };

    Fenw fenw(M);

    // We'll process queries offline:
    // For each query, we need to count:
    // 1) segments with a < c and b in (c, d)
    // 2) segments with a in (c, d) and b > d

    // We'll process queries offline sorted by c and d.

    // Let's read queries first:
    int Q; cin >> Q;
    struct Query {
        int c, d, idx;
    };
    vector<Query> queries(Q);
    for (int i = 0; i < Q; i++) {
        int c, d; cin >> c >> d;
        if (c > d) swap(c, d);
        queries[i] = {c, d, i};
    }

    // Sort queries by c ascending
    sort(queries.begin(), queries.end(), [](auto &x, auto &y) {
        return x.c < y.c;
    });

    // We'll answer part 1: count segments with a < c and b in (c, d)
    // For this, we iterate segments in ascending order of a,
    // and for each query with c, we add segments with a < c to Fenw,
    // then query Fenw for b in (c, d).

    // Prepare answers array
    vector<int> ans(Q, 0);

    // Sort segments by a ascending (already sorted)
    // We'll iterate segments with pointer seg_ptr

    int seg_ptr = 0;
    // Fenw on B compressed indices
    Fenw fenw1((int)allB.size());

    for (auto &q : queries) {
        // Add all segments with a < c to fenw1
        while (seg_ptr < M && A[seg_ptr] < q.c) {
            int bidx = getBidx(B[seg_ptr]);
            fenw1.add(bidx, 1);
            seg_ptr++;
        }
        // Query fenw1 for b in (c, d)
        // b in (c, d) means b > c and b < d
        // So b in (c, d) => b > c and b < d
        // We find compressed indices for c and d
        int left = int(lower_bound(allB.begin(), allB.end(), q.c+1) - allB.begin()) + 1;
        int right = int(lower_bound(allB.begin(), allB.end(), q.d) - allB.begin());
        if (right < left) ans[q.idx] += 0;
        else ans[q.idx] += fenw1.range_sum(left, right);
    }

    // Now answer part 2: count segments with a in (c, d) and b > d
    // For this, we sort queries by d ascending
    // and segments by a ascending (already sorted)
    // We'll iterate segments with pointer seg_ptr2 and add segments with a <= d to fenw2 on b
    // For each query, count how many segments have a <= d and b > d
    // Then subtract how many have a <= c (or a < c+1) and b > d to get segments with a in (c, d]

    // So we need fenw2 to count segments with b > d
    // We'll store b in fenw2 and query sum of b > d

    // For fenw2, we add segments in order of a ascending
    // For queries, we process in order of d ascending

    // Prepare queries sorted by d ascending
    vector<Query> queries_by_d = queries;
    sort(queries_by_d.begin(), queries_by_d.end(), [](auto &x, auto &y) {
        return x.d < y.d;
    });

    Fenw fenw2((int)allB.size());
    int seg_ptr2 = 0;

    // For each query, we want:
    // count of segments with a <= d and b > d
    // minus count of segments with a <= c and b > d

    // We'll precompute prefix sums for a <= x

    // We'll process queries in ascending d order
    // For each query, we add segments with a <= d to fenw2
    // Then query fenw2 for b > d

    // To get count for a <= c, we do the same with c as d

    // So we process all queries and also queries with c as d

    // We'll create events for queries and for c values

    struct Event {
        int x; // a value (d or c)
        int type; // 0 = add segment, 1 = query d, 2 = query c
        int b; // b value for segment or d value for query
        int idx; // query index for queries
    };

    vector<Event> events;

    // Add segment events
    for (int i = 0; i < M; i++) {
        events.push_back({A[i], 0, B[i], -1});
    }

    // Add query events for d
    for (int i = 0; i < Q; i++) {
        events.push_back({queries[i].d, 1, queries[i].d, i});
    }

    // Add query events for c
    for (int i = 0; i < Q; i++) {
        events.push_back({queries[i].c, 2, queries[i].d, i});
    }

    // Sort events by x ascending, type ascending (to process adds before queries)
    sort(events.begin(), events.end(), [](auto &a, auto &b) {
        if (a.x != b.x) return a.x < b.x;
        return a.type < b.type;
    });

    vector<int> res_d(Q, 0), res_c(Q, 0);

    for (auto &e : events) {
        if (e.type == 0) {
            // add segment
            int bidx = getBidx(e.b);
            fenw2.add(bidx, 1);
        } else {
            // query
            // count segments with b > e.b
            // b > e.b means bidx > getBidx(e.b)
            int bidx = int(lower_bound(allB.begin(), allB.end(), e.b + 1) - allB.begin()) + 1;
            int total = fenw2.sum((int)allB.size());
            int less_equal = fenw2.sum(bidx - 1);
            int cnt = total - less_equal;
            if (e.type == 1) res_d[e.idx] = cnt;
            else res_c[e.idx] = cnt;
        }
    }

    // Now add res_d - res_c to ans
    for (int i = 0; i < Q; i++) {
        ans[i] += res_d[i] - res_c[i];
    }

    // Output answers
    for (int i = 0; i < Q; i++) {
        cout << ans[i] << '\n';
    }

    return 0;
}