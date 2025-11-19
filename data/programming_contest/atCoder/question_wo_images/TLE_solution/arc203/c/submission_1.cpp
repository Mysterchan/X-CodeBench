#define TEST
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#if 1
const int INFI = (int)(1e9);
const ll INFL = (ll)(1e18l);
const int MOD = 998244353;
const double EPS = 1e-9;

template<typename U, typename V>
class Pair : public pair<U, V> {
public:
    using pair<U, V>::pair;
    Pair() : pair<U, V>() {}
    Pair(U u, V v) : pair<U, V>(u, v) {}
    U& operator[](int i) { return i ? this->second : this->first; };
    const U& operator[](int i) const { return i ? this->second : this->first; };
};

template <typename U>
class Pair2 : public pair<U, U> {
public:
    using pair<U, U>::pair;
    Pair2() : pair<U, U>() {}
    Pair2(U u) : pair<U, U>(u, u) {}
    U& operator[](int i) { return i ? this->second : this->first; };
    const U& operator[](int i) const { return i ? this->second : this->first; };
};

template<typename... T>
using Tup = tuple<T...>;

template<typename T, typename C = greater<T>>
using Heap = priority_queue<T, vector<T>, C>;

template<typename T>
using MinHeap = Heap<T>;

template<typename T>
using MaxHeap = Heap<T, less<T>>;

template<typename U, size_t N>
using Vec = array<U, N>;
template<typename U> using Vec2 = Pair2<U>;
template<typename U> using Vec3 = Vec<U, 3>;
using Vec2i = Vec2<int>;
using Vec2l = Vec2<ll>;
using Vec2d = Vec2<double>;
using Vec3i = Vec3<int>;
using Vec3l = Vec3<ll>;
using Vec3d = Vec3<double>;

template<typename U, size_t N>
istream& operator>>(istream& is, Vec<U, N>& v) {
    for (auto& x : v) is >> x;
    return is;
}

template<typename U, size_t N>
ostream& operator<<(ostream& os, const Vec<U, N>& v) {
    for (auto& x : v) os << x << ' ';
    return os;
}

template<typename U, typename V>
istream& operator>>(istream& is, Pair<U, V>& p) {
    is >> p.first >> p.second;
    return is;
}

template<typename U, typename V>
ostream& operator<<(ostream& os, const Pair<U, V>& p) {
    os << p.first << ' ' << p.second;
    return os;
}

template<typename U>
istream& operator>>(istream& is, Pair2<U>& p) {
    is >> p.first >> p.second;
    return is;
}

template<typename U>
ostream& operator<<(ostream& os, const Pair2<U>& p) {
    os << p.first << ' ' << p.second;
    return os;
}

#ifdef HASH
namespace std {
    template<typename U, typename V>
    struct hash<Pair<U,V>> {
        size_t operator()(Pair<U,V> const& a) const noexcept {
            size_t h1 = std::hash<U>{}(a.first);
            size_t h2 = std::hash<V>{}(a.second);
            return h1 ^ (h2 + 0x9e3779b9 + (h1<<6) + (h1>>2));
        }
    };

    template<typename... T>
    struct hash<Tup<T...>> {
        size_t operator()(Tup<T...> const& a) const noexcept {
            size_t h = 0;
            std::apply([&](auto const&... elems) {
                ((h ^= std::hash<std::decay_t<decltype(elems)>>{}(elems)
                    + 0x9e3779b9 + (h << 6) + (h >> 2)), ...);
            }, a);
            return h;
        }
    };

    template<typename U, size_t N>
    struct hash<Vec<U,N>> {
        size_t operator()(Vec<U,N> const& a) const noexcept {
            size_t h = 0;
            hash<U> hU;
            for (auto& e : a) {
                h ^= hU(e) + 0x9e3779b9 + (h << 6) + (h >> 2);
            }
            return h;
        }
    };
}
#endif


template<typename T>
T I() { T x; cin >> x; return x; }

template<typename T>
vector<T> II(int n) {
    vector<T> v(n);
    for (int i = 0; i < n; i++) cin >> v[i];
    return v;
}

template<typename T>
vector<vector<T>> III(int n, int m) {
    vector<vector<T>> a(n, vector<T>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> a[i][j];
        }
    }
    return a;
}

