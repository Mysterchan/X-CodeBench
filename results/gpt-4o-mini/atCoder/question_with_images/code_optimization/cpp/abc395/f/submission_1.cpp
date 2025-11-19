#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, X;
    cin >> N >> X;
    vector<long long> U(N), D(N);
    long long S = 0;

    for (int i = 0; i < N; ++i) {
        cin >> U[i] >> D[i];
        S += U[i] + D[i];
    }

    long long total_cost = 0;
    long long min_H = LLONG_MAX;

    // Keep track of the required adjustments for U to fit H 
    // and the costs needed to meet the upper bound constraints
    for (int i = 0; i < N; ++i) {
        // Determine valid H for tooth i
        long long H = U[i] + D[i];
        if (H < min_H) {
            min_H = H;
        }
    }

    // Adjust for the upper teeth massaging constraints
    long long current_upper_length = U[0];

    for (int i = 1; i < N; ++i) {
        long long target_upper = current_upper_length + X;

        // If current U[i] > target, we need to grind it down
        if (U[i] > target_upper) {
            total_cost += U[i] - target_upper;
            U[i] = target_upper;
        }

        // Update the cost for the last adjustment
        current_upper_length = U[i];
    }

    // Check for lower teeth fitting for the minimum H
    for (int i = 0; i < N; ++i) {
        if (D[i] < min_H - U[i]) {
            total_cost += min_H - U[i] - D[i];
        }
    }

    cout << total_cost << endl;
}