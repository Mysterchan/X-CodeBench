#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int n, m, k;
        cin >> n >> m >> k;
        vector<int> cnt(m + 1, 0);
        for (int i = 0; i < k; ++i) {
            int x, y; cin >> x >> y;
            ++cnt[y];
        }

        bool mimo_wins = false;
        // If n == 1, only column 2 matters for moves
        if (n == 1) {
            if (m >= 2 && (cnt[2] & 1)) mimo_wins = true;
        } else {
            // For n > 1, any odd count in columns 2..m means Mimo wins
            for (int y = 2; y <= m; ++y) {
                if (cnt[y] & 1) {
                    mimo_wins = true;
                    break;
                }
            }
        }

        cout << (mimo_wins ? "Mimo\n" : "Yuyu\n");
    }

    return 0;
}