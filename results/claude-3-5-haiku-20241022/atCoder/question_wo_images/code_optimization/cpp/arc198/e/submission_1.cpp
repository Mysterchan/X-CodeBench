#include <bits/stdc++.h>
#define REP(i, l, r) for (int i = (l); i <= (r); ++ i)
#define CUP(i, l, r) for (int i = (l); i < (r); ++ i)
using namespace std;

namespace math {
	typedef long long LL;
	template <class T> T qpow(T a, LL b) { if (!b) return {1}; T rs = a; b --; for (; b; b >>= 1, a = a * a) if (b & 1) rs = rs * a; return rs; }
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
		friend istream &operator >> (istream &is, mint &a) { LL x; is >> x, a = x; return is; }
		friend ostream &operator << (ostream &os, const mint &a) { os << a.v; return os; }
	};
	template <> unsigned mint<0>::mod = 998244353;
}

using namespace math;
typedef mint<998244353> MI;

int n, m, x, c[1 << 24];
MI f[1 << 24], A[1 << 24], B[1 << 24];

void slv(int S, int n) {
	if (n < 0) {
		A[S] = (S ? f[S - 1] : 1);
		f[S] += A[S] * c[S];
		B[S] = f[S];
		return;
	}
	slv(S, n - 1);
	int bit = 1 << n;
	CUP(i, S, S + bit)
		f[i | bit] += A[i] * c[i | bit] - B[i];
	slv(S | bit, n - 1);
	CUP(i, S, S + bit) {
		A[i | bit] += A[i];
		B[i | bit] += B[i];
	}
}

int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin >> n >> m;
	REP(i, 1, m) cin >> x, c[x] ++;
	m = (1 << n) - 1;
	REP(i, 0, n - 1) REP(j, 0, m)
		if (j >> i & 1) c[j] += c[j ^ 1 << i];
	slv(0, n - 1);
	cout << f[m] << '\n';
	return 0;
}