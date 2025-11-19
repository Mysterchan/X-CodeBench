#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll maxXOR(const vector<ll>& nums, int idx, int mask) {
    if (idx == nums.size()) {
        return mask;
    }
    
    // Option to not place a domino on the current cell
    ll best = maxXOR(nums, idx + 1, mask ^ nums[idx]);

    // Option to place a domino horizontally if within bounds
    if (idx % 2 == 0 && idx + 1 < nums.size()) {
        best = max(best, maxXOR(nums, idx + 2, mask));
    }
    
    // Option to place a domino vertically if within bounds (skip next column)
    if (idx + 2 < nums.size()) {
        best = max(best, maxXOR(nums, idx + 2, mask));
    }
    
    return best;
}

int main() {
    int h, w;
    cin >> h >> w;
    vector<ll> a(h * w);
    
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            cin >> a[i * w + j];
        }
    }

    cout << maxXOR(a, 0, 0) << "\n";
    return 0;
}