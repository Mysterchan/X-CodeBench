#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int tc;
    cin >> tc;
    
    while (tc--) {
        int n;
        cin >> n;
        n -= 2;  // Adjusting for good cells
        
        vector<int> U(n), D(n), L(n), R(n);
        for (int& x : U) cin >> x;
        for (int& x : D) cin >> x;
        for (int& x : L) cin >> x;
        for (int& x : R) cin >> x;
        
        const ll INF = 1e18;
        
        auto solve = [&](const vector<int>& a, const vector<int>& b) {
            vector<ll> pre_min(a.size());
            ll min_so_far = INF;
            for (int i = 0; i < a.size(); ++i) {
                pre_min[i] = a[i] + min_so_far;
                min_so_far = min(min_so_far, (ll)a[i]);
            }

            ll result = INF;
            min_so_far = INF;
            for (int i = 0; i < b.size(); ++i) {
                min_so_far = min(min_so_far, (ll)b[i]);
                result = min(result, pre_min[i] + min_so_far);
            }
            return result;
        };

        ll best = INF;
        
        for (int rotation = 0; rotation < 2; ++rotation) {
            best = min(best, solve(L, R) + solve(U, D));
            rotate(L.begin(), L.begin() + 1, L.end());
            rotate(R.begin(), R.begin() + 1, R.end());
            rotate(U.begin(), U.begin() + 1, U.end());
            rotate(D.begin(), D.begin() + 1, D.end());
        }
        
        cout << best << '\n';
    }
}