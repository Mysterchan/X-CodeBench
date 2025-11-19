#include<bits/stdc++.h>
using namespace std;
#define int long long

int N;
vector<int> A;
map<pair<int,int>, int> memo;

int solve(int l, int r) {
    if (l > r) return 0;
    if ((r - l + 1) % 2 == 1) return 0; // odd length, one element remains
    
    pair<int,int> key = {l, r};
    if (memo.count(key)) return memo[key];
    
    int res = 0;
    // Try pairing A[l] with A[l+1], A[l+3], A[l+5], ...
    for (int i = l + 1; i <= r; i += 2) {
        int score = abs(A[l] - A[i]);
        int left = solve(l + 1, i - 1);
        int right = solve(i + 1, r);
        res = max(res, score + left + right);
    }
    
    memo[key] = res;
    return res;
}

signed main() {
    cin >> N;
    A.resize(N);
    for (int i = 0; i < N; i++) cin >> A[i];
    
    cout << solve(0, N - 1) << endl;
    
    return 0;
}