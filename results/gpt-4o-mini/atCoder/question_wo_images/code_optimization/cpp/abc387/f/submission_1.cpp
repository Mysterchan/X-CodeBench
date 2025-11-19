#include <iostream>
#include <vector>
using namespace std;

const long long MOD = 998244353;

int main() {
    int N, M;
    cin >> N >> M;
    
    vector<int> A(N + 1);
    for (int i = 1; i <= N; i++) {
        cin >> A[i];
    }

    vector<int> dp(N + 1, 0);
    dp[0] = 1;

    for (int num = 1; num <= M; num++) {
        vector<int> new_dp(N + 1, 0);
        for (int i = 1; i <= N; i++) {
            new_dp[i] = dp[i];
            if (A[i] <= i) {
                new_dp[i] = (new_dp[i] + dp[A[i]]) % MOD;
            }
        }
        dp.swap(new_dp);
    }

    long long ans = 0;
    for (int i = 1; i <= N; i++) {
        ans = (ans + dp[i]) % MOD;
    }

    cout << ans << endl;
    return 0;
}