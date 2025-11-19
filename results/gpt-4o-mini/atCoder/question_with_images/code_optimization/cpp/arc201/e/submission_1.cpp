#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int mod = 998244353;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    // Calculate prefix sums and counts
    vector<ll> prefixSum(n + 1, 0), prefixCount(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        prefixSum[i] = (prefixSum[i - 1] + a[i]) % mod;
        prefixCount[i] = (prefixCount[i - 1] + 1) % mod; // Total count of elements
    }

    ll totalAreaSum = 0;
    
    // Outer loops to handle bounding boxes
    for (int l = 1; l <= n; ++l) {
        for (int r = l + 1; r <= n; ++r) {
            int minY = min(a[l], a[r]);
            int maxY = max(a[l], a[r]);
            
            // Area of the bounding box
            ll width = r - l;
            ll height = maxY - minY;

            // Total area considers subsets of points from l to r
            ll areaContribution = (width * height) % mod;

            // Calculate the number of valid subsets
            ll count = (prefixCount[r - 1] - prefixCount[l] + mod) % mod;

            // Each selection of points contributes the area multiplied by the count of valid subsets
            totalAreaSum = (totalAreaSum + areaContribution * count) % mod;
        }
    }

    cout << totalAreaSum << '\n';
    return 0;
}