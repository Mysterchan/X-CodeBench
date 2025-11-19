#include<bits/stdc++.h>
using namespace std;
#define ll long long
const int MAXN = 200005, MOD = 998244353;

ll ksm(ll a, int b) {
    ll r = 1;
    while (b) {
        if (b & 1) r = r * a % MOD;
        a = a * a % MOD;
        b >>= 1;
    }
    return r;
}

ll inf[MAXN], fac[MAXN];

void precompute() {
    inf[0] = fac[0] = 1;
    for (int i = 1; i < MAXN; i++) {
        fac[i] = fac[i - 1] * i % MOD;
        inf[i] = ksm(fac[i], MOD - 2);
    }
}

void solve() {
    int n;
    cin >> n;
    vector<int> a(n + 1);
    
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }
    
    vector<int> b(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        b[min(i, n + 1 - i)]++;
    }
    
    ll ans = 1, c = 0;
    for (int i = n; i >= 1; i--) {
        c += b[i];
        ans = ans * inf[a[i]] % MOD;
        
        while (a[i] > 0) {
            ans = ans * c % MOD;
            a[i]--;
            c--;
        }
    }
    
    cout << (c == 0 ? ans : 0) << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    precompute();
    
    int T;
    cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}