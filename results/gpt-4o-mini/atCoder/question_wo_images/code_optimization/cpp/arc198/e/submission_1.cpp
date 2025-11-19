#include <bits/stdc++.h>
using namespace std;
const int MOD = 998244353;
const int MAXN = 1 << 24;

int n, m, c[MAXN];
long long f[MAXN];

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    cin >> n >> m;
    int target = (1 << n) - 1;

    // Count occurrences of each s_i
    for (int i = 0; i < m; i++) {
        int x;
        cin >> x;
        c[x]++;
    }

    // Precompute contributions from lower bits
    for (int i = 0; i < n; i++) {
        for (int j = target; j >= 0; j--) {
            if (j >> i & 1) {
                c[j] += c[j ^ (1 << i)];
            }
        }
    }

    f[0] = 1; // There's one way to start at 0
    for (int S = 0; S <= target; S++) {
        if (f[S]) {
            for (int i = 0; i < m; i++) {
                int next = (S | (1 << i)) + 1; // Update x to next state
                if (next <= target) {
                    f[next] = (f[next] + f[S] * c[next]) % MOD;
                }
            }
        }
    }

    cout << f[target] << '\n';
    return 0;
}
