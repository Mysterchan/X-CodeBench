#include <bits/stdc++.h>

#define endl '\n'

#define ft first
#define sd second

#define yes cout << "yes\n"
#define no cout << "no\n"

#define Yes cout << "Yes\n"
#define No cout << "No\n"

#define YES cout << "YES\n"
#define NO cout << "NO\n"

#define pb push_back
#define eb emplace_back

#define all(x) x.begin(), x.end()
#define all1(x) x.begin() + 1, x.end()
#define unq_all(x) x.erase(unique(all(x)), x.end())
#define unq_all1(x) x.erase(unique(all1(x)), x.end())
#define sort_all(x) sort(all(x))
#define sort1_all(x) sort(all1(x))
#define reverse_all(x) reverse(all(x))
#define reverse1_all(x) reverse(all1(x))

#define inf 0x3f3f3f3f
#define infll 0x3f3f3f3f3f3f3f3fLL

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ld, ld> pdd;
typedef pair<ll, int> pli;
typedef pair<string, string> pss;
typedef pair<string, int> psi;
typedef pair<string, ll> psl;

typedef tuple<int, int, int> ti3;
typedef tuple<ll, ll, ll> tl3;
typedef tuple<ld, ld, ld> tld3;

typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<string> vs;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
typedef vector<pli> vpli;
typedef vector<pss> vpss;
typedef vector<ti3> vti3;
typedef vector<tl3> vtl3;
typedef vector<tld3> vtld3;

typedef vector<vi> vvi;
typedef vector<vl> vvl;

typedef queue<int> qi;
typedef queue<ll> ql;
typedef queue<pii> qpii;
typedef queue<pll> qpll;
typedef queue<psi> qpsi;
typedef queue<psl> qpsl;

typedef priority_queue<int> pqi;
typedef priority_queue<ll> pql;
typedef priority_queue<string> pqs;
typedef priority_queue<pii> pqpii;
typedef priority_queue<psi> pqpsi;
typedef priority_queue<pll> pqpll;
typedef priority_queue<psi> pqpsl;

typedef map<int, int> mii;
typedef map<int, bool> mib;
typedef map<ll, ll> mll;
typedef map<ll, bool> mlb;
typedef map<char, int> mci;
typedef map<char, ll> mcl;
typedef map<char, bool> mcb;
typedef map<string, int> msi;
typedef map<string, ll> msl;
typedef map<int, bool> mib;

typedef unordered_map<int, int> umii;
typedef unordered_map<ll, ll> uml;
typedef unordered_map<char, int> umci;
typedef unordered_map<char, ll> umcl;
typedef unordered_map<string, int> umsi;
typedef unordered_map<string, ll> umsl;

std::mt19937_64 rng (std::chrono::steady_clock::now ().time_since_epoch ().count ());

template <typename T>
inline T read () {
    T x = 0;
    int y = 1;
    char ch = getchar ();
    while (ch > '9' || ch < '0') {
        if (ch == '-')
            y = -1;
        ch = getchar ();
    }
    while (ch >= '0' && ch <= '9') {
        x = (x << 3) + (x << 1) + (ch ^ 48);
        ch = getchar ();
    }
    return x * y;
}

template <typename T>
inline void write (T x) {
    if (x < 0) {
        putchar ('-');
        x = -x;
    }
    if (x >= 10) {
        write (x / 10);
    }
    putchar (x % 10 + '0');
}


bool test = 0;

void init () {}

void solve () {
    int n;
    cin >> n;
    vvi a (n);
    for (int i = 0;i < n;i++) {
        int sz;cin >> sz;
        while (sz--) {
            int x;cin >> x;
            a[i].pb (x);
        }
        sort_all (a[i]);
    }
    pll ans = { 0,1 };
    for (int i = 0;i < n;i++) {
        for (int j = i + 1;j < n;j++) {
            ll cnt = 0;

            int li, lj;
            li = lj = 0;
            while (li < a[i].size () && lj < a[j].size ()) {
                int t = 0;
                while (lj < a[j].size () && a[j][lj] == a[i][li]) {
                    t++, lj++;
                }

                int idx = li;
                while (idx < a[i].size () && a[i][idx] == a[i][li]) {
                    cnt += t;
                    idx++;
                }
                li = idx;
            }
            ll g = __gcd (cnt, (ll) a[i].size () * (ll) a[j].size ());
            pll tt = { cnt / g, (ll) a[i].size () * (ll) a[j].size () / g };
            if (tt.ft * ans.sd > ans.ft * tt.sd)ans = tt;
        }
    }
    cout << double (ans.ft) / double (ans.sd) << endl;
}



int main () {
    ios::sync_with_stdio (false), std::cin.tie (0), std::cout.tie (0);
    int _ = 1;
    if (test)cin >> _;
    init ();
    while (_--) {
        solve ();
    }

    return 0;
}


