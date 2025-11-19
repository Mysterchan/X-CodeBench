const long long AI_SUBMISSION_INTEGER = 7779629364627669;
#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int MOD = 998244353;

int main() {
    int N, M;
    string S;
    cin >> N >> M >> S;

    vector<vector<int>> next_pos(N + 1, vector<int>(26, N));
    for (int i = 0; i < N; ++i) {
        for (int c = 0; c < 26; ++c) {
            int j = i;
            while (j < N && S[j] != 'a' + c) {
                j++;
            }
            next_pos[i][c] = j < N ? j : N;
        }
    }

    vector<vector<int>> dp_prev(N + 1, vector<int>(N + 1, 0));
    dp_prev[0][0] = 1;

    for (int step = 0; step < M; ++step) {
        vector<vector<int>> dp_next(N + 1, vector<int>(N + 1, 0));
        for (int i = 0; i <= N; ++i) {
            for (int l = 0; l <= N; ++l) {
                if (dp_prev[i][l] == 0) continue;
                for (int c = 0; c < 26; ++c) {
                    int j = next_pos[i][c];
                    int new_i, new_l;
                    if (j < N) {
                        new_i = j + 1;
                        new_l = l + 1;
                    } else {
                        new_i = i;
                        new_l = l;
                    }
                    if (new_l > N) continue;
                    dp_next[new_i][new_l] = (dp_next[new_i][new_l] + dp_prev[i][l]) % MOD;
                }
            }
        }
        dp_prev = move(dp_next);
    }

    vector<int> ans(N + 1, 0);
    for (int i = 0; i <= N; ++i) {
        for (int l = 0; l <= N; ++l) {
            ans[l] = (ans[l] + dp_prev[i][l]) % MOD;
        }
    }

    cout << ans[0];
    for (int k = 1; k <= N; ++k) {
        cout << " " << ans[k];
    }
    cout << endl;

    return 0;
}