#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<pair<int,int>> segs(m);
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        if (a > b) swap(a, b);
        segs[i] = {a, b};
    }

    int q;
    cin >> q;
    while (q--) {
        int c, d;
        cin >> c >> d;
        if (c > d) swap(c, d);
        int cnt = 0;
        for (auto [a,b] : segs) {
            if ((a < c && c < b && b < d) || (c < a && a < d && d < b)) {
                cnt++;
            }
        }
        cout << cnt << '\n';
    }
    return 0;
}
