#include <bits/stdc++.h>
using namespace std;

#define ar array

const int mxN = 4e5;
int n, q;

struct DSU {
    int p[mxN], r[mxN];
    vector<ar<int, 3>> ops;
    vector<int> st;

    void init() {
        iota(p, p + n, 0);
        fill(r, r + n, 0);
        ops.clear();
        st.clear();
    }

    int find(int x) {
        while (x != p[x]) x = p[x];
        return x;
    }

    bool join(int x, int y) {
        x = find(x);
        y = find(y);
        if (x == y) return false;
        if (r[x] < r[y]) swap(x, y);
        ops.push_back({x, y, r[x] == r[y]});
        p[y] = x;
        if (r[x] == r[y]) r[x]++;
        return true;
    }

    void record() {
        st.push_back((int)ops.size());
    }

    void rollback() {
        int s = st.back();
        st.pop_back();
        while ((int)ops.size() > s) {
            auto a = ops.back();
            ops.pop_back();
            p[a[1]] = a[1];
            if (a[2]) r[a[0]]--;
        }
    }
};

DSU da1, da2, db;

void solve(const vector<ar<int, 5>> &qs, int l2 = 0, int r2 = -1, int ans = 0) {
    if (r2 == -1) r2 = q - 1;
    da1.record();
    da2.record();
    db.record();

    // Process edges fully active in [l2, r2]
    for (auto &a : qs) {
        if (a[1] <= l2 && r2 <= a[2]) {
            int c = a[0], u = a[3], v = a[4];
            if (c == 1) { // B graph
                if (db.join(u, v)) {
                    if (da2.join(u, v))
                        ans++;
                }
            } else { // A graph
                if (da1.join(u, v)) {
                    if (!da2.join(u, v))
                        ans--;
                }
            }
        }
    }

    if (l2 == r2) {
        cout << ans << "\n";
        da1.rollback();
        da2.rollback();
        db.rollback();
        return;
    }

    int m2 = (l2 + r2) / 2;
    vector<ar<int, 5>> ql, qr;
    for (auto &a : qs) {
        if (a[1] <= m2)
            ql.push_back(a);
        if (m2 < a[2])
            qr.push_back(a);
    }

    solve(ql, l2, m2, ans);
    solve(qr, m2 + 1, r2, ans);

    da1.rollback();
    da2.rollback();
    db.rollback();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> q;
    da1.init();
    da2.init();
    db.init();

    // Map to store edge insertion time for each graph
    // Using unordered_map with custom hash to speed up
    struct pair_hash {
        size_t operator()(const pair<int,int>& x) const {
            return (size_t)x.first * 400000 + x.second;
        }
    };
    unordered_map<pair<int,int>, int, pair_hash> s[2];

    vector<ar<int, 5>> qs;

    for (int i = 0; i < q; i++) {
        char c;
        int x, y;
        cin >> c >> x >> y;
        --x; --y;
        if (x > y) swap(x, y);
        int ci = c - 'A';

        auto &mp = s[ci];
        pair<int,int> e = {x, y};
        auto it = mp.find(e);
        if (it == mp.end()) {
            mp[e] = i;
        } else {
            qs.push_back({ci, it->second, i - 1, x, y});
            mp.erase(it);
        }
    }

    for (int c = 0; c < 2; c++) {
        for (auto &a : s[c]) {
            qs.push_back({c, a.second, q - 1, a.first.first, a.first.second});
        }
    }

    solve(qs);

    return 0;
}