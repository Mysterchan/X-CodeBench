#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll prime = 998244353;

int main() {
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
#endif
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll t;
    cin >> t;
    while (t--) {
        ll h, w;
        cin >> h >> w;
        vector<string> a(h);
        for (auto &it: a) cin >> it;

        vector<bool> rowVisit(h), colVisit(w);
        vector<vector<int>> arr(h);
        for (int i = 0; i < h; ++i) {
            arr[i].resize(w);
        }
        ll ans = 1;
        bool pos = true;
        for (int i = 0; i < h; ++i) {
            if (rowVisit[i]) continue;
            rowVisit[i] = true;
            stack<pair<ll, ll>> rows, cols;
            for (int j = 0; j < w; ++j) {
                if (a[i][j] == 'B') {
                    rows.push(make_pair(i, j));
                    cols.push(make_pair(i, j));
                    colVisit[j] = true;
                    arr[i][j] = 1;
                    break;
                }
            }
            ans = (ans * 2) % prime;
            if (rows.empty()) {
                if (w % 2 == 1) {
                    pos = false;
                    break;
                }
                continue;
            }
            while (!rows.empty() || !cols.empty()) {
                if (!pos) break;
                if (!rows.empty()) {
                    auto cur = rows.top();
                    ll last = cur.second;
                    rows.pop();
                    for (int j = 1; j <= w; ++j) {
                        if (a[cur.first][(cur.second + j) % w] == 'B') {
                            int next = 0;
                            if ((cur.second + j - last) % 2 == 1) next = arr[cur.first][last % w];
                            else next = 3 - arr[cur.first][last % w];
                            last = cur.second + j;
                            if (arr[cur.first][(cur.second + j) % w] != 0 &&
                                arr[cur.first][(cur.second + j) % w] != next) {
                                pos = false;
                                break;
                            }
                            if (arr[cur.first][(cur.second + j) % w] != 0) continue;
                            arr[cur.first][(cur.second + j) % w] = next;
                            cols.push(make_pair(cur.first, (cur.second + j) % w));
                            colVisit[(cur.second + j) % w] = true;
                        }
                    }
                    continue;
                }
                auto cur = cols.top();
                ll last = cur.first;
                cols.pop();
                for (int j = 1; j <= h; ++j) {
                    if (a[(cur.first + j) % h][cur.second] == 'B') {
                        int next = 0;
                        if ((cur.first + j - last) % 2 == 1) next = arr[last % h][cur.second];
                        else next = 3 - arr[last % h][cur.second];
                        last = cur.first + j;
                        if (arr[(cur.first + j) % h][cur.second] != 0 &&
                            arr[(cur.first + j) % h][cur.second] != next) {
                            pos = false;
                            break;
                        }
                        if (arr[(cur.first + j) % h][cur.second] != 0) continue;
                        arr[(cur.first + j) % h][cur.second] = next;
                        rows.push(make_pair((cur.first + j) % h, cur.second));
                        rowVisit[(cur.first + j) % h] = true;
                    }
                }
            }
            if (!pos) break;
        }
        for (int j = 0; j < w; ++j) {
            bool empty = true;
            for (int i = 0; i < h; ++i) {
                if (a[i][j] == 'B') {
                    empty = false;
                    break;
                }
            }
            if (empty) {
                if (h % 2 == 1) {
                    pos = false;
                    break;
                }
                ans = (ans * 2) % prime;
            }
        }
        if (pos) cout << ans << endl;
        else cout << 0 << endl;
    }

    return 0;
}