template<typename T, size_t N>
Vec<vector<T>, N> IV(int n) {
    Vec<vector<T>, N> a;
    for (auto& vec : a) vec.resize(n);
    for (int i = 0; i < n; i++) {
        auto x = I<Vec<T, N>>();
        for (int j = 0; j < N; j++) {
            a[j][i] = x[j];
        }
    }
    return a;
}

auto Ii = I<int>;
auto Il = I<ll>;
auto Is = I<string>;
auto Ii2 = I<Vec2i>;
auto Il2 = I<Vec2l>;
auto Id2 = I<Vec2d>;
auto Ii3 = I<Vec3i>;
auto Il3 = I<Vec3l>;
auto Id3 = I<Vec3d>;

auto IIi = II<int>;
auto IIl = II<ll>;
auto IIs = II<string>;
auto IIi2 = II<Vec2i>;
auto IIl2 = II<Vec2l>;
auto IId2 = II<Vec2d>;
auto IIi3 = II<Vec3i>;
auto IIl3 = II<Vec3l>;
auto IId3 = II<Vec3d>;

auto IIIi = III<int>;
auto IIIl = III<ll>;
auto IIIs = III<string>;
auto IIIi2 = III<Vec2i>;
auto IIIl2 = III<Vec3l>;
auto IIId2 = III<Vec2d>;
auto IIIi3 = III<Vec3i>;
auto IIIl3 = III<Vec3l>;
auto IIId3 = III<Vec3d>;

auto IVi2 = IV<int, 2>;
auto IVl2 = IV<ll, 2>;
auto IVd2 = IV<double, 2>;
auto IVi3 = IV<int, 3>;
auto IVl3 = IV<ll, 3>;
auto IVd3 = IV<double, 3>;

vector<vector<int>> IG(int n, int m, bool directed = false, bool one_indexed = true) {
    vector<vector<int>> g(n + (one_indexed ? 1 : 0));
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        if (!directed) g[v].push_back(u);
    }
    return g;
}

template<typename W>
vector<vector<Pair<int, W>>> IWG(int n, int m, bool directed = false, bool one_indexed = true) {
    vector<vector<Pair<int, W>>> g(n + (one_indexed ? 1 : 0));
    for (int i = 0; i < m; i++) {
        int u, v; W w;
        cin >> u >> v >> w;
        g[u].emplace_back(v, w);
        if (!directed) g[v].emplace_back(u, w);
    }
    return g;
}

template<typename... T>
void O(T... x) {
    ((cout << x << " "), ...);
    cout << '\n';
}

template<typename T>
void OI(vector<T> x) {
    for (auto& e : x) cout << e << ' ';
    cout << '\n';
}

template<typename T>
void OII(vector<vector<T>> x) {
    for (auto& e : x) {
        for (auto& f : e) cout << f << ' ';
        cout << '\n';
    }
}

void OYN(bool b) { O(b ? "Yes" : "No"); }
void OHP(double x) { O(fixed, setprecision(16), x); }

namespace tools {

ll qpow(ll x, ll n) {
    x %= MOD;
    ll res = 1;
    while (n) {
        if (n & 1) res = (res * x) % MOD;
        x = (x * x) % MOD;
        n >>= 1;
    }
    return res;
}

ll inv(ll x) {
    return qpow(x, MOD - 2);
}

template<typename T>
T sum(const vector<T>& a) {
    return accumulate(a.begin(), a.end(), T(0));
}

template<typename T>
T max(const T& a) {
    return a;
}

template<typename T, typename... Args>
T max(const T& a, const Args&... args) {
    return std::max(a, max(args...));
}

template<typename T>
T min(const T& a) {
    return a;
}

template<typename T, typename... Args>
T min(const T& a, const Args&... args) {
    return std::min(a, min(args...));
}

template<typename T>
T max_element(const vector<T>& a) {
    return *max_element(a.begin(), a.end());
}

template<typename T>
T min_element(const vector<T>& a) {
    return *min_element(a.begin(), a.end());
}

template<typename T>
int bisect_left(const vector<T>& a, T x) {
    return int(lower_bound(a.begin(), a.end(), x) - a.begin());
}

template<typename T>
int bisect_right(const vector<T>& a, T x) {
    return int(upper_bound(a.begin(), a.end(), x) - a.begin());
}

template<typename T>
void sort(vector<T>& a, bool rev = false, function<bool(T, T)> cmp = less<T>()) {
    if (rev) {
        sort(a.begin(), a.end(), [&](const T& x, const T& y) {
            return cmp(y, x);
            });
    }
    else {
        sort(a.begin(), a.end(), cmp);
    }
}

}


