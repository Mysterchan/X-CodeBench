#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];

    int operations = 0;
    int last = a[0], count = 1;

    for (int i = 1; i < n; i++) {
        if (a[i] == last) {
            count++;
        } else {
            operations++;
            last = a[i];
            count = 1;
        }
    }

    // Add 1 for the last segment
    operations += count > 0 ? 1 : 0;

    // The number of delete operations is equal to segments
    cout << operations + (n - operations) << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T;
    cin >> T;
    while (T--) {
        solve();
    }

    return 0;
}
