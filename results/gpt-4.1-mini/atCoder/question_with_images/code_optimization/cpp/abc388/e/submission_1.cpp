#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; cin >> n;
    vector<int> a(n);
    for (int &x : a) cin >> x;

    int left = 0, right = n / 2;
    int ans = 0;

    // Greedy pairing: try to pair smallest mochi with smallest possible bigger mochi
    while (left < n / 2 && right < n) {
        if (a[left] * 2 <= a[right]) {
            ans++;
            left++;
            right++;
        } else {
            right++;
        }
    }

    cout << ans << "\n";
    return 0;
}