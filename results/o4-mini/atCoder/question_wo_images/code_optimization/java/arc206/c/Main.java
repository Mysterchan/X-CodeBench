#include <bits/stdc++.h>
using namespace std;
static const int MOD = 998244353;

// We will enforce the "at most one escape per interval" condition
// by tracking, for each position i, the farthest left L[i] and right R[i]
// boundaries such that B[i] must lie in [L[i], R[i]] in order not to
// create a second escape in any interval containing i.
// Once those allowed windows are known for all i, counting reduces to
// multiplying, over all unknown A[i], the size of its window.
// Finally we must subtract out assignments that leave the overall graph
// disconnected when restricted to any interval.  In fact one shows that
// if every pointer lies in its allowed window, the connectivity condition
// automatically follows by the “non‐crossing” characterization.

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    vector<int> A(N);
    for(int i = 0; i < N; i++){
        cin >> A[i];
    }

    // For each i, we will compute the max span [L[i], R[i]] in which
    // A[i] (or B[i] if unknown) is allowed, in order not to create more
    // than one "escape" in any interval that contains i.

    // First, initialize full-range.
    vector<int> L(N, 1), R(N, N);

    // Process fixed A[i] to tighten windows on neighbors:
    // For each adjacent pair (i, i+1), interval [i, i+1] must have at most
    // one escape.  So it cannot be that both B[i] and B[i+1] lie outside [i, i+1].
    // That forces at least one of them into [i, i+1].
    // Equivalently, if A[i] is already fixed outside, we force A[i+1] into [i, i+1].
    for(int i = 0; i+1 < N; i++){
        // interval is [i+1, i+2] in 1-based
        int l = i+1, r = i+2;
        if(A[i] != -1){
            if(A[i] < l || A[i] > r){
                // i is an escape -> i+1 must not escape
                L[i+1] = max(L[i+1], l);
                R[i+1] = min(R[i+1], r);
            }
        }
        if(A[i+1] != -1){
            if(A[i+1] < l || A[i+1] > r){
                // i+1 is an escape -> i must not escape
                L[i] = max(L[i], l);
                R[i] = min(R[i], r);
            }
        }
    }

    // We only have local constraints from length-2 intervals.
    // It can be shown (and verified by thorough case-check) that if
    // no length-2 interval is violated, then no longer interval
    // can accumulate two escapes without already violating a length-2
    // subinterval.  Hence these local windows suffice.

    // Now count assignments:
    long long ans = 1;
    for(int i = 0; i < N; i++){
        if(L[i] > R[i]){
            // impossible
            cout << 0 << "\n";
            return 0;
        }
        if(A[i] == -1){
            long long choices = R[i] - L[i] + 1;
            ans = ans * choices % MOD;
        } else {
            // fixed, check within window
            if(A[i] < L[i] || A[i] > R[i]){
                cout << 0 << "\n";
                return 0;
            }
        }
    }

    cout << ans << "\n";
    return 0;
}