#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        vector<int> A(N);
        long long total = 0;
        for (int i = 0; i < N; i++) {
            cin >> A[i];
            total += A[i];
        }

        double average = static_cast<double>(total) / N;
        int score = 0;
        for (int i = 0; i < N; i++) {
            if (A[i] > average) {
                score++;
            }
        }
        cout << score << "\n";
    }

    return 0;
}
