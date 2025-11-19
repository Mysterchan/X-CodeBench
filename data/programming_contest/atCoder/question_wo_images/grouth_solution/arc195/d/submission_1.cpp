#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ldb;
const int INF = 0x3f3f3f3f;
const ll LLINF = 0x3f3f3f3f3f3f3f3f;
const ldb eps = 1e-14;
const ldb pi = acos(-1.0);
const int P = 998244353;
const int N = 1000005;

void solve(){
    int n; cin >> n;
    vector <int> a(n + 1);
    vector <int> f(n + 1,0);
    for(int i = 1;i <= n;i ++) cin >> a[i];
    for(int i = 1;i <= n;i ++){
        vector <int> swp;
        int to = n + 1;
        for(int j = i;j + 1 <= n;j += 2){
            if(a[j] == a[j + 1]){
                to = j + 1; break;
            }
            if(j + 2 <= n && a[j] == a[j + 2]){
                swap(a[j + 1],a[j + 2]);
                swp.push_back(j + 1);
            }
            else break;
        }
        for(auto x : swp) swap(a[x],a[x + 1]);
        if(to <= n) f[to] = max(f[to],f[i] + 1);
        if(i < n) f[i + 1] = max(f[i + 1],f[i] + (a[i] == a[i + 1]));
    }
    cout << n - f[n] << '\n';
}

int main(){
    ios::sync_with_stdio(false);
    int TC;
    cin >> TC;
    while(TC --){
        solve();
    }
    return 0;
}