#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        long long s; int k;
        cin >> s >> k;

        // If s is divisible by k, no turns needed, power remains k
        if (s % k == 0) {
            cout << k << '\n';
            continue;
        }

        // We want to find the maximum power p (1 <= p <= k)
        // such that s can be represented as:
        // s = p * m + (p-1) * n, with m,n >= 1
        // This means s - p * m = (p-1) * n
        // => s - p * m divisible by (p-1)
        // and m,n >= 1 => m >= 1, n >= 1
        // Also, m <= k (since power decreases by 1 after each turn, max strokes with power p is p)
        // Actually, m can be any positive integer, but since s and k are large,
        // we just check for existence of m in [1, k] satisfying the divisibility.

        int ans = 1;
        for (int p = k; p >= 1; p--) {
            int d = p - 1;
            if (d == 0) {
                // p=1, no turns possible, must reach s by strokes of length 1
                if (s >= 1) {
                    ans = 1;
                    break;
                }
            } else {
                // Check if there exists m in [1, k] such that (s - p*m) % d == 0 and s - p*m >= d
                // Because n = (s - p*m)/d >= 1
                // So s - p*m >= d
                // So m <= (s - d)/p
                // Also m >= 1 and m <= k
                // So m in [1, min(k, floor((s - d)/p))]

                long long max_m = (s - d) / p;
                if (max_m < 1) continue;
                max_m = min((long long)k, max_m);

                // We want to find m in [1, max_m] such that (s - p*m) % d == 0
                // => s % d == (p*m) % d
                // Since p % d = 1 (because p = d + 1)
                // So (p*m) % d = m % d
                // So s % d == m % d
                // So m ≡ s mod d

                int rem = s % d;

                // Find m in [1, max_m] with m % d == rem
                // The smallest such m is:
                long long m_candidate = rem;
                if (m_candidate == 0) m_candidate = d;
                if (m_candidate <= max_m) {
                    ans = p;
                    break;
                }
            }
        }
        cout << ans << '\n';
    }
    return 0;
}