#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

int count_nodes(int l1, int r1, int l2, int r2) {
    int count = 0;

    // Divide the region into segments of [0, 2^k]
    // Loop to find the largest power of 2 that covers the given rectangles
    int size = 1;
    while (size < max(r1, r2)) {
        size *= 2;
    }
    
    for (int x = 0; x < size; x += size / 2) {
        for (int y = 0; y < size; y += size / 2) {
            int seg_l1 = x, seg_r1 = x + size / 2;
            int seg_l2 = y, seg_r2 = y + size / 2;

            // Check if the segment intersects with the query rectangle
            if (!(seg_r1 <= l1 || r1 <= seg_l1 || seg_r2 <= l2 || r2 <= seg_l2)) {
                // Add how many complete segments can be made with the current size
                if (seg_l1 < l1 && r1 < seg_r1 && seg_l2 < l2 && r2 < seg_r2) {
                    // Complete intersection
                    count += (seg_r1 - seg_l1) / (size / 2) * (seg_r2 - seg_l2) / (size / 2);
                } else {
                    count++;
                }
            }
        }
    }
    
    return count;
}

signed main() {
    cin.tie(0)->sync_with_stdio(0);

    int t;
    cin >> t;

    while (t--) {
        int l1, r1, l2, r2;
        cin >> l1 >> r1 >> l2 >> r2;

        cout << count_nodes(l1, r1, l2, r2) << endl;
    }

    return 0;
}