#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ll n, m;
    cin >> n >> m;
    vector<ll> p(n);
    for (ll i = 0; i < n; i++) {
        cin >> p[i];
    }

    // Sort the product prices
    sort(p.begin(), p.end());

    ll total_units = 0;
    for (ll i = 0; i < n; i++) {
        ll price_per_unit = p[i];
        ll max_k = sqrt(m / price_per_unit); // maximum units we can buy of this type of product
        ll cost = max_k * max_k * price_per_unit; // cost for buying max_k units
        if (cost <= m) {
            total_units += max_k; // We can buy max_k units of this product
            m -= cost; // Reduce the budget
        } else {
            // If we can't buy all max_k, find the maximum we can buy with remaining budget
            ll left = 0, right = max_k;
            while (left < right) {
                ll mid = (left + right + 1) / 2;
                if (mid * mid * price_per_unit <= m) {
                    left = mid; // mid is valid, try for more
                } else {
                    right = mid - 1; // mid is too much
                }
            }
            total_units += left;
            break; // No budget left to buy more units
        }
    }

    cout << total_units << endl;
    return 0;
}