#include<bits/stdc++.h>
using namespace std;

#define endl '\n'
#define rep(i,n,m) for(ll i = (n); i < (ll)(m); i++)

namespace template_tute {
  using ll = long long;

  const ll INF = 4.1e18;

  template<typename T> T min(const vector<T>&v) { return *min_element(v.begin(), v.end()); }
  template<typename T> T max(const vector<T>&v) { return *max_element(v.begin(), v.end()); }
}

using namespace template_tute;

void solve() {
  ll n;
  cin >> n;
  vector<ll> l(n), r(n);
  rep(i, 0, n) cin >> l[i] >> r[i];
  vector<ll> d(n);
  rep(i, 0, n) {
    d[i] = r[i] - l[i] + 1;
  }
  if (min(d) == max(d) && min(d) % 2 == 0) {
    bool sw = true;
    ll len = min(d) / 2;
    rep(i, 0, n - 1) {
      if (abs(l[i] - l[i + 1]) >= len) {
        sw = false;
        break;
      }
    }
    if (sw) {
      cout << "YES" << endl;
      return;
    }
  }
  rep(k, 1, n + 1) {
    if (k * 2 > n) break;
    bool ch = false;
    rep(i, 0, k) {
      ll now = d[i];
      for (ll j = i + k; j < n; j += k) {
        if (j + k >= n) {
          if (now != d[j]) {
            ch = true;
          }
          break;
        }
        now = d[j] - now;
        if (now <= 0) {
          ch = true;
          break;
        }
      }
      if (ch) break;
    }
    if (ch) continue;
    vector<ll> xd(n), yd(n);
    rep(i, 0, n) {
      if (i < k) {
        xd[i] = d[i];
      } else {
        yd[i] = xd[i - k];
        if (i + k < n) {
          xd[i] = d[i] - yd[i];
        }
      }
    }
    assert(min(xd) >= 0 && min(yd) >= 0);
    rep(_, 0, 2) {
      bool sw = true;
      vector<ll> diffx, diffy;
      rep(i, 0, n - 1) {
        if (xd[i] > 0 && xd[i + 1] > 0) {
          ll l1 = l[i], r1 = l[i] + xd[i] - 1;
          ll l2 = l[i + 1], r2 = l[i + 1] + xd[i + 1] - 1;
          if (max(l1, l2) > min(r1, r2)) {
            sw = false;
            break;
          }
          diffx.push_back(l2 - l1);
        }
        if (yd[i] > 0 && yd[i + 1] > 0) {
          ll l1 = r[i] - yd[i] + 1, r1 = r[i];
          ll l2 = r[i + 1] - yd[i + 1] + 1, r2 = r[i + 1];
          diffy.push_back(l2 - l1);
          if (max(l1, l2) > min(r1, r2)) {
            sw = false;
            break;
          }
        }
      }
      if (diffx != diffy) sw = false;
      if (sw) {
        cout << "YES" << endl;
        return;
      }
      rep(i, 0, n) {
        swap(l[i], r[i]);
        l[i] *= -1;
        r[i] *= -1;
      }
    }
  }
  cout << "NO" << endl;
}

int main() {
  cin.tie(nullptr);
  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  while (T--) {
    solve();
  }
  return 0;
}