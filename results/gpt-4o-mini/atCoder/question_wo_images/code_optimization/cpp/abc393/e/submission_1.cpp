#include <bits/stdc++.h>
using namespace std;
const int M = 1e6 + 2;
int n, k, a[1200001], cnt[M];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n >> k;

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        cnt[a[i]]++;
    }

    for (int i = M - 1; i >= 1; --i) {
        for (int j = i * 2; j < M; j += i) {
            cnt[i] += cnt[j];
        }
    }

    for (int i = 1; i <= n; ++i) {
        int x = a[i], res = 1;

        for (int d = 1; d * d <= x; ++d) {
            if (x % d == 0) {
                if (cnt[d] >= k) res = max(res, d);
                if (d != x / d) {
                    if (cnt[x / d] >= k) {
                        res = max(res, x / d);
                    }
                }
            }
        }
        cout << res << '\n';
    }
    return 0;
}