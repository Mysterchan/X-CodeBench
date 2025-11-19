#include <bits/stdc++.h>
using u32 = unsigned;
using i32 = int;
using i64 = long long;
using u64 = unsigned long long;
using i128 = __int128_t;
using u128 = __uint128_t;
using namespace std;

#define pb push_back
#define eb emplace_back
#define bug(x) << #x << " = " << x << ' '
#define vi vector < i32 >
#define mtc() int T = 1; MTC >> T; while (T--) work();

#define For(i, l, r) for (i32 i = (l); i <= (r); i++)
#define ForL(i, l, r) for (i64 i = (l); i <= (r); i++)
#define Fep(i, l, r) for (i32 i = (l); i >= (r); i--)
#define FepL(i, l, r) for (i64 i = (l); i >= (r); i--)

#define read(arr, l, r, p) for (i32 i = (l); i <= (r); i++) p >> arr[i];
#define write(arr, l, r, p) for (i32 i = (l); i <= (r); i++) p << arr[i] << " \n"[i == r];
#define ALL(S) S.begin(), S.end()
#define srt(S) sort(ALL(S))
#define rev(S) reverse(ALL(S))
#define sz(S) (i32)(S.size())

inline void work();
signed main();

const i32 NN = (1 << 20) + 5, mod = 998244353;
typedef vi poly;
u64 tmp[NN];
i32 gw[NN], A[NN], B[NN], C[NN];
inline i32 sm(i32 x) { return (x >= mod) ? (x - mod) : (x); }
inline i32 ksm(i32 x, i32 y, i32 res = 1) {
	for (; y; y >>= 1, x = 1ll * x * x % mod) if (y & 1) res = 1ll * res * x % mod;
	return res;
}
inline void init() {
	i32 t = 1; while ((1 << t) < NN) t++; t--;
	gw[0] = 1; gw[1 << t] = ksm(31, 1 << 21 - t);
	Fep (i, t, 1) gw[1 << i - 1] = 1ll * gw[1 << i] * gw[1 << i] % mod;
	For (i, 1, (1 << t) - 1) gw[i] = 1ll * gw[i & (i - 1)] * gw[i & (-i)] % mod;
}
inline void DIF(i32* A, i32 limit)
{
	for (i32 i = 0; i < limit; i++) tmp[i] = A[i];
	for (i32 len = limit >> 1; len >= 1; len >>= 1)
	{
		u64* k = tmp;
		for (i32* g = gw; k < tmp + limit; k += (len << 1), g++)
		{
			for (u64* x = k; x < k + len; x++)
			{
				i32 u = 1ll * x[len] * *g % mod;
				x[len] = *x + mod - u, * x += u;
			}
		}
	}
	for (i32 i = 0; i < limit; i++) A[i] = tmp[i] % mod;
}
inline void DIT(i32* A, i32 limit)
{
	for (i32 i = 0; i < limit; i++) tmp[i] = A[i];
	for (i32 len = 1; len < limit; len <<= 1)
	{
		u64* k = tmp;
		for (i32* g = gw; k < tmp + limit; k += (len << 1), g++)
		{
			for (u64* x = k; x < k + len; x++)
			{
				i32 u = x[len] % mod;
				x[len] = 1ll * (*x + mod - u) * *g % mod, * x += u;
			}
		}
	} i32 inv = ksm(limit, mod - 2); for (i32 i = 0; i < limit; i++) A[i] = 1ll * tmp[i] % mod * inv % mod;
	reverse(A + 1, A + limit);
}


const i32 N = 4e5 + 5;
i32 n, q[N], p[N], f[N];
i32 fac[N], inv[N];
char ch[N];
inline i32 INV(i32 x) {
	if (x < 0) return 0;
	return inv[x];
}
inline void solve(i32 l, i32 r) {
	if (l == r) {
		f[l] = 1ll * sm(fac[l] - f[l] + mod) * INV(l - q[l]) % mod;
		return ;
	}
	i32 mid = l + r >> 1;
	solve(l, mid);
	i32 L = q[l], R = q[mid], len = R - L + 1, L1 = max(0, mid + 1 - R), R1 = max(0, r - L), len1 = R1 - L1 + 1;
	For (i, l, mid) A[q[i] - L] = sm(A[q[i] - L] + f[i]);
	For (i, L1, R1) B[i - L1] = fac[i];
	i32 limit = 1; while (limit <= len + len1) limit <<= 1;
	DIF(A, limit), DIF(B, limit);
	For (i, 0, limit - 1) A[i] = 1ll * A[i] * B[i] % mod;
	DIT(A, limit);
	For (i, mid + 1, r) f[i] = sm(f[i] + A[i - L - L1]);
	For (i, 0, limit - 1) A[i] = B[i] = 0;
	solve(mid + 1, r);
}
inline void work() {
	cin >> n >> ch;
	if (ch[0] == 'W' || ch[n + n - 1] == 'B') return cout << "0\n", void();
	fac[0] = 1; For (i, 1, N - 1) fac[i] = 1ll * fac[i - 1] * i % mod;
	inv[N - 1] = ksm(fac[N - 1], mod - 2); Fep (i, N - 1, 1) inv[i - 1] = 1ll * inv[i] * i % mod;
	i32 j = 1; For (i, 1, n + n) (ch[i - 1] == 'W') && (p[j++] = i);
	For (i, 1, n) q[i] = p[i] - i;
	solve(1, n); cout << f[n] << '\n';
}


signed main() {
	init();
#ifdef LOCAL
	freopen(LOCAL".in", "r", stdin);
	freopen(LOCAL".out", "w", stdout);
#endif
	ios::sync_with_stdio(false), cin.tie(), cout.tie();
#ifdef MTC
	mtc();
#else
	work();
#endif
}