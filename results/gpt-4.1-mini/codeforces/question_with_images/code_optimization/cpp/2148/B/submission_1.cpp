#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while (T--) {
        int n, m;
        long long x, y;
        cin >> n >> m >> x >> y;

        // Since lasers are sorted and strictly inside (0,x) or (0,y),
        // the minimal crossings is the count of lasers strictly between 0 and x (for vertical)
        // and strictly between 0 and y (for horizontal).
        // We just need to count how many lasers are strictly less than x (vertical)
        // and strictly less than y (horizontal).

        // Read horizontal lasers (y-coordinates)
        vector<long long> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];

        // Read vertical lasers (x-coordinates)
        vector<long long> b(m);
        for (int i = 0; i < m; i++) cin >> b[i];

        // Use binary search to count how many horizontal lasers are < y
        // and how many vertical lasers are < x
        // Since a and b are sorted, we can use upper_bound

        int horizontal_crossings = (int)(std::upper_bound(a.begin(), a.end(), y - 1) - a.begin());
        int vertical_crossings = (int)(std::upper_bound(b.begin(), b.end(), x - 1) - b.begin());

        cout << horizontal_crossings + vertical_crossings << "\n";
    }

    return 0;
}