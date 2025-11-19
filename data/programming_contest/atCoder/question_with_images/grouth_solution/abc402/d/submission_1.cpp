#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pll pair<ll, ll>
#define pii pair<int, int>
#define endl '\n'

void solve()
{
  int n, m;
  ll ans = 0;
  cin >> n >> m;
  vector<int> t(n);
  for (int i = 0; i < m; i++)
  {
    int a, b;
    cin >> a >> b;
    t[(a + b) % n]++;
  }

  for (int i = 0; i < n; i++)
  {
    ans += t[i] * (m - t[i]);
  }

  cout << ans / 2 << '\n';
}

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(0);
  int t;
  t = 1;
  while (t--)
  {
    solve();
  }
  return 0;
}