#include <bits/stdc++.h>
using namespace std;

const int N = 5e5 + 5;

int n, x, y;
int a[N], b[N], tmp[N];

// Compress the array f by grouping runs of 0s and 1s,
// replacing runs of length x of 0 with 2, and runs of length y of 1 with 3.
int work(int *f) {
    int len = 0;
    int cnt = 0;
    for (int i = 1; i <= n; ++i) {
        if (i > 1 && f[i] != f[i - 1]) {
            // Process the previous run
            while (cnt > 0) {
                if (f[i - 1] == 0 && cnt >= x) {
                    int times = cnt / x;
                    for (int _ = 0; _ < times; ++_) tmp[++len] = 2;
                    cnt %= x;
                } else if (f[i - 1] == 1 && cnt >= y) {
                    int times = cnt / y;
                    for (int _ = 0; _ < times; ++_) tmp[++len] = 3;
                    cnt %= y;
                }
                while (cnt--) tmp[++len] = f[i - 1];
            }
            cnt = 0;
        }
        ++cnt;
    }
    // Process the last run
    while (cnt > 0) {
        if (f[n] == 0 && cnt >= x) {
            int times = cnt / x;
            for (int _ = 0; _ < times; ++_) tmp[++len] = 2;
            cnt %= x;
        } else if (f[n] == 1 && cnt >= y) {
            int times = cnt / y;
            for (int _ = 0; _ < times; ++_) tmp[++len] = 3;
            cnt %= y;
        }
        while (cnt--) tmp[++len] = f[n];
    }
    for (int i = 1; i <= len; ++i) f[i] = tmp[i];
    return len;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> x >> y;
    string s, t;
    cin >> s >> t;

    for (int i = 0; i < n; ++i) a[i + 1] = s[i] - '0';
    for (int i = 0; i < n; ++i) b[i + 1] = t[i] - '0';

    int l1 = work(a), l2 = work(b);
    if (l1 != l2) {
        cout << "No\n";
        return 0;
    }

    // Check if a and b are identical after compression
    for (int i = 1; i <= l1; ++i) {
        if (a[i] != b[i]) {
            cout << "No\n";
            return 0;
        }
    }

    cout << "Yes\n";
    return 0;
}