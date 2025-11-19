#include <bits/stdc++.h>
using namespace std;

#define int long long

int popcount(int x) {
    return __builtin_popcountll(x);
}

void solve() {
    int n, k;
    cin >> n >> k;

    // Count number of set bits in n
    int c = popcount(n);

    // Number of compatible X is 2^c
    // If k > 2^c, no such k-th compatible number
    if (k > (1LL << c)) {
        cout << -1 << '\n';
        return;
    }

    // We want to find the k-th smallest compatible X
    // Compatible X satisfy: (X XOR N) == (X % N)
    // From analysis:
    // Let bits set in n be at positions p0 < p1 < ... < p_{c-1}
    // For each compatible X, bits at positions p_i are set to 1
    // The bits at other positions (where n has 0) correspond to bits of (X % N)
    // The mapping from (X % N) to X is:
    // X = N + sum over i of (bit_i of (X % N)) * 2^{p_i}
    // where p_i are positions of zero bits in n.

    // Find positions of zero bits in n (from LSB to MSB)
    vector<int> zero_bits;
    for (int i = 0; i < 31; i++) {
        if ((n & (1LL << i)) == 0) {
            zero_bits.push_back(i);
        }
    }

    // k-th smallest compatible X corresponds to (k-1) as the bits for zero_bits positions
    int rem = k - 1;
    int ans = n;
    for (int i = 0; i < (int)zero_bits.size(); i++) {
        if (rem & (1LL << i)) {
            ans |= (1LL << zero_bits[i]);
        }
    }

    cout << ans << '\n';
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) solve();

    return 0;
}