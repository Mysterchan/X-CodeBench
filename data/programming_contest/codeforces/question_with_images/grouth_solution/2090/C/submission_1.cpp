#ifdef ONLINE_JUDGE
#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif

#include <bits/stdc++.h>
using namespace std;

#define fo(i, l, r) for (int i = l; i <= r; ++i)
#define fi first
#define se second

const int N = 5e4;
int n, t[N + 2];

int dis(const pair<int, int> &x) {
    if (x.fi % 3 == 2 && x.se % 3 == 2) return x.fi + x.se + 2;
    return x.fi + x.se;
}

struct cmp {
    bool operator()(const pair<int, int> &x, const pair<int, int> &y) const {
        if (dis(x) != dis(y)) return dis(x) < dis(y);
        return x < y;
    }
};

set<pair<int, int>, cmp> f, g;
set<pair<int, int>> st;

void add(int x, int y) {
    if (st.count({x, y})) return;
    st.emplace(x, y);
    fo(i, 0, 1) fo(j, 0, 1) f.emplace(x + i, y + j);
    g.emplace(x, y);
}

void expand(int x, int y) {
    add(x + 3, y);
    add(x, y + 3);
}

void occupy(int x, int y) {
    if (x % 3 == 1 && y % 3 == 1) {
        expand(x, y);
        g.erase({x, y});
    }
    f.erase({x, y});
}

void __main__() {
    cin >> n;
    fo(i, 1, n) cin >> t[i];
    add(1, 1);
    fo(i, 1, n) {
        if (t[i]) {
            auto d = *f.begin();
            cout << d.fi << " " << d.se << "\n";
            occupy(d.fi, d.se);
        } else {
            auto d = *g.begin();
            cout << d.fi << " " << d.se << "\n";
            occupy(d.fi, d.se);
        }
    }
    f.clear();
    g.clear();
    st.clear();
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while (T--) __main__();
    return 0;
}