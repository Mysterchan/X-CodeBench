#include<bits/stdc++.h>
#define int long long
using namespace std;

const int maxN = 2e5 + 10;
int a[maxN], b[maxN], sumA[maxN], sumB[maxN];

void solve() {
    int n, m;
    cin >> n >> m;

    for (int i = 1; i <= n; i++) cin >> a[i];
    for (int i = 1; i <= m; i++) cin >> b[i];

    sort(a + 1, a + n + 1);
    sort(b + 1, b + m + 1);

    int maxOperations = 0;
    if (n >= 2 * m) {
        maxOperations = m;
    } else if (m >= 2 * n) {
        maxOperations = n;
    } else {
        maxOperations = min((n + m) / 3, min(n, m));
    }

    vector<int> areas(maxOperations + 1, 0);

    for (int k = 1; k <= maxOperations; k++) {
        int maxTriangleArea = 0;

        for (int i = 0; i <= k; i++) {
            int u = (k - i);
            if (i <= n / 2 && u <= m / 2) {
                maxTriangleArea = max(maxTriangleArea, (a[i * 2 + 1] - a[i * 2]) + (b[u * 2 + 1] - b[u * 2]));
            }
        }
        areas[k] = maxTriangleArea;
    }

    cout << maxOperations << endl;
    for (int k = 1; k <= maxOperations; k++) {
        cout << areas[k] << (k == maxOperations ? '\n' : ' ');
    }
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}