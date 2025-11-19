#include <iostream>
using namespace std;

const int MAXN = 2e5 + 3;
int a[MAXN];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, q;
    cin >> n;

    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }

    cin >> q;

    while (q--) {
        int l, r;
        cin >> l >> r;

        int ans = 0;
        int mid = (l + r) / 2;
        int j = mid + 1;
        
        for (int i = l; i <= mid && j <= r; i++) {
            while (j <= r && a[i] * 2 > a[j]) {
                j++;
            }
            if (j <= r) {
                ans++;
                j++;
            }
        }
        
        cout << ans << '\n';
    }
    
    return 0;
}