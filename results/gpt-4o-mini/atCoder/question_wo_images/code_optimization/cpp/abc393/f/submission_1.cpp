#include<bits/stdc++.h>
using namespace std;

vector<long long> createLIS(const vector<long long>& nums) {
    vector<long long> dp;
    for (long long num : nums) {
        auto it = lower_bound(dp.begin(), dp.end(), num);
        if (it == dp.end())
            dp.push_back(num);
        else 
            *it = num;
    }
    return dp;
}

int main() {
    long long N, Q;
    cin >> N >> Q;
    vector<long long> A(N);
    for (long long i = 0; i < N; ++i)
        cin >> A[i];

    // Precompute the longest increasing subsequence for the whole array
    vector<long long> allLIS = createLIS(A);
    vector<vector<long long>> dp(N + 1, vector<long long>(allLIS.size() + 1, 0));

    // Fill dynamic programming table based on LIS values
    for (long long i = 1; i <= N; ++i) {
        for (long long j = 0; j <= allLIS.size(); ++j) {
            dp[i][j] = dp[i - 1][j];
            if (j > 0 && A[i - 1] == allLIS[j - 1]) {
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1);
            } else if (A[i - 1] < allLIS[j]) {
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + 1);
            }
        }
    }
    
    // Answering the queries
    for (long long i = 0; i < Q; ++i) {
        long long R, X;
        cin >> R >> X;
        vector<long long> validNums;
        for (long long j = 0; j < R; ++j) {
            if (A[j] <= X) {
                validNums.push_back(A[j]);
            }
        }
        if (validNums.empty()) {
            cout << 0 << endl;
        } else {
            vector<long long> resultLIS = createLIS(validNums);
            cout << resultLIS.size() << endl;
        }
    }
}