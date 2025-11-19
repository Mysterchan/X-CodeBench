#include <bits/stdc++.h>
using namespace std;
using ll = long long;

void solve() {
    int n;
    cin >> n;
    ll totalProblems = 0, totalPairs = 0;

    for (int i = 0; i < n; i++) {
        ll a, b, c;
        cin >> a >> b >> c;
        totalPairs += min(a, b);
        totalProblems += min(b, c);
    }

    cout << min(totalPairs, totalProblems) << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
