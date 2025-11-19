
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ull = unsigned long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using vi = vector<int>;
using vll = vector<ll>;

#define fi first
#define se second
#define ls(p) (p << 1)
#define rs(p) (p << 1 | 1)
#define file(a) freopen(#a".in","r",stdin);freopen(#a".out","w",stdout)

#ifdef LOCAL
void debug_out() { cout << endl; }
template <typename Head, typename... Tail>
void debug_out(Head H, Tail... T) {
    cout << H << " ";
    debug_out(T...);
}
#define debug(...) cout << "[" << #__VA_ARGS__ << "]:", debug_out(__VA_ARGS__)
#else
#define debug(...) 42
#endif

const int MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;
const ll LLINF = 0x3f3f3f3f3f3f3f3f;
const double EPS = 1e-9;
const int N = 3010;

int n, top;
int c[2 * N], d[2 * N];
ll s1[N], s2[N], s3[N], s4[N];
vector<pair<long double, pii>> edges;
vi graph[2 * N];

bool dfs(int u) {
    d[u] = 1;
    for (int v : graph[u]) {
        if (!c[v] || (!d[c[v]] && dfs(c[v]))) {
            c[v] = u;
            return true;
        }
    }
    return false;
}

bool check(ll x) {
    for (int i = 1; i <= 2 * n; i++) {
        c[i] = 0;
        graph[i].clear();
    }
    
    for (int i = 0; i < min((ll)edges.size(), x); i++) {
        auto [dist, edge] = edges[i];
        int u = edge.fi;
        int v = edge.se;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    
    int match_count = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= 2 * n; j++) {
            d[j] = 0;
        }
        if (dfs(i)) {
            match_count++;
        }
    }
    
    return match_count == n;
}

int main() {
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        scanf("%lld%lld", &s1[i], &s2[i]);
    }
    for (int i = 1; i <= n; i++) {
        scanf("%lld%lld", &s3[i], &s4[i]);
    }
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            ll dx = s1[i] - s3[j];
            ll dy = s2[i] - s4[j];
            long double dist = sqrt((long double)(dx * dx + dy * dy));
            edges.emplace_back(dist, make_pair(i, n + j));
        }
    }
    
    sort(edges.begin(), edges.end());
    
    ll left = 0, right = edges.size() + 1;
    while (left + 1 < right) {
        ll mid = (left + right) / 2;
        if (check(mid)) {
            right = mid;
        } else {
            left = mid;
        }
    }
    
    printf("%.20Lf\n", edges[right - 1].fi);
    
    return 0;
}