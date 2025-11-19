#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, d;
    cin >> n >> d;
    vector<int> t(n), l(n);
    for (int i = 0; i < n; ++i) cin >> t[i] >> l[i];

    // Precompute max thickness and max weight at k=0
    int max_t = 0;
    int max_weight_0 = 0;
    for (int i = 0; i < n; ++i) {
        max_t = max(max_t, t[i]);
        max_weight_0 = max(max_weight_0, t[i] * l[i]);
    }

    // For each k, max weight = max_weight_0 + max_t * k
    for (int k = 1; k <= d; ++k) {
        cout << max_weight_0 + max_t * k << "\n";
    }

    return 0;
}