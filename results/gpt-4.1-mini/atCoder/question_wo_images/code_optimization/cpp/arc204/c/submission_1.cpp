#include <bits/stdc++.h>
using namespace std;

const int N = 300007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; cin >> n;
    vector<int> p(n);
    for (int i = 0; i < n; ++i) {
        cin >> p[i];
        --p[i];
    }

    vector<int> vis(n, 0);
    vector<int> cycles;
    int even_half_sum = 0;
    vector<int> cnt(n + 1, 0);

    // Find cycles and count even cycle halves
    for (int i = 0; i < n; ++i) {
        if (!vis[i]) {
            int c = 0;
            for (int j = i; !vis[j]; j = p[j]) {
                vis[j] = 1;
                c++;
            }
            cycles.push_back(c);
            if (c % 2 == 0) {
                int half = c / 2;
                even_half_sum += half;
                cnt[half]++;
            }
        }
    }

    // Combine pairs of same length halves into bigger halves
    for (int i = 1; i <= n; ++i) {
        while (cnt[i] > 2) {
            int pairs = cnt[i] / 2 * 2;
            int add = pairs / 2;
            cnt[i * 2] += add;
            cnt[i] -= pairs;
        }
    }

    // Bitset DP for subset sums of half-lengths
    bitset<N> dp;
    dp[0] = 1;
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < cnt[i]; ++j) {
            dp |= (dp << i);
        }
    }

    // Sort cycles: even cycles first descending, then odd cycles descending
    sort(cycles.begin(), cycles.end(), [](int a, int b) {
        if ((a % 2) == (b % 2)) return a > b;
        return (a % 2) == 0;
    });

    int q; cin >> q;
    while (q--) {
        int A0, A1, A2; cin >> A0 >> A1 >> A2;
        // A0 + A1 + A2 = n guaranteed

        // Base score from zeros: each zero-zero pair contributes 2 to score
        // Score base = 2 * A0
        int base = 2 * A0;

        // Special case: if A0 == A1 and A0 <= even_half_sum
        // Then answer is either 4*A0 or 4*A0 - 1 depending on dp
        if (A0 == A1 && A0 <= even_half_sum) {
            if (dp[A0]) {
                cout << 4 * A0 << "\n";
            } else {
                cout << 4 * A0 - 1 << "\n";
            }
            continue;
        }

        // Distribute zeros among cycles to maximize score
        // cnt00: count of zero-zero edges lost (penalty)
        // cnt1: count of edges with mex=1
        // cnt2: count of edges with mex=2
        int cnt00 = 0, cnt1 = 0, cnt2 = 0;
        int a = A0;

        // First assign zeros to even cycles
        for (int x : cycles) {
            if (a == 0) break;
            if (x % 2 == 0) {
                int half = x / 2;
                if (a >= half) {
                    cnt2 += half;
                    a -= half;
                } else {
                    // Partial assignment in even cycle
                    cnt1 += 2;
                    cnt2 += a - 1;
                    a = 0;
                }
            }
        }

        // Then assign zeros to odd cycles
        for (int x : cycles) {
            if (a == 0) break;
            if (x % 2 == 1) {
                a--;
                cnt00++;
                if (x > 1) {
                    cnt1 -= 2;
                    cnt2++;
                }
            }
        }

        // Remaining zeros assigned to pairs of edges (penalty)
        cnt00 += a * 2;
        cnt2 -= a;
        a = 0;

        // Calculate final answer
        int ans = base - cnt00;
        int mn = min(A1, cnt2);
        ans += mn * 2;
        A1 -= mn;
        ans += min(A1, cnt1);

        cout << ans << "\n";
    }
}