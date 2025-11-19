#include <bits/stdc++.h>
#define ll int
#define LL long long
#define ull unsigned ll
#define fi first
#define se second
#define mkp make_pair
#define pir pair<ll, ll>
#define pb push_back
#define i128 __int128
using namespace std;
char buf[1 << 22], *p1, *p2;
template <class T>
const inline void rd(T &x) {
    char ch;
    bool neg = 0;
    while (!isdigit(ch = getchar()))
        if (ch == '-')
            neg = 1;
    x = ch - '0';
    while (isdigit(ch = getchar())) x = (x << 1) + (x << 3) + ch - '0';
    if (neg)
        x = -x;
}
const ll maxn = 1e6 + 10, inf = 1e9, mod = 1e9 + 7;
ll power(ll a, ll b = mod - 2) {
    ll s = 1;
    while (b) {
        if (b & 1)
            s = 1ll * s * a % mod;
        a = 1ll * a * a % mod, b >>= 1;
    }
    return s;
}
template <class T, class _T>
const inline ll pls(const T x, const _T y) { return x + y >= mod ? x + y - mod : x + y; }
template <class T, class _T>
const inline ll mus(const T x, const _T y) { return x < y ? x + mod - y : x - y; }
template <class T, class _T>
const inline void add(T &x, const _T y) { x = x + y >= mod ? x + y - mod : x + y; }
template <class T, class _T>
const inline void sub(T &x, const _T y) { x = x < y ? x + mod - y : x - y; }
template <class T, class _T>
const inline void chkmax(T &x, const _T y) { x = x < y ? y : x; }
template <class T, class _T>
const inline void chkmin(T &x, const _T y) { x = x < y ? x : y; }

ll T, n, a[maxn], b[maxn], ma, mb, da, db, ans;
char stra[maxn], strb[maxn];

ll calc() {
	ll d = 0;
	for(ll i = 1; i <= ma; i++) d += a[i];
	for(ll i = 1; i <= mb; i++) d -= b[i];
	if(d < 0) return inf;
	for(ll i = 1, j = 0, o = 0; i <= ma; i++) {
		if(j < mb && a[i] >= b[j + 1] && (a[i] > b[j + 1] || o == 0))
			o ^= (a[i] - b[++j]) & 1;
		else o ^= a[i] & 1;
		if(i == ma && j < mb) return inf;
	}
	return d / 2 + abs(da + d / 2 - db);
}

void solve() {
	rd(n), scanf("%s%s", stra + 1, strb + 1);
	ma = mb = 0, ans = inf;
	for(ll i = 1, j = 0; i <= n; i++)
		if(stra[i] == '1') {
			if(!j) da = i;
			else a[++ma] = i - j;
			j = i;
		}
	for(ll i = 1, j = 0; i <= n; i++)
		if(strb[i] == '1') {
			if(!j) db = i;
			else b[++mb] = i - j;
			j = i;
		}
	if(ma < mb) return puts("-1"), void();
	ll u = 0;
	for(ll i = 1; i <= ma; i++) u += a[i];
	for(ll i = 1; i <= mb; i++) u += b[i];
	if(u & 1) {
		--a[ma], ++da;
		chkmin(ans, calc() + 1);
		++a[ma], --da;
		--a[1];
		chkmin(ans, calc() + 1);
		++a[1];
	} else {
		chkmin(ans, calc());
		--a[ma], --a[1], ++da;
		chkmin(ans, calc() + 2);
		++a[ma], ++a[1], --da;
	}
	if(ans == inf) ans = -1;
	printf("%d\n", ans);
}

int main() {
	rd(T); while(T--) solve();
	return 0;
}