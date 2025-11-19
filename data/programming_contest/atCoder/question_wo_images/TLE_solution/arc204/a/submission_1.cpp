#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;
const int MAXN = 5005;
const int MAXC = 250000 + 5005;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, L, R;
    cin >> N >> L >> R;

    vector<int> A(N + 1), B(N + 1);
    for (int i = 1; i <= N; ++i) cin >> A[i];
    for (int i = 1; i <= N; ++i) cin >> B[i];

    vector<unordered_map<int, int>> dp(N + 2), dp_next(N + 2);
    dp[0][0] = 1;

    for (int step = 0; step < 2 * N; ++step) {
        for (int qsize = 0; qsize <= N; ++qsize) {
            for (auto& [c, cnt] : dp[qsize]) {
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
                    if (c_new <= MAXC)
                        dp_next[qsize - 1][c_new] = (dp_next[qsize - 1][c_new] + cnt) % MOD;
                }
            }
        }
        dp.swap(dp_next);
        for (int i = 0; i <= N; ++i) dp_next[i].clear();
    }

    int result = 0;
    for (auto& [c, cnt] : dp[0]) {
        if (L <= c && c <= R) {
            result = (result + cnt) % MOD;
        }
    }

    cout << result << '\n';
    return 0;
}
