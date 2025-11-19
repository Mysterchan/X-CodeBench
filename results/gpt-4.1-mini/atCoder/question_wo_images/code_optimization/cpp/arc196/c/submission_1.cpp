#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int P = 998244353;

struct mint {
  int d;
  mint() : d(0) {}
  mint(int x) : d(x < 0 ? x + P : x >= P ? x - P : x) {}
  mint(ll x) : d(int((x % P + P) % P)) {}
  explicit operator int() const { return d; }
  mint& operator+=(const mint& rhs) {
    d += rhs.d;
    if (d >= P) d -= P;
    return *this;
  }
  mint& operator-=(const mint& rhs) {
    d -= rhs.d;
    if (d < 0) d += P;
    return *this;
  }
  mint& operator*=(const mint& rhs) {
    d = int((ll)d * rhs.d % P);
    return *this;
  }
  friend mint operator+(mint lhs, const mint& rhs) { return lhs += rhs; }
  friend mint operator-(mint lhs, const mint& rhs) { return lhs -= rhs; }
  friend mint operator*(mint lhs, const mint& rhs) { return lhs *= rhs; }
  static mint qpow(mint a, ll b) {
    mint res = 1;
    while (b > 0) {
      if (b & 1) res *= a;
      a *= a;
      b >>= 1;
    }
    return res;
  }
  mint inv() const { return qpow(*this, P - 2); }
  mint& operator/=(const mint& rhs) { return *this *= rhs.inv(); }
  friend mint operator/(mint lhs, const mint& rhs) { return lhs /= rhs; }
};

struct poly : vector<mint> {
  using vector<mint>::vector;
  void ntt(bool inv) {
    int n = (int)size();
    static vector<int> rev;
    if ((int)rev.size() != n) {
      rev.assign(n, 0);
      int lg = __builtin_ctz(n);
      for (int i = 0; i < n; i++) {
        rev[i] = (rev[i >> 1] >> 1) | ((i & 1) << (lg - 1));
      }
    }
    for (int i = 0; i < n; i++) {
      if (i < rev[i]) swap((*this)[i], (*this)[rev[i]]);
    }
    for (int len = 1; len < n; len <<= 1) {
      mint wlen = mint(3).inv().pow((P - 1) / (len << 1));
      if (!inv) wlen = wlen.inv();
      for (int i = 0; i < n; i += (len << 1)) {
        mint w = 1;
        for (int j = 0; j < len; j++) {
          mint u = (*this)[i + j], v = (*this)[i + j + len] * w;
          (*this)[i + j] = u + v;
          (*this)[i + j + len] = u - v;
          w *= wlen;
        }
      }
    }
    if (inv) {
      mint inv_n = mint(n).inv();
      for (auto& x : *this) x *= inv_n;
    }
  }
  poly operator*(const poly& b) const {
    int n = (int)size(), m = (int)b.size();
    int sz = 1;
    while (sz < n + m - 1) sz <<= 1;
    poly A(sz), B(sz);
    for (int i = 0; i < n; i++) A[i] = (*this)[i];
    for (int i = 0; i < m; i++) B[i] = b[i];
    A.ntt(false);
    B.ntt(false);
    for (int i = 0; i < sz; i++) A[i] *= B[i];
    A.ntt(true);
    A.resize(n + m - 1);
    return A;
  }
};

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  string S;
  cin >> n >> S;
  S = " " + S;

  // If first vertex is white or last vertex is black, no solution
  if (S[1] == 'W' || S[2 * n] == 'B') {
    cout << 0 << "\n";
    return 0;
  }

  // pre[i] = number of black vertices before the i-th white vertex
  vector<int> pre(n + 1, 0);
  int wcnt = 0, bcnt = 0;
  for (int i = 1; i <= 2 * n; i++) {
    if (S[i] == 'W') {
      wcnt++;
      pre[wcnt] = bcnt;
    } else {
      bcnt++;
    }
  }

  // Precompute factorials and inverse factorials
  vector<mint> fact(n + 1), invfact(n + 1);
  fact[0] = 1;
  for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i;
  invfact[n] = fact[n].inv();
  for (int i = n - 1; i >= 0; i--) invfact[i] = invfact[i + 1] * (i + 1);

  auto slv = [&](int x, int y) -> mint {
    // y! / (y - x)!
    if (x > y) return 0;
    return fact[y] * invfact[y - x];
  };

  vector<mint> f(n + 1, 0);
  for (int i = 1; i <= n; i++) {
    if (pre[i] <= i) {
      f[i] = slv(pre[i], i);
    }
  }

  vector<mint> sum(n + 1, 0);

  // Divide and conquer optimization
  function<void(int, int)> solve = [&](int l, int r) {
    if (l == r) return;
    int mid = (l + r) >> 1;
    solve(l, mid);
    for (int i = l; i <= mid; i++) {
      sum[pre[i]] += f[i];
    }
    if (pre[l] <= r) {
      // Build polynomials for convolution
      // sum[pre[l]..pre[mid]] * fact[0..r - pre[l]]
      int len1 = pre[mid] - pre[l] + 1;
      int len2 = r - pre[l] + 1;
      if (len1 > 0 && len2 > 0) {
        poly A(len1), B(len2);
        for (int i = 0; i < len1; i++) A[i] = sum[pre[l] + i];
        for (int i = 0; i < len2; i++) B[i] = fact[i];
        poly res = A * B;
        for (int i = mid + 1; i <= r; i++) {
          if (i >= pre[i]) {
            int idx = i - pre[l];
            if (idx < (int)res.size()) {
              f[i] -= res[idx] * invfact[i - pre[i]];
            }
          }
        }
      }
    }
    for (int i = l; i <= mid; i++) {
      sum[pre[i]] = 0;
    }
    solve(mid + 1, r);
  };

  solve(1, n);

  cout << int(f[n]) << "\n";

  return 0;
}