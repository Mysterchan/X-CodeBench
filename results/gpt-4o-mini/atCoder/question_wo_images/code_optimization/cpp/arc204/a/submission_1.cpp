#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;
const int MAXC = 250000 + 5005;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, L, R;
    cin >> N >> L >> R;

    vector<int> A(N), B(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    for (int i = 0; i < N; ++i) cin >> B[i];

    vector<vector<int>> dp(N + 1, vector<int>(MAXC, 0));
    dp[0][0] = 1;

    for (int step = 0; step < 2 * N; ++step) {
        vector<vector<int>> dp_next(N + 1, vector<int>(MAXC, 0));
        for (int qsize = 0; qsize <= N; ++qsize) {
            for (int c = 0; c < MAXC; ++c) {
                if (dp[qsize][c] > 0) {
                    int pushed = (step + qsize) / 2;
                    int popped = step - pushed;

                    // Action 1: Add element i to Q
                    if (pushed < N) {
                        int ai = A[pushed];
                        int c_new = max(0, c - ai);
                        dp_next[qsize + 1][c_new] = (dp_next[qsize + 1][c_new] + dp[qsize][c]) % MOD;
                    }

                    // Action 2: Remove element from Q
                    if (qsize > 0 && popped < N) {
                        int bi = B[popped];
                        int c_new = c + bi;
                        if (c_new < MAXC) {
                            dp_next[qsize - 1][c_new] = (dp_next[qsize - 1][c_new] + dp[qsize][c]) % MOD;
                        }
                    }
                }
            }
        }
        dp.swap(dp_next);
    }

    int result = 0;
    for (int c = L; c <= R; ++c) {
        result = (result + dp[0][c]) % MOD;
    }

    cout << result << '\n';
    return 0;
}
