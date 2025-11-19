#include <bits/stdc++.h>
using namespace std;

const long long MOD = 998244353;

int N, M;
string S;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M >> S;

    // Extract unique characters in S
    vector<char> T;
    {
        string tmp = S;
        sort(tmp.begin(), tmp.end());
        tmp.erase(unique(tmp.begin(), tmp.end()), tmp.end());
        T.assign(tmp.begin(), tmp.end());
    }
    int rem = 26 - (int)T.size();

    // DP[i]: map from vector<int> (length N) to count of sequences of length i
    // vec[i] = length of LCS with S[0..i] ending at position i in S
    // The vector stores the length of the longest common subsequence ending at each position i in S
    // The maximum length of LCS is max over vec[i]

    // Use unordered_map with custom hash for vector<int> to speed up
    struct VectorHash {
        size_t operator()(const vector<int>& v) const {
            size_t seed = v.size();
            for (auto& i : v) {
                seed ^= i + 0x9e3779b9 + (seed << 6) + (seed >> 2);
            }
            return seed;
        }
    };

    using StateMap = unordered_map<vector<int>, long long, VectorHash>;

    StateMap dp[101];
    vector<int> start(N, 0);
    dp[0][start] = 1;

    for (int i = 0; i < M; i++) {
        StateMap& cur = dp[i];
        StateMap& nxt = dp[i + 1];
        for (auto& [vec, val] : cur) {
            long long v = val % MOD;
            // Add sequences with a character not in S
            if (rem > 0) {
                // Same vec, multiplied by rem
                long long add_val = (v * rem) % MOD;
                auto it = nxt.find(vec);
                if (it == nxt.end()) nxt[vec] = add_val;
                else {
                    it->second += add_val;
                    if (it->second >= MOD) it->second -= MOD;
                }
            }
            // Add sequences with characters in S
            for (char c : T) {
                vector<int> u = vec;
                int ma = 0;
                for (int j = 0; j < N; j++) {
                    int pma = ma;
                    ma = max(ma, u[j]);
                    if (S[j] == c) {
                        u[j] = pma + 1;
                    }
                }
                auto it = nxt.find(u);
                if (it == nxt.end()) nxt[u] = v;
                else {
                    it->second += v;
                    if (it->second >= MOD) it->second -= MOD;
                }
            }
        }
    }

    vector<long long> res(N + 1, 0);
    for (auto& [vec, val] : dp[M]) {
        int lcs = 0;
        for (int x : vec) lcs = max(lcs, x);
        res[lcs] = (res[lcs] + val) % MOD;
    }

    for (int i = 0; i <= N; i++) {
        cout << res[i] % MOD << (i == N ? '\n' : ' ');
    }
}