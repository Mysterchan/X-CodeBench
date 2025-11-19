#include<bits/stdc++.h>
using namespace std;
long long lengthOfLIS(const vector<long long>& nums) {
    vector<long long> dp;
    for (long long num : nums) {
        auto it = lower_bound(dp.begin(), dp.end(), num);
        if (it == dp.end())dp.push_back(num);
        else *it = num;
    }return dp.size();
}signed main() {
    long long N, Q;
    cin >> N >> Q;
    vector<long long> A(N);
    for (long long i = 0; i < N; ++i)cin >> A[i];
    for (long long i = 0; i < Q; ++i) {
        long long R, X;
        cin >> R >> X;
        vector<long long> validNums;
        for (long long j = 0; j < R; ++j)if (A[j] <= X)validNums.push_back(A[j]);
        long long result = lengthOfLIS(validNums);
        cout << result << endl;
    }
}