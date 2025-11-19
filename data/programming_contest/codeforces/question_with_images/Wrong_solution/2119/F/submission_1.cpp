#include "bits/stdc++.h"
using namespace std;


#ifdef LOCAL
#include "debug.h"
#else
#define debu(...)
#define debug(...)
#endif

using ll = long long;

using str = string;
using AR2 = array<int, 2>;
template <class T> using vec = vector<T>;
template <class T> using vvec = vec<vec<T>>;
template <class T> using vvvec = vec<vvec<T>>;
template <class T, size_t SZ> using vac = vec<array<T, SZ>>;
template <class T, size_t SZ> using vvac = vec<vac<T, SZ>>;
template <class T> using pqueue = priority_queue<T, vec<T>>;
template <class T> using pqueue_min = priority_queue<T, vec<T>, greater<T>>;

#define sz(x) int((x).size())
#define all(x) begin(x), end(x)
#define rall(x) x.rbegin(), x.rend()
#define sor(x) sort(all(x))
#define pb push_back

#define F_OR(i, a, b, s) for (int i=(a); (s)>0?i<(int)(b):i>(int)(b); i+=(s))
#define F_OR1(e) F_OR(i, 0, e, 1)
#define F_OR2(i, e) F_OR(i, 0, e, 1)
#define F_OR3(i, b, e) F_OR(i, b, e, 1)
#define F_OR4(i, b, e, s) F_OR(i, b, e, s)
#define GET5(a, b, c, d, e, ...) e
#define F_ORC(...) GET5(__VA_ARGS__, F_OR4, F_OR3, F_OR2, F_OR1)
#define FOR(...) F_ORC(__VA_ARGS__)(__VA_ARGS__)
#define E_ACH2(x, a) for (auto& x: a)
#define E_ACH3(x, y, a) for (auto& [x, y]: a)
#define E_ACH4(x, y, z, a) for (auto& [x, y, z]: a)
#define E_ACHC(...) GET5(__VA_ARGS__, E_ACH4, E_ACH3, E_ACH2)
#define EACH(...) E_ACHC(__VA_ARGS__)(__VA_ARGS__)
#define SUBMASKS(t, s) for (ll t = (s); t >= 0; t = (t == 0 ? -1 : (t - 1) & (s)))
#define MIN(v) *min_element(all(v))
#define MAX(v) *max_element(all(v))
#define SUM(v) accumulate(all(v), 0);

constexpr int popcount(int x) { return __builtin_popcount(x); }
constexpr int bitlength(int x) { return x == 0 ? 0 : 31 - __builtin_clz(x); }
ll cdiv(ll a, ll b) { return a/b + ((a^b) > 0 && a % b); };
ll fdiv(ll a, ll b) { return a/b - ((a^b) < 0 && a % b); };
template <class T> T pop(vec<T> &v) { T x = v.back(); v.pop_back(); return x; }
template <class T> bool bounds(T a, T lo, T hi) { return lo <= a && a <= hi; }
template <class T> T truemod(T x, T M) { return (x % M + M) % M; }
template <class T> bool umin(T &a, const T &b) { return b < a ? a = b, 1 : 0; }
template <class T> bool umax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }
template <class T> int lwb(vec<T> &a,  T b) { return int(lower_bound(all(a), b) - begin(a)); }
template <class T> int upb(vec<T> &a,  T b) { return int(upper_bound(all(a), b) - begin(a)); }
template <class T> void removeDupes(vec<T> &v) { sort(all(v)); v.erase(unique(all(v)), end(v)); }
template <class T, class U> void eraseOne(T &t,  U &u) { auto it = t.find(u); assert(it != end(t)); t.erase(it); }
template <class T, class P> void removeif(std::vector<T>& v, P p) { v.erase(remove_if(v.begin(), v.end(), p), v.end());}
template <class T, class U> T firstTrue(T lo, T hi, U f) {
    ++hi; assert(lo <= hi);
    while (lo < hi) {
        T mi = lo + (hi-lo) / 2;
        f(mi) ? hi = mi : lo = mi + 1;
    }
    return lo;
}
template <class T, class U> T lastTrue(T lo, T hi, U f) {
    --lo; assert(lo <= hi);
    while (lo < hi) {
        T mi = lo + (hi-lo+1) / 2;
        f(mi) ? lo = mi : hi = mi - 1;
    }
    return lo;
}

