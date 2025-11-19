#include <bits/stdc++.h>
using namespace std;

#ifdef MIKU
string dbmc = "\033[1;38;2;57;197;187m", dbrs = "\033[0m";
#define debug(x...) cerr << dbmc << "[" << #x << "]: ", dout(x)
void dout() { cerr << dbrs << endl; }
template <typename T, typename ...U>
void dout(T t, U ...u) { cerr << t << (sizeof...(u) ? ", " : ""); dout(u...); }
#else
#define debug(...) 39
#endif

#define fs first
#define sc second
#define mp make_pair
#define FOR(i, j, k) for (int i = j, Z = k; i < Z; i++)
using ll = long long;
typedef pair<int, int> pii;

const int MXN = 1005;
int n, m, x, y;
vector<int> G[MXN];

bitset<MXN> b, ban;

void DFS(int id) {
    b[id] = true;
    for (auto &i : G[id]) {
        if (ban[i] || b[i]) {
            continue;
        }
        DFS(i);
    }
}

void miku() {
    cin >> n >> m >> x >> y;
    while (m--) {
        int a, b;
        cin >> a >> b;
        G[a].push_back(b);
        G[b].push_back(a);
    }
    cout << x << ' ';
    ban[x] = true;
    while (!ban[y]) {
        DFS(y);
        int id = b._Find_first();
        cout << id << ' ';
        ban[id] = true;
        b.reset();
    }
    cout << '\n';
    ban.reset();
    FOR(i, 1, n + 1) {
        G[i].clear();
    }
}

int32_t main() {
    cin.tie(0) -> sync_with_stdio(false);
    cin.exceptions(cin.failbit);
    int t;
    cin >> t;
    while (t--) {
        miku();
    }
    return 0;
}

