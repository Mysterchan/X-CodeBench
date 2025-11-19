#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, D;
    cin >> N >> D;
    vector<int> T(N), L(N);
    for (int i = 0; i < N; ++i) {
        cin >> T[i] >> L[i];
    }

    for (int k = 1; k <= D; ++k) {
        int best = 0;
        for (int i = 0; i < N; ++i) {
            int w = T[i] * (L[i] + k);
            if (w > best) best = w;
        }
        cout << best << "\n";
    }

    return 0;
}