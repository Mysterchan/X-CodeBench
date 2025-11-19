#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    vector<string> S(N), T(M);
    for (int i = 0; i < N; ++i) {
        cin >> S[i];
    }
    for (int i = 0; i < M; ++i) {
        cin >> T[i];
    }

    for (int i = 0; i + M <= N; ++i) {
        for (int j = 0; j + M <= N; ++j) {
            bool match = true;
            for (int r = 0; r < M; ++r) {
                // compare the substring of length M starting at column j
                if (S[i + r].compare(j, M, T[r]) != 0) {
                    match = false;
                    break;
                }
            }
            if (match) {
                cout << (i + 1) << " " << (j + 1) << "\n";
                return 0;
            }
        }
    }

    return 0;
}