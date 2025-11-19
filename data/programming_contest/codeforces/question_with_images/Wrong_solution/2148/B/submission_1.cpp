#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n, m, x, y;
    cin >> n >> m >> x >> y;
    cout << n + m << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    if (fopen("B.INP", "r")) {
        freopen("B.INP", "r", stdin);
        freopen("B.OUT", "w", stdout);
    }

    int t;
    cin >> t;
    while(t--) solve();

    return 0;
}