template <class T, size_t SZ> istream &operator>>(istream &s, array<T, SZ>& v) { FOR(sz(v)) s >> v[i]; return s; }
template <class T> istream &operator>>(istream &s, vec<T>& v) { FOR(sz(v)) s >> v[i]; return s; }
template <class T> ostream &operator<<(ostream &s, vec<T>& v) { FOR(sz(v)) s << (i?" ":"") << v[i]; return s; }
template <class T> ostream &operator<<(ostream &s, const vec<T>& v) { FOR(sz(v)) s << (i?" ":"") << v[i]; return s; }
template <class T1, class T2> ostream &operator<<(ostream &s, const pair<T1, T2>& v) { s << v.first << " " << v.second; return s;}

template<class A> void write(A x) { cout << x; }
template<class H, class... T> void write(const H& h, const T&... t) { 
  write(h); write(t...); }
void print() { write("\n"); }
template<class H, class... T> void print(const H& h, const T&... t) { 
  write(h); if (sizeof...(t)) write(" "); print(t...); }

void decrement() {}
template <class T, size_t SZ> void decrement(vec<array<T, SZ>> &v) { EACH(row, v) EACH(x, row) --x; }
template <class T> void decrement(vec<vec<T>> &v) { EACH(row, v) EACH(x, row) --x; }
template <class T> void decrement(vec<T> &v) { EACH(x, v) --x; }
template <class T, class... U> void decrement(T &t, U &...u) { --t; decrement(u...); }

template <class T> void read(T& x) { cin >> x; }
template<class T, class... U> void read(T &t, U &...u) { read(t); read(u...); }
#define ints(...) int __VA_ARGS__; read(__VA_ARGS__);
#define int1(...) ints(__VA_ARGS__); decrement(__VA_ARGS__);
#define jnts(...) ll __VA_ARGS__; read(__VA_ARGS__);
#define vint(n, a) int n; cin >> n; vec<int> a(n); cin >> a;
#define vin(n, a) vec<int> a((n)); cin >> a;
#define vjn(n, a) vec<ll> a((n)); cin >> a;
#define vvin(n, m, a) vec<vec<int>> a((n), vec<int>((m))); cin >> a;
#define vain(n, m, a) vec<array<int, (m)>> a((n)); cin >> a;
#define graphin(n, m, adj) vvec<int> adj(n); FOR(m) {int1(u, v); adj[u].pb(v); adj[v].pb(u); }
#define lgraphin(n, m, adj) vvac<int, 2> adj(n); FOR(i, m) {int1(u, v); adj[u].pb({v,i}); adj[v].pb({u,i}); }
#define wgraphin(n, m, adj) vvac<int, 2> adj(n); FOR(m) {int1(u, v); ints(w); adj[u].pb({v,w}); adj[v].pb({u,w}); }
#define dgraphin(n, m, adj) vvec<int> adj(n); FOR(m) {int1(u, v); adj[u].pb(v);}
#define dwgraphin(n, m, adj) vvac<int, 2> adj(n); FOR(m) {int1(u, v, w); adj[u].pb({v, w+1});}


void solve() {
    ints(N);
    int1(st);
    vin(N, W);
    graphin(N, N - 1, adj);

    int LOG = 1;
    while ((1 << LOG) <= N)
        LOG++;
    vvec<int> parent(LOG, vec<int>(N));
    vec<int> depth(N), sm(N), qu;

    qu.pb(0);
    int qi = 0;
    while (qi < sz(qu)) {
        int u = qu[qi++];
        for (int v : adj[u]) {
            if (v == parent[0][u])
                continue;
            parent[0][v] = u;
            depth[v] = depth[u] + 1;
            qu.pb(v);
        }
    }

    FOR(k, 1, LOG) FOR(u, 0, N) { //
        parent[k][u] = parent[k - 1][parent[k - 1][u]];
    }
    FOR(i, 0, sz(qu)) { //
        sm[qu[i]] = depth[qu[i]];
    }
    FOR(i, sz(qu) - 1, 0, -1) {
        int u = qu[i];
        int p = parent[0][u];
        umax(sm[p], sm[u]);
    }

    int d = depth[st];
    int up = d - (d + 2) / 2;
    int u = st;
    FOR(b, 0, LOG) if (up & (1 << b)) u = parent[b][u];
    int ans = sm[u];
    if (d % 2 == 0)
        ans--;
    print(ans);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ints(T);
    FOR(tc, T) solve();
}