#include <bits/stdc++.h>
using namespace std;
using ll = long long;

void solve() {
    int n;
    cin >> n;
    vector<ll> a(n), b(n), c(n);
    
    ll sum_b = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i] >> b[i] >> c[i];
        sum_b += b[i];
    }
    
    auto check = [&](ll k) {
        ll div1 = 0, div2 = 0;
        for (int i = 0; i < n; i++) {
            // Allocate optimally for writer i
            // For Div.1: need min(A[i], allocated_B)
            // For Div.2: need min(C[i], remaining_B)
            // We want at least k from Div.1 total and k from Div.2 total
            
            ll max_div1 = min(a[i], b[i]);
            ll max_div2 = min(c[i], b[i]);
            
            // Greedy: try to balance or give priority
            ll use_div1 = min(max_div1, b[i]);
            ll use_div2 = min(max_div2, b[i] - use_div1);
            
            // Better: give to Div.1 as much as needed, rest to Div.2
            use_div1 = min({a[i], b[i], k - div1});
            use_div1 = max(0LL, use_div1);
            use_div2 = min({c[i], b[i] - use_div1, k - div2});
            use_div2 = max(0LL, use_div2);
            
            div1 += use_div1;
            div2 += use_div2;
        }
        return div1 >= k && div2 >= k;
    };
    
    ll l = 0, r = sum_b;
    while (l < r) {
        ll mid = (l + r + 1) / 2;
        if (check(mid)) {
            l = mid;
        } else {
            r = mid - 1;
        }
    }
    
    cout << l << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    
    return 0;
}