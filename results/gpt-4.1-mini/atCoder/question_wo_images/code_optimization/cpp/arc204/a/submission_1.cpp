#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;
const int MAXN = 5005;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, L, R;
    cin >> N >> L >> R;

    vector<int> A(N + 1), B(N + 1);
    for (int i = 1; i <= N; ++i) cin >> A[i];
    for (int i = 1; i <= N; ++i) cin >> B[i];

    // Maximum possible sum of B[i] is at most 5000*5000=25,000,000, too large for DP dimension.
    // But since C can only increase by B[i] when popping, and decrease by A[i] when pushing,
    // and A[i], B[i] <= 5000, and N <= 5000, max C can be at most sum(B).
    // We'll compress C dimension by offsetting and using a vector of maps is too slow.
    // Instead, we use a vector of vectors with pruning.

    // The key insight:
    // At each step, qsize can be from 0 to N.
    // Number of pushes = (step + qsize)/2
    // Number of pops = step - pushes
    // We can only push if pushes < N
    // We can only pop if qsize > 0 and pops < N

    // We'll keep dp[qsize][c] = number of ways
    // To optimize memory and speed, we use vector<int> with offset for c.
    // But c can be up to sum(B), which can be large.
    // We'll use a map<int,int> for dp[qsize] to store only reachable c states.

    // However, unordered_map is slow. We'll use std::map for better cache locality and pruning.

    // To further optimize, we note that at each step, qsize changes by +1 or -1,
    // so we only need dp for qsize in [0..N].
    // We'll keep dp as vector<map<int,int>>.

    // But since the original code uses unordered_map and is slow,
    // we can optimize by using a vector of vectors with coordinate compression.

    // Let's find max sum of B to limit dp dimension.
    int maxC = 0;
    for (int i = 1; i <= N; ++i) maxC += B[i];

    // We'll use dp[qsize][c] where c in [0..maxC].
    // To save memory, we keep dp and dp_next as vector<vector<int>> with size maxC+1.
    // But maxC can be up to 25 million, too large for memory.

    // So we use a sparse representation: for each qsize, keep only reachable c in a map<int,int>.
    // To speed up, we use vector<pair<int,int>> to store states and a boolean visited array.

    // Implementation:
    // For each qsize, keep vector<pair<int,int>> states: (c, count)
    // For dp_next, we use a map<int,int> or unordered_map<int,int> to accumulate counts.
    // After processing, convert dp_next to vector<pair<int,int>> for next iteration.

    // This approach reduces overhead compared to unordered_map in inner loops.

    vector<vector<pair<int,int>>> dp(N + 1), dp_next(N + 1);
    dp[0].emplace_back(0, 1);

    for (int step = 0; step < 2 * N; ++step) {
        for (int qsize = 0; qsize <= N; ++qsize) {
            if (dp[qsize].empty()) continue;

            int pushed = (step + qsize) / 2;
            int popped = step - pushed;

            // Use map<int,int> to accumulate dp_next[qsize +/- 1]
            unordered_map<int,int> next_push, next_pop;

            if (pushed < N) {
                int ai = A[pushed + 1];
                for (auto& [c, cnt] : dp[qsize]) {
                    int c_new = c - ai;
                    if (c_new < 0) c_new = 0;
                    int& val = next_push[c_new];
                    val = (val + cnt) % MOD;
                }
            }

            if (qsize > 0 && popped < N) {
                int bi = B[popped + 1];
                for (auto& [c, cnt] : dp[qsize]) {
                    int c_new = c + bi;
                    // No upper bound check needed since c_new can be large but we only store reachable states
                    int& val = next_pop[c_new];
                    val = (val + cnt) % MOD;
                }
            }

            // Merge results into dp_next
            if (pushed < N) {
                int nq = qsize + 1;
                auto& vec = dp_next[nq];
                vec.reserve(vec.size() + next_push.size());
                for (auto& [c, cnt] : next_push) {
                    vec.emplace_back(c, cnt);
                }
            }
            if (qsize > 0 && popped < N) {
                int nq = qsize - 1;
                auto& vec = dp_next[nq];
                vec.reserve(vec.size() + next_pop.size());
                for (auto& [c, cnt] : next_pop) {
                    vec.emplace_back(c, cnt);
                }
            }
        }

        // Merge duplicates in dp_next and mod
        for (int q = 0; q <= N; ++q) {
            if (dp_next[q].empty()) continue;
            // Sort by c to merge duplicates
            auto& vec = dp_next[q];
            sort(vec.begin(), vec.end());
            int sz = 0;
            for (int i = 1; i < (int)vec.size(); ++i) {
                if (vec[sz].first == vec[i].first) {
                    vec[sz].second = (vec[sz].second + vec[i].second) % MOD;
                } else {
                    ++sz;
                    vec[sz] = vec[i];
                }
            }
            vec.resize(sz + 1);
        }

        dp.swap(dp_next);
        for (int q = 0; q <= N; ++q) dp_next[q].clear();
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