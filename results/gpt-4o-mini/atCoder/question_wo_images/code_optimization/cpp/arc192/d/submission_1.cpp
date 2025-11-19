#include<bits/stdc++.h>
using namespace std;
const int mod = 998244353;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    vector<int> A(n - 1);
    for (int i = 0; i < n - 1; ++i) {
        cin >> A[i];
    }
    
    int maxA = *max_element(A.begin(), A.end());
    vector<vector<long long>> dp(maxA + 1, vector<long long>(2, 0));
    
    dp[0][0] = 1;  // Initial empty product
    dp[0][1] = 0;  // Not valid state
    
    for (int i = 0; i < n - 1; ++i) {
        vector<vector<long long>> new_dp(maxA + 1, vector<long long>(2, 0));
        for (int j = 0; j <= maxA; ++j) {
            if (dp[j][0] > 0) {
                // Adding A[i] results
                new_dp[j + A[i]][0] = (new_dp[j + A[i]][0] + dp[j][0] * (j + A[i])) % mod;
                new_dp[0][1] = (new_dp[0][1] + dp[j][0]) % mod;  // accumulate good sequences without contributing to the score
            }
            if (dp[j][1] > 0) {
                new_dp[j + A[i]][1] = (new_dp[j + A[i]][1] + dp[j][1] * (j + A[i])) % mod;
                new_dp[0][1] = (new_dp[0][1] + dp[j][1]) % mod;
            }
        }
        dp.swap(new_dp);  // Move to the next iteration
    }
    
    long long answer = 0;
    for (int j = 0; j <= maxA; ++j) {
        answer = (answer + dp[j][1]) % mod;  // Only collect final results with gcd 1
    
    }
    
    cout << answer << endl;
    return 0;
}
