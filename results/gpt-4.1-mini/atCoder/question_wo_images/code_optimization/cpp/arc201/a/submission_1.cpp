#include <bits/stdc++.h>
using namespace std;
using ll = long long;

void solve() {
    int n; cin >> n;
    ll sumA = 0, sumB = 0, sumC = 0;
    for (int i = 0; i < n; i++) {
        ll A, B, C; cin >> A >> B >> C;
        sumA += A;
        sumB += B;
        sumC += C;
    }
    // Maximum number of times C2C can be held is limited by:
    // - sum of B (Medium problems) because both divisions require Medium
    // - sum of A + sum of C (Hard + Easy problems)
    // Each contest requires 1 Hard+1 Medium (Div1) and 1 Medium+1 Easy (Div2)
    // So total Medium needed per contest = 2
    // Total Hard+Easy needed per contest = 2
    // So max contests = min(sumB/2, (sumA+sumC)/2)
    ll ans = min(sumB / 2, (sumA + sumC) / 2);
    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T; cin >> T;
    while (T--) solve();
    return 0;
}