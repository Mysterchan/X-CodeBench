#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        vector<ll> A(N);
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }
        if (N < 2) {
            cout << 0 << "\n";
            continue;
        }
        sort(A.begin(), A.end());
        vector<ll> pref(N + 1, 0);
        for (int i = 0; i < N; i++) {
            pref[i + 1] = pref[i] + A[i];
        }
        ll s1 = A[0];
        int ans = 0;
        // consider b1 = A[i], i from 1..N-1
        for (int i = 1; i < N; i++) {
            ll b1 = A[i];
            ll limit = b1 - s1;
            if (limit <= 0) continue;
            int lo = 1, hi = N - i, best = 0;
            while (lo <= hi) {
                int mid = (lo + hi) >> 1;
                // sum of A[i..i+mid-1] = pref[i+mid] - pref[i]
                ll sum_big = pref[i + mid] - pref[i];
                // D = sum_big - mid * b1
                ll D = sum_big - (ll)mid * b1;
                if (D < limit) {
                    best = mid;
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
            ans = max(ans, best);
        }
        cout << ans << "\n";
    }

    return 0;
}