namespace ps {

template<typename T>
vector<T> build(const vector<T>& a) {
    int n = (int)a.size();
    vector<T> res(n + 1);
    for (int i = 0; i < n; i++)
        res[i + 1] = res[i] + a[i];
    return res;
}

template<typename T>
T query(const vector<T>& a, int l, int r) {
    return a[r + 1] - a[l];
}

}

namespace comb {

vector<ll> _fact;
vector<ll> _ifact;

void init(int n) {
    _fact.resize(n + 1);
    _fact[0] = 1;
    for (int i = 1; i <= n; i++)
        _fact[i] = _fact[i - 1] * i % MOD;

    _ifact.resize(n + 1);
    _ifact[n] = tools::inv(_fact[n]);
    for (int i = n - 1; i >= 0; i--)
        _ifact[i] = _ifact[i + 1] * (i + 1) % MOD;
}

ll nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return _fact[n] * _ifact[r] % MOD * _ifact[n - r] % MOD;
}

}

namespace topk {

template<typename T>
void add(const T& x, vector<T>& dst, int k, bool rev = false) {
    auto pos = rev
        ? lower_bound(dst.begin(), dst.end(), x, greater<T>())
        : upper_bound(dst.begin(), dst.end(), x);
    dst.insert(pos, x);

    if ((int)dst.size() > k)
        dst.pop_back();
}

template<typename T>
vector<T> build(const vector<T>& a, int k, bool rev = false) {
    vector<T> res;
    for (const T& x : a) {
        add(x, res, k, rev);
    }
    return res;
}

template<typename T>
vector<T> ksmallest(const vector<T>& a, int k) {
    return build(a, k, false);
}

template<typename T>
vector<T> klargest(const vector<T>& a, int k) {
    return build(a, k, true);
}

}

#define max_eq(a, ...) a = tools::max((a), __VA_ARGS__);
#define min_eq(a, ...) a = tools::min((a), __VA_ARGS__);

#endif

void solve();

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

#ifdef TEST
    int t = Ii();
    while (t--) solve();
#else
    solve();
#endif
    return 0;
}


ll norm(ll x) {
    x %= MOD;
    if (x < 0) x += MOD;
    return x;
}

void solve() {
    auto [n0, m0, k] = Ii3();
    ll n = n0, m = m0;
    ll need = n + m - 2;
    if (k < need) {
        O(0);
        return;
    }

    ll total_full = (n - 1) * 1ll * m + (m - 1) * 1ll * n;
    comb::init(need);
    ll ans = comb::nCr(need, (int)(n - 1));
    ans = norm(ans);

    if (k == need) {
        O(ans);
        return;
    }

    ll more = norm(total_full - need);

    if (k == need + 1) {
        ans = norm(ans * more);
        O(ans);
        return;
    }

    ll inv2 = tools::inv(2);
    ll mul = more * ((more - 1 + MOD) % MOD) % MOD;
    mul = mul * inv2 % MOD;
    ans = ans * mul % MOD;

    ll term1 = comb::nCr(need - 2, (int)(n - 2)) * ((need - 1) % MOD) % MOD;
    ans = norm(ans - term1);

    for (int t = 0; t < 2; t++) {
        ll nn = (t == 0 ? n0 : m0);
        ll mm = (t == 0 ? m0 : n0);
        if (need - 1 >= 0 && nn <= need - 1 && nn >= 0) {
            ll c1 = comb::nCr(need - 1, (int)nn) % MOD;
            ll add = c1 * (need % MOD) % MOD;
            ans = norm(ans + add);
        }
        if (need >= 0 && nn + 1 <= need && nn + 1 >= 0) {
            ll c2 = comb::nCr(need, (int)(nn + 1)) % MOD;
            ll sub = (2 % MOD) * c2 % MOD;
            ans = norm(ans - sub);
        }
    }

    O(ans);
}
