#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;
const int MAX_A = 1 << 20; // 2^20
const int MAX_N = 400005;

int n, a[MAX_N], ans[MAX_N];

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    vector<long long> product(MAX_A, 1); // Product for each value
    for (int k = 1; k <= n; ++k) {
        int current_value = a[k];
        long long result = product[current_value];

        // For all i <= k, check if (a[i] | a[k]) == a[k]
        for (int i = 1; i < k; ++i) {
            if ((a[i] | current_value) == current_value) {
                result = (result * a[i]) % MOD;
            }
        }

        cout << result << '\n';

        // Update the product for current_value for future k's
        product[current_value] = (product[current_value] * current_value) % MOD;
    }
    
    return 0;
}
