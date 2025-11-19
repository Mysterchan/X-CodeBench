
#include <bits/stdc++.h>

using namespace std;

#ifdef LOCAL
#include "algo/debug.h"
#else
#define debug(...) 42
#endif

template<typename T>
T extgcd(T a, T b, T &x, T &y) {
  if (a == 0) {
    x = 0;
    y = 1;
    return b;
  }
  T p = b / a;
  T g = extgcd(b - p * a, a, y, x);
  x -= p * y;
  return g;
}

template<typename T>
bool diophantine(T a, T b, T c, T &x, T &y, T &g) {
  if (a == 0 && b == 0) {
    if (c == 0) {
      x = y = g = 0;
      return true;
    }
    return false;
  }
  if (a == 0) {
    if (c % b == 0) {
      x = 0;
      y = c / b;
      g = abs(b);
      return true;
    }
    return false;
  }
  if (b == 0) {
    if (c % a == 0) {
      x = c / a;
      y = 0;
      g = abs(a);
      return true;
    }
    return false;
  }
  g = extgcd(a, b, x, y);
  if (c % g != 0) {
    return false;
  }
  T dx = c / a;
  c -= dx * a;
  T dy = c / b;
  c -= dy * b;
  x = dx + (T) ((__int128) x * (c / g) % b);
  y = dy + (T) ((__int128) y * (c / g) % a);
  g = abs(g);
  return true;
}

bool crt(int64_t k1, int64_t m1, int64_t k2, int64_t m2, int64_t &k, int64_t &m) {
  k1 %= m1;
  if (k1 < 0) k1 += m1;
  k2 %= m2;
  if (k2 < 0) k2 += m2;
  int64_t x, y, g;
  if (!diophantine(m1, -m2, k2 - k1, x, y, g)) {
    return false;
  }
  int64_t dx = m2 / g;
  int64_t delta = x / dx - (x % dx < 0);
  k = m1 * (x - dx * delta) + k1;
  m = m1 / g * m2;
  assert(0 <= k && k < m);
  return true;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int tt;
  cin >> tt;
  while (tt--) {
    int64_t n, x, y, vx, vy;
    cin >> n >> x >> y >> vx >> vy;
    auto A = n * vy;
    auto B = -n * vx;
    auto C = x * vy - y * vx;
    int64_t a0, b0, g;
    if (!diophantine(A, B, C, a0, b0, g)) {
      cout << -1 << '\n';
      continue;
    }
    auto delta_a = -B / g;
    auto delta_b = A / g;
    if (a0 <= 0) {
      auto r = (abs(a0) + delta_a) / delta_a;
      a0 += delta_a * r;
      b0 += delta_b * r;
    }
    if (b0 <= 0) {
      auto r = (abs(b0) + delta_b) / delta_b;
      a0 += delta_a * r;
      b0 += delta_b * r;
    }
    if (a0 > delta_a && b0 > delta_b) {
      auto r = min((a0 - 1) / delta_a, (b0 - 1) / delta_b);
      a0 -= r * delta_a;
      b0 -= r * delta_b;
    }
    if (a0 > 0 && b0 > 0) {
      cout << a0 + b0 + max(a0, b0) + ((a0 + b0 + 1) % 2) - 3 << '\n';
    } else {
      cout << -1 << '\n';
    }
  }
  return 0;
}
