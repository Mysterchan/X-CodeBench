#include<bits/stdc++.h>
using namespace std;

#define M 1000000007LL
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define RFOR(i,a,b) for(int i=(a);i>=(b);--i)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define debug(x) cout<<(x)<<endl

typedef long long L;
typedef tuple<L,L,L> T;

int main(){
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(NULL);
    
    int t; cin >> t;
    vector<T> q(t);
    int x = 0;

    for(auto &z : q){
        L a, b, c;
        cin >> a >> b >> c;
        z = {a, b, c};
        x = max(x, int(a));
    }

    vector<L> y(x + 2);
    y[1] = 1;
    FOR(i, 2, x + 1) y[i] = (M - M / i * y[M % i] % M) % M;

    auto C = [&](L n, int r) -> L {
        L u = 1;
        FOR(i, 1, r) {
            L v = (n - r + i) % M;
            u = u * v % M;
            u = u * y[i] % M;
        }
        return u;
    };

    auto solve = [&](L a, L b, L c){
        L n = (a - 1) * c + 1;
        L u = C(n, int(a));
        L v = ((b - 1) % M) * (c % M) % M;
        v = (v * u + 1) % M;
        cout << n % M << " " << v << "\n";
    };

    while(t--){
        auto[a,b,c] = q[t];
        solve(a,b,c);
    }
    return 0;
}
