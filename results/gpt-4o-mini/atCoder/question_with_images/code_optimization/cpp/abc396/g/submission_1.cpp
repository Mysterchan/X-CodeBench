#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const ll N = 200005;
ll n, m, a[N];
string s;

int main() {
    cin >> n >> m;
    for (ll i = 1; i <= n; ++i) {
        cin >> s;
        a[i] = stoll(s, nullptr, 2);  // Convert binary string to long long directly
    }

    ll min_sum = n * m;  // Start with the maximum possible sum
    for (ll mask = 0; mask < (1 << m); ++mask) {
        ll total = 0;
        for (ll i = 1; i <= n; ++i) {
            // Count bits set in a[i] XOR mask
            total += __builtin_popcountll(a[i] ^ mask);
        }
        min_sum = min(min_sum, total);
    }

    cout << min_sum << "\n";
    return 0;
}