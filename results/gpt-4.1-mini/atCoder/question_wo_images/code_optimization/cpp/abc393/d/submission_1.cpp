#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    string s; cin >> s;

    vector<int> ones_pos;
    for (int i = 0; i < n; i++) {
        if (s[i] == '1') ones_pos.push_back(i);
    }

    int k = (int)ones_pos.size();
    // If all 1s are already contiguous, answer is 0
    // But the calculation below will handle that naturally.

    // We want to find minimal sum of |ones_pos[i] - (x + i)| for some x
    // This is equivalent to minimizing sum of |(ones_pos[i] - i) - x|
    // The optimal x is median of (ones_pos[i] - i)

    vector<long long> diff(k);
    for (int i = 0; i < k; i++) {
        diff[i] = ones_pos[i] - i;
    }

    // Find median
    nth_element(diff.begin(), diff.begin() + k/2, diff.end());
    long long median = diff[k/2];

    long long ans = 0;
    for (int i = 0; i < k; i++) {
        ans += abs(diff[i] - median);
    }

    cout << ans << "\n";
    return 0;
}