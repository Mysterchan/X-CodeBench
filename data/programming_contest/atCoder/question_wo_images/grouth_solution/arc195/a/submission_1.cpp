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

bool solve(){
    int n,m;
    cin >> n >> m;
    vector <int> a(n + 1),b(m + 2);
    vector <int> pre(n + 1),suf(n + 1);
    for(int i = 1;i <= n;i ++) cin >> a[i];
    for(int i = 1;i <= m;i ++) cin >> b[i];
    b[0] = b[m + 1] = -1;
    for(int i = 1;i <= n;i ++){
        pre[i] = pre[i - 1];
        if(a[i] == b[pre[i] + 1]) pre[i] ++;
    }
    suf[n + 1] = m + 1;
    for(int i = n;i >= 1;i --){
        suf[i] = suf[i + 1];
        if(a[i] == b[suf[i] - 1]) suf[i] --;
    }
    for(int i = 1;i < n;i ++){
        if(pre[i] >= suf[i + 1]) return 1;
    }
    return 0;
}

int main(){
    ios::sync_with_stdio(false);
    cout << (solve() ? "Yes" : "No") << '\n';
    return 0;
}