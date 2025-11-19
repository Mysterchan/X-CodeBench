#include <bits/stdc++.h>
using namespace std;

const int MAX_R = 500000;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N; cin >> N;
    vector<int> diff(MAX_R + 2, 0);

    for (int i = 0; i < N; i++) {
        int L, R; cin >> L >> R;
        diff[L]++;
        if (R + 1 <= MAX_R) diff[R + 1]--;
    }

    // Prefix sum to get count of intervals covering each rating
    for (int i = 1; i <= MAX_R; i++) {
        diff[i] += diff[i - 1];
    }

    // Precompute final rating after all contests for each initial rating
    // final_rating[x] = x + diff[x]
    // We can answer queries in O(1)
    int Q; cin >> Q;
    while (Q--) {
        int X; cin >> X;
        cout << X + diff[X] << "\n";
    }

    return 0;
}