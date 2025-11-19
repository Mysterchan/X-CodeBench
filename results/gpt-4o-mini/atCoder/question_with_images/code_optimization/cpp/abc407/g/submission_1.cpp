#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    ll h, w;
    cin >> h >> w;
    
    vector<vector<ll>> a(h, vector<ll>(w));
    ll total_sum = 0;
    
    for (ll i = 0; i < h; ++i) {
        for (ll j = 0; j < w; ++j) {
            cin >> a[i][j];
            total_sum += a[i][j];
        }
    }
    
    ll min_cover = 0;

    for (ll r = 0; r < h; ++r) {
        for (ll c = 0; c < w; ++c) {
            if (r < h - 1 && a[r][c] + a[r + 1][c] < 0) {
                min_cover += (-(a[r][c] + a[r + 1][c]));
            }
            if (c < w - 1 && a[r][c] + a[r][c + 1] < 0) {
                min_cover += (-(a[r][c] + a[r][c + 1]));
            }
        }
    }
    
    cout << total_sum + min_cover << "\n";

    return 0;
}