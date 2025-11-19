#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

int main() {
    int N;
    int M;
    if (!(cin >> N >> M)) return 0;
    string S;
    cin >> S;
    int Slen = N;
    int states = 1 << N;
    auto mask_to_row = [&](int mask, vector<int> &row) {
        row.assign(N + 1, 0);
        for (int i = 1; i <= N; i++) {
            int bit = (mask >> (i - 1)) & 1;
            row[i] = row[i - 1] + bit;
        }
    };
    auto row_to_mask = [&](const vector<int> &row) -> int {
        int m = 0;
        for (int i = 1; i <= N; i++) {
            int d = row[i] - row[i - 1];
            if (d) {
                m |= (1 << (i - 1));
            }
        }
        return m;
    };
    vector<int> dp(states);
    dp[0] = 1;
    vector<int> f(N + 1);
    vector<int> g(N + 1);
    vector<int> ndp(states);
    for (int step = 0; step < M; step++) {
        fill(ndp.begin(), ndp.end(), 0);
        for (int mask = 0; mask < states; mask++) {
            int ways = dp[mask];
            if (!ways) continue;
            mask_to_row(mask, f);
            for (int c = 0; c < 26; c++) {
                g[0] = 0;
                for (int i = 1; i <= N; i++) {
                    int t1 = g[i - 1];
                    int t2 = f[i];
                    int t3 = -1000000000;
                    if (S[i - 1] - 'a' == c) {
                        t3 = f[i - 1] + 1;
                    }
                    g[i] = t1;
                    if (t2 > g[i]) {
                        g[i] = t2;
                    }
                    if (t3 > g[i]) {
                        g[i] = t3;
                    }
                }
                int nmask = row_to_mask(g);
                int nv = ndp[nmask] + ways;
                if (nv >= MOD) nv -= MOD;
                ndp[nmask] = nv;
            }
        }
        dp.swap(ndp);
    }
    vector<int> ans(N + 1);
    vector<int> last(N + 1);
    for (int mask = 0; mask < states; mask++) {
        int ways = dp[mask];
        if (!ways) continue;
        mask_to_row(mask, last);
        int k = last[N];
        int nv = ans[k] + ways;
        if (nv >= MOD) nv -= MOD;
        ans[k] = nv;
    }
    for (int k = 0; k <= N; k++) {
        if (k) cout << " ";
        cout << ans[k];
    }
    cout << "\n";
    return 0;
}
