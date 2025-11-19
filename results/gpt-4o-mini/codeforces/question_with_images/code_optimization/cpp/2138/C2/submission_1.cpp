#include <bits/stdc++.h>
using namespace std;

const int N = 2e5 + 1;
int n, k, p[N], h[N], cnt[N];

void solve() {
    cin >> n >> k;
    vector<int> deg(n + 1, 0);
    fill(cnt, cnt + n + 1, 0);
    
    for (int i = 2; i <= n; ++i) {
        cin >> p[i];
        ++deg[p[i]];
    }

    int mnh = n;
    for (int i = 2; i <= n; ++i) {
        h[i] = h[p[i]] + 1;
        ++cnt[h[i]];
        if (deg[i] == 0) mnh = min(mnh, h[i]);
    }

    vector<bool> cur(k + 1, false);
    cur[0] = true;
    int totalLeaves = 0;

    for (int i = 0; i <= mnh; ++i) {
        totalLeaves += cnt[i];
        int minRequiredZeros = max(0, k - totalLeaves);
        
        for (int j = k; j >= minRequiredZeros; --j) {
            cur[j] = cur[j] || (j >= cnt[i] && cur[j - cnt[i]]);
        }

        if (cur[k]) {
            cout << i + 1 << '\n';
            return;
        }
    }
    cout << 0 << '\n'; // In case no subsequence could be derived
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}