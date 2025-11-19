#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        int n;
        cin >> n;
        vector<long long> a(n+1);
        for (int i = 1; i <= n; ++i) cin >> a[i];

        vector<long long> diff(n+2, 0);
        long long active = 0;
        long long K = 0;

        for (int i = 1; i <= n; ++i) {
            active += diff[i];
            long long h = a[i] + active;

            if (i < n && i + h >= n) K++;

            if (h > 0) {
                diff[i+1] += 1;
                long long endpos = min<long long>(n+1, i + h + 1);
                diff[endpos] -= 1;
            }
        }
        cout << (K + 1) << "\n";
    }
    return 0;
}