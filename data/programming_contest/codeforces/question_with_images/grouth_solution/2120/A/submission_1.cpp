#ifdef DEBUG
#define _GLIBCXX_DEBUG
#endif
#include<bits/stdc++.h>
using namespace std;

#ifdef DEBUG
#include "lib/debug.h"
#else
#define debug(...) 228
#endif

#define pb push_back

typedef long long ll;
typedef long double ld;
void solve() {
    int a[3], b[3];
    for (int i = 0; i < 3; i++) {
        cin >> a[i] >> b[i];
    }
    if (a[0] == a[1] + a[2] && b[1] == b[2] && a[0] == b[0] + b[1]) {
        cout << "YES\n";
        return;
    }
    if (b[0] == b[1] + b[2] && a[1] == a[2] && b[0] == a[0] + a[1]) {
        cout << "YES\n";
        return;
    }
    if ((a[0] == a[2] && a[0] == b[0] + b[1] + b[2]) || (b[0] == b[2] && b[0] == a[0] + a[1] + a[2])) {
        cout << "YES\n";
        return;
    }
    cout << "NO\n";
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    auto start = std::chrono::high_resolution_clock::now();
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
#endif
    int tst;
    cin >> tst;
    while (tst--) solve();
    return 0;
}