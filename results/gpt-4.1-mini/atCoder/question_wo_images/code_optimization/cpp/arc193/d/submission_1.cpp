#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while (T--) {
        int N; cin >> N;
        string A, B;
        cin >> A >> B;

        vector<int> va, vb;
        for (int i = 0; i < N; i++) {
            if (A[i] == '1') va.push_back(i + 1);
        }
        for (int i = 0; i < N; i++) {
            if (B[i] == '1') vb.push_back(i + 1);
        }

        // If number of pieces differ, impossible
        if ((int)va.size() != (int)vb.size()) {
            cout << -1 << "\n";
            continue;
        }

        int M = (int)va.size();

        // Check if the order of pieces can be matched
        // The operation can only move pieces closer to some position,
        // but the relative order of pieces is preserved.
        // So if the sorted positions of A and B differ in order, impossible.
        // Here va and vb are sorted by construction.

        // Calculate minimal number of operations:
        // The minimal number of operations is the maximum over i of |va[i] - vb[i]|
        // Because each operation can move all pieces one step closer to some position,
        // and the minimal number of operations needed to move piece i from va[i] to vb[i]
        // is at least the distance |va[i] - vb[i]|.

        int ans = 0;
        for (int i = 0; i < M; i++) {
            ans = max(ans, abs(va[i] - vb[i]));
        }

        cout << ans << "\n";
    }

    return 0;
}