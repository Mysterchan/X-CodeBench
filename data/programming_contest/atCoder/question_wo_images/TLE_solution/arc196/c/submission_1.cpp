#include <bits/stdc++.h>
#define V vector
#define Vi vector<int>
#define sz(a) ((int)a.size())
#define fi first
#define se second
#define Int pair<int, int>
#define Inf ((int)1e9)
#define pb push_back
#define ins insert
#define For(i, x, y) for (int i = (x); i <= (y); i++)
#define Rep(i, x, y) for (int i = (x); i >= (y); i--)
#define seg int p, int l, int r
#define lid p << 1, l, mid
#define all(a) a.begin(), a.end()
#define rid p << 1 | 1, mid + 1, r
#define mid ((l + r) / 2)
#define Ceil(x, y) (((x) + (y) - 1) / (y))
#define cmax(a, b) a = max(a, b)
#define cmin(a, b) a = min(a, b)
#define IO(x) freopen(#x ".in", "r", stdin), freopen(#x ".out", "w", stdout);
using namespace std;
#define ll long long
const int P = 998244353;
struct mint {
  int d;
  mint() = default;
  mint(int x) : d(x < 0 ? x + P : x) {}
  mint(ll x) : d(int(x % P)) {}
  explicit operator int() { return d; }
  friend istream &operator>>(istream &x, mint &y) { return x >> y.d; }
  friend ostream &operator<<(ostream &x, mint y) { return x << y.d; }
  friend mint operator+(mint x, mint y) {
    return (x.d += y.d) < P ? x.d : x.d - P;
  }
  mint &operator+=(mint z) { return (d += z.d) < P ? d : d -= P, *this; }
  friend mint operator-(mint x, mint y) {
    return (x.d -= y.d) < 0 ? x.d + P : x.d;
  }
  mint &operator-=(mint z) { return (d -= z.d) < 0 ? d += P : d, *this; }
  friend mint operator*(mint x, mint y) { return int(1ll * x.d * y.d % P); }
  mint &operator*=(mint z) { return d = int(1ll * d * z.d % P), *this; }
  static mint qpow(int x, ll y = P - 2) {
    int z = 1;
    for (; y; y >>= 1, x = int(1ll * x * x % P))
      if (y & 1) z = int(1ll * x * z % P);
    return z;
  }
  friend mint operator/(mint x, mint y) { return x *= qpow(y.d); }
  mint &operator/=(mint z) { return (*this) *= qpow(z.d); }
  mint inv() { return qpow(d); }
  mint pow(mint z) { return qpow(d, z.d); }
  mint pow(int z) { return z >= 0 ? qpow(d, z) : 1 / qpow(d, -z); }
  mint operator+() { return d; }
  mint operator-() { return P - d; }
};
mint operator""_m(unsigned ll x) { return mint(int(x)); }
struct poly : vector<mint> {
  poly() = default;
  poly(int x) { resize(x); }
  poly(const initializer_list<mint> &s) : std::vector<mint>(s) {}
  template <typename T>
  poly(T a, T b) : std::vector<mint>(a, b) {}
  friend void NTT(poly &A, int T) {
    int S = A.size();
    Vi cnt(S);
    for (int i = 0; i < S; i++) {
      cnt[i] = (cnt[i >> 1] >> 1) + (i & 1) * S / 2;
      if (i < cnt[i]) std::swap(A[i], A[cnt[i]]);
    }
    mint G = 3, Gi = G.inv();
    for (int len = 1; len < S; len *= 2) {
      mint W = (T ? G : Gi).pow((P - 1) / len / 2);
      V<mint> pw(len, 1);
      For(i, 1, len - 1) pw[i] = pw[i - 1] * W;
      for (int L = 0; L < S; L += len * 2) For(k, 0, len - 1) {
          mint x = A[L + k], y = A[L + len + k] * pw[k];
          A[L + k] = x + y, A[L + len + k] = x - y;
        }
    }
  }
  friend poly operator*(poly a, poly b) {
    int n = sz(a) - 1, m = sz(b) - 1, S;
    for (S = 2; S <= n + m; S *= 2);
    poly A(S), B(S);
    for (int i = 0; i <= n; i++) A[i] = a[i];
    for (int i = 0; i <= m; i++) B[i] = b[i];
    NTT(A, 1), NTT(B, 1);
    for (int i = 0; i < S; i++) A[i] *= B[i];
    NTT(A, 0);
    mint Inv = 1_m / S;
    B.resize(n + m + 1);
    for (int i = 0; i <= n + m; i++) B[i] = Inv * A[i];
    return B;
  }
};
int main() {
  ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);

  int n;
  string S;
  cin >> n >> S, S = " " + S;

  if (S[1] == 'W' || S[2 * n] == 'B') {
    cout << "0\n";
    return 0;
  }

  int s1 = 0, s2 = 0;
  Vi pre(n + 5);
  For(i, 1, 2 * n) {
    s1 += S[i] == 'W', s2 += S[i] == 'B';
    if (S[i] == 'W') pre[s1] = s2;
  }

  poly jie(n + 5, 1), ni(n + 5);
  For(i, 1, n) jie[i] = jie[i - 1] * i;
  ni[n] = jie[n].inv();
  Rep(i, n, 1) ni[i - 1] = ni[i] * i;

  auto slv = [&](int x, int y) { return jie[y] * ni[y - x]; };

  poly f(n + 5);
  For(i, 1, n) if (pre[i] <= i) {
    f[i] = slv(pre[i], i);
  }

  poly sum(n + 5);
  auto solve = [&](auto lf, int l, int r) -> void {
    if (l == r) return;
    lf(lf, l, mid);
    For(i, l, mid) sum[pre[i]] += f[i];
    if (pre[l] <= r) {
      poly res = (poly){&sum[pre[l]], &sum[pre[mid] + 1]} *
                 (poly){&jie[0], &jie[r - pre[l] + 1]};
      For(i, mid + 1, r) if (i >= pre[i]) f[i] -=
          res[i - pre[l]] * ni[i - pre[i]];
    }
    For(i, pre[l], pre[mid]) sum[i] = 0;
    lf(lf, mid + 1, r);
  };
  solve(solve, 1, n);

  cout << f[n] << '\n';
}