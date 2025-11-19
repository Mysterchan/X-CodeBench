#include<bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
#define pii pair<int, int>
#define vi vector<int>
#define vii vector<vi>
#define lowbit(x) (x & (-x))
const int N = 4e5 + 5, inf = 0x3f3f3f3f;
int f[N], mx;

struct st{
  int l, r;
  bool operator < (const st & x)const{ return r < x.r;}
}a[N];

struct BIT{
    int n; vi tr;
    BIT(int n1 = 0){init(n1);}
    void init(int n1){
        n = n1;
        tr.assign(n + 1, 0);
    }

    void modify(int x, int k){
      for(int i = x; i; i -= lowbit(x))tr[i] = max(tr[i], k);
    }
    int query(int x){
      int res = 0;
      for(int i = x; i < n; i += lowbit(i))res = max(res, tr[i]);
      return res;
    }



}tr1;

void solve(){
  int n; cin >> n; int x, y; tr1.init(N);
  for(int i = 1; i <= n; ++i){
    cin >> x >> y;
    if(x > y)swap(x, y);
    a[i] = {x, y};
  }
 
  sort(a + 1, a + 1 + n);
  for(int i = 1; i <= n; ++i){
    int l = a[i].l;
    f[i] = tr1.query(l) + 1;
    tr1.modify(l, f[i]);
  }

  for(int i = 1; i <= n; ++i){
    f[i] += tr1.query(a[i].r);
    mx = max(mx, f[i]);
  }
  cout << mx << endl;
}
signed main() {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int T = 1;
    while(T--) solve();
    return 0;
}
