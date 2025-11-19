#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct Query {
    int R, idx;
    ll X;
};
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;
    vector<ll> A(N+1);
    for (int i = 1; i <= N; i++) {
        cin >> A[i];
    }
    vector<Query> queries(Q);
    for (int i = 0; i < Q; i++) {
        cin >> queries[i].R >> queries[i].X;
        queries[i].idx = i;
    }
    sort(queries.begin(), queries.end(), [](const Query &a, const Query &b){
        return a.R < b.R;
    });

    vector<int> ans(Q);
    vector<ll> d;
    d.reserve(N);
    int qi = 0;
    for (int i = 1; i <= N; i++) {
        ll v = A[i];
        auto it = lower_bound(d.begin(), d.end(), v);
        if (it == d.end()) d.push_back(v);
        else *it = v;
        // answer all queries with R == i
        while (qi < Q && queries[qi].R == i) {
            ll X = queries[qi].X;
            // find max k such that d[k-1] <= X
            int k = int(upper_bound(d.begin(), d.end(), X) - d.begin());
            ans[queries[qi].idx] = k;
            qi++;
        }
    }
    // For any queries with R > N (shouldn't happen by constraints), they'd have been skipped; but constraints guarantee R<=N.

    // Output answers in original order
    for (int i = 0; i < Q; i++) {
        cout << ans[i] << "\n";
    }
    return 0;
}