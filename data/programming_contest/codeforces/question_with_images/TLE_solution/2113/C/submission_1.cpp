#include <bits/stdc++.h>
using namespace std;
#define int long long
#define ld long double
#define rev(a) reverse(a.begin(),a.end())
#define s1(a) sort(a.begin(),a.end())
#define s2(a,n) sort(a,a+n)
#define cy cout << "YES" << endl;
#define cn cout << "NO" << endl;
#define g(x,y) __gcd(x,y)
#define minV(ans) *min_element(ans.begin(), ans.end())
#define maxV(ans) *max_element(ans.begin(), ans.end())
#define merge(v1,v2) v1.insert(v1.end(), v2.begin(), v2.end());


int gold(vector<vector<char>> mat, int r, int c, int n, int m, int k) {
   int side = 2 * k + 1 - 2;
   int golds = 0;
   int z = 0;
   for (int i = r; i <= min(r + side / 2, n - 1); i++) {
      for (int j = c; j <= min(c + side / 2, m - 1); j++) {
         if (mat[i][j] == 'g') { golds++; }
      }
   }
   for (int i = r - 1; i >= max(r - side / 2, z); i--) {
      for (int j = c; j <= min(c + side / 2, m - 1); j++) {
         if (mat[i][j] == 'g') { golds++; }
      }
   }
   for (int i = r; i <= min(r + side / 2, n - 1); i++) {
      for (int j = c-1; j >= max(c - side / 2, z); j--) {
         if (mat[i][j] == 'g') { golds++; }
      }
   }

   for (int i = r - 1; i >= max(r - side / 2, z); i--) {
      for (int j = c - 1; j >= max(c - side / 2, z); j--) {
         if (mat[i][j] == 'g') { golds++; }
      }
   }

   return golds;

}


void solve() {
   int n, m, k; cin >> n >> m >> k;
   vector<vector<char>> mat(n, vector<char>(m));
   int golds = 0;
   for (int i = 0; i < n; ++i)
   {
      for (int j = 0; j < m; ++j)
      {
         cin >> mat[i][j];
         if (mat[i][j] == 'g') { golds++; }
      }
   }
   int mini = INT_MAX;

   for (int i = 0; i < n; ++i)
   {
      for (int j = 0; j < m; ++j)
      {
         if (mat[i][j] == '.') { mini = min(mini, gold(mat, i, j, n, m, k)); }

      }
   }

   if (mini == INT_MAX) { cout << 0 << endl; }
   else {
      cout << golds - mini << endl;
   }


}



signed main()
{
#ifndef ONLINE_JUDGE
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
#endif
   ios_base::sync_with_stdio(false);
   cin.tie(0);
   cout.tie(0);
   int t;
   cin >> t;
   while (t--) solve();
   return 0;
}