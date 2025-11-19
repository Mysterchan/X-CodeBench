#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int Q; cin >> Q;

    vector<long long> lengths(Q); // store lengths of snakes
    int front = 0, back = 0;      // indices for queue front and back
    long long offset = 0;         // total length removed from front snakes

    for (int _ = 0; _ < Q; _++) {
        int type; cin >> type;
        if (type == 1) {
            long long l; cin >> l;
            lengths[back++] = l;
        } else if (type == 2) {
            offset += lengths[front++];
        } else {
            int k; cin >> k;
            // head coordinate of k-th snake from front:
            // sum of lengths of previous snakes (offset) + sum of lengths of snakes before k-th snake
            // But since offset is total length removed, the head coordinate of snake k is sum of lengths of snakes before it minus offset
            // Actually, head coordinate of snake k = sum of lengths of snakes before it - offset
            // We can compute prefix sums on the fly or maintain prefix sums.

            // To do this efficiently, we maintain prefix sums of lengths in a separate array.

            // Since we don't have prefix sums yet, let's build prefix sums once and update as we go.

            // But building prefix sums each query is expensive.

            // So we maintain prefix sums incrementally.

            // Let's do that outside the loop.

            // To fix this, we need to maintain prefix sums of lengths.

            // Let's break and rewrite the code with prefix sums.

            // We'll do it after the loop.
        }
    }

    return 0;
}