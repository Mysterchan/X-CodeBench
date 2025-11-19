#include <bits/stdc++.h>
using namespace std;

const int P = 998244353;

struct mint {
  int d;
  mint() = default;
  mint(int x) : d(x < 0 ? x + P : x) {}
  mint(ll x) : d(int(x % P)) {}
  explicit operator int() { return d; }
  friend ostream &operator<<(ostream &x, mint y) { return x << y.d; }
  friend mint operator+(mint x, mint y) {
    return (x.d += y.d) < P ? x.d : x.d - P;
  }
  mint &operator+=(mint z) { return (d += z.d) < P ? d : d -= P, *this; }
  friend mint operator-(mint x, mint y) {
    return (x.d -= y.d) < 0 ? x.d + P : x.d;
  }
  mint &operator-=(mint z) { return (d -= z.d) < 0 ? d += P : d, *this; }
  friend mint operator*(mint x, mint y) { return (long long)x.d * y.d % P; }
  mint &operator*=(mint z) { return d = (long long)d * z.d % P, *this; }
  static mint qpow(int x, long long y = P - 2) {
    int z = 1;
    for (; y; y >>= 1, x = (long long)x * x % P)
      if (y & 1) z = (long long)x * z % P;
    return z;
  }
  friend mint operator/(mint x, mint y) { return x *= qpow(y.d); }
  mint inv() { return qpow(d); }
};

struct poly : vector<mint> {
  poly() = default;
  poly(int x) { resize(x); }
  poly(const initializer_list<mint> &s) : vector<mint>(s) {}
  template <typename T>
  poly(T a, T b) : vector<mint>(a, b) {}
  
  friend void NTT(poly &A, int T) {
    int S = A.size();
    for (int i = 1, j = 0; i < S - 1; i++) {
      for (int k = S >> 1; (j ^= k) < k; k >>= 1);
      if (i < j) swap(A[i], A[j]);
    }
    mint W, x, y;
    for (int len = 1; len < S; len <<= 1) {
      W = mint(3).qpow((P - 1) / (len << 1));
      if (!T) W = W.inv();
      for (int L = 0; L < S; L += len << 1) {
        mint pw = 1;
        for (int k = 0; k < len; k++, pw *= W) {
          x = A[L + k], y = A[L + len + k] * pw;
          A[L + k] = x + y, A[L + len + k] = x - y;
        }
      }
    }
  }
  
  friend poly operator*(poly a, poly b) {
    int n = a.size() - 1, m = b.size() - 1, S = 1;
    while (S <= n + m) S <<= 1;
    a.resize(S), b.resize(S);
    NTT(a, 1), NTT(b, 1);
    for (int i = 0; i < S; i++) a[i] *= b[i];
    NTT(a, 0);
    mint Inv = mint(S).inv();
    a.resize(n + m + 1);
    for (int i = 0; i <= n + m; i++) a[i] *= Inv;
    return a;
  }
};

int main() {
  ios::sync_with_stdio(0), cin.tie(0);

  int n;
  string S;
  cin >> n >> S;

  if (S[0] == 'W' || S[2 * n - 1] == 'B') {
    cout << "0\n";
    return 0;
  }

  int s1 = 0, s2 = 0;
  vector<int> pre(n + 1);
  for (int i = 0; i < 2 * n; i++) {
    if (S[i] == 'W') pre[++s1] = s2;
    else s2++;
  }

  poly jie(n + 1, 1), ni(n + 1);
  for (int i = 1; i <= n; i++) jie[i] = jie[i - 1] * i;
  ni[n] = jie[n].inv();
  for (int i = n; i >= 1; i--) ni[i - 1] = ni[i] * i;

  poly f(n + 1), sum(n + 1);
  for (int i = 1; i <= n; i++) 
    if (pre[i] <= i) f[i] = jie[i] * ni[i - pre[i]];

  function<void(int, int)> solve = [&](int l, int r) {
    if (l == r) return;
    int mid = (l + r) >> 1;
    solve(l, mid);
    
    for (int i = l; i <= mid; i++) sum[pre[i]] += f[i];
    
    if (pre[l] <= r) {
      int len1 = pre[mid] - pre[l] + 1, len2 = r - pre[l] + 1;
      poly a(len1), b(len2);
      for (int i = 0; i < len1; i++) a[i] = sum[pre[l] + i];
      for (int i = 0; i < len2; i++) b[i] = jie[i];
      poly res = a * b;
      for (int i = mid + 1; i <= r; i++)
        if (i >= pre[i]) f[i] -= res[i - pre[l]] * ni[i - pre[i]];
    }
    
    for (int i = pre[l]; i <= pre[mid]; i++) sum[i] = 0;
    solve(mid + 1, r);
  };
  
  solve(1, n);
  cout << f[n] << '\n';
}