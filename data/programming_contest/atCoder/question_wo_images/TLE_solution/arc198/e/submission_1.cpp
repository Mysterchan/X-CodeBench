#include <bits/stdc++.h>
#define REP(i, l, r) for (int i = (l); i <= (r); ++ i)
#define DEP(i, r, l) for (int i = (r); i >= (l); -- i)
#define CUP(i, l, r) for (int i = (l); i < (r); ++ i)
#define CDW(i, r, l) for (int i = (r) - 1; i >= (l); -- i)
#define fi first
#define se second
#define pb emplace_back
#define mems(x, v) memset((x), (v), sizeof(x))
#define SZ(x) (int)(x).size()
#define ALL(x) (x).begin(), (x).end()
#define ppc(x) __builtin_popcount(x)
using namespace std;
namespace math {
	typedef long long LL;
	template <class T> T qpow(T a, LL b) { if (!b) return {1}; T rs = a; b --; for (; b; b >>= 1, a = a * a) if (b & 1) rs = rs * a; return rs; }
	LL mul(LL a, LL b, LL p) { LL rs = a * b - LL(1.L * a * b / p) * p; rs %= p; if (rs < 0) rs += p; return rs; }
	template <unsigned P = 0> struct mint {
		unsigned v; static unsigned mod; mint() = default;
		template <class T> mint(T x) { x %= (int)getmod(), v = x < 0 ? x + getmod() : x; }
		constexpr static unsigned getmod() { if (P > 0) return P; else return mod; }
		static void setmod(unsigned m) { mod = m; }
		mint operator + () const { return *this; }
		mint operator - () const { return mint(0) - *this; }
		mint inv() const { return assert(v), qpow(*this, getmod() - 2); }
		int val() const { return v; }
		mint &operator += (const mint &q) { if (v += q.v, v >= getmod()) v -= getmod(); return *this; }
		mint &operator -= (const mint &q) { if (v -= q.v, v >= getmod()) v += getmod(); return *this; }
		mint &operator *= (const mint &q) { v = 1ull * v * q.v % getmod(); return *this; }
		mint &operator /= (const mint &q) { return *this *= q.inv(); }
		friend mint operator + (mint p, const mint &q) { return p += q; }
		friend mint operator - (mint p, const mint &q) { return p -= q; }
		friend mint operator * (mint p, const mint &q) { return p *= q; }
		friend mint operator / (mint p, const mint &q) { return p /= q; }
		friend bool operator == (const mint &p, const mint &q) { return p.v == q.v; }
		friend bool operator != (const mint &p, const mint &q) { return p.v != q.v; }
		friend bool operator < (const mint &p, const mint &q) { return p.v < q.v; }
		friend bool operator > (const mint &p, const mint &q) { return p.v > q.v; }
		friend bool operator <= (const mint &p, const mint &q) { return p.v <= q.v; }
		friend bool operator >= (const mint &p, const mint &q) { return p.v >= q.v; }
		friend istream &operator >> (istream &is, mint &a) { LL x; is >> x, a = x; return is; }
		friend ostream &operator << (ostream &os, const mint &a) { os << a.v; return os; }
	};
	template <> unsigned mint<0>::mod = 998244353;
}
namespace Milkcat {
	using namespace math;
	typedef long long LL;
	typedef pair<LL, LL> pii;
	const int N = 1 << 24, mod = 998244353;
	typedef mint<mod> MI;
	int n, m, x, c[N]; MI f[N], A[N], B[N];
	void slv(int S, int n) {
		if (n < 0) {
			A[S] = (S ? f[S - 1] : 1), f[S] += A[S] * c[S], B[S] = f[S];
			return;
		}
		slv(S, n - 1);
		CUP(i, S, S + (1 << n))
			f[i | 1 << n] += A[i] * c[i | 1 << n] - B[i];
		slv(S | 1 << n, n - 1);
		CUP(i, S, S + (1 << n))
			A[i | 1 << n] += A[i], B[i | 1 << n] += B[i];
	}
	int main() {
		cin >> n >> m;
		REP(i, 1, m) cin >> x, c[x] ++;
		m = (1 << n) - 1;
		REP(i, 0, n - 1) REP(j, 0, m)
			if (j >> i & 1) c[j] += c[j ^ 1 << i];
		slv(0, n - 1);
		cout << f[m] << '\n';
		REP(i, 0, m) cerr << f[i] << ' ';
		cerr << '\n';
		return 0;
	}
}
int main() {
	cin.tie(0)->sync_with_stdio(0);
	int T = 1;
	while (T --) Milkcat::main();
	return 0;
}