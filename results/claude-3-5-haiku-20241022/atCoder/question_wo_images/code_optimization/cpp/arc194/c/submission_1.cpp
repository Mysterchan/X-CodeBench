#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define vll vector<ll>

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(0);
    
    int n; cin >> n;
    vector<int> a(n), b(n), c(n);
    for(int i = 0; i < n; i++) cin >> a[i];
    for(int i = 0; i < n; i++) cin >> b[i];
    for(int i = 0; i < n; i++) cin >> c[i];
    
    if(a == b) {
        cout << 0 << '\n';
        return 0;
    }
    
    vll d, u, both;
    for(int i = 0; i < n; i++) {
        if(a[i] == 0 && b[i] == 1) u.push_back(c[i]);
        else if(a[i] == 1 && b[i] == 0) d.push_back(c[i]);
        else if(a[i] == 1 && b[i] == 1) both.push_back(c[i]);
    }
    
    sort(both.begin(), both.end());
    const int N = both.size();
    
    vll pre(N + 1, 0);
    for(int i = 0; i < N; i++) {
        pre[i + 1] = pre[i] + both[i];
    }
    
    sort(d.rbegin(), d.rend());
    sort(u.rbegin(), u.rend());
    
    const int D = d.size(), U = u.size();
    vll d_cost(D + 1, 0), u_cost(U + 1, 0);
    for(int i = 0; i < D; i++) {
        d_cost[i + 1] = d_cost[i] + (ll)i * d[i];
    }
    for(int i = 0; i < U; i++) {
        u_cost[i + 1] = u_cost[i] + (ll)(i + 1) * u[i];
    }
    
    ll res = LLONG_MAX;
    
    for(int k = 0; k <= N; k++) {
        int extra = N - k;
        ll now = (ll)(D + U + 2 * extra) * pre[k];
        
        now += d_cost[D];
        now += u_cost[U];
        
        for(int i = 0; i < extra; i++) {
            now += (ll)(D + i) * both[k + i];
            now += (ll)(U + i + 1) * both[k + i];
        }
        
        res = min(res, now);
    }
    
    cout << res << '\n';
    return 0;
}