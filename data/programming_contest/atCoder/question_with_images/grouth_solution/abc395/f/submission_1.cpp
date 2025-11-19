#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#define int long long
using namespace std;

bool check(int mid, vector<int>& upper, vector<int>& lower, int x) {
    int n = upper.size();
    int u_lower = max(0LL, mid - lower[0]);
    int u_upper = min(upper[0], mid);
    if (u_lower > u_upper) return false;

    for (int i = 1; i < n; i++) {
        u_lower = max(max(0LL, mid - lower[i]), u_lower - x);
        u_upper = min(min(upper[i], mid), u_upper + x);
        if (u_lower > u_upper) return false;
    }
    return true;
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, x;
    cin >> n >> x;
    int sum = 0;
    int min_h = 2e9;
    vector<int> u(n), d(n);
    for (int i = 0; i < n; i++) {
        cin >> u[i] >> d[i];
        sum += u[i] + d[i];
        min_h = min(min_h, u[i] + d[i]);
    }

    int l = 2, r = min_h;
    int best_h = 0;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (check(mid, u, d, x)) {
            best_h = mid;
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    cout << sum - best_h * n << '\n';
    return 0;
}