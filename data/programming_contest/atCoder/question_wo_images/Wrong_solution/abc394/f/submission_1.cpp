#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, n) for (int i = 0; i <= (int)(n); i++)
#define rep3(i, s, n) for (int i = (s); i < (int)(n); i++)
#define rep4(i, s, n) for (int i = (s); i <= (int)(n); i++)
#define all(v) (v).begin(), (v).end()

using namespace std;
using ll = long long;
using ul = unsigned long long;
using ld = long double;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
template <class T> using v = vector<T>;



void dfs(int from, int cur, const v<v<int>> &G, v<int> &record) {
    vector<int> scores;
    for (int to : G[cur]) {
        if (to == from)
            continue;
        dfs(cur, to, G, record);
        scores.push_back(record[to]);
    }
    int score = 0;
    sort(all(scores), greater<int>());
    if (scores.size() >= 4) {
        if (from == -1 || record[from] == 0) {
            score = scores[0] + scores[1] + scores[2] + scores[3];
        } else {
            score = scores[0] + scores[1] + scores[2];
        }
    } else {
        for (int s : scores) {
            score += s;
        }
    }

    if (G[cur].size() >= 4) {
        record[cur] = score + 1;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    v<v<int>> G(N);
    rep(i, N - 1) {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        G[a].push_back(b);
        G[b].push_back(a);
    }

    int ans = -1;
    v<int> record(N, 0);

    dfs(-1, 0, G, record);

    rep(i, N) {
        ans = max(ans, record[i]);
    }
    cout << endl;

    if (ans == 0) {
        cout << -1 << endl;
    } else {
        cout << ans * 3 + 2 << endl;
    }
    return 0;
}
