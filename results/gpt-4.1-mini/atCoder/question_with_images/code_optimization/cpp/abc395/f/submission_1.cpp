#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N; long long X;
    cin >> N >> X;
    vector<long long> U(N), D(N);
    long long S = 0;
    for (int i = 0; i < N; ++i) {
        cin >> U[i] >> D[i];
        S += U[i] + D[i];
    }

    // We want to find H = U_i + D_i for all i, and minimize cost = sum of reductions.
    // Conditions:
    // 1) U_i + D_i = H for all i
    // 2) |U_i - U_{i+1}| <= X for all i

    // Let A_i = U_i + D_i (initial sums)
    // We want to find H <= min(A_i) (since we can only reduce lengths)
    // and find U_i such that:
    //   U_i + D_i = H
    //   |U_i - U_{i+1}| <= X
    //   0 <= U_i <= U_i_initial (since we can only reduce)
    //   0 <= D_i = H - U_i <= D_i_initial

    // The problem reduces to:
    // For fixed H, find U_i satisfying:
    //   max(0, H - D_i) <= U_i <= min(U_i_initial, H)
    //   |U_i - U_{i+1}| <= X

    // We want to maximize H (to minimize cost = S - N*H)
    // So binary search on H in [0, min(A_i)]

    long long low = 0, high = *min_element(U.begin(), U.end());
    for (int i = 0; i < N; ++i) {
        high = min(high, U[i] + D[i]);
    }

    auto can = [&](long long H) -> bool {
        // Check if there exists U_i satisfying constraints for given H
        // We'll keep track of feasible intervals for U_i
        long long L = max(0LL, H - D[0]);
        long long R = min(U[0], H);
        if (L > R) return false;
        for (int i = 1; i < N; ++i) {
            long long nl = max(0LL, H - D[i]);
            long long nr = min(U[i], H);
            if (nl > nr) return false;

            // Due to |U_i - U_{i-1}| <= X:
            // U_i in [L - X, R + X] intersect [nl, nr]
            L = max(nl, L - X);
            R = min(nr, R + X);
            if (L > R) return false;
        }
        return true;
    };

    while (low < high) {
        long long mid = (low + high + 1) / 2;
        if (can(mid)) low = mid;
        else high = mid - 1;
    }

    // Minimum cost = S - N * low
    cout << S - N * low << "\n";

    return 0;
}