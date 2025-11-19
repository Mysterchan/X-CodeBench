
#include <bits/stdc++.h>

#define all(a) a.begin(),a.end()
#define len(a) (int)(a.size())
#define mp make_pair
#define pb push_back
#define fi first
#define se second

using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;
template<class T>
using vec = vector<T>;

template<typename T>
bool umin(T &a, T b) {
    if (b < a) {
        a = b;
        return true;
    }
    return false;
}
template<typename T>
bool umax(T &a, T b) {
    if (a < b) {
        a = b;
        return true;
    }
    return false;
}

#ifdef KoRoVa
#define DEBUG for (bool _FLAG = true; _FLAG; _FLAG = false)
#define LOG(...) print(#__VA_ARGS__" ::", __VA_ARGS__) << endl
template <class ...Ts> auto &print(Ts ...ts) { return ((cerr << ts << " "), ...); }
#else
#define DEBUG while (false)
#define LOG(...)
#endif

const int max_n = -1, inf = 1000111222;

struct node {
    ll x, y, z, xy, yz, xyz;
    node() : x(0), y(0), z(0), xy(0), yz(0), xyz(0) {}
};

inline node norm (ll a, ll b, ll c, ll d, ll e) {
    node res;
    res.x = min({a, b, c});
    res.y = min({b, c, d});
    res.z = min({c, d, e});
    res.xy = min({b, c});
    res.yz = min({c, d});
    res.xyz = c;



    umin(res.x, min(res.xy, res.xyz));
    umin(res.y, min({res.xy, res.yz, res.xyz}));
    umin(res.z, min(res.yz, res.xyz));
    umin(res.xy, min(res.x + res.y, res.xyz));
    umin(res.yz, min(res.y + res.z, res.xyz));
    umin(res.xyz, min(res.x + res.y + res.z, res.xy + res.z));
    umin(res.xyz, min(res.x + res.y + res.z, res.yz + res.x));

    return res;
}


void test_case() {
    int n;
    cin >> n;
    ll a, b, c, d, e;
    node ans;
    for (int i = 0; i < n; i++) {
        cin >> a >> b >> c >> d >> e;
        node res = norm(a, b, c, d, e);
        ans.x += res.x;
        ans.y += res.y;
        ans.z += res.z;
        ans.xy += res.xy;
        ans.xyz += res.xyz;
        ans.yz += res.yz;
        ll cur = min({ans.x, ans.y, ans.z, ans.xy / 2, ans.yz / 2, ans.xyz / 3});
        cout << cur << ' ';
    }
    cout << '\n';
}



int main() {

    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t = 1;

     cin >> t;

    while (t--) test_case();

    return 0;
}


