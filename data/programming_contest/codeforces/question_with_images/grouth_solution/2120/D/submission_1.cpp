#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9+7;
const int N = 1e5+5;
int inv[N];

int main () {
  ios_base::sync_with_stdio(0); cin.tie(0);
  inv[1] = 1;
  for (int i = 2; i < N; i++) inv[i] = 1LL*(MOD-MOD/i)*inv[MOD % i] % MOD;

  int T;
  cin >> T;
  while (T--) {
    int a, b, k;
    cin >> a >> b >> k;
    const int64_t x = 1LL * (a-1) * k + 1;
    int xm = x % MOD;
    int c = 1;
    for (int i = 0; i < a; i++) {
      c = 1LL * c * (xm-i) % MOD * inv[i+1] % MOD;
    }
    c = (1LL * c * (b-1) % MOD * k % MOD + 1) % MOD;
    if (c < 0) c += MOD;
    cout << xm << ' ' << c << '\n';
  }
}
