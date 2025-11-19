#include <bits/stdc++.h>
#define int long long
using namespace std;

const int MOD = 998244353;

int main() {
    int n;
    cin >> n;
    vector<int> a(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }
    
    // Initialize limits and counts
    int left = 1, right = n, count_fixed = 0;
    for (int i = 1; i <= n; i++) {
        if (a[i] != -1) {
            if (a[i] < left || a[i] > right || (a[i] == i + 1) || (a[i] == i - 1)) {
                cout << 0 << endl;
                return 0;
            }
            count_fixed++;
            left = max(left, a[i] + 1);
            right = min(right, a[i] - 1);
        }
    }
    
    // Check condition for fixed values
    if (count_fixed > 1) {
        cout << 0 << endl;
        return 0;
    }

    // Calculate the number of ways to fill -1s
    int ways = 1;
    for (int i = left; i <= right; i++) {
        if (a[i] == -1) {
            if (i == 1 || a[i - 1] == -1) {
                ways = (ways * (n - 1)) % MOD; // Two options
            } else {
                ways = (ways * n) % MOD; // One option
            }
        }
    }

    cout << ways << endl;
    return 0;
}
