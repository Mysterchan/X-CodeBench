#include <bits/stdc++.h>
using namespace std;
using ll = long long;

static int ceilLog2(ll x) {
    int fl = 63 - __builtin_clzll(x);
    if ((1LL << fl) == x) return fl;
    return fl + 1;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        ll n, m, a, b;
        cin >> n >> m >> a >> b;

        int Fn      = ceilLog2(n);
        int Fm      = ceilLog2(m);
        int Fa      = ceilLog2(a);
        int Fna     = ceilLog2(n - a + 1);
        int Fb      = ceilLog2(b);
        int Fmb     = ceilLog2(m - b + 1);

        ll costHoriz = 1LL + ( ll(Fm) + ll(min(Fa, Fna)) );

        ll costVert  = 1LL + ( ll(Fn) + ll(min(Fb, Fmb)) );

        ll ans = min(costHoriz, costVert);
        cout << ans << "\n";
    }

    return 0;
}
