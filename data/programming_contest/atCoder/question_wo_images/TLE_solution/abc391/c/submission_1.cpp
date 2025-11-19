#include <bits/stdc++.h>
using namespace std;

using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)(n); i++)
#define all(x) (x).begin(), (x).end()

int main() {
  ll n, q;
  cin >> n >> q;

  vector<ll> pigeons(n + 1);
  for (ll i = 1; i <= n; i++) {
    pigeons[i] = i;
  }

  vector<ll> count(n + 1);
  for (ll i = 1; i <= n; i++) {
    count[i] = 1;
  }

  for (ll i = 0; i < q; i++) {
    char c;
    cin >> c;
    if (c == '1') {
      ll p, h;
      cin >> p >> h;

      count[pigeons[p]]--;

      pigeons[p] = h;

      count[h]++;
    } else {
      ll doubleCount = 0;
      for (ll i = 1; i <= n; i++) {
        if (count[i] > 1) {
          doubleCount++;
        }
      }
      cout << doubleCount << endl;
    }
  }
  return 0;
}
