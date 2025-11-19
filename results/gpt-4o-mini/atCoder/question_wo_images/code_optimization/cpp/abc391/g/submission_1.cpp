#include <bits/stdc++.h>
using namespace std;

int N, M;
string S;
const long long MOD = 998244353;

int main() {
    cin >> N >> M >> S;

    // Precompute powers of 26 modulo MOD
    vector<long long> power(101);
    power[0] = 1;
    for (int i = 1; i <= 100; i++) {
        power[i] = (power[i - 1] * 26) % MOD;
    }

    // Count distinct characters in S
    unordered_set<char> unique_chars(S.begin(), S.end());
    int k = unique_chars.size();
    int rem = 26 - k; // remaining letters not in S

    // DP to count possibilities for each k
    vector<long long> res(N + 1, 0);

    // DP transition
    for (int i = 0; i <= M; i++) {
        vector<long long> temp(N + 1, 0);
        for (int j = 0; j <= N; j++) {
            if (j == 0) {
                // no common subsequence
                temp[0] = (temp[0] + power[i] * (j == 0 ? 1 : 0)) % MOD;
            } else {
                // determine how many ways to achieve a common subsequence of length j
                for (int p = 0; p < N; ++p) {
                    if (S[p] == (char)('a' + (j - 1))) {
                        temp[j] = (temp[j] + res[j - 1]) % MOD;
                    }
                }
                temp[j] = (temp[j] + (rem * res[j]) % MOD) % MOD;
            }
        }
        swap(res, temp);
    }

    // Output the result
    for (int i = 0; i <= N; i++) {
        cout << res[i] << " \n"[i == N];
    }

    return 0;
}