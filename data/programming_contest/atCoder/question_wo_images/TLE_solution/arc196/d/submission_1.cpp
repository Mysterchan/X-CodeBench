#include <bits/stdc++.h>
#define _rep(i, x, y) for(int i = x; i <= y; ++i)
#define _req(i, x, y) for(int i = x; i >= y; --i)
#define _rev(i, u) for(int i = head[u]; i; i = e[i].nxt)
#define pb push_back
#define fi first
#define se second
#define mst(f, i) memset(f, i, sizeof f)
using namespace std;
#ifdef ONLINE_JUDGE
#define debug(...) 0
#else
#define debug(...) fprintf(stderr, __VA_ARGS__), fflush(stderr)
#endif
typedef long long ll;
typedef pair<ll, ll> PII;
namespace fastio{
    #ifdef ONLINE_JUDGE
    char ibuf[1 << 20],*p1 = ibuf, *p2 = ibuf;
    #define get() p1 == p2 && (p2 = (p1 = ibuf) + fread(ibuf, 1, 1 << 20, stdin), p1 == p2) ? EOF : *p1++
    #else
    #define get() getchar()
    #endif
    template<typename T> inline void read(T &t){
        T x = 0, f = 1;
        char c = getchar();
        while(!isdigit(c)){
            if(c == '-') f = -f;
            c = getchar();
        }
        while(isdigit(c)) x = x * 10 + c - '0', c = getchar();
        t = x * f;
    }
    template<typename T, typename ... Args> inline void read(T &t, Args&... args){
        read(t);
        read(args...);
    }
    template<typename T> void write(T t){
        if(t < 0) putchar('-'), t = -t;
        if(t >= 10) write(t / 10);
        putchar(t % 10 + '0');
    }
    template<typename T, typename ... Args> void write(T t, Args... args){
        write(t), putchar(' '), write(args...);
    }
    template<typename T> void writeln(T t){
        write(t);
        puts("");
    }
    template<typename T> void writes(T t){
        write(t), putchar(' ');
    }
    #undef get
};
using namespace fastio;
#define multitest() int T; read(T); _rep(tCase, 1, T)
namespace Calculation{
    const ll mod = 998244353;
    ll ksm(ll p, ll h){ll base = p % mod, res = 1; while(h){if(h & 1ll) res = res * base % mod; base = base * base % mod, h >>= 1ll;} return res;}
    void dec(ll &x, ll y){x = ((x - y) % mod + mod) % mod;}
    void add(ll &x, ll y){x = (x + y) % mod;}
    void mul(ll &x, ll y){x = x * y % mod;}
    ll sub(ll x, ll y){return ((x - y) % mod + mod) % mod;}
    ll pls(ll x, ll y){return ((x + y) % mod + mod) % mod;}
    ll mult(ll x, ll y){return x * y % mod;}
}
using namespace Calculation;
const int N = 4e5 + 5;
int n, m, q, op[N];
PII a[N];
bool check(int l, int r){
	bool ok = 1;
	_rep(i, l, r) _rep(j, i + 1, r){
		int xl = a[i].fi, xr = a[i].se, yl = a[j].fi, yr = a[j].se;
        int zl = xl < xr, zr = yl < yr;
		if(xl > xr) swap(xl, xr); if(yl > yr) swap(yl, yr);
		if(xl == yl && xr != yr || xl != yl && xr == yr) ok = 0; 
        if(xl == yl && xr == yr && zl != zr) ok = 0;
		if(zl == zr){
			if(xl > yl) swap(xl, yl), swap(xr, yr);
			if(xl < yl && yl < xr && xr < yr) ok = 0;
		}
	}
	return ok;
}
int f[N];
map<PII, int> mp[2];
int cntl[N], cntr[N];
multiset<int> st[2][N], st2[2][N];
void ins(int x){
    mp[op[x]][a[x]]++;
    cntl[a[x].fi]++, cntr[a[x].se]++;
    st[op[x]][a[x].se].insert(a[x].fi);
    st2[op[x]][a[x].fi].insert(a[x].se);
}
void del(int x){
    mp[op[x]][a[x]]--;
    cntl[a[x].fi]--, cntr[a[x].se]--;
    st[op[x]][a[x].se].erase(st[op[x]][a[x].se].find(a[x].fi));
    st2[op[x]][a[x].fi].erase(st2[op[x]][a[x].fi].find(a[x].se));
}
bool check(int x){
    if(mp[op[x] ^ 1][a[x]]) return 0;
    int l = a[x].fi, r = a[x].se, t = mp[op[x]][a[x]];
    if(cntl[l] != t || cntr[r] != t) return 0;
    _rep(i, l + 1, r - 1){
        auto it = st[op[x]][i].lower_bound(l);
        if(it != st[op[x]][i].begin()) return 0;
    }
    _rep(i, l + 1, r - 1){
        auto it = st2[op[x]][i].upper_bound(r);
        if(it != st2[op[x]][i].end()) return 0;
    }
    return 1;
}
int main(){
	read(n, m, q);
	_rep(i, 1, m){
        read(a[i].fi, a[i].se), op[i] = a[i].fi < a[i].se;
        if(a[i].fi > a[i].se) swap(a[i].fi, a[i].se);
    }
    for(int i = 1, j = 1; i <= m; ++i){
        ins(i);
        while(!check(i)) del(j++);
        f[i] = j;
    }
	_rep(i, 1, q){
		int l, r; read(l, r);
        puts(f[r] <= l ? "Yes" : "No");
	}
    return 0;
}
