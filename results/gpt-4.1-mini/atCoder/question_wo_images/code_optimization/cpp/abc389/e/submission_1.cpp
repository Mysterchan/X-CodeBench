#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll n, m; cin >> n >> m;
    vector<ll> p(n);
    for (ll i = 0; i < n; i++) cin >> p[i];

    // We want to maximize sum of k_i such that sum(k_i^2 * p_i) <= m.
    // For each product i, cost = p_i * k_i^2.
    // Total cost = sum over i of p_i * k_i^2 <= m.

    // We can binary search on total units x = sum k_i.
    // For a fixed x, minimal cost is achieved by distributing units to minimize sum p_i * k_i^2.
    // Since cost is convex in k_i, minimal cost is when k_i proportional to 1/sqrt(p_i).
    // Specifically, k_i = floor(x / sum_j sqrt(p_j) * (1 / sqrt(p_i))).

    // To check feasibility for x:
    // 1. Compute sum_sqrt = sum sqrt(p_i)
    // 2. For each i, k_i = floor(x / sum_sqrt / sqrt(p_i))
    // 3. Compute cost = sum p_i * k_i^2
    // 4. If cost <= m, x is feasible.

    // Because k_i are integers, we may have leftover units to assign.
    // Assign leftover units one by one to the product with minimal incremental cost:
    // incremental cost for adding one unit to product i when k_i units are bought:
    // cost increase = p_i * (2*k_i + 1)

    // Implement binary search on x.

    vector<double> inv_sqrt_p(n);
    double sum_inv_sqrt = 0;
    for (ll i = 0; i < n; i++) {
        inv_sqrt_p[i] = 1.0 / sqrt((double)p[i]);
        sum_inv_sqrt += inv_sqrt_p[i];
    }

    auto can_buy = [&](ll x) -> bool {
        // Compute initial k_i
        vector<ll> k(n);
        ll sum_k = 0;
        __int128 cost = 0;
        for (ll i = 0; i < n; i++) {
            k[i] = (ll)((double)x * inv_sqrt_p[i] / sum_inv_sqrt);
            sum_k += k[i];
        }
        ll rem = x - sum_k;

        // Compute cost for initial k_i
        for (ll i = 0; i < n; i++) {
            __int128 val = (__int128)k[i] * k[i] * p[i];
            cost += val;
            if (cost > (__int128)m) return false;
        }

        if (rem == 0) return cost <= m;

        // Prepare min-heap for incremental cost of adding one unit
        // incremental cost = p_i * (2*k_i + 1)
        using T = pair<__int128, int>;
        priority_queue<T, vector<T>, greater<T>> pq;
        for (ll i = 0; i < n; i++) {
            __int128 inc = (__int128)p[i] * (2 * k[i] + 1);
            pq.emplace(inc, i);
        }

        for (ll i = 0; i < rem; i++) {
            auto [inc, idx] = pq.top();
            pq.pop();
            cost += inc;
            if (cost > (__int128)m) return false;
            k[idx]++;
            inc = (__int128)p[idx] * (2 * k[idx] + 1);
            pq.emplace(inc, idx);
        }
        return cost <= m;
    };

    ll left = 0, right = 2000000000; // upper bound guess (2e9)
    // Because max cost for 2e9 units with p_i=1 is (2e9)^2 * 1 = 4e18 > 1e18 max M,
    // so 2e9 is safe upper bound.

    while (left < right) {
        ll mid = left + (right - left + 1) / 2;
        if (can_buy(mid)) left = mid;
        else right = mid - 1;
    }

    cout << left << "\n";
    return 0;
}