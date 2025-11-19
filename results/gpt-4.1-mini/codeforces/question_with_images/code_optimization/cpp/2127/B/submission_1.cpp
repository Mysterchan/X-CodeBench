#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while (T--) {
        int n, x; cin >> n >> x;
        string s; cin >> s;

        // Count empty cells to the left of x (excluding x)
        int left_empty = 0;
        for (int i = x - 2; i >= 0; i--) {
            if (s[i] == '.') left_empty++;
            else break;
        }

        // Count empty cells to the right of x (excluding x)
        int right_empty = 0;
        for (int i = x; i < n; i++) {
            if (s[i] == '.') right_empty++;
            else break;
        }

        // The answer is 1 + min(left_empty, right_empty)
        // Explanation:
        // Mani will try to block the side with fewer empty cells first,
        // forcing Hamid to escape from the other side after destroying walls.
        cout << 1 + min(left_empty, right_empty) << "\n";
    }

    return 0;
}