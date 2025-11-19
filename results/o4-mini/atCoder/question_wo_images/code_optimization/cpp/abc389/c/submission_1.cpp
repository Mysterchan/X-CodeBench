#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int Q;
    cin >> Q;
    vector<ll> head_pos(Q + 5), length_v(Q + 5);
    ll removed_sum = 0;
    ll end_pos = 0;
    int head_idx = 0, tail_idx = 0;
    int size = 0;

    while (Q--) {
        int type;
        cin >> type;
        if (type == 1) {
            ll l;
            cin >> l;
            // Insert new snake with absolute head = end_pos
            head_pos[tail_idx] = end_pos;
            length_v[tail_idx] = l;
            tail_idx++;
            size++;
            end_pos += l;
        } else if (type == 2) {
            // Pop front
            removed_sum += length_v[head_idx];
            head_idx++;
            size--;
            if (size == 0) {
                // Reset end_pos when queue becomes empty
                end_pos = removed_sum;
            }
        } else {
            int k;
            cin >> k;
            // k-th from front is at index head_idx + k - 1
            int idx = head_idx + k - 1;
            ll ans = head_pos[idx] - removed_sum;
            cout << ans << "\n";
        }
    }

    return 0;
}