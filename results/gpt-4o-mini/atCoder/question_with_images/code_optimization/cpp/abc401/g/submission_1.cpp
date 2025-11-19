#include <bits/stdc++.h>
using namespace std;

using ld = long double;
using pd = pair<ld, ld>;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int N;
    cin >> N;
    vector<pd> people(N), butts(N);
    
    for (auto& [x, y] : people) cin >> x >> y;
    for (auto& [x, y] : butts) cin >> x >> y;

    ld lo = 0, hi = 1e18, best = 1e18;

    while (hi - lo > 1e-7) {
        ld mid = (lo + hi) / 2;
        
        vector<int> mt(N, -1);
        vector<bool> vis(N);
        bool possible = true;

        for (int i = 0; i < N; ++i) {
            fill(vis.begin(), vis.end(), false);
            function<bool(int)> try_kuhn = [&](int v) {
                if (vis[v]) return false;
                vis[v] = true;
                for (int j = 0; j < N; ++j) {
                    ld d = hypot(butts[j].first - people[v].first, butts[j].second - people[v].second);
                    if (d <= mid && (mt[j] == -1 || try_kuhn(mt[j]))) {
                        mt[j] = v;
                        return true;
                    }
                }
                return false;
            };

            possible = false;
            for (int j = 0; j < N; ++j) {
                if (hypot(butts[j].first - people[i].first, butts[j].second - people[i].second) <= mid && try_kuhn(j)) {
                    possible = true;
                    break;
                }
            }
            if (!possible) break;
        }

        if (possible) {
            best = mid;
            hi = mid;
        } else {
            lo = mid;
        }
    }

    cout << fixed << setprecision(7) << best << "\n";
    return 0;
}