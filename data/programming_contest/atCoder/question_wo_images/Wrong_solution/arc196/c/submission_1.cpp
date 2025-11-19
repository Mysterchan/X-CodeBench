#pragma optimize "-03, unroll - loops"
#pragma GCC optmize("avx2,bmi,bmi2,lzcnt,popcnt")
#pragma GCC optmize("unroll-loops")
#pragma GCC optmize("O3")
#include <bits/extc++.h>
using namespace std;
using namespace __gnu_pbds;
mt19937 rnd(time(NULL));
template <class T>
using order_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
const int M = 2e5;
vector<int> g[M + 1];
int a[M + 1];
cc_hash_table<int, int> Tree[2 * M + 1];
long long inv = 0;
int n, m;
inline void add(int x, int y, int val) {
    for (int i = x; i <= 2 * M; i |= i + 1) {
        for (int j = y; j <= M; j |= j + 1) Tree[i][j] += val;
    }
    return;
}
inline int get(int x, int y) {
    int res = 0;
    for (int i = x; i >= 0; i = (i & (i + 1)) - 1) {
        for (int j = y; j >= 0; j = (j & (j + 1)) - 1) {
            if (Tree[i].find(j) != Tree[i].end()) {
                res += Tree[i][j];
            }
        }
    }
    return res;
}
inline int get(int x1, int x2, int y1, int y2) {
    return get(x2, y2) + get(x1 - 1, y1 - 1) - get(x2, y1 - 1) - get(x1 - 1, y2);
};
signed main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    scanf("%d %d", &n, &m);
    for (int i = 1; i <= n; ++i) scanf("%d", &a[i]), g[a[i]].push_back(i);
    for (int i = 0; i <= m; ++i) reverse(g[i].begin(), g[i].end());
    for (int i = 1; i <= n; ++i) add(a[i] + M, i, 1);
    for (int i = 1; i <= n; ++i) {
        inv += get(a[i] + M + 1, 2 * M, 1, i - 1);
    }
    printf("%d\n", inv);
    for (int j = 1; j < m; ++j) {
        for (auto to : g[m - j]) {
            inv -= get(0, a[to] + M - 1, to + 1, n);
            add(a[to] + M, to, -1);
            a[to] = -j;
            add(a[to] + M, to, 1);
            inv += get(a[to] + M + 1, 2 * M, 1, to);
        }
        printf("%d\n", inv);
    }
    return 0;
}
