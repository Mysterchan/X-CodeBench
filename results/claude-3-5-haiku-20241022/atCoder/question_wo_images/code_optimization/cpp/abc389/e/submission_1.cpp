#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ll n, m; 
    cin >> n >> m;
    vector<ll> p(n);
    for(int i = 0; i < n; i++) cin >> p[i];
    
    sort(p.begin(), p.end());
    
    auto cost = [&](ll total) -> ll {
        ll remaining = total;
        ll sum = 0;
        for(int i = 0; i < n && remaining > 0; i++){
            ll k = min(remaining, (ll)sqrt(m / p[i]) + 10);
            ll low = 0, high = k;
            while(high - low > 1){
                ll mid = (low + high + 1) / 2;
                if(mid * mid * p[i] <= m) low = mid;
                else high = mid - 1;
            }
            if(high * high * p[i] <= m) k = high;
            else k = low;
            
            k = min(k, remaining);
            if(sum > m - k * k * p[i]) return m + 1;
            sum += k * k * p[i];
            remaining -= k;
        }
        return sum;
    };
    
    ll left = 0, right = 2e9;
    while(left < right){
        ll mid = (left + right + 1) / 2;
        if(cost(mid) <= m) left = mid;
        else right = mid - 1;
    }
    
    cout << left << endl;
    return 0;
}