#include<bits/stdc++.h>
using namespace std;
#define endl '\n'
#define pii pair<int, int>
const int N = 1e2 + 7;
char s[N][N], t[N][N];
void solve(){
  int n, m;
   cin >> n >> m;
   for(int i = 1; i <= n; ++i)
    for(int j = 1; j <= n; ++j)cin >> s[i][j];
  for(int i = 1; i <= m; ++i)
    for(int j = 1; j <= m; ++j) cin >> t[i][j];
 
      for(int i = 1; i <= m; ++i){
        for(int j = 1; j <= m; ++j){
           for(int a = 1; a <= n - m + 1; ++a){
              for(int b = 1; b <= n - m + 1; ++b){
          if(s[a + i - 1][b + j - 1] == t[i][j]){
            cout << a << " " << b << endl;
            return ;
          }
        }
      }
    }
  }
  
}
signed main(){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int T = 1;
    while (T--) solve();
    return 0;
}