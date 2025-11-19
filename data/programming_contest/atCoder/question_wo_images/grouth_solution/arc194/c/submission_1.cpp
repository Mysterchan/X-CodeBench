#include <bits/stdc++.h>

#define lowbit(x) ((x) & (-(x)))
using LL = long long;
const int V = 1e6;

struct BIT {
  int n; std::vector<LL> s;
  BIT(int n) : n(n), s(n + 1) {}
  void mdf(int x, int p) {
    for (; x <= n; x += lowbit(x)) s[x] += p;
  }
  LL qry(int x) {
    LL ans(0);
    for (; x; x -= lowbit(x)) ans += s[x];
    return ans;
  }
  LL qry(int l, int r) { return qry(r) - qry(l - 1); }
};

int main() {
  int n; scanf("%d", &n);
  std::vector<int> a(n), b(n), c(n);
  LL sum = 0;
  for (int &x : a) scanf("%d", &x);
  for (int &x : b) scanf("%d", &x);
  for (int &x : c) scanf("%d", &x);
  BIT s(V), t(V), ss(V), tt(V);
  std::vector<int> v;
  int cnt1 = 0, cnt2 = 0;
  LL s1 = 0, s2 = 0, tot = 0;
  for (int i = 0; i < n; i++) {
    if (a[i] && !b[i]) {
      s1 += s.qry(1, c[i]) + 1ll * ss.qry(c[i] + 1, V) * c[i];
      s.mdf(c[i], c[i]), ss.mdf(c[i], 1);
      ++cnt1;
    }
    if (!a[i] && b[i]) {
      s2 += t.qry(1, c[i]) + 1ll * tt.qry(c[i] + 1, V) * c[i] + c[i];
      t.mdf(c[i], c[i]), tt.mdf(c[i], 1);
      ++cnt2;
    }
    if (a[i] && b[i]) v.push_back(c[i]), sum += c[i];
  }
  LL cur = 0;
  std::sort(v.begin(), v.end(), std::greater<int>());
  LL ans = s1 + sum * (cnt1 + cnt2) + s2;
  for (auto x : v) {
    s1 += s.qry(1, x) + 1ll * ss.qry(x + 1, V) * x;
    s.mdf(x, x), ss.mdf(x, 1);
    sum -= x, ++cnt1;

    s2 += t.qry(1, x) + 1ll * tt.qry(x + 1, V) * x + x;
    t.mdf(x, x), tt.mdf(x, 1);
    ++cnt2;
    ans = std::min(ans, s1 + sum * (cnt1 + cnt2) + s2);
  }
  printf("%lld\n", ans);
} 