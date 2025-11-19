#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, L, R;
    cin >> N >> L >> R;

    vector<int> A(N + 1), B(N + 1);
    for (int i = 1; i <= N; ++i) cin >> A[i];
    for (int i = 1; i <= N; ++i) cin >> B[i];

    int max_c = 0;
    for (int i = 1; i <= N; ++i) max_c += B[i];
    
    vector<vector<int>> dp(N + 1, vector<int>(max_c + 1, 0));
    vector<vector<int>> dp_next(N + 1, vector<int>(max_c + 1, 0));
    
    dp[0][0] = 1;

    for (int step = 0; step < 2 * N; ++step) {
        for (int qsize = 0; qsize <= N; ++qsize) {
            for (int c = 0; c <= max_c; ++c) {
                if (dp[qsize][c] == 0) continue;
                
                int cnt = dp[qsize][c];
                int pushed = (step + qsize) / 2;
                int popped = step - pushed;

                if (pushed < N) {
                    int ai = A[pushed + 1];
                    int c_new = max(0, c - ai);
                    dp_next[qsize + 1][c_new] = (dp_next[qsize + 1][c_new] + cnt) % MOD;
                }

                if (qsize > 0 && popped < N) {
                    int bi = B[popped + 1];
                    int c_new = c + bi;
                    if (c_new <= max_c)
                        dp_next[qsize - 1][c_new] = (dp_next[qsize - 1][c_new] + cnt) % MOD;
                }
            }
        }
        swap(dp, dp_next);
        for (int i = 0; i <= N; ++i) {
            fill(dp_next[i].begin(), dp_next[i].end(), 0);
        }
    }

    int result = 0;
    for (int c = L; c <= min(R, max_c); ++c) {
        result = (result + dp[0][c]) % MOD;
    }

    cout << result << '\n';
    return 0;
}