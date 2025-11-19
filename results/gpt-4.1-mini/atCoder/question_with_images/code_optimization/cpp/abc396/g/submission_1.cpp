#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H, W;
    cin >> H >> W;
    vector<ll> rows(H);
    for (int i = 0; i < H; i++) {
        string s; cin >> s;
        ll val = 0;
        for (int j = 0; j < W; j++) {
            val = (val << 1) | (s[j] - '0');
        }
        rows[i] = val;
    }

    // Precompute popcount for all masks
    int max_mask = 1 << W;
    vector<int> popcount(max_mask);
    for (int i = 1; i < max_mask; i++) {
        popcount[i] = popcount[i >> 1] + (i & 1);
    }

    // Precompute f[num] = min(popcount(num), W - popcount(num))
    vector<int> f(max_mask);
    for (int i = 0; i < max_mask; i++) {
        int c = popcount[i];
        f[i] = min(c, W - c);
    }

    int ans = H * W;

    // Iterate only over half of the masks due to symmetry
    // (num ^ ((1<<W)-1)) < num means the complement mask is smaller, so skip
    for (int num = 0; num < max_mask; num++) {
        if ((num ^ (max_mask - 1)) < num) continue;

        ll sum = 0;
        for (int i = 0; i < H; i++) {
            sum += f[rows[i] ^ num];
            if (sum >= ans) break; // early pruning
        }
        if (sum < ans) ans = (int)sum;
    }

    cout << ans << "\n";
    return 0;
}