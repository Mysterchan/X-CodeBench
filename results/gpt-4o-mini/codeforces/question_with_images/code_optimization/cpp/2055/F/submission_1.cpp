#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pii pair<int, int>
#define vll vector<pair<ll, ll>>

bool can_partition(const vll &S) {
    int N = S.size();
    ll total = 0, half_total = 0;

    for (const auto &[l, r] : S) {
        total += (r - l + 1);
    }

    // An even area is guaranteed, we can proceed directly
    for (int i = 0; i < N; ++i) {
        if (i % 2 == 0) {
            half_total += (S[i].second - S[i].first + 1);
        } else {
            half_total -= (S[i].second - S[i].first + 1);
        }
    }

    if (half_total != 0) return false;

    ll last_end = 0;
    for (int i = 0; i < N; ++i) {
        if (S[i].first <= last_end) {
            last_end = max(last_end, S[i].second);
        } else {
            return false;
        }
    }

    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vll S(n);
        for (int i = 0; i < n; ++i) {
            ll l, r;
            cin >> l >> r;
            S[i] = {l, r};
        }

        if (can_partition(S)) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
    return 0;
}