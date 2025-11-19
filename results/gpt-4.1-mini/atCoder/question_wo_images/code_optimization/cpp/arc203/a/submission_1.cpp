#include <bits/stdc++.h>
using namespace std;
#define int long long

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while (T--) {
        int N, M; cin >> N >> M;
        // The maximum number of perfect record players is min(M * (N - 1), N * M) but since each player plays N-1 games,
        // and only players from one team can be undefeated, the maximum is M * (N - 1) capped by total players M*N.
        // Actually, the problem reduces to the maximum number of players who can be undefeated.
        // The known formula from the editorial or reasoning is:
        // max_perfect = M * (N - 1) - (N - 2) * M = M * (N - 1) - M * (N - 2) = M
        // But from the sample, the answer is min(M * (N - 1), N * M - M) = M * (N - 1)
        // Actually, the answer is M * (N - 1) - (N - 2) * M = M * (N - 1) - M * (N - 2) = M
        // The original code's logic is:
        // It tries to maximize ans = max(ans, m + res) where res increments by n and m decreases by 2.
        // This is equivalent to: ans = max over k of (m - 2k) + k * n, for k >= 0 and m - 2k >= 0.
        // The maximum is achieved at k = floor(m/2), so:
        // ans = max over k of m - 2k + k * n = m + k*(n - 2)
        // For n >= 2, n-2 >= 0, so max at k = floor(m/2)
        // So ans = m + floor(m/2)*(n - 2)
        // Implement this formula directly.

        int k = M / 2;
        int ans = M + k * (N - 2);
        cout << ans << "\n";
    }

    return 0;
}