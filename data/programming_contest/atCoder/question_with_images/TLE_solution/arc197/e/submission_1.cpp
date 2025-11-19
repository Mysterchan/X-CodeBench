#include <bits/stdc++.h>
#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2")
#define int long long
#define pii pair<int,int>
#define vi vector<int>
#define ff first
#define ss second
#define sp << " " <<
#define all(x) x.begin(),x.end()
#define big(x) ((int)(x.size()))
using namespace std;
const int MOD = 998244353, LIM = 1e6+1, inf = 2e9;

const int N = 1e5+1;
int add(int x,int y) {
    if ((x + y) >= MOD) return x + y - MOD;
    return x + y;
}

int mult(int x,int y) {
    return (1LL * x * y) % MOD;
}

int s(int x) {
    if (x%2) return mult(x,(x+1)/2);
    return mult(x/2,x+1);
}
void solve() {
    int n,h,w;
    cin >> n >> h >> w;
    if (h < 2*n || w<2*n) {
        cout << 0 << '\n';
        return;
    }
    int todos = mult(mult(s(w-2*n+1),s(w-2*n+1)),mult(s(h-2*n+1),s(h-2*n+1)));
    int minush = 0,minusw = 0;
    for (int j = 1;j<=h-2*n;j++) {
        minush=add(minush,mult(j,s(h-2*n+1-j)));
    }
    for (int j = 1;j<=w-2*n;j++) {
        minusw=add(minusw,mult(j,s(w-2*n+1-j)));
    }
    todos=add(todos,MOD-mult(2,mult(minush,minusw)));
    cout << todos << '\n';
} 

signed main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    #ifdef Dodi
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    #endif
    int t = 1;
    cin >> t;
    while (t --> 0) solve();
}