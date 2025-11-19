#include <iostream>
#include <vector>
using namespace std;

const int MAXN = 2e5 + 3;

int main() {
    int n, q;
    vector<int> a(MAXN);
    cin >> n;

    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }

    cin >> q;
    while (q--) {
        int l, r;
        cin >> l >> r;

        int ans = 0;
        int j = l; // Pointer for the smaller mochi

        // Use two pointers to count pairs
        for (int i = l; i <= r; i++) {
            while (j <= r && a[j] < a[i] * 2) {
                j++;
            }
            // If j is still within the bounds, we can form a kagamimochi
            if (j <= r) {
                ans++;
                j++; // Move j to form the next pair
            }
        }
        cout << ans << endl;
    }

    return 0;
}