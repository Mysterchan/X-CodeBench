#include <bits/stdc++.h>
using namespace std;

const int M = 5e5 + 5;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    vector<int> increase(M, 0);

    for (int i = 0; i < n; i++) {
        int l, r;
        cin >> l >> r;
        increase[l]++;
        if (r + 1 < M) {
            increase[r + 1]--;
        }
    }

    // Compute the cumulative sum to prepare for queries
    for (int i = 1; i < M; i++) {
        increase[i] += increase[i - 1];
    }

    int q;
    cin >> q;
    while (q--) {
        int x;
        cin >> x;
        // Rating increases by the precalculated value at x
        cout << x + increase[x] << "\n";
    }

    return 0;
}