#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 500000;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, x, y;
    cin >> n >> x >> y;

    string s, t;
    cin >> s >> t;

    // Prepare initial counts of segments
    vector<int> count0(n + 1), count1(n + 1);
    
    for (int i = 1; i <= n; ++i) {
        count0[i] = count0[i - 1] + (s[i - 1] == '0');
        count1[i] = count1[i - 1] + (s[i - 1] == '1');
    }

    // Function to check if we can make the segment from `l` to `r` all zeros or all ones
    auto can_make_zero_segment = [&](int l, int r) {
        return (count0[r] - count0[l - 1] == r - l + 1);
    };

    auto can_make_one_segment = [&](int l, int r) {
        return (count1[r] - count1[l - 1] == r - l + 1);
    };

    for (int i = 0; i <= n - (x + y); ++i) {
        // Check if we can perform Operation A to make zeros followed by ones
        if (can_make_zero_segment(i + 1, i + x) && can_make_one_segment(i + x + 1, i + x + y)) {
            for (int j = 0; j < y; ++j) {
                s[i + j] = '1';
            }
            for (int j = 0; j < x; ++j) {
                s[i + x + j] = '0';
            }
        }

        // Check if we can perform Operation B to make ones followed by zeros
        if (can_make_one_segment(i + 1, i + y) && can_make_zero_segment(i + y + 1, i + y + x)) {
            for (int j = 0; j < x; ++j) {
                s[i + j] = '0';
            }
            for (int j = 0; j < y; ++j) {
                s[i + y + j] = '1';
            }
        }
    }

    cout << (s == t ? "Yes" : "No") << '\n';
    
    return 0;
}
