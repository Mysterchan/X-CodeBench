#include "bits/stdc++.h"
using namespace std;

#define int long long
#define endl '\n'

void test() {
    int n;
    cin >> n;
    vector<pair<int, int>> points(n);

    for (int i = 0; i < n; i++) {
        cin >> points[i].first >> points[i].second;
    }

    if (n == 1) {
        cout << 1 << '\n';
        return;
    }

    int min_x = LLONG_MAX, max_x = LLONG_MIN, min_y = LLONG_MAX, max_y = LLONG_MIN;

    for (const auto &[x, y] : points) {
        min_x = min(min_x, x);
        max_x = max(max_x, x);
        min_y = min(min_y, y);
        max_y = max(max_y, y);
    }

    // We can try moving one monster to any extreme corner
    int original_area = (max_x - min_x + 1) * (max_y - min_y + 1);
    
    // Calculating the minimum area needed by considering moving one monster
    // Move one monster that is at (min_x, min_y) to (max_x + 1, min_y), or to other possible corners
    int candidates[] = {
        (max_x - min_x + 1) * (max_y - min_y + 1),
        ((max_x - min_x + 2) * (max_y - min_y + 1)), // Move one to the right
        ((max_x - min_x + 1) * (max_y - min_y + 2)), // Move one up
        ((max_x - min_x + 2) * (max_y - min_y + 2))  // Move both
    };

    int ans = LLONG_MAX;
    for (int area : candidates) {
        ans = min(ans, area);
    }

    cout << ans << '\n';
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        test();
    }
    return 0;
}