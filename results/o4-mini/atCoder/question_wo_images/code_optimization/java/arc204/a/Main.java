#include <bits/stdc++.h>
using namespace std;
const int MOD = 998244353;
int add(int a, int b) { a += b; if (a >= MOD) a -= MOD; return a; }
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    int L, R;
    cin >> N >> L >> R;
    vector<int> A(N+1), B(N+1);
    for(int i = 1; i <= N; i++) cin >> A[i];
    for(int i = 1; i <= N; i++) cin >> B[i];
    vector<int> cumA(N+1,0), cumB(N+1,0);
    for(int i = 1; i <= N; i++){
        cumA[i] = cumA[i-1] + A[i];
        cumB[i] = cumB[i-1] + B[i];
    }
    int tot = cumB[N] - cumA[N];
    // dp rows: prev for ai-1, curr for ai
    vector<array<int,2>> prev(N+1), curr(N+1);
    // base dp[0][0]
    prev[0][0] = prev[0][1] = 0;
    if (tot > R) {
        // both zero
    } else if (tot >= L) {
        prev[0][1] = 1;
    } else {
        prev[0][0] = 1;
    }
    // DP
    for(int ai = 1; ai <= N; ai++){
        // clear curr for bi=0..ai
        for(int bi = 0; bi <= ai; bi++){
            curr[bi][0] = curr[bi][1] = 0;
        }
        for(int bi = 0; bi <= ai; bi++){
            // state (ai, bi)
            if (ai==0 && bi==0) continue;
            int sum = cumB[bi] - cumA[ai];
            int val = tot - sum;
            if (val > R) {
                // no transitions
            } else if (val >= L) {
                // good range: contribute to dp[*][1]
                if (ai > bi) {
                    // from prev[bi]
                    curr[bi][1] = add(curr[bi][1], prev[bi][0]);
                    curr[bi][1] = add(curr[bi][1], prev[bi][1]);
                }
                if (bi > 0) {
                    // from curr[bi-1]
                    curr[bi][1] = add(curr[bi][1], curr[bi-1][0]);
                    curr[bi][1] = add(curr[bi][1], curr[bi-1][1]);
                }
            } else {
                // val < L: contribute to dp[*][0]
                if (ai > bi) {
                    curr[bi][0] = add(curr[bi][0], prev[bi][0]);
                    curr[bi][0] = add(curr[bi][0], prev[bi][1]);
                }
                if (bi > 0) {
                    curr[bi][0] = add(curr[bi][0], curr[bi-1][0]);
                    curr[bi][0] = add(curr[bi][0], curr[bi-1][1]);
                }
            }
        }
        // swap prev and curr
        prev.swap(curr);
    }
    // result dp[N][N][1]
    cout << prev[N][1] << "\n";
    return 0;
}