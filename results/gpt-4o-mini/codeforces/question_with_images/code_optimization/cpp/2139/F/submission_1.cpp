#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <map>

const int MOD = 1'000'000'007;

void solve() {
    int n, m, q;
    std::cin >> n >> m >> q;

    std::vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }

    std::vector<std::pair<int, long long>> ops(q);
    for (int i = 0; i < q; ++i) {
        std::cin >> ops[i].first >> ops[i].second;
    }

    std::vector<long long> sum_f(n, 0);
    std::vector<long long> total_f(n, 0);

    for (int i = 0; i < q; ++i) {
        int idx = ops[i].first - 1;
        long long x = ops[i].second;

        for (int j = idx; j < n; ++j) {
            if (j == idx) {
                // For the slider that is currently moving
                if (j > 0 && a[j - 1] >= x) {
                    x = a[j - 1] + 1;
                }
                sum_f[j] += x;
                total_f[j]++;
                a[j] = x; // Move the current slider to new position
            } else {
                // For the sliders down the track
                if (a[j] <= x) {
                    sum_f[j] += a[j];
                } else {
                    sum_f[j] += x;
                    x = a[j] + 1; // Push right
                }
                total_f[j]++;
                a[j] = x;
            }
        }
        // Restore positions for next operation simulation
        for (int j = 0; j < n; ++j) {
            a[j] = a[j - 1] + (j > 0);
        }
    }

    for (int j = 0; j < n; ++j) {
        long long result = (sum_f[j] + total_f[j] * (j + 1)) % MOD;
        std::cout << result << (j + 1 == n ? "\n" : " ");
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t;
    std::cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}