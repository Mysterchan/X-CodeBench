#include <iostream>
using namespace std;

const int MAXN = 2e5 + 3;

int main() {
    int n, q;
    int a[MAXN] = {0};
    cin >> n;

    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }

    cin >> q;

    while (q--) {
        int l, r;
        cin >> l >> r;

        int ans = 0, mid = (l + r >> 1) + 1;

        for (int i = l, j = mid; j <= r; j++) {
            if (a[i] * 2 <= a[j]) {
                ans++;
                i++;
            }
        }
        cout << ans << endl;
    }
}
