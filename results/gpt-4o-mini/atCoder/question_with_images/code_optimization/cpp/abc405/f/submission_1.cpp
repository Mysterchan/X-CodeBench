#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<pair<int, int>> segs(m);
    unordered_map<int, vector<int>> posMap;

    // Read the segments and populate the position map
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        if (a > b) swap(a, b);
        segs[i] = {a, b};
        posMap[a].push_back(i);
        posMap[b].push_back(i);
    }

    int q;
    cin >> q;
    while (q--) {
        int c, d;
        cin >> c >> d;
        if (c > d) swap(c, d);
        
        // Find all segments connected to points C and D
        unordered_set<int> intersectingSegments;
        if (posMap.count(c)) {
            for (int idx : posMap[c]) {
                intersectingSegments.insert(idx);
            }
        }
        if (posMap.count(d)) {
            for (int idx : posMap[d]) {
                intersectingSegments.insert(idx);
            }
        }

        // Count valid intersections
        int cnt = 0;
        for (int idx : intersectingSegments) {
            auto [a, b] = segs[idx];
            if ((a < c && c < b && b < d) || (c < a && a < d && d < b)) {
                cnt++;
            }
        }
        cout << cnt << '\n';
    }
    return 0;